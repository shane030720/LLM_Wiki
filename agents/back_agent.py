#!/usr/bin/env python3
"""Back Agent - LLM Wiki 유지보수 에이전트

사용법: python back_agent.py
"""

import json
import subprocess
import sys
import re
import shutil
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
WIKI_DIR = PROJECT_DIR / "wiki"
RAW_DIR = PROJECT_DIR / "raw"
PAGES_DIR = WIKI_DIR / "pages"
LOG_FILE = WIKI_DIR / "log.md"
STATUS_FILE = WIKI_DIR / "ingest_status.json"

EDIT_AGENT = Path(__file__).parent / "edit_agent.py"

sys.path.insert(0, str(PROJECT_DIR))
from llm_provider import run as llm_run

SYSTEM_PROMPT = """너는 LLM Wiki 유지보수 에이전트야.

보고 규칙:
- 체크 결과를 한국어로 보고서 형식으로 작성
- 업데이트가 필요한 항목은 구체적으로 명시
- 자동으로 수정하지 말고 보고서만 작성
- 정상이면 "이상 없음"으로 기록

보고서 출력 형식:
## [YYYY-MM-DD] back-check | 유지보수 점검

- **raw/ 신규 파일:** 없음 | <파일명>
- **오래된 wiki 페이지:** 없음 | [[slug]] (raw 파일 대비 N일 지연)
- **깨진 링크:** 없음 | [[slug]]에서 [[broken-slug]] 참조 오류
- **종합:** 이상 없음 | 업데이트 필요 항목 N건"""


def fmt_date(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def get_wiki_pages() -> list[Path]:
    return sorted(PAGES_DIR.rglob("*.md")) if PAGES_DIR.exists() else []


def get_all_slugs() -> set[str]:
    return {p.stem for p in get_wiki_pages()}


# ── ingest_status.json 기반 빠른 상태 확인 ────────────────────────────

def load_ingest_status() -> dict:
    if STATUS_FILE.exists():
        return json.loads(STATUS_FILE.read_text(encoding="utf-8"))
    return {}


def find_new_raw_pdfs(ingest_status: dict) -> list[Path]:
    """ingest_status에 없는 미처리 PDF 목록."""
    result = []
    for pdf in sorted(RAW_DIR.rglob("*.pdf")):
        if ":Zone.Identifier" in str(pdf):
            continue
        rel = str(pdf.relative_to(PROJECT_DIR))
        if rel not in ingest_status:
            result.append(pdf)
    return result


def find_stale_pdfs(ingest_status: dict) -> list[tuple[str, str]]:
    """raw 파일이 마지막 ingest 이후에 수정된 항목 (rel, date) 목록."""
    stale = []
    for rel, info in ingest_status.items():
        if info.get("status") != "done":
            continue
        raw_path = PROJECT_DIR / rel
        if not raw_path.exists():
            continue
        raw_mtime = datetime.fromtimestamp(raw_path.stat().st_mtime).strftime("%Y-%m-%d")
        if raw_mtime > info.get("date", ""):
            stale.append((rel, raw_mtime))
    return stale


def print_ingest_summary() -> tuple[list[Path], list[tuple[str, str]]]:
    """ingest_status.json을 읽어 현황을 출력하고, 조치 필요 항목을 반환한다."""
    status = load_ingest_status()
    new_pdfs = find_new_raw_pdfs(status)
    stale = find_stale_pdfs(status)

    done = sum(1 for v in status.values() if v.get("status") == "done")
    skipped = sum(1 for v in status.values() if v.get("status") == "skipped")
    failed = sum(1 for v in status.values() if v.get("status") == "failed")

    print(f"[ingest 현황]", file=sys.stderr)
    print(f"  완료: {done}개 | 스킵: {skipped}개 | 실패: {failed}개", file=sys.stderr)
    print(f"  미처리 신규: {len(new_pdfs)}개 | raw 갱신됨: {len(stale)}개", file=sys.stderr)

    if new_pdfs:
        print("  [신규]", file=sys.stderr)
        for p in new_pdfs:
            print(f"    - {p.relative_to(PROJECT_DIR)}", file=sys.stderr)

    if stale:
        print("  [갱신 필요]", file=sys.stderr)
        for rel, mtime in stale:
            print(f"    - {rel} (raw 수정: {mtime})", file=sys.stderr)

    return new_pdfs, stale


# ── 기존 wiki 점검 로직 ───────────────────────────────────────────────

def find_broken_links() -> list[tuple[str, str]]:
    slugs = get_all_slugs()
    broken = []
    for page in get_wiki_pages():
        content = page.read_text(encoding="utf-8", errors="replace")
        for link in re.findall(r"\[\[([^\]]+)\]\]", content):
            slug = link.split("|")[0].strip()
            if slug not in slugs:
                broken.append((page.name, slug))
    return broken


def find_stale_pages() -> list[tuple[str, str, int]]:
    stale = []
    for page in get_wiki_pages():
        content = page.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"sources:\s*\[([^\]]*)\]", content, re.DOTALL)
        if not match:
            continue
        sources = [s.strip().strip("\"'") for s in match.group(1).split(",") if s.strip()]
        page_mtime = page.stat().st_mtime
        for src in sources:
            src_path = PROJECT_DIR / src
            if src_path.exists():
                raw_mtime = src_path.stat().st_mtime
                if raw_mtime > page_mtime:
                    delay_days = int((raw_mtime - page_mtime) / 86400)
                    stale.append((page.name, src, delay_days))
    return stale


def build_status_report(today: str, new_pdfs: list, stale_pdfs: list) -> str:
    wiki_pages = get_wiki_pages()
    broken = find_broken_links()
    stale_pages = find_stale_pages()

    new_list = "\n".join(
        f"  - {p.relative_to(PROJECT_DIR)}" for p in new_pdfs
    ) or "  없음"

    stale_raw_list = "\n".join(
        f"  - {rel} (raw 수정: {mtime})" for rel, mtime in stale_pdfs
    ) or "  없음"

    broken_list = "\n".join(
        f"  - {page}에서 [[{slug}]] 참조 오류" for page, slug in broken
    ) or "  이상 없음"

    stale_page_list = "\n".join(
        f"  - {page} (출처: {src}, {days}일 지연)" for page, src, days in stale_pages
    ) or "  이상 없음"

    return f"""점검 날짜: {today}
wiki 페이지 수: {len(wiki_pages)}개

ingest 대기 (신규 raw):
{new_list}

re-ingest 필요 (raw 갱신):
{stale_raw_list}

깨진 링크:
{broken_list}

wiki 페이지 업데이트 필요:
{stale_page_list}"""


def append_to_log(entry: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{entry}\n")


def trigger_ingest() -> None:
    """edit_agent.py --ingest 를 호출해 미처리 파일을 자동 처리한다."""
    print("  → edit_agent.py --ingest 실행 중...", file=sys.stderr)
    subprocess.Popen(
        ["python3", str(EDIT_AGENT), "--ingest"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def trigger_rebuild_index() -> None:
    """edit_agent.py --rebuild-index 를 호출해 index.md를 재생성한다."""
    print("  → index.md 재생성 중...", file=sys.stderr)
    subprocess.run(
        ["python3", str(EDIT_AGENT), "--rebuild-index"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def run(auto_ingest: bool = True) -> str:
    today = datetime.now().strftime("%Y-%m-%d")

    new_pdfs, stale_pdfs = print_ingest_summary()

    needs_ingest = bool(new_pdfs or stale_pdfs)

    status_report = build_status_report(today, new_pdfs, stale_pdfs)

    prompt = (
        f"다음 LLM Wiki 점검 결과를 바탕으로 AGENTS.md 형식에 맞게 "
        f"한국어로 유지보수 보고서를 작성해줘:\n\n{status_report}"
    )

    report = llm_run(prompt, system=SYSTEM_PROMPT)
    append_to_log(report)
    print(f"✓ log.md에 기록 완료", file=sys.stderr)

    # 처리할 파일이 있으면 edit_agent 자동 실행
    if needs_ingest and auto_ingest:
        print(f"  미처리/갱신 파일 {len(new_pdfs) + len(stale_pdfs)}개 발견 → edit_agent 자동 실행", file=sys.stderr)
        trigger_ingest()

    return report


if __name__ == "__main__":
    # --no-ingest 플래그로 자동 ingest 비활성화 가능
    auto = "--no-ingest" not in sys.argv
    print(run(auto_ingest=auto))
