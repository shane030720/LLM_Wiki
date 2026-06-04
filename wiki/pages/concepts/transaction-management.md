```markdown
---
title: Transaction Management
category: concept
tags: [transaction, atomicity, consistency, concurrency, database]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Transaction Management는 데이터베이스에서 일련의 연산이 원자적(atomic)으로 수행되도록 보장하는 메커니즘이다. Transaction은 단일 작업을 위한 일련의 연산들의 집합으로, 모든 연산이 완전히 완료되거나 전혀 수행되지 않아야 한다(all-or-nothing). [[database-management-system]] 내 Transaction Manager가 이를 담당한다.

## How It Works

Transaction Manager는 Storage Manager의 핵심 컴포넌트로 다음을 보장한다.

1. **Atomicity 보장**: 트랜잭션 내 연산 전부 완료 또는 전부 취소
2. **Consistency 보장**: 장애 발생 시에도 데이터베이스의 일관성 유지

**은행 계좌 이체 예시 (A에서 B로 50 이체)**:
- A에서 50 차감
- B에 50 추가
→ 위 두 연산은 반드시 함께 완료되거나 함께 취소되어야 함; 중간 상태(A만 차감됨)는 허용 불가

파일 시스템의 두 가지 핵심 문제:
- **부분 업데이트(partial update)**: 장애 발생 시 일부 연산만 완료된 상태로 남을 수 있음
- **동시성 문제(concurrency issue)**: 두 사용자가 동시에 잔액 100을 읽고 각각 50씩 출금 시, 최종 잔액이 50이 되어야 하나 0이 되는 불일치 발생

## Key Properties

- **Atomicity**: 트랜잭션 내 모든 연산은 전부 완료되거나 전부 취소
- **Consistency**: 트랜잭션 수행 전후로 데이터베이스 무결성 유지
- **Concurrency Control**: 다중 사용자 환경에서 동시 접근 시에도 일관성 있는 결과 보장
- **Failure Recovery**: 장애 발생 후 일관된 상태로 복구

## Relationships

- [[database]] (Transaction Management가 적용되는 시스템)
- [[database-management-system]] (Transaction Manager가 내장된 소프트웨어)
- [[query-processing]] (트랜잭션 내에서 실행되는 SQL 질의들의 처리 과정)

## Open Questions

- ACID(Atomicity, Consistency, Isolation, Durability) 속성을 모두 만족하면서 성능을 극대화하는 방법은?
- 분산 데이터베이스 환경에서 트랜잭션의 원자성은 어떻게 보장되는가? (2-Phase Commit의 한계는?)

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
