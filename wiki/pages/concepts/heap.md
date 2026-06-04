---
title: Heap
category: concept
tags: [heap, tree, priority-queue, data-structure]
sources: [raw/자료구조/CSE2112_02_week10_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Heap은 각 노드에 키(key)를 저장하는 이진 트리(binary tree)로, 다음 두 가지 속성을 동시에 만족하는 자료구조다.

1. **Heap-order property**: 루트를 제외한 모든 내부 노드 v에 대해 부모 노드의 키가 자식 노드의 키보다 작거나 같다 (min-heap 기준: key(v) >= key(parent(v))).
2. **Complete binary tree property**: 높이 h인 heap에서, 깊이 0~h-1까지의 각 레벨 i에는 정확히 2^i개의 노드가 존재하며, 깊이 h에서는 내부 노드들이 왼쪽부터 빠짐없이 채워진다.

Priority Queue를 구현하는 데 사용될 때는 각 내부 노드에 (key, element) 쌍을 저장하고, 마지막 노드(last node)의 위치를 별도로 추적한다.

## How It Works

### Insert (삽입)

1. **삽입 노드 탐색**: complete binary tree 속성을 유지하는 새 마지막 노드 z를 찾는다.
2. **키 저장**: z에 새로운 키 k를 저장한다.
3. **Upheap**: heap-order 속성을 복원하기 위해 upheap 알고리즘을 수행한다.

**Upheap 알고리즘**: 삽입 노드에서 시작해 키 k를 부모와 비교하며 위쪽으로 스왑한다. k가 루트에 도달하거나, 부모 노드의 키가 k보다 작거나 같을 때 종료한다. 힙의 높이가 O(log n)이므로 O(log n) 시간에 완료된다.

```
upheap(idx):
  if idx == 1 (root): return
  parent_idx = idx / 2
  if parent의 우선순위 < child의 우선순위:
    swap(idx, parent_idx)
    upheap(parent_idx)
```

### RemoveMin (최솟값 제거)

1. **루트 키 교체**: 루트 키를 마지막 노드 w의 키로 교체한다.
2. **마지막 노드 제거**: w를 힙에서 제거한다.
3. **Downheap**: heap-order 속성을 복원하기 위해 downheap 알고리즘을 수행한다.

**Downheap 알고리즘**: 루트에서 시작해 키 k를 두 자식 중 더 높은 우선순위(더 작은 키)를 가진 자식과 비교하며 아래쪽으로 스왑한다. k가 리프 노드에 도달하거나, 모든 자식의 키가 k보다 크거나 같을 때 종료한다. O(log n) 시간에 완료된다.

```
downheap(idx):
  left_idx = idx * 2
  right_idx = idx * 2 + 1
  if 자식이 없으면: return
  child_idx = 우선순위가 높은 자식의 인덱스
  if child의 우선순위 > parent의 우선순위:
    swap(idx, child_idx)
    downheap(child_idx)
```

### Vector Representation (벡터 기반 구현)

Complete binary tree는 1-indexed 배열(벡터)로 포인터 없이 효율적으로 표현할 수 있다.

- 루트: 인덱스 1
- 노드 u의 왼쪽 자식: 인덱스 2f(u)
- 노드 u의 오른쪽 자식: 인덱스 2f(u) + 1
- 노드 u의 부모: 인덱스 floor(f(u) / 2)
- 인덱스 0은 사용하지 않음

insert 연산은 인덱스 n+1에, removeMin 연산은 인덱스 n에서의 원소 처리에 해당하며, 이를 통해 in-place heap-sort가 가능해진다.

## Key Properties

- **높이**: n개의 노드를 가진 힙의 높이는 O(log n)
- **시간 복잡도**:
  - `size()`, `empty()`, `min()`: O(1)
  - `insert()`, `removeMin()`: O(log n)
- **공간 복잡도**: O(n)
- Complete binary tree 속성 덕분에 배열로 포인터 없이 표현 가능하며 캐시 효율이 높다
- Priority Queue ADT의 가장 효율적인 표준 구현체

## Relationships

- [[priority-queue]] (heap이 구현하는 추상 자료형)
- [[heap-sort]] (heap을 이용한 O(n log n) 정렬 알고리즘)
- [[bottom-up-heap-construction]] (n개의 키로 힙을 O(n)에 일괄 구성하는 알고리즘)

## Open Questions

- n번의 연속적인 insert로 힙을 구성하면 O(n log n)이 소요되는데, [[bottom-up-heap-construction]]은 O(n)을 달성한다. 두 방식의 상수 인자 차이를 고려할 때 실제 소규모 데이터에서도 bottom-up이 항상 유리한가?
- 벡터 기반 구현에서 동적 크기 조정이 필요한 경우 amortized 비용이 추가되는데, 이것이 worst-case 보장에 어떤 영향을 미치는가?

## Sources

- raw/자료구조/CSE2112_02_week10_2.pdf
