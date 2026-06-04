---
title: Vector ADT
category: concept
tags: [vector, array-list, adt, data-structure, index]
sources: [raw/자료구조/CSE2112_02_week05_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Vector(또는 Array List) ADT는 배열의 개념을 확장하여 객체의 시퀀스를 저장하는 추상 자료형이다. 각 요소는 인덱스(앞에 위치한 요소의 수)로 접근, 삽입, 제거된다. 잘못된 인덱스(예: 음수 인덱스)를 사용하면 예외가 발생한다.

## How It Works

**주요 연산:**
- `at(i)`: 인덱스 i의 요소 반환 (제거 없음)
- `set(i, o)`: 인덱스 i의 요소를 o로 교체
- `insert(i, o)`: 인덱스 i에 새 요소 o 삽입 — A[i]부터 A[n-1]까지 한 칸씩 앞으로 이동
- `erase(i)`: 인덱스 i의 요소 제거 — A[i+1]부터 A[n-1]까지 한 칸씩 뒤로 이동
- `size()`, `empty()`

**Growable Array (동적 배열):**
배열이 꽉 찼을 때(n == N) 더 큰 새 배열로 교체한다.
- Incremental strategy: 크기를 상수 c씩 증가
- Doubling strategy: 크기를 2배로 증가 (amortized 효율 면에서 일반적으로 선호)

```
Algorithm insert(o):  // 끝에 삽입
  if n = N then
    A ← new array of size 2N   {Doubling}
    for i ← 0 to n-1 do A[i] ← S[i]
    delete S; S ← A; N ← 2N
  S[n] ← o
  n ← n + 1
```

## Key Properties
- 인덱스 기반 임의 접근: at(i), set(i, o) 모두 O(1)
- insert(i, o) / erase(i): 최악의 경우(i=0) O(n), 요소 이동 필요
- insertLast(e): 배열이 여유 있을 때 O(1), 꽉 찼을 때 O(n)
- 공간 복잡도: O(N) (N = 배열의 capacity, N >= n)
- Doubling 전략 사용 시 insertLast의 amortized 복잡도 O(1)

| 연산 | 복잡도 |
|------|--------|
| size(), empty() | O(1) |
| at(i), set(i, e) | O(1) |
| insert(i, e) | O(n) |
| insertLast(e) | O(1) / O(n) if full |
| erase(i) | O(n) |

## Relationships
- [[list-adt]] (인덱스 대신 Position을 사용하는 대응 ADT; insert/erase O(1) 가능)
- [[sequence-adt]] (Vector와 List를 통합한 상위 ADT)
- [[queue]] (Circular Array 기반 Queue 구현의 토대)

## Open Questions
- Incremental strategy와 Doubling strategy의 amortized 삽입 비용을 정확히 비교하면 어떻게 되는가?
- Doubling 시 메모리 단편화 문제와 실질적 한계는 무엇인가?

## Sources
- raw/자료구조/CSE2112_02_week05_1.pdf
