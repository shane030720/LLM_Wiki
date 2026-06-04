---
title: SQL (Structured Query Language)
category: entity
tags: [sql, database, query-language, standard, relational]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

SQL(Structured Query Language)은 관계형 데이터베이스를 정의하고 조작하기 위한 표준 언어다. IBM San Jose Research Laboratory의 System R 프로젝트에서 "Sequel"이라는 이름으로 개발되었으며, 이후 ANSI와 ISO의 공식 표준으로 채택되었다. SQL-86을 시작으로 SQL:2023까지 지속적으로 개정되고 있다. 상용 DBMS는 SQL-92의 기능 대부분을 지원하며 이후 표준의 일부 기능과 독자적인 확장(proprietary feature)을 추가로 제공한다. 이로 인해 동일한 SQL이 모든 시스템에서 동일하게 동작하지 않을 수 있다.

## Capabilities

- **DDL (Data Definition Language)**: 테이블 생성(`CREATE TABLE`), 삭제(`DROP TABLE`), 수정(`ALTER TABLE`) 등 스키마 정의
- **DML (Data Manipulation Language)**: 데이터 조회(`SELECT`), 삽입(`INSERT`), 수정(`UPDATE`), 삭제(`DELETE`)
- **무결성 제약 조건 선언**: `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`
- **집계 연산**: `AVG`, `SUM`, `COUNT`, `MIN`, `MAX` 및 `GROUP BY`, `HAVING` 절
- **중첩 서브쿼리**: `IN`, `EXISTS`, `SOME`, `ALL`, `UNIQUE`, `WITH` 절을 통한 복잡한 질의 표현
- **집합 연산**: `UNION`, `INTERSECT`, `EXCEPT`
- **문자열 패턴 매칭**: `LIKE` 연산자 (`%`, `_` 와일드카드)
- **NULL 처리**: true/false/unknown 3-값 논리(three-valued logic) 기반의 NULL 의미론

## Limitations

- 표준 SQL과 각 상용 DBMS의 방언(dialect) 간 차이가 존재하여 이식성이 완전하지 않다.
- Natural join은 동명(同名) 속성을 자동으로 조인하므로 의미상 무관한 속성이 같은 이름을 가질 경우 잘못된 결과를 낼 수 있다.
- `ALTER TABLE DROP COLUMN`은 많은 데이터베이스에서 지원하지 않는다.
- SQL은 순서 없는 집합(set) 모델을 기반으로 하므로, 행 순서에 의존하는 처리는 `ORDER BY` 없이 보장되지 않는다.

## Relationships

- [[sql-ddl]] (SQL의 스키마 정의 언어: 도메인 타입, CREATE/DROP/ALTER TABLE)
- [[sql-select-query]] (SQL의 기본 조회 질의 구조: SELECT-FROM-WHERE, 조인, 집합 연산)
- [[sql-aggregate-functions]] (집계 함수 및 GROUP BY, HAVING)
- [[sql-subqueries]] (중첩 서브쿼리: IN, EXISTS, SOME, ALL, WITH, 파생 관계)
- [[sql-null-values]] (NULL 값과 3-값 논리)
- [[sql-dml]] (데이터 삽입·수정·삭제: INSERT, UPDATE, DELETE)

## Sources

- raw/데이터베이스/SQL Basics.pdf
