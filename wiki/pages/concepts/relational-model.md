---
title: Relational Model
category: concept
tags: [database, relation, tuple, schema, key]
sources: [raw/데이터베이스/Relational Model 2.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Relational Model은 데이터를 테이블(table) 형태로 조직화하는 데이터 모델이다. 각 테이블은 relation이라 불리며, 행(row)은 tuple, 열(column)은 attribute를 나타낸다. 각 attribute는 허용되는 값의 집합인 domain을 가지며, 모든 domain은 원자적(atomic), 즉 더 이상 분리되지 않아야 한다. 관계형 데이터베이스는 이러한 relation들의 집합으로 구성된다.

## How It Works

- **Relation의 형식적 정의**: 속성 A1, A2, …, An과 그에 대응하는 domain D1, D2, …, Dn이 주어질 때, relation r은 D1 × D2 × … × Dn의 부분집합이다. 즉, r은 n-tuple (a1, a2, …, an)의 집합이며 각 ai ∈ Di를 만족한다.
- **Null value**: 모든 domain의 멤버로, 값이 알려지지 않거나 존재하지 않음을 나타낸다. 다만 여러 연산의 정의를 복잡하게 만드는 원인이 된다.
- **Tuple의 순서**: Relation은 집합(set)이므로 tuple 간 순서는 의미가 없으며, 임의의 순서로 저장될 수 있다.
- **Schema vs Instance**:
  - **Database schema**: 데이터베이스의 논리적 설계. 예: `instructor(ID, name, dept_name, salary)`
  - **Database instance**: 특정 시점의 데이터 스냅샷. relation instance는 현재 테이블에 저장된 실제 값들이다.

## Key Properties

- 모든 attribute의 domain은 **atomic**(원자적)이어야 한다 — 다중값이나 복합값 허용 불가
- Null value는 모든 domain에 속하는 특수 값이다
- Relation은 집합이므로 **중복 tuple이 존재하지 않는다**
- Tuple의 순서는 관계없다 (unordered)
- **Superkey**: 각 tuple을 고유하게 식별하기에 충분한 속성의 집합. 예: `{ID}`, `{ID, name}` 모두 instructor의 superkey
- **Candidate key**: 최소 superkey. 예: `{ID}`는 instructor의 candidate key
- **Primary key**: candidate key 중 하나를 선택한 것
- **Foreign key constraint**: 한 relation의 값이 다른 relation에도 반드시 존재해야 한다는 제약 (referencing relation → referenced relation)

## Relationships

- [[relational-algebra]] — 이 모델 위에서 동작하는 연산 체계
- [[normalization-theory]] — 좋은 relation schema를 설계하기 위한 이론 (이 자료에서 언급만 됨, 7장에서 다룸)

## Open Questions

- Null value가 포함될 때 각종 연산(집계, 조인 등)의 결과를 어떻게 정의해야 하는가?
- 좋은 schema 설계 기준(Normalization theory)은 무엇인가? (본 자료에서 미수록)
- Bad design 예시(`univ` 단일 테이블)에서 발생하는 데이터 중복 및 null value 문제를 어떻게 체계적으로 방지할 수 있는가?

## Sources

- raw/데이터베이스/Relational Model 2.pdf (p.2–p.8)
