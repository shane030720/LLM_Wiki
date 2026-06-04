---
title: Dynamic Programming
category: concept
tags: [algorithm, optimization, dynamic-programming, subproblem]
sources: [raw/알고리즘/CH10 동적 계획법.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Dynamic Programming(동적 계획법)은 하위 문제(subproblem)의 해를 재계산하지 않고 테이블이나 딕셔너리에 저장해두었다가 재사용함으로써 시간 복잡도를 획기적으로 줄이는 알고리즘 설계 패러다임이다. 핵심 원리는 "공간을 희생하여 속도를 얻는 것(trade space for speed)"이며, 동일한 하위 문제가 반복 등장하는 재귀 구조에서 특히 효과적이다.

## How It Works

Dynamic Programming 알고리즘은 일반적으로 다음 4단계 개발 과정을 따른다.

1. **최적 해의 구조 파악 (Characterize optimal solution structure):** 전체 문제의 최적 해가 하위 문제들의 최적 해로 구성되는지(optimal substructure) 확인한다.
2. **최적 해의 값을 재귀적으로 정의 (Recursively define the value of an optimal solution):** 하위 문제 간의 점화식(recurrence relation)을 수립한다.
3. **Bottom-up 방식으로 최적 해의 값 계산 (Compute in a bottom-up fashion):** 가장 작은 하위 문제부터 순서대로 계산하여 테이블에 채워나간다. 재귀 호출 없이 테이블 조회만으로 상위 문제를 해결한다.
4. **최적 해 구성 (Construct an optimal solution):** 계산 과정에서 저장한 선택 정보(예: 분할 위치 `s[i,j]`)를 역추적하여 실제 최적 해를 복원한다.

## Key Properties

- **Optimal substructure:** 전체 문제의 최적 해가 하위 문제들의 최적 해의 조합으로 표현된다.
- **Overlapping subproblems:** 단순 분할 정복과 달리, 동일한 하위 문제가 여러 경로에서 반복 등장한다. 이 특성이 있어야 메모이제이션이 의미를 가진다.
- **Bottom-up computation:** 작은 크기의 하위 문제부터 해를 구해 테이블에 저장하고, 더 큰 문제는 테이블 조회로 해결한다.
- **두 가지 구현 방식:** 하향식(Top-down, [[memoization]])과 상향식(Bottom-up, tabulation)이 있으며, 두 방식 모두 점근적 시간 복잡도는 동일하다.

## Relationships

- [[memoization]] — Dynamic Programming의 Top-down 구현 방식. 재귀 구조를 유지하면서 딕셔너리로 중복 계산을 제거한다.
- [[matrix-chain-multiplication]] — DP 4단계 설계 방법론을 교과서적으로 적용한 대표 예제 알고리즘.

## Open Questions

- Bottom-up(tabulation)과 Top-down([[memoization]]) 중 실제 구현에서 어느 방식이 더 효율적인가? 일반적으로 Bottom-up은 함수 호출 오버헤드가 없고, Top-down은 불필요한 하위 문제를 계산하지 않는다는 장점이 있어 문제에 따라 다르다.
- 하위 문제의 수가 지수적으로 증가하는 경우 메모리 사용량 폭증 문제를 어떻게 완화할 것인가?

## Sources

- raw/알고리즘/CH10 동적 계획법.pdf
