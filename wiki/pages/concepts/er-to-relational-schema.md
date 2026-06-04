---
title: ER Model to Relational Schema Reduction
category: concept
tags: [database, er-model, relational-schema, schema-design, reduction]
sources: [raw/데이터베이스/ER model.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

ER 다이어그램을 관계형 데이터베이스 스키마(relational schema)로 변환하는 체계적 절차이다. 모든 entity set과 relationship set은 고유한 이름을 가진 relation schema로 균일하게 표현되며, 각 schema는 attribute에 대응하는 column들을 갖는다.

## How It Works

**Strong Entity Set**
- 동일한 attribute를 가진 schema로 직접 변환된다
- 예: `student(ID, name, tot_cred)`

**Weak Entity Set**
- Identifying strong entity set의 primary key를 포함하는 schema로 변환된다
- 예: `section(course_id, sec_id, sem, year)`
- Identifying relationship에 대응하는 schema는 redundant하여 별도로 생성하지 않는다

**Composite Attribute**
- 각 component attribute를 별도의 column으로 flatten한다
- 예: name(first_name, middle_initial, last_name) → 각각의 column
- 모호함이 없는 경우 prefix를 생략할 수 있다

**Multivalued Attribute**
- Entity E의 multivalued attribute M → 별도의 schema EM(E의 primary key, M) 생성
- 예: instructor의 phone_number → `instructor_phone(ID, phone_number)`
- 하나의 entity가 가진 각 값은 개별 tuple로 저장된다
- 최적화: entity의 non-key attribute가 오직 하나의 multivalued attribute뿐이면 entity schema를 생략하고 multivalued attribute schema만 생성한다 (단, 이 경우 해당 attribute를 참조하는 foreign key 제약이 적용되지 않는 caveat 존재)

**Many-to-Many Relationship Set**
- 두 참여 entity set의 primary key와 descriptive attribute로 구성된 schema로 변환된다
- 예: `advisor(s_id, i_id)`

**Many-to-One / One-to-Many Relationship Set (total on many side)**
- 별도의 relationship schema를 만들지 않고, "many" 쪽 entity schema에 "one" 쪽의 primary key를 extra attribute로 추가한다 (schema redundancy 제거)
- 예: inst_dept 관계 대신 instructor schema에 dept_name 추가
- "many" 쪽 participation이 partial이면 해당 extra attribute에 null 값이 발생할 수 있으므로 주의

**One-to-One Relationship Set**
- 어느 쪽이든 "many" 역할을 담당하도록 선택하여, 해당 쪽 entity schema에 extra attribute를 추가한다

## Key Properties

- Entity set과 relationship set은 각각 고유한 schema 이름을 가진다
- Relationship set의 schema redundancy: total participation이 있는 many-to-one 관계는 별도 schema 없이 "many" 쪽 entity schema의 extra attribute로 통합 가능하다
- Derived attribute는 relational schema에 저장하지 않는 것이 일반적이다
- Composite attribute는 평탄화(flatten)되며, 계층 구조는 column 이름의 prefix로만 유지된다
- Multivalued attribute 최적화 시 foreign key 무결성 제약 적용이 제한될 수 있다

## Relationships

- [[entity-relationship-model]] (변환의 출발점인 ER 모델)
- [[er-attributes]] (composite, multivalued, derived attribute의 변환 규칙)
- [[mapping-cardinality]] (카디널리티에 따라 relationship schema 생성 여부가 결정됨)
- [[weak-entity-set]] (weak entity set의 특수한 변환 규칙)

## Open Questions

- Many-to-one 관계에서 "many" 쪽 participation이 partial일 때 null을 허용하는 방식 외에 null을 피하는 대안적 설계가 있는가?
- Multivalued attribute 최적화 시 외래 키 무결성을 보장하기 위한 대안적 접근법은 무엇인가?

## Sources

- raw/데이터베이스/ER model.pdf
