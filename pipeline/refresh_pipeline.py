#!/usr/bin/env python3
"""
클라우드 드라이브 자동 갱신 파이프라인 (OneDrive / Google Drive)

동작:
  1. 지정 드라이브 폴더의 파일 목록 조회
  2. 로컬 해시와 비교 → 신규/변경된 파일만 선별
  3. 변경 파일 다운로드 → raw/{subject}/ 저장
  4. 해당 파일만 재임베딩 (ChromaDB upsert)
  5. 결과를 data/refresh_log.jsonl 에 기록

Usage:
  python pipeline/refresh_pipeline.py                          # OneDrive (기본)
  python pipeline/refresh_pipeline.py --provider gdrive        # Google Drive
  python pipeline/refresh_pipeline.py --folder "/강의자료/자료구조" --subject 자료구조
  python pipeline/refresh_pipeline.py --dry-run                # 다운로드 없이 변경 목록만 출력

환경 변수:
  DRIVE_PROVIDER=onedrive|gdrive   (기본: onedrive)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "backend"))

from dotenv import load_dotenv
load_dotenv(ROOT / ".env")

import pipeline.onedrive as _onedrive
import pipeline.gdrive   as _gdrive

_PROVIDERS = {
    "onedrive": _onedrive,
    "gdrive":   _gdrive,
}

def _get_provider(name: str):
    name = name.lower()
    if name not in _PROVIDERS:
        raise ValueError(f"지원하지 않는 provider: '{name}'. 선택 가능: {list(_PROVIDERS)}")
    return _PROVIDERS[name]
from pipeline.parse import parse_file
from pipeline.chunk import chunk_pages
from pipeline.embed import get_embedder, embed_and_upsert

REFRESH_LOG = ROOT / "data" / "refresh_log.jsonl"

# 지원 확장자
SUPPORTED_EXTS = {".pdf", ".md", ".txt", ".pptx"}

# 과목별 OneDrive 폴더 매핑 (기본값; --folder 로 오버라이드 가능)
DEFAULT_FOLDER_MAP = {
    "자료구조":      "/자료구조",
    "알고리즘":      "/알고리즘",
    "컴퓨터네트워크": "/컴퓨터 네트워크",
    "데이터베이스":   "/데이터베이스",
    "시스템분석":     "/시스템 분석",
}

DEFAULT_PROVIDER = os.environ.get("DRIVE_PROVIDER", "onedrive")


def _log(entry: dict) -> None:
    REFRESH_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(REFRESH_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _get_chroma_collection():
    import chromadb
    chroma_dir = ROOT / "chroma_db"
    chroma_dir.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_dir))
    return client.get_or_create_collection("wiki_chunks", metadata={"hnsw:space": "cosine"})


def _is_supported(filename: str) -> bool:
    return Path(filename).suffix.lower() in SUPPORTED_EXTS


def _file_fingerprint(item: dict) -> str:
    """size + mtime 조합으로 변경 감지 (rclone은 eTag 대신 이걸 사용)."""
    return f"{item['size']}_{item['mtime']}"


def sync_folder(
    folder: str,
    subject: str,
    hash_store: dict,
    dry_run: bool = False,
    provider: str = "onedrive",
) -> dict:
    """
    클라우드 드라이브 폴더 하나를 동기화.
    변경 감지: size + mtime 조합.
    """
    drv = _get_provider(provider)
    print(f"\n{'[DRY-RUN] ' if dry_run else ''}[{provider}] 폴더 동기화: {folder} (과목={subject})")

    # 1. 드라이브 파일 목록
    try:
        remote_files = drv.list_files(folder)
    except Exception as e:
        print(f"  ❌ 폴더 조회 실패: {e}")
        return {"folder": folder, "subject": subject, "error": str(e)}

    print(f"  원격 파일: {len(remote_files)}개")

    # 2. 변경 파일 선별 (size+mtime 비교)
    new_items, changed = [], []
    for item in remote_files:
        key = item["id"]
        fp  = _file_fingerprint(item)
        stored = hash_store.get(key, {})
        if not stored:
            new_items.append(item)
        elif stored.get("fingerprint") != fp:
            changed.append(item)

    to_process = new_items + changed
    print(f"  신규: {len(new_items)}개 / 변경: {len(changed)}개 / 스킵: {len(remote_files) - len(to_process)}개")

    if dry_run or not to_process:
        for item in to_process:
            tag = "신규" if item in new_items else "변경"
            print(f"  [{tag}] {item['path']}")
        return {
            "folder": folder, "subject": subject,
            "new": len(new_items), "changed": len(changed),
            "skipped": len(remote_files) - len(to_process),
            "processed": [],
        }

    # 3. 다운로드 + 임베딩
    dest_dir = ROOT / "raw" / subject
    dest_dir.mkdir(parents=True, exist_ok=True)

    collection = _get_chroma_collection()
    model = get_embedder()
    processed = []

    for item in to_process:
        dest_path = dest_dir / item["name"]
        tag = "신규" if item in new_items else "변경"
        print(f"  [{tag}] 다운로드: {item['name']} ...", end=" ", flush=True)

        try:
            drv.download_file(item["path"], str(dest_path))
            print("✓", end=" ", flush=True)
        except Exception as e:
            print(f"❌ 다운로드 실패: {e}")
            processed.append({"file": item["name"], "status": "download_failed", "error": str(e)})
            continue

        # 임베딩
        try:
            pages = parse_file(str(dest_path))
            for p in pages:
                p["subject"] = subject
            chunks = chunk_pages(pages)
            embed_and_upsert(chunks, model, collection)
            print(f"임베딩 {len(chunks)}청크 ✓")
            processed.append({"file": item["name"], "status": "ok", "chunks": len(chunks)})
        except Exception as e:
            print(f"❌ 임베딩 실패: {e}")
            processed.append({"file": item["name"], "status": "embed_failed", "error": str(e)})
            continue

        # 핑거프린트 갱신
        hash_store[item["id"]] = {
            "fingerprint": _file_fingerprint(item),
            "name":        item["name"],
            "subject":     subject,
            "synced":      datetime.now().isoformat(),
        }

    return {
        "folder": folder, "subject": subject,
        "new": len(new_items), "changed": len(changed),
        "skipped": len(remote_files) - len(to_process),
        "processed": processed,
    }


def run_all(
    folder_map: dict[str, str],
    dry_run: bool = False,
    provider: str = "onedrive",
):
    drv = _get_provider(provider)
    hash_store = drv.load_hash_store()

    started_at = datetime.now().isoformat()
    results = []

    for subject, folder in folder_map.items():
        result = sync_folder(folder, subject, hash_store, dry_run=dry_run, provider=provider)
        results.append(result)

    if not dry_run:
        drv.save_hash_store(hash_store)

    summary = {
        "timestamp":  started_at,
        "dry_run":    dry_run,
        "subjects":   list(folder_map.keys()),
        "results":    results,
        "total_new":  sum(r.get("new", 0) for r in results),
        "total_changed": sum(r.get("changed", 0) for r in results),
        "total_skipped": sum(r.get("skipped", 0) for r in results),
    }

    _log(summary)

    print(f"\n{'='*50}")
    print(f"[{provider}] 동기화 완료 {'(DRY-RUN)' if dry_run else ''}")
    print(f"  신규: {summary['total_new']}  변경: {summary['total_changed']}  스킵: {summary['total_skipped']}")
    print(f"  로그: {REFRESH_LOG}")
    print(f"{'='*50}\n")

    return summary


def main():
    parser = argparse.ArgumentParser(description="클라우드 드라이브 강의자료 자동 갱신 파이프라인")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER,
                        choices=["onedrive", "gdrive"],
                        help="클라우드 드라이브 선택 (기본: 환경변수 DRIVE_PROVIDER 또는 onedrive)")
    parser.add_argument("--folder",   help="드라이브 폴더 경로 (단일 과목 실행 시)")
    parser.add_argument("--subject",  help="과목 이름 (--folder 와 함께 사용)")
    parser.add_argument("--dry-run",  action="store_true", help="변경 목록만 출력, 실제 다운로드/임베딩 없음")
    parser.add_argument("--show-log", action="store_true", help="최근 갱신 로그 출력")
    args = parser.parse_args()

    if args.show_log:
        if REFRESH_LOG.exists():
            lines = REFRESH_LOG.read_text().strip().splitlines()
            for line in lines[-5:]:
                entry = json.loads(line)
                print(f"[{entry['timestamp'][:19]}] [{entry.get('provider','onedrive')}] "
                      f"신규:{entry.get('total_new',0)} 변경:{entry.get('total_changed',0)} 스킵:{entry.get('total_skipped',0)}")
        else:
            print("갱신 로그 없음")
        return

    if args.folder:
        if not args.subject:
            parser.error("--folder 사용 시 --subject 도 필요합니다")
        folder_map = {args.subject: args.folder}
    else:
        folder_map = DEFAULT_FOLDER_MAP

    run_all(folder_map, dry_run=args.dry_run, provider=args.provider)


if __name__ == "__main__":
    main()
