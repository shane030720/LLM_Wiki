---
title: Pseudocode
category: concept
tags: [algorithm, pseudocode, notation, analysis]
sources: [raw/자료구조/CSE2112_02_week01_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Pseudocode(의사코드)란 알고리즘을 기술하기 위한 고수준(high-level) 표기법으로, 영어 산문보다는 구조적이고 실제 프로그램보다는 덜 상세하다. 특정 프로그래밍 언어에 종속되지 않으면서 알고리즘의 핵심 로직을 명확히 표현하며, 알고리즘 기술의 표준 표기법(preferred notation)으로 사용된다.

## How It Works

### 기본 문법 요소

**제어 흐름 (Control flow):**
- `if … then … [else …]`
- `while … do …`
- `repeat … until …`
- `for … do …`
- 중괄호 대신 들여쓰기로 블록 구조 표현

**메서드 선언:**
```
Algorithm method(arg [, arg...])
 Input  ...
 Output ...
```

**표기 규칙:**
- 대입: `←` 기호 (C++의 `=`에 해당)
- 동등 비교: `=` 기호 (C++의 `==`에 해당)
- 지수 등 수학 서식 허용 (예: n²)
- 메서드 호출: `var.method(arg [, arg…])`
- 반환: `return expression`

### 예시: arrayMax

```
Algorithm arrayMax(A, n)
 Input  array A of n integers
 Output maximum element of A
 currentMax <- A[0]
 for i <- 1 to n - 1 do
  if A[i] > currentMax then
   currentMax <- A[i]
 return currentMax
```

### 왜 Pseudocode를 사용하는가

같은 알고리즘을 C/C++, Java, Python으로 구현하면 언어마다 문법과 세부 사항이 다르지만, 의사코드는 언어 중립적으로 핵심 로직만을 표현한다. 이를 통해 알고리즘 자체에 집중하고 프로그램 설계 세부 사항(program design issues)을 숨길 수 있다.

## Key Properties

- **언어 독립성:** 특정 프로그래밍 언어 문법에 종속되지 않아 다양한 독자가 이해 가능하다
- **분석 용이성:** Primitive operation 카운팅과 Big-Oh 분석의 기반이 된다
- **추상화 수준:** 영어 산문보다 구조적이고, 실제 코드보다 덜 상세한 중간 수준이다
- **설계 집중:** 프로그래밍 언어 세부 사항을 숨겨 알고리즘 로직 설계에 집중할 수 있다
- **범용성:** 학술 논문, 교재, 강의에서 알고리즘 기술의 표준으로 폭넓게 사용된다

## Relationships

- [[algorithm-analysis]] — 이론적 알고리즘 분석의 기술 수단으로, pseudocode를 분석하여 primitive operation 수를 도출한다
- [[big-oh-notation]] — pseudocode로 기술된 알고리즘의 연산 횟수를 세어 Big-Oh 복잡도를 유도한다

## Open Questions

- 의사코드의 표준화 수준은 저자마다 다를 수 있어, 동일한 알고리즘도 표기 방식이 다양할 수 있다
- 의사코드에서 primitive operation의 경계를 어디까지로 볼 것인가는 분석의 세밀도에 따라 달라진다

## Sources

- raw/자료구조/CSE2112_02_week01_2.pdf
