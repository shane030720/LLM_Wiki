---
title: Transitive Closure
category: concept
tags: [graph, digraph, reachability, dynamic-programming]
sources: [raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

방향 그래프(digraph) G가 주어졌을 때, G의 **transitive closure** G\*는 G와 동일한 정점 집합을 가지며, G에서 정점 u로부터 v로 향하는 방향 경로(directed path)가 존재하면(u ≠ v) G\*에는 u에서 v로의 방향 간선(directed edge)이 존재하는 digraph이다. Transitive closure는 원래 그래프의 도달 가능성(reachability) 정보를 압축적으로 표현한다.

## How It Works

Transitive closure를 계산하는 방법은 크게 두 가지다.

**방법 1 — DFS 반복**
- 각 정점을 출발점으로 DFS를 수행하여, 도달 가능한 모든 정점에 대해 간선을 추가한다.
- 시간 복잡도: O(n(n + m)) — 정점 수 n, 간선 수 m

**방법 2 — Floyd-Warshall 동적 프로그래밍**
- 정점을 v₁, v₂, …, vₙ으로 번호를 붙인다.
- Gk를 "번호 1, …, k인 정점만 중간 경유지로 사용하는 경우의 도달 가능 관계"로 정의한다.
- 점화식: Gk에 간선 (vi, vj)를 추가하는 조건 → Gk-1에 (vi, vk)와 (vk, vj)가 모두 존재할 때
- G0 = G에서 시작하여 Gn = G\*가 될 때까지 n단계를 반복한다.
- 시간 복잡도: O(n³) (adjacency matrix 사용 시 areAdjacent가 O(1))

## Key Properties

- G\*의 정점 집합은 G와 동일하다.
- G\*의 간선 (u, v)는 G에서 u → v로의 방향 경로가 존재함을 의미한다 (자기 자신 제외).
- Transitivity 반영: G에서 A → B 경로와 B → C 경로가 있으면 G\*에는 A → C 간선이 추가된다.
- Adjacency matrix를 사용하면 공간 O(n²), 시간 O(n³)으로 계산 가능하다.
- DFS 기반 방법은 희소 그래프(sparse graph)에서 Floyd-Warshall보다 유리할 수 있다.

## Relationships

- [[floyd-warshall-algorithm]] — transitive closure를 O(n³)에 계산하는 동적 프로그래밍 알고리즘
- [[all-pairs-shortest-paths]] — 동일한 DP 구조를 가중치 그래프의 최단 경로 계산에 확장한 문제

## Open Questions

- 매우 희소한 그래프(sparse graph)에서 DFS 기반 방법과 Floyd-Warshall 중 어느 쪽이 실제로 더 빠른가?
- 동적으로 간선이 추가·삭제되는 그래프에서 transitive closure를 효율적으로 유지(incremental update)하는 방법은?
- 비트 병렬화(bit-parallelism)를 활용한 adjacency matrix 연산으로 Floyd-Warshall을 실질적으로 얼마나 가속할 수 있는가?

## Sources

- raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf
