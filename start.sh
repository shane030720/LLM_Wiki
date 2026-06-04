#!/usr/bin/env bash

# systemd 서비스로 관리 (부팅 시 자동 시작)
if systemctl --user is-active --quiet llm-wiki.service 2>/dev/null; then
  echo "✅ 이미 실행 중 — http://localhost:8000"
else
  systemctl --user start llm-wiki.service
  for i in $(seq 1 10); do
    sleep 1
    if curl -s http://localhost:8000/api/health >/dev/null 2>&1; then
      echo "✅ 서버 시작 완료 — http://localhost:8000"
      exit 0
    fi
  done
  echo "❌ 서버 시작 실패. 로그 확인: journalctl --user -u llm-wiki.service"
  exit 1
fi
