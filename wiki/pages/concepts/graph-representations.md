---
title: Graph Representations (그래프 표현 방법)
category: concept
tags: [graph, data-structure, edge-list, adjacency-list, adjacency-matrix]
sources: [raw/자료구조/CSE2112_02_week13_1 (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

그래프 G = (V, E)를 컴퓨터 메모리에 저장하는 세 가지 표준 방법이다: Edge List, Adjacency List, Adjacency Matrix. 각 방법은 공간 복잡도와 주요 연산의 시간 복잡도에서 서로 다른 트레이드오프를 가진다.

## How It Works

### 1. Edge List Structure

정점 시퀀스와 간선 시퀀스 두 개의 리스트를 유지한다.

- **Vertex object**: element + 정점 시퀀스 내 자신의 위치(position) 참조
- **Edge object**: element + 출발 정점 객체 참조 + 목적 정점 객체 참조 + 간선 시퀀스 내 자신의 위치 참조
- **Vertex sequence**: 모든 정점 객체의 시퀀스
- **Edge sequence**: 모든 간선 객체의 시퀀스

특정 정점의 incident edges를 찾으려면 전체 간선 시퀀스를 모두 스캔해야 한다. 간단하지만 incidentEdges() 연산이 O(m)으로 비효율적이다.

### 2. Adjacency List Structure

Edge List Structure에 각 정점마다 **incidence sequence**를 추가한 확장 구조이다.

- **Incidence sequence I(v)**: 정점 v에 incident한 간선 객체들에 대한 참조 시퀀스
- **Augmented edge object**: 양 끝점 각각의 incidence sequence 내 자신의 위치를 역참조

정점 v의 incident edges에 직접 접근할 수 있으므로 incidentEdges(v)가 O(deg(v))로 개선된다.

### 3. Adjacency Matrix Structure

Edge List Structure에 **2차원 adjacency array**를 추가한 구조이다.

- 각 정점에 정수 키(index) 부여
- matrix[i][j]: 정점 i와 j 사이의 간선 객체 참조. 인접하지 않으면 null.
- 고전적 구현에서는 간선이 있으면 1, 없으면 0을 저장한다.
- 두 정점의 인접 여부를 O(1)에 확인할 수 있으나, 공간이 O(n²) 필요하다.

## Key Properties

n개의 정점, m개의 간선, 자기 루프 없음, 중복 간선 없음을 가정한 성능 비교:

| 연산 | Edge List | Adjacency List | Adjacency Matrix |
|------|-----------|----------------|-----------------|
| Space | O(n + m) | O(n + m) | O(n²) |
| incidentEdges(v) | O(m) | O(deg(v)) | O(n) |
| isAdjacentTo(v, w) | O(m) | O(min(deg(v), deg(w))) | O(1) |
| insertVertex(o) | O(1) | O(1) | O(n²) |
| insertEdge(v, w, o) | O(1) | O(1) | O(1) |
| eraseVertex(v) | O(m) | O(deg(v)) | O(n²) |
| eraseEdge(e) | O(1) | O(1) | O(1) |

- Edge List / Adjacency List: 희소 그래프(sparse graph, m << n²)에 공간 효율적
- Adjacency Matrix: 밀집 그래프(dense graph)이거나 인접 여부를 O(1)로 자주 조회해야 할 때 유리하지만, 정점 삽입/삭제 비용이 O(n²)으로 매우 크다.

## Relationships

- [[graph]] — 그래프의 기본 정의 및 ADT 명세
- [[depth-first-search]] — Adjacency List 구조 사용 시 O(n+m) 시간 보장
- [[breadth-first-search]] — Adjacency List 구조 사용 시 O(n+m) 시간 보장

## Open Questions

- 정점과 간선의 동적 삽입/삭제가 빈번한 경우 어떤 표현이 가장 적합한가?
- 방향 그래프에서 in-degree와 out-degree를 모두 효율적으로 지원하려면 어떤 구조가 필요한가?
- 가중치 그래프(weighted graph)를 표현할 때 각 구조의 확장 방식은?

## Sources

- raw/자료구조/CSE2112_02_week13_1 (1).pdf
