---
title: Selection Sort
category: concept
tags: [sorting, algorithm, selection-sort, in-place]
sources: [raw/자료구조/CSE2112_02_week09_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Selection Sort(선택 정렬)는 우선순위 큐를 비정렬 시퀀스(unsorted sequence)로 구현한 [[pq-sort]]의 변형이다. 매 단계에서 남은 원소 중 최솟값을 선택(select)하여 정렬된 위치에 배치하는 방식으로 동작하며, 전체 시간 복잡도는 O(n²)이다.

## How It Works

**시퀀스 기반 구현:**

- Phase 1 - n번 insert: 각 원소를 시퀀스 끝에 그냥 추가 → 각 O(1), 합계 O(n)
- Phase 2 - n번 removeMin: 전체를 순회하여 최솟값 탐색 후 제거 → 각 O(n), 합계 O(n²)
  - 비용 합산: 1 + 2 + ... + n = n(n+1)/2 = O(n²)

```cpp
void UnsortedSequence::insert(int value) {
    elements.push_back(value);  // O(1): 끝에 바로 추가
}

void UnsortedSequence::removeMin() {
    list<int>::iterator min_itr, temp_itr;
    min_itr = temp_itr = elements.begin();
    while (temp_itr != elements.end()) {
        if (comp(*temp_itr, *min_itr))  // 더 작은 원소 발견 시 업데이트
            min_itr = temp_itr;
        ++temp_itr;
    }
    elements.erase(min_itr);  // O(n) 전체 탐색 후 제거
}
```

**In-place 구현:**

외부 자료구조 없이 배열 자체를 분할하여 사용한다.
- A[0..i-1]: 이미 정렬된 부분
- A[i..n-1]: 미정렬 부분 (비정렬 우선순위 큐 역할)
- 각 단계에서 A[i:]의 최솟값을 찾아 A[i]와 교환(swap)

```cpp
void selectionSort(int A[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        int idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (A[j] < A[idx]) idx = j;
        }
        swap(A[i], A[idx]);
    }
}
```

**실행 예시 (입력: 5 4 2 3 1):**

```
[5 4 2 3 1]  → 최솟값 1 선택, A[0]과 교환
[1 4 2 3 5]  → 최솟값 2 선택, A[1]과 교환
[1 2 4 3 5]  → 최솟값 3 선택, A[2]와 교환
[1 2 3 4 5]  → 완료
```

## Key Properties

- insert: O(1) / removeMin: O(n)
- 전체 시간 복잡도: O(n²) (best, average, worst case 모두 동일)
- In-place 구현 가능: 추가 메모리 O(1)
- 비교 횟수가 항상 n(n-1)/2로 입력 순서에 무관하게 일정
- 불안정 정렬(unstable sort): 동일 key 원소의 상대 순서 보장 안 됨 (swap으로 인해)
- swap 횟수가 최대 n-1번으로 적어, 데이터 이동 비용이 큰 경우 유리

## Relationships

- [[priority-queue]] (Selection Sort의 내부 자료구조로 비정렬 시퀀스를 사용)
- [[pq-sort]] (Selection Sort는 비정렬 시퀀스 기반 PQ-Sort)
- [[insertion-sort]] (같은 O(n²)이지만 정렬 시퀀스 기반; insert/removeMin 비용 분포가 반대)

## Open Questions

- 불안정한 in-place Selection Sort를 안정 정렬로 만들려면 어떤 수정이 필요한가?
- 데이터 이동 비용(swap)이 매우 큰 경우, Selection Sort가 Insertion Sort보다 실질적으로 유리한 상황이 있는가?
- Cache 지역성(locality) 관점에서 Selection Sort와 Insertion Sort 중 어느 쪽이 실제 하드웨어에서 더 빠른가?

## Sources

- raw/자료구조/CSE2112_02_week09_2.pdf
