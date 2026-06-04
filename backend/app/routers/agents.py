"""
에이전트 API 엔드포인트
POST /api/agents/edit          — Edit Agent (파일 정리, 스트리밍)
POST /api/agents/wiki          — Wiki Agent (질문 답변, 스트리밍)
POST /api/agents/quiz/generate — Quiz Agent 문제 출제
POST /api/agents/quiz/grade    — Quiz Agent 채점
"""
from __future__ import annotations

import asyncio
import codecs
import logging
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))
from llm_provider import astream as llm_astream, web_search as llm_web_search

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent.parent.parent
AGENTS_DIR = ROOT / "agents"
RAW_DIR = ROOT / "raw"
WIKI_PAGES_DIR = ROOT / "wiki" / "pages"

router = APIRouter()

# 웹 UI용 wiki 시스템 프롬프트
_WIKI_SYSTEM_PROMPT = """당신은 대학교 강의자료 기반 LLM Wiki 어시스턴트입니다.

역할:
- 제공된 강의 노트와 wiki 페이지 내용을 기반으로 학생 질문에 정확하고 친절하게 답변합니다.
- 모든 답변은 한국어로 작성합니다. 핵심 용어는 영어 유지.
- 답변 말미에 반드시 출처(강의 노트 또는 wiki 페이지명)를 인용합니다.

역할 경계:
- 문제 출제, 채점, 오답 노트 작성은 당신의 역할이 아닙니다.
- 퀴즈나 시험 문제를 요청받으면 "퀴즈는 📝 퀴즈 탭에서 이용해 주세요."라고 안내하고 답변하지 마세요.

답변 형식 (다크 테마 UI에 표시되므로 반드시 지켜야 함):
- 마크다운 사용 (제목, 굵게, 표, 코드블록 등)
- 핵심 개념은 굵게 표시
- 출처·교육자료 이름은 반드시 **굵게** 표시
- 블록인용(>) 문법 절대 사용 금지 — 어두운 회색으로 표시되어 읽을 수 없음
- 색상 지정 HTML 태그 사용 금지
- 마지막에 **출처** 섹션 추가"""

_STOPWORDS = {
    "이란", "무엇", "인가", "하는", "이고", "이다", "이며", "이면",
    "에서", "에서는", "으로", "하고", "하며", "하면", "하여", "해서",
    "은", "는", "이", "가", "을", "를", "과", "와", "의", "로",
    "에", "까지", "부터", "도", "만", "이나",
}


def _find_wiki_pages(question: str, max_pages: int = 5) -> list[Path]:
    """질문 키워드로 관련 wiki 페이지를 찾는다. 파일명·태그·제목에 가중치를 부여한다."""
    if not WIKI_PAGES_DIR.exists():
        return []

    all_kw = re.findall(r"\w+", question.lower())
    keywords = {kw for kw in all_kw if len(kw) >= 2 and kw not in _STOPWORDS}
    if not keywords:
        return []

    scored: list[tuple[int, Path]] = []
    for page in WIKI_PAGES_DIR.rglob("*.md"):
        raw = page.read_text(encoding="utf-8", errors="replace")
        lower = raw.lower()

        stem_score = sum(3 for kw in keywords if kw in page.stem.lower())

        tag_m = re.search(r"tags:\s*\[(.*?)\]", lower, re.DOTALL)
        tag_score = sum(2 for kw in keywords if tag_m and kw in tag_m.group(1))

        title_m = re.search(r"title:\s*(.+)", lower)
        title_score = sum(2 for kw in keywords if title_m and kw in title_m.group(1))

        body_score = sum(1 for kw in keywords if kw in lower)

        total = stem_score + tag_score + title_score + body_score
        if total > 0:
            scored.append((total, page))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored[:max_pages]]


class EditRequest(BaseModel):
    source: str
    subject: str


class WikiRequest(BaseModel):
    question: str
    notes: Optional[str] = None   # Edit Agent가 정리한 현재 화면의 강의 노트
    subject: Optional[str] = None  # 현재 선택된 과목


class QuizGenerateRequest(BaseModel):
    notes: str
    count: int = 5


class QuizGradeRequest(BaseModel):
    notes: str
    question: str
    answer: str


async def _stream_proc(cmd: list[str]):
    """edit_agent.py 등 subprocess 스트리밍 (LiteLLM stream → stdout → 여기서 읽음)."""
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )
    decoder = codecs.getincrementaldecoder("utf-8")("replace")
    while True:
        chunk = await proc.stdout.read(256)
        if not chunk:
            tail = decoder.decode(b"", final=True)
            if tail:
                yield tail
            break
        text = decoder.decode(chunk)
        if text:
            yield text
    await proc.wait()


@router.post("/agents/edit")
async def edit_file(req: EditRequest):
    file_path = RAW_DIR / req.subject / req.source
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"파일 없음: {file_path}")
    return StreamingResponse(
        _stream_proc([sys.executable, str(AGENTS_DIR / "edit_agent.py"), str(file_path)]),
        media_type="text/plain; charset=utf-8",
    )


@router.post("/agents/wiki")
async def wiki_query(req: WikiRequest):
    """강의 노트(notes) + wiki 페이지를 컨텍스트로 claude에 직접 스트리밍."""
    context_parts: list[str] = []
    has_notes = bool(req.notes and req.notes.strip())

    # 1순위: 현재 화면에 표시 중인 강의 노트
    if has_notes:
        label = f"({req.subject})" if req.subject else ""
        context_parts.append(
            f"## 현재 열람 중인 강의 노트 {label}\n\n{req.notes.strip()}"
        )

    # 2순위: wiki 페이지 키워드 검색
    wiki_pages = _find_wiki_pages(req.question)
    if wiki_pages:
        pages_text = "\n\n---\n\n".join(
            f"### {p.stem}\n\n{p.read_text(encoding='utf-8', errors='replace')}"
            for p in wiki_pages
        )
        context_parts.append(f"## 관련 Wiki 페이지\n\n{pages_text}")

    # 로그: 어떤 컨텍스트로 답변하는지 기록 (이상 답변 시 진단용)
    logger.info(
        "wiki_query | q=%r | notes=%s | wiki_pages=%s | fallback_web=%s",
        req.question[:80],
        f"yes({req.subject})" if has_notes else "no",
        [p.stem for p in wiki_pages] if wiki_pages else "none",
        not context_parts,
    )

    if context_parts:
        context = "\n\n".join(context_parts)
        prompt = f"{context}\n\n## 질문\n\n{req.question}"
    else:
        # 3순위: 웹 검색 (모든 LLM에서 동작하는 DuckDuckGo 사용)
        search_results = llm_web_search(req.question)
        prompt = (
            f"## 질문\n\n{req.question}\n\n"
            f"## 웹 검색 결과\n\n{search_results}"
        )

    return StreamingResponse(
        llm_astream(prompt, system=_WIKI_SYSTEM_PROMPT),
        media_type="text/plain; charset=utf-8",
    )


@router.post("/agents/quiz/generate")
async def quiz_generate(req: QuizGenerateRequest):
    if not req.notes.strip():
        raise HTTPException(status_code=400, detail="notes가 비어 있습니다. 먼저 파일을 선택하세요.")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(req.notes)
        tmp = f.name
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, str(AGENTS_DIR / "quiz_agent.py"),
            "generate", tmp, "--count", str(req.count),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
            env=_AGENT_ENV,
        )
        stdout, _ = await proc.communicate()
        return {"result": stdout.decode("utf-8", errors="replace").strip()}
    finally:
        os.unlink(tmp)


@router.post("/agents/quiz/grade")
async def quiz_grade(req: QuizGradeRequest):
    if not req.notes.strip():
        raise HTTPException(status_code=400, detail="notes가 비어 있습니다.")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(req.notes)
        tmp = f.name
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, str(AGENTS_DIR / "quiz_agent.py"),
            "grade", tmp, "--question", req.question, "--answer", req.answer,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
            env=_AGENT_ENV,
        )
        stdout, _ = await proc.communicate()
        return {"result": stdout.decode("utf-8", errors="replace").strip()}
    finally:
        os.unlink(tmp)
