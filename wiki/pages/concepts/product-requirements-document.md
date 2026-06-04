---
title: Product Requirements Document (PRD)
category: concept
tags: [requirement, documentation, sdlc, vibe-coding, agentic-coding]
sources: [raw/시스템 분석 실습/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Product Requirements Document(PRD)는 소프트웨어 제품이 무엇을 해야 하는지를 Why → What → How 순서로 기술하는 요구사항 명세 문서다. AI Assisted Coding 시대에서는 코딩을 시작하기 전에 PRD를 먼저 작성하고 LLM과 공유함으로써 개발 의도를 정렬하고 작업을 분해하는 Spec-First 접근의 핵심 산출물로 활용된다.

## How It Works

PRD는 다음 핵심 구성 요소를 포함한다:

- **Target User**: 이 제품을 사용하는 대상 사용자를 구체적으로 정의한다. (예: "정렬 알고리즘은 이해하지만 Randomized Quicksort를 모르는 학습자")
- **Key Features**: 제품이 반드시 제공해야 하는 핵심 기능 목록. (예: 상세 로그, O(n log n) 시각적 추적, 단계별 실행)
- **Constraints**: 기술적·비즈니스적 제약조건. (예: 브라우저 기반, 단일 HTML 파일)
- **Acceptance Criteria**: 사용자가 요구사항이 충족되었다고 판단하는 구체적인 기준. (예: "사용자가 pivot 선택의 무작위성이 최악 케이스를 방지하는 원리를 이해할 수 있어야 함")

AI 협업 워크플로에서 PRD는 다음 순서로 활용된다:

1. AI와 협업하여 PRD와 단계별 계획(Plan)을 먼저 작성하여 의도를 맞춘다
2. SRS(Software Requirements Specification)를 작성하여 SW 요구사항 명세를 LLM과 논의한다
3. Acceptance Criteria가 포함된 User Story를 산출한다
4. 완성된 PRD를 프롬프트에 포함시켜 LLM에게 전달하면, 단순 자연어 프롬프트 대비 월등히 향상된 결과물이 생성된다

## Key Properties

- **Why → What → How 흐름**: 비즈니스 목적(Why)에서 기능 정의(What), 구현 방향(How)으로 이어지는 논리적 계층 구조를 갖는다
- **LLM 컨텍스트 정렬 효과**: PRD를 프롬프트에 포함하면 LLM이 개발 의도를 정확히 파악하여 결과물 품질이 크게 향상된다
- **작업 분해(Task Decomposition)**: Agentic Coding에서 Sequential Agent의 태스크 의존관계 설계와 동일한 역할을 수행한다. PRD가 곧 파이프라인 설계도다
- **Acceptance Criteria의 범위**: 단순한 기능 완성 여부를 넘어 "사용자가 이해할 수 있어야 함"과 같은 학습·비즈니스 목표까지 포함할 수 있다
- **SRS와의 관계**: PRD가 제품 수준의 요구사항을 기술한다면, SRS(Software Requirements Specification)는 SW 구현 수준의 기술 명세까지 포함한다

## Relationships

- [[requirement-engineering]] — PRD는 요구사항 공학의 Specification 단계에서 생성되는 핵심 산출물이다
- [[spec-driven-development]] — Spec-First 패턴에서 PRD를 코딩 전에 먼저 작성하는 접근법의 중심 문서
- [[sdlc]] — PRD는 SDLC의 Planning 및 Analysis 단계 산출물로, System Request의 Business Requirements를 구체화한 것이다
- [[agentic-coding]] — Agentic Coding에서는 PRD/SRS를 적절한 프롬프트와 함께 각 에이전트에 전달하여 구조화된 개발을 수행한다
- [[vibe-coding]] — Vibe Coding에서도 PRD 요소를 프롬프트에 포함할수록 결과물이 개선됨이 실증되었다
- [[sequential-agent]] — PRD에서 정의된 Key Features와 단계별 계획이 Sequential Agent의 의존관계 설계 입력이 된다

## Open Questions

- PRD의 상세 수준(granularity)은 프로젝트 규모에 따라 어떻게 달라져야 하는가?
- LLM이 인터뷰·대화를 통해 PRD를 자동 생성할 때 누락되기 쉬운 요소는 무엇인가?
- Acceptance Criteria를 자동으로 테스트 케이스로 변환하는 파이프라인이 실용적으로 가능한가?
- PRD와 SRS 사이의 경계를 어떻게 설정해야 AI 협업에 최적화될 수 있는가?

## Sources

- raw/시스템 분석 실습/2. SDLC pipeline in Vibe coding.pdf
