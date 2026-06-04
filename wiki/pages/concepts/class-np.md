---
title: Class NP (Non-Deterministic Polynomial Time)
category: concept
tags: [complexity, verification, nondeterministic, certificate]
sources: [raw/알고리즘/CH13 NP-완전 문제.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Class NP는 **비결정론적 다항 시간(non-deterministic polynomial time)** 내에 풀 수 있는 결정 문제들의 집합이다. 실용적 정의로는, 어떤 후보 해(certificate)가 주어졌을 때 그것이 올바른 해인지를 **다항 시간 내에 검증(verify)** 할 수 있는 문제들의 클래스다. P ⊆ NP가 성립하며, P = NP인지는 미해결 문제다.

## How It Works

NP 검증은 다음 구조를 따른다:

1. **Certificate(증명서)**: 후보 해 y를 외부에서 입력으로 받는다.
2. **Verification Algorithm**: y가 문제의 해임을 다항 시간에 확인한다.

예시 — "그래프 G에 가중치 K 이하의 MST가 존재하는가?":
1. Certificate로 n-1개의 간선 집합 T를 사용한다.
2. T가 spanning tree를 형성하는지 검사한다.
3. T의 총 가중치가 K 이하인지 검사한다.
4. 전체 검사는 O(n+m) 시간으로 다항 시간에 완료된다.

NP에서의 비결정론(non-determinism)은 "정답을 마법처럼 추측한 뒤 검증한다"는 개념 모델이다.

## Key Properties

- 해를 **찾는** 것이 아니라 주어진 후보를 **검증**하는 것이 다항 시간에 가능하다
- P ⊆ NP: P에 속하는 문제는 풀 수 있으므로 검증도 가능하다
- 대부분의 연구자들은 P ≠ NP라고 믿는다
- NP는 "비효율적인 문제들의 집합"이 아니라 "효율적으로 검증 가능한 문제들의 집합"이다
- NP 내에서 가장 어려운 문제들이 [[np-completeness|NP-Complete]] 문제들이다

## Relationships

- [[class-p]] — P ⊆ NP; P에 속하는 모든 문제는 NP에도 속한다
- [[np-completeness]] — NP 내에서 NP-Hard이기도 한 가장 어려운 문제들의 부분집합

## Open Questions

- **P = NP?** — NP의 모든 문제를 다항 시간에 풀 수 있는지의 여부. 밀레니엄 7대 수학 난제 중 하나.
- P ≠ NP라면, NP와 P 사이에 "NP-intermediate"(NP-완전도 아니고 P에도 속하지 않는) 문제들이 존재하는가? (Ladner's Theorem에 따르면 P ≠ NP일 경우 존재한다)

## Sources

- raw/알고리즘/CH13 NP-완전 문제.pdf (p.10–p.11)
