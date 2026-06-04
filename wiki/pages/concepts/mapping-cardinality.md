---
title: Mapping Cardinality
category: concept
tags: [database, er-model, cardinality, relationship, participation]
sources: [raw/데이터베이스/ER model.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Mapping cardinality(매핑 카디널리티)는 하나의 entity가 특정 relationship set을 통해 연결될 수 있는 다른 entity의 최대 수를 나타내는 제약 조건이다. 주로 binary relationship set을 기술할 때 사용된다.

## How It Works

**Binary Relationship의 네 가지 유형**

| 유형 | A 측 | B 측 | E-R Diagram 표기 |
|------|------|------|-----------------|
| One-to-One | at most one B와 연결 | at most one A와 연결 | A —◆→ B (양방향 directed line) |
| One-to-Many | several B와 연결 | at most one A와 연결 | A →◆— B |
| Many-to-One | at most one B와 연결 | several A와 연결 | A —◆→ B |
| Many-to-Many | several B와 연결 | several A와 연결 | A —◆— B (양방향 undirected line) |

- Directed line (→): "one" (at most one)을 의미
- Undirected line (—): "many" (zero or more)를 의미
- A, B 중 일부 element는 어느 쪽에도 매핑되지 않을 수 있다

**Participation Constraint(참여 제약)**
- Total participation (이중 선): entity set의 모든 entity가 relationship에 적어도 하나 참여해야 한다
  - 예: section은 반드시 하나의 course를 가져야 한다 (sec_course 관계에서 total participation)
- Partial participation (단일 선): 일부 entity가 어떤 relationship에도 참여하지 않을 수 있다
  - 예: instructor는 advisor 관계에서 associated student가 없을 수 있다

**Ternary 이상 Relationship의 카디널리티**
- Ternary relationship에서는 최대 하나의 arrow(→)만 허용한다
- 예: proj_guide에서 instructor 쪽에 arrow → 각 student는 특정 project에 대해 최대 한 명의 instructor를 가진다
- Arrow가 둘 이상이면 의미가 모호해지므로 금지한다

**Relationship Set의 Primary Key 결정**
카디널리티에 따라 relationship set의 primary key가 달라진다:
- One-to-one: 참여하는 두 entity set 중 어느 한쪽의 primary key
- Many-to-one / One-to-many: "many" 쪽 entity set의 primary key
- Many-to-many: 두 entity set의 primary key의 합집합(union)

## Key Properties

- A와 B 사이의 entity pair는 특정 relationship set에서 최대 하나의 relationship을 가질 수 있다 (relationship set의 super key = 참여 entity set primary key 조합)
- 카디널리티 제약은 현실 세계의 비즈니스 규칙을 반영한다
- Total participation은 E-R Diagram에서 이중 선으로 시각적으로 구분된다
- Many-to-one(total on many side) 관계는 별도 relationship schema 대신 "many" 쪽 entity schema에 extra attribute를 추가하여 표현할 수 있다

## Relationships

- [[entity-relationship-model]] (카디널리티가 적용되는 ER 모델 전반)
- [[er-to-relational-schema]] (카디널리티에 따른 relational schema 변환 전략)
- [[weak-entity-set]] (identifying relationship은 one-to-many total participation이 필수)

## Open Questions

- Participation constraint(total/partial)를 relational schema 수준에서 강제하려면 어떤 추가 제약이 필요한가?
- Ternary relationship에서 arrow를 하나로 제한하는 규칙을 우회하는 더 표현력 있는 대안이 있는가?

## Sources

- raw/데이터베이스/ER model.pdf
