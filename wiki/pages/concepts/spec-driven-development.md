---
title: Spec-Driven Development
category: concept
tags: [coding-paradigm, requirements, vibe-coding, best-practice]
sources: [raw/시스템 분析 실습/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

"Spec First, Code Later" 원칙에 따라 코드 작성 이전에 요구사항 명세를 먼저 완성하는 개발 방법론. 바이브 코딩의 효과를 극대화하는 베스트 프랙티스이며, PRD → SRS → User Story 순서로 Why → What → How를 달성한다.

## How It Works

1. **PRD 작성** — Product Requirements Document를 먼저 작성 (코딩 시작 전)
2. **AI와 협업하여 Plan 수립** — PRD와 단계별 계획을 AI와 함께 만들어 의도를 맞추고 작업 분해
3. **SRS 작성** — Software Requirements Spec을 통해 SW요구사항 명세를 LLM과 논의
4. **User Story 산출** — PRD와 수용 기준(Acceptance Criteria)이 포함된 User Story 도출
5. **Why → What → How 달성** — 이 순서를 통해 코딩에 진입

**Case 예시 (Quick Sort Viewer):**
- Target User: 정렬 알고리즘은 이해하지만 Randomized Quicksort를 모르는 학습자
- Key Feature: 상세 로그, O(n log n) 시각적 추적, 단계별 실행
- Constraint: 브라우저 기반, 단일 HTML 파일
- Acceptance Criteria: 사용자가 pivot 선택의 무작위성이 최악 케이스를 방지하는 원리를 이해할 수 있어야 함

## Key Properties

- **Project Manager처럼 일하기** — 개발자가 코드 대신 명세를 먼저 작성하며 PM 역할 수행
- **Incremental Requirements 대응** — 점진적으로 요구사항이 개선되는 상황에서 비체계적 개발을 방지
- **LLM 출력 품질 향상** — 간단한 PRD 요소를 프롬프트에 포함시키면 결과물 품질이 월등히 향상됨
- **작업 분해** — PRD를 기반으로 에이전트 태스크를 명확히 분해 가능

## Limitations

- PRD/SRS 작성에 추가 시간이 필요하여 빠른 프로토타이핑 속도를 저해할 수 있음
- 작은 규모의 일회성 도구에는 과도한 오버헤드가 될 수 있음

## Relationships

- [[vibe-coding]] (spec-driven development로 효과를 높이는 베이스 패러다임)
- [[sdlc]] (spec-driven development가 SDLC의 Analysis/Design 단계를 실천하는 방식)
- [[agentic-coding]] (spec을 에이전트에게 전달하여 체계적 구현을 달성)
- [[plan-mode]] (spec 생성 후 plan-mode로 전환하여 구현 전 검토)

## Open Questions

- PRD 없이 에이전트와 대화하며 실시간으로 요구사항을 수집하는 것이 가능한가?
- 매우 빠르게 변화하는 요구사항 환경에서 SRS의 유효 기간은 얼마나 되는가?

## Sources

- raw/2. SDLC pipeline in Vibe coding.pdf
