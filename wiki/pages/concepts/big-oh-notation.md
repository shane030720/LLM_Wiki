---
title: Big-Oh Notation
category: concept
tags: [algorithm, complexity, big-oh, asymptotic, primitive-operation]
sources: [raw/자료구조/CSE2112_02_week02_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Big-Oh notation은 함수 f(n)의 점근적 상한(asymptotic upper bound)을 표현하는 수학적 표기법이다. f(n)이 O(g(n))이라는 것은 양의 상수 c와 n₀가 존재하여 n ≥ n₀인 모든 n에 대해 f(n) ≤ c·g(n)이 성립함을 의미한다. 알고리즘 분석에서는 입력 크기 n에 대한 최악의 경우(worst-case) 실행 시간을 표현할 때 주로 사용된다.

## How It Works

Big-Oh를 구하는 과정은 다음 세 단계로 이루어진다.

**1단계: Primitive Operations 계산**

Pseudocode를 검사하여 기본 연산(primitive operation)의 수를 n의 함수로 표현한다. RAM 모델에서 각 primitive operation은 상수 시간이 걸린다고 가정한다. 인정되는 primitive operation의 종류:
- 변수에 값 할당 (`x = 5`)
- 산술 연산 (`a + b`)
- 두 값 비교 (`if a > b`)
- 배열 인덱싱 (`A[3]`)
- 함수 호출 및 반환
- 객체 참조 (`student.name`)

예시: `arrayMax(A, n)`의 primitive operation 수 계산
```
currentMax ← A[0]          : 2회
for i ← 1 to n−1 do        : 2n회
  if A[i] > currentMax then : 2(n−1)회
    currentMax ← A[i]      : 2(n−1)회
return currentMax           : 1회
총계: 6n − 1
```

**2단계: 수식 단순화 (Big-Oh 규칙 적용)**

- 하위 차수 항(lower-order terms) 제거
- 상수 계수(constant factors) 제거
- 예: 6n − 1 → O(n)

**3단계: 수학적 증명 (필요 시)**

c와 n₀ 값을 명시적으로 구성하여 정의를 만족함을 보인다.
- 예: 2n + 10이 O(n)임을 증명 → c = 3, n₀ = 10으로 설정하면 n ≥ 10에서 2n + 10 ≤ 3n 성립.
- 예: 3n³ + 20n² + 5가 O(n³)임을 증명 → c = 4, n₀ = 21로 설정.
- 예: 3 log n + 5가 O(log n)임을 증명 → c = 8, n₀ = 2로 설정.

## Key Properties

- **Drop lower-order terms**: f(n) = 3n³ + 20n² + 5 → O(n³)
- **Drop constant factors**: f(n) = 7n − 2 → O(n)
- **Smallest possible class 사용**: "2n is O(n)"을 쓰며 "2n is O(n²)"이라 하지 않는다.
- **Simplest expression 사용**: "3n + 5 is O(n)"을 쓰며 "3n + 5 is O(3n)"이라 하지 않는다.
- 점근적 분석에서 상수와 하위 항은 결국 무시되므로, primitive operation 계산 시 정밀한 계수보다 차수(order)에 집중해도 무방하다.
- Big-Oh는 유일하지 않다(non-unique): 하나의 함수에 대해 O(n), O(n²), O(n³) 등 여러 상한이 모두 수학적으로 참이다. 그러나 가장 작은 클래스(tightest upper bound)를 사용하는 것이 관례다.

## Relationships

- [[asymptotic-bounds]] — Big-Oh의 대응 개념인 Big-Omega(하한)와 Big-Theta(tight bound)
- [[time-complexity-classes]] — Big-Oh로 분류되는 주요 복잡도 클래스 계층과 대표 알고리즘 예시

## Open Questions

- Primitive operation 하나의 정의 범위는 언어·모델마다 달라질 수 있다. 예를 들어 `i++`는 단일 증분(1회), arithmetic+assignment(2회), read+arithmetic+assignment(3회) 중 어느 것으로 셀 것인가는 명확히 정해져 있지 않다. Big-Oh 차원에서는 무관하지만, 정밀한 연산 횟수 분석이 필요한 경우 기준을 명시해야 한다.
- 이 강의에서는 worst-case 분석을 중심으로 다루고 있으나, average-case 분석은 다루지 않는다.

## Sources

- raw/자료구조/CSE2112_02_week02_1.pdf
