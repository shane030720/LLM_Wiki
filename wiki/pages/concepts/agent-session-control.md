---
title: Agent Session Control
category: concept
tags: [agent, session, cli, persistence, permission]
sources: [raw/시스템 분석 실습/3. Agents subprocess calling.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

AI CLI 에이전트(Claude, Codex, Gemini)에서 대화 세션을 식별·재개·유지 또는 폐기하는 메커니즘의 총칭. 각 에이전트는 고유한 세션 ID를 부여하며, 이를 통해 이전 대화 맥락을 복원하거나 의도적으로 영속성을 차단할 수 있다. 권한 수준 설정도 세션 인터페이스의 핵심 축을 구성한다.

## How It Works

### 세션 재개 (Resume)

각 에이전트는 세션 목록 조회, 마지막 세션 재개, 특정 세션 ID로 복귀를 각각 지원한다:

**Claude:**
```
claude -c                          # 최근 세션 즉시 이어감 (--continue)
claude --resume                    # 세션 목록에서 선택
claude --resume <session-id>       # 특정 세션으로 직접 이어감
```

Python에서 세션 재개 시:
```python
subprocess.run(
    ["claude", "-p", "--resume", SESSION_ID, "--output-format", "json"],
    input="이전 질문을 확인해주세요.",
    capture_output=True, encoding="utf-8"
)
```

**Codex:**
```
codex resume                       # 세션 picker에서 선택
codex resume <session-id>          # 특정 세션으로 직접
codex resume --last                # 현재 디렉토리 기준 최근 세션
```

**Gemini:**
```
gemini --resume                    # 최근 세션 이어감
gemini --resume <index>            # 인덱스로 특정 세션
gemini --list-sessions             # 세션 목록 확인
```

### 세션 영속성 제어 플래그

| 에이전트 | 영속성 제거 플래그 |
|---|---|
| Claude | `--no-session-persistence` |
| Codex | `--ephemeral` |
| Gemini | 해당 없음 (모든 세션은 로컬에 저장이 원칙) |

`--ephemeral` 또는 `--no-session-persistence`를 사용하면 해당 실행의 세션이 로컬에 저장되지 않아, 이후 resume이 불가능하다. 자동화 파이프라인에서 세션 누적을 방지할 때 유용하다.

### 권한 수준 (Permission Levels)

에이전틱 코딩 인터페이스의 또 다른 축은 에이전트가 취할 수 있는 행동의 권한 범위다.

**권한 완전 허용 플래그:**
```
claude --dangerously-skip-permissions
gemini --yolo
codex --dangerously-bypass-approvals-and-sandbox
```

기본 동작은 위험한 명령 실행 전 사용자 확인을 요청한다:
```
Would you like to run the following command?
$ git clone https://github.com/openai/codex.git codex-cli
> 1. Yes, proceed (y)
  2. Yes, and don't ask again for commands that start with ...
  3. No, and tell Codex what to do differently (esc)
```

## Key Properties

- 세션 ID는 응답 JSON의 `session_id` 필드에서 추출할 수 있다
- Gemini는 세션 영속성 제거 플래그가 없어 모든 실행이 로컬에 기록된다
- 권한 완전 허용 시 단점: 사용자가 더 이상 완전한 제어권을 가지지 않으며, 멈춰야 할 순간에 에이전트가 멈추지 않는다
- 권한 완전 허용의 실패 사례: 테스트 코드 작성 및 실행 후, 사용자 의도와 무관하게 테스트용 코드와 산출물을 복구 불가능하게 삭제한 사례
- 세션 재개를 위해 `build_cli_command()`에서 `--ephemeral`/`--no-session-persistence` 플래그를 제거해야 한다 (세션 ID가 저장되어야 resume이 가능하므로)
- 하나의 작업 환경에서 여러 에이전트를 운용할 때 각 에이전트의 세션을 별도로 관리해야 한다

## Relationships

- [[ai-cli-invocation]] (세션 플래그가 포함된 명령 구성 방식)
- [[claude-code]] (Claude의 세션 플래그: -c, --resume, --no-session-persistence)
- [[codex-cli]] (Codex의 세션 플래그: resume, --ephemeral)
- [[gemini-cli]] (Gemini의 세션 플래그: --resume, --list-sessions)
- [[agentic-coding]] (세션 관리가 필요한 상위 개발 패러다임)
- [[parallel-agent]] (다수 에이전트 운용 시 세션 격리 필요성)

## Open Questions

- 하나의 작업 환경에서 Claude, Codex, Gemini를 동시에 운용할 때 각 에이전트의 세션 ID를 어떻게 통합 관리할 것인가?
- 세션 영속성을 의도적으로 유지해야 하는 시나리오(장기 프로젝트, 컨텍스트 누적)와 제거해야 하는 시나리오(자동화 파이프라인, 독립 실행) 간의 기준은 무엇인가?
- `--dangerously-skip-permissions` 수준의 권한을 부여했을 때 에이전트의 행동을 사후에 감사(audit)하는 메커니즘이 필요하다

## Sources

- raw/시스템 분석 실습/3. Agents subprocess calling.pdf
