---
title: Matrix-Chain Multiplication Algorithm
category: entity
tags: [algorithm, dynamic-programming, optimization, matrix, combinatorics]
sources: [raw/알고리즘/CH10 동적 계획법.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Matrix-Chain Multiplication(행렬 체인 곱셈) 알고리즘은 n개의 행렬 A1, A2, ..., An의 곱을 계산할 때 스칼라 곱셈 횟수를 최소화하는 괄호 묶기(parenthesization) 순서를 결정하는 최적화 알고리즘이다. [[dynamic-programming]]의 4단계 설계 방법론을 교과서적으로 적용한 대표 예제로, CLRS(Introduction to Algorithms) 등의 표준 교재에서 DP 학습의 출발점으로 사용된다.

**입력:** 행렬 차원 벡터 p = <p0, p1, ..., pn> (행렬 Ai의 크기는 p_{i-1} × p_i)  
**출력:** 최소 스칼라 곱셈 횟수 및 최적 괄호 묶기 순서

행렬 곱셈은 결합 법칙(associative)을 만족하므로 괄호 묶기 순서에 따라 계산 비용이 크게 달라진다. 예를 들어 A1(30×1), A2(1×40), A3(40×10), A4(10×25)의 경우:

| 괄호 묶기 | 스칼라 곱셈 횟수 |
|---|---|
| ((A1 A2) A3) A4 | 20,700 |
| A1 (A2 (A3 A4)) | 11,750 |
| (A1 A2)(A3 A4) | 41,200 |
| A1 ((A2 A3) A4) | **1,400** |

## Capabilities

**Step 1 — 최적 부분 구조 파악:**  
체인 Ai...Aj를 어떤 분할 위치 k에서 Ai...Ak와 Ak+1...Aj로 나눌 때, 두 부분 체인 각각이 최적으로 계산되어야 전체가 최적이다(optimal substructure).

**Step 2 — 점화식 정의:**  
`m[i,j]` = Ai...Aj를 계산하는 데 필요한 최소 스칼라 곱셈 횟수

```
m[i,j] = 0                                            (if i = j)
m[i,j] = min over i <= k < j { m[i,k] + m[k+1,j] + p_{i-1} * p_k * p_j }   (if i < j)
```

`s[i,j]` = 최적 분할 위치 k (경로 복원용)

**Step 3 — Bottom-up 계산 (MATRIX-CHAIN-ORDER):**  
체인 길이 `l`을 2부터 n까지 늘려가며 모든 `(i,j)` 쌍에 대해 `m[i,j]`와 `s[i,j]`를 테이블에 채운다.

```
MATRIX-CHAIN-ORDER(p)
  n ← length(p) - 1
  for i ← 1 to n
    m[i,i] ← 0                         // 단일 행렬: 비용 0
  for l ← 2 to n                       // l: 체인 길이
    for i ← 1 to n - l + 1
      j ← i + l - 1
      m[i,j] ← ∞
      for k ← i to j - 1
        q ← m[i,k] + m[k+1,j] + p_{i-1} * p_k * p_j
        if q < m[i,j]
          m[i,j] ← q
          s[i,j] ← k
  return m and s
```

시간 복잡도: O(n³) — 세 개의 중첩 루프  
공간 복잡도: O(n²) — m, s 테이블

**Step 4 — 최적 해 구성 (PRINT-OPTIMAL-PARENS):**  
s 테이블을 재귀적으로 역추적하여 최적 괄호 묶기 문자열을 출력한다.

```
PRINT-OPTIMAL-PARENS(s, i, j)
  if i = j
    print "A_i"
  else
    print "("
    PRINT-OPTIMAL-PARENS(s, i, s[i,j])
    PRINT-OPTIMAL-PARENS(s, s[i,j]+1, j)
    print ")"
```

## Limitations

- 행렬의 실제 곱셈을 수행하지 않고 **최적 순서만 결정**한다. 실제 곱셈은 별도로 수행해야 한다.
- 행렬이 정방행렬이 아닌 경우, 차원 벡터 p를 정확히 입력해야 하며 차원 불일치 오류에 대한 검증이 포함되어 있지 않다.
- n이 매우 클 경우 O(n²) 공간의 테이블이 메모리 부담이 될 수 있다.
- 행렬 원소의 수치적 특성(희소 행렬, 구조적 행렬 등)은 고려하지 않는다.

## Relationships

- [[dynamic-programming]] — 본 알고리즘이 구현하는 핵심 패러다임. DP 4단계 설계 과정의 교과서적 예제이다.
- [[memoization]] — 동일한 점화식을 Top-down 방식으로 구현하는 대안적 접근. 본 알고리즘은 Bottom-up tabulation을 사용한다.

## Sources

- raw/알고리즘/CH10 동적 계획법.pdf
