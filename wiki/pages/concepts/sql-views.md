---
title: SQL Views
category: concept
tags: [sql, view, virtual-relation, database]
sources: [raw/데이터베이스/Intermediate SQL.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

View(뷰)는 실제 데이터베이스에 물리적으로 저장된 릴레이션이 아닌 가상 릴레이션(virtual relation)이다. `CREATE VIEW` 문으로 정의되며, 쿼리 결과를 저장하는 것이 아니라 쿼리 표현식 자체를 저장한다. 특정 사용자에게 데이터의 일부만 노출하거나 복잡한 쿼리를 단순화하는 메커니즘으로 활용된다.

## How It Works

**뷰 정의 (View Definition)**

```sql
CREATE VIEW v AS <query expression>
```

뷰를 참조하는 쿼리 실행 시 저장된 표현식이 해당 위치에 substitution(대입)된다. Precomputed 결과가 아니다.

```sql
-- 급여를 제외한 강사 정보 뷰
CREATE VIEW faculty AS
    SELECT ID, name, dept_name
    FROM instructor;

-- 학과별 급여 합계 뷰
CREATE VIEW departments_total_salary(dept_name, total_salary) AS
    SELECT dept_name, SUM(salary)
    FROM instructor
    GROUP BY dept_name;
```

**뷰를 기반으로 한 뷰 정의**

다른 뷰를 기반으로 새로운 뷰를 중첩 정의할 수 있다.

```sql
CREATE VIEW physics_fall_2009 AS
    SELECT course.course_id, sec_id, building, room_number
    FROM course, section
    WHERE course.course_id = section.course_id
      AND course.dept_name = 'Physics'
      AND section.semester = 'Fall'
      AND section.year = '2009';

CREATE VIEW physics_fall_2009_watson AS
    SELECT course_id, room_number
    FROM physics_fall_2009
    WHERE building = 'Watson';
```

**뷰 갱신 (Update of a View)**

뷰에 대한 삽입/수정은 기저 릴레이션(base relation)에 반영되어야 한다. 예를 들어 `faculty` 뷰에 `('30765', 'Green', 'Music')`을 삽입하면 기저 릴레이션인 `instructor`에 `('30765', 'Green', 'Music', null)`이 삽입된다.

**Updatable View 조건**

SQL 뷰가 updatable(갱신 가능)로 간주되려면 다음 조건을 모두 만족해야 한다.

1. `FROM` 절에 하나의 데이터베이스 릴레이션만 포함
2. `SELECT` 절에 속성 이름만 포함 (표현식, 집계함수, `DISTINCT` 없음)
3. `SELECT`에 없는 속성은 null로 설정 가능
4. `GROUP BY` 또는 `HAVING` 절 없음

**WITH CHECK OPTION**

뷰 정의의 `WHERE` 조건을 만족하지 않는 행의 삽입을 방지한다. `history_instructors` 뷰(`dept_name = 'History'`)에 Biology 학과 강사를 삽입하려 하면 뷰 조건을 위반하므로 `WITH CHECK OPTION` 선언 시 차단된다.

## Key Properties

- 뷰는 precomputed 결과가 아닌 쿼리 표현식으로 저장된다.
- 갱신이 유일하게 변환될 수 없는 경우(예: 여러 학과가 동일 건물에 있을 때) 뷰 갱신은 거부된다.
- 뷰는 데이터 은닉(data hiding)과 논리적 독립성(logical independence)을 제공한다.
- 중첩된 뷰 정의가 가능하다.
- `WITH CHECK OPTION`으로 뷰 조건에 위배되는 삽입을 방지할 수 있다.

## Relationships

- [[sql-join-expressions]] (뷰 정의 내 쿼리 표현식에서 조인 연산을 사용할 수 있다)
- [[sql-integrity-constraints]] (updatable view의 허용 조건과 무결성 제약이 상호작용한다)
- [[sql-transactions]] (뷰 갱신은 트랜잭션 컨텍스트 내에서 처리된다)

## Open Questions

- Materialized View(구체화 뷰)는 일반 뷰와 달리 결과를 저장하는데, 두 방식의 성능 trade-off는 무엇인가?
- 뷰 중첩 깊이가 쿼리 최적화기(query optimizer)에 미치는 영향은 어떠한가?

## Sources

- raw/데이터베이스/Intermediate SQL.pdf (p.12–p.18)
