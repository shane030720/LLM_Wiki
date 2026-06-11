"""
GET /api/wiki/pages           — MCP wiki_mcp.list_pages() 기반 전체 목록
GET /api/wiki/pages/{slug}    — MCP wiki_mcp.get_page() 기반 단일 페이지 내용
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from fastapi import APIRouter, HTTPException

ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.wiki_client import pages_list, read_page

router = APIRouter()


def _split_frontmatter(raw: str) -> tuple[dict, str]:
    """frontmatter와 본문을 분리한다."""
    # get_page()의 "# 파일 경로:" 헤더 제거
    if raw.startswith("# 파일 경로:"):
        raw = raw.split("\n\n", 1)[-1]

    if not raw.startswith("---"):
        return {}, raw

    end = raw.find("---", 3)
    if end == -1:
        return {}, raw

    fm_text = raw[3:end].strip()
    body = raw[end + 3:].lstrip("\n")

    fm: dict = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key] = val

    return fm, body


@router.get("/wiki/pages")
def list_wiki_pages(subject: str | None = None):
    """wiki/pages/ 전체 페이지 목록 (카테고리·태그·sources 포함)."""
    return pages_list(subject)


@router.get("/wiki/pages/{slug}")
def get_wiki_page(slug: str):
    """slug로 wiki 페이지를 반환. frontmatter는 메타데이터로 분리."""
    raw = read_page(slug)
    if raw.startswith("[오류]") or raw.startswith("[error]"):
        raise HTTPException(status_code=404, detail=raw)

    fm, body = _split_frontmatter(raw)
    return {
        "slug": slug,
        "title": fm.get("title", slug),
        "category": fm.get("category", ""),
        "tags": fm.get("tags", []),
        "sources": fm.get("sources", []),
        "content": body,
    }
