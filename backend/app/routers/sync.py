"""
OneDrive 동기화 API 엔드포인트
POST /api/sync          — 전체 과목 동기화 (백그라운드)
POST /api/sync/subject  — 특정 과목만 동기화
GET  /api/sync/log      — 최근 갱신 로그
GET  /api/sync/status   — 마지막 동기화 결과
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

router = APIRouter()

REFRESH_LOG = ROOT / "data" / "refresh_log.jsonl"
_last_result: dict = {}


class SyncRequest(BaseModel):
    subject: Optional[str] = None
    folder: Optional[str] = None
    dry_run: bool = False
    provider: str = "onedrive"   # "onedrive" | "gdrive"


def _do_sync(subject: Optional[str], folder: Optional[str], dry_run: bool, provider: str):
    global _last_result
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")

    from pipeline.refresh_pipeline import run_all, DEFAULT_FOLDER_MAP

    if subject and folder:
        folder_map = {subject: folder}
    elif subject:
        folder_map = {subject: DEFAULT_FOLDER_MAP.get(subject, f"/강의자료/{subject}")}
    else:
        folder_map = DEFAULT_FOLDER_MAP

    result = run_all(folder_map, dry_run=dry_run, provider=provider)
    _last_result = result


@router.post("/sync")
async def trigger_sync(req: SyncRequest, background_tasks: BackgroundTasks):
    """동기화를 백그라운드로 시작합니다. 완료 여부는 /api/sync/log 로 확인."""
    background_tasks.add_task(_do_sync, req.subject, req.folder, req.dry_run, req.provider)
    return {"message": "동기화 시작됨", "provider": req.provider, "dry_run": req.dry_run}


@router.get("/sync/status")
def sync_status():
    """마지막 동기화 결과 반환."""
    return _last_result or {"message": "아직 동기화 이력 없음"}


@router.get("/sync/log")
def sync_log(limit: int = 10):
    """최근 동기화 로그 반환."""
    if not REFRESH_LOG.exists():
        return {"entries": []}
    lines = REFRESH_LOG.read_text().strip().splitlines()
    entries = []
    for line in lines[-limit:]:
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return {"entries": list(reversed(entries))}
