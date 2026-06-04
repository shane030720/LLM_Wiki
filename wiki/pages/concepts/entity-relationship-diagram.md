---
title: Entity Relationship Diagram (ERD)
category: concept
tags: [erd, entity, attribute, relationship, cardinality, modality, foreign-key, data-modeling]
sources: [raw/시스템분석/ch06-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Entity Relationship Diagram(ERD)은 데이터 모델을 시각적으로 표현하는 가장 대표적인 방법이다. 시스템 내에서 데이터를 수집하는 대상(Entity), 그 대상의 특성(Attribute), 그리고 대상들 간의 연관(Relationship)을 도식으로 나타내며, 비즈니스 규칙(business rules)을 구조적으로 표현하는 데 활용된다.

## How It Works

ERD는 세 가지 핵심 구성 요소로 이루어진다.

### Entity
데이터를 수집하는 사람(person), 장소(place), 사건(event), 사물(thing)을 의미한다. 반드시 복수의 인스턴스(occurrence)가 존재해야 entity로 인정된다. 예: STUDENT, DORM, BOOK, LIBRARY CHECK-OUT, COURSE.

### Attribute
Entity에 대해 포착되는 정보 항목이다. 속성명은 명사(noun)로 표현하며, 조직에서 실제로 사용하는 속성만 포함한다. 세 가지 특수 유형이 있다.
- **Composite Attribute**: 여러 하위 속성으로 구성됨 (예: Address → Street, City, State, Zip)
- **Multi-valued Attribute**: 하나의 entity 인스턴스에 대해 복수의 값을 가질 수 있음 (예: Major)
- **Derived Attribute**: 다른 값들로부터 계산되어 도출됨 (예: Grade Point)

하나 이상의 attribute가 **Identifier**로 지정되어 각 entity 인스턴스를 고유하게 식별한다. 여러 attribute가 결합된 **Concatenated Identifier**도 허용된다.

### Relationship
Entity들 간의 연관성이다. 관계에서 첫 번째 entity는 **parent entity**, 두 번째는 **child entity**로 구분된다. 관계명은 능동적 동사 구문(active verb phrase)으로 표현하며, 양방향으로 읽을 수 있어야 한다.

**Cardinality**: 한 entity 인스턴스가 다른 entity 인스턴스와 몇 번 연관될 수 있는지를 나타낸다.
| 표기 | 의미 |
|------|------|
| 1:1 | 하나 대 하나 |
| 1:N | 하나 대 다수 |
| M:N | 다수 대 다수 |

**Modality**: child entity 인스턴스가 parent entity 인스턴스 없이 존재할 수 있는지를 나타낸다.
- **Not Null**: 관련 entity 인스턴스가 반드시 존재해야 함
- **Null**: 관련 entity 인스턴스가 없어도 유효함

### Foreign Key
관계는 foreign key를 통해 물리적으로 구현된다. Parent entity의 primary key가 child entity에 복제(migrate)되어 foreign key가 된다. M:N 관계는 직접 foreign key로 해결할 수 없으므로 **Intersection Entity**를 도입한다.

### Intersection Entity (교차 엔티티)
M:N 관계를 해소하기 위해 두 entity 사이에 새로운 entity를 생성한다.
1. 기존 M:N 관계 제거
2. 두 개의 1:N 관계로 분리 (원래 entity들이 parent, 신규 entity가 child)
3. 교차 entity에 두 parent의 primary key를 foreign key로 이전 (연결된 primary key 구성 가능)

예: STUDENT — COURSE 의 M:N 관계 → COURSE REGISTRATION 교차 entity 생성

## Key Properties

- ERD는 비즈니스 규칙(business rules)을 구조적으로 표현하는 도구다.
- Entity 간 선행 조건(must-exist)을 modality로 표현한다.
- Relationship은 항상 양방향으로 읽을 수 있어야 한다.
- M:N 관계는 반드시 intersection entity로 해소해야 논리 모델이 완성된다.
- DFD의 data store는 일반적으로 ERD의 entity에 대응한다.
- 구현에 관련된 entity(예: 오래된 데이터의 archive 파일)는 분석 단계 ERD에 포함하지 않는다.

## Relationships

- [[data-modeling]] — ERD는 data model을 표현하는 주요 도구
- [[normalization]] — ERD로 표현된 논리 데이터 모델을 검증하고 개선하는 기법

## Open Questions

- Binary relationship 외에 Ternary(삼원) 관계 또는 그 이상의 관계를 ERD에서 처리하는 방법에 대한 내용이 본 자료에서는 다루어지지 않았다.
- CASE 도구에서 ERD를 자동 생성하거나 DFD와 균형 검증을 자동화하는 범위와 한계가 구체적으로 명시되지 않았다.
- 복잡한 비즈니스 도메인에서 entity의 적정 granularity(세분화 수준)를 결정하는 기준이 명확하지 않다.

## Sources

- raw/시스템분석/ch06-1.pdf — Dennis, Wixom, and Roth, *Systems Analysis and Design*, 2019, Chapter 6
