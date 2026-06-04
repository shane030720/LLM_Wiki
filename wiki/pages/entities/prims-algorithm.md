---
title: Prim's Algorithm
category: entity
tags: [algorithm, graph, mst, greedy]
sources: [raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview
Prim's Algorithm은 연결된 무방향 가중 그래프에서 [[minimum-spanning-tree]]를 구하는 그리디 알고리즘이다. 임의의 시작 정점(root)에서 출발하여 현재 트리에 연결 가능한 최소 가중치 간선을 반복적으로 선택함으로써 트리를 점진적으로 확장한다. 알고리즘 수행 중 정점은 Tree, Fringe, Unseen의 세 가지 상태로 분류된다.

## Capabilities
- 임의의 시작 정점에서 MST 구성 가능(시작점 무관하게 동일한 MST 반환)
- 정점 상태 분류를 통해 알고리즘 진행 상태를 추적:
  - Tree vertices: 현재까지 구성된 트리에 포함된 정점
  - Fringe vertices: 트리 외부이나 트리 정점에 인접한 정점
  - Unseen vertices: 그 외 모든 정점
- 각 반복에서 Tree 정점 t와 Fringe 정점 v 사이의 최소 가중치 간선을 선택하여 트리에 추가
- 알고리즘 개요(Outline):

```
PrimMST(G, n)
  모든 정점을 unseen으로 초기화
  임의의 시작 정점 s를 tree로 분류
  s에 인접한 모든 정점을 fringe로 분류
  fringe 정점이 존재하는 동안:
    tree 정점 t와 fringe 정점 v 사이의 최소 가중치 간선 선택
    v를 tree로 분류; 간선 tv를 트리에 추가
    v에 인접한 unseen 정점들을 fringe로 분류
```

## Limitations
- 우선순위 큐(priority queue) 없이 구현할 경우 시간 복잡도가 비효율적
- 비연결 그래프(disconnected graph)에는 직접 적용 불가
- 동일 가중치 간선이 복수 존재할 경우 선택 순서에 따라 서로 다른 MST가 생성될 수 있음

## Relationships
- [[minimum-spanning-tree]] (이 알고리즘이 해결하는 문제)
- [[greedy-algorithm]] (Prim's Algorithm이 따르는 알고리즘 패러다임)
- [[kruskals-algorithm]] (같은 MST 문제를 간선 정렬 방식으로 해결하는 알고리즘)
- [[dijkstras-algorithm]] (정점 분류와 반복 확장 구조가 동일하며, 선택 기준만 다름)

## Sources
- raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
