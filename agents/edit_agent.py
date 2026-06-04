#!/usr/bin/env python3
"""Edit Agent - 교육자료 정리 에이전트

사용법:
  python edit_agent.py <파일경로>   # 단일 파일 study notes 출력 (기존 모드)
  python edit_agent.py --ingest     # raw/ 미처리 PDF 자동 wiki 페이지 생성
  python edit_agent.py              # --ingest 와 동일

auto-ingest 모드는 Claude 세션 한도에 도달하면 reset 시간까지 자동 대기 후 재개한다.
"""

import subprocess
import sys
import re
import shutil
import time
from pathlib import Path
from datetime import datetime, timedelta

PROJECT_DIR = Path(__file__).parent.parent
WIKI_DIR = PROJECT_DIR / "wiki"
RAW_DIR = PROJECT_DIR / "raw"
PAGES_DIR = WIKI_DIR / "pages"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"
STATUS_FILE = WIKI_DIR / "ingest_status.json"

# nvm 등 비표준 경로에 설치된 경우를 위해 절대 경로로 고정
CLAUDE_BIN = shutil.which("claude") or "/home/shane/.nvm/versions/node/v24.14.0/bin/claude"


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

    result = subprocess.run(
        [CLAUDE_BIN, "--system-prompt", EDIT_SYSTEM_PROMPT, "-p", prompt],
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0:
        return f"오류: {result.stderr.strip()}"
    return result.stdout.strip()


# ── 신규: wiki auto-ingest 모드 ──────────────────────────────────────

class SessionLimitError(Exception):
    def __init__(self, wait_seconds: int, reset_str: str):
        self.wait_seconds = wait_seconds
        self.reset_str = reset_str


def _parse_session_limit(text: str) -> SessionLimitError | None:
    """출력에서 세션 한도 메시지를 감지하고 대기 시간을 계산한다.

    예: "You've hit your session limit · resets 12:50am (Asia/Seoul)"
    """
    m = re.search(r"resets (\d+):(\d+)(am|pm)\s*\(([^)]+)\)", text, re.IGNORECASE)
    if not m or "session limit" not in text.lower():
        return None

    hour, minute, ampm, tz_name = int(m.group(1)), int(m.group(2)), m.group(3).lower(), m.group(4)

    if ampm == "pm" and hour != 12:
        hour += 12
    elif ampm == "am" and hour == 12:
        hour = 0

    try:
        from zoneinfo import ZoneInfo
        tz = ZoneInfo(tz_name)
        now = datetime.now(tz)
        reset = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if reset <= now:
            reset += timedelta(days=1)
        wait = int((reset - now).total_seconds()) + 90  # 1분 30초 버퍼
    except Exception:
        wait = 3600  # fallback: 1시간

    reset_str = f"{m.group(1)}:{m.group(2)}{ampm} ({tz_name})"
    return SessionLimitError(wait, reset_str)


def _get_existing_slugs() -> set[str]:
    return {p.stem for p in PAGES_DIR.rglob("*.md")} if PAGES_DIR.exists() else set()


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

    return f"""너는 LLM Wiki 페이지 생성 에이전트야. 교육자료 PDF를 분석해서 CLAUDE.md 스키마에 맞는 wiki 페이지를 생성한다.

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
        "status": result,          # "done" | "skipped" | "failed"
        "date": datetime.now().strftime("%Y-%m-%d"),
        "pages": pages,
        **({"reason": reason} if reason else {}),
    }
    _save_status(status)


def get_processed_sources() -> set[str]:
    """wiki 페이지의 sources 필드에 등록된 raw 파일 경로 집합을 반환한다."""
    processed: set[str] = set()
    if not PAGES_DIR.exists():
        return processed
    for page in PAGES_DIR.rglob("*.md"):
        content = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"sources:\s*\[([^\]]*)\]", content, re.DOTALL)
        if m:
            for src in m.group(1).split(","):
                src = src.strip().strip("\"'")
                if src:
                    processed.add(src)
    return processed


# ingest에서 제외할 raw/ 하위 폴더 이름 목록
EXCLUDED_DIRS: set[str] = set()


def find_unprocessed_pdfs() -> list[Path]:
    """raw/ 하위 PDF 중 미처리 파일 목록을 반환한다.

    다음 중 하나라도 해당하면 처리된 것으로 간주한다:
    - wiki 페이지의 sources: 필드에 등록됨
    - ingest_status.json에 done/skipped으로 기록됨
    - EXCLUDED_DIRS에 속한 폴더
    """
    processed = get_processed_sources()
    status = _load_status()
    skipped_or_done = {k for k, v in status.items() if v.get("status") in ("done", "skipped")}

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


def _call_claude(pdf_path: Path) -> str:
    """PDF를 Claude로 분석해 wiki 페이지 출력을 반환한다.

    세션 한도에 도달하면 SessionLimitError를 raise한다.
    """
    content = read_file(pdf_path)
    if not content.strip():
        return ""

    rel = str(pdf_path.relative_to(PROJECT_DIR))
    prompt = (
        f"다음 교육자료를 분석해서 wiki 페이지를 생성해줘.\n"
        f"파일 경로(sources 필드에 이 값을 그대로 사용): {rel}\n\n{content}"
    )

    result = subprocess.run(
        [
            CLAUDE_BIN,
            "--system-prompt", _ingest_system_prompt(_get_existing_slugs()),
            "--disallowedTools", "Write,Edit,Bash,TodoWrite,TodoRead",
            "-p",
        ],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600,
    )

    combined = result.stdout + result.stderr

    # 세션 한도 감지 → 호출자가 대기 후 재시도하도록 예외 raise
    limit_err = _parse_session_limit(combined)
    if limit_err:
        raise limit_err

    if result.stdout.strip():
        if result.returncode != 0 and result.stderr.strip():
            print(f"  경고 (exit={result.returncode}): {result.stderr.strip()[:120]}", file=sys.stderr)
        return result.stdout.strip()

    if result.returncode != 0:
        print(f"  오류: {result.stderr.strip()}", file=sys.stderr)
    return ""


def _parse_output(text: str) -> tuple[list[tuple[Path, str]], list[str]]:
    """Claude 출력에서 (경로, 내용) 페이지 목록과 index 행 목록을 파싱한다."""
    pages: list[tuple[Path, str]] = []
    for m in re.finditer(r"<<<PAGE:(.*?)>>>\s*(.*?)\s*<<<END_PAGE>>>", text, re.DOTALL):
        path = PROJECT_DIR / m.group(1).strip()
        pages.append((path, m.group(2).strip()))

    index_rows: list[str] = []
    for m in re.finditer(r"<<<INDEX_ROW>>>\s*(.*?)\s*<<<END_INDEX_ROW>>>", text, re.DOTALL):
        index_rows.append(m.group(1).strip())

    return pages, index_rows


def _write_pages(pages: list[tuple[Path, str]]) -> list[str]:
    slugs = []
    for path, content in pages:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content + "\n", encoding="utf-8")
        slugs.append(path.stem)
        print(f"  ✓ {path.relative_to(PROJECT_DIR)}", file=sys.stderr)
    return slugs


def rebuild_index() -> None:
    """wiki/pages/ 하위 모든 .md 파일을 스캔해 index.md를 전체 재생성한다."""
    seen: set[str] = set()
    rows: dict[str, list] = {"concept": [], "entity": [], "synthesis": []}

    for md in sorted(PAGES_DIR.rglob("*.md")):
        if md.stem == "_about" or md.stem in seen:
            continue
        seen.add(md.stem)

        content = md.read_text(encoding="utf-8", errors="replace")
        title   = re.search(r"^title:\s*(.+)",       content, re.M)
        cat     = re.search(r"^category:\s*(.+)",    content, re.M)
        tags    = re.search(r"^tags:\s*\[(.+)\]",    content, re.M)
        updated = re.search(r"^updated:\s*(.+)",     content, re.M)

        title   = title.group(1).strip()   if title   else md.stem
        cat     = cat.group(1).strip()     if cat     else md.parent.name
        tags    = tags.group(1).strip()    if tags    else ""
        updated = updated.group(1).strip() if updated else datetime.now().strftime("%Y-%m-%d")

        sm = re.search(r"## (?:Definition|Overview|Thesis)\n+(.+)", content)
        summary = sm.group(1).strip() if sm else ""
        summary = re.sub(r"\[\[.*?\]\]", "", summary)
        summary = summary[:70] + ("..." if len(summary) > 70 else "")

        bucket = cat if cat in rows else "concept"
        rows[bucket].append((title, md.stem, tags, updated, summary))

    for bucket in rows:
        rows[bucket].sort(key=lambda x: x[0].lower())

    def _fmt(bucket: str) -> str:
        return "\n".join(
            f"| [[{slug}]] | {bucket} | {tags} | {updated} | {summary} |"
            for _, slug, tags, updated, summary in rows[bucket]
        )

    total = sum(len(v) for v in rows.values())
    today = datetime.now().strftime("%Y-%m-%d")

    INDEX_FILE.write_text(
        f"""# Wiki Index

Master catalog of all wiki pages. Updated automatically at every Ingest and Lint operation.

> **LLM instruction:** Keep this table sorted by Category (concept → entity → synthesis), then alphabetically by Page within each category. Never delete rows — use ~~strikethrough~~ for deprecated pages.

---

## Content Catalog

| Page | Category | Tags | Updated | Summary |
|------|----------|------|---------|---------|
{_fmt("concept")}
{_fmt("entity")}
{_fmt("synthesis")}

---

## Statistics

- **Total pages:** {total}
- **Concepts:** {len(rows["concept"])}
- **Entities:** {len(rows["entity"])}
- **Syntheses:** {len(rows["synthesis"])}
- **Open contradictions:** 0
- **Last updated:** {today}
""",
        encoding="utf-8",
    )
    print(f"index.md 재생성 완료: {total}개 페이지 (concept {len(rows['concept'])}, entity {len(rows['entity'])}, synthesis {len(rows['synthesis'])})", file=sys.stderr)


def _update_index(new_rows: list[str]) -> None:
    if not new_rows or not INDEX_FILE.exists():
        return
    content = INDEX_FILE.read_text(encoding="utf-8")
    insertion = "\n".join(new_rows)
    updated = content.replace(
        "\n\n---\n\n## Statistics",
        f"\n{insertion}\n\n---\n\n## Statistics",
    )
    if updated == content:
        updated = content.rstrip() + "\n" + insertion + "\n"
    INDEX_FILE.write_text(updated, encoding="utf-8")


def _append_log(sources: list[str], slugs: list[str]) -> None:
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
    """미처리 PDF를 모두 처리할 때까지 실행한다.

    Claude 세션 한도에 도달하면 reset 시간까지 자동 대기 후 재개한다.
    """
    all_sources: list[str] = []
    all_slugs: list[str] = []

    while True:
        unprocessed = find_unprocessed_pdfs()
        if not unprocessed:
            break

        print(f"미처리 PDF {len(unprocessed)}개 발견:", file=sys.stderr)
        for p in unprocessed:
            print(f"  - {p.relative_to(PROJECT_DIR)}", file=sys.stderr)
        print(file=sys.stderr)

        session_limited = False

        for pdf in unprocessed:
            rel = str(pdf.relative_to(PROJECT_DIR))
            print(f"처리 중: {rel}", file=sys.stderr)

            try:
                output = _call_claude(pdf)
            except SessionLimitError as e:
                mins = e.wait_seconds // 60
                print(
                    f"\n  [세션 한도] resets {e.reset_str} — {mins}분 후 자동 재개합니다.",
                    file=sys.stderr,
                )
                time.sleep(e.wait_seconds)
                session_limited = True
                break

            if not output:
                print("  건너뜀 (출력 없음)", file=sys.stderr)
                _mark_status(rel, "skipped", [], reason="no extractable text")
                continue

            pages, index_rows = _parse_output(output)
            if not pages:
                print(
                    f"  경고: 페이지 파싱 실패. 원본 출력 앞부분:\n{output[:500]}",
                    file=sys.stderr,
                )
                _mark_status(rel, "failed", [], reason="parse error")
                continue

            slugs = _write_pages(pages)
            _update_index(index_rows)
            _mark_status(rel, "done", slugs)
            all_sources.append(rel)
            all_slugs.extend(slugs)
            print(file=sys.stderr)

        if not session_limited:
            break  # for 루프가 break 없이 완료 = 전체 처리 완료

    if all_slugs:
        _append_log(all_sources, all_slugs)
        print(f"완료: {len(all_slugs)}개 페이지 생성, log.md 업데이트됨", file=sys.stderr)
    else:
        print("미처리 PDF 없음. 모두 처리되었습니다.", file=sys.stderr)

    rebuild_index()


# ── 진입점 ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--ingest":
        auto_ingest()
    elif sys.argv[1] == "--rebuild-index":
        rebuild_index()
    else:
        print(run(sys.argv[1]))
