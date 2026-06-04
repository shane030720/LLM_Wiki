---
title: Hash Function
category: concept
tags: [hash-function, hash-code, compression-function, collision, hash-table]
sources: [raw/자료구조/CSE2112_02_week12_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Hash Function(해시 함수)은 임의의 key를 hash table의 bucket 인덱스 [0, N-1]로 변환하는 함수 h이다. 일반적으로 두 단계의 합성 함수 h(x) = h2(h1(x))로 정의된다.

## How It Works

Hash function은 두 단계로 구성된다:

**1단계 — Hash Code** h1: keys → integers
- 임의의 key를 정수로 변환
- key의 타입(문자열, 객체 등)에 따라 다양하게 설계

**2단계 — Compression Function** h2: integers → [0, N-1]
- 정수를 배열 범위 내로 압축
- 가장 단순한 예: h2(y) = y mod N
- Double hashing에서 보조 함수: d(k) = q − (k mod q), 여기서 q < N이고 q는 소수

**구체적 예시** (SSN을 key로 사용하는 경우):
- N = 10,000, h(x) = x의 마지막 4자리
- h(451-229-0004) → 버킷 4, h(981-101-0002) → 버킷 2, h(200-751-9998) → 버킷 9998

**Collision 발생 예시**:
- h(k) = k mod 5 일 때, h(12) = 2, h(17) = 2 → collision 발생

## Key Properties

- 결정론적(deterministic): 동일한 key는 항상 동일한 hash value를 반환해야 한다
- 균일 분포(uniform distribution): key들을 버킷에 고르게 분산시켜야 "good" hash function
- 계산 효율성: O(1)에 가깝게 빠르게 계산 가능해야 한다
- Collision 불가피성: n > N 이면 Pigeonhole Principle에 의해 반드시 collision 발생 (n+1개 항목을 n개 버킷에 넣으면 반드시 하나 이상 겹침)

## Relationships

- [[hash-table]] — hash function이 적용되는 자료구조
- [[collision-handling]] — collision 발생 시 처리 전략; double hashing에서는 보조 hash function으로도 사용됨

## Open Questions

- 특정 key 집합에 대해 collision이 전혀 없는 perfect hash function을 어떻게 설계하는가?
- 문자열·복합 객체 등 비정수형 key에 대한 hash code 설계의 표준적 접근법은 무엇인가?
- Cryptographic hash function과 일반 hash function의 차이는 hash table 성능에 어떤 영향을 주는가?

## Sources

- raw/자료구조/CSE2112_02_week12_1.pdf
