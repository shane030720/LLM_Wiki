---
title: Parallel Agent
category: concept
tags: [agent-pattern, multi-agent, performance, workflow]
sources: [raw/시스템 분析 실습/4. Plan_mode Sequential and Parallel agents.pdf, raw/5. Agent Specifications.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

여러 에이전트가 동일한 입력을 동시에 처리하거나 독립적인 작업을 병렬로 수행하는 구조. 총 실행 시간이 가장 오래 걸리는 단계의 시간으로 결정되어 sequential 대비 처리 속도가 향상된다.

## How It Works

**두 가지 병렬 패턴:**

**패턴 1: 동일 입력 병렬 처리 (Fan-out)**
```
Input → [Agent A]  ↘
        [Agent B]  → Aggregator → Output
        [Agent C]  ↗
```
예: 같은 문서를 다국어로 동시 번역, 동일 코드베이스를 여러 측면으로 동시 분석

**패턴 2: 독립 작업 병렬 처리**
```
[Task A] → [Agent A] ↘
[Task B] → [Agent B] → 합산 → Output
[Task C] → [Agent C] ↗
```
예: 여러 PDF를 동시에 처리, 독립적인 모듈을 동시에 구현

**Python 구현 패턴:**

```python
import concurrent.futures

def run_parallel_agents(tasks):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(run_agent, task["command"], task["input"]): task
            for task in tasks
        }
        results = {}
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            results[task["id"]] = future.result()
    return results
```

**Research 활용 예시 (WebSearch 병렬화):**
```
[Query 1: "agentic coding"]  → [Agent 1] ↘
[Query 2: "vibe coding"]     → [Agent 2] → 결과 통합
[Query 3: "SDLC pipeline"]   → [Agent 3] ↗
```

**결과 집계 (Aggregator):**
- 단순 병합: 모든 결과를 하나의 문서로 concat
- 최선 선택: 여러 결과 중 품질 기준으로 최적 선택
- 투표: 다수결로 최종 결과 결정

## Key Properties

- **성능 향상** — 독립적 N개 작업을 1/N 시간에 처리
- **탐색 다양성** — 동일 문제를 다양한 관점으로 동시 탐색
- **장애 격리** — 한 에이전트 실패가 다른 에이전트에 영향 없음
- **집계 필요** — 결과를 통합하는 Aggregator 단계가 반드시 필요

## Limitations

- 에이전트 간 작업이 완전히 독립적일 때만 효과적
- 결과 집계 로직이 복잡해질 수 있음
- 동시 실행으로 인한 API 요청 제한(Rate Limit) 초과 위험
- 공유 자원(동일 파일)에 동시 쓰기 시 race condition 발생

## Relationships

- [[sequential-agent]] (의존 관계가 있을 때 parallel의 대안)
- [[agent-pool]] (orchestrator가 pool에서 병렬 실행할 에이전트를 동적으로 선택)
- [[subprocess]] (Python threading/multiprocessing으로 subprocess를 병렬 실행)
- [[agentic-coding]] (병렬 에이전트로 대규모 작업을 효율적으로 처리)
- [[harness-engineering]] (병렬 실행의 동기화와 집계를 harness가 담당)

## Open Questions

- 병렬 에이전트의 결과 품질이 불균일할 때 최적의 집계 전략은?
- 병렬 실행 수(worker count)를 동적으로 조정하는 기준은?

## Sources

- raw/4. Plan_mode Sequential and Parallel agents.pdf
- raw/5. Agent Specifications.pdf
