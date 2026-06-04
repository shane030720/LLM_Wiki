---
title: 멀티 에이전트 파이프라인 설계 패턴 비교
category: synthesis
tags: [agent-pattern, pipeline, design, comparison]
sources: [raw/시스템 분析 실습/4. Plan_mode Sequential and Parallel agents.pdf, raw/5. Agent Specifications.pdf, raw/7. Harness and Skills.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Thesis

멀티 에이전트 파이프라인 설계에서 Sequential, Parallel, Orchestrator-Workers, Ping-Pong의 네 가지 핵심 패턴은 작업의 의존성과 품질 목표에 따라 선택된다. 이 패턴들은 조합 가능하며, 대부분의 실제 시스템은 두 개 이상의 패턴을 혼합한다.

## Evidence

**Sequential 패턴의 강점:**
- 단계 간 의존 관계가 명확할 때 유일한 선택 (B가 A의 결과를 반드시 필요로 하는 경우)
- Handoff 파일로 중간 산출물이 보존되어 디버깅과 감사가 용이
- SDLC의 Planning→Analysis→Design→Implementation 흐름을 자연스럽게 표현
- Three-Agent Harness (Planner→Reviewer→Implementer)가 대표적 적용 사례

**Parallel 패턴의 강점:**
- 독립적인 N개 작업을 1/N 시간에 처리
- 동일 문제를 다양한 관점으로 탐색할 때 (Fan-out)
- WebSearch처럼 I/O 병목이 있는 작업에서 효과 극대화
- Rate Limit와 Race Condition 관리가 핵심 과제

**Orchestrator-Workers의 강점:**
- 작업 규모가 동적으로 변할 때 유연하게 대응
- Agent Pool과 결합하면 에이전트 추가·제거가 파이프라인 수정 없이 가능
- 실패한 Worker를 Orchestrator가 감지하고 대체 에이전트 투입 가능

**Ping-Pong (Evaluator-Optimizer)의 강점:**
- 주관적 품질 기준(8/10 이상)을 만족할 때까지 자동 반복
- 생성과 평가를 분리하여 각 에이전트가 전문화된 역할 수행
- Contract-Driven Iteration과 결합하면 Done-when 달성까지 자동 루프

## Counterevidence

- Ping-Pong은 수렴하지 않으면 무한 루프 위험 → max_attempts 필수
- Parallel은 결과 집계(Aggregator) 복잡도가 과소평가되는 경향 — 집계 로직이 파이프라인 전체 품질을 좌우함
- Orchestrator-Workers에서 Orchestrator에 과도한 부담이 집중되면 단일 장애점(SPOF)이 됨
- Sequential이 단순해 보이지만 앞 단계 오류가 전체를 멈추는 취약점이 있음

## Conclusion

**패턴 선택 가이드:**

| 상황 | 권장 패턴 |
|------|-----------|
| A의 결과를 B가 반드시 필요로 함 | Sequential |
| 작업들이 서로 독립적 | Parallel |
| 작업 수가 동적으로 결정됨 | Orchestrator-Workers |
| 품질 기준을 충족할 때까지 반복 | Ping-Pong |
| 계획→검토→구현 3단계 | Three-Agent Harness (Sequential의 특수형) |

**가장 많이 사용되는 조합:**
1. `Sequential + Ping-Pong` — 각 단계 내에서 품질을 보장하며 진행
2. `Parallel + Sequential` — 병렬 수집 후 순차 처리 (Research → Write)
3. `Orchestrator-Workers + Agent Pool` — 동적 규모 조정이 필요한 대형 파이프라인

핵심 원칙: **Handoff 파일로 단계를 분리하고, Harness로 실행 환경을 구조화하면 어떤 패턴 조합도 유지보수 가능한 형태로 구현할 수 있다.**

## Sources

- raw/4. Plan_mode Sequential and Parallel agents.pdf
- raw/5. Agent Specifications.pdf
- raw/7. Harness and Skills.pdf
