---
title: System Analysis
category: concept
tags: [system-analysis, requirements, specification, modeling, constraint]
sources: [raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

System Analysis(시스템 분석)란 사용자·운영·비즈니스가 원하는 목표를 도출하고, 시스템의 범위와 제약을 명확화하며, 요구사항을 검증 가능한 모델 및 명세로 변환하고, 제약 내에서 설계 선택을 결정하는 일련의 프로세스이다. 단순한 기능 기술이 아니라 이해관계자의 의도를 구조화된 산출물로 바꾸는 지적 작업이다.

## How It Works

시스템 분석은 다음 네 단계 활동으로 구성된다.

1. **목표 도출(Goal Elicitation)**: 사용자(User), 운영(Operations), 비즈니스(Business) 관점의 목표를 식별하고 우선순위화.
2. **범위 및 제약 명확화(Scope & Constraint Clarification)**: 시스템 경계(안/밖)를 확정하고, 시간·비용·규정·성능 등의 제약 조건을 문서화.
3. **요구사항 모델링(Requirements Modeling)**: 요구사항을 Use Case, BPMN/DFD, ERD 등 형식 모델과 명세(Specification)로 변환하여 검증 가능하게 만듦.
4. **설계 의사결정(Design Decision Making)**: 제약 조건 내에서 우선순위·리스크·대안을 평가하고 선택.

이 과정에서 세 가지 역할이 협력한다.

| 역할 | 책임 |
|------|------|
| 시스템 설계자(System Designer) | 의사 결정 및 책임 |
| 프로젝트 관리자(Project Manager) | 계획 수립 및 관리 |
| 소프트웨어 엔지니어(Software Engineer) | 구현 및 검증 |

## Key Properties

- 검증 가능성(Verifiability): 분석의 결과물은 단순한 텍스트 기술이 아닌 검증 가능한 모델이어야 함
- 이해관계자 지향성: 사용자·운영·비즈니스 모두의 관점을 통합적으로 고려
- 제약 인식: 이상적 요구사항이 아닌 실현 가능한 제약 범위 내의 요구사항을 다룸
- 다중 모델 활용: Use Case, DFD, ERD 등 다양한 표현 도구를 목적에 따라 선택
- 협업 기반: 단일 역할이 아닌 설계자·관리자·엔지니어의 협업으로 수행

## Relationships

- [[system]] (분석의 대상이 되는 시스템)
- [[systems-analyst]] (시스템 분석을 수행하는 전문 역할)
- [[sdlc]] (시스템 분석이 포함되는 전체 개발 생명주기)
- [[feasibility-analysis]] (시스템 분석에 선행하는 타당성 검토)
- [[use-case]] (요구사항 모델링에 사용하는 행위 기반 명세 도구)
- [[data-flow-diagram]] (요구사항 모델링에 사용하는 데이터 흐름 표현 도구)
- [[entity-relationship-diagram]] (요구사항 모델링에 사용하는 데이터 구조 표현 도구)
- [[spec-driven-development]] (명세 기반 개발로 시스템 분석 산출물을 활용하는 패러다임)
- [[business-process-management]] (프로세스 관점의 시스템 분석 모델링과 관련)

## Open Questions

- LLM이 요구사항 모델링 작업을 자동화할 경우, 시스템 분석가의 역할은 어떻게 재정의되어야 하는가?
- Use Case, DFD, ERD 중 어느 모델이 LLM 기반 명세 생성에 가장 적합한가?
- "검증 가능하게 만든다"는 기준을 LLM이 자동으로 판단할 수 있는가?

## Sources

- raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf (p.3~p.5)
