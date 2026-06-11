#!/usr/bin/env python3
"""Edit Agent - 교육자료 정리 에이전트

사용법:
  python edit_agent.py <파일경로>   # 단일 파일 study notes 출력 (기존 모드)
  python edit_agent.py --ingest     # raw/ 미처리 PDF 자동 wiki 페이지 생성
  python edit_agent.py              # --ingest 와 동일

wiki 페이지 접근은 tools/wiki_client.py (MCP 인터페이스)를 경유한다.
파일시스템 직접 접근 없음 (raw/ PDF 읽기 및 운영 파일 제외).

auto-ingest 모드는 Claude 세션 한도에 도달하면 reset 시간까지 자동 대기 후 재개한다.
"""

import subprocess
import sys
import re
import shutil
from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).parent.parent
WIKI_DIR = PROJECT_DIR / "wiki"
RAW_DIR = PROJECT_DIR / "raw"
LOG_FILE = WIKI_DIR / "log.md"
STATUS_FILE = WIKI_DIR / "ingest_status.json"

sys.path.insert(0, str(PROJECT_DIR))
from llm_provider import run as llm_run, stream as llm_stream
from tools.wiki_client import (
    get_existing_slugs,
    get_processed_sources,
    create_page,
    rebuild_index,
)


# ── 기존: study notes 모드 ────────────────────────────────────────────

EDIT_SYSTEM_PROMPT = """너는 교육자료 정리 에이전트야.

읽기 규칙:
- 손글씨 필기는 전부 무시
- 단, 별표(★, ☆, *) 표시가 있는 페이지나 내용은 중요도 높음으로 판단
- "시험 안나옴", "시험 X", "안나옴" 같은 표시가 있는 내용은 제외

정리 규칙:
- 교육자료 원본 내용만 기반으로 정리
- 핵심 단어(전문 용어, 개념명)는 영어 원문 유지
- 나머지 설명은 전부 한국어로 작성
- 별표 표시된 내용은 더 상세하고 정밀하게 정리
- 별표 없는 내용은 핵심만 간략하게 정리
- 출처 페이지 번호 명시
- 이모지 사용 금지 (특수문자, 그림 문자 일체 사용하지 말 것)

출력 형식:
## [페이지 제목]
[중요] (별표 있으면 이 태그 표시, 없으면 생략)
- 핵심 개념 설명 (한국어)
- 예시 및 부연 설명"""


def read_file(path: Path) -> str:
    """raw/ 파일 읽기 — PDF 또는 텍스트."""
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(path))
            pages = []
            for i, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                if text.strip():
                    pages.append(f"[p.{i}]\n{text}")
            return "\n\n".join(pages)
        except ImportError:
            sys.exit("오류: PDF 읽기에 pypdf 필요. pip install pypdf")
    return path.read_text(encoding="utf-8", errors="replace")


def run(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        return f"오류: 파일을 찾을 수 없습니다: {file_path}"

    content = read_file(path)
    if not content.strip():
        return "오류: 파일 내용이 비어 있습니다."

    prompt = f"다음 교육자료를 정리해줘.\n파일명: {path.name}\n\n{content}"

    return llm_run(prompt, system=EDIT_SYSTEM_PROMPT)


# ── 신규: wiki auto-ingest 모드 ──────────────────────────────────────

def _ingest_system_prompt(existing_slugs: set[str] | None = None) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    if existing_slugs:
        slug_list = ", ".join(sorted(existing_slugs))
        existing_note = f"""
## 이미 존재하는 wiki 페이지 슬러그 (중복 생성 금지)
{slug_list}

위 슬러그에 해당하는 개념이 PDF에 복습/리뷰 형태로 등장해도 새 페이지를 만들지 말 것.
완전히 새로운 개념이나 기존 페이지에 없는 내용만 페이지로 생성한다."""
    else:
        existing_note = ""

    return f"""너는 LLM Wiki 페이지 생성 에이전트야. 교육자료 PDF를 분석해서 LLM.md 스키마에 맞는 wiki 페이지를 생성한다.

오늘 날짜: {today}{existing_note}

## 페이지 유형 (category)
- concept  : 개념·이론 정의 (what a thing IS) → wiki/pages/concepts/
- entity   : 도구·시스템·알고리즘·사람 (who/what EXISTS) → wiki/pages/entities/
- synthesis: 비교·분석·오픈 퀘스천 (cross-source analysis) → wiki/pages/syntheses/

## 필수 Frontmatter
---
title: <Human-readable title>
category: concept | entity | synthesis
tags: [tag1, tag2]
sources: [raw/<파일 상대경로>]
created: {today}
updated: {today}
---

## Concept 페이지 필수 섹션 (이 순서로)
## Definition
## How It Works
## Key Properties
## Relationships
## Open Questions
## Sources

## Entity 페이지 필수 섹션
## Overview
## Capabilities
## Limitations
## Relationships
## Sources

## Synthesis 페이지 필수 섹션
## Thesis
## Evidence
## Counterevidence
## Conclusion
## Sources

## 작성 규칙
- 핵심 전문 용어는 영어 원문 유지, 설명은 한국어
- 파일명: kebab-case.md (영문 소문자, 하이픈)
- Cross-reference: [[slug]] 형식 (slug = 파일명에서 .md 제외)
- 이모지 사용 금지

## 출력 형식 (반드시 정확히 사용할 것)

wiki 페이지:
<<<PAGE:wiki/pages/{{category}}/{{slug}}.md>>>
[frontmatter + 섹션 내용 전체]
<<<END_PAGE>>>

index.md 추가 행:
<<<INDEX_ROW>>>
| [[{{slug}}]] | {{category}} | tag1, tag2 | {today} | 한 줄 요약 (한국어) |
<<<END_INDEX_ROW>>>

한 PDF에서 주제별로 여러 페이지를 생성할 수 있다.

## 절대 금지
- Write, Edit, Bash 등 파일 쓰기/실행 도구 사용 금지
- 위 구분자 형식을 벗어난 응답 금지
- 파일 쓰기 권한을 요청하거나 도구를 사용하려 하지 말 것
- 반드시 텍스트로만 응답할 것"""


def _load_status() -> dict:
    if STATUS_FILE.exists():
        import json
        return json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    return {}


def _save_status(status: dict) -> None:
    import json
    STATUS_FILE.write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _mark_status(rel: str, result: str, pages: list[str], reason: str = "") -> None:
    """ingest_status.json에 파일 처리 결과를 기록한다."""
    status = _load_status()
    status[rel] = {
        "status": result,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "pages": pages,
        **({"reason": reason} if reason else {}),
    }
    _save_status(status)


# ingest에서 제외할 raw/ 하위 폴더 이름 목록
EXCLUDED_DIRS: set[str] = set()


def find_unprocessed_pdfs() -> list[Path]:
    """raw/ 하위 PDF 중 미처리 파일 목록을 반환한다.

    wiki 페이지 정보는 MCP 인터페이스(get_processed_sources)를 통해 조회한다.
    """
    processed = get_processed_sources()       # MCP 경유
    status = _load_status()
    skipped_or_done = {k for k, v in status.items() if v.get("status") in ("done", "skipped")}
    # "failed"는 재처리 대상 (LLM 오류이므로 다음 실행 시 다시 시도)

    result = []
    for pdf in sorted(RAW_DIR.rglob("*.pdf")):
        if ":Zone.Identifier" in str(pdf):
            continue
        try:
            parts = pdf.relative_to(RAW_DIR).parts
            if parts[0] in EXCLUDED_DIRS:
                continue
        except ValueError:
            pass
        rel = str(pdf.relative_to(PROJECT_DIR))
        if rel not in processed and rel not in skipped_or_done:
            result.append(pdf)
    return result


def _call_claude(pdf_path: Path) -> str | None:
    """PDF를 Claude로 분석해 wiki 페이지 출력을 반환한다.

    Returns:
        str  — LLM 출력 (빈 문자열이면 텍스트 없는 PDF)
        None — LLM 호출 자체가 실패 (재처리 필요)
    """
    content = read_file(pdf_path)
    if not content.strip():
        return ""

    rel = str(pdf_path.relative_to(PROJECT_DIR))
    prompt = (
        f"다음 교육자료를 분석해서 wiki 페이지를 생성해줘.\n"
        f"파일 경로(sources 필드에 이 값을 그대로 사용): {rel}\n\n{content}"
    )

    existing = get_existing_slugs()
    return llm_run(prompt, system=_ingest_system_prompt(existing))


def _parse_output(text: str) -> tuple[list[tuple[str, str, str]], list[str]]:
    """Claude 출력에서 (category, slug, content) 페이지 목록과 index 행 목록을 파싱한다."""
    pages: list[tuple[str, str, str]] = []
    for m in re.finditer(r"<<<PAGE:(.*?)>>>\s*(.*?)\s*<<<END_PAGE>>>", text, re.DOTALL):
        rel_path = m.group(1).strip()          # e.g. "wiki/pages/concepts/binary-search.md"
        content = m.group(2).strip()
        parts = Path(rel_path).parts           # ("wiki", "pages", "concepts", "binary-search.md")
        if len(parts) >= 4:
            cat_dir = parts[2]                 # "concepts"
            slug = Path(parts[3]).stem         # "binary-search"
            _CAT_DIR_MAP = {"concepts": "concept", "entities": "entity", "syntheses": "synthesis"}
            category = _CAT_DIR_MAP.get(cat_dir, "concept")
        else:
            category = "concept"
            slug = Path(rel_path).stem
        pages.append((category, slug, content))

    index_rows: list[str] = []
    for m in re.finditer(r"<<<INDEX_ROW>>>\s*(.*?)\s*<<<END_INDEX_ROW>>>", text, re.DOTALL):
        index_rows.append(m.group(1).strip())

    return pages, index_rows


def _write_pages(pages: list[tuple[str, str, str]]) -> list[str]:
    """MCP create_page를 통해 wiki 페이지를 저장한다."""
    slugs = []
    for category, slug, content in pages:
        # frontmatter의 title 추출 (없으면 slug 사용)
        m = re.search(r"^title:\s*(.+)", content, re.M)
        title = m.group(1).strip() if m else slug

        result = create_page(title=title, content=content, category=category, slug=slug)
        if result.startswith("[완료]"):
            slugs.append(slug)
            print(f"  ✓ {result.replace('[완료] ', '')}", file=sys.stderr)
        else:
            print(f"  ! {result}", file=sys.stderr)
    return slugs


def _append_log(sources: list[str], slugs: list[str]) -> None:
    """wiki/log.md에 ingest 작업 상세 기록을 추가한다 (운영 파일 직접 기록)."""
    today = datetime.now().strftime("%Y-%m-%d")
    names = [Path(s).name for s in sources]
    desc = ", ".join(names[:3]) + ("..." if len(names) > 3 else "")
    sources_str = "\n".join(f"  - {s}" for s in sources)
    pages_str = ", ".join(f"[[{s}]]" for s in slugs) or "없음"

    entry = (
        f"\n## [{today}] ingest | {desc}\n\n"
        f"- **Source(s):**\n{sources_str}\n"
        f"- **Pages created:** {pages_str}\n"
        f"- **Pages updated:** 없음\n"
        f"- **Contradictions flagged:** 없음\n"
        f"- **Notes:** edit_agent.py --ingest 자동 처리\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def auto_ingest() -> None:
    """미처리 PDF를 모두 처리할 때까지 실행한다."""
    all_sources: list[str] = []
    all_slugs: list[str] = []

    unprocessed = find_unprocessed_pdfs()
    if not unprocessed:
        print("미처리 PDF 없음. 모두 처리되었습니다.", file=sys.stderr)
        return

    print(f"미처리 PDF {len(unprocessed)}개 발견:", file=sys.stderr)
    for p in unprocessed:
        print(f"  - {p.relative_to(PROJECT_DIR)}", file=sys.stderr)
    print(file=sys.stderr)

    for pdf in unprocessed:
        rel = str(pdf.relative_to(PROJECT_DIR))
        print(f"처리 중: {rel}", file=sys.stderr)

        try:
            output = _call_claude(pdf)
        except Exception as e:
            print(f"  LLM 오류 (재처리 가능): {e}", file=sys.stderr)
            _mark_status(rel, "failed", [], reason=str(e))
            continue

        if output == "":
            print("  건너뜀 (텍스트 없는 PDF)", file=sys.stderr)
            _mark_status(rel, "skipped", [], reason="no extractable text")
            continue

        pages, _ = _parse_output(output)
        if not pages:
            print(
                f"  경고: 페이지 파싱 실패. 원본 출력 앞부분:\n{output[:500]}",
                file=sys.stderr,
            )
            _mark_status(rel, "failed", [], reason="parse error")
            continue

        slugs = _write_pages(pages)
        _mark_status(rel, "done", slugs)
        all_sources.append(rel)
        all_slugs.extend(slugs)
        print(file=sys.stderr)

    if all_slugs:
        _append_log(all_sources, all_slugs)
        print(f"완료: {len(all_slugs)}개 페이지 생성, log.md 업데이트됨", file=sys.stderr)

    # MCP를 통해 index.md 전체 재생성 (정합성 보장)
    result = rebuild_index()
    print(result, file=sys.stderr)


# ── 진입점 ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--ingest":
        auto_ingest()
    elif sys.argv[1] == "--rebuild-index":
        print(rebuild_index())
    else:
        path = Path(sys.argv[1])
        content = read_file(path)
        if content.strip():
            prompt = f"다음 교육자료를 정리해줘.\n파일명: {path.name}\n\n{content}"
            for chunk in llm_stream(prompt, system=EDIT_SYSTEM_PROMPT):
                print(chunk, end="", flush=True)
