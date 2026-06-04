---
title: Heapsort
category: entity
tags: [sort, algorithm, comparison-sort, heap, tree, divide-and-conquer]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Heapsort(힙 정렬)는 Heap 자료구조를 이용한 비교 기반 in-place 정렬 알고리즘이다. 모든 원소를 최대 힙(max-heap)으로 구성한 후, 루트(최댓값)를 반복적으로 제거하고 남은 원소들로 힙 성질을 복구하는 과정을 반복한다.

**Heap 정의**:
- **Heap Structure (left-complete binary tree)**: 높이 h의 이진 트리로, 깊이 h-1까지 완전하고 깊이 h의 리프는 모두 왼쪽에 집중된 구조
- **Partial Order Tree Property (maximizing heap)**: 각 노드의 키가 자식 노드들의 키보다 크거나 같다

**배열 구현**: 인덱스 1부터 n까지 사용; 인덱스 i의 노드에 대해 왼쪽 자식 = 2i, 오른쪽 자식 = 2i+1, 부모 = floor(i/2)

**주요 단계**:
1. `constructHeap`: [[divide-and-conquer]]로 힙 구성 — 각 서브트리를 재귀적으로 힙으로 만든 뒤 루트에 `fixHeap` 적용
2. `fixHeap(H, K)`: K를 힙 H에 삽입하면서 partial order tree property를 복구; 두 자식 중 큰 쪽과 비교하며 하향 이동
3. `deleteMax` + `heapSort`: 루트 제거 후 최하단 오른쪽 원소 K를 루트에 놓고 `fixHeap(H, K)` 호출, 이를 n번 반복

**fixHeap worst case**: 높이 h의 힙에서 최대 2h번 비교

## Capabilities

- **In-place 정렬**: 배열 구현 시 추가 공간 불필요
- **Worst-case comparisons (일반 Heapsort)**: 2n log n + O(n)
  - 전체 삭제에 대한 총 비교: Σ(k=1 to n-1) 2·log(k) ∈ θ(n log n)
- **Accelerated Heapsort** (`fixHeapFast` 사용): worst case n log n + θ(n log log n)
  - **전략**: 빈 자리(vacant)를 트리의 절반(h/2)까지 먼저 필터링(`promote`)한 뒤, K가 해당 위치의 부모보다 크면 위로 버블업(`bubbleUpHeap`); 아니면 재귀 반복
  - `fixHeapFast` 비교 횟수: h + log(h) (worst case) — 일반 fixHeap의 2h에 비해 약 2배 절감
  - 전체 삭제 총 비교: Σ(k=1 to n-1) log(k) ∈ θ(n log n)

## Limitations

- 일반 `fixHeap`은 worst case에서 2h번 비교가 필요하여 Accelerated 버전 대비 약 2배 느리다.
- `fixHeapFast`는 `promote`, `bubbleUpHeap` 등 여러 서브루틴이 필요하여 구현 복잡도가 높다.
- 트리 구조 특성상 메모리 접근 패턴이 불규칙하여 [[quick-sort]]에 비해 캐시 효율이 낮다.

## Relationships

- [[divide-and-conquer]]: `constructHeap`과 `fixHeapFast` 내부에서 분할 정복 적용
- [[quick-sort]]: 둘 다 in-place이나, Quick-Sort는 worst case를 보장하지 못하는 반면 Heapsort는 보장
- [[mergesort]]: 둘 다 worst case θ(n log n) 범주이나 Heapsort는 in-place, Mergesort는 O(n) 추가 메모리 필요
- [[sorting-algorithm-comparison]]: worst case가 보장되며 in-place인 비교 정렬로 비교 분석

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.23–40)
