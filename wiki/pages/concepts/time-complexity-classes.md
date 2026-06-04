---
title: Time Complexity Classes
category: concept
tags: [algorithm, complexity, time-complexity, hierarchy]
sources: [raw/자료구조/CSE2112_02_week02_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

시간 복잡도 클래스(time complexity class)는 알고리즘의 실행 시간이 입력 크기 n에 대해 어떤 함수적 관계를 가지는지를 점근적으로 분류한 것이다. Big-Oh 또는 Big-Theta 표기법으로 표현되며, 클래스 간에는 명확한 계층 관계(hierarchy)가 존재한다. 복잡도 클래스가 낮을수록 입력이 커졌을 때도 효율적으로 동작한다.

## How It Works

**복잡도 계층 (낮은 복잡도 → 높은 복잡도)**

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

각 클래스의 특성과 대표 예:

| 표기 | 이름 | 특성 | 대표 알고리즘 예 |
|------|------|------|----------------|
| O(1) | Constant | 입력 크기와 무관한 일정 시간 | 배열 임의 접근(array access) |
| O(log n) | Logarithmic | 입력이 2배 늘어도 연산 수가 1씩 증가 | 이진 탐색(binary search), 이진 트리 탐색 |
| O(n) | Linear | 입력에 비례하는 시간 | 선형 탐색(linear search), prefix averages 최적화 버전 |
| O(n log n) | Linear-Logarithmic | 선형보다 조금 느리나 2차보다 훨씬 빠름 | 병합 정렬(merge sort) |
| O(n²) | Quadratic | 입력의 제곱에 비례 | 버블 정렬(bubble sort), prefix averages 단순 버전 |
| O(2ⁿ) | Exponential | 입력이 1 증가할 때마다 실행 시간이 2배 | 피보나치 재귀 계산 (Fₙ = Fₙ₋₁ + Fₙ₋₂) |

**같은 문제, 다른 복잡도 클래스 예시**

prefix averages 문제 (A[i] = (X[0] + X[1] + ... + X[i]) / (i+1)):

- `prefixAverages1` (중첩 루프): 매 i마다 X[0]부터 X[i]까지 합산 → 1 + 2 + ... + (n−1) = n(n+1)/2 연산 → **O(n²)**
- `prefixAverages2` (running sum): 누적합 s를 유지하며 s ← s + X[i]로 갱신 → 루프당 상수 연산 → **O(n)**

power function 문제 (p(x, n) = xⁿ):

- 단순 재귀 (p(x, n) = x · p(x, n−1)): n번 재귀 호출 → **O(n)**
- Repeated squaring: n을 반으로 나누며 재귀 (짝수: p(x, n/2)², 홀수: x · p(x, (n−1)/2)²) → 재귀 깊이 log n → **O(log n)**

## Key Properties

- 복잡도 클래스 사이의 차이는 n이 클수록 극단적으로 벌어진다. n = 10⁶에서 O(n)은 10⁶ 연산이지만, O(n²)은 10¹² 연산이다.
- Polynomial 복잡도(O(nᵏ))는 현실적으로 다룰 수 있는 알고리즘으로 간주되지만, Exponential O(2ⁿ)은 입력이 조금만 커져도 비실용적이다.
- 같은 문제라도 알고리즘 설계에 따라 복잡도 클래스가 달라진다. 더 낮은 클래스의 알고리즘이 항상 선호된다.
- Iterative 알고리즘과 Recursive 알고리즘이 같은 복잡도 클래스에 속할 수 있으나, 재귀 설계 방식(단순 재귀 vs. divide-and-conquer)에 따라 클래스가 달라질 수 있다.

## Relationships

- [[big-oh-notation]] — 각 클래스를 형식적으로 표현하는 Big-Oh 표기법의 정의와 규칙
- [[asymptotic-bounds]] — Big-Theta를 통한 각 클래스의 tight bound 표현 및 best/worst-case 구분

## Open Questions

- O(n log n)과 O(n²) 사이에 실용적으로 중요한 O(n^1.585) (Karatsuba 곱셈) 같은 중간 복잡도가 존재하지만, 기본 교육과정에서는 표준 클래스들만 다루어진다.
- 공간 복잡도(space complexity)는 이 강의에서 별도로 다루어지지 않았다. 재귀 알고리즘의 경우 call stack으로 인해 시간 복잡도와 공간 복잡도가 같은 클래스에 속하는 경향이 있다.
- Exponential 클래스 이상(예: O(n!))은 이 강의에서 언급되지 않았으나, 조합 최적화 문제에서 자주 등장한다.

## Sources

- raw/자료구조/CSE2112_02_week02_1.pdf
