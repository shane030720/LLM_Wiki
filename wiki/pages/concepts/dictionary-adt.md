---
title: Dictionary ADT
category: concept
tags: [dictionary, adt, hash, data-structure, search]
sources: [raw/자료구조/CSE2112_02_week12_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Dictionary ADT(추상 자료형)는 키-값(key-value) 쌍의 항목(entry)들을 저장하며, 탐색(search)·삽입(insert)·삭제(delete) 연산을 제공하는 자료 구조 인터페이스이다. 동일 키를 가진 복수 항목을 허용한다. 응용 예시로는 단어-정의 쌍, 학번-학적 기록, DNS 호스트명-IP 주소 매핑 등이 있다.

## How It Works

### 주요 메서드

- `find(k)`: 키 k를 가진 항목이 있으면 해당 이터레이터를 반환, 없으면 end 반환
- `findAll(k)`: 키 k를 가진 모든 항목의 범위 `[b, e)`를 이터레이터 쌍으로 반환
- `put(k, v)`: 키 k, 값 v를 가진 항목을 삽입하고 이터레이터 반환
- `erase(k)`: 키 k를 가진 항목 삭제

### List-Based Dictionary (Log File)

비정렬 시퀀스(unsorted sequence)로 구현한다.

```
Algorithm find(k):
  for each p in [S.begin(), S.end()) do
    if p.key() = k then return p

Algorithm put(k, v):
  Create a new entry e = (k, v)
  p = S.insertBack(e)
  return p

Algorithm erase(k):
  for each p in [S.begin(), S.end()) do
    if p.key() = k then S.erase(p)
```

- `put`: O(1) — 시퀀스 맨 앞 또는 뒤에 삽입
- `find`, `erase`: O(n) — 전체 순회 필요
- 삽입이 빈번하고 탐색·삭제가 드문 소규모 사전에 적합 (예: 워크스테이션 로그인 기록)

### Ordered Search Table

정렬된 배열(sorted array)로 구현한다.

- `find`: O(log n) — 이진 탐색([[binary-search]]) 활용
- `put`, `erase`: O(n) — 항목 이동(shift)이 필요
- 탐색이 빈번하고 삽입·삭제가 드문 소규모 사전에 적합

### Hash Table-Based Dictionary

해시 함수와 충돌 처리 전략([[hash-collision-handling]])을 사용한다.

- 평균 O(1) 탐색·삽입·삭제
- 최악의 경우 O(n) (모든 해시 값이 동일할 때)

## Key Properties

- 동일 키를 가진 복수 항목을 허용한다
- 구현 방식(List, Search Table, Hash Table)에 따라 성능 특성이 상이하다
- List 기반은 삽입에 최적화되어 있으나 탐색 최악 보장이 없다
- Ordered Search Table은 탐색에 최적화되어 있으나 수정 연산 비용이 크다
- Hash Table은 평균 O(1)이나 최악의 경우를 보장하지 못한다
- 최악의 경우를 보장하려면 BST 등의 정렬 기반 구조가 필요하다

## Relationships

- [[hash-collision-handling]] (Hash Table 기반 구현의 충돌 처리 전략)
- [[binary-search]] (Ordered Search Table의 find 연산에서 사용)

## Open Questions

- Hash Table 기반 Dictionary에서 최악의 경우 O(n)을 피하려면 어떤 구조를 사용해야 하는가?
- `findAll` 연산을 Hash Table 위에서 효율적으로 구현하려면 어떤 변형이 필요한가?

## Sources

- raw/자료구조/CSE2112_02_week12_2.pdf
