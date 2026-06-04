---
title: SQL SELECT Query
category: concept
tags: [sql, select, query, join, natural-join, set-operation, order-by]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL SELECT 질의는 하나 이상의 관계에서 조건을 만족하는 튜플들의 특정 속성 값을 추출하는 연산이다. 관계 대수의 projection, selection, Cartesian product에 대응하는 `SELECT`, `WHERE`, `FROM` 절로 구성되며, 질의 결과 역시 하나의 관계다.

## How It Works

### 기본 구조

```sql
select A1, A2, ..., An
from r1, r2, ..., rm
where P
```

- `SELECT`: 결과에 포함할 속성 나열 — 관계 대수의 projection에 대응
- `FROM`: 질의에 관여하는 관계 나열 — Cartesian product 생성에 대응
- `WHERE`: 결과 튜플이 만족해야 하는 조건 — 관계 대수의 selection에 대응

### SELECT 절 주요 기능

```sql
select distinct dept_name from instructor;           -- 중복 제거
select all dept_name from instructor;                -- 중복 허용 (기본값)
select * from instructor;                            -- 모든 속성
select ID, name, salary/12 as monthly_salary         -- 산술 표현식 + 별칭
from instructor;
```

SQL은 기본적으로 중복 튜플을 허용(multiset 의미론)하므로 중복 제거가 필요하면 `DISTINCT`를 명시해야 한다.

### WHERE 절 조건

```sql
-- 논리 연산자
where dept_name = 'Comp. Sci.' and salary > 80000

-- BETWEEN (경계 포함)
where salary between 90000 and 100000

-- 튜플 비교
where (instructor.ID, dept_name) = (teaches.ID, 'Biology')
```

비교 결과는 `and`, `or`, `not`으로 결합할 수 있다.

### JOIN

**Cartesian product + WHERE 조건** (묵시적 조인):

```sql
select name, course_id
from instructor, teaches
where instructor.ID = teaches.ID;
```

**Natural join** — 공통 속성 값이 모두 동일한 튜플만 매칭, 공통 컬럼은 한 번만 표시:

```sql
select name, course_id
from instructor natural join teaches;
```

Natural join의 위험: 이름이 같지만 의미상 무관한 속성이 있으면 의도하지 않은 조인이 발생한다. 이 경우 `join ... using(attr)` 구문으로 조인 기준 속성을 명시하는 것이 안전하다.

```sql
-- 잘못된 버전: course.dept_name과 instructor.dept_name이 의도치 않게 조인됨
select name, title
from instructor natural join teaches natural join course;

-- 올바른 버전
select name, title
from (instructor natural join teaches) join course using(course_id);
```

### 이름 변경 (AS / Rename)

```sql
select distinct T.name
from instructor as T, instructor as S
where T.salary > S.salary and S.dept_name = 'Comp. Sci.';
```

`AS`는 생략 가능하다(`instructor T` ≡ `instructor as T`). 동일 테이블을 두 번 참조하는 self-join에 필수적이다.

### 문자열 패턴 매칭 (LIKE)

```sql
where name like '%dar%'           -- 'dar'를 포함하는 임의 문자열
where s like '100 \%' escape '\'  -- 리터럴 '%' 문자 매칭
```

- `%`: 임의 부분 문자열 (0자 이상)
- `_`: 임의 단일 문자 정확히 1개

### 정렬 (ORDER BY)

```sql
select distinct name from instructor order by name desc;
order by dept_name asc, name desc;   -- 다중 속성 정렬 (asc가 기본값)
```

### 집합 연산 (Set Operations)

```sql
(select course_id from section where sem = 'Fall' and year = 2009)
union
(select course_id from section where sem = 'Spring' and year = 2010);

intersect   -- 교집합

except      -- 차집합

union all / intersect all / except all   -- 중복 유지 버전
```

`union`, `intersect`, `except`는 기본적으로 중복을 제거한다. `all` 버전에서 튜플이 r에 m번, s에 n번 등장하면: `union all`은 m+n번, `intersect all`은 min(m,n)번, `except all`은 max(0, m-n)번 나타난다.

## Key Properties

- SQL은 multiset 의미론을 기본으로 하므로 중복 튜플이 결과에 포함될 수 있다; 제거하려면 `DISTINCT` 필요
- `FROM` 절의 여러 테이블은 Cartesian product를 생성하며, `WHERE` 조건이 의미 있는 조인으로 변환한다
- Natural join은 편리하지만 동명이지만 의미가 다른 속성으로 인한 오류에 취약하다
- SQL 키워드 및 식별자는 대소문자를 구분하지 않는다 (`Name` ≡ `NAME` ≡ `name`)
- 집합 연산(`union`, `intersect`, `except`)은 기본적으로 중복을 제거한다

## Relationships

- [[sql]] (SELECT 질의가 속하는 SQL 언어 전체)
- [[sql-aggregate-functions]] (SELECT와 함께 사용되는 집계 연산 및 GROUP BY)
- [[sql-subqueries]] (SELECT 내부에 중첩되는 서브쿼리)
- [[sql-null-values]] (WHERE 조건 평가 시 NULL 처리 방식)

## Open Questions

- Natural join 대신 `USING` 절과 `ON` 절 중 언제 어떤 것을 쓰는 것이 더 적절한가?
- Cartesian product가 포함된 쿼리에 대해 DBMS가 내부적으로 어떤 최적화를 수행하는가?

## Sources

- raw/데이터베이스/SQL Basics.pdf
