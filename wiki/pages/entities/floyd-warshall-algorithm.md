---
title: Floyd-Warshall Algorithm
category: entity
tags: [algorithm, dynamic-programming, graph, shortest-path, transitive-closure]
sources: [raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Floyd-Warshall 알고리즘은 방향 그래프(digraph)에서 동적 프로그래밍(dynamic programming)을 이용해 두 가지 문제를 O(n³) 시간에 해결하는 고전 알고리즘이다.

1. **Transitive closure 계산**: G\*의 모든 도달 가능 간선을 결정한다.
2. **All-pairs shortest paths 계산**: 모든 정점 쌍 (i, j) 사이의 최단 거리를 결정한다.

핵심 아이디어는 정점을 v₁, …, vₙ으로 번호 매기고, "번호 1부터 k까지의 정점만 중간 경유지로 허용"하는 부분 문제를 단계적으로 확장하는 것이다. 알고리즘의 각 반복(phase k)은 이전 단계의 결과를 기반으로 k번 정점을 새 중간 경유지로 추가한다.

**Transitive Closure 버전 알고리즘 (의사코드)**

```
Algorithm FloydWarshall(G)
  Input  : digraph G
  Output : transitive closure G* of G

  번호 부여: 각 정점 v → vi
  G0 ← G
  for k ← 1 to n do
    Gk ← Gk-1
    for i ← 1 to n (i ≠ k) do
      for j ← 1 to n (j ≠ i, k) do
        if Gk-1.areAdjacent(vi, vk) ∧ Gk-1.areAdjacent(vk, vj)
          if ¬Gk.areAdjacent(vi, vj)
            Gk.insertDirectedEdge(vi, vj, k)
  return Gn
```

**All-Pairs Shortest Paths 버전 점화식**

```
D0[i,j] = 0           (i = j)
         = weight(i,j) (간선 존재)
         = +∞          (간선 없음)

Dk[i,j] = min( Dk-1[i,j],  Dk-1[i,k] + Dk-1[k,j] )
```

## Capabilities

- 방향 그래프에서 모든 정점 쌍의 도달 가능성을 O(n³)에 계산한다.
- 가중치 방향 그래프에서 모든 정점 쌍 간의 최단 거리를 O(n³)에 계산한다.
- 음수 가중치 간선이 있는 그래프에도 적용 가능하다 (단, 음수 사이클 없는 경우).
- 구현이 단순하여 n이 수백~수천 규모일 때 실용적이다.
- Adjacency matrix를 사용하면 areAdjacent가 O(1)이므로 세 겹 루프가 O(n³)을 정확히 보장한다.

## Limitations

- 시간 복잡도 O(n³)은 정점 수 n이 클수록 비실용적이다.
- Adjacency matrix 기반이므로 공간 복잡도가 O(n²)이다 — 희소 그래프에서 공간 낭비가 크다.
- 음수 사이클(negative cycle)이 존재하면 최단 경로가 정의되지 않아 알고리즘이 올바른 결과를 내지 못한다.
- All-pairs shortest paths에서 음수 간선이 없다면, n번의 Dijkstra 호출(O(nm log n))이 희소 그래프에서 더 효율적일 수 있다.
- 경로 자체(path reconstruction)를 원할 경우 predecessor matrix 같은 추가 자료 구조가 필요하다.

## Relationships

- [[transitive-closure]] — 이 알고리즘이 해결하는 1차 문제
- [[all-pairs-shortest-paths]] — 동일한 DP 구조를 가중치 문제로 확장한 응용
- [[dijkstra-algorithm]] (미작성) — 단일 출발점 최단 경로 알고리즘; n회 호출로 all-pairs를 O(nm log n)에 풀 수 있어 Floyd-Warshall과 경쟁 관계

## Sources

- raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf
