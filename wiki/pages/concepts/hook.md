---
title: Hook
category: concept
tags: [automation, agent-lifecycle, determinism, harness]
sources: [raw/시스템 분析 실습/9. Loop and Hooks.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트 생명주기의 특정 이벤트에서 자동으로 실행되는 스크립트. 확률적으로 동작하는 AI 에이전트의 결정을 특정 시점에서 결정론적으로 강제하는 메커니즘. Claude Code의 설정을 통해 등록하며 에이전트가 인식하지 못하는 방식으로 동작한다.

## How It Works

**6가지 Hook 이벤트:**

| 이벤트 | 발생 시점 | 주요 활용 |
|--------|-----------|-----------|
| `UserPromptSubmit` | 사용자 메시지 전송 직후 | 프롬프트 전처리, 컨텍스트 주입 |
| `PreToolUse` | 도구 호출 직전 | 위험 명령어 차단, 승인 요청 |
| `PostToolUse` | 도구 호출 직후 | 결과 로깅, 후처리 |
| `PermissionRequest` | 권한 요청 시 | 자동 승인/거부 규칙 적용 |
| `Stop` | 에이전트 종료 시 | 정리 작업, 알림 발송 |
| `SessionStart` | 세션 시작 시 | 환경 초기화, 컨텍스트 로드 |

**Hook 등록 방법 (CLAUDE.md / settings.json):**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/check_dangerous_commands.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/log_tool_use.sh"
          }
        ]
      }
    ]
  }
}
```

**위험 명령어 차단 Hook 예시:**

```bash
#!/bin/bash
# PreToolUse: check_dangerous_commands.sh
COMMAND="$1"
if echo "$COMMAND" | grep -q "rm -rf\|DROP TABLE\|format"; then
    echo "BLOCKED: Dangerous command detected"
    exit 1  # 0이 아닌 종료 코드로 실행 차단
fi
exit 0
```

**활용 패턴:**
- `SessionStart`: TASK.md 로드, 이전 컨텍스트 복원
- `UserPromptSubmit`: 프롬프트에 자동으로 컨텍스트(프로젝트 정보, 규칙) 추가
- `PreToolUse`: `rm`, `DROP`, `push --force` 등 위험 명령어 사전 차단
- `PostToolUse`: 모든 파일 변경 사항을 자동 로그
- `Stop`: 완료 알림(Slack, 이메일) 자동 발송

## Key Properties

- **결정론적 강제** — LLM의 확률적 결정이 아닌 규칙 기반의 확실한 동작 보장
- **에이전트 투명성** — 에이전트는 Hook 실행을 인식하지 못함 (외부에서 주입)
- **비침습적** — 에이전트 코드나 프롬프트 수정 없이 동작 제어 가능
- **감사 로그** — PostToolUse Hook으로 에이전트의 모든 행동 기록

## Limitations

- Hook 스크립트 오류 시 에이전트 전체 동작이 중단될 수 있음
- 너무 많은 Hook이 실행 시간 증가와 복잡도 유발
- Hook 로직 자체에 버그가 있으면 정상 작업까지 차단

## Relationships

- [[harness-engineering]] (Hook이 harness의 안전 장치이자 Journal 자동화 도구)
- [[mcp]] (MCP 도구 사용 이벤트에 Hook을 연결하여 도구 사용 제어)
- [[loop]] (Loop 실행 중 Hook으로 각 반복 시작/종료 시 자동 동작 삽입)
- [[contract-driven-iteration]] (Hook으로 TASK.md 로그를 자동 업데이트)

## Open Questions

- Hook 스크립트 자체를 에이전트가 생성하거나 수정하는 것이 허용되어야 하는가?
- 여러 Hook이 동일 이벤트에 등록될 때 실행 순서와 충돌 해결 방법은?

## Sources

- raw/9. Loop and Hooks.pdf
