---
title: Minimum Spanning Tree
category: concept
tags: [graph, tree, optimization, spanning-tree]
sources: [raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Minimum Spanning Tree(최소 신장 트리, MST)는 연결된 무방향 가중 그래프 G=(V,E,W)에서 모든 정점을 포함하면서 포함된 간선 가중치의 합이 최소인 신장 트리(Spanning Tree)이다. Spanning Tree란 G의 부분 그래프(subgraph) 중 비순환(acyclic) 연결 트리이면서 V의 모든 정점을 포함하는 것을 말한다.

## How It Works
- 가중 그래프에서 서브그래프의 가중치는 포함된 간선 가중치의 합으로 정의된다.
- 신장 트리는 정확히 |V|-1개의 간선으로 구성되며 모든 정점을 연결한다.
- 동일한 그래프에 여러 신장 트리가 존재할 수 있으며, 그 중 가중치 합이 최소인 것을 MST라 한다.
- 그리디 알고리즘(Prim, Kruskal)을 적용하면 MST의 정확한 최적해를 구할 수 있다.

## Key Properties
- 간선 수: 정점 수 |V|인 그래프의 MST는 항상 |V|-1개의 간선을 가짐
- 비순환성: 사이클(cycle)을 포함하지 않음
- 연결성: 모든 정점이 하나의 연결된 트리로 구성됨
- 최적 부분 구조(Optimal substructure): 그리디 알고리즘이 전역 최적해를 보장하는 문제 중 하나

## Relationships
- [[greedy-algorithm]] (MST를 정확하게 풀기 위해 사용되는 알고리즘 패러다임)
- [[prims-algorithm]] (정점 확장 방식으로 MST를 구성하는 알고리즘)
- [[kruskals-algorithm]] (간선 정렬 방식으로 MST를 구성하는 알고리즘)
- [[dijkstras-algorithm]] (동일한 그래프 최적화 계열이나 목표는 최단 경로)

## Open Questions
- 간선 가중치에 동일한 값이 복수 존재할 때 MST는 유일(unique)한가?
- 비연결 그래프(disconnected graph)에서 MST 개념은 어떻게 확장되는가(Minimum Spanning Forest)?

## Sources
- raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
