---
title: Heap Sort
category: concept
tags: [heap, sort, algorithm, priority-queue]
sources: [raw/자료구조/CSE2112_02_week10_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Heap-sort는 [[heap]] 기반 Priority Queue를 활용하는 비교 정렬 알고리즘으로, n개의 원소를 O(n log n) 시간에 정렬한다. PQ-sort 패러다임에서 Priority Queue를 힙으로 구현했을 때 얻어지는 알고리즘이며, 이차 시간 알고리즘인 selection-sort, insertion-sort보다 점근적으로 우월하다.

## How It Works

### PQ-Sort 패러다임

```
PQ-Sort(S, C):
  P ← comparator C를 가진 빈 Priority Queue
  while S가 비지 않음:
    e ← S.front(); S.eraseFront()
    P.insert(e, ∅)
  while P가 비지 않음:
    e ← P.removeMin()
    S.insertBack(e)
```

Priority Queue 구현 방식에 따라 도출되는 정렬 알고리즘이 달라진다.

### PQ 구현별 정렬 알고리즘 비교

| Priority Queue 구현 | 도출되는 정렬 | Phase 1 (insert) | Phase 2 (removeMin) | 전체 |
|---|---|---|---|---|
| 정렬되지 않은 시퀀스 | Selection Sort | O(n) | O(n²) | O(n²) |
| 정렬된 시퀀스 | Insertion Sort | O(n²) | O(n) | O(n²) |
| Heap | Heap Sort | O(n log n) | O(n log n) | O(n log n) |

- **Selection Sort** (비정렬 시퀀스): insert는 O(1)이지만 removeMin마다 전체 시퀀스를 탐색하므로 O(n)
- **Insertion Sort** (정렬 시퀀스): insert 시 정렬 위치 탐색이 O(n)이지만 removeMin은 O(1)
- **Heap Sort**: insert와 removeMin 모두 O(log n)으로 균형 잡힌 성능

### 힙 기반 수행 과정

1. **Phase 1 (힙 구성)**: n번의 insert 연산 → 각 O(log n) → 총 O(n log n)
   - [[bottom-up-heap-construction]] 적용 시 Phase 1을 O(n)으로 단축 가능
2. **Phase 2 (정렬 추출)**: n번의 removeMin 연산 → 각 O(log n) → 총 O(n log n)

벡터 기반 힙 구현을 사용하면 추가 공간 없이 **in-place heap-sort**가 가능하다.

## Key Properties

- **시간 복잡도**: O(n log n) — worst, average, best case 모두 동일하게 보장
- **공간 복잡도**: O(n); 벡터 기반 in-place 구현 시 O(1) 추가 공간
- **안정성(stability)**: 기본 구현은 불안정 정렬(unstable sort)
- selection-sort, insertion-sort 대비 점근적으로 훨씬 빠름
- [[bottom-up-heap-construction]]으로 Phase 1을 O(n)으로 가속할 수 있어 실제 구현에서 Phase 2가 주요 병목

## Relationships

- [[heap]] (heap-sort의 핵심 자료구조; upheap과 downheap 연산 활용)
- [[priority-queue]] (heap-sort가 기반하는 추상 자료형)
- [[bottom-up-heap-construction]] (Phase 1을 O(n)으로 가속하는 기법)

## Open Questions

- Heap-sort는 O(n log n) worst-case를 보장하지만, 캐시 지역성(cache locality)이 낮아 실제 벤치마크에서 quicksort보다 느린 경우가 많다. 어떤 상황에서 heap-sort가 실용적으로 우월한가?
- In-place heap-sort의 표준 구현은 max-heap을 사용하는데, 본 강의의 min-heap 기반 PQ-sort 방식과 어떻게 다른가? 두 방식의 공간 사용 차이는?

## Sources

- raw/자료구조/CSE2112_02_week10_2.pdf
