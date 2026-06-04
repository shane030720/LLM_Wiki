---
title: Subprocess
category: concept
tags: [python, agent-communication, cli, implementation]
sources: [raw/시스템 분析 실습/3. Agents subprocess calling.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

Python `subprocess` 모듈을 사용하여 하나의 에이전트가 다른 CLI 에이전트를 프로세스로 호출하는 메커니즘. 에이전트 간 통신의 기본 구현 방법이며, `subprocess.run()`을 통해 외부 프로세스를 실행하고 그 결과를 수집한다.

## How It Works

**핵심 함수: `subprocess.run()`**

```python
result = subprocess.run(
    command,           # 실행할 명령어 (리스트 또는 문자열)
    input=stdin_text,  # stdin으로 전달할 텍스트
    capture_output=True,
    text=True,
    timeout=300
)
```

**반환값 (`CompletedProcess`):**
- `result.returncode` — 0이면 성공, 비0이면 오류
- `result.stdout` — 표준 출력 (에이전트 응답)
- `result.stderr` — 표준 오류
- `result.args` — 실행된 명령어

**CLI 에이전트 호출 두 가지 방식:**

| 방식 | 용도 | 예시 |
|------|------|------|
| stdin | 긴 프롬프트, 멀티라인 내용 | `input=prompt_text` |
| 명령행 인수 | 짧고 단순한 지시 | `["claude", "-p", "요약해줘"]` |

**`build_cli_command()` 패턴:**

```python
def build_cli_command(agent_config):
    cmd = ["claude"]
    if agent_config.get("system_prompt"):
        cmd += ["--system-prompt", agent_config["system_prompt"]]
    if agent_config.get("output_format") == "json":
        cmd += ["--output-format", "json"]
    return cmd
```

**`run_agent()` 패턴:**

```python
def run_agent(command, prompt, timeout=300):
    result = subprocess.run(
        command,
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout
    )
    if result.returncode != 0:
        raise AgentError(result.stderr)
    return result.stdout
```

**세션 제어 플래그:**
- `--resume <session_id>` — 이전 대화 세션 재개
- `--dangerously-skip-permissions` (Claude) / `--yolo` (Codex) — 권한 확인 생략
- `--output-format json` — JSON 형식 출력 강제

**JSON 출력 활용:**

```python
output = run_agent(command, prompt)
data = json.loads(output)
next_stage_input = data["result"]
```

## Key Properties

- **단방향 호출** — Orchestrator → Sub-agent 방향; 응답은 stdout으로만 반환
- **격리된 실행** — 각 subprocess 호출은 독립된 프로세스; 상태 공유 없음
- **타임아웃 필수** — 무한 대기 방지를 위해 `timeout` 파라미터 지정 권장
- **에러 처리** — `returncode != 0` 확인 및 `stderr` 로깅 필수

## Limitations

- 프로세스 생성 오버헤드가 있어 고빈도 호출에는 비효율적
- stdin 방식은 매우 긴 프롬프트를 전달할 때 메모리 제한에 걸릴 수 있음
- 세션 유지 없이 매번 새 프로세스를 생성하면 컨텍스트 누적 불가

## Relationships

- [[agentic-coding]] (subprocess로 에이전트 간 통신을 구현하는 실행 메커니즘)
- [[sequential-agent]] (sequential 파이프라인에서 subprocess를 통해 단계별로 에이전트 호출)
- [[parallel-agent]] (subprocess를 병렬로 실행하여 병렬 에이전트 구조 구현)
- [[agent-pool]] (orchestrator가 pool의 에이전트를 subprocess로 동적 호출)
- [[harness-engineering]] (subprocess 실행을 포함한 전체 실행 환경 설계)

## Open Questions

- subprocess 방식 외에 API 호출(HTTP)로 에이전트를 호출하는 방식과의 트레이드오프는?
- 세션 재개(`--resume`) 기능을 파이프라인에서 활용하면 컨텍스트 효율이 얼마나 향상되는가?

## Sources

- raw/3. Agents subprocess calling.pdf
