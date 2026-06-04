---
title: Agentic Coding Patterns
category: concept
tags: [agent-pattern, design-pattern, coding-paradigm, best-practice]
sources: [raw/시스템 분析 실습/7. Harness and Skills.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전틱 코딩 환경에서 반복적으로 사용되는 구조화된 에이전트 협업 패턴의 집합. 기본 5가지 패턴과 코딩 특화 4가지 패턴으로 구성되며, 문제 유형에 따라 적합한 패턴을 선택하여 적용한다.

## How It Works

### 기본 5가지 패턴 (Basic Patterns)

**1. Prompt Chaining**
```
Input → [A] → [B] → [C] → Output
```
이전 에이전트 출력을 다음의 입력으로 연결. 복잡한 작업을 단순한 단계로 분해.

**2. Routing**
```
Input → [Router] → [Agent A] (조건 1)
                 → [Agent B] (조건 2)
                 → [Agent C] (조건 3)
```
입력 분류 후 적합한 전문 에이전트로 라우팅.

**3. Parallelization**
```
Input → [Agent 1] ↘
        [Agent 2] → [Aggregator] → Output
        [Agent 3] ↗
```
독립적인 작업을 동시에 처리하여 성능 향상.

**4. Orchestrator-Workers**
```
[Orchestrator] → 작업 분해
              → [Worker 1] → 결과 수집
              → [Worker 2]
              → [Worker 3]
              → 결과 통합
```
Orchestrator가 작업을 분해하고 Worker들을 동적으로 관리.

**5. Evaluator-Optimizer**
```
[Generator] → 초안 → [Evaluator] → 점수
                  ↗      |
                  ←──── 피드백 (점수 미달 시)
```
생성과 평가를 반복하여 품질 향상. Ping-Pong의 기반 패턴.

### 코딩 특화 4가지 패턴 (Coding Patterns)

**EPCC (Explore → Plan → Code → Commit)**
```
[Explore] 코드베이스 탐색
  → [Plan] 구현 계획 수립
  → [Code] 구현
  → [Commit] 커밋
```
체계적 코딩 워크플로. Spec-Driven Development와 연계.

**TDD (Test-Driven Development)**
```
[Test Writer] 실패하는 테스트 작성
  → [Implementer] 테스트 통과 코드 작성
  → [Refactorer] 코드 정리
```
테스트를 먼저 작성하여 구현을 주도.

**Visual Iteration**
```
[Generator] UI 생성
  → [Screenshot] 스크린샷 캡처
  → [Evaluator] 시각적 평가
  → 반복 (품질 충족 시 종료)
```
UI 컴포넌트를 시각적으로 평가하며 반복 개선.

**Three-Agent Harness**
```
[Planner]     계획 수립 → 00_planning.md
[Reviewer]    계획 검토 → 01_review.md
[Implementer] 계획 실행 → 코드
```
계획-검토-실행 3단계를 전담 에이전트로 분리.

### Ping-Pong 패턴

Evaluator-Optimizer의 특수 형태로 두 에이전트가 품질 임계값 달성까지 반복 교환:

```
[Generator] → 초안
[Reviewer]  → 점수 + 피드백 (8/10 미만)
[Generator] → 개선본
[Reviewer]  → 점수 + 피드백 (8/10 이상 → 완료)
```

## Key Properties

- **패턴 조합 가능** — 기본 패턴을 조합하여 복잡한 워크플로 구성
- **문제 유형별 선택** — 각 패턴이 특정 문제 구조에 최적화
- **재사용 가능한 블루프린트** — 패턴 이름으로 팀 내 설계 의사소통 단순화

## Relationships

- [[sequential-agent]] (Prompt Chaining이 Sequential Agent의 구현 패턴)
- [[parallel-agent]] (Parallelization 패턴의 구조적 기반)
- [[agent-pool]] (Orchestrator-Workers 패턴에서 pool 개념과 연계)
- [[harness-engineering]] (Three-Agent Harness가 harness 설계의 구체적 패턴)
- [[plan-mode]] (EPCC 패턴의 Plan 단계가 Plan Mode와 대응)
- [[contract-driven-iteration]] (Evaluator-Optimizer / Ping-Pong이 contract 루프의 구현)

## Open Questions

- 이 패턴들을 자동으로 선택하는 메타-Orchestrator 설계는 가능한가?
- 패턴 조합의 복잡도가 증가할수록 디버깅 어려움을 어떻게 완화하는가?

## Sources

- raw/7. Harness and Skills.pdf
