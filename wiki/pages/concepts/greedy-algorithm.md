---
title: Greedy Algorithm
category: concept
tags: [algorithm, optimization, greedy]
sources: [raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Greedy Algorithm(욕심쟁이 알고리즘)은 각 단계에서 주어진 제한적인 "단기적 기준(short-term criterion)"에 따라 현재 시점에서 가장 최선으로 보이는 선택을 순차적으로 수행하는 알고리즘 설계 패러다임이다. 한 번 내려진 선택은 이후에 더 나쁜 결과가 드러나더라도 취소(undo)되지 않는다.

## How It Works
1. 일련의 선택(sequence of choices)을 순서대로 수행한다.
2. 각 선택은 평가 비용이 낮은 단기 기준으로 결정된다.
3. 선택은 비가역적(irrevocable)이며 번복되지 않는다.
4. 개별 최선 선택들의 합이 전체 최적해(overall optimal)를 구성하도록 설계된다.

잠재적 단점: 단기 비용이 낮은 선택이 이후 불가피한 대규모 비용을 초래할 수 있다. 그리디 알고리즘이 전역 최적을 보장하지 않는 문제에 적용되면 준최적(suboptimal) 결과를 낸다.

## Key Properties
- 비가역성(Irrevocability): 선택된 결과는 취소 불가
- 근시안적 판단(Short-term criterion): 전역 상태가 아닌 국소 정보 기반 선택
- 연산 효율성: 선택 기준 평가가 저비용이어야 함
- 최적 보장 조건: Greedy-choice property와 Optimal substructure가 성립하는 문제에서만 전역 최적 보장

## Relationships
- [[minimum-spanning-tree]] (그리디 알고리즘이 전역 최적해를 보장하는 대표적 그래프 문제)
- [[prims-algorithm]] (MST를 구성하는 정점 확장 방식의 그리디 알고리즘)
- [[kruskals-algorithm]] (MST를 구성하는 간선 정렬 방식의 그리디 알고리즘)
- [[dijkstras-algorithm]] (단일 출발점 최단 경로 문제에 적용된 그리디 알고리즘)

## Open Questions
- Greedy-choice property와 Optimal substructure가 동시에 충족되어야만 그리디가 최적을 보장하는가, 아니면 둘 중 하나로 충분한 경우가 있는가?
- 그리디가 실패하는 문제(예: 0/1 Knapsack)와 성공하는 문제(예: MST, SSSP) 사이의 구조적 경계를 어떻게 일반화할 수 있는가?

## Sources
- raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
