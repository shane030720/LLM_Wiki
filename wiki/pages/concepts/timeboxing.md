---
title: Timeboxing
category: concept
tags: [project-management, scheduling, agile, scope]
sources: [raw/시스템 분석 이론/ch02-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Timeboxing은 프로젝트에 고정된 마감 기한(timebox)을 설정하고, 그 기한 내에 완수 가능한 핵심·필수 기능에만 집중하는 프로젝트 시간 관리 기법이다. 시간 추정 결과가 가용 시간을 초과할 때, 기한을 연장하거나 품질을 낮추는 대신 범위를 제한하고 나머지 기능은 이후 반복 주기에서 추가하는 방식으로 일정을 준수한다.

## How It Works

1. **기한 설정**: 엄격하지만 현실적인 마감 기한을 정한다. 이 기한은 협상 불가 원칙으로 운용된다.
2. **핵심 요구사항 식별**: 시스템의 핵심적(core)이고 필수적(essential)인 기능 요구사항을 명확히 정의하고, 비필수 기능과 구분한다.
3. **집중 개발**: 팀은 정의된 핵심 기능에만 집중하며 고품질(high quality) 결과물을 생산한다.
4. **반복(Iteration)**: 첫 timebox 완료 후 동일 방식으로 추가 기능을 개발하는 반복 주기를 수행하여 시스템을 점진적으로 완성한다.

## Key Properties

- **고정 기한(Fixed Deadline)**: 기한 자체는 변경하지 않으며, 대신 범위를 조정함
- **우선순위 기반 범위 제한**: 모든 기능이 아닌 핵심 필수 기능에만 집중
- **품질 비타협**: 빠른 개발 속도에도 품질 기준을 타협하지 않음을 명시적으로 강조
- **반복 가능성**: 한 timebox의 완료가 다음 timebox의 자연스러운 시작으로 이어짐
- **범위 관리 도구**: [[scope-creep]] 방지를 위한 실용적이고 구조적인 메커니즘

## Relationships

- [[scope-creep]] — Timeboxing은 범위 증가 압력에 대응하는 핵심 기법이다
- [[agile-development-methodology]] — 애자일 방법론은 Timeboxing을 스프린트(Sprint) 형태로 구조화하여 핵심 메커니즘으로 사용한다
- [[rapid-application-development]] — RAD의 반복적 접근법은 Timeboxing과 함께 활용될 때 효과적이다
- [[project-estimation-and-planning]] — 시간 추정 결과가 가용 시간을 초과하는 상황에서 Timeboxing을 적용 판단한다
- [[sdlc-methodology-selection]] — Timeboxing은 짧은 일정이나 일정 가시성이 요구되는 프로젝트의 방법론 선택 기준과 연관된다

## Open Questions

- "핵심 기능"의 범위를 누가, 어떤 기준으로 결정하는가? 이해관계자 간 의견이 다를 경우 어떻게 조율하는가?
- 품질을 타협하지 않으면서도 빠른 개발을 달성하는 것이 실제로 가능한가? 어떤 조건에서 가능한가?
- 첫 번째 timebox에서 누락된 기능이 이후 timebox에서 추가될 때 아키텍처 변경이 필요한 경우 어떻게 처리하는가?

## Sources

- raw/시스템 분석 이론/ch02-1.pdf (p. 36)
