---
title: SQL Aggregate Functions
category: concept
tags: [sql, aggregate, group-by, having, avg, sum, count]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL 집계 함수(Aggregate Functions)는 관계의 특정 컬럼에 있는 값들의 집합(또는 멀티셋)에 대해 단일 스칼라 값을 반환하는 함수다. `GROUP BY`로 집계 단위 그룹을 정의하고, `HAVING`으로 그룹 수준의 조건을 지정한다.

## How It Works

### 기본 집계 함수

| 함수 | 설명 |
|------|------|
| `avg(col)` | 평균값 |
| `min(col)` | 최솟값 |
| `max(col)` | 최댓값 |
| `sum(col)` | 합계 |
| `count(col)` | NULL이 아닌 값의 행 수 |
| `count(*)` | NULL 포함 전체 행 수 |

```sql
-- Computer Science 학과 교수들의 평균 급여
select avg(salary)
from instructor
where dept_name = 'Comp. Sci.';

-- 2010년 봄학기에 강의한 교수의 수 (중복 제거)
select count(distinct ID)
from teaches
where semester = 'Spring' and year = 2010;

-- course 테이블의 전체 행 수
select count(*) from course;
```

### GROUP BY

그룹별 집계를 수행한다.

```sql
select dept_name, avg(salary) as avg_salary
from instructor
group by dept_name;
```

**중요 제약**: `SELECT` 절에서 집계 함수 밖에 나오는 속성은 반드시 `GROUP BY` 절에 포함되어야 한다. 그렇지 않으면 오류다.

```sql
-- 오류: ID는 group by에 없으므로 집계 함수 밖에서 사용 불가
select dept_name, ID, avg(salary)
from instructor
group by dept_name;
```

### HAVING

그룹 형성 이후에 적용되는 조건이다.

```sql
select dept_name, avg(salary)
from instructor
group by dept_name
having avg(salary) > 42000;
```

`WHERE`는 개별 튜플 단위로 그룹 형성 전에 평가되고, `HAVING`은 그룹 형성 후 그룹 단위로 평가된다.

### NULL 값과 집계

- `count(*)`를 제외한 모든 집계 함수는 NULL 값을 가진 튜플을 무시한다.
- 집계 대상 컬렉션이 비어 있을 때: `count`는 0을 반환하고, 나머지 함수는 `null`을 반환한다.

## Key Properties

- `WHERE`는 개별 튜플 필터링 (그룹 형성 전), `HAVING`은 그룹 필터링 (그룹 형성 후)
- `SELECT` 절에 집계 함수와 일반 속성을 함께 쓸 때, 일반 속성은 반드시 `GROUP BY`에 포함해야 한다
- `count(*)`만이 NULL을 포함한 모든 행을 센다; `count(col)`은 NULL을 무시한다
- 빈 컬렉션에 대해 `count`는 0, 나머지 집계 함수는 NULL을 반환한다

## Relationships

- [[sql-select-query]] (집계 함수가 사용되는 SELECT 질의의 기본 구조)
- [[sql-null-values]] (NULL 값의 집계 처리 방식)
- [[sql-subqueries]] (HAVING 절 내 서브쿼리 활용, WITH 절을 이용한 다단계 집계)

## Open Questions

- `GROUP BY ROLLUP`, `CUBE`, `GROUPING SETS` 등 확장 집계 연산(SQL:1999 이후)의 동작 방식은?
- 대규모 데이터셋에서 `GROUP BY` 성능 최적화에 사용되는 해싱 vs 정렬 기반 전략의 차이는?

## Sources

- raw/데이터베이스/SQL Basics.pdf
