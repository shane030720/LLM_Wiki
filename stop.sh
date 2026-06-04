#!/usr/bin/env bash

systemctl --user stop llm-wiki.service 2>/dev/null && echo "🛑 서버 종료" || echo "⚠️  실행 중인 서버가 없습니다."
