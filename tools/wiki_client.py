"""
Wiki Client — 에이전트용 Python 래퍼

에이전트(edit_agent 등)가 wiki/pages/ 에 직접 접근하는 대신
이 모듈을 통해 MCP 서버 인터페이스를 경유하도록 한다.

사용법:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from tools.wiki_client import search, read_page, create_page, ...
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.wiki_mcp import (
    search_wiki as _search_wiki,
    get_page as _get_page,
    add_page as _add_page,
    update_page as _update_page,
    list_pages as _list_pages,
    get_processed_sources as _get_processed_sources,
    rebuild_index as _rebuild_index,
)


def search(query: str, top_k: int = 5) -> list[dict]:
    """wiki 키워드 검색. [{slug, title, category, tags, summary, path}, ...] 반환."""
    raw = _search_wiki(query, top_k)
    result = json.loads(raw)
    if isinstance(result, dict) and "error" in result:
        return []
    return result


def read_page(page_name: str) -> str:
    """slug 또는 제목으로 페이지 전체 마크다운 반환. 없으면 오류 문자열."""
    return _get_page(page_name)


def create_page(
    title: str,
    content: str,
    category: str = "concept",
    slug: Optional[str] = None,
) -> str:
    """새 wiki 페이지 생성. 성공 시 '[완료] ...' 문자열 반환."""
    return _add_page(title, content, category, slug)


def modify_page(title: str, content: str) -> str:
    """기존 wiki 페이지 내용 교체. 성공 시 '[완료] ...' 문자열 반환."""
    return _update_page(title, content)


def pages_list(subject: Optional[str] = None) -> dict:
    """페이지 목록. {total, pages: [{slug, title, category, tags, sources, updated}]} 반환."""
    raw = _list_pages(subject)
    result = json.loads(raw)
    if isinstance(result, dict) and "error" in result:
        return {"total": 0, "pages": []}
    return result


def get_existing_slugs() -> set[str]:
    """위키에 존재하는 모든 페이지 slug 집합 반환."""
    result = pages_list()
    return {p["slug"] for p in result.get("pages", [])}


def get_processed_sources() -> set[str]:
    """wiki 페이지 sources 필드에 등록된 raw 파일 경로 집합 반환."""
    raw = _get_processed_sources()
    return set(json.loads(raw))


def rebuild_index() -> str:
    """wiki/pages/ 전체 스캔으로 index.md 재생성. 완료 메시지 반환."""
    return _rebuild_index()
