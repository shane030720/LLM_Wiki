---
title: Memoization
category: concept
tags: [algorithm, dynamic-programming, recursion, caching, top-down]
sources: [raw/알고리즘/CH10 동적 계획법.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Memoization(메모이제이션)은 재귀 알고리즘에서 하위 문제의 해를 딕셔너리(또는 테이블)에 저장해두고, 동일한 하위 문제가 다시 요청될 때 재계산 없이 저장된 값을 즉시 반환하는 최적화 기법이다. [[dynamic-programming]]의 Top-down 구현 방식에 해당하며, 기존 재귀 알고리즘의 구조를 그대로 유지하면서 중복 계산만 제거한다.

## How It Works

메모이제이션이 적용된 재귀 함수는 다음 절차를 따른다.

1. 래퍼 함수(wrapper)에서 빈 딕셔너리 `soln`을 생성하여 핵심 재귀 함수에 전달한다.
2. 재귀 호출 전, `member(soln, Q)`로 딕셔너리에 해당 하위 문제 Q의 해가 이미 저장되어 있는지 확인한다.
3. 저장되어 있지 않으면 재귀 호출을 수행한다.
4. 저장되어 있으면 `retrieve(soln, Q)`로 값을 가져오고 재귀 호출을 생략한다.
5. 해를 반환하기 직전 `store(soln, k, fib)`로 계산 결과를 딕셔너리에 기록한다.

Fibonacci 수열 예제:

```
fibDPwrap(n)
  Dict soln = create(n)
  return fibDP(soln, n)

fibDP(soln, k)
  if (k < 2) fib = k
  else
    if member(soln, k-1) == false: f1 = fibDP(soln, k-1)
    else: f1 = retrieve(soln, k-1)

    if member(soln, k-2) == false: f2 = fibDP(soln, k-2)
    else: f2 = retrieve(soln, k-2)

    fib = f1 + f2
  store(soln, k, fib)
  return fib
```

## Key Properties

- **Top-down 방식:** 큰 문제에서 시작하여 필요한 하위 문제를 재귀적으로 분해하며 내려간다.
- **Lazy evaluation:** 실제로 필요한 하위 문제만 계산한다. 불필요한 하위 문제는 계산하지 않는다.
- **재귀 구조 보존:** 원래 재귀 알고리즘의 구조를 거의 그대로 유지하여 구현이 직관적이다.
- **딕셔너리 조회 비용:** 해시 기반 딕셔너리 사용 시 조회/저장은 평균 O(1)이다.
- **함수 호출 오버헤드:** Bottom-up DP와 달리 재귀 호출 스택이 남아 있어 스택 오버플로우 가능성이 있다.

## Relationships

- [[dynamic-programming]] — 메모이제이션이 속하는 상위 알고리즘 패러다임. Bottom-up tabulation과 함께 DP의 두 가지 구현 전략 중 하나이다.
- [[matrix-chain-multiplication]] — Bottom-up DP로 구현된 예제. 메모이제이션 방식으로도 동등하게 구현 가능하다.

## Open Questions

- 재귀 깊이가 매우 깊을 경우 스택 오버플로우를 방지하기 위해 반복문 기반 Bottom-up으로 전환해야 하는데, 이 전환 기준은 무엇인가?
- 딕셔너리 키로 복잡한 자료구조(예: 2D 인덱스 쌍)를 사용할 때 해시 충돌이나 성능 저하를 어떻게 관리할 것인가?

## Sources

- raw/알고리즘/CH10 동적 계획법.pdf
