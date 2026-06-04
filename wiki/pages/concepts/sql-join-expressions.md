---
title: SQL Join Expressions
category: concept
tags: [sql, join, relational-algebra, database]
sources: [raw/데이터베이스/Intermediate SQL.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL Join 연산은 두 릴레이션의 튜플을 조인 조건(join predicate)에 따라 결합하는 연산이다. 기본적으로 Cartesian product에 매칭 조건을 적용하며, 결과에 포함될 속성을 결정한다. SQL은 명시적 조인 조건을 지정하는 다양한 형태의 조인을 제공한다.

## How It Works

**Inner Join (기본 조인)**

조인 조건을 만족하는 튜플만 결과에 포함한다. 아래 세 표현은 동등하다.

```sql
SELECT name, course_id
FROM instructor JOIN teaches ON instructor.ID = teaches.ID;

SELECT name, course_id
FROM instructor NATURAL JOIN teaches;

SELECT name, course_id
FROM instructor, teaches
WHERE instructor.ID = teaches.ID;
```

**Natural Join**

두 릴레이션에서 이름이 같은 모든 속성의 값이 일치하는 튜플을 자동으로 결합한다. 의도치 않은 공통 속성이 매칭될 경우 잘못된 결과를 낼 수 있다는 위험이 있다.

**Outer Join**

Inner Join에서 손실되는 튜플을 보존하기 위한 조인 확장이다. 매칭되지 않는 속성에는 null 값을 사용한다. 세 가지 형태가 있다.

- **Left Outer Join**: 왼쪽 릴레이션의 모든 튜플을 보존한다.
  ```sql
  course NATURAL LEFT OUTER JOIN prereq
  ```
- **Right Outer Join**: 오른쪽 릴레이션의 모든 튜플을 보존한다.
  ```sql
  course NATURAL RIGHT OUTER JOIN prereq
  ```
- **Full Outer Join**: 양쪽 릴레이션의 모든 튜플을 보존한다.
  ```sql
  course NATURAL FULL OUTER JOIN prereq
  ```

조인 조건은 `ON` 절 또는 `USING` 절로 명시할 수 있다.

```sql
course FULL OUTER JOIN prereq USING (course_id)
course LEFT OUTER JOIN prereq ON course.course_id = prereq.course_id
```

## Key Properties

- Join predicate는 두 릴레이션에서 어떤 튜플이 매칭되는지, 결과에 어떤 속성이 포함되는지를 정의한다.
- Natural Join은 공통 속성을 자동으로 탐지하므로 스키마 변경 시 예기치 않은 동작이 발생할 수 있다.
- Outer Join은 정보 손실 없이 두 릴레이션을 결합하기 위해 null 값을 활용한다.
- Inner Join의 기본 키워드는 `INNER`이며 생략 가능하다.

## Relationships

- [[sql-views]] (뷰 정의 내 쿼리 표현식에서 조인을 사용할 수 있다)
- [[sql-integrity-constraints]] (참조 무결성이 조인의 의미론적 기반인 릴레이션 간 관계를 정의한다)

## Open Questions

- Natural Join에서 의도치 않은 공통 속성이 매칭되는 문제를 방지하기 위한 best practice는 무엇인가?
- Outer Join과 subquery를 사용한 동등한 표현 간에 쿼리 최적화 관점에서 성능 차이가 존재하는가?

## Sources

- raw/데이터베이스/Intermediate SQL.pdf (p.3–p.11)
