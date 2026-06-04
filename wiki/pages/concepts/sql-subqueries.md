---
title: SQL Subqueries
category: concept
tags: [sql, subquery, exists, in, with, derived-relation, correlated-subquery]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL 서브쿼리(subquery)는 다른 쿼리 내부에 중첩된 `SELECT-FROM-WHERE` 표현식이다. 집합 멤버십 검사, 집합 비교, 공집합 검사, 중복 부재 검사 등을 표현하는 데 활용된다. 서브쿼리는 `WHERE` 절, `FROM` 절, `SELECT` 절 어디에도 위치할 수 있다.

## How It Works

### IN / NOT IN — 집합 멤버십 검사

```sql
-- Fall 2009와 Spring 2010 모두 개설된 강좌
select distinct course_id from section
where semester = 'Fall' and year = 2009 and
      course_id in (select course_id from section
                    where semester = 'Spring' and year = 2010);

-- Fall 2009에는 있지만 Spring 2010에는 없는 강좌
select distinct course_id from section
where semester = 'Fall' and year = 2009 and
      course_id not in (select course_id from section
                        where semester = 'Spring' and year = 2010);
```

### SOME — 존재 비교

`F <comp> some r`: r에 F와의 비교를 만족하는 튜플이 하나 이상 존재하면 true.

```sql
select name from instructor
where salary > some (select salary from instructor
                     where dept_name = 'Biology');
```

- `= some` ≡ `in`
- `<> some` ≢ `not in` (주의)

### ALL — 전체 비교

`F <comp> all r`: r의 모든 튜플에 대해 비교가 만족되면 true.

```sql
select name from instructor
where salary > all (select salary from instructor
                    where dept_name = 'Biology');
```

- `<> all` ≡ `not in`
- `= all` ≢ `in` (주의)

### EXISTS / NOT EXISTS — 공집합 검사

`exists r`은 r이 비어 있지 않으면 true, `not exists r`은 r이 비어 있으면 true.

```sql
-- Correlated subquery: 외부 쿼리 변수 S를 내부 서브쿼리에서 참조
select course_id from section as S
where semester = 'Fall' and year = 2009 and
      exists (select * from section as T
              where semester = 'Spring' and year = 2010
                    and S.course_id = T.course_id);
```

**"모든 X에 대해" 패턴** — `not exists (A except B)`는 A ⊆ B를 표현한다:

```sql
-- Biology 학과의 모든 강좌를 수강한 학생
select distinct S.ID, S.name from student as S
where not exists (
    (select course_id from course where dept_name = 'Biology')
    except
    (select T.course_id from takes as T where S.ID = T.ID)
);
```

### UNIQUE — 중복 부재 검사

서브쿼리 결과에 중복 튜플이 없으면 true.

```sql
-- 2009년에 최대 1회만 개설된 강좌
select T.course_id from course as T
where unique (select R.course_id from section as R
              where T.course_id = R.course_id and R.year = 2009);
```

### FROM 절 서브쿼리 — Derived Relations (파생 관계)

서브쿼리를 `FROM` 절에서 임시 가상 테이블로 활용한다.

```sql
select dept_name, avg_salary
from (select dept_name, avg(salary) as avg_salary
      from instructor
      group by dept_name) as dept_avg
where avg_salary > 42000;
```

`HAVING` 절 없이도 집계 결과에 조건을 적용할 수 있어 쿼리 구조를 유연하게 구성할 수 있다.

### WITH 절 — Common Table Expression (CTE)

쿼리 내에서만 유효한 임시 뷰를 정의한다. 여러 CTE를 체인으로 연결할 수 있다.

```sql
with max_budget(value) as (
    select max(budget) from department
)
select budget from department, max_budget
where department.budget = max_budget.value;

-- 다중 CTE 체인
with dept_total(dept_name, value) as (
        select dept_name, sum(salary) from instructor group by dept_name),
     dept_total_avg(value) as (
        select avg(value) from dept_total)
select dept_name
from dept_total, dept_total_avg
where dept_total.value >= dept_total_avg.value;
```

### Scalar Subquery — 스칼라 서브쿼리

단일 값을 반환하는 서브쿼리로, `SELECT` 절이나 `WHERE` 절에서 단일 값처럼 사용한다.

```sql
select dept_name,
       (select count(*) from instructor
        where department.dept_name = instructor.dept_name) as num_instructors
from department;
```

## Key Properties

- `= some` ≡ `in`, `<> all` ≡ `not in` — 이 두 등가 관계의 반대 방향은 성립하지 않는다
- Correlated subquery는 외부 쿼리의 각 행(correlation variable)에 대해 내부 쿼리가 재평가된다
- `not exists (A except B)` 패턴은 "A의 모든 원소가 B에 포함"됨을 표현하는 표준 기법이다
- `WITH` 절(CTE)은 복잡한 쿼리의 가독성을 향상시키고 동일 서브쿼리를 여러 번 참조할 때 유용하다
- Scalar subquery가 둘 이상의 값을 반환하면 런타임 오류가 발생한다

## Relationships

- [[sql-select-query]] (서브쿼리가 포함되는 기본 질의 구조)
- [[sql-aggregate-functions]] (서브쿼리 내 집계 함수 활용)
- [[sql-null-values]] (서브쿼리 결과에서 NULL 처리)

## Open Questions

- Correlated subquery와 동등한 JOIN 표현 중 어느 쪽이 성능상 우월한지는 DBMS 옵티마이저에 따라 얼마나 달라지는가?
- `UNIQUE` 구문은 주요 상용 DBMS(PostgreSQL, MySQL, Oracle, SQL Server)에서 모두 지원되는가?

## Sources

- raw/데이터베이스/SQL Basics.pdf
