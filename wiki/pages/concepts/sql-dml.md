---
title: SQL DML – Data Modification (INSERT, UPDATE, DELETE)
category: concept
tags: [sql, dml, insert, update, delete, case, modification]
sources: [raw/데이터베이스/SQL Basics.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL 데이터 수정 언어는 기존 관계의 내용을 변경하는 명령어 집합이다. `DELETE`(튜플 삭제), `INSERT`(튜플 삽입), `UPDATE`(속성 값 변경)의 세 가지 유형이 있으며, 각각 서브쿼리와 결합하여 복잡한 조건을 표현할 수 있다.

## How It Works

### DELETE

```sql
-- 모든 행 삭제
delete from instructor;

-- 조건부 삭제
delete from instructor
where dept_name = 'Finance';

-- 서브쿼리를 이용한 삭제
delete from instructor
where dept_name in (select dept_name from department
                    where building = 'Watson');

-- 집계 서브쿼리를 이용한 삭제
delete from instructor
where salary < (select avg(salary) from instructor);
```

마지막 예시에서 SQL은 먼저 평균 급여와 삭제 대상 튜플을 모두 식별한 후 삭제를 수행한다. 따라서 삭제 도중 평균이 변하는 문제가 발생하지 않는다.

### INSERT

```sql
-- 값 직접 지정
insert into course values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);

-- 컬럼 순서 명시적 지정 (선언 순서와 달라도 됨)
insert into course (course_id, title, dept_name, credits)
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);

-- NULL 값 삽입
insert into student values ('3003', 'Green', 'Finance', null);

-- 서브쿼리 결과 삽입 (모든 교수를 tot_cred = 0으로 student에 추가)
insert into student
select ID, name, dept_name, 0
from instructor;
```

`INSERT ... SELECT` 구문에서 `SELECT`는 `INSERT` 이전에 완전히 평가된다. 따라서 동일 테이블에서 읽어 삽입하는 경우에도 안전하다.

### UPDATE

```sql
-- 단순 조건부 갱신 (순서에 따라 결과가 달라질 수 있음)
update instructor
set salary = salary * 1.03
where salary > 100000;

update instructor
set salary = salary * 1.05
where salary <= 100000;

-- CASE 문을 이용한 단일 패스 갱신 (권장)
update instructor
set salary = case
                 when salary <= 100000 then salary * 1.05
                 else salary * 1.03
             end;

-- 스칼라 서브쿼리를 이용한 갱신
update student S
set tot_cred = (
    select sum(credits)
    from takes natural join course
    where S.ID = takes.ID
      and takes.grade <> 'F'
      and takes.grade is not null
);
```

여러 개의 `UPDATE` 문을 순서대로 실행하면 앞 문장의 결과가 뒤 문장의 조건에 영향을 줄 수 있다. `CASE` 문으로 하나로 묶으면 한 번의 패스로 처리되어 이 문제를 피할 수 있다.

## Key Properties

- `DELETE`는 테이블에서 튜플 전체를 제거한다; 특정 속성만 null로 만들려면 `UPDATE ... SET col = null`을 사용한다
- 서브쿼리가 포함된 `DELETE`는 먼저 삭제 대상 집합을 완전히 결정한 후 삭제를 수행하므로 집계값 변동 문제가 없다
- `UPDATE ... CASE`는 여러 조건을 단일 패스로 처리하므로 다중 `UPDATE`보다 안전하고 일반적으로 더 효율적이다
- 스칼라 서브쿼리를 `SET` 절에 사용하면 다른 테이블의 계산 결과를 기반으로 값을 갱신할 수 있다

## Relationships

- [[sql-ddl]] (수정 대상이 되는 스키마 정의)
- [[sql-select-query]] (DELETE/UPDATE의 WHERE 절에서 사용되는 서브쿼리 구조)
- [[sql-null-values]] (삽입·갱신 시 NULL 처리 및 IS NULL 조건)
- [[sql-subqueries]] (DELETE/UPDATE/INSERT에 사용되는 서브쿼리)

## Open Questions

- 대용량 테이블에서 `DELETE without WHERE`와 `TRUNCATE TABLE`의 성능·트랜잭션 처리 차이는?
- `INSERT ... SELECT`에서 동일 테이블을 참조할 때 모든 DBMS가 동일하게 안전하게 처리하는가?

## Sources

- raw/데이터베이스/SQL Basics.pdf
