---
title: SQL Transactions
category: concept
tags: [sql, transaction, atomicity, isolation, database]
sources: [raw/데이터베이스/Intermediate SQL.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Transaction(트랜잭션)은 데이터베이스에서 하나의 논리적 작업 단위(unit of work)이다. 원자성(atomicity)을 보장하여 트랜잭션 내 모든 연산이 완전히 수행되거나, 오류 발생 시 전혀 수행되지 않은 것처럼 롤백된다. 또한 동시 실행 중인 다른 트랜잭션으로부터 격리(isolation)된다.

## How It Works

트랜잭션은 묵시적으로 시작된다. 종료는 다음 두 가지 방법으로 이루어진다.

- `COMMIT WORK`: 트랜잭션의 모든 변경을 확정하여 데이터베이스에 영구 반영한다.
- `ROLLBACK WORK`: 트랜잭션의 모든 변경을 취소하고 이전 상태로 복원한다. (`WORK` 키워드는 선택적이다.)

대부분의 데이터베이스는 기본적으로 각 SQL 문을 자동으로 커밋하는 **auto-commit** 모드로 동작한다. API를 통해 세션 단위로 auto-commit을 비활성화할 수 있다.

SQL:1999에서는 명시적 트랜잭션 블록을 다음 구문으로 정의할 수 있다.

```sql
BEGIN ATOMIC
    ...
END
```

**트랜잭션 내 무결성 제약 지연**

상호 참조 삽입(예: 서로를 배우자로 참조하는 두 사람)처럼 삽입 순서로 인해 일시적 제약 위반이 불가피한 경우, 제약 검사를 트랜잭션 종료 시점까지 지연할 수 있다.

```sql
SET CONSTRAINTS spouse_ref DEFERRED
```

## Key Properties

- **원자성(Atomicity)**: 트랜잭션 내 모든 연산이 완전히 수행되거나, 전혀 수행되지 않는다.
- **격리성(Isolation)**: 동시 실행 중인 다른 트랜잭션의 중간 변경 사항으로부터 격리된다.
- 기본 auto-commit 모드에서는 각 SQL 문이 독립적인 트랜잭션으로 처리된다.
- 무결성 제약 위반은 트랜잭션 내에서 `DEFERRED`로 지연될 수 있어 복잡한 삽입 시나리오를 처리할 수 있다.

## Relationships

- [[sql-integrity-constraints]] (트랜잭션 내에서 무결성 제약 위반을 `DEFERRED`로 지연 처리할 수 있다)
- [[sql-views]] (뷰 갱신은 트랜잭션 컨텍스트 내에서 처리된다)

## Open Questions

- ACID 특성(원자성, 일관성, 격리성, 지속성) 중 이 자료에서는 원자성과 격리성만 다루는데, 일관성(Consistency)과 지속성(Durability)은 어떻게 구현적으로 보장되는가?
- 격리 수준(READ COMMITTED, REPEATABLE READ, SERIALIZABLE)에 따라 트랜잭션 동작이 어떻게 달라지는가?

## Sources

- raw/데이터베이스/Intermediate SQL.pdf (p.19)
