---
title: Hash Collision Handling
category: concept
tags: [hash, collision, open-addressing, separate-chaining, data-structure]
sources: [raw/자료구조/CSE2112_02_week12_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Hash collision은 서로 다른 두 개 이상의 키(key)가 동일한 해시 값(hash value)을 가져 동일한 버킷(bucket)에 매핑되는 현상이다. 비둘기 집의 원리(Pigeonhole Principle)에 의해 키의 수 n이 버킷 수 N보다 크면 충돌은 반드시 발생한다. Collision handling은 이를 해결하는 전략들의 총칭이다.

## How It Works

### Separate Chaining

테이블의 각 셀이 해당 버킷에 매핑된 항목들의 연결 리스트(linked list)를 가리키도록 한다. 충돌 시 리스트에 새 항목을 추가한다. 구현이 단순하지만 테이블 외부에 추가 메모리가 필요하다.

### Open Addressing

충돌 발생 시 테이블 내의 다른 빈 셀을 탐색(probe)하여 저장한다. 추가 메모리가 불필요하지만 부하율(load factor)이 높아지면 성능이 저하된다.

#### Linear Probing

충돌 발생 시 다음 인덱스를 순차적으로 탐색한다. 탐색 인덱스: `(hash + j) mod N`, j = 0, 1, 2, ... Clustering(군집화) 문제가 발생할 수 있다.

```cpp
string find(int key) {
  int hash = compress(key);
  for (int j = 0; j < N; ++j) {
    int idx = compress(hash + j);
    if (key == bucket[idx].key)
      return &bucket[idx];
  }
  return nullptr;
}
```

#### Quadratic Probing

충돌 발생 시 탐색 간격을 제곱수로 증가시킨다. 탐색 인덱스: `(hash + j²) mod N`. Linear probing의 primary clustering 문제를 완화한다.

```cpp
string find(int key) {
  int hash = compress(key);
  for (int j = 0; j < N; ++j) {
    int idx = compress(hash + j * j);
    if (key == bucket[idx].key)
      return &bucket[idx];
  }
  return nullptr;
}
```

#### Double Hashing

두 번째 해시 함수를 사용하여 탐색 간격을 결정한다. 탐색 인덱스: `(hash + j * hash2(key)) mod N`. 예: `hash2(k) = divisor – (k mod divisor)`. 군집화 문제를 가장 효과적으로 해결한다.

```cpp
int hash2(int hash) {
  return divisor - (hash % divisor);
}
string find(int key) {
  int idx = compress(key);
  int probe = 1;
  while (probe <= N) {
    if (key == bucket[idx].key)
      return &bucket[idx];
    idx = compress(idx + hash2(key));
    ++probe;
  }
  return nullptr;
}
```

## Key Properties

- Separate Chaining은 구현이 단순하고 부하율에 덜 민감하나, 추가 메모리가 필요하다
- Linear Probing은 캐시 효율이 좋지만 primary clustering이 발생한다
- Quadratic Probing은 primary clustering을 줄이지만 secondary clustering이 남는다
- Double Hashing은 충돌 분산이 가장 균등하나 두 번째 해시 함수 설계가 필요하다
- Open Addressing에서 모든 해시 값이 동일하면 최악의 경우 O(n) 탐색이 발생한다

## Relationships

- [[dictionary-adt]] (Hash Table 기반 Dictionary 구현에서 이 전략들을 활용)
- [[graph]] (해시 테이블이 그래프 ADT 내부 구현에 쓰이기도 함)

## Open Questions

- 각 충돌 처리 전략의 평균 탐색 시간은 부하율에 따라 어떻게 달라지는가?
- Double Hashing에서 최적의 두 번째 해시 함수를 선택하는 기준은 무엇인가?
- Separate Chaining과 Open Addressing의 실제 성능이 역전되는 부하율 임계점은?

## Sources

- raw/자료구조/CSE2112_02_week12_2.pdf
