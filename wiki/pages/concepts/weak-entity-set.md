---
title: Weak Entity Set
category: concept
tags: [database, er-model, weak-entity, primary-key, discriminator]
sources: [raw/데이터베이스/ER model.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Weak entity set은 자체적인 primary key를 가지지 않는 entity set이다. 그 존재가 identifying(owner) entity set에 의존하며, identifying relationship을 통해서만 식별될 수 있다.

## How It Works

**구조적 특성**
- Identifying entity set(강한 entity set): weak entity set이 의존하는 strong entity set
- Identifying relationship: identifying entity set에서 weak entity set으로의 total, one-to-many 관계
  - E-R Diagram에서 이중 다이아몬드(double diamond)로 표기
- Discriminator(부분 키): 동일한 identifying entity에 속하는 weak entity들을 서로 구분하는 속성 집합
  - E-R Diagram에서 점선 밑줄로 표기

**Primary Key 구성**
```
weak entity set의 primary key
    = identifying strong entity set의 primary key
    + weak entity set의 discriminator
```
예: section의 primary key = (course_id, sec_id, semester, year)
- course_id: identifying entity(course)의 primary key
- sec_id, semester, year: section의 discriminator

**Relational Schema 변환**
- Weak entity set → identifying strong entity set의 primary key를 포함하는 schema
  - 예: section(course_id, sec_id, sem, year)
- Identifying strong entity set의 primary key는 E-R Diagram에서 weak entity set에 명시적으로 저장되지 않는다 (identifying relationship에 암묵적으로 내포)
- Weak entity set과 identifying entity set 사이의 relationship schema는 redundant하다 (이미 weak entity schema에 포함됨)

**Redundancy 주의**
- course_id를 section에 명시적으로 저장하면 section을 strong entity로 만들 수 있지만, 그렇게 하면 course와의 관계가 attribute에 의해 암묵적으로 이중 표현된다

## Key Properties

- Weak entity set은 identifying entity set 없이 존재할 수 없다 (total participation 필수)
- Identifying relationship은 반드시 one-to-many이어야 한다 (identifying → weak 방향)
- Discriminator는 같은 identifying entity에 속한 weak entity들 사이에서만 구분력을 가진다; 전체 weak entity set에서 유일하지 않아도 된다
- E-R Diagram에서 weak entity set은 이중 사각형(double rectangle)으로 표기한다

## Relationships

- [[entity-relationship-model]] (weak entity set이 등장하는 ER 모델 전반)
- [[mapping-cardinality]] (identifying relationship은 total participation이 있는 one-to-many 관계)
- [[er-to-relational-schema]] (weak entity set을 relational schema로 변환하는 규칙)

## Open Questions

- Weak entity set의 식별 관계가 체인 형태(weak entity가 또 다른 weak entity의 identifying entity 역할)로 중첩될 수 있는가? 그 경우 primary key는 어떻게 구성되는가?

## Sources

- raw/데이터베이스/ER model.pdf
