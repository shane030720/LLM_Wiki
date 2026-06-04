---
title: Amortized Analysis
category: concept
tags: [algorithm, analysis, complexity, data-structure]
sources: [raw/알고리즘/CH06 동적 집합과 탐색.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Amortized Analysis(상각 분석)는 연속적인 연산의 최악 경우(worst case)에서 각 연산의 평균 비용을 분석하는 기법이다. 개별 연산이 경우에 따라 비용이 크게 달라지더라도, 일련의 연산 전체에 걸쳐 총 비용을 분산(amortize)하여 각 연산의 실질적인 비용을 추정한다.

## How It Works

Accounting Method(회계 방법)을 사용하여 분석한다.

- **amortized cost = actual cost + accounting cost**
- 각 연산마다 서로 다른 accounting cost를 배정한다.
- 합법적인(legal) 연산 순서에 대해 accounting cost의 합은 항상 0 이상이어야 한다 (feasibility 조건).
- accounting cost가 음수인 경우, 이전 연산에서 쌓아 둔 잉여분(credit)을 사용하는 것으로 해석한다.

**Array Doubling을 이용한 Stack 예시:**

| 상황 | actual cost | accounting cost | amortized cost |
|------|------------|----------------|---------------|
| 배열 확장 없이 push | 1 | +2t | 1 + 2t |
| 배열 확장(doubling) 발생 시 push | 1 + t·n | −t·n + 2t | 1 + 2t |

두 경우 모두 amortized cost가 `1 + 2t`로 동일하게 유지됨을 보여, 개별 연산의 상각 비용이 일정함을 증명한다.

## Key Properties

- 개별 연산의 최악 비용이 아닌, **연속된 연산 시퀀스 전체**에 대한 비용을 분석한다.
- Accounting method에서 accounting cost의 누적 합은 어느 시점에서도 음수가 되어선 안 된다.
- 실제 비용이 큰 연산(예: 배열 확장)은 음의 accounting cost를 부여해 이전 연산들이 미리 비용을 적립하도록 설계한다.
- 결과적으로 각 연산의 amortized cost는 O(1) 혹은 O(log n) 등 단순한 형태로 표현된다.

## Relationships

- [[array-doubling]] (amortized analysis의 대표적 적용 사례로, 배열 배증 비용 분석에 사용됨)
- [[binary-search-tree]] (트리 연산의 평균 비용 분석에도 유사한 개념이 적용됨)

## Open Questions

- Accounting method 외에 Potential method, Aggregate method 등 다른 상각 분석 기법과의 표현력 차이는 무엇인가?
- 비결정적(non-deterministic) 연산 순서에서도 상각 분석이 유효한가?

## Sources

- raw/알고리즘/CH06 동적 집합과 탐색.pdf
