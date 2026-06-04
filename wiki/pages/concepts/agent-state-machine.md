---
title: Agent State Machine
category: concept
tags: [agent, state-machine, agentic-coding, lifecycle, dashboard]
sources: [raw/시스템 분석 실습/6. Agent pool and Orchestrator.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Agent State Machine은 에이전틱 시스템에서 개별 에이전트가 가지는 런타임 상태(state)의 집합과 각 상태 간 전이(transition) 규칙을 정의한 모델이다. 에이전트는 생성부터 종료까지 정해진 상태들을 순서에 따라 거치며, Orchestrator와 대시보드는 이 상태 정보를 통해 에이전트의 현재 상황을 추적한다.

## How It Works

에이전트는 다음 상태들 중 하나를 가진다:

```
[Idle] ──→ [Processing / Running] ──→ [Completed]
                    │
                    └──→ [Failed]
```

| 상태 | 의미 |
|------|------|
| `idle` | 풀에 등록되어 있으나 현재 요청을 처리하지 않는 대기 상태 |
| `processing` / `running` | Orchestrator에 의해 선택되어 subprocess로 실행 중 |
| `completed` | 작업을 성공적으로 마치고 출력을 반환한 상태 |
| `failed` | 오류, 타임아웃(`timeout_seconds`), 최대 시도 횟수 초과(`max_attempts`) 등으로 종료된 상태 |

**상태 전이 트리거:**
- `idle → running`: Orchestrator가 해당 에이전트를 선택하고 subprocess를 생성
- `running → completed`: subprocess가 정상 종료 코드(0)로 출력 반환
- `running → failed`: subprocess가 비정상 종료, 타임아웃, 또는 `max_attempts` 초과

**라운드(Round) 개념:**  
동일 에이전트가 같은 실행 세션 내에서 반복 호출될 수 있다. 각 호출은 라운드 번호로 구분되며, 해당 라운드의 입력과 출력이 이력(history)으로 누적된다.

## Key Properties

- **관찰 가능성(Observability)**: 상태는 대시보드에서 실시간으로 표시되어, 사람이나 상위 Orchestrator가 진행 상황을 모니터링할 수 있다.
- **이력 누적**: 에이전트가 실행될 때마다 라운드 번호와 출력이 이력에 추가된다. 상태가 `completed`로 바뀌어도 이전 라운드 기록은 보존된다.
- **동적 반영**: 에이전트가 풀에 추가되거나 제거되면 상태 테이블이 동적으로 갱신된다.
- **제약 기반 실패**: `constraints.max_attempts`, `constraints.timeout_seconds`는 `failed` 전이의 기준이 된다.
- **상태 독립성**: 각 에이전트의 상태는 독립적으로 관리된다. 한 에이전트의 `failed` 상태가 다른 에이전트를 즉시 중단시키지 않는다(Orchestrator 정책에 따라 다름).

## Relationships

- [[orchestrator]] — 에이전트의 상태 전이를 유발하고 전체 상태를 추적하는 제어 주체
- [[agent-pool]] — 상태를 가지는 에이전트들의 집합
- [[agent-specification]] — `max_attempts`, `timeout_seconds` 등 상태 전이 규칙의 파라미터를 정의하는 스키마
- [[subprocess]] — `idle → running` 전이를 물리적으로 구현하는 실행 메커니즘
- [[agent-session-control]] — 세션 단위에서의 에이전트 제어와 라이프사이클 관리

## Open Questions

- `failed` 상태의 에이전트를 자동으로 `idle`로 복구(retry)하는 전략을 Orchestrator가 결정해야 하는가, 아니면 에이전트 스펙에 명시해야 하는가?
- 동일 에이전트가 병렬로 여러 라운드를 동시에 실행할 경우 상태 모델을 어떻게 확장할 것인가?
- 상태 이력(history)의 보존 기간과 정리(cleanup) 정책은 어떻게 설계하는가?

## Sources

- raw/시스템 분석 실습/6. Agent pool and Orchestrator.pdf
