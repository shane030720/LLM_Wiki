#!/usr/bin/env bash
set -e

echo "=== LLM Wiki 백엔드 설치 ==="

cd "$(dirname "$0")"

# 가상환경 생성
if [ ! -d ".venv" ]; then
  python3 -m venv .venv --without-pip
  curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python3
  echo "가상환경 생성 완료"
fi

source .venv/bin/activate

# 의존성 설치
pip install -q -r backend/requirements.txt

echo ""
echo "=== 설치 완료 ==="
echo ""
echo "다음 단계:"
echo "  1. .env 파일에 ANTHROPIC_API_KEY 입력"
echo "  2. 문서 임베딩:  source .venv/bin/activate && python pipeline/embed.py --dir raw/ --subject 시스템분석이론"
echo "  3. 서버 실행:    source .venv/bin/activate && cd backend && uvicorn app.main:app --reload --port 8000"
echo "  4. 브라우저:     http://localhost:8000"
