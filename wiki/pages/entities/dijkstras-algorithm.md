---
title: Dijkstra's Algorithm
category: entity
tags: [algorithm, graph, shortest-path, greedy]
sources: [raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview
Dijkstra's Algorithm은 비음수 가중치(nonnegative weights)를 갖는 가중 그래프에서 단일 출발점(single source) s로부터 도달 가능한 모든 정점까지의 최단 거리를 계산하는 그리디 알고리즘이다. Single-Source Shortest Path(SSSP) 문제를 정확하게 해결한다. [[prims-algorithm]]과 정점 분류 구조가 동일하지만, 선택 기준이 간선 가중치 W(tv)에서 누적 거리 d(s,t)+W(tv)로 바뀐다.

## Capabilities
- 출발점 s에서 도달 가능한 모든 정점의 최단 거리 d(s,v)를 계산
- 정점 상태 분류(Tree / Fringe / Unseen)를 통해 진행 상태 추적
- 최단 경로의 부분 경로 최적성(Shortest Path Property) 활용:
  - x에서 z까지의 최단 경로가 y를 경유하면, x→y 구간과 y→z 구간도 각각 최단 경로임
- 알고리즘 개요(Outline):

```
dijkstraSSSP(G, n)
  모든 정점을 unseen으로 초기화
  출발 정점 s를 tree로 분류; d(s,s) = 0
  s에 인접한 모든 정점을 fringe로 분류
  fringe 정점이 존재하는 동안:
    d(s,t) + W(tv)가 최소인 tree 정점 t와 fringe 정점 v 사이의 간선 선택
    v를 tree로 분류; 간선 tv를 트리에 추가
    d(s,v) = d(s,t) + W(tv)로 정의
    v에 인접한 unseen 정점들을 fringe로 분류
```

- 정확성 보장(Correctness Theorem): 비음수 가중치 그래프에서, d(s,y)+W(yz)를 최소화하는 간선 yz를 선택하면 s에서 z까지의 최단 경로가 보장된다.

## Limitations
- 음수 가중치(negative weight) 간선이 존재하는 경우 정확성 보장 불가(Bellman-Ford 등 별도 알고리즘 필요)
- 단일 쌍(s→t) 최단 경로만 구하더라도 최악의 경우 전체 SSSP 문제와 동일한 시간 복잡도를 가짐
- 우선순위 큐 없이 구현 시 시간 복잡도가 O(V²)로 증가하여 밀집 그래프 외에는 비효율적

## Relationships
- [[greedy-algorithm]] (Dijkstra's Algorithm이 따르는 알고리즘 패러다임)
- [[minimum-spanning-tree]] (유사한 정점 확장 구조를 공유하는 관련 그래프 최적화 문제)
- [[prims-algorithm]] (알고리즘 구조가 동일하며 선택 기준(W(tv) vs d(s,t)+W(tv))만 다름)

## Sources
- raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
