---
title: SQL DDL (Data Definition Language)
category: concept
tags: [sql, ddl, schema, table, constraint, data-type]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL DDL(Data Definition Language)은 관계형 데이터베이스의 스키마를 정의·변경·삭제하는 SQL 명령어 집합이다. 주요 명령어는 `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`이며, 속성의 도메인 타입(domain type)과 무결성 제약 조건(integrity constraint)을 함께 선언한다.

## How It Works

### 도메인 타입 (Domain Types)

| 타입 | 설명 |
|------|------|
| `char(n)` | 길이 n의 고정 길이 문자열 |
| `varchar(n)` | 최대 길이 n의 가변 길이 문자열 |
| `int` / `smallint` | 정수 (기계 의존적 범위) |
| `numeric(p, d)` | 전체 p자리, 소수점 이하 d자리의 고정 소수점 수 |
| `real` / `double precision` | 부동소수점 / 배정밀도 부동소수점 |
| `float(n)` | 최소 n자리 정밀도의 부동소수점 수 |

### CREATE TABLE

```sql
create table instructor (
    ID          char(5),
    name        varchar(20) not null,
    dept_name   varchar(20),
    salary      numeric(8,2),
    primary key (ID),
    foreign key (dept_name) references department
);
```

- `primary key (A1, ..., An)`: 해당 속성(들)을 기본 키로 선언하며, 자동으로 `NOT NULL`과 유일성을 보장한다.
- `foreign key (Am, ..., An) references r`: 참조 무결성(referential integrity)을 선언한다.
- `not null`: 해당 속성에 NULL 값 삽입을 금지한다.

### DROP TABLE

```sql
drop table r;
```

관계 r과 그 모든 튜플 및 스키마를 제거한다.

### ALTER TABLE

```sql
alter table r add A D;    -- 속성 A(도메인 D)를 추가; 기존 튜플의 해당 값은 null로 초기화
alter table r drop A;     -- 속성 A를 제거 (많은 DBMS에서 미지원)
```

## Key Properties

- 스키마 정의와 동시에 무결성 제약 조건을 선언할 수 있다.
- `primary key` 선언은 `NOT NULL`과 유일성을 자동으로 보장한다.
- `ALTER TABLE add`로 새 속성 추가 시 기존 모든 행의 해당 값은 `null`로 초기화된다.
- 속성 삭제(`alter table drop`)는 많은 DBMS에서 지원하지 않는다.
- `insert into r values (...)` 구문으로 튜플을 삽입하며, null 값도 명시적으로 삽입 가능하다.

## Relationships

- [[sql]] (DDL이 속하는 SQL 언어 전체)
- [[sql-null-values]] (NOT NULL 제약 및 NULL의 의미론)
- [[sql-dml]] (정의된 스키마에 데이터를 조작하는 DML)

## Open Questions

- `ALTER TABLE DROP COLUMN`의 DBMS별 지원 범위는 어디까지인가?
- 대규모 테이블에 `NOT NULL` 컬럼을 추가할 때 성능 영향은 어떻게 최소화할 수 있는가?

## Sources

- raw/데이터베이스/SQL Basics.pdf
