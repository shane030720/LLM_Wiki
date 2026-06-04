#!/usr/bin/env bash
# new-semester.sh — 새 학기 LLM Wiki 서버 초기화
#
# 사용법:
#   bash new-semester.sh [포트번호]
#
# 예시:
#   bash new-semester.sh 8001   → ~/LLM_Wiki_8001/ 생성, 포트 8001에서 서비스 실행
#   bash new-semester.sh        → 포트 입력 안내
#
# 동작:
#   1. 코드만 새 디렉터리에 복사 (raw/, chroma_db/, wiki/, data/ 제외)
#   2. 새 .venv 설치
#   3. 새 systemd 서비스 등록 (llm-wiki-{PORT}.service)
#   4. 새 서버 시작

set -e

# ── 포트 결정 ──────────────────────────────────────────────────────────────
PORT="${1:-}"
if [ -z "$PORT" ]; then
  echo "새 학기 LLM Wiki 서버를 만듭니다."
  echo ""
  read -p "사용할 포트 번호 (예: 8001): " PORT
fi

if ! [[ "$PORT" =~ ^[0-9]+$ ]] || [ "$PORT" -lt 1024 ] || [ "$PORT" -gt 65535 ]; then
  echo "❌ 유효하지 않은 포트: $PORT (1024~65535 범위여야 합니다)"
  exit 1
fi

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST_DIR="${HOME}/LLM_Wiki_${PORT}"
SERVICE_NAME="llm-wiki-${PORT}"

# ── 이미 존재하는지 확인 ───────────────────────────────────────────────────
if [ -d "$DEST_DIR" ]; then
  echo "❌ 이미 존재합니다: $DEST_DIR"
  echo "   다른 포트를 선택하거나 기존 디렉터리를 삭제하세요."
  exit 1
fi

echo ""
echo "=== 새 학기 LLM Wiki 생성 ==="
echo "  원본: $SRC_DIR"
echo "  대상: $DEST_DIR"
echo "  포트: $PORT"
echo ""

# ── 코드 복사 (데이터 제외) ────────────────────────────────────────────────
echo "1. 코드 복사 중..."
rsync -a \
  --exclude='.venv/' \
  --exclude='raw/' \
  --exclude='chroma_db/' \
  --exclude='wiki/pages/' \
  --exclude='wiki/index.md' \
  --exclude='wiki/log.md' \
  --exclude='wiki/ingest_status.json' \
  --exclude='data/' \
  --exclude='.env' \
  --exclude='.git/' \
  "$SRC_DIR/" "$DEST_DIR/"

# wiki 디렉터리 초기 구조 생성
mkdir -p "$DEST_DIR/wiki/pages/concepts"
mkdir -p "$DEST_DIR/wiki/pages/entities"
mkdir -p "$DEST_DIR/wiki/pages/syntheses"
touch "$DEST_DIR/wiki/index.md"
echo "# Wiki Operation Log" > "$DEST_DIR/wiki/log.md"
mkdir -p "$DEST_DIR/raw"
mkdir -p "$DEST_DIR/data"

echo "   완료"

# ── .env 복사 (API 키 재사용) ──────────────────────────────────────────────
if [ -f "$SRC_DIR/.env" ]; then
  cp "$SRC_DIR/.env" "$DEST_DIR/.env"
  echo "2. .env 복사 완료 (API 키 재사용)"
else
  cp "$DEST_DIR/.env.example" "$DEST_DIR/.env"
  echo "2. .env.example → .env 복사 (API 키를 직접 입력하세요)"
fi

# ── 가상환경 설치 ─────────────────────────────────────────────────────────
echo "3. Python 패키지 설치 중..."
cd "$DEST_DIR"
python3 -m venv .venv --without-pip
curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python3 -q
.venv/bin/pip install -q -r backend/requirements.txt
echo "   완료"

# ── systemd 서비스 등록 ────────────────────────────────────────────────────
echo "4. systemd 서비스 등록 중..."

SERVICE_FILE="${HOME}/.config/systemd/user/${SERVICE_NAME}.service"
mkdir -p "$(dirname "$SERVICE_FILE")"

cat > "$SERVICE_FILE" << EOF
[Unit]
Description=LLM Wiki RAG Server (port ${PORT})
After=network.target

[Service]
Type=simple
WorkingDirectory=${DEST_DIR}
ExecStart=${DEST_DIR}/.venv/bin/uvicorn backend.app.main:app --host 0.0.0.0 --port ${PORT}
Restart=on-failure
RestartSec=5
Environment=PYTHONPATH=${DEST_DIR}

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable "$SERVICE_NAME"
systemctl --user start "$SERVICE_NAME"

echo ""
echo "=== 완료 ==="
echo ""
echo "  새 서버 주소:  http://localhost:${PORT}"
echo "  디렉터리:      $DEST_DIR"
echo "  서비스명:      $SERVICE_NAME"
echo ""
echo "  강의자료는 $DEST_DIR/raw/ 에 넣거나,"
echo "  웹 UI의 ☁️ Drive 버튼으로 Drive에서 직접 가져오세요."
echo ""
echo "  서버 제어:"
echo "    시작: systemctl --user start $SERVICE_NAME"
echo "    종료: systemctl --user stop $SERVICE_NAME"
echo "    로그: journalctl --user -u $SERVICE_NAME -f"
