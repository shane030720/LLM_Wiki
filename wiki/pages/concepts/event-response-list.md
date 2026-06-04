---
title: Event-Response List
category: concept
tags: [systems-analysis, use-case, requirement, event]
sources: [raw/시스템 분석 이론/ch04-2.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Event-Response List는 시스템이 반응해야 하는 모든 이벤트(event)를 식별하고 목록화한 아티팩트(artifact)로, use case 작성 전 단계에서 시스템의 범위와 기능적 요구사항을 파악하기 위해 사용된다. 각 이벤트는 시스템이 응답해야 할 외부 자극 또는 시간적 조건을 나타낸다.

## How It Works

1. 시스템 분석가는 시스템 환경에서 발생할 수 있는 모든 이벤트를 식별한다.
2. 이벤트는 **외부 트리거(external trigger)** (사용자나 외부 시스템이 발생시킴)와 **시간적 트리거(temporal trigger)** (특정 시간이나 기간에 의해 발생)로 분류된다.
3. 이벤트 목록이 완성되면, 단순한 이벤트는 별도 use case 없이 처리하고, 복잡한 이벤트에 대해서만 개별 use case를 작성한다.
4. 각 use case는 해당 이벤트에 대한 시스템의 응답을 상세히 기술한다.
5. 분석 과정에서 발견된 새로운 이벤트는 목록에 추가하고, 기능적 요구사항을 지속적으로 수정한다.

## Key Properties

- 이벤트 중심 모델링(event-driven modeling)의 핵심 도구로, 시스템 내 모든 것은 트리거 이벤트에 대한 응답으로 간주된다.
- Use case 작성의 전제 조건(precondition)으로 기능하며, 분석 범위를 명확히 한다.
- 단순 이벤트와 복잡 이벤트를 구분함으로써 불필요한 use case 작성을 방지한다.
- 기능적 요구사항 도출의 입력값 역할을 한다.
- 시스템 분석가가 사용자 관점을 개발자 관점으로 변환하는 기반 자료가 된다.

## Relationships

- [[use-case]] — Event-Response List에서 식별된 복잡 이벤트 각각에 대해 use case가 작성된다.
- [[use-case-formats]] — 이벤트의 복잡도에 따라 casual 또는 fully-dressed 포맷의 use case를 선택한다.
- [[requirement-engineering]] — Event-Response List는 기능적 요구사항을 더욱 완전하게 기술하기 위한 요구공학 활동의 일부이다.
- [[functional-dependency]] — 도출된 기능적 요구사항은 개발자에게 시스템이 수행해야 할 동작을 구체적으로 전달한다.
- [[system-analysis]] — 시스템 분석 활동 중 이벤트 식별 단계에서 생성되는 아티팩트이다.

## Open Questions

- 이벤트 목록의 완전성(completeness)을 보장하기 위한 체계적인 방법은 무엇인가?
- 대규모 시스템에서 수백 개의 이벤트를 효과적으로 관리하기 위한 도구나 프로세스는 어떻게 구성해야 하는가?
- Agile 방법론([[agile-development-methodology]])에서도 Event-Response List가 유용하게 활용될 수 있는가, 아니면 전통적 방법론([[structured-systems-development]])에 더 적합한가?

## Sources

- raw/시스템 분석 이론/ch04-2.pdf
