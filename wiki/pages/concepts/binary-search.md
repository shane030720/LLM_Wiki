---
title: Binary Search
category: concept
tags: [search, algorithm, sorted-array, data-structure]
sources: [raw/자료구조/CSE2112_02_week12_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Binary Search(이진 탐색)는 정렬된 배열에서 목표 키를 탐색할 때, 매 단계마다 탐색 범위를 절반으로 줄여 O(log n) 시간에 탐색을 완료하는 알고리즘이다. "High-Low 게임"과 동일한 원리로 동작한다.

## How It Works

1. `low = 0`, `high = n - 1`로 초기화한다.
2. 중간 인덱스 `mid = floor((low + high) / 2)`를 계산한다.
3. `L[mid].key()`와 목표 키 k를 비교한다:
   - `k == L[mid].key()`: 탐색 성공, mid 반환
   - `k < L[mid].key()`: `high = mid - 1`로 왼쪽 절반으로 범위 축소
   - `k > L[mid].key()`: `low = mid + 1`로 오른쪽 절반으로 범위 축소
4. `low > high`가 되면 탐색 실패, end 반환

### 재귀적 구현

```
Algorithm BinarySearch(L, k, low, high):
  if low > high then
    return end
  mid <- floor((low + high) / 2)
  if k = L[mid].key() then
    return mid
  else if k < L[mid].key() then
    return BinarySearch(L, k, low, mid-1)
  else
    return BinarySearch(L, k, mid+1, high)
```

초기 호출: `BinarySearch(L, k, 0, n-1)`

### 반복적 구현

```
Algorithm BinarySearch(L, k):
  low <- 0
  high <- n - 1
  while (low <= high) {
    mid <- floor((low + high) / 2)
    if k = L[mid].key() then return mid
    else if k < L[mid].key() then high <- mid - 1
    else low <- mid + 1
  }
```

### 예시: find(7), n=13

```
index:  0  1  2  3  4  5  6  7  8  9  10  11  12
값:     1  3  4  5  7  8  9  11 14  16  18  19

1단계: l=0,  h=12, m=6  → L[6]=9  > 7 → h=5
2단계: l=0,  h=5,  m=2  → L[2]=4  < 7 → l=3
3단계: l=3,  h=5,  m=4  → L[4]=7  = 7 → 반환
```

## Key Properties

- 전제 조건: 배열이 키 기준으로 정렬되어 있어야 한다
- 시간 복잡도: O(log n)
- 공간 복잡도: 반복적 구현 O(1), 재귀적 구현 O(log n) 스택 사용
- 매 단계마다 탐색 후보 수가 절반으로 줄어든다
- 로그 횟수 이후 종료가 보장된다

## Relationships

- [[dictionary-adt]] (Ordered Search Table의 find 연산에서 사용)

## Open Questions

- 정렬되지 않은 동적 데이터에서 이진 탐색과 동등한 O(log n) 탐색을 얻으려면 어떤 자료 구조가 필요한가?
- 중복 키가 존재할 때 모든 해당 항목을 찾으려면 이진 탐색을 어떻게 수정해야 하는가?

## Sources

- raw/자료구조/CSE2112_02_week12_2.pdf
