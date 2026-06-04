---
title: Use Case
category: concept
tags: [use-case, requirements, systems-analysis, actor, event-driven]
sources: [raw/시스템분석/ch04-2.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Use Case는 시스템이 외부 환경과 상호작용하는 방식을 표현하는 요구사항 분석 도구다. 외부 사용자(actor)가 특정 이벤트를 발생시키면 시스템이 그에 응답하는 일련의 활동을 기술하며, 사용자 관점에서 기능 요구사항을 명확히 하는 데 사용된다. 모든 시스템 동작을 트리거 이벤트에 대한 응답으로 바라보는 event-driven modeling의 핵심 표현 수단이다.

## How It Works

1. **이벤트 식별**: 시스템이 응답해야 하는 이벤트를 Event-Response List로 먼저 정리한다.
2. **Use Case 작성**: 복잡한 이벤트에 대해 use case 양식을 작성한다.
3. **주요 단계 정의**: 각 use case별로 normal course(주 흐름)를 구성하는 주요 단계를 식별한다.
4. **입출력 명세**: 각 단계의 입력과 출력 요소를 식별한다.
5. **사용자 검증**: role-playing을 통해 사용자와 함께 use case를 확인한다.
6. **기능 요구사항 도출**: use case의 내용을 바탕으로 개발자 관점의 functional requirements를 작성한다.

Use case는 종종 순서(sequence)를 갖고 연속으로 수행되며, 단일 use case가 지나치게 커지지 않도록 초기 상태(initial state)와 종료 상태(ending state)를 명확히 정의해야 한다.

## Key Properties

- **Name / Number**: 각 use case는 고유한 이름과 번호, 간략한 설명을 가진다.
- **Priority**: 상대적 중요도를 나타내는 우선순위를 지정할 수 있다.
- **Actor**: 시스템과 상호작용하는 사람, 다른 시스템, 또는 하드웨어 장치.
- **Trigger**: use case를 시작시키는 이벤트로, external trigger(외부 발생)와 temporal trigger(시간 기반)로 구분된다.
- **Normal Course**: 이벤트에 대한 응답을 실행하기 위한 주요 단계들의 흐름.
- **Preconditions**: 해당 use case가 시작되기 전에 완료되어야 하는 조건.
- **Postconditions**: 해당 use case가 종료될 때 완료된 상태에 대한 정의.
- **사용자 가독성**: 텍스트 기반으로 작성되어 사용자가 이해하기 쉽다.
- **점진적 정제(Gradual Refinement)**: 처음부터 완벽하게 작성하기보다 반복적으로 세부화한다.

## Relationships

- [[use-case-formats]] — casual format과 fully-dressed format 등 use case의 상세 수준별 작성 형식
- [[functional-requirements]] — use case로부터 도출되는 개발자 관점의 기능 요구사항
- [[event-response-list]] — use case 작성의 선행 단계로, 시스템이 응답해야 할 이벤트 목록
- [[process-model]] — use case는 프로세스 모델 작성으로 자연스럽게 이어진다
- [[data-model]] — use case 분석은 데이터 모델 작성의 기초가 된다

## Open Questions

- 단순한 이벤트에는 use case 작성이 불필요하다고 명시되어 있으나, "단순함"의 기준이 구체적으로 제시되지 않는다. 실무에서 어느 수준부터 use case를 작성해야 하는가?
- Use case는 사용자 관점만 반영하며, 개발자 관점으로의 변환은 시스템 분석가의 역할이라고 강조된다. 이 변환 과정에서 발생하는 해석 오류를 최소화하는 방법은 무엇인가?
- Event-driven modeling 이외의 패러다임(예: 데이터 흐름 중심 모델링)과 use case를 병행할 때 충돌이 발생할 수 있는가?

## Sources

- raw/시스템분석/ch04-2.pdf — Dennis, Wixom, Roth, *Systems Analysis and Design*, 2019, Chapter 4-2: Use Case Analysis
