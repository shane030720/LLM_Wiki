---
title: Stack Implementation Comparison: Array vs Linked List
category: synthesis
tags: [stack, array, linked-list, comparison, tradeoff, data-structure]
sources: [raw/자료구조/CSE2112_02_week03_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Thesis

[[stack]] ADT를 구현하는 두 가지 주요 방식—[[array-based-stack]]과 [[linked-list-based-stack]]—은 모든 연산에서 동일한 O(1) 시간복잡도를 제공하지만, 메모리 관리 방식과 예외 처리 범위에서 근본적인 트레이드오프를 가진다. 어느 구현이 우월하다고 단정할 수 없으며, 사용 환경의 요구사항에 따라 선택해야 한다.

## Evidence

**공통점**
- push, pop, top, size, empty 연산 모두 O(1) 시간복잡도
- 빈 스택에서 `top()`, `pop()` 호출 시 `StackEmpty` 예외 발생

**Array-based Stack의 특징**
- 멤버 변수: 배열 S, 용량 capacity, top 인덱스 t (초기값 -1)
- `push` 시 `t ← t + 1`로 인덱스 이동; 배열 범위 초과 시 `StackFull` 예외 발생
- 연속된 메모리 블록 사용으로 캐시 효율 우수
- 공간 사용이 실제 원소 수 n이 아닌 배열 크기 N에 고정됨

**Linked List-based Stack의 특징**
- 멤버 변수: SLinkedList S, 원소 수 n (head 초기값 nullptr)
- `push` = `addFront`, `pop` = `removeFront`로 head에서 O(1) 처리
- 용량 제한 없음: `StackFull` 예외가 존재하지 않음
- 각 노드에 next 포인터 저장으로 메모리 오버헤드 발생

| 항목 | Array-based | Linked List-based |
|------|-------------|-------------------|
| 시간복잡도 | O(1) | O(1) |
| 공간복잡도 | O(N) — N 고정 | O(n) — n에 비례 |
| 최대 용량 | 사전 정의 필요 | 제한 없음 |
| StackFull 예외 | 발생 | 발생하지 않음 |
| StackEmpty 예외 | 발생 | 발생 |
| 메모리 연속성 | 연속 (캐시 효율↑) | 비연속 (포인터 오버헤드) |

## Counterevidence

- Array-based Stack도 내부적으로 동적 배열(예: C++ `std::vector`)을 사용하면 용량 제한을 우회할 수 있다. 단, 이 경우 resize 발생 시 amortized O(1)이 되어 엄밀히는 worst-case O(1)이 보장되지 않는다.
- Linked List-based Stack의 포인터 오버헤드는 원소 데이터가 클수록 상대적으로 무시할 수 있는 수준이 된다.

## Conclusion

최대 원소 수를 예측 가능하고 메모리 연속성이 중요한 성능 민감 환경에서는 [[array-based-stack]]이 적합하다. 원소 수가 가변적이거나 StackFull 예외 처리를 피해야 하는 환경에서는 [[linked-list-based-stack]]이 적합하다. 교육 자료(CSE2112)는 두 구현이 Stack ADT의 핵심 계약(O(1) 연산, StackEmpty 예외)을 동등하게 만족하되, 용량 제한(`StackFull`)이 ADT 고유의 제약이 아닌 Array-based 구현 특유의 한계임을 명시한다.

## Sources

- raw/자료구조/CSE2112_02_week03_2.pdf
