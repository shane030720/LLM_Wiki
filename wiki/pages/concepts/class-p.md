---
title: Class P (Polynomial Time)
category: concept
tags: [complexity, polynomial, algorithm, decision-problem]
sources: [raw/알고리즘/CH13 NP-완전 문제.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Class P는 **다항 시간(polynomial time)** 내에 해를 구할 수 있는 결정 문제(decision problem)들의 집합이다. 어떤 알고리즘의 시간 복잡도가 T(n) = O(n^k) (k는 상수)를 만족하면 그 알고리즘은 다항 시간에 실행된다고 하며, 이러한 알고리즘이 존재하는 문제는 Class P에 속한다. 다항 시간은 알고리즘의 "효율성(efficiency)" 기준으로 간주된다.

## How It Works

- 문제의 복잡도는 그 문제를 푸는 **최선의 알고리즘**의 복잡도로 정의된다.
- 동일한 문제도 평균/최악/최선 케이스에 따라 복잡도가 달라질 수 있다.
- P에 속하는 문제는 입력 크기 n에 대해 다항식으로 표현 가능한 시간 안에 해를 구하는 알고리즘이 존재한다.
- 대표 예시:
  - 정렬되지 않은 배열에서 최댓값 찾기: Ω(n) → P에 속함
  - 배열 정렬: Ω(n log n) → P에 속함
  - SHORTEST-PATH (최단 경로): 그래프 G와 정점 u, v가 주어졌을 때 최소 간선 수의 경로를 구하는 문제 → P에 속함

## Key Properties

- T(n) = O(n^k) (k는 고정 상수)를 만족하는 알고리즘이 존재하면 P에 속한다
- 다항 시간은 지수 시간(exponential time)보다 훨씬 효율적이다
- P에 속하는 모든 문제는 [[class-np]]에도 속한다 (P ⊆ NP)
- 결정 문제(yes/no 답변) 형태로 정의된다; 최적화 문제는 대응하는 결정 문제로 변환 가능하다
- 예: SHORTEST-PATH(최적화) ↔ PATH(결정): "u에서 v까지 k개 이하 간선으로 가는 경로가 있는가?"

## Relationships

- [[class-np]] — P의 상위 집합; P ⊆ NP 관계가 성립
- [[np-completeness]] — P에 속하지 않는 것으로 여겨지는 NP 내 가장 어려운 문제들

## Open Questions

- P = NP인가? 즉, 검증 가능한 모든 문제를 다항 시간에 풀 수도 있는가? 이론 컴퓨터 과학의 가장 유명한 미해결 문제다.
- 특정 문제에 대해 다항 시간 하한(lower bound)을 엄밀히 증명하는 것은 일반적으로 매우 어렵다.

## Sources

- raw/알고리즘/CH13 NP-완전 문제.pdf (p.3–p.6)
