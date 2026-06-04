---
title: Normalization
category: concept
tags: [normalization, 1nf, 2nf, 3nf, data-modeling, logical-model, validation]
sources: [raw/시스템분석/ch06-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Normalization은 논리적 데이터 모델(logical data model)을 검증(validate)하고 그 조직을 개선하기 위해 적용하는 일련의 규칙(a series of rules)이다. 분석가가 ERD로 표현된 논리 데이터 모델의 품질을 확인하는 기법으로, 데이터 중복과 이상(anomaly)을 제거하여 구조를 견고하게 만든다. 일반적으로 세 가지 정규화 규칙(Normal Form)이 사용된다.

## How It Works

정규화는 비정규화 상태(Unnormalized)에서 출발하여 단계적으로 적용된다.

### 비정규화 상태 (Unnormalized)
하나의 entity 인스턴스에 대해 반복되는 속성(또는 속성 그룹)이 존재하는 상태. 예를 들어 ORDER entity가 1~22개의 Item 속성 그룹을 반복적으로 포함하는 경우.

---

### 1차 정규형 (1NF: First Normal Form)

**규칙**: 하나의 entity 인스턴스에서 둘 이상 반복되는 속성(또는 속성 그룹)이 있으면, 해당 속성들을 분리하여 별도의 entity로 독립시킨다.

**적용 예**:
- 비정규화: ORDER entity 내에 Item Number, Item Name, Quantity Ordered 등이 1~22번 반복
- 1NF 적용 후: ORDER entity와 ORDERED ITEM entity를 분리하고 1:N 관계 설정

**핵심 질문**: "하나의 entity 인스턴스에 대해 둘 이상 발생하는 속성(그룹)이 있는가?"

---

### 2차 정규형 (2NF: Second Normal Form)

**규칙**: Concatenated key(복합 식별자)를 가진 entity에서, 전체 키가 아닌 키의 일부에만 종속되는 속성이 있으면, 그 속성들을 새로운 entity로 분리한다. 단, Concatenated key를 가진 entity에만 적용된다.

**적용 예**:
- ORDERED ITEM entity의 식별자: (Item Number + Order Number)
- Item Name, Item Unit, Item Price는 Item Number에만 종속 → ITEM entity로 분리
- Quantity Ordered, Quantity Shipped는 전체 키에 종속 → ORDERED ITEM에 잔류

**핵심 질문**: "키의 일부에만 종속되는 속성이 있는가?"

---

### 3차 정규형 (3NF: Third Normal Form)

**규칙**: entity의 키(identifier)가 아닌 다른 속성에 종속되는 속성이 있으면, 그 속성들을 새로운 entity로 분리한다.

**적용 예**:
- ORDER entity에서 CustomerName, CustomerAddress, CustomerType, District Number, Region Number는 CustomerNumber에 종속 → CUSTOMER entity로 분리
- ORDER entity에는 CustomerNumber만 foreign key로 잔류

**핵심 질문**: "entity의 키가 아닌 속성에 종속되는 속성이 있는가?"

---

### 정규화 결과 요약 예시

| 단계 | 생성된 Entity |
|------|--------------|
| Unnormalized | ORDER (반복 그룹 포함) |
| 1NF | ORDER, ORDERED ITEM |
| 2NF | ORDER, ORDERED ITEM, ITEM |
| 3NF | ORDER, ORDERED ITEM, ITEM, CUSTOMER |

## Key Properties

- 정규화는 논리 데이터 모델에 적용되며, 분석(Analysis) 단계에서 수행된다.
- 세 가지 정규형(1NF, 2NF, 3NF)이 실무에서 일반적으로 사용된다.
- 2NF는 Concatenated key를 가진 entity에만 적용 가능하다.
- 3NF는 비키(non-key) 속성 간의 종속(transitive dependency)을 제거한다.
- 정규화 결과로 entity 수가 증가하고, 각 entity는 더 명확한 단일 책임을 갖게 된다.
- ERD의 설계 품질을 보장하는 검증 도구로 활용된다.

## Relationships

- [[data-modeling]] — 정규화는 논리 데이터 모델을 검증·개선하는 기법
- [[entity-relationship-diagram]] — 정규화 적용 대상이 되는 ERD 기반의 논리 모델

## Open Questions

- 본 자료에서는 3NF까지만 다루고 있으나, 실무에서 언급되는 BCNF(Boyce-Codd Normal Form), 4NF, 5NF 등 상위 정규형과의 관계 및 적용 필요성이 명시되지 않았다.
- 정규화를 과도하게 적용할 경우 발생하는 성능 저하(과도한 join 연산)와의 trade-off, 즉 의도적인 비정규화(denormalization) 전략에 대한 논의가 포함되어 있지 않다.
- 정규화와 Physical Data Model로의 변환 사이에서 설계자가 어떤 기준으로 정규화 수준을 결정해야 하는지가 명확하지 않다.

## Sources

- raw/시스템분석/ch06-1.pdf — Dennis, Wixom, and Roth, *Systems Analysis and Design*, 2019, Chapter 6
