---
title: Array-Based Vector
category: concept
tags: [vector, array, data-structure, adt]
sources: [raw/자료구조/CSE2112_02_week05_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Array-Based Vector는 고정 크기 배열을 내부 저장소로 사용하여 Vector ADT를 구현한 자료구조다. 요소는 0부터 시작하는 정수 인덱스(index)로 참조된다. 용량(capacity `N`)이 실제 크기(size `n`)에 도달하면 두 배 크기의 새 배열을 할당해 확장하는 Growable Vector 전략을 채택한다.

## How It Works

**내부 상태**: 세 멤버 변수를 유지한다.
- `elements`: 요소를 저장하는 배열 포인터
- `n`: 현재 저장된 요소 수 (size)
- `N`: 현재 할당된 배열 용량 (capacity), 초기값 1

**주요 연산**:
- `at(i)` / `set(i, value)`: 인덱스 i의 요소에 O(1)로 접근·수정
- `insert(i, value)`: 인덱스 i 이후 요소를 모두 한 칸씩 오른쪽으로 이동 후 삽입 → O(n)
- `erase(i)`: 인덱스 i+1부터 끝까지 요소를 한 칸씩 왼쪽으로 이동하여 덮어쓴 뒤 `n--` → O(n)

**Growable Vector (동적 확장)**: `n == N`일 때 삽입 시도 시:
1. 크기 `N * 2`인 새 배열 B를 할당
2. 기존 배열 A의 내용을 B로 복사
3. 기존 배열 A를 해제하고 포인터를 B로 교체

## Key Properties

- 요소 참조 방식: Index (정수)
- Random access: O(1) — 인덱스로 직접 주소 계산
- 삽입/삭제: O(n) — 요소 이동 필요
- 공간 복잡도: O(N) — N은 실제 요소 수 n보다 클 수 있음
- 2배 확장 전략으로 amortized O(1) append 달성
- 연속 메모리 배치로 cache locality 우수

## Relationships

- [[sequence-adt]] (Array-Based Vector에 position 접근을 추가하면 Sequence ADT가 됨)
- [[vector-vs-list]] (Array-Based Vector와 List ADT의 시간·공간 복잡도 비교)
- [[list-adt]] (대안적 구현 — 배열 대신 이중 연결 리스트 사용)

## Open Questions

- 배열 축소(shrinking) 전략: 요소가 많이 줄었을 때 배열을 줄이는 기준은 무엇인가?
- `insert`와 `erase`의 O(n) 비용을 줄이기 위한 대안 구조(예: gap buffer, deque)는 언제 적용하는가?
- capacity 초기값을 1로 설정했을 때 초기 확장 비용이 지나치게 자주 발생하지는 않는가?

## Sources

- raw/자료구조/CSE2112_02_week05_2.pdf (Week 05 Lecture 02, slides 5–8)
