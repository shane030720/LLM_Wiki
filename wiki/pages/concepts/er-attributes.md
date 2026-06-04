---
title: ER Model Attributes
category: concept
tags: [database, er-model, attribute, composite, multivalued, derived]
sources: [raw/데이터베이스/ER model.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

ER 모델에서 attribute(속성)는 entity set의 모든 구성원이 공통으로 가지는 서술적 특성(descriptive property)이다. 각 attribute는 허용되는 값의 집합인 domain을 가지며, entity를 구체적으로 설명한다.

## How It Works

**Simple vs. Composite Attributes**
- Simple attribute: 더 이상 분해되지 않는 단일 속성 (예: salary)
- Composite attribute: 여러 하위 component attribute로 구성되는 속성 (예: name → first_name, middle_initial, last_name / address → street_number, street_name, city, state, zip_code)
- Composite attribute는 계층적으로 중첩될 수 있다

**Single-valued vs. Multivalued Attributes**
- Single-valued attribute: 하나의 entity에 대해 단일 값을 가진다 (예: ID)
- Multivalued attribute: 하나의 entity에 대해 여러 값을 가질 수 있다 (예: phone_numbers → {456-7890, 123-4567})
- E-R Diagram에서 중괄호로 표기: `{phone_numbers}`

**Derived Attributes**
- 다른 저장된 attribute로부터 계산될 수 있는 속성
- 예: date_of_birth로부터 age를 도출
- 물리적으로 저장하지 않고 필요 시 계산한다

**Relational Schema 변환 시 처리 방식**
- Composite attribute → 각 component attribute를 별도의 column으로 flatten (예: name → name_first_name, name_last_name)
- Multivalued attribute M (entity E 소속) → 별도의 schema EM 생성: EM(E의 primary key, M)
  - 예: instructor의 phone_number → instructor_phone(ID, phone_number)
  - 하나의 entity가 가진 multivalued attribute의 각 값은 별도의 tuple로 매핑된다
- Derived attribute → 일반적으로 schema에 저장하지 않음

## Key Properties

- 모든 attribute는 해당 entity set의 모든 구성원에게 적용된다
- Domain은 attribute가 가질 수 있는 허용값의 범위를 정의한다
- Composite attribute를 entity로 올릴지, 단순 attribute로 남길지는 설계 결정 사항이다 (예: phone을 entity로 올리면 부가 정보 저장 및 다수 번호 허용 가능)
- Multivalued attribute를 가진 entity가 primary key 외 multivalued attribute만 존재할 경우, entity schema를 별도로 만들지 않고 multivalued attribute schema만 생성하는 최적화가 가능하다 (예: time_slot)

## Relationships

- [[entity-relationship-model]] (attribute가 속하는 ER 모델의 전반적 구조)
- [[er-to-relational-schema]] (composite 및 multivalued attribute를 relational schema로 변환하는 규칙)

## Open Questions

- Composite attribute와 별도의 entity를 사용하는 기준은 어디에 두어야 하는가?
- Derived attribute를 materialized view처럼 저장할지 계산할지는 어떤 기준으로 결정하는가?

## Sources

- raw/데이터베이스/ER model.pdf
