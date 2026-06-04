---
title: SQL NULL Values and Three-Valued Logic
category: concept
tags: [sql, null, three-valued-logic, unknown, is-null]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL에서 NULL은 값이 알 수 없거나(unknown) 존재하지 않음을 나타내는 특수 마커다. NULL을 포함하는 비교 연산은 true나 false가 아닌 unknown을 반환하며, 이로 인해 SQL은 true/false/unknown의 3-값 논리(three-valued logic)를 채택한다. NULL은 0이나 빈 문자열과 구별되는 개념이다.

## How It Works

### 산술 연산에서의 NULL

NULL이 포함된 모든 산술 연산의 결과는 NULL이다.

```
5 + null  →  null
```

### 비교 연산에서의 NULL

NULL과의 모든 비교 연산은 unknown을 반환한다.

```
5 < null     → unknown
null = null  → unknown
null <> null → unknown
```

NULL 여부 확인에는 반드시 `IS NULL` / `IS NOT NULL` 술어를 사용한다.

```sql
select name from instructor where salary is null;
```

### 3-값 논리 진리표

| 연산 | 결과 |
|------|------|
| unknown OR true | true |
| unknown OR false | unknown |
| unknown OR unknown | unknown |
| true AND unknown | unknown |
| false AND unknown | false |
| unknown AND unknown | unknown |
| NOT unknown | unknown |

### WHERE 절에서의 처리

`WHERE` 절의 조건이 unknown으로 평가되면 false로 취급되어, 해당 튜플은 결과에 포함되지 않는다.

### 집계 함수에서의 처리

- `count(*)`를 제외한 모든 집계 함수는 NULL 값을 가진 튜플을 무시한다.
- 집계 대상 컬렉션이 비어 있을 때: `count`는 0을 반환하고, 나머지 함수는 null을 반환한다.

## Key Properties

- NULL은 "알 수 없음" 또는 "존재하지 않음"을 의미하며, 0이나 빈 문자열과 다른 개념이다
- `NULL = NULL`은 unknown이므로 NULL 동등 비교에는 반드시 `IS NULL`을 사용해야 한다
- `WHERE` 조건이 unknown으로 평가되면 해당 튜플은 결과에서 제외된다 (false와 동일하게 처리)
- 집계 함수는 NULL을 무시하므로, NULL이 많은 컬럼의 집계 결과 해석에 주의가 필요하다
- `primary key`로 선언된 속성은 자동으로 `NOT NULL`이 보장된다

## Relationships

- [[sql-ddl]] (NOT NULL 제약 선언 및 primary key와의 관계)
- [[sql-select-query]] (WHERE 절 평가 시 NULL의 영향)
- [[sql-aggregate-functions]] (집계 연산에서 NULL 처리 규칙)
- [[sql-subqueries]] (서브쿼리 결과에서 NULL 포함 집합의 처리)

## Open Questions

- NULL이 여러 개 있는 컬럼에 UNIQUE 제약을 적용할 때 DBMS별로 동작 방식이 다른가?
- 3-값 논리의 대안으로 NULL을 다르게 처리하는 데이터 모델(예: Codd의 4-값 논리)은 실용적으로 어떤 트레이드오프가 있는가?

## Sources

- raw/데이터베이스/SQL Basics.pdf
