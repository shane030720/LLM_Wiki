---
title: Insertion Sort
category: concept
tags: [sorting, algorithm, insertion-sort, in-place]
sources: [raw/자료구조/CSE2112_02_week09_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Insertion Sort(삽입 정렬)는 우선순위 큐를 정렬 시퀀스(sorted sequence)로 구현한 [[pq-sort]]의 변형이다. 새 원소를 삽입할 때마다 적절한 위치를 찾아 정렬된 상태를 유지하며, 전체 시간 복잡도는 O(n²)이다. 거의 정렬된 입력에 대해 실질적으로 빠른 성능을 보인다.

## How It Works

**시퀀스 기반 구현:**

- Phase 1 - n번 insert: 정렬된 위치를 탐색 후 삽입 → 각 O(n), 합계 O(n²)
  - 비용 합산: 1 + 2 + ... + n = n(n+1)/2 = O(n²)
- Phase 2 - n번 removeMin: 시퀀스 맨 앞(최솟값) 제거 → 각 O(1), 합계 O(n)

```cpp
void SortedSequence::insert(int value) {
    list<int>::iterator temp_itr = elements.begin();
    // 삽입 위치 탐색: O(n)
    while (temp_itr != elements.end() && comp(*temp_itr, value))
        ++temp_itr;
    elements.insert(temp_itr, value);
}

int SortedSequence::min() {
    return elements.front();  // O(1): 맨 앞이 항상 최솟값
}

void SortedSequence::removeMin() {
    elements.pop_front();  // O(1)
}
```

**In-place 구현:**

외부 자료구조 없이 배열 자체를 분할하여 사용한다.
- A[0..idx-1]: 이미 정렬된 부분 (정렬 시퀀스 우선순위 큐 역할)
- A[idx]: 새로 삽입할 원소
- A[idx]를 A[0..idx-1]의 올바른 위치에 삽입 (큰 원소들을 오른쪽으로 밀어 공간 확보)

```cpp
void insertionSort(int A[], int n) {
    for (int idx = 1; idx < n; ++idx) {
        int value = A[idx];
        int j = idx - 1;
        while (j >= 0 && A[j] > value) {
            A[j + 1] = A[j];  // 한 칸씩 오른쪽으로 이동
            j = j - 1;
        }
        A[j + 1] = value;  // 올바른 위치에 삽입
    }
}
```

**실행 예시 (입력: 5 4 2 3 1):**

```
[5 | 4 2 3 1]  → 4를 정렬 부분에 삽입: [4 5]
[4 5 | 2 3 1]  → 2를 삽입: [2 4 5]
[2 4 5 | 3 1]  → 3을 삽입: [2 3 4 5]
[2 3 4 5 | 1]  → 1을 삽입: [1 2 3 4 5]
```

## Key Properties

- insert: O(n) / removeMin: O(1)
- 전체 시간 복잡도: O(n²)
- In-place 구현 가능: 추가 메모리 O(1)
- 거의 정렬된 입력에서 best case O(n) 달성 가능 (비교·이동 횟수가 줄어듦)
- 안정 정렬(stable sort): 동일 key 원소의 상대 순서 보존
- 소규모 데이터 또는 거의 정렬된 데이터에서 실용적으로 우수한 성능

## Relationships

- [[priority-queue]] (Insertion Sort의 내부 자료구조로 정렬 시퀀스를 사용)
- [[pq-sort]] (Insertion Sort는 정렬 시퀀스 기반 PQ-Sort)
- [[selection-sort]] (같은 O(n²)이지만 비정렬 시퀀스 기반; insert/removeMin 비용 분포가 반대)

## Open Questions

- Binary Insertion Sort처럼 이진 탐색으로 삽입 위치를 찾으면 비교 횟수는 O(n log n)으로 줄어드는데, 왜 전체 복잡도는 여전히 O(n²)인가? (원소 이동(shift) 비용이 여전히 O(n)이기 때문)
- 입력이 역순으로 정렬된 경우 Insertion Sort의 실제 수행 시간은 Selection Sort와 비교하여 어떤가?
- 실제 정렬 라이브러리(Timsort 등)가 소규모 구간에 Insertion Sort를 사용하는 이유는 무엇인가?

## Sources

- raw/자료구조/CSE2112_02_week09_2.pdf
