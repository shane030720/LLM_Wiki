---
title: Planner-Reviewer Pipeline
category: concept
tags: [agent, pipeline, planner, reviewer, multi-agent, ping-pong, quality-gate]
sources: [raw/시스템 분석 실습/5. Agent Specifications.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Planner-Reviewer Pipeline은 Planner(AGENT1)와 Reviewer(AGENT2) 두 개의 전문화된 에이전트가 점수 기반 핑퐁(ping-pong) 메커니즘으로 계획을 반복 정제하는 멀티 에이전트 파이프라인 패턴이다. Reviewer가 일정 점수 이상을 부여할 때까지 Planner가 계획을 수정하는 루프가 반복되며, 품질 게이트를 통과한 결과물만 최종 출력으로 승인된다.

## How It Works

### AGENT1 — Planner

입력 프롬프트를 받아 세 단계를 순서대로 수행한다.

| 단계 | 역할 |
|------|------|
| Step 1. Analysis | 요청을 읽고 목표(Goal)와 기술적 제약(Constraints)을 판단 |
| Step 2. Decomposition | 목표를 실현 가능한 단위로 분해하고 실행 순서·의존성을 결정 |
| Step 3. Planning | 각 TODO에 입력, 출력, 구현 방법, 완료 기준(Acceptance Criteria)을 구체화 |

출력물: `Plan.md` (전체 계획), `TODO.md` (AC가 포함된 태스크 목록)

### AGENT2 — Reviewer

Planner의 출력을 받아 세 단계를 순서대로 수행한다.

| 단계 | 역할 |
|------|------|
| Step 1. Validation | 모든 TODO에 입력/출력/AC가 있는지, 누락 항목이 있는지 확인 |
| Step 2. Review | 기술적 구현 가능성, 의존성 순서, 모호한 부분 평가 |
| Step 3. Revise | 1~10점 점수와 구체적 개선사항을 항목별로 작성 |

출력물: `REVIEW.md` (점수 + 개선사항)

### 핑퐁 루프 (Ping-Pong Loop)

```
User Prompt
    → AGENT1 (Planner) → Plan.md + TODO.md
    → AGENT2 (Reviewer) → REVIEW.md (점수 + 개선사항)
    → [점수 < 8] → AGENT1이 REVIEW.md를 참고해 재계획
    → Revised_Plan.md + Final_TODO.md
    → [점수 >= 8] → 파이프라인 종료, 최종 출력 승인
```

실습에서는 첫 번째 평가를 무조건 7점 이하로 제한하여 최소 한 번의 재계획 사이클을 보장한다.

### 확장: Planner-Reviewer-Coder-Tester

기본 2-에이전트 파이프라인은 Coder와 Tester 에이전트를 추가하여 4단계 파이프라인으로 확장 가능하다.

```
Planner → Reviewer → Coder → Tester
```

각 에이전트는 독립적인 [[agent-specification]]을 가지며, Hand-Off 파일을 통해 이전 단계의 출력을 다음 단계의 입력으로 전달한다.

## Key Properties

- **점수 기반 품질 게이트**: 10점 척도에서 8점 이상이어야 다음 단계로 진행 (threshold-gated quality control)
- **명시적 출력 계약**: 각 에이전트의 출력이 파일(`Plan.md`, `TODO.md`, `REVIEW.md`, `Revised_Plan.md`, `Final_TODO.md`)로 고정되어 핸드오프 오류를 최소화
- **역할 분리**: 생성(Planner)과 검증(Reviewer)을 분리함으로써 자기 검증 편향(self-review bias)을 줄임
- **수렴 보장**: 점수 임계값이 명확하여 루프 종료 조건이 결정적
- **확장성**: Coder·Tester 등 단계를 추가하여 전체 소프트웨어 개발 파이프라인으로 성장 가능

## Relationships

- [[agent-specification]] (Planner와 Reviewer 각각의 System Prompt·Context·Inputs·Outputs를 이 구조로 정의)
- [[plan-mode]] (Planner의 Analysis→Decomposition→Planning 단계는 Plan-Mode 워크플로우와 구조적으로 동일)
- [[pipeline-design-patterns]] (Planner-Reviewer Pipeline은 이 일반 패턴의 구체적 구현체)
- [[sequential-agent]] (Planner→Reviewer의 순차 실행 구조가 sequential agent 패턴을 따름)
- [[contract-driven-iteration]] (AC 기반 TODO 명세와 반복 정제는 contract-driven iteration의 원칙을 적용)
- [[spec-driven-development]] (Plan.md와 TODO.md의 명시적 명세가 spec-driven 접근과 연결)

## Open Questions

- 핑퐁 루프에서 수렴하지 않을 경우(예: Reviewer가 계속 낮은 점수를 부여할 경우) 최대 반복 횟수를 어떻게 설정해야 하는가?
- Reviewer의 첫 평가를 강제로 7점 이하로 제한하는 방식이 실제 품질 향상에 기여하는가, 아니면 형식적 반복을 유발하는가?
- Planner-Reviewer-Coder-Tester 4단계 파이프라인에서 Coder 단계 실패 시 Planner로 피드백을 되돌리는 역방향 루프가 필요한가?
- 점수 임계값(8점)은 어떤 근거로 결정하며, 태스크 복잡도에 따라 동적으로 조정해야 하는가?

## Sources

- raw/시스템 분석 실습/5. Agent Specifications.pdf
