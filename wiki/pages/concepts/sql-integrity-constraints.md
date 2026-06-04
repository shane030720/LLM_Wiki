---
title: SQL Integrity Constraints
category: concept
tags: [sql, integrity, constraint, referential-integrity, foreign-key, database]
sources: [raw/데이터베이스/Intermediate SQL.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Integrity Constraint(무결성 제약)는 권한이 있는 사용자의 데이터베이스 변경이 데이터 일관성을 훼손하지 않도록 보호하는 규칙이다. 우발적인 데이터 손상을 방지하며, 스키마 정의 시 선언적으로 명시된다. 예를 들어 강사 이름은 null일 수 없고, 학과 예산은 반드시 $0.00 이상이어야 한다.

## How It Works

**단일 릴레이션 제약 (Constraints on a Single Relation)**

1. **NOT NULL**: 속성 값이 null이 될 수 없음을 선언한다.
   ```sql
   name varchar(20) not null
   budget numeric(12,2) not null
   ```

2. **UNIQUE (A1, A2, …, Am)**: 나열된 속성들이 후보키(candidate key)를 형성함을 선언한다. Primary key와 달리 null 값이 허용된다.

3. **PRIMARY KEY**: 릴레이션의 기본키를 선언한다. NOT NULL과 UNIQUE를 암묵적으로 적용한다.

4. **CHECK (P)**: 릴레이션의 모든 튜플이 술어(predicate) P를 만족해야 한다.
   ```sql
   CREATE TABLE section (
       course_id  varchar(8),
       sec_id     varchar(8),
       semester   varchar(6),
       year       numeric(4,0),
       ...
       PRIMARY KEY (course_id, sec_id, semester, year),
       CHECK (semester IN ('Fall', 'Winter', 'Spring', 'Summer'))
   );
   ```

**참조 무결성 (Referential Integrity)**

한 릴레이션의 특정 속성 집합에 나타나는 값이 다른 릴레이션의 기본키에도 반드시 존재해야 함을 보장한다. 예를 들어 `instructor` 릴레이션에 'Biology'라는 학과명이 나타나면 `department` 릴레이션에도 반드시 'Biology' 튜플이 존재해야 한다.

선언 방법:

```sql
-- 단축 표기
dept_name varchar(20) references department

-- 연쇄 작업 명시
FOREIGN KEY (dept_name) REFERENCES department
    ON DELETE CASCADE
    ON UPDATE CASCADE
```

`CASCADE` 외의 대안 연쇄 작업:

| 액션 | 설명 |
|------|------|
| `CASCADE` | 참조된 튜플 삭제/수정 시 참조하는 튜플도 함께 삭제/수정 |
| `SET NULL` | 참조 속성을 null로 설정 |
| `SET DEFAULT` | 참조 속성을 선언된 기본값으로 설정 |

**트랜잭션 내 제약 지연 (Deferred Constraints)**

상호 참조 관계(예: 서로를 배우자로 참조하는 John과 Mary)를 삽입할 때, 삽입 순서로 인해 일시적 참조 무결성 위반이 발생할 수 있다. 이 경우 제약 검사를 트랜잭션 종료 시점으로 지연할 수 있다.

```sql
CREATE TABLE person (
    ID      char(10),
    name    char(40),
    spouse  char(10),
    PRIMARY KEY (ID),
    CONSTRAINT spouse_ref FOREIGN KEY (spouse) REFERENCES person
);

SET CONSTRAINTS spouse_ref DEFERRED;
INSERT INTO person VALUES ('10101', 'John', '11111');
INSERT INTO person VALUES ('11111', 'Mary', '10101');
COMMIT;
```

## Key Properties

- NOT NULL과 UNIQUE는 속성 수준 또는 테이블 수준으로 선언 가능하다.
- UNIQUE는 null 허용, PRIMARY KEY는 null 불허이다.
- CHECK 제약은 삽입 및 수정 시 평가된다.
- 외래키의 연쇄 작업(CASCADE, SET NULL, SET DEFAULT)은 참조 무결성 유지의 핵심 메커니즘이다.
- 무결성 제약은 트랜잭션 내에서 `DEFERRED`로 지연될 수 있어 복잡한 삽입 순서 문제를 해결한다.

## Relationships

- [[sql-transactions]] (제약 위반은 트랜잭션 내에서 `DEFERRED`로 지연 처리될 수 있다)
- [[sql-join-expressions]] (참조 무결성이 정의하는 릴레이션 간 관계는 조인 연산의 의미론적 기반이 된다)
- [[sql-views]] (updatable view의 허용 조건과 무결성 제약이 상호작용한다)

## Open Questions

- CHECK 제약 내에서 서브쿼리를 사용할 수 있는가? SQL 표준과 개별 DBMS 구현 간에 차이가 있는가?
- 대규모 테이블에서 외래키 CASCADE 연산이 성능에 미치는 영향은 어느 정도인가?
- 다중 릴레이션에 걸친 제약인 ASSERTION이 대부분의 DBMS에서 지원되지 않는 이유는 무엇인가?

## Sources

- raw/데이터베이스/Intermediate SQL.pdf (p.20–p.26)
