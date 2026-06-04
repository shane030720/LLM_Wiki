"""
GET /api/subjects        — raw/ 폴더 기반 과목·파일 목록
GET /api/file-preview    — 특정 파일의 ChromaDB 청크 미리보기
"""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import APIRouter, Query

ROOT = Path(__file__).resolve().parent.parent.parent.parent
RAW_DIR = ROOT / "raw"

SUPPORTED_EXTS = {".pdf", ".md", ".txt", ".pptx"}

router = APIRouter()


@router.get("/subjects")
def list_subjects():
    """raw/ 하위 폴더 = 과목, 그 안의 파일 = 강의자료"""
    if not RAW_DIR.exists():
        return {"subjects": []}

    subjects = []
    for subj_dir in sorted(RAW_DIR.iterdir()):
        if not subj_dir.is_dir():
            continue
        files = sorted(
            f.name for f in subj_dir.iterdir()
            if f.is_file() and f.suffix.lower() in SUPPORTED_EXTS
        )
        if files:
            subjects.append({"name": subj_dir.name, "files": files})

    return {"subjects": subjects}


@router.get("/file-preview")
def file_preview(
    source: str = Query(..., description="파일명"),
    subject: str = Query(..., description="과목명"),
    limit: int = 5,
):
    """ChromaDB에서 해당 파일의 청크를 가져와 미리보기로 반환."""
    from app.db.chroma import get_collection

    collection = get_collection()
    results = collection.get(
        where={"$and": [{"source": source}, {"subject": subject}]},
        limit=min(limit, 20),
        include=["documents", "metadatas"],
    ) if collection.count() > 0 else {"documents": [], "metadatas": []}

    chunks = []
    for doc, meta in zip(results["documents"], results["metadatas"]):
        chunks.append({"page": meta.get("page", ""), "text": doc})

    chunks.sort(key=lambda c: int(c["page"]) if c["page"].isdigit() else 0)

    return {
        "source": source,
        "subject": subject,
        "chunks": chunks,
    }
