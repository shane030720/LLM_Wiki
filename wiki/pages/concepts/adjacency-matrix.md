---
title: Adjacency Matrix (인접 행렬)
category: concept
tags: [graph, adjacency-matrix, data-structure, implementation]
sources: [raw/자료구조/(참고자료) Week13_Graphs (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Adjacency Matrix(인접 행렬)는 [[graph]]를 2차원 행렬로 표현하는 구현 방식이다. 각 정점에 고유한 인덱스 번호를 부여하고, n×n 크기의 행렬에서 `matrix[i][j]`에 정점 i와 정점 j를 연결하는 간선의 포인터(또는 NULL)를 저장한다. 간선의 수가 상대적으로 많은 밀집 그래프(dense graph)이거나, 두 정점 사이의 인접 여부를 자주 조회해야 할 때 효율적이다.

## How It Works

### 내부 필드

- `vertices_list` : 정점 객체들의 리스트. 각 정점은 고유한 인덱스를 갖는다.
- `edges_list` : 간선 객체들의 리스트.
- `matrix` : 간선을 참조하는 2차원 행렬. `matrix[i][j]`는 인덱스 i인 정점과 인덱스 j인 정점을 연결하는 간선의 포인터를 저장하며, 간선이 없으면 NULL(∅)이다.

### 주요 연산 절차

**insert_vertex(vid)**
1. 새로운 정점 객체를 생성하고 인덱스를 부여한다.
2. `vertices_list` 맨 뒤에 추가한다.
3. `matrix`를 확장하여 새로운 정점에 대응하는 행과 열을 추가한다. 새로 추가된 셀은 모두 NULL로 초기화된다.

**insert_edge(vid1, vid2, eid)**
1. 새로운 간선 객체를 생성한다.
2. `edges_list` 맨 뒤에 추가한다.
3. `matrix[index(vid1)][index(vid2)]`와 `matrix[index(vid2)][index(vid1)]`에 해당 간선의 포인터를 저장한다 (무향 그래프의 경우 대칭).

**erase_edge(eid)**
1. `matrix`에서 해당 간선이 참조된 두 셀을 NULL로 초기화한다.
2. `edges_list`에서 간선을 제거한다.
3. 간선 객체를 메모리에서 해제한다.

**erase_vertex(vid)**
1. 해당 정점에 인접한 간선이 있으면 먼저 모두 삭제한다.
2. `matrix`에서 해당 정점에 대응하는 행과 열을 모두 제거한다.
3. `vertices_list`에서 삭제된 정점 이후에 위치한 정점들의 인덱스를 1씩 감소시킨다.
4. `vertices_list`에서 정점을 제거하고 객체를 메모리에서 해제한다.

## Key Properties

연산별 시간 복잡도는 다음과 같다 (n: 정점 개수, m: 간선 개수).

| 연산 | 복잡도 |
|---|---|
| `vertices()` | O(n) |
| `edges()` | O(m) |
| `is_adjacent_to(vid1, vid2)` | O(1) |
| `incident_edges(vid)` | O(n) |
| `insert_vertex(vid)` | O(n) |
| `insert_edge(vid1, vid2, eid)` | O(1) |
| `erase_edge(eid)` | O(1) |
| `erase_vertex(vid)` | O(n²) |

- `is_adjacent_to`가 O(1)인 것이 인접 행렬의 핵심 강점이다.
- `erase_vertex`가 O(n²)인 이유는 행렬에서 해당 행·열 제거 후 나머지 정점들의 인덱스를 재조정하는 과정에서 행렬 전체를 재구성해야 하기 때문이다.
- `incident_edges`가 O(n)인 이유는 특정 행(또는 열) 전체를 순회하여 NULL이 아닌 셀을 찾아야 하기 때문이다.
- 공간 복잡도는 O(n²)이며, 간선이 적은 희소 그래프(sparse graph)에서는 공간 낭비가 크다.

## Relationships

- [[graph]] : 인접 행렬이 구현하는 추상 자료형. 그래프의 연산 인터페이스를 따른다.
- [[adjacency-list]] : 그래프의 대안 구현 방식. 희소 그래프에서 공간 효율이 높으나 `is_adjacent_to`가 O(n)으로 느리다.

## Open Questions

- 유향 그래프(directed graph)의 경우 `matrix[i][j]`와 `matrix[j][i]`가 서로 다른 간선을 가리킬 수 있으므로, `insert_edge` 및 `erase_edge`의 대칭성 처리가 달라진다. 본 자료에서는 무향 그래프 중심으로 설명되어 있어, 유향 그래프 적용 시 변경 사항이 명시되지 않았다.
- 행렬 확장(insert_vertex) 시 동적 배열 재할당 전략(예: amortized doubling)을 적용하면 삽입 복잡도를 개선할 수 있는지 여부가 다루어지지 않았다.

## Sources

- raw/자료구조/(참고자료) Week13_Graphs (1).pdf
