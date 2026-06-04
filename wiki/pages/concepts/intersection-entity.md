---
title: Intersection Entity
category: concept
tags: [erd, data-modeling, many-to-many, normalization, systems-analysis]
sources: [raw/시스템 분석 이론/ch06-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Intersection Entity(교차 엔티티, 연관 엔티티)는 두 엔티티 사이의 다대다(M:N) 관계를 해소하기 위해 새롭게 생성되는 엔티티다. M:N 관계는 관계형 데이터베이스에서 직접 구현이 불가능하므로, Intersection Entity를 사이에 삽입하여 두 개의 1:N 관계로 분해한다. 연관 테이블(associative table), 접합 엔티티(junction entity)라고도 불린다.

## How It Works

M:N 관계를 Intersection Entity로 해소하는 절차는 다음과 같다.

1. **M:N 관계 제거**: 두 엔티티 사이의 다대다 관계를 제거한다.
2. **Intersection Entity 삽입**: 두 엔티티 사이에 새 엔티티를 생성한다.
3. **1:N 관계 두 개 생성**: 원래 두 엔티티가 각각 Intersection Entity의 부모가 되는 1:N 관계를 설정한다.
4. **외래 키 마이그레이션**: 각 부모 엔티티의 기본 키(PK)를 Intersection Entity로 외래 키(FK)로 이관한다.
5. **복합 기본 키 구성**: 이관된 FK들이 Intersection Entity의 기본 키를 구성하는 경우가 많다(concatenated/composite key).
6. **관계 고유 속성 추가**: Intersection Entity는 관계 자체에 속하는 고유 속성을 가질 수 있다.

**예시**: STUDENT와 COURSE 사이의 M:N 관계를 COURSE_REGISTRATION으로 해소

```
STUDENT (Student ID - PK) 
    ↕ 1:N
COURSE_REGISTRATION (Student ID - PK/FK, Course ID - PK/FK, Semester - PK, Final Grade)
    ↕ N:1
COURSE (Course ID - PK)
```

Final Grade와 Semester는 특정 학생의 특정 수강에만 속하는 속성이므로 COURSE_REGISTRATION에 배치된다.

## Key Properties

- Intersection Entity는 항상 두 부모 엔티티의 PK를 FK로 포함하며, 이것이 복합 PK를 형성한다.
- 관계 자체에 귀속되는 속성(예: 수강 학점, 등록 날짜)을 저장할 수 있다.
- M:N 관계를 반드시 해소해야 하는 시점은 물리 설계 단계이지만, 논리 분석 단계에서도 명확성을 위해 미리 도입할 수 있다.
- Intersection Entity는 독립적인 비즈니스 의미를 갖는 경우가 많아 별도의 이름을 붙이는 것이 권장된다.

## Relationships

- [[mapping-cardinality]] — M:N 카디널리티가 Intersection Entity 생성의 직접적 원인
- [[entity-relationship-model]] — Intersection Entity는 ERD의 고급 구문 요소
- [[entity-relationship-diagram]] — ERD에서 M:N 해소를 위한 표준 패턴
- [[er-to-relational-schema]] — Intersection Entity는 관계형 스키마에서 접합 테이블(junction table)로 변환됨
- [[database-normalization]] — Intersection Entity 도입은 제2정규형(2NF) 적용과 관련됨; 복합 키의 부분 종속 제거

## Open Questions

- Intersection Entity가 독자적인 비즈니스 의미를 가질 때와 순수하게 기술적 목적으로만 존재할 때, 이름 부여 및 설계 방식을 달리해야 하는가?
- Intersection Entity 자체가 다른 엔티티와 또 M:N 관계를 가질 경우, 재귀적 해소 절차를 어떻게 관리하는가?

## Sources

- raw/시스템 분석 이론/ch06-1.pdf (pp. 33–35)
