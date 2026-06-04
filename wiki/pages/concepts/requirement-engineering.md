---
title: Requirement Engineering
category: concept
tags: [requirement, sdlc, system-analysis, software-engineering]
sources: [raw/시스템 분석 실습/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Requirement Engineering은 소프트웨어 시스템이 "무엇을" 해야 하는지를 체계적으로 수집, 분석, 명세, 검증하는 공학적 프로세스다. 단순 도구 개발과 달리, 복잡한 정보 시스템 및 실세계 Embedded 시스템에서는 구체적인 문서화와 이해관계자 간 논의 없이는 그 누구도 제대로 된 시스템을 개발할 수 없다.

## How It Works

요구사항 공학은 다음 활동으로 구성된다:

1. **요구사항 수집(Elicitation)**: 이해관계자(Stakeholder)로부터 실제 필요를 도출한다. 사용자가 명확히 표현하지 못하는 암묵적 요구까지 끌어내는 것이 핵심 난이도다.
2. **요구사항 분석(Analysis)**: 수집된 요구의 충돌, 모호성, 실현 가능성을 검토한다. 단순 도구와 달리 복잡한 시스템에서는 이해관계자가 User, Admin, Operator 등 다수 존재하여 상충이 빈번하다.
3. **요구사항 명세(Specification)**: [[product-requirements-document]](PRD), SRS(Software Requirements Specification) 등의 문서로 구체화한다.
4. **요구사항 검증(Validation)**: Acceptance Criteria를 통해 명세된 요구사항이 실제 이해관계자 필요를 충족하는지 확인한다.

AI Assisted Coding 맥락에서 Vibe Coding의 One-Shot 접근은 체계적 요구사항 없이 시작하는 경향이 있어, 점진적으로 요구사항이 사후에 개선되는 Incremental Requirements 문제가 발생한다. 이를 해결하기 위해 Spec-First 패턴, 즉 코딩 전 PRD 작성이 강조된다.

## Key Properties

- **이해관계자 복잡성**: 단순 도구는 User 1명이지만, 실제 시스템은 User, Admin, Operator 등 다양한 이해관계자를 상정해야 한다
- **기대치 격차**: 단순 도구는 기대치가 낮지만, 복잡한 시스템에서는 이해관계자의 기대치가 극히 높다(Extremely High)
- **비기능적 요구사항(Non-Functional Requirements)**: 단순 도구에서는 없거나 미미하지만, 실제 시스템에서는 성능, 보안, 확장성이 필수 항목으로 등장한다
- **통합/마이그레이션(Integration or Migrations)**: DB, Auth, API 등 외부 시스템과의 연동이 필요하다
- **실패 비용(Failure Costs)**: 복잡한 시스템에서 요구사항 오류는 단순 도구보다 훨씬 높은 비용을 초래한다
- **실제 요구사항 도출의 어려움**: 사용자는 자신이 원하는 것을 명확히 모르거나 잘못 표현하는 경우가 많다

## Relationships

- [[sdlc]] — SDLC의 Analysis 단계에서 요구사항 공학이 수행된다. Analysis는 "무엇이 필요한가"(요구사항 수집, 분석 모델)를 다룬다
- [[product-requirements-document]] — 요구사항 공학의 핵심 산출물이자 LLM과의 협업 입력 문서
- [[spec-driven-development]] — Spec-First 접근으로 요구사항 공학을 AI 협업 워크플로에 적용하는 패턴
- [[feasibility-analysis]] — Planning 단계에서 요구사항의 실현 가능성을 검토하는 선행 활동
- [[system-analysis]] — 요구사항 공학을 포함하는 상위 맥락인 시스템 분석 활동
- [[vibe-coding]] — 체계적 요구사항 없이 진행하는 방식으로, 단순 도구 이상의 시스템에서는 비체계적 개발 문제가 발생한다
- [[agentic-coding]] — Sequential Agent의 태스크 의존관계 설계가 SDLC Analysis 단계의 작업 분해(Task Decomposition)와 동일한 활동이다

## Open Questions

- AI가 요구사항 수집(Elicitation) 인터뷰를 수행하거나 암묵적 요구를 자동 도출할 수 있는 수준은 어디까지인가?
- LLM이 생성한 PRD/SRS의 완결성과 일관성을 어떻게 검증할 것인가?
- Agentic Coding에서 요구사항 변경이 발생할 경우, 이미 실행 중인 Sequential Agent 파이프라인에 어떻게 전파할 것인가?
- 지하철 스크린 도어와 같은 Embedded 시스템의 요구사항은 정보 시스템과 어떻게 다르게 접근해야 하는가?

## Sources

- raw/시스템 분석 실습/2. SDLC pipeline in Vibe coding.pdf
