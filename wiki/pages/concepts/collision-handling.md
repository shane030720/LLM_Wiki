---
title: Collision Handling
category: concept
tags: [collision, separate-chaining, open-addressing, linear-probing, quadratic-probing, double-hashing, hash-table]
sources: [raw/자료구조/CSE2112_02_week12_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Collision Handling(충돌 처리)은 hash table에서 서로 다른 key가 동일한 hash value를 가져 같은 버킷에 매핑될 때 이를 해결하는 전략이다. 크게 Separate Chaining(분리 연결법)과 Open Addressing(개방 주소법) 두 방식으로 나뉜다.

## How It Works

### Separate Chaining (분리 연결법, Closed Addressing)

각 버킷이 linked list를 가리키며, 동일한 hash value를 가진 항목들을 리스트에 연결하여 저장한다.
- 구현이 단순하나 테이블 외부에 추가 메모리(linked list 노드) 필요
- Load factor λ가 1 이상도 허용됨
- 예: h(k) = k mod 13 적용 시, 충돌하는 key들이 동일 버킷의 리스트에 연결

### Open Addressing (개방 주소법, Closed Hashing)

모든 항목을 hash table 배열 자체에 저장하며, λ ≤ 1 항상 유지. 빈 슬롯을 찾는 탐사(probing) 방식에 따라 세 가지로 나뉜다.

**1. Linear Probing (선형 탐사)**

충돌 시 다음 빈 슬롯을 순차적으로 탐색: A[(i + j) mod N], j = 0, 1, 2, ...

- 항목들이 연속으로 뭉치는 primary clustering 발생 → 이후 탐색에서 probe 수 증가
- 메모리 오버헤드 낮고 캐시 지역성(locality) 우수 → 실제로 가장 빠른 전략 중 하나

삭제 시 AVAILABLE 마커 사용:
- empty: 한 번도 사용되지 않은 슬롯 → 탐색 중단
- AVAILABLE: 사용 후 삭제된 슬롯 → 탐색 시 건너뜀, 삽입 시 재사용 가능

탐색 알고리즘 (find(k)):
```
i ← h(k), p ← 0
repeat
  c ← A[i]
  if c = empty: return null
  else if c.key() = k: return c.value()
  else: i ← (i + 1) mod N, p ← p + 1
until p = N
return null
```

**2. Quadratic Probing (이차 탐사)**

충돌 시 이차 함수 간격으로 탐색: A[(i + j²) mod N], j = 0, 1, 2, ...

- Linear probing의 primary clustering 문제 완화
- 예: 22 mod 7 = 1, 30 mod 7 = 2, 50 mod 7 = 1 → 50은 (1+0²)=1, (1+1²)=2, (1+2²)=5 순으로 탐색하여 슬롯 5에 저장

**3. Double Hashing (이중 해싱)**

보조 hash function d(k)를 사용하여 probe 간격 결정: (i + j·d(k)) mod N, j = 0, 1, ..., N-1

- d(k) ≠ 0 이어야 함
- 모든 슬롯 탐색을 보장하기 위해 N은 소수여야 함
- 보조 함수 일반 선택: d(k) = q − (k mod q), q < N이고 q는 소수 → d(k) ∈ {1, 2, ..., q}

예시 (N=13, h(k) = k mod 13, d(k) = 7 − k mod 7):

| k | h(k) | d(k) | Probes |
|---|------|------|--------|
| 18 | 5 | 3 | 5 |
| 41 | 2 | 1 | 2 |
| 44 | 5 | 5 | 5→10 |
| 31 | 5 | 4 | 5→9→0 |

## Key Properties

- Separate Chaining: 구현 단순, 추가 메모리 필요, λ 제한 없음
- Linear Probing: 캐시 친화적, 빠르나 clustering 발생
- Quadratic Probing: clustering 감소, 모든 슬롯 탐색 미보장 가능성
- Double Hashing: 가장 균일한 분포, N이 소수여야 함
- Open addressing expected probe 수: 1/(1−λ)
  - λ = 0.5 → 평균 2회 / λ = 0.99 → 평균 100회

## Relationships

- [[hash-table]] — collision handling이 적용되는 자료구조
- [[hash-function]] — double hashing에서 보조 hash function으로 활용

## Open Questions

- Primary clustering을 완전히 방지하면서 open addressing의 캐시 이점을 유지할 수 있는가?
- 삭제 연산이 빈번한 경우 AVAILABLE 마커의 누적이 장기적으로 성능에 미치는 영향은?
- 실제 구현 환경(캐시 크기, 메모리 제약)에 따라 separate chaining과 open addressing의 선택 기준은 무엇인가?

## Sources

- raw/자료구조/CSE2112_02_week12_1.pdf
