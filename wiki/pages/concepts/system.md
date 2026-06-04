---
title: System
category: concept
tags: [system, architecture, components, boundary, constraint]
sources: [raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

System(시스템)이란 공통된 목적이나 목표를 달성하기 위해 함께 동작하는, 상호작용하고 상호 연관되거나 상호 의존적인 구성요소들의 집합과 그 상호작용 규칙으로 이루어진 복잡한 통합체이다. 구성요소들은 독립적으로 존재하지 않고 경계(boundary)와 제약(constraint) 안에서 서로 관계를 맺으며 목표 달성에 기여한다.

## How It Works

시스템은 다음 다섯 가지 핵심 요소의 상호작용으로 동작한다.

1. **Goal**: 시스템이 달성하려는 공통 목적. 모든 구성요소의 존재 이유를 정의.
2. **Components**: 시스템을 구성하는 부품들. Builder(개발자, 엔지니어 포함)도 구성요소의 일부로 간주.
3. **Interactions**: 구성요소 간 통신·협력 규칙. 메시지, 데이터 흐름, 의존 관계 등으로 표현.
4. **Boundaries**: 시스템의 안(inside)과 밖(outside)을 구분하는 경계. 무엇이 시스템에 속하고 무엇이 외부 환경인지를 명확히 함.
5. **Constraints**: 시스템 운영을 제한하는 조건. 시간, 비용, 규정, 성능 요구사항 등이 포함.

소프트웨어 엔지니어 자신도 기업 시스템의 Component의 일부로 작동하며, 엔지니어의 산출물은 시스템이 목표를 달성하도록 돕는 포괄적인 Solution으로 평가된다.

## Key Properties

- 목적 지향성(purposeful): 시스템은 반드시 달성하려는 목표를 가짐
- 전체성(wholeness): 구성요소들의 합 이상의 창발적 특성이 존재
- 경계 명확성: 내부와 외부를 구분해야 분석 및 설계가 가능
- 제약 내 동작: 시스템은 항상 특정 제약(시간, 비용, 성능, 규정) 안에서 운영됨
- Builder 포함성: 시스템을 만드는 주체(엔지니어, 팀)도 시스템의 구성요소로 취급 가능

## Relationships

- [[system-analysis]] (이 시스템을 이해하고 명세화하는 프로세스)
- [[systems-analyst]] (시스템을 분석하는 역할을 수행하는 사람)
- [[sdlc]] (시스템을 개발하고 유지하는 전체 생명주기)
- [[feasibility-analysis]] (시스템 구현 가능성을 판단하는 초기 분석)
- [[entity-relationship-diagram]] (시스템 내 데이터 구조를 모델링하는 도구)
- [[data-flow-diagram]] (시스템 내 데이터 흐름을 모델링하는 도구)

## Open Questions

- 소프트웨어 엔지니어가 시스템의 Component라면, 엔지니어가 AI 에이전트로 대체될 경우 시스템의 경계와 목표 정의는 어떻게 달라지는가?
- Boundary를 어디에 설정하느냐에 따라 동일한 실체가 내부 구성요소가 될 수도 있고 외부 행위자(actor)가 될 수도 있다. 이 결정의 기준은 무엇인가?

## Sources

- raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf (p.3)
