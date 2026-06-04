---
title: Kruskal's Algorithm
category: entity
tags: [algorithm, graph, mst, greedy, disjoint-set]
sources: [raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview
Kruskal's Algorithm은 연결된 무방향 가중 그래프에서 [[minimum-spanning-tree]]를 구하는 그리디 알고리즘이다. 전체 간선을 가중치 오름차순으로 처리하면서 사이클을 형성하지 않는 간선만 선택하여 포레스트(forest)를 점진적으로 하나의 MST로 합쳐 나간다.

## Capabilities
- 간선 중심(edge-centric) 접근: 전체 간선을 가중치 기준으로 정렬 후 처리
- Disjoint Set(서로소 집합) 자료구조로 사이클 감지:
  - `find(u)`: u가 속한 집합 반환
  - `union(u, v)`: u와 v가 속한 두 집합을 하나로 합침
- 서로 다른 트리(집합)에 속한 정점을 연결하는 간선만 MST에 추가하여 사이클 방지
- 알고리즘 개요(Outline):

```
KruskalMST(G, n)
  R = E       // 남은 간선 집합
  F = {}      // 포레스트(MST) 간선 집합
  while R가 비어 있지 않은 동안:
    R에서 최소 가중치 간선 vw를 제거
    if vw가 F에서 사이클을 형성하지 않으면:
      vw를 F에 추가
  return F
```

- 중간 상태를 포레스트(forest of disjoint trees) 형태로 유지

## Limitations
- 간선 전체 정렬에 O(E log E) 시간이 필요
- 비연결 그래프에 적용하면 MST 대신 최소 신장 포레스트(Minimum Spanning Forest)가 반환됨
- Disjoint Set 자료구조의 구현 복잡도가 추가되며, union-find 연산의 효율적 구현(path compression, union by rank)이 성능에 영향

## Relationships
- [[minimum-spanning-tree]] (이 알고리즘이 해결하는 문제)
- [[greedy-algorithm]] (Kruskal's Algorithm이 따르는 알고리즘 패러다임)
- [[prims-algorithm]] (같은 MST 문제를 정점 확장 방식으로 해결하는 알고리즘)

## Sources
- raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
