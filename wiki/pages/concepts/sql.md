```markdown
---
title: SQL (Structured Query Language)
category: concept
tags: [sql, query-language, ddl, dml, database]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL(Structured Query Language)은 관계형 데이터베이스를 기술하고 조작하기 위한 비절차적(non-procedural) 표준 질의 언어이다. 1980년대에 산업 표준이 되었으며, "무엇을" 가져올지만 기술하고 "어떻게" 가져올지는 DBMS 내부의 query optimizer가 결정한다. 현재도 개발자 언어 인기 조사에서 상위권을 유지하고 있다.

## How It Works

SQL은 두 가지 주요 구성요소로 나뉜다.

**DDL (Data Definition Language)** — 데이터베이스 스키마를 선언

```sql
CREATE TABLE instructor (
    ID        char(5),
    name      varchar(20) NOT NULL,
    dept_name varchar(20),
    salary    numeric(8,2)
);

DROP TABLE instructor;
ALTER TABLE instructor DROP salary;
```

**DML (Data Manipulation Language)** — 데이터를 질의·수정하는 언어

기본 질의 구조:
```sql
SELECT A1, A2, ..., An
FROM   r1, r2, ..., rm
WHERE  P
```

- `SELECT` 절: 결과에 포함할 attribute 나열 (대소문자 구분 없음)
- `FROM` 절: 질의에 관련된 relation 나열; 복수 나열 시 Cartesian Product 생성
- `WHERE` 절: 결과가 만족해야 할 조건 명시; `AND`, `OR`, `NOT` 논리 연산자 조합 가능

Join 예시:
```sql
SELECT name, course_id
FROM   instructor, teaches
WHERE  instructor.ID = teaches.ID;
```

삽입/삭제:
```sql
INSERT INTO instructor VALUES (12345, 'Choi', 'Comp. Sci.', 10000);
DELETE FROM instructor WHERE dept_name = 'Finance';
```

## Key Properties

- 비절차적(non-procedural): "무엇을" 가져올지만 기술, "어떻게"는 DBMS가 결정
- SQL query의 결과도 relation(테이블)
- 대소문자 구분 없음 (case insensitive)
- DDL과 DML의 명확한 역할 분리
- 현재도 개발자 언어 인기 조사 상위권 유지

## Relationships

- [[relational-model]] (SQL이 조작하는 데이터 모델)
- [[database-management-system]] (SQL을 파싱·최적화·실행하는 시스템)
- [[query-processing]] (SQL 질의가 내부적으로 처리되는 과정)
- [[postgresql]] (SQL 표준을 높은 수준으로 준수하는 오픈소스 RDBMS)

## Open Questions

- SQL의 비절차적 특성이 복잡한 그래프 탐색·재귀 질의에서도 항상 충분한가?
- NoSQL 시스템에서 SQL-like 언어(Hive, SparkSQL, BigQuery 등)가 재등장하는 이유는 무엇인가?

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
