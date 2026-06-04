---
title: Vector (Array List)
category: concept
tags: [vector, array-list, sequence, data-structure, dynamic-array]
sources: [raw/자료구조/CSE2112_02_week04_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Vector(Array List)는 n개의 요소를 선형 순서로 저장하고, 인덱스(index)를 통해 임의 접근(random access)을 지원하는 Sequence 자료구조다. 배열의 개념을 확장하여 동적 삽입·제거 연산을 제공하며, 잘못된 인덱스를 지정하면 예외(exception)가 발생한다.

## How It Works

**핵심 연산 및 시간 복잡도:**

| 연산 | 설명 | 시간 복잡도 |
|------|------|-------------|
| `at(i)` | i번째 요소 반환 | O(1) |
| `set(i, e)` | i번째 요소를 e로 교체 | O(1) |
| `insert(i, e)` | 인덱스 i에 요소 e 삽입; A[i]~A[n-1]을 한 칸씩 앞으로 이동 | O(n) worst case |
| `erase(i)` | i번째 요소 제거; A[i+1]~A[n-1]을 한 칸씩 당겨옴 | O(n) worst case |
| `size()` | 요소 수 반환 | O(1) |
| `empty()` | 비어있는지 여부 반환 | O(1) |

`insert`와 `erase`의 worst case는 i=0일 때이며, 모든 요소를 이동해야 하므로 O(n)이 된다.

**Growable Array (동적 확장):**

배열이 가득 찰 경우 더 큰 배열로 교체하는 절차:
1. 더 큰 크기의 새 배열 할당
2. 기존 요소 전체 복사
3. 기존 메모리 해제 (`delete[]`)

크기 결정 전략 두 가지:
- **Incremental strategy**: 크기를 상수 c만큼 증가 → 총 삽입 비용 O(n²) amortized O(n)
- **Doubling strategy**: 크기를 2배로 증가 (`N = 2N`) → amortized O(1) 삽입 보장

C++ `std::vector`는 doubling strategy를 사용한다.
- `capacity()`: 현재 할당된 메모리 블록의 최대 수용 크기
- `size()`: 실제 저장된 요소 수

```cpp
vector<int> v = {1, 2, 3, 4, 5};
// capacity: 5, size: 5
for(int i=0; i<3; i++) v.push_back(i);
// size: 8, capacity: 10  (doubled from 5 to 10)
```

**원형 배열 활용:**

배열을 원형으로 사용하면 `insert(0, x)` 및 `erase(0)` 연산을 O(1)로 수행할 수 있다.

## Key Properties

- 연속된 메모리 주소(contiguous memory)에 저장 → cache-friendly 접근
- `at`, `set` → O(1); `insert`, `erase` → O(n) worst case
- Doubling strategy 적용 시 공간 복잡도 O(N), amortized 삽입 O(1)
- 직접 활용: 정렬된 객체 컬렉션 (초보적 데이터베이스)
- 간접 활용: 알고리즘의 보조 자료구조, 다른 자료구조의 구성 요소

## Relationships

- [[queue]] (원형 배열로 구현 가능한 자료구조; Vector의 원형 활용 기법과 연관)
- [[deque]] (양방향 접근을 지원하는 Sequence; C++ `std::deque`는 Vector의 변형)

## Open Questions

- Incremental strategy vs. Doubling strategy의 정확한 amortized 시간 복잡도 비교: 각각 O(n)과 O(1)이 되는 이유를 수식으로 어떻게 증명하는가?
- 원형 배열을 적용할 경우 중간 인덱스 `insert`/`erase` 연산의 복잡도는 여전히 O(n)인가?
- 메모리 할당 비용(new/delete)이 amortized 분석에서 어떻게 처리되는가?

## Sources

- raw/자료구조/CSE2112_02_week04_2.pdf
