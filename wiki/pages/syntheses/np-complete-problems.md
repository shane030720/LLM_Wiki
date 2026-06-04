---
title: NP-Complete Problems Survey
category: synthesis
tags: [np-complete, sat, tsp, vertex-cover, reduction, knapsack, hamiltonian]
sources: [raw/알고리즘/CH13 NP-완전 문제.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Thesis

NP-Complete 문제들은 다항 시간 환원(polynomial reduction)의 연쇄를 통해 서로 연결된 구조적 패밀리를 형성한다. 모두 CIRCUIT-SAT로부터 파생되며, 이 환원 체인은 서로 겉으로는 전혀 달라 보이는 조합론적·그래프 이론적 문제들이 본질적으로 동등한 계산 난이도를 가진다는 것을 보인다.

## Evidence

**CIRCUIT-SAT (환원 체인의 기원)**
- AND, OR, NOT 게이트로 구성된 불리언 회로의 만족 가능성(satisfiability) 문제
- 모든 NP-Complete 증명의 최초 출발점 (Cook-Levin Theorem)

**SAT (Boolean Satisfiability)**
- 불리언 변수들에 0/1을 할당하여 전체 수식이 참(1)이 되는 할당이 존재하는가?
- 예: (a+b+¬d+e)(¬a+¬c)(¬b+c+d+e)(a+¬c+¬e)
- CIRCUIT-SAT로부터 환원 → NP-Complete

**3SAT**
- CNF(Conjunctive Normal Form) 형식에서 각 절(clause)이 정확히 3개의 리터럴(literal)을 가지는 SAT
- 예: (a+b+¬d)(¬a+¬c+e)(¬b+d+e)(a+¬c+¬e)
- SAT로부터 환원 → NP-Complete

**VERTEX-COVER**
- 그래프 G=(V,E)에서 모든 간선의 적어도 한 끝점을 포함하는 크기 K 이하의 정점 집합이 존재하는가?
- 3SAT로부터 환원 → NP-Complete
- 이후 다수의 NP-Complete 증명의 기반 문제로 활용됨

**SET-COVER**
- m개의 집합 중 K개를 골라 합집합이 전체 집합과 같아지는 조합이 존재하는가?
- VERTEX-COVER로부터 환원 → NP-Complete

**SUBSET-SUM**
- 정수 집합과 목표값 K가 주어졌을 때, 합이 정확히 K가 되는 부분집합이 존재하는가?
- VERTEX-COVER로부터 환원 → NP-Complete

**0/1 Knapsack**
- 무게와 가치가 있는 물건들 중, 총 무게 W 이하이면서 총 가치 K 이상인 부분집합이 존재하는가?
- SUBSET-SUM으로부터 환원 → NP-Complete

**Hamiltonian Cycle**
- 그래프 G에서 모든 정점을 정확히 한 번씩 방문하는 사이클이 존재하는가?
- VERTEX-COVER로부터 환원 → NP-Complete

**Traveling Salesperson Problem (TSP)**
- 완전 가중 그래프에서 모든 정점을 방문하는 총 비용 K 이하의 투어(tour)가 존재하는가?
- Hamiltonian Cycle로부터 환원 → NP-Complete

**환원 체인 요약**:
```
CIRCUIT-SAT
  └→ SAT
       └→ 3SAT
            └→ VERTEX-COVER
                 ├→ SET-COVER
                 ├→ SUBSET-SUM
                 │    └→ 0/1 Knapsack
                 └→ Hamiltonian Cycle
                      └→ TSP
```

## Counterevidence

- 일부 NP-Complete 문제는 특수한 제약 하에서 다항 시간 알고리즘이 존재한다. 예: 2SAT(각 절에 리터럴 2개)는 P에 속하지만 3SAT는 NP-Complete이다. 문제의 미세한 구조 변화가 복잡도 클래스를 바꿀 수 있다.
- 근사 알고리즘(approximation algorithm)이나 휴리스틱으로 실용적인 근사 해를 다항 시간에 구할 수 있다. 예: TSP에 대한 Christofides 알고리즘은 최적해의 1.5배 이내를 보장한다.
- 특수 구조를 가진 입력(예: 평면 그래프의 TSP)에서는 효율적인 알고리즘이 존재하기도 한다.

## Conclusion

NP-Complete 문제들은 CIRCUIT-SAT에서 시작된 환원 체인으로 연결된 구조적 패밀리를 형성한다. 논리적 만족 가능성(SAT), 그래프 커버(Vertex Cover), 집합 문제(Subset Sum), 경로 최적화(TSP) 등 매우 다양한 분야의 실용적 문제들이 동등한 계산 난이도를 갖는다. 현재까지 어떤 NP-Complete 문제도 다항 시간 알고리즘이 발견되지 않았으며, 이를 해결해야 하는 경우 근사 알고리즘, 휴리스틱, 또는 특수 구조 활용이 현실적 접근이다.

## Sources

- raw/알고리즘/CH13 NP-완전 문제.pdf (p.14–p.20)
