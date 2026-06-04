---
title: AI CLI Invocation Pattern
category: concept
tags: [cli, subprocess, agent, python, invocation]
sources: [raw/시스템 분석 실습/3. Agents subprocess calling.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Python 코드에서 AI CLI 도구(Claude, Codex, Gemini)를 `subprocess.run()`으로 호출하는 체계적 패턴. 터미널에서 직접 실행할 때와 Python 코드에서 실행할 때 프롬프트 전달 방식이 다르며, 에이전트별로 명령 구성 방식이 상이하다.

## How It Works

### 두 가지 호출 방식

**방식 1 — 명령줄 인자 (터미널 직접 실행):**
프롬프트가 명령어의 일부로 전달된다.
```
claude -p "1+1 의 답을 숫자만 말해줘"
```

**방식 2 — stdin 파이프 (Python에서 실행):**
프롬프트가 표준 입력(stdin)으로 전달된다.
```python
subprocess.run(["claude", "-p"], input="프롬프트", capture_output=True, text=True)
```

### subprocess.run() 핵심 파라미터

| 파라미터 | 역할 |
|---|---|
| `input` | 프로세스의 stdin에 문자열을 보내고, 보낸 뒤 stdin을 자동으로 닫는다 |
| `capture_output` | `stdout=PIPE, stderr=PIPE`의 축약형 |
| `text` / `encoding` | 입출력을 bytes 대신 str로 처리 |
| `timeout` | 지정 시간 초과 시 `TimeoutExpired` 예외 발생 |

### 에이전트별 명령 구성 (build_cli_command)

각 에이전트는 프롬프트를 받는 방식과 필수 플래그가 다르다:

- **Claude**: stdin으로 전달, `["claude", "-p", "--output-format", "json"]`
- **Codex**: stdin으로 전달, `["codex", "exec", "--ephemeral", "--json", "--skip-git-repo-check"]`
- **Gemini**: `-p` 인자에 프롬프트 포함 필수 (stdin 전달 불가), `["gemini", "-p", prompt, "--output-format", "json"]`

Gemini는 stdin으로 프롬프트를 전달할 수 없으므로, `use_stdin = prompt if agent != "gemini" else None` 분기가 필요하다.

### CompletedProcess 반환값 처리

`subprocess.run()`은 `CompletedProcess` 객체를 반환한다:

| 속성 | 타입 | 의미 |
|---|---|---|
| `.returncode` | int | 종료 코드 (0 = 성공, 그 외 = 실패) |
| `.stdout` | str | CLI가 출력한 내용 |
| `.stderr` | str | 에러/경고 메시지 |
| `.args` | list | 실행된 명령어 리스트 |

`returncode == 0` 규칙은 Unix/Windows 공통이며, 모든 CLI 도구가 따르는 표준이다.

### JSON 응답 파싱

각 에이전트의 출력 JSON 포맷이 다르다:

```python
# Claude, Gemini: 단일 JSON 객체
response = json.loads(result.stdout)

# Codex: 줄 단위 JSON (JSON Lines 형식)
lines = [json.loads(line) for line in result.stdout.strip().splitlines()]
```

Claude의 응답 JSON에는 `type`, `subtype`, `result`, `session_id`, `total_cost_usd`, `usage` 등의 필드가 포함된다. Gemini는 내부적으로 `gemini-2.5-flash-lite`가 먼저 라우팅한 후 다른 모델을 재호출하는 구조를 가진다.

## Key Properties

- 에이전트마다 프롬프트 전달 방식(stdin vs args)이 다르므로 에이전트별 분기 로직이 필요하다
- `pick_binary()` 함수로 OS 및 에이전트 이름에 따라 실행 바이너리를 결정한다 (Windows에서 Codex/Gemini는 `.cmd` 확장자 필요)
- `build_cli_command()`와 `run_agent()`로 추상화하면 에이전트 교체 시 상위 코드 변경이 최소화된다
- JSON 출력 포맷이 에이전트별로 상이하므로 파싱 단계도 에이전트별로 처리해야 한다
- `--skip-git-repo-check` (Codex): Git 저장소 외부에서도 실행 가능하게 한다
- `timeout` 파라미터 미설정 시 응답이 없으면 무한 대기하므로 반드시 지정한다

## Relationships

- [[subprocess]] (이 패턴의 기반이 되는 Python 표준 라이브러리 모듈)
- [[claude-code]] (Claude CLI 도구, stdin 방식)
- [[codex-cli]] (Codex CLI 도구, stdin 방식, JSON Lines 출력)
- [[gemini-cli]] (Gemini CLI 도구, 명령줄 인자 방식)
- [[agent-session-control]] (세션 재개 및 권한 설정과 연계되는 호출 파라미터)
- [[agentic-coding]] (이 패턴이 활용되는 상위 개발 패러다임)

## Open Questions

- Local 파일 경로를 에이전트에게 전달하는 방법: 제공된 코드만으로는 로컬 파일을 직접 전달할 수 없으며, 파일 내용을 읽어 프롬프트에 삽입하거나 에이전트가 파일 시스템 접근 권한을 가지도록 설정하는 방식이 필요하다
- 에이전트별 JSON 응답 스키마를 통일하는 표준화 레이어가 없으면, 에이전트 교체 시 파싱 코드도 함께 수정해야 한다는 문제가 있다
- Gemini의 내부 라우팅(flash-lite → 다른 모델) 구조가 비용 및 응답 품질에 미치는 영향

## Sources

- raw/시스템 분석 실습/3. Agents subprocess calling.pdf
