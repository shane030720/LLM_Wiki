---
title: Graph (그래프)
category: concept
tags: [graph, data-structure, vertex, edge]
sources: [raw/자료구조/CSE2112_02_week13_1 (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Graph는 객체 간의 쌍별(pairwise) 관계를 표현하는 자료구조로, 정점(vertex)의 집합 V와 간선(edge)의 모음 E로 구성된 순서쌍 G = (V, E)이다. 정점은 위치(position)이면서 원소(element)를 저장하며, 간선 또한 두 정점을 연결하는 위치로서 원소를 저장한다.

## How It Works

### 간선 유형

- **Directed edge (방향 간선)**: 순서가 있는 정점 쌍 (u, v). u는 출발점(origin), v는 목적지(destination). 항공편(flight)이 대표적인 예시이다.
- **Undirected edge (무방향 간선)**: 순서가 없는 정점 쌍 (u, v). 항공 노선(flight route)처럼 양방향으로 사용되는 연결을 표현한다.
- **Directed graph**: 모든 간선이 방향 간선인 그래프
- **Undirected graph**: 모든 간선이 무방향 간선인 그래프
- **Mixed graph**: 방향 간선과 무방향 간선이 혼재하는 그래프. 무방향 간선 (u, v)는 (u, v)와 (v, u) 두 방향 간선으로 변환할 수 있다.

### 주요 용어

- **End vertices / Endpoints**: 간선의 양 끝 정점 (예: 간선 a의 끝점이 U, V이면 U와 V가 endpoints)
- **Incident edges**: 특정 정점에 연결된 간선들
- **Adjacent vertices**: 간선 하나로 직접 연결된 두 정점
- **Degree (deg(v))**: 정점 v에 incident한 간선의 수
- **Parallel edges**: 동일한 두 정점 사이에 존재하는 복수의 간선
- **Self-loop**: 한 정점에서 자기 자신으로 이어지는 간선
- **Path**: 정점과 간선을 교대로 나열한 시퀀스. 첫 정점에서 시작해 마지막 정점으로 끝나며, 각 간선은 양 끝점이 앞뒤 정점과 일치한다.
- **Simple path**: 모든 정점과 간선이 중복 없는 경로
- **Cycle**: 시작 정점으로 돌아오는 순환 정점-간선 시퀀스
- **Simple cycle**: 모든 정점과 간선이 중복 없는 사이클

### 서브그래프 및 연결성

- **Subgraph**: 그래프 G의 정점 부분집합과 간선 부분집합으로 이루어진 그래프
- **Spanning subgraph**: G의 모든 정점을 포함하는 서브그래프
- **Connected graph**: 모든 정점 쌍 사이에 경로가 존재하는 그래프
- **Connected component**: 그래프 내 최대 크기(maximal)의 connected subgraph
- **Free tree**: 연결되어 있고 사이클이 없는 무방향 그래프. rooted tree와는 구분되는 개념이다.
- **Forest**: 사이클이 없는 무방향 그래프. 각 connected component가 tree이다.
- **Spanning tree**: connected graph의 spanning subgraph 중 tree인 것
- **Spanning forest**: 그래프의 spanning subgraph 중 forest인 것

### Graph ADT 주요 메서드

**접근자(Accessor) 메서드:**
- `e.endVertices()`: 간선 e의 두 끝점 반환
- `e.opposite(v)`: 간선 e에서 v의 반대편 정점 반환
- `u.isAdjacentTo(v)`: u와 v가 인접하면 true

**갱신(Update) 메서드:**
- `insertVertex(o)`: 원소 o를 저장하는 정점 삽입
- `insertEdge(v, w, o)`: 정점 v, w를 연결하고 원소 o를 저장하는 간선 삽입
- `eraseVertex(v)`: 정점 v와 incident 간선 모두 제거
- `eraseEdge(e)`: 간선 e 제거

**순회(Iterable collection) 메서드:**
- `incidentEdges(v)`: v에 incident한 간선 목록
- `vertices()`: 전체 정점 목록
- `edges()`: 전체 간선 목록

### 응용 분야

- **전자 회로**: 인쇄 회로 기판(PCB), 집적 회로(IC)
- **교통 네트워크**: 고속도로망, 항공 네트워크
- **컴퓨터 네트워크**: LAN, 인터넷, 웹
- **데이터베이스**: Entity-Relationship 다이어그램

## Key Properties

- **Property 1**: 모든 정점의 차수 합 = 2m (각 간선이 두 끝점에서 각각 한 번씩 카운팅됨)
  - sum of deg(v) = 2m
- **Property 2**: 자기 루프와 중복 간선이 없는 무방향 그래프에서 m <= n(n-1)/2 (각 정점의 최대 차수가 n-1이므로)
- **방향 그래프에서**: sum of indeg(v) = sum of outdeg(v) = m

## Relationships

- [[graph-representations]] — 그래프를 메모리에 저장하는 세 가지 방법 (Edge List, Adjacency List, Adjacency Matrix)
- [[depth-first-search]] — 그래프의 연결성과 spanning forest를 계산하는 탐색 알고리즘
- [[breadth-first-search]] — 간선 수 기준 최단 경로를 찾는 레벨별 탐색 알고리즘

## Open Questions

- 방향 그래프에서 간선 수 m의 상한은? (무방향의 경우 n(n-1)/2인 데 비해 방향 그래프는 n(n-1))
- Mixed graph를 효율적으로 지원하는 최적의 자료구조는 무엇인가?

## Sources

- raw/자료구조/CSE2112_02_week13_1 (1).pdf
