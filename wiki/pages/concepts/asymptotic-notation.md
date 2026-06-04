---
title: Asymptotic Notation (점근 표기법)
category: concept
tags: [asymptotic, complexity, big-o, big-theta, big-omega, growth-rate]
sources: [raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

점근 표기법(Asymptotic Notation)은 함수의 점근적 성장률(asymptotic growth rate, asymptotic order)을 상수 인자와 소규모 입력의 영향을 무시하고 비교·분류하는 수학적 도구이다. 알고리즘의 복잡도 함수를 O(g), Θ(g), Ω(g) 등의 집합(동치류)으로 분류함으로써, 입력 크기가 충분히 커질 때의 상대적 효율을 표현한다.

## How It Works

비음수 정수에서 비음수 실수로 가는 함수 f, g에 대해, 실수 상수 c > 0와 비음수 정수 상수 n0이 존재할 때 다음과 같이 정의한다.

### 집합 정의

| 표기 | 이름 | 조건 | 의미 |
|------|------|------|------|
| O(g) | Big-Oh | f(n) ≤ c·g(n) for all n ≥ n0 | f는 g보다 빠르게 성장하지 않는다 (상한) |
| Ω(g) | Big-Omega | f(n) ≥ c·g(n) for all n ≥ n0 | f는 g보다 느리게 성장하지 않는다 (하한) |
| Θ(g) | Big-Theta | O(g) ∩ Ω(g) | f와 g는 동일한 점근 성장률을 가진다 (tight bound) |

### 극한을 이용한 분류

lim_{n→∞} f(n)/g(n)의 값에 따라:

| 극한값 | 결론 |
|--------|------|
| < ∞ (0 포함) | f ∈ O(g) |
| > 0 (∞ 포함) | f ∈ Ω(g) |
| 0 < c < ∞ | f ∈ Θ(g) |
| = 0 | f ∈ o(g) (little-oh, 진성 상한) |
| = ∞ | f ∈ ω(g) (little-omega, 진성 하한) |

f ∈ o(g)는 f가 g보다 엄격하게 느리게 성장함을, f ∈ ω(g)는 f가 g보다 엄격하게 빠르게 성장함을 의미한다.

### 주요 성장률 분류 예시

- O(1): 상수 함수 집합 (입력 크기와 무관한 연산)
- Θ(log n): 로그 성장 (예: 이진 탐색)
- Θ(n): 선형 성장 (예: 순차 탐색)
- Θ(n log n): 선형 로그 성장 (예: 효율적인 정렬)
- Θ(n²): 이차 성장; Θ(n³): 삼차 성장
- Θ(c^n): 지수 성장 (c > 1)

수열 합의 점근 결과:
- Σ_{i=1}^{n} i ∈ Θ(n²)
- Σ_{i=1}^{n} i^d ∈ Θ(n^{d+1})
- Σ_{i=1}^{n} i·log(i) ∈ Θ(n²·log n)

## Key Properties

- **추이성(Transitivity)**: f ∈ O(g), g ∈ O(h) ⟹ f ∈ O(h). Ω, Θ, o, ω 모두 추이성을 만족한다.
- **반사성(Reflexivity)**: f ∈ Θ(f)
- **대칭성(Symmetry)**: f ∈ Θ(g) ⟺ g ∈ Θ(f)
- **Θ는 동치 관계(equivalence relation)**를 정의하며, 각 Θ(f)는 복잡도 클래스(complexity class)를 이룬다.
- f ∈ O(g) ⟺ g ∈ Ω(f)
- O(f + g) = O(max(f, g)) (Ω, Θ에도 유사한 등식 성립)
- lg n ∈ o(n^α) for any α > 0: 로그는 임의의 양수 지수 다항식보다 느리게 증가한다.
- n^k ∈ o(c^n) for any k > 0, c > 1: 다항식은 임의의 지수 함수보다 느리게 증가한다.

## Relationships

- [[algorithm-analysis]] — 복잡도 함수 W(n), A(n)을 분류하고 비교하는 데 사용
- [[binary-search]] — W(n) ∈ Θ(log n)의 대표적 예시이자 최적성 증명에 활용
- [[sequential-search]] — W(n) ∈ Θ(n)의 대표적 예시

## Open Questions

- 점근 표기법은 상수 인자를 무시하므로, 동일한 Θ 클래스 내에서도 실제 성능 차이가 클 수 있다 — 실용적 알고리즘 선택에서 이 한계를 어떻게 보완할 것인가?
- o(g), ω(g) (little 표기법)는 알고리즘 분석에서 Big 표기법에 비해 언제 유용한가?

## Sources

- raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf
