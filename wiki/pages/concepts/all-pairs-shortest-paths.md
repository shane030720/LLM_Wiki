---
title: All-Pairs Shortest Paths
category: concept
tags: [graph, shortest-path, dynamic-programming, weighted-graph]
sources: [raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

**All-pairs shortest paths(모든 쌍 최단 경로)** 문제는 가중치 방향 그래프(weighted directed graph) G에서 모든 정점 쌍 (i, j)에 대해 최단 경로의 거리(distance)를 구하는 문제이다. 단일 출발점 최단 경로(single-source shortest paths)를 모든 정점에 대해 반복 적용하거나, 동적 프로그래밍으로 한 번에 해결한다.

## How It Works

**방법 1 — Dijkstra's Algorithm 반복 적용**
- 음수 간선이 없는 경우에 한해 사용 가능하다.
- 각 정점을 출발점으로 Dijkstra를 n번 호출한다.
- 시간 복잡도: O(nm log n)

**방법 2 — Dynamic Programming (Floyd-Warshall 방식)**
정점을 1, …, n으로 번호 매긴 뒤 다음 점화식을 적용한다.

초기화:
```
D0[i,j] = 0            (i = j)
         = weight(i,j)  (간선 (i,j)가 존재할 때)
         = +∞           (간선이 없을 때)
```

점화식 (k = 1 → n):
```
Dk[i,j] = min( Dk-1[i,j],  Dk-1[i,k] + Dk-1[k,j] )
```

- Dk[i,j]는 "번호 1, …, k인 정점만 중간 경유지로 허용했을 때 i → j 최단 거리"를 의미한다.
- 최종 Dn이 모든 쌍의 최단 거리 행렬이다.
- 시간 복잡도: O(n³)

## Key Properties

- D 행렬은 n × n 크기이며 공간 복잡도는 O(n²)이다 (in-place 갱신으로 O(n²) 유지 가능).
- 음수 간선이 허용되나 음수 사이클이 있으면 최단 경로가 정의되지 않는다.
- 밀집 그래프(dense graph, m ≈ n²)에서는 O(n³) DP가 O(nm log n) Dijkstra 반복보다 경쟁력이 있다.
- 희소 그래프(sparse graph, m << n²)에서는 Dijkstra 반복이 더 효율적이다.
- [[transitive-closure]] 계산과 동일한 3중 루프 DP 구조를 공유한다 — 가중치 대신 부울 도달 가능성을 다룰 때 transitive closure가 된다.

## Relationships

- [[floyd-warshall-algorithm]] — 이 문제를 O(n³)에 해결하는 DP 알고리즘
- [[transitive-closure]] — 가중치 없이 도달 가능성만 묻는 구조적으로 동일한 문제
- [[dijkstra-algorithm]] (미작성) — 음수 간선이 없을 때 단일 출발점 최단 경로를 구하는 알고리즘; n회 반복으로 all-pairs를 해결하는 대안

## Open Questions

- 음수 사이클을 사전에 탐지하는 효율적인 방법을 이 DP 과정에 통합할 수 있는가?
- 정점 수 n이 수만 이상인 대규모 그래프에서 O(n³) DP를 병렬화하거나 근사하는 현실적인 방법은?
- 간선 가중치가 실시간으로 변하는 동적 그래프에서 모든 쌍 최단 거리를 효율적으로 유지(incremental update)하는 방법은?

## Sources

- raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf
