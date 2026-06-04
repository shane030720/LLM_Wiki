from __future__ import annotations

import asyncio
import codecs
from typing import AsyncIterator

MODEL_FLAG = []  # add e.g. ["--model", "claude-opus-4-5"] to override

SYSTEM_PROMPT = """당신은 대학교 강의자료 기반 LLM Wiki 어시스턴트입니다.

역할:
- 제공된 강의자료 청크를 기반으로 학생 질문에 정확하고 친절하게 답변합니다.
- 모든 답변은 한국어로 작성합니다.
- 답변 말미에 반드시 출처(문서명·페이지)를 인용합니다.
- 자료에 없는 내용은 "제공된 자료에서 찾을 수 없습니다"라고 명시합니다.

답변 형식:
- 마크다운 사용 (제목, 굵게, 표, 코드블록 등)
- 핵심 개념은 굵게 표시
- 코드 예제는 ```언어 블록 안에 작성
- 마지막에 ## 출처 섹션 추가"""


def _build_context(chunks: list[dict]) -> str:
    if not chunks:
        return "관련 강의자료를 찾을 수 없습니다."
    parts = []
    for i, c in enumerate(chunks, 1):
        label = f"[{i}] {c['source']}" + (f" p.{c['page']}" if c["page"] else "")
        parts.append(f"{label}\n{c['text']}")
    return "\n\n---\n\n".join(parts)


def _source_list(chunks: list[dict]) -> list[dict]:
    seen: set[str] = set()
    sources = []
    for c in chunks:
        key = f"{c['source']}-{c['page']}"
        if key not in seen:
            seen.add(key)
            sources.append({"source": c["source"], "page": c["page"], "score": c["score"]})
    return sources


def _build_prompt(query: str, chunks: list[dict]) -> str:
    context = _build_context(chunks)
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"## 참고 강의자료\n\n{context}\n\n"
        f"## 질문\n\n{query}"
    )


async def stream_answer(query: str, chunks: list[dict]) -> AsyncIterator[str]:
    """claude -p 를 subprocess로 호출하고 stdout을 청크 단위로 스트리밍."""
    prompt = _build_prompt(query, chunks)

    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", prompt, *MODEL_FLAG,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )

    # 멀티바이트 문자(한국어 등)가 청크 경계에서 잘리지 않도록 incremental decoder 사용
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


async def generate_exam(
    subject: str,
    topic: str,
    difficulty: str,
    chunks: list[dict],
    count: int = 5,
) -> str:
    """시험 문제 생성 (non-streaming)."""
    context = _build_context(chunks)
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"## 참고 강의자료\n\n{context}\n\n"
        f"## 요청\n\n"
        f"과목: {subject}, 주제: {topic}, 난이도: {difficulty}, 문제 수: {count}\n"
        f"위 강의자료를 기반으로 예상 시험 문제를 생성해주세요. "
        f"각 문제에 정답, 해설, 출처(문서명·페이지)를 포함하세요."
    )

    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", prompt, *MODEL_FLAG,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )
    stdout, _ = await proc.communicate()
    return stdout.decode("utf-8", errors="replace")
