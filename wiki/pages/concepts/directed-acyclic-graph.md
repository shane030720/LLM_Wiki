---
title: Directed Acyclic Graph (DAG)
category: concept
tags: [graph, dag, directed-graph, topological-order, digraph]
sources: [raw/자료구조/CSE2112_02_week13_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
DAG(Directed Acyclic Graph, 방향 비순환 그래프)는 모든 간선이 방향을 가지며(directed), 방향을 따라가는 순환(directed cycle)이 존재하지 않는 그래프다. Digraph(directed graph)의 특수한 경우로, "A digraph admits a topological order if and only if it is a DAG"라는 동치 정리가 성립한다.

## How It Works

Digraph는 모든 간선이 방향을 가진 그래프로, 일방통행 도로, 항공 노선, 작업 스케줄링 등 비대칭 관계를 모델링한다. DAG는 그 중 directed cycle이 없는 특수한 경우다.

**Topological order(위상 순서)**: DAG의 정점을 v1, v2, ..., vn으로 나열했을 때, 모든 간선 (vi, vj)에 대해 i < j를 만족하는 선형 순서. 즉, 간선의 방향을 거스르지 않는 순서다.

**응용 예시**:
- 작업 스케줄링(task scheduling): 선행 조건(precedence constraint)을 만족하는 실행 순서 결정
- 일방통행 도로(one-way streets) 경로 계획
- 항공 노선(flights) 연결 분석
- 빌드 시스템에서 컴파일 의존성 해소

## Key Properties
- Directed cycle이 없을 때, 그리고 오직 그때만 topological order가 존재 (필요충분조건)
- In-degree가 0인 정점(진입 간선이 없는 정점)이 항상 하나 이상 존재
- In-degree가 0인 정점이 topological order에서 첫 번째 위치 후보
- Topological order는 유일하지 않을 수 있음 (in-degree = 0인 정점이 여러 개일 때)
- 트리(tree)는 DAG의 특수한 경우

## Relationships
- [[topological-sorting]] (DAG에서 topological order를 구하는 알고리즘)
- [[depth-first-search]] (DFS 기반으로 위상 정렬 구현 가능)
- [[graph]] (DAG가 속하는 상위 자료구조 범주)

## Open Questions
- Cycle 탐지와 DAG 검증을 동시에 수행하는 효율적인 알고리즘 설계 방법은?
- DAG에서 topological order가 유일한 경우(Hamiltonian path 존재)를 O(n+m) 시간에 판별할 수 있는가?

## Sources
- raw/자료구조/CSE2112_02_week13_2.pdf (p.37–p.40)
