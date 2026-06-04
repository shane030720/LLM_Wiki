---
title: PQ-Sort
category: concept
tags: [sorting, algorithm, priority-queue]
sources: [raw/자료구조/CSE2112_02_week09_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

PQ-Sort는 우선순위 큐를 중간 자료구조로 활용하는 범용 비교 기반 정렬 알고리즘이다. 시퀀스 S의 n개 원소를 오름차순으로 정렬하기 위해 두 단계로 진행하며, 우선순위 큐의 내부 구현 방식에 따라 [[selection-sort]] 또는 [[insertion-sort]]가 된다.

## How It Works

```
Algorithm PQ-Sort(S, C)
  Input  시퀀스 S, 비교자 C
  Output C에 따라 오름차순 정렬된 S

  P ← comparator C를 사용하는 빈 우선순위 큐
  while ¬S.empty()
    e ← S.front();  S.eraseFront()
    P.insert(e, ·)
  while ¬P.empty()
    e ← P.removeMin()
    S.insertBack(e)
```

**Phase 1 - 삽입**: 시퀀스 S의 모든 원소를 n번의 insert 연산으로 빈 우선순위 큐 P에 이동시킨다.

**Phase 2 - 추출**: P에서 n번의 removeMin 연산으로 원소를 오름차순으로 꺼내 S에 다시 삽입한다.

우선순위 큐 구현 방식별 시간 복잡도:

| 구현 방식 | insert 1회 | removeMin 1회 | Phase 1 합계 | Phase 2 합계 | 전체 |
|---------|-----------|--------------|------------|------------|------|
| 비정렬 시퀀스 | O(1) | O(n) | O(n) | O(n²) | O(n²) |
| 정렬 시퀀스 | O(n) | O(1) | O(n²) | O(n) | O(n²) |
| 힙 | O(log n) | O(log n) | O(n log n) | O(n log n) | O(n log n) |

## Key Properties

- 두 단계(삽입 Phase, 추출 Phase)로 구성된 정렬 프레임워크
- 우선순위 큐의 구현과 무관하게 정렬 정확성 보장
- 시퀀스 기반 구현(비정렬·정렬 모두)에서 전체 시간 복잡도 O(n²)
- Comparator C를 교체하면 정렬 기준(오름차순/내림차순, 사용자 정의 순서)을 쉽게 변경 가능
- 힙(Heap)으로 구현하면 O(n log n) 달성 가능 (Heap Sort)

## Relationships

- [[priority-queue]] (PQ-Sort가 내부적으로 사용하는 핵심 자료구조)
- [[selection-sort]] (비정렬 시퀀스 기반 PQ-Sort 변형; insert O(1), removeMin O(n))
- [[insertion-sort]] (정렬 시퀀스 기반 PQ-Sort 변형; insert O(n), removeMin O(1))
- [[heap]] (PQ-Sort를 O(n log n)으로 만드는 힙 자료구조)

## Open Questions

- 힙 기반 PQ-Sort(Heap Sort)의 실제 상수 인자는 merge sort, quick sort 대비 어느 수준인가?
- 안정 정렬(stable sort)이 되려면 우선순위 큐 구현에 어떤 추가 조건이 필요한가?
- 동일 key를 가진 entry가 많을 경우 각 구현 방식에서 성능 차이가 발생하는가?

## Sources

- raw/자료구조/CSE2112_02_week09_2.pdf
