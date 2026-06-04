---
title: Modality (ERD)
category: concept
tags: [erd, data-modeling, relationship, constraint, systems-analysis]
sources: [raw/시스템 분석 이론/ch06-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Modality는 ERD에서 관계(relationship)의 필수성(optionality)을 나타내는 개념으로, 한 엔티티의 인스턴스가 존재하기 위해 관련 엔티티의 인스턴스가 반드시 존재해야 하는지를 정의한다. Cardinality가 "몇 개"를 다루는 반면, Modality는 "필수인가, 선택인가"를 다룬다.

## How It Works

Modality는 두 가지 값을 가진다.

- **Not Null (Mandatory)**: 관련 엔티티의 인스턴스가 반드시 존재해야 현재 엔티티 인스턴스가 유효하다. 예를 들어, 주문(ORDER) 인스턴스가 생성되려면 고객(CUSTOMER) 인스턴스가 반드시 먼저 존재해야 한다.
- **Null (Optional)**: 관련 엔티티의 인스턴스 없이도 현재 엔티티 인스턴스가 유효할 수 있다. 예를 들어, 고객(CUSTOMER)은 주문(ORDER)이 없어도 시스템에 존재할 수 있다.

ERD 표기법에서 Modality는 관계선의 끝부분 기호로 표현된다.
- 원(circle): optional (Null 허용)
- 수직선(bar): mandatory (Not Null)

Modality는 관계의 양쪽 방향에 각각 독립적으로 정의될 수 있다. 즉, 부모→자식 방향과 자식→부모 방향이 서로 다른 Modality를 가질 수 있다.

## Key Properties

- Modality는 비즈니스 규칙(business rule)을 반영한다.
- Cardinality(1:1, 1:N, M:N)와 함께 사용되어 관계의 완전한 의미를 표현한다.
- Not Null 제약은 물리 데이터 모델에서 외래 키(foreign key)의 NULL 허용 여부로 구현된다.
- 잘못된 Modality 설정은 데이터 무결성 문제나 비즈니스 규칙 위반으로 이어질 수 있다.
- 최종 결정은 업무 담당자(knowledgeable users)와의 협의를 통해 이루어진다.

## Relationships

- [[mapping-cardinality]] — cardinality(1:1, 1:N, M:N)와 함께 관계의 전체 의미를 구성하는 보완 개념
- [[entity-relationship-model]] — Modality는 ER 모델 관계의 필수 속성 중 하나
- [[entity-relationship-diagram]] — ERD 표기법의 기호(원, 수직선 등)를 통해 시각적으로 표현
- [[database-normalization]] — Modality는 정규화 과정에서 엔티티 분리 여부 결정에 영향을 미침

## Open Questions

- CASE 도구마다 Modality 표기 방식(crow's foot, Chen notation 등)이 달라 팀 간 혼란이 생길 수 있는데, 표준 표기법 선택 기준은 무엇인가?
- 분석 단계에서 정의한 Modality가 설계 단계에서 외래 키 제약(NOT NULL constraint)과 정확히 1:1로 매핑되는가, 아니면 설계 단계에서 재검토가 필요한가?

## Sources

- raw/시스템 분석 이론/ch06-1.pdf (pp. 22–23)
