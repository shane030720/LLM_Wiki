#!/usr/bin/env python3
"""PreToolUse hook: wiki/pages/ 직접 편집 차단

Edit/Write 도구 호출 시 대상 경로가 wiki/pages/ 하위이면 차단한다.
edit_agent는 MCP(wiki_client → wiki_mcp)를 통해 Python 파일 쓰기를 하므로
Edit/Write 도구를 사용하지 않아 이 hook의 영향을 받지 않는다.

exit 0 → 허용
exit 2 → 차단 (Claude Code가 작업 취소 + 메시지 출력)
"""
import json
import sys

data = json.load(sys.stdin)
tool_input = data.get("tool_input", {})
file_path = str(tool_input.get("file_path", "") or tool_input.get("path", ""))

if "wiki/pages/" in file_path:
    print(
        "[차단] wiki/pages/ 직접 편집은 허용되지 않습니다.\n"
        "wiki 페이지는 반드시 MCP 도구를 통해서만 수정하세요:\n"
        "  add_page(title, content, category)  — 새 페이지 생성\n"
        "  update_page(title, content)          — 기존 페이지 수정\n"
        "  (edit_agent --ingest 실행 시 자동으로 MCP를 경유합니다)"
    )
    sys.exit(2)

sys.exit(0)
