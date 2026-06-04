---
title: Asymptotic Bounds (Big-Omega, Big-Theta, Best/Worst Case)
category: concept
tags: [algorithm, complexity, big-omega, big-theta, asymptotic, best-case, worst-case]
sources: [raw/자료구조/CSE2112_02_week02_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

점근적 경계(asymptotic bounds)는 알고리즘 복잡도를 상한·하한·tight bound 세 관점에서 표현하는 표기 체계다. Big-Oh(O)는 점근적 상한, Big-Omega(Ω)는 점근적 하한, Big-Theta(Θ)는 상한과 하한이 일치하는 tight bound를 나타낸다. 실제 복잡도 f(n)에 대해 Ω(g(n)) ≤ f(n) ≤ O(g(n))이 동시에 성립할 때 f(n) = Θ(g(n))이다.

## How It Works

**세 표기법의 수학적 정의**

| 표기 | 이름 | 의미 |
|------|------|------|
| O(g(n)) | Upper bound (상한) | f(n) ≤ c·g(n) for n ≥ n₀ |
| Ω(g(n)) | Lower bound (하한) | f(n) ≥ c·g(n) for n ≥ n₀ |
| Θ(g(n)) | Tight bound | Ω(g(n)) ≤ f(n) ≤ O(g(n)) |

Big-Oh와 Big-Omega는 유일하지 않다. 3n log n + 2n에 대해 O(n log n), O(n²), O(n³) 등이 모두 기술적으로 성립한다. 반면 Big-Theta는 일반적으로 유일(unique)하며 가장 정확한 복잡도 표현이다.

**표기법 선택 예시**

| 함수 | Big-Oh (upper) | Big-Omega (lower) | Big-Theta (tight) |
|------|----------------|-------------------|-------------------|
| 3n log n + 2n | O(n log n), O(n²), … | Ω(n log n), Ω(n), … | Θ(n log n) |
| 3n log n + 5 log n | O(n log n), O(n²), … | Ω(n log n), Ω(n), … | Θ(n log n) |
| n log n + n³ | O(n³), O(n⁴), … | Ω(n³), Ω(n²), … | Θ(n³) |

실용적 관례: 항상 가장 tight한 표기를 사용한다.
- O(n log n)을 쓰며 O(n²)이라 하지 않는다.
- Ω(n log n)을 쓰며 Ω(n)이라 하지 않는다.

**Best-case와 Worst-case 복잡도**

- **Best-case**: 알고리즘에 가장 유리한 입력에 대한 복잡도. Θ로 표현하거나 O와 Ω를 함께 명시한다.
- **Worst-case**: 가장 불리한 입력에 대한 복잡도. 성능 보장의 기준으로 가장 중요하게 다루어진다.

Linear search 예시:
```
Algorithm linearSearch(A, n, x)
  for i ← 0 to n−1 do
    if A[i] = x then
      return i
```
- Best-case: Θ(1) — 찾는 원소가 인덱스 0에 위치할 때
  - O(1) 또는 Ω(1)은 물론, O(n), O(n²) 등도 수학적으로 참이나, tight bound인 Θ(1)이 정확한 표현
- Worst-case: Θ(n) — 찾는 원소가 마지막 인덱스에 있거나 배열에 없을 때
  - O(n) 또는 Ω(n)은 물론, O(n²), Ω(1) 등도 참이나, tight bound인 Θ(n)이 정확한 표현

## Key Properties

- Big-Oh와 Big-Omega는 non-unique: 느슨한 bound도 수학적으로 참이다.
- Big-Theta는 일반적으로 unique하며 가장 정밀한 복잡도 표현이다.
- 실용적 분석에서는 항상 tight bound를 우선 사용한다.
- Worst-case 복잡도가 알고리즘 성능 보장의 표준 기준이다.
- Best-case만으로 알고리즘을 평가하는 것은 오해를 유발할 수 있다.

## Relationships

- [[big-oh-notation]] — Big-Oh의 수학적 정의, 계산 규칙, primitive operations 계산법
- [[time-complexity-classes]] — 각 표기법으로 분류되는 대표적 복잡도 클래스들

## Open Questions

- Average-case 복잡도는 이 강의에서 다루어지지 않았다. Quicksort와 같이 average-case가 worst-case보다 실용적으로 더 중요한 알고리즘에서는 확률적 분석이 필요하며, 이는 별도의 분석 체계를 요한다.
- Best-case 복잡도는 실용적 가치가 제한적이나, 특정 경우(예: already-sorted input에 대한 insertion sort)에서는 의미 있는 분석 도구가 된다.

## Sources

- raw/자료구조/CSE2112_02_week02_1.pdf
