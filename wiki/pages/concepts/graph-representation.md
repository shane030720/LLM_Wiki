---
title: Graph Representation
category: concept
tags: [graph, data-structure, adjacency-list, adjacency-matrix, edge-list]
sources: [raw/자료구조/CSE2112_02_week13_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
그래프를 컴퓨터 메모리에 저장하는 세 가지 주요 방식: Edge List, Adjacency List, Adjacency Matrix. 각 방식은 공간 복잡도와 특정 연산의 시간 복잡도에서 서로 다른 트레이드오프를 가지며, Adjacency List가 Adjacency Matrix의 기반이 되는 계층적 관계를 형성한다.

## How It Works

### Edge List
- Vertex object: element, vertex sequence 내 위치 참조(reference)
- Edge object: element, origin vertex, destination vertex, edge sequence 내 위치 참조
- Vertex sequence와 Edge sequence를 별도 목록으로 유지
- 모든 간선을 단순 나열 방식으로 저장

### Adjacency List
- Edge List 구조를 기반으로 확장
- 각 정점마다 Incidence sequence 유지: 해당 정점에 인접한 간선 객체들의 참조 목록
- Augmented edge objects: 양 끝 정점의 incidence sequence 내 위치를 역참조
- Vector 기반 구현 시 세 가지 배열 사용:
  - `vertices`: 크기 N×1, 정점 존재 여부 (1/0)
  - `edges`: 크기 N×2, 간선의 양 끝점 인덱스
  - `adjacency_list`: 크기 N×deg(v), 인접 정점 목록

### Adjacency Matrix
- Edge List 구조를 기반으로 확장
- 각 정점에 정수 인덱스(key) 부여
- N×N 2D 배열: 인접 정점 쌍에는 간선 객체 참조, 비인접 쌍에는 null (단순 구현에서는 1/0)
- Vector 기반 구현 시 세 가지 배열 사용:
  - `vertices_exist`: 크기 N×1, 정점 존재 여부
  - `edges_list`: 크기 N×2, 간선 양 끝점
  - `adjacency_matrix`: 크기 N×N, 인접 여부 (1/0)

## Key Properties
- Edge List: 구조 단순, 특정 정점의 인접 간선 탐색에 O(m) 시간 소요
- Adjacency List: 인접 간선 직접 접근 가능, 희소 그래프(sparse graph)에 효율적, 공간 O(n+m)
- Adjacency Matrix: 두 정점의 인접 여부를 O(1)에 확인 가능, 공간 O(n²), 밀집 그래프(dense graph)에 적합
- BFS, DFS 등 그래프 순회 알고리즘은 Adjacency List 구조 사용 시 O(n+m) 시간 보장 (∑ deg(v) = 2m)

## Relationships
- [[graph]] (이 표현 방식들이 저장하는 자료구조 본체)
- [[depth-first-search]] (Adjacency List를 사용하면 O(n+m) 시간 보장)
- [[breadth-first-search]] (Adjacency List를 사용하면 O(n+m) 시간 보장)

## Open Questions
- 동적 그래프(정점·간선 추가·삭제가 빈번한 경우)에서 세 방식의 시간 복잡도 비교 우위는 무엇인가?
- Edge List가 Adjacency List·Matrix의 기반으로만 쓰이는지, 독자적으로 활용되는 실용적 맥락이 있는지?

## Sources
- raw/자료구조/CSE2112_02_week13_2.pdf (p.5–p.11)
