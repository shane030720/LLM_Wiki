---
title: Breadth-First Search (BFS)
category: concept
tags: [graph, traversal, bfs, algorithm, queue, shortest-path]
sources: [raw/자료구조/CSE2112_02_week13_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
BFS(Breadth-First Search, 너비 우선 탐색)는 그래프의 모든 정점과 간선을 방문하는 순회 알고리즘이다. 시작 정점으로부터 거리(간선 hop 수)가 같은 정점들을 같은 레벨(level)로 묶어 층별로 방문한다. Queue 자료구조를 사용하여 구현하며 O(n+m) 시간에 동작한다.

## How It Works

### 전체 그래프 BFS
```
Algorithm BFS(G):
  모든 정점 u: u.setLabel(UNEXPLORED)
  모든 간선 e: e.setLabel(UNEXPLORED)
  모든 정점 v:
    if v.getLabel() = UNEXPLORED:
      BFS(G, v)
```

### 단일 시작점 BFS(G, s)
```
Algorithm BFS(G, s):
  L0 <- {s},  s.setLabel(VISITED),  i <- 0
  while L_i is not empty:
    L_{i+1} <- empty sequence
    for all v in L_i:
      for all e in v.incidentEdges():
        if e.getLabel() = UNEXPLORED:
          w <- e.opposite(v)
          if w.getLabel() = UNEXPLORED:
            e.setLabel(DISCOVERY)
            w.setLabel(VISITED)
            L_{i+1}.insertBack(w)
          else:
            e.setLabel(CROSS)   -- 교차 간선
    i <- i + 1
```

Queue 기반 동작 순서:
1. 시작 노드를 enqueue
2. Front 원소를 dequeue
3. 미방문 인접 노드를 모두 enqueue
4. Queue가 빌 때까지 2–3 반복

### C++ 구현
```cpp
void BFS(int src) {
    queue<int> q;
    visited[src] = true;
    q.push(src);
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int& adj : adjacency_list[cur]) {
            if (!visited[adj]) {
                visited[adj] = true;
                q.push(adj);
            }
        }
    }
}
```

간선은 두 종류로 레이블된다:
- **Discovery edge**: 처음 방문하는 정점으로 향하는 간선. BFS spanning tree를 구성
- **Cross edge**: 같은 레벨 또는 인접 레벨의 이미 방문한 정점으로 향하는 간선

## Key Properties
- 시간 복잡도: O(n+m), Adjacency List 표현 사용 시 (∑ deg(v) = 2m)
- 각 정점, 각 간선은 정확히 두 번 레이블 변경 (UNEXPLORED → VISITED/DISCOVERY/CROSS)
- BFS spanning tree의 성질 (Property 3): Level L_i의 정점 v에 대해 시작점 s에서 v까지의 경로 길이 = i이며, 이는 s에서 v까지 가능한 모든 경로 중 최솟값
- Weighted graph가 아닌 Unweighted graph에서만 최단 경로(최소 간선 수) 보장

### 주요 응용 (O(n+m) 시간)
- 그래프의 연결 성분(connected components) 계산
- Spanning forest 계산
- 두 정점 간 최소 간선 수 경로 탐색
- 단순 사이클(simple cycle) 존재 여부 탐색

## Relationships
- [[graph-representation]] (Adjacency List 구조로 O(n+m) 시간 보장)
- [[depth-first-search]] (대조적 순회 방식: 너비 우선 vs. 깊이 우선)
- [[graph]] (BFS가 적용되는 자료구조)

## Open Questions
- Weighted graph에서 최단 경로를 보장하지 않는 BFS의 한계를 Dijkstra 알고리즘이 어떻게 극복하는가?
- BFS spanning tree와 DFS spanning tree는 동일한 그래프에 대해 어떤 구조적 차이를 보이는가?

## Sources
- raw/자료구조/CSE2112_02_week13_2.pdf (p.20–p.29)
