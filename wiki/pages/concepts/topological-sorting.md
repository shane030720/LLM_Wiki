---
title: Topological Sorting
category: concept
tags: [graph, dag, algorithm, topological-order, dfs]
sources: [raw/자료구조/CSE2112_02_week13_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
위상 정렬(Topological Sorting)은 DAG(Directed Acyclic Graph)의 정점들을 topological order — 모든 간선 (u, v)에 대해 u가 v보다 앞에 오는 선형 순서 — 로 나열하는 알고리즘이다. 시간 복잡도는 O(n+m)이며, 두 가지 주요 구현 방식이 존재한다.

## How It Works

### 방법 1: 진출 간선 제거 알고리즘
```
Algorithm TopologicalSort(G):
  H <- G의 임시 복사본
  n <- G.numVertices()
  while H is not empty:
    진출 간선(outgoing edge)이 없는 정점 v를 선택
    v에 레이블 n 부여
    n <- n - 1
    H에서 v 제거
```
진출 간선이 없는 정점 = 후속 작업이 없는 마지막 완료 작업. 번호를 n, n-1, ..., 1 순으로 뒤에서부터 부여한다.

### 방법 2: DFS 기반 구현 (권장, O(n+m))
```
Algorithm topologicalDFS(G):
  n <- G.numVertices()
  모든 정점 u: u.setLabel(UNEXPLORED)
  모든 정점 v:
    if v.getLabel() = UNEXPLORED:
      topologicalDFS(G, v)

Algorithm topologicalDFS(G, v):
  v.setLabel(VISITED)
  for all e in v.outEdges():     -- 진출 간선만 탐색
    w <- e.opposite(v)
    if w.getLabel() = UNEXPLORED:
      topologicalDFS(G, w)       -- discovery edge
    -- else: forward 또는 cross edge
  v에 위상 번호 n 부여
  n <- n - 1
```

핵심 아이디어: DFS가 완전히 완료된(모든 후속 정점 방문 완료) 정점부터 번호를 부여한다. 따라서 번호가 클수록 위상 순서에서 앞에 위치한다.

### 시각적 예시 (강의 예제)
정점이 9개인 DAG에서 DFS 완료 순서의 역으로 번호 1–9를 부여하면 위상 순서가 된다.

## Key Properties
- 시간 복잡도: O(n+m)
- DAG에서만 정의됨 (directed cycle이 있으면 topological order 불가능)
- DFS 기반 구현에서 위상 번호는 DFS 완료 순서(post-order)의 역순으로 부여
- 결과가 유일하지 않을 수 있음 (in-degree = 0인 정점이 여러 개일 때)
- 방법 1은 개념 이해에 직관적, 방법 2는 DFS를 활용하므로 추가 공간 불필요

## Relationships
- [[directed-acyclic-graph]] (위상 정렬이 정의되는 그래프 유형; DAG일 때만 적용 가능)
- [[depth-first-search]] (방법 2의 핵심 알고리즘; post-order 방문 순서를 활용)
- [[graph]] (적용 대상 자료구조)

## Open Questions
- Kahn's algorithm(in-degree 기반 BFS 방식)과 DFS post-order 방식 중 실제 구현에서 성능·메모리 측면의 우위는?
- 위상 정렬 결과가 유일한 경우(즉, DAG에 Hamiltonian path가 존재하는 경우)를 효율적으로 판별할 수 있는가?

## Sources
- raw/자료구조/CSE2112_02_week13_2.pdf (p.40–p.52)
