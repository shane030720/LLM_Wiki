---
title: Sequence ADT
category: concept
tags: [sequence, adt, data-structure, index, position]
sources: [raw/자료구조/CSE2112_02_week05_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Sequence ADT는 Vector ADT(인덱스 기반 접근)와 List ADT(position 기반 접근)를 통합한 추상 자료형이다. 동일한 요소에 대해 정수 인덱스와 Iterator position 두 가지 방식으로 모두 참조할 수 있으며, 두 표현 사이를 변환하는 연산인 `atIndex(i)`와 `indexOf(p)`를 제공한다.

## How It Works

**두 가지 접근 방식 통합**:
- Index 접근 (Vector 방식): `A[0]`, `A[1]`, ... 형태의 정수 인덱스
- Position 접근 (List 방식): Iterator/포인터로 노드 직접 참조

**변환 연산**:

`atIndex(i)` — 인덱스 → Position:
```cpp
Iterator atIndex(int i) {
  Iterator curr = begin();
  for (int j = 0; j < i; j++) { ++curr; }
  return curr;
}
```
`begin()`부터 i번 전진 → O(n)

`indexOf(p)` — Position → 인덱스:
```cpp
int indexOf(Iterator p) {
  int count = 0;
  Iterator curr = begin();
  while (p != curr) { ++curr; ++count; }
  return count;
}
```
`begin()`부터 p에 도달할 때까지 카운트 → O(n)

## Key Properties

- Vector와 List의 연산을 모두 지원
- `atIndex` / `indexOf` 변환 비용: 이중 연결 리스트 기반 구현 시 모두 O(n)
- 동일 데이터를 인덱스와 position 두 방식으로 모두 접근 가능
- 내부 구현은 이중 연결 리스트 또는 배열 중 선택 가능 (트레이드오프 상이)

## Relationships

- [[array-based-vector]] (Sequence의 인덱스 접근 기능의 원형)
- [[list-adt]] (Sequence의 position 접근 기능의 원형)
- [[iterator]] (position 표현 및 `atIndex`·`indexOf` 순회에 사용)
- [[vector-vs-list]] (Sequence는 두 ADT의 트레이드오프를 절충하는 통합 인터페이스)

## Open Questions

- 이중 연결 리스트 기반 Sequence에서 `atIndex(i)`가 O(n)인 한계를 극복하는 자료구조(예: skip list, order-statistic tree)는 언제 필요한가?
- 배열 기반 Sequence 구현에서 `indexOf(p)`를 O(1)로 만들 수 있는가? (포인터 산술 연산 활용 가능성)
- 실용적인 구현에서 Sequence ADT를 직접 노출하는 경우와 Vector/List를 별도로 사용하는 경우 중 어느 쪽이 더 흔한가?

## Sources

- raw/자료구조/CSE2112_02_week05_2.pdf (Week 05 Lecture 02, slides 27–30)
