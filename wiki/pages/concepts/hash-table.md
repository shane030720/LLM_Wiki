---
title: Hash Table
category: concept
tags: [hash-table, data-structure, map, bucket-array, load-factor, rehashing]
sources: [raw/자료구조/CSE2112_02_week12_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Hash Table(해시 테이블)은 key-value 쌍을 저장하는 자료구조로, hash function을 통해 key를 bucket array의 인덱스로 변환함으로써 평균 O(1) 시간복잡도로 탐색·삽입·삭제를 수행한다. Bucket array와 hash function 두 가지 핵심 구성 요소로 이루어진다.

## How It Works

1. **Bucket Array**: N개의 슬롯을 가진 배열 A. 각 슬롯(bucket)은 하나 이상의 key-value 쌍을 담을 수 있다.
2. **Hash Function**: key k를 받아 배열 인덱스 h(k) ∈ [0, N-1]을 반환한다.
3. key k를 가진 항목은 A[h(k)] 버킷에 저장된다.
4. key가 정수이고 [0, N-1] 범위에 고르게 분포된다면 직접 인덱스 접근과 동일하여 O(1)이 된다.

**Load Factor**: λ = n/N (n: 저장된 항목 수, N: 버킷 배열 크기)
- λ가 클수록 collision 확률 증가
- Open addressing에서 λ ≤ 1이며, 성능 보장을 위해 낮게 유지해야 한다

**Rehashing**: λ가 임계값을 초과하면 배열 크기를 최소 2배로 늘리고 새 hash function으로 모든 항목을 재삽입한다. Vector의 doubling 전략과 유사하다.

**시간복잡도 비교**:

| 자료구조 | 평균 | 최악 |
|---------|------|------|
| Binary Search Tree | Θ(log n) | O(n) |
| AVL Tree | Θ(log n) | O(log n) |
| Hash Table | Θ(1) | O(n) |

## Key Properties

- 평균 시간복잡도: Θ(1) (탐색·삽입·삭제 모두)
- 최악 시간복잡도: O(n) — 모든 key가 동일한 hash value를 가질 때 발생
- Open addressing에서 expected probe 수 = 1/(1−λ)
  - λ = 0.5 이면 평균 2회 probe
  - λ = 0.99 이면 평균 100회 probe
- 실용적 응용: 소규모 데이터베이스, 컴파일러 심볼 테이블, 브라우저 캐시

## Relationships

- [[hash-function]] — hash table의 핵심 구성 요소로 key를 bucket 인덱스로 변환
- [[collision-handling]] — 동일한 hash value를 가진 key들을 처리하는 전략
- [[dictionary-adt]] — hash table이 구현하는 추상 자료형

## Open Questions

- Hash function의 품질을 실제로 어떻게 측정하고 보장할 수 있는가?
- Rehashing 중 동시 접근(concurrent access)이 발생하면 어떻게 처리하는가?
- 최악의 경우 O(n)을 완전히 방지할 수 있는 hash table 구조가 존재하는가? (예: perfect hashing, cuckoo hashing)

## Sources

- raw/자료구조/CSE2112_02_week12_1.pdf
