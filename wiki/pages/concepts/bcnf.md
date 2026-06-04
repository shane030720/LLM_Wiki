---
title: Boyce-Codd Normal Form (BCNF)
category: concept
tags: [database, normalization, bcnf, functional-dependency]
sources: [raw/데이터베이스/Relational DB Design (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

BCNF(Boyce-Codd Normal Form)는 관계 스키마 R이 FD 집합 F에 대해 만족해야 하는 정규형으로, F+에 속하는 모든 non-trivial FD α → β에 대해 α가 R의 superkey여야 한다. BCNF를 만족하는 스키마는 함수 종속성으로 인한 모든 중복이 제거된 상태다.

## How It Works

**BCNF 위반 판별**: α → β가 non-trivial(β ⊄ α)이고 α가 superkey가 아니면 BCNF 위반이다. 예) big_instructor에서 dept_name → building, budget이 성립하지만 dept_name은 superkey가 아니므로 BCNF 위반.

**BCNF 분해 알고리즘**: BCNF를 위반하는 non-trivial FD α → β를 발견하면 R을 다음 두 릴레이션으로 분해한다.
- R1 = α ∪ β
- R2 = R - (β - α)

예) α = dept_name, β = {building, budget}이면:
- R1 = (dept_name, building, budget)
- R2 = (ID, name, salary, dept_name)

분해를 재귀적으로 적용하여 모든 릴레이션이 BCNF를 만족할 때까지 반복한다.

**Lossless-join 보장**: 위 분해에서 R1 ∩ R2 = α이고 α → R1이므로 α가 R1의 superkey가 되어 lossless-join이 항상 보장된다.

**Dependency Preservation 미보장**: R=(J,K,L), F={JK→L, L→K}에서 candidate key는 JK와 JL이다. BCNF 분해 시 어떤 방식으로도 JK→L을 단일 릴레이션에서 검사할 수 없는 분해만 존재한다. 이처럼 BCNF 분해가 항상 dependency preservation을 달성하지는 못한다.

## Key Properties

- BCNF이면 반드시 3NF이지만, 역은 성립하지 않는다.
- BCNF 분해는 lossless-join을 항상 보장한다.
- BCNF 분해는 dependency preservation을 보장하지 않는다.
- BCNF는 데이터베이스 정규화의 이상적 목표 정규형이다.
- 모든 관계를 항상 BCNF로 분해할 수 있다(lossless-join 분해의 존재성은 보장).

## Relationships

- [[functional-dependency]] — BCNF 정의와 분해 판단의 수학적 기반
- [[third-normal-form]] — BCNF의 완화 버전; dependency preservation을 보장하는 대안
- [[database-normalization]] — BCNF는 정규화 설계 목표의 최우선 정규형

## Open Questions

- BCNF 분해가 dependency preservation을 희생할 때, 실제 시스템에서 무결성을 유지하기 위한 현실적 대안(trigger, application-level check 등)은 어떻게 평가되는가?

## Sources

- raw/데이터베이스/Relational DB Design (1).pdf
