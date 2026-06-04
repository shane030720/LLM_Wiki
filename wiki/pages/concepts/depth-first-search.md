---
title: Depth-First Search (DFS)
category: concept
tags: [graph, traversal, dfs, algorithm, recursion]
sources: [raw/자료구조/CSE2112_02_week13_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
DFS(Depth-First Search, 깊이 우선 탐색)는 그래프의 모든 정점과 간선을 방문하는 순회 알고리즘이다. 시작 정점에서 한 방향으로 방문할 수 있는 곳까지 최대한 깊이 진행한 뒤, 더 이상 미방문 정점이 없으면 되돌아와(backtrack) 다른 경로를 탐색한다. 재귀 호출 스택으로 구현하며 O(n+m) 시간에 동작한다.

## How It Works

### 전체 그래프 DFS
```
Algorithm DFS(G):
  모든 정점 u: u.setLabel(UNEXPLORED)
  모든 간선 e: e.setLabel(UNEXPLORED)
  모든 정점 v:
    if v.getLabel() = UNEXPLORED:
      DFS(G, v)
```

### 단일 시작점 DFS(G, v)
```
Algorithm DFS(G, v):
  v.setLabel(VISITED)
  for all e in G.incidentEdges(v):
    if e.getLabel() = UNEXPLORED:
      w <- e.opposite(v)
      if w.getLabel() = UNEXPLORED:
        e.setLabel(DISCOVERY)   -- 발견 간선
        DFS(G, w)
      else:
        e.setLabel(BACK)        -- 후향 간선
```

### C++ 재귀 구현
```cpp
void DFS_recursive(int cur) {
    visited[cur] = true;
    for (int& adj : adjacency_list[cur]) {
        if (!visited[adj]) {
            DFS_recursive(adj);
        }
    }
}
```

간선은 두 종류로 레이블된다:
- **Discovery edge**: 처음 방문하는 정점으로 향하는 간선. DFS spanning tree를 구성
- **Back edge**: 이미 방문한 정점으로 향하는 간선. 무방향 그래프에서 사이클 존재를 시사

## Key Properties
- 시간 복잡도: O(n+m), Adjacency List 표현 사용 시
- 각 정점은 UNEXPLORED에서 VISITED로 정확히 한 번 레이블 변경
- 각 간선은 UNEXPLORED에서 DISCOVERY 또는 BACK으로 정확히 한 번 레이블 변경
- Discovery edge들이 모여 DFS spanning tree(신장 트리)를 형성
- Back edge는 사이클(cycle) 탐지 및 그래프 속성 검사에 활용

## Relationships
- [[graph-representation]] (Adjacency List 구조로 O(n+m) 시간 보장)
- [[breadth-first-search]] (대조적 순회 방식: 깊이 우선 vs. 너비 우선)
- [[topological-sorting]] (DFS 완료 순서를 역이용하여 위상 정렬 구현)
- [[graph]] (DFS가 적용되는 자료구조)

## Open Questions
- 재귀 깊이가 매우 큰 그래프에서 스택 오버플로우(stack overflow) 위험이 있을 때, 반복(iterative) DFS 구현과의 정확한 트레이드오프는?
- 방향 그래프(directed graph)에서 Back edge 외에 나타나는 Forward edge, Cross edge의 의미와 활용 방법은?

## Sources
- raw/자료구조/CSE2112_02_week13_2.pdf (p.14–p.17)
