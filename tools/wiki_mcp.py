#!/usr/bin/env python3
"""
LLM Wiki MCP Server

에이전트가 wiki 페이지에 표준화된 방식으로 접근할 수 있도록 하는 MCP 서버.
API 키 불필요 — 파일시스템 직접 접근 (백엔드 서버 불필요).

Tools:
  search_wiki(query, top_k)        — wiki 페이지 키워드 검색
  get_page(page_name)              — 특정 페이지 전체 내용 반환
  add_page(title, content, category) — 새 페이지 추가 + index.md 갱신
  update_page(title, content)      — 기존 페이지 수정 + index.md 갱신
  list_pages(subject)              — 과목/카테고리별 페이지 목록

실행:
  python tools/wiki_mcp.py              # stdio (Claude Code MCP 연동)

Claude Code 설정 (.claude/settings.json):
  {
    "mcpServers": {
      "llm-wiki": {
        "command": "python",
        "args": ["tools/wiki_mcp.py"]
      }
    }
  }
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Optional

from fastmcp import FastMCP

# ── 경로 설정 ─────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
PAGES_DIR = WIKI_DIR / "pages"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

CATEGORIES = ("concepts", "entities", "syntheses")

mcp = FastMCP(
    "LLM Wiki",
    instructions=(
        "LLM Wiki MCP 서버. wiki/pages/ 아래의 마크다운 페이지를 검색·읽기·추가·수정할 수 있다. "
        "API 키 불필요. 백엔드 서버 없이 파일시스템으로 직접 동작."
    ),
)


# ── 헬퍼 ──────────────────────────────────────────────────────────────────────

_CAT_DIR_TO_SINGULAR = {
    "concepts": "concept",
    "entities": "entity",
    "syntheses": "synthesis",
}

_CAT_TO_DIR = {
    "concept": "concepts",   "concepts": "concepts",
    "entity": "entities",    "entities": "entities",
    "synthesis": "syntheses","syntheses": "syntheses",
}


def _title_to_slug(title: str) -> str:
    """'Binary Search Tree' → 'binary-search-tree'"""
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def _find_page(page_name: str) -> Optional[Path]:
    """slug 또는 제목으로 페이지 파일 탐색. 없으면 None."""
    slug = _title_to_slug(page_name)
    for cat in CATEGORIES:
        p = PAGES_DIR / cat / f"{slug}.md"
        if p.exists():
            return p
    # 부분 매칭 시도 (slug 포함)
    for cat in CATEGORIES:
        cat_dir = PAGES_DIR / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.glob("*.md"):
            if f.stem == "_about":
                continue
            if slug in f.stem or f.stem in slug:
                return f
    return None


def _parse_frontmatter(content: str) -> dict:
    """YAML frontmatter 파싱 (간단 구현)."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    result: dict = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1]
            result[key] = [v.strip() for v in inner.split(",") if v.strip()]
        else:
            result[key] = val
    return result


def _extract_summary(content: str, max_len: int = 80) -> str:
    """## Definition 또는 ## Overview 첫 문장을 요약으로 추출."""
    for header in ("## Definition", "## Overview", "## Summary"):
        idx = content.find(header)
        if idx == -1:
            continue
        body = content[idx + len(header):].lstrip("\n")
        # 코드 블록 건너뜀
        if body.startswith("```"):
            continue
        # 첫 비어있지 않은 줄
        first = next((l.strip() for l in body.splitlines() if l.strip()), "")
        if first:
            return first[:max_len] + ("..." if len(first) > max_len else "")
    # fallback: frontmatter 이후 첫 텍스트 줄
    lines = content.splitlines()
    for line in lines:
        line = line.strip()
        if line and not line.startswith(("#", "-", "|", "---", "```", ">")):
            return line[:max_len] + ("..." if len(line) > max_len else "")
    return ""


def _score_page(path: Path, keywords: list[str]) -> int:
    """파일 내용에서 키워드 등장 횟수로 점수 계산."""
    try:
        text = path.read_text(encoding="utf-8").lower()
    except Exception:
        return 0
    score = 0
    for kw in keywords:
        kw_lower = kw.lower()
        # 제목/태그에 등장하면 가중치 3
        fm_end = text.find("---", 3)
        fm_text = text[:fm_end] if fm_end != -1 else ""
        score += fm_text.count(kw_lower) * 3
        # 본문 등장
        body = text[fm_end:] if fm_end != -1 else text
        score += body.count(kw_lower)
    return score


def _update_index(slug: str, category: str, fm: dict, summary: str) -> None:
    """index.md 테이블에 행 추가 또는 갱신."""
    if not INDEX_FILE.exists():
        return

    today = date.today().isoformat()
    tags_str = ", ".join(fm.get("tags", []))
    cat_label = _CAT_DIR_TO_SINGULAR.get(category, category)
    new_row = f"| [[{slug}]] | {cat_label} | {tags_str} | {today} | {summary} |"

    content = INDEX_FILE.read_text(encoding="utf-8")

    # 기존 행이 있으면 교체
    pattern = rf"\|\s*\[\[{re.escape(slug)}\]\].*"
    if re.search(pattern, content):
        content = re.sub(pattern, new_row, content)
    else:
        # 테이블 마지막 행 다음에 추가
        table_end = content.rfind("| [[")
        if table_end != -1:
            line_end = content.find("\n", table_end)
            content = content[: line_end + 1] + new_row + "\n" + content[line_end + 1 :]
        else:
            content += f"\n{new_row}\n"

    INDEX_FILE.write_text(content, encoding="utf-8")


def _append_log(action: str, slug: str, category: str) -> None:
    """wiki/log.md에 작업 기록 추가."""
    if not LOG_FILE.exists():
        return
    today = date.today().isoformat()
    entry = f"- {today} | MCP | {action} | `{category}/{slug}.md`\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)


# ── MCP Tools ─────────────────────────────────────────────────────────────────

@mcp.tool()
def search_wiki(query: str, top_k: int = 5) -> str:
    """
    wiki 페이지에서 키워드 검색.

    Args:
        query: 검색어 (예: "binary search tree", "TCP 혼잡제어")
        top_k: 반환할 최대 결과 수 (기본 5)

    Returns:
        JSON 배열: [{slug, title, category, tags, summary, path}, ...]
    """
    if not PAGES_DIR.exists():
        return json.dumps({"error": "wiki/pages/ 디렉토리를 찾을 수 없습니다."}, ensure_ascii=False)

    keywords = [w for w in re.split(r"[\s,]+", query.strip()) if w]
    if not keywords:
        return json.dumps([], ensure_ascii=False)

    scored: list[tuple[int, Path]] = []
    for cat in CATEGORIES:
        cat_dir = PAGES_DIR / cat
        if not cat_dir.exists():
            continue
        for page_file in cat_dir.glob("*.md"):
            if page_file.stem == "_about":
                continue
            s = _score_page(page_file, keywords)
            if s > 0:
                scored.append((s, page_file))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for _, page_file in scored[:top_k]:
        try:
            content = page_file.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = _parse_frontmatter(content)
        results.append({
            "slug": page_file.stem,
            "title": fm.get("title", page_file.stem),
            "category": fm.get("category", _CAT_DIR_TO_SINGULAR.get(page_file.parent.name, page_file.parent.name)),
            "tags": fm.get("tags", []),
            "summary": _extract_summary(content),
            "path": str(page_file.relative_to(ROOT)),
        })

    return json.dumps(results, ensure_ascii=False, indent=2)


@mcp.tool()
def get_page(page_name: str) -> str:
    """
    wiki 페이지 전체 내용 반환.

    Args:
        page_name: 페이지 slug 또는 제목 (예: "mcp", "binary-search-tree", "TCP 3-way handshake")

    Returns:
        마크다운 전체 내용. 페이지가 없으면 오류 메시지.
    """
    page_file = _find_page(page_name)
    if page_file is None:
        return f"[오류] '{page_name}' 페이지를 찾을 수 없습니다. search_wiki()로 정확한 slug를 확인하세요."

    try:
        content = page_file.read_text(encoding="utf-8")
    except Exception as e:
        return f"[오류] 파일 읽기 실패: {e}"

    return f"# 파일 경로: {page_file.relative_to(ROOT)}\n\n{content}"


@mcp.tool()
def get_processed_sources() -> str:
    """
    wiki 페이지 전체를 스캔해 sources 필드에 등록된 raw 파일 경로 집합 반환.

    Returns:
        JSON 배열: ["raw/과목/파일.pdf", ...]
    """
    if not PAGES_DIR.exists():
        return json.dumps([], ensure_ascii=False)

    sources: set[str] = set()
    for page_file in PAGES_DIR.rglob("*.md"):
        if page_file.stem == "_about":
            continue
        try:
            content = page_file.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = _parse_frontmatter(content)
        for src in fm.get("sources", []):
            src = src.strip().strip("\"'")
            if src:
                sources.add(src)

    return json.dumps(sorted(sources), ensure_ascii=False)


@mcp.tool()
def rebuild_index() -> str:
    """
    wiki/pages/ 전체를 스캔해 index.md를 완전히 재생성한다.
    ingest 완료 후 정합성 보장을 위해 호출한다.

    Returns:
        완료 메시지 (생성된 페이지 수 포함).
    """
    if not PAGES_DIR.exists():
        return "[오류] wiki/pages/ 디렉토리를 찾을 수 없습니다."

    from datetime import datetime as _dt
    today = date.today().isoformat()

    seen: set[str] = set()
    rows: dict[str, list] = {"concept": [], "entity": [], "synthesis": []}

    for md in sorted(PAGES_DIR.rglob("*.md")):
        if md.stem == "_about" or md.stem in seen:
            continue
        seen.add(md.stem)
        try:
            content = md.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = _parse_frontmatter(content)
        title = fm.get("title", md.stem)
        cat = fm.get("category", _CAT_DIR_TO_SINGULAR.get(md.parent.name, md.parent.name))
        tags = ", ".join(fm.get("tags", []))
        updated = fm.get("updated", today)
        summary = _extract_summary(content)

        bucket = cat if cat in rows else "concept"
        rows[bucket].append((title, md.stem, tags, updated, summary))

    for bucket in rows:
        rows[bucket].sort(key=lambda x: x[0].lower())

    def _fmt(bucket: str) -> str:
        return "\n".join(
            f"| [[{slug}]] | {bucket} | {tags} | {upd} | {summ} |"
            for _, slug, tags, upd, summ in rows[bucket]
        )

    total = sum(len(v) for v in rows.values())

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

    return f"[완료] index.md 재생성: {total}개 (concept {len(rows['concept'])}, entity {len(rows['entity'])}, synthesis {len(rows['synthesis'])})"


@mcp.tool()
def add_page(title: str, content: str, category: str = "concept", slug: Optional[str] = None) -> str:
    """
    새 wiki 페이지 추가. index.md와 log.md도 자동 갱신.

    Args:
        title: 페이지 제목 (예: "Dijkstra Algorithm")
        content: 마크다운 내용 (frontmatter 포함 권장)
        category: "concept" | "entity" | "synthesis" (기본: "concept")
        slug: 파일명 slug 직접 지정 (미지정 시 title에서 자동 생성)

    Returns:
        생성된 파일 경로 또는 오류 메시지.
    """
    cat_dir_name = _CAT_TO_DIR.get(category.lower(), "concepts")

    slug = slug or _title_to_slug(title)
    cat_dir = PAGES_DIR / cat_dir_name
    cat_dir.mkdir(parents=True, exist_ok=True)

    page_file = cat_dir / f"{slug}.md"
    if page_file.exists():
        return f"[오류] '{slug}.md'가 이미 존재합니다. update_page()를 사용하세요."

    # frontmatter가 없으면 자동 생성
    if not content.strip().startswith("---"):
        today = date.today().isoformat()
        fm = (
            f"---\n"
            f"title: {title}\n"
            f"category: {_CAT_DIR_TO_SINGULAR.get(cat_dir_name, category.lower())}\n"
            f"tags: []\n"
            f"sources: []\n"
            f"created: {today}\n"
            f"updated: {today}\n"
            f"---\n\n"
        )
        content = fm + content
    else:
        # updated 날짜 갱신
        today = date.today().isoformat()
        content = re.sub(r"(updated:\s*)[\d-]+", f"\\g<1>{today}", content)

    page_file.write_text(content, encoding="utf-8")

    fm_parsed = _parse_frontmatter(content)
    summary = _extract_summary(content)
    _update_index(slug, cat_dir_name, fm_parsed, summary)
    _append_log("add", slug, cat_dir_name)

    return f"[완료] {page_file.relative_to(ROOT)} 생성됨"


@mcp.tool()
def update_page(title: str, content: str) -> str:
    """
    기존 wiki 페이지 내용 수정. index.md와 log.md도 자동 갱신.

    Args:
        title: 수정할 페이지의 slug 또는 제목
        content: 새 마크다운 내용 (전체 교체)

    Returns:
        수정된 파일 경로 또는 오류 메시지.
    """
    page_file = _find_page(title)
    if page_file is None:
        return f"[오류] '{title}' 페이지를 찾을 수 없습니다. search_wiki()로 정확한 slug를 확인하세요."

    # updated 날짜 갱신
    today = date.today().isoformat()
    if "updated:" in content:
        content = re.sub(r"(updated:\s*)[\d-]+", f"\\g<1>{today}", content)

    page_file.write_text(content, encoding="utf-8")

    fm_parsed = _parse_frontmatter(content)
    summary = _extract_summary(content)
    cat_dir_name = page_file.parent.name
    _update_index(page_file.stem, cat_dir_name, fm_parsed, summary)
    _append_log("update", page_file.stem, cat_dir_name)

    return f"[완료] {page_file.relative_to(ROOT)} 수정됨"


@mcp.tool()
def list_pages(subject: Optional[str] = None) -> str:
    """
    wiki 페이지 목록 반환.

    Args:
        subject: 필터 조건 (선택).
                 - 카테고리: "concept", "entity", "synthesis"
                 - 과목명 키워드: "자료구조", "알고리즘", "데이터베이스", "컴퓨터네트워크" 등
                 - None이면 전체 목록

    Returns:
        JSON 배열: [{slug, title, category, tags, updated}, ...]
    """
    if not PAGES_DIR.exists():
        return json.dumps({"error": "wiki/pages/ 디렉토리를 찾을 수 없습니다."}, ensure_ascii=False)

    # 카테고리 필터 결정
    cat_map = {"concept": "concepts", "entity": "entities", "synthesis": "syntheses"}
    filter_cats: list[str] = []
    filter_source: str = ""

    if subject:
        normalized = subject.lower().strip()
        if normalized in cat_map:
            filter_cats = [cat_map[normalized]]
        elif normalized in ("concepts", "entities", "syntheses"):
            filter_cats = [normalized]
        else:
            filter_source = normalized  # 과목명 키워드

    scan_cats = filter_cats if filter_cats else list(CATEGORIES)

    pages = []
    for cat in scan_cats:
        cat_dir = PAGES_DIR / cat
        if not cat_dir.exists():
            continue
        for page_file in sorted(cat_dir.glob("*.md")):
            if page_file.stem == "_about":
                continue
            try:
                content = page_file.read_text(encoding="utf-8")
            except Exception:
                continue
            fm = _parse_frontmatter(content)

            # 과목명 필터: sources 필드에 키워드 포함 여부
            if filter_source:
                sources = " ".join(fm.get("sources", [])).lower()
                tags = " ".join(fm.get("tags", [])).lower()
                title_lower = fm.get("title", "").lower()
                if filter_source not in sources and filter_source not in tags and filter_source not in title_lower:
                    continue

            pages.append({
                "slug": page_file.stem,
                "title": fm.get("title", page_file.stem),
                "category": fm.get("category", _CAT_DIR_TO_SINGULAR.get(cat, cat)),
                "tags": fm.get("tags", []),
                "sources": fm.get("sources", []),
                "updated": fm.get("updated", ""),
            })

    total = len(pages)
    return json.dumps({"total": total, "pages": pages}, ensure_ascii=False, indent=2)


# ── 진입점 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
