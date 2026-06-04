---
title: Entity-Relationship Model
category: concept
tags: [database, er-model, schema-design, modeling]
sources: [raw/데이터베이스/ER model.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Entity-Relationship(ER) 모델은 데이터베이스 스키마를 개념적으로 설계하기 위한 데이터 모델이다. 현실 세계를 entity(개체)의 집합과 entity 간의 relationship(관계)으로 표현하며, 이후 relational model로 변환되는 설계 단계에서 사용된다.

## How It Works

ER 모델은 세 가지 핵심 구성 요소로 이루어진다.

**Entity와 Entity Set**
- Entity: 현실 세계에서 구별 가능하고 독립적으로 존재하는 객체 (예: 특정 사람, 회사, 사건)
- Entity set: 동일한 유형과 속성을 공유하는 entity들의 집합 (예: 모든 instructor의 집합)
- 각 entity는 attributes(속성)로 서술된다

**Relationship와 Relationship Set**
- Relationship: 여러 entity 간의 연관(association)
- Relationship set: n개(n ≥ 2)의 entity set에서 각각 하나씩 취한 entity들 사이의 수학적 관계의 집합
  - `{(e1, e2, … en) | e1 ∈ E1, e2 ∈ E2, …, en ∈ En}`
- Relationship 자체도 descriptive attribute를 가질 수 있다 (예: advisor 관계의 date 속성)
- Relationship은 참여하는 entity들에 의해서만 식별된다

**E-R Diagram 표기법**
- Rectangle(사각형): entity set
- Diamond(마름모): relationship set
- 속성은 entity 사각형 내부에 나열
- Primary key 속성은 밑줄로 표시
- Directed line (→): "one" 의미
- Undirected line (—): "many" 의미
- Double diamond(이중 마름모): weak entity set의 identifying relationship
- Double line(이중 선): total participation

**Degree of a Relationship Set**
- Binary relationship: 두 entity set을 연결 (가장 일반적)
- Ternary relationship: 세 entity set을 연결 (예: instructor–student–project의 proj_guide)
- 대부분의 relationship은 binary이며, non-binary relationship은 필요한 경우에만 사용

**Role**
- 하나의 entity set이 relationship에서 두 가지 다른 역할로 참여할 수 있다
- 예: course entity set이 prereq relationship에서 "course_id"와 "prereq_id" 두 역할을 담당

## Key Properties

- Entity set은 primary key를 통해 각 entity를 유일하게 식별한다
- Relationship set의 super key는 참여하는 entity set들의 primary key 조합으로 구성된다
- Binary relationship이 데이터베이스 시스템에서 가장 일반적이다
- Non-binary relationship은 경우에 따라 여러 binary relationship으로 분해할 수 있으나, 의미 손실이 발생할 수 있다
- Redundant attribute: relationship으로 이미 표현된 정보를 entity attribute로 중복 저장하는 것은 지양해야 한다 (예: inst_dept 관계가 있을 때 instructor의 dept_name 속성은 중복)

## Relationships

- [[er-attributes]] (ER 모델에서 entity와 relationship을 서술하는 속성 유형)
- [[mapping-cardinality]] (entity 간 연결 가능한 수를 제약하는 카디널리티 개념)
- [[weak-entity-set]] (primary key가 없는 특수한 entity set)
- [[er-to-relational-schema]] (ER 다이어그램을 관계형 스키마로 변환하는 방법)

## Open Questions

- N-ary relationship을 binary relationship으로 분해할 때 의미 보존이 항상 가능한가? 어떤 경우에 분해가 적절하지 않은가?
- Relationship attribute를 relationship set에 두어야 할지, 참여 entity set에 두어야 할지의 기준은 무엇인가?

## Sources

- raw/데이터베이스/ER model.pdf
