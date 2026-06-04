---
title: Vector vs List 비교 분석
category: synthesis
tags: [vector, list, data-structure, comparison, ADT, sequence, time-complexity]
sources: [raw/자료구조/CSE2112_02_week06_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Thesis

Array 기반 Vector와 Doubly linked list 기반 List는 동일한 Sequence ADT를 구현하지만, 원소 참조 방식과 삽입·삭제의 시간복잡도에서 근본적인 trade-off를 가진다. Sequence ADT는 `atIndex()`와 `indexOf()` 연산으로 두 방식을 통합하지만, 이 변환 연산 자체가 O(n) 비용을 수반한다.

## Evidence

### 핵심 비교표

| 항목 | Vector | List |
|------|--------|------|
| 원소 참조 방식 | Index (정수) | Position (포인터/iterator) |
| 내부 구현 | 배열(Array) | 이중 연결 리스트(Doubly linked list) |
| 삽입 시간복잡도 | O(n) | O(1) (위치를 이미 알고 있는 경우) |
| 삭제 시간복잡도 | O(n) | O(1) (위치를 이미 알고 있는 경우) |
| 공간복잡도 | O(N) (N = 할당 용량) | O(n) (n = 실제 원소 수) |

- Vector의 삽입/삭제가 O(n)인 이유: 인덱스 i 이후의 원소를 모두 한 칸씩 shift해야 하기 때문
- List의 삽입/삭제가 O(1)인 이유: 포인터 연결만 변경하면 되기 때문

### Sequence ADT의 통합 연산

Sequence는 Vector와 List의 특성을 결합한 ADT로, 인덱스↔위치 변환을 제공한다.

- `atIndex(i)`: begin()에서 `i`번 `++curr`를 반복하여 해당 position 반환 → O(i) 시간
- `indexOf(p)`: begin()에서 `p`에 도달할 때까지 카운트 → O(n) 시간

```cpp
// atIndex: O(i)
Iterator atIndex(int i) {
  Iterator curr = begin();
  for (int j = 0; j < i; j++) { ++curr; }
  return curr;
}

// indexOf: O(n) 최악
int indexOf(Iterator p) {
  int count = 0;
  Iterator curr = begin();
  while (p != curr) { ++curr; ++count; }
  return count;
}
```

## Counterevidence

- List의 삽입·삭제가 O(1)이라도, **해당 위치를 먼저 탐색**해야 한다면 O(n) 탐색이 선행되어 실질적인 이점이 사라질 수 있다.
- Vector는 임의 접근(random access)이 O(1)이므로, 읽기 위주 또는 인덱스 기반 접근이 잦은 상황에서는 Vector가 더 유리하다.
- Vector의 공간복잡도 O(N)은 Growable Vector(동적 배열)에서 실제 원소 수(n)보다 더 많은 메모리를 점유할 수 있다. 단, 이는 resize 빈도를 줄이기 위한 의도된 trade-off다.
- List는 각 노드마다 `prev`, `next` 포인터와 `pos_in_seq`, `pos_in_parent` iterator를 별도로 저장하므로, 노드당 메모리 오버헤드가 크다.

## Conclusion

삽입·삭제 연산이 빈번하고 해당 위치(iterator)를 이미 알고 있는 상황(예: 벨트 컨베이어 시뮬레이션, 커서 기반 편집)에서는 **List**가 적합하다. 인덱스 기반 임의 접근이 잦고 순서 변경이 드문 상황에서는 **Vector**가 적합하다. Sequence ADT는 두 방식을 통합하지만, `atIndex()`와 `indexOf()`의 O(n) 비용을 감수해야 하므로 변환이 자주 필요한 설계는 지양해야 한다.

## Sources

- raw/자료구조/CSE2112_02_week06_1.pdf (pp.9–13)
