"""
Google Drive client — rclone 기반 (OAuth 앱 등록 불필요)

최초 설정 (1회):
  python pipeline/gdrive.py --auth
  → 브라우저에서 Google 계정 로그인만 하면 완료

이후 사용:
  python pipeline/gdrive.py --ls /강의자료
  python pipeline/gdrive.py --whoami
"""
from __future__ import annotations

import json
import os
import subprocess
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HASH_STORE_PATH = ROOT / "data" / "file_hashes_gdrive.json"
RCLONE_REMOTE   = "gdrive"
RCLONE_BIN      = os.path.expanduser("~/.local/bin/rclone")
SUPPORTED_EXTS  = {".pdf", ".md", ".txt", ".pptx"}


# ── rclone 실행 헬퍼 ──────────────────────────────────────────────────────────

def _run(args: list[str], check=True) -> subprocess.CompletedProcess:
    return subprocess.run(
        [RCLONE_BIN] + args,
        capture_output=True, text=True, check=check
    )


def _is_rclone_available() -> bool:
    try:
        _run(["--version"])
        return True
    except (FileNotFoundError, PermissionError):
        return False


def _is_remote_configured() -> bool:
    result = _run(["listremotes"], check=False)
    return f"{RCLONE_REMOTE}:" in result.stdout


# ── 인증 ─────────────────────────────────────────────────────────────────────

def auth():
    """rclone config으로 Google Drive 원격 설정 (브라우저 로그인만 필요)."""
    if not _is_rclone_available():
        print("❌ rclone이 설치되지 않았습니다.")
        print("   설치: curl https://rclone.org/install.sh | sudo bash")
        return

    if _is_remote_configured():
        print(f"✅ '{RCLONE_REMOTE}' 원격이 이미 설정돼 있습니다.")
        return

    print("\n" + "="*60)
    print("Google Drive 연동 설정")
    print("="*60)
    print("아래 단계를 따라 설정해주세요:\n")
    print("  1. 'n' 입력 (New remote)")
    print(f"  2. 이름: '{RCLONE_REMOTE}' 입력")
    print("  3. Storage type: 'drive' 선택 (Google Drive 번호 입력)")
    print("  4. client_id, client_secret: 공백으로 Enter (기본값 사용)")
    print("  5. scope: '1' 선택 (전체 Drive 접근)")
    print("  6. 나머지는 기본값 Enter")
    print("  7. 'y' 입력 → 브라우저에서 Google 계정 로그인")
    print("  8. 마지막에 'y' 확인\n")
    print("="*60 + "\n")
    print("터미널에서 다음 명령을 실행해주세요:")
    print("\n  rclone config\n")


# ── 파일 목록 ─────────────────────────────────────────────────────────────────

def list_files(folder_path: str = "/") -> list[dict]:
    """
    Google Drive 폴더의 파일을 재귀 조회.
    반환: [{id, name, size, mtime, path, ext}]
    """
    remote_path = f"{RCLONE_REMOTE}:{folder_path.lstrip('/')}"
    result = _run([
        "lsjson", "--recursive", "--files-only",
        "--no-modtime", remote_path
    ], check=False)

    if result.returncode != 0:
        raise RuntimeError(f"rclone lsjson 실패: {result.stderr.strip()}")

    items = []
    for entry in json.loads(result.stdout or "[]"):
        name = entry.get("Name", "")
        ext  = Path(name).suffix.lower()
        if ext not in SUPPORTED_EXTS:
            continue
        items.append({
            "id":    entry.get("ID", entry.get("Path", name)),
            "name":  name,
            "size":  entry.get("Size", 0),
            "mtime": entry.get("ModTime", ""),
            "path":  f"{folder_path.rstrip('/')}/{entry.get('Path', name)}",
        })
    return items


# ── 다운로드 ──────────────────────────────────────────────────────────────────

def download_file(remote_path: str, dest_path: str) -> None:
    """단일 파일 다운로드."""
    src = f"{RCLONE_REMOTE}:{remote_path.lstrip('/')}"
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    _run(["copyto", src, str(dest)])


def sync_folder(remote_folder: str, local_folder: str) -> None:
    """폴더 전체를 로컬로 동기화 (변경분만)."""
    src = f"{RCLONE_REMOTE}:{remote_folder.lstrip('/')}"
    _run(["sync", src, local_folder, "--progress"])


# ── 해시 스토어 ───────────────────────────────────────────────────────────────

def load_hash_store() -> dict:
    if HASH_STORE_PATH.exists():
        return json.loads(HASH_STORE_PATH.read_text())
    return {}


def save_hash_store(store: dict) -> None:
    HASH_STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
    HASH_STORE_PATH.write_text(json.dumps(store, ensure_ascii=False, indent=2))


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Google Drive rclone 헬퍼")
    parser.add_argument("--auth",   action="store_true", help="Google Drive 연동 설정 안내")
    parser.add_argument("--ls",     metavar="FOLDER", nargs="?", const="/", help="파일 목록 조회")
    parser.add_argument("--whoami", action="store_true", help="연결 상태 확인")
    args = parser.parse_args()

    if not _is_rclone_available():
        print("❌ rclone 미설치. 설치 후 다시 실행하세요:")
        print("   curl https://rclone.org/install.sh | sudo bash")
        return

    if args.auth:
        auth()
        return

    if args.whoami:
        if _is_remote_configured():
            result = _run(["about", f"{RCLONE_REMOTE}:"], check=False)
            print(f"✅ '{RCLONE_REMOTE}' 연결됨\n{result.stdout}")
        else:
            print(f"❌ '{RCLONE_REMOTE}' 미설정. 먼저 실행: python pipeline/gdrive.py --auth")
        return

    if args.ls is not None:
        files = list_files(args.ls)
        print(f"\nGoogle Drive '{args.ls}' — {len(files)}개 파일:")
        for f in files:
            print(f"  {f['size']//1024:6d} KB  {f['path']}")


if __name__ == "__main__":
    main()
