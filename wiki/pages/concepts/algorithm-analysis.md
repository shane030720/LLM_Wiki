---
title: Analysis of Algorithms
category: concept
tags: [algorithm, analysis, running-time, complexity, worst-case]
sources: [raw/자료구조/CSE2112_02_week01_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Algorithm Analysis(알고리즘 분석)란 알고리즘의 실행 시간(running time)과 자원 사용량을 입력 크기 n의 함수로 특성화하는 이론적 방법론이다. 실제 구현 없이도 알고리즘의 효율성을 하드웨어·소프트웨어 환경에 독립적으로 평가할 수 있게 한다. N. Wirth의 표현처럼 "프로그램 = 자료구조 + 알고리즘"이며, 알고리즘은 문제를 효율적으로 풀기 위한 유한하고 명확한 단계의 집합이다.

## How It Works

### 실험적 분석 (Experimental Studies)
알고리즘을 실제로 구현한 뒤 다양한 크기와 구성의 입력으로 실행하고, `clock()` 같은 함수로 실제 실행 시간을 측정하여 플롯한다.

**한계:**
- 구현이 선행되어야 하므로 비용이 크다
- 실험에 포함되지 않은 입력에 대한 결과를 보장할 수 없다
- 두 알고리즘을 공정하게 비교하려면 동일한 하드웨어/소프트웨어 환경이 필요하다

### 이론적 분석 (Theoretical Analysis)
알고리즘을 의사코드(pseudocode)로 고수준 기술하고, 실행 시간을 입력 크기 n의 함수로 표현한다. 모든 가능한 입력을 고려하며 환경에 독립적이다.

### Primitive Operations (기본 연산)
RAM(Random Access Machine) 모델에서 각각 상수 시간이 걸린다고 가정하는 기본 연산:
- 표현식 평가 (Evaluating an expression)
- 변수 값 할당 (Assigning a value to a variable)
- 배열 인덱싱 (Indexing into an array)
- 메서드 호출 (Calling a method)
- 메서드에서 반환 (Returning from a method)

### Running Time 분석 예시 (arrayMax)

```
Algorithm arrayMax(A, n)              # operations
 currentMax <- A[0]                  2
 for i <- 1 to n - 1 do              2n
  if A[i] > currentMax then          2(n - 1)
   currentMax <- A[i]               2(n - 1)
 return currentMax                   1
                           Total: 6n - 1
```

최악의 경우 6n − 1번의 기본 연산이 실행된다. 가장 빠른 기본 연산 시간을 a, 가장 느린 것을 b라 하면 실행 시간 T(n)은 두 선형 함수 사이에 bounded된다:

```
a(6n - 1) <= T(n) <= b(6n - 1)
```

## Key Properties

- **Worst-case focus:** 최악의 경우 실행 시간에 집중한다. 분석이 용이하고 게임·금융·로봇공학 등 응용에서 결정적이다
- **Growth rate의 불변성:** 하드웨어/소프트웨어 환경 변화는 T(n)에 상수 인자만 영향을 미치며 성장률(growth rate) 자체는 변하지 않는다
- **Constant factors 무시:** 성장률은 상수 인자나 하위 차수 항(lower-order terms)에 영향 받지 않는다 (예: 102n + 105는 선형, 105n² + 108n는 이차)
- **입력 크기 n:** 알고리즘 실행 시간의 주요 결정 인자이며, 대부분의 알고리즘은 n이 커질수록 실행 시간이 증가한다

## Relationships

- [[big-oh-notation]] — 성장률을 수학적으로 표현하는 점근적 표기법으로, 알고리즘 분석의 핵심 도구
- [[pseudocode]] — 이론적 분석에서 알고리즘을 구현 없이 기술하는 데 사용하는 고수준 표기법

## Open Questions

- 평균 경우(average case) 시간 분석은 종종 결정하기 어렵다 — 입력의 확률 분포에 대한 가정이 필요하다
- 공간 복잡도(space complexity) 분석은 이 자료에서 다루지 않는다
- Best case와 average case가 worst case와 크게 다를 때 worst-case focus만으로 충분한가

## Sources

- raw/자료구조/CSE2112_02_week01_2.pdf
