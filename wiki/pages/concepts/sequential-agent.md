---
title: Sequential Agent
category: concept
tags: [agent-pattern, pipeline, multi-agent, workflow]
sources: [raw/시스템 분析 실습/4. Plan_mode Sequential and Parallel agents.pdf, raw/5. Agent Specifications.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

이전 에이전트의 완료를 기다린 후 다음 에이전트가 실행되는 직렬 파이프라인 구조. 각 에이전트의 출력이 다음 에이전트의 입력이 되며, 작업 간 의존 관계가 명확할 때 적합하다.

## How It Works

**기본 구조:**

```
Input → [Agent A] → [Agent B] → [Agent C] → Output
         (완료 대기)  (완료 대기)
```

**파이프라인 단계 예시 (PRD → 구현):**

```
[Planner]         → 00_planning.md
[Reviewer]        → 01_review.md
[Reviser]         → 02_revision.md
[Implementer]     → 03_code/
[Tester]          → 04_test_report.md
```

**Python 구현 패턴:**

```python
def run_sequential_pipeline(stages, initial_input):
    current_input = initial_input
    for stage in stages:
        result = run_agent(stage["command"], current_input)
        write_handoff(stage["output_file"], result)
        current_input = result
    return current_input
```

**의존 관계 설계 원칙:**
- 각 단계의 입력/출력을 사전에 명확히 정의 (Agent Spec)
- 단계 순서는 SDLC Analysis 단계에서 결정
- 단계 실패 시 재시도 로직 필요 (`max_attempts` 설정)

## Key Properties

- **결정론적 실행 순서** — 항상 동일한 순서로 실행되어 예측 가능
- **컨텍스트 누적** — 각 단계의 결과가 다음 단계의 컨텍스트를 풍부하게 함
- **디버깅 용이** — 어느 단계에서 오류가 발생했는지 즉시 식별 가능
- **의존 관계 강제** — B가 A의 결과를 반드시 필요로 할 때 적합

## Limitations

- 총 실행 시간 = 각 단계 시간의 합 (병렬 처리 불가)
- 앞 단계의 오류가 전체 파이프라인을 멈춤
- 독립적인 작업을 순차 처리하면 비효율

## Relationships

- [[parallel-agent]] (독립 작업에서 sequential의 비효율을 극복하는 대안)
- [[handoff]] (sequential 파이프라인에서 단계 간 데이터를 전달하는 메커니즘)
- [[agent-pool]] (orchestrator가 sequential 파이프라인의 각 단계 에이전트를 pool에서 선택)
- [[agentic-coding]] (sequential agent가 SDLC 단계별 실행을 구현하는 구조)
- [[subprocess]] (Python에서 sequential 파이프라인의 각 단계를 subprocess로 실행)

## Open Questions

- Sequential 파이프라인에서 특정 단계를 조건부로 건너뛰는 패턴은?
- 단계 실패 시 이전 단계로 롤백하는 메커니즘을 어떻게 구현하는가?

## Sources

- raw/4. Plan_mode Sequential and Parallel agents.pdf
- raw/5. Agent Specifications.pdf
