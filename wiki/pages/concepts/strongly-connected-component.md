---
title: Strongly Connected Component (강연결 요소)
category: concept
tags: [graph, algorithm, directed-graph, connectivity, scc]
sources: [raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Strongly Connected Component(SCC, 강연결 요소)는 방향 그래프(digraph)의 극대 강연결 부분 그래프(maximal strongly connected subgraph)이다. 강연결(strongly connected)이란 부분 그래프 내의 모든 정점 쌍 (v, w)에 대해 v→w 경로와 w→v 경로가 모두 존재함을 의미한다. 모든 방향 그래프는 유일한 SCC 분해를 가진다.

## How It Works

### SCC 분해 알고리즘 (Kosaraju's Algorithm, 2-Phase DFS)

**Phase 1 — DFS on G with finishing-time stack:**

1. 원래 그래프 G에 대해 표준 DFS를 수행한다.
2. 각 정점의 DFS 완료 시점(finishing time)에 해당 정점을 스택에 push한다.
3. 탐색 완료 후 스택의 top에는 가장 늦게 완료된 정점(가장 "출구에 가까운" 정점)이 위치한다.

**Phase 2 — DFS on G^T (transpose graph) using stack order:**

1. 그래프 G의 모든 간선 방향을 역전시킨 전치 그래프(transpose graph) G^T를 구성한다.
2. 스택에서 정점을 pop하는 순서로 G^T에 대해 DFS를 수행한다.
3. 각 DFS 호출로 방문되는 정점들이 하나의 SCC를 구성하며, 그 시작 정점이 해당 SCC의 **leader**가 된다.

## Key Properties

- 모든 방향 그래프는 유일한 SCC 분해를 가진다.
- SCC들을 노드로 압축하면 SCC 간 간선으로 이루어진 DAG(Directed Acyclic Graph)가 형성된다.
- **Transpose graph G^T:** G의 모든 간선 (u, v)를 (v, u)로 역전시킨 그래프이다.
- 알고리즘 전체 시간 복잡도: O(n + m) — 두 번의 DFS로 구성된다.
- Phase 1 DFS에서 발생하는 간선 유형: tree edge, back edge, descendant edge, cross edge.
- SCC 내의 모든 정점은 서로 도달 가능하므로, SCC 단위로 그래프를 단순화할 수 있다.

## Relationships

- [[graph]] — SCC는 방향 그래프 위에 정의되는 개념
- [[depth-first-search]] — 알고리즘의 두 페이즈 모두 DFS를 활용; finishing time이 핵심 정보
- [[breadth-first-search]] — 그래프 순회의 대안 전략 (SCC 알고리즘에서는 미사용)

## Open Questions

- 본 자료에서는 transpose graph G^T의 구체적 구성 방법(구현 수준)을 제시하지 않는다.
- Tarjan's SCC algorithm과의 성능·구현 복잡도 비교는 다루지 않는다.
- SCC 크기 분포나 SCC 압축 후 DAG 구조 분석에 대한 내용은 포함되지 않는다.

## Sources

- raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf
