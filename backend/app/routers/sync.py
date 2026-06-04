"""
클라우드 드라이브 동기화 API

POST /api/sync            — 전체 과목 동기화 (백그라운드)
GET  /api/sync/browse     — Drive 폴더 탐색
POST /api/sync/pull       — Drive 폴더 선택 → raw/{subject}/ 동기화
GET  /api/sync/log        — 최근 갱신 로그
GET  /api/sync/status     — 마지막 동기화 결과
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


@router.get("/sync/browse")
def browse_drive(provider: str = "onedrive", path: str = "/"):
    """Drive 폴더 탐색 — 하위 디렉터리 목록 반환."""
    try:
        from pipeline.refresh_pipeline import _get_provider
        drv = _get_provider(provider)
        if not hasattr(drv, "list_folders"):
            raise HTTPException(status_code=400, detail="이 provider는 폴더 탐색을 지원하지 않습니다.")
        if not drv._is_rclone_available():
            raise HTTPException(status_code=503, detail="rclone이 설치되지 않았습니다.")
        if not drv._is_remote_configured():
            raise HTTPException(status_code=503, detail=f"'{drv.RCLONE_REMOTE}' remote가 설정되지 않았습니다. python pipeline/{provider}.py --auth 를 실행하세요.")
        folders = drv.list_folders(path)
        parent = str(Path(path).parent) if path != "/" else None
        return {"path": path, "parent": parent, "folders": folders}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class PullRequest(BaseModel):
    provider: str = "onedrive"
    drive_folder: str          # Drive 경로, 예: /강의자료/자료구조
    subject: str               # raw/ 하위 폴더명, 예: 자료구조


def _do_pull(drive_folder: str, subject: str, provider: str):
    global _last_result
    from pipeline.refresh_pipeline import _get_provider, sync_folder, _get_chroma_collection
    from pipeline.parse import parse_file
    from pipeline.chunk import chunk_pages
    from pipeline.embed import get_embedder, embed_and_upsert
    from pathlib import Path as _Path

    drv = _get_provider(provider)
    hash_store = drv.load_hash_store()

    dest_dir = ROOT / "raw" / subject
    dest_dir.mkdir(parents=True, exist_ok=True)

    # 파일 목록 조회
    try:
        remote_files = drv.list_files(drive_folder)
    except Exception as e:
        _last_result = {"error": str(e)}
        return

    collection = _get_chroma_collection()
    model = get_embedder()
    processed = []

    for item in remote_files:
        dest_path = dest_dir / item["name"]
        try:
            drv.download_file(item["path"], str(dest_path))
            pages = parse_file(str(dest_path))
            for p in pages:
                p["subject"] = subject
            chunks = chunk_pages(pages)
            embed_and_upsert(chunks, model, collection)
            hash_store[item["id"]] = {
                "fingerprint": f"{item['size']}_{item['mtime']}",
                "name": item["name"],
                "subject": subject,
            }
            processed.append({"file": item["name"], "status": "ok"})
        except Exception as e:
            processed.append({"file": item["name"], "status": "error", "error": str(e)})

    drv.save_hash_store(hash_store)
    _last_result = {"subject": subject, "drive_folder": drive_folder, "processed": processed}


@router.post("/sync/pull")
async def pull_drive_folder(req: PullRequest, background_tasks: BackgroundTasks):
    """Drive의 특정 폴더를 raw/{subject}/에 동기화."""
    if not req.subject.strip():
        raise HTTPException(status_code=400, detail="subject가 비어있습니다.")
    background_tasks.add_task(_do_pull, req.drive_folder, req.subject.strip(), req.provider)
    return {"message": f"'{req.drive_folder}' → raw/{req.subject}/ 동기화 시작", "provider": req.provider}


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
