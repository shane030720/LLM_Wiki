---
title: Array Doubling
category: concept
tags: [array, dynamic-array, amortized, data-structure]
sources: [raw/알고리즘/CH06 동적 집합과 탐색.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Array Doubling(배열 배증)은 동적 배열(dynamic array)에서 공간이 부족할 때 현재 배열의 두 배 크기의 새 배열을 할당하고 기존 요소를 모두 이전함으로써 배열 크기를 자동으로 늘리는 기법이다. 계산 시작 시점에 필요한 배열 크기를 알 수 없을 때 사용한다.

## How It Works

1. 새 원소 삽입 시 현재 배열에 공간이 없으면 배열 배증을 트리거한다.
2. 현재 크기의 두 배 크기의 새 배열을 할당한다.
3. 기존 모든 원소를 새 배열로 복사한다 (원소 하나당 비용 t).
4. 이후 삽입은 새 배열에서 계속된다.

**총 비용 분석:**

- (n+1)번째 원소 삽입 시 배열 배증이 발생한다고 가정하면, 이번 배증 비용은 `t·n`이다.
- 이전 배증들의 비용 합: `t·n/2 + t·n/4 + t·n/8 + … < t·n` (등비급수)
- 따라서 n번의 삽입에 대한 **총 비용은 2t·n을 초과하지 않는다.**
- 연산당 상각 비용(amortized cost per operation)은 O(1)이다.

Stack에 적용할 경우, push 연산의 amortized cost는 `1 + 2t`로 일정하게 유지된다.

## Key Properties

- 배열 크기를 두 배씩 늘리므로 메모리 낭비는 최대 50%다.
- 개별 삽입 연산의 최악 비용은 O(n)이지만, 상각 비용은 O(1)이다.
- 크기를 1씩 늘리는 방식 대비 전체 복사 비용이 O(n²) → O(n)으로 개선된다.
- Stack, Queue, Vector 등 동적 컬렉션 구현의 기반 기법이다.

## Relationships

- [[amortized-analysis]] (배열 배증의 비용을 정확히 분석하는 데 사용되는 분석 기법)

## Open Questions

- 배증 비율을 2가 아닌 1.5나 다른 상수로 설정할 경우 상각 비용과 메모리 효율은 어떻게 달라지는가?
- 배열 축소(shrinking) 시에도 유사한 상각 분석이 성립하는가?

## Sources

- raw/알고리즘/CH06 동적 집합과 탐색.pdf
