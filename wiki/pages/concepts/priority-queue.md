---
title: Priority Queue
category: concept
tags: [data-structure, abstract-data-type, queue, sorting]
sources: [raw/자료구조/CSE2112_02_week10_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Priority Queue(우선순위 큐)는 각 원소에 우선순위(key)를 부여하여 저장하는 추상 자료형(ADT)이다. 스택·큐·리스트 등 위치 기반(position-based) 자료구조와 달리, 원소는 삽입 위치가 아닌 key 값에 따라 관리되며, key가 가장 작은 원소(= 가장 높은 우선순위)가 항상 먼저 제거된다. 각 원소는 (key, value) 쌍으로 구성된 Entry 형태로 저장된다.

## How It Works

### 핵심 연산

- **insert(e)**: 연관된 key를 가진 entry e를 삽입한다.
- **removeMin()**: key가 가장 작은 entry를 제거하고 반환한다.
- **min()**: key가 가장 작은 entry를 제거하지 않고 반환한다.
- **size()**, **empty()**: 크기 및 공백 여부를 반환한다.

### Sequence 기반 구현 비교

|  | Unsorted List | Sorted List |
|---|---|---|
| insert(e) | O(1) — 맨 앞/뒤에 바로 삽입 | O(n) — 삽입 위치 탐색 필요 |
| removeMin() / min() | O(n) — 전체 순회로 최솟값 탐색 | O(1) — 맨 앞/뒤 원소가 최솟값 |

### PQ-Sort 패턴

Priority Queue를 이용한 정렬의 일반 패턴(시간복잡도는 구현에 의존):

1. n번의 insert 연산으로 모든 원소를 PQ에 삽입한다.
2. n번의 removeMin 연산으로 정렬된 순서로 원소를 추출한다.

구현에 따른 정렬 알고리즘:

- Unsorted List 기반 → Selection Sort: O(n²)
- Sorted List 기반 → Insertion Sort: O(n²)
- [[heap]] 기반 → [[heap-sort]]: O(n log n)

## Key Properties

- 우선순위는 key로 표현되며, key가 작을수록 우선순위가 높다 (min-priority queue 기준).
- 위치 기반이 아닌 priority 기반으로 원소를 관리한다.
- Sequence 기반 구현에서는 insert와 removeMin 중 하나가 반드시 O(n)이 된다.
- [[heap]]을 사용하면 insert와 removeMin 모두 O(log n)으로 개선 가능하다.
- 대기열 우선순위 예시: 항공기 대기 탑승객(standby flyers) — 우선순위 번호 순으로 탑승.

## Relationships

- [[heap]] — Priority Queue의 효율적인 구현체; insert와 removeMin 모두 O(log n) 보장
- [[heap-sort]] — Heap 기반 PQ를 이용한 O(n log n) 정렬 알고리즘
- [[selection-sort]] — Unsorted List 기반 PQ-sort의 구체화; O(n²) 시간복잡도
- [[insertion-sort]] — Sorted List 기반 PQ-sort의 구체화; O(n²) 시간복잡도

## Open Questions

- Sequence 기반 구현에서 insert와 removeMin 두 연산을 동시에 O(n) 미만으로 만들 수 있는가? (이를 극복하기 위해 트리 기반 구조인 Heap이 도입됨)
- 동일한 key를 가진 원소들 사이의 순서(tie-breaking) 정책은 어떻게 정의해야 하는가?
- Max-priority queue(key가 클수록 우선순위가 높음)는 어떻게 구현하는가?

## Sources

- raw/자료구조/CSE2112_02_week10_1.pdf — Week 10 Lecture 01, p.3–p.13, p.33 (Priority Queue ADT, Sequence 기반 구현, PQ-Sort 패턴)
