---
title: 정렬 알고리즘 비교 분석
category: synthesis
tags: [sort, algorithm, comparison, analysis, complexity]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Thesis

비교 기반 정렬 알고리즘들은 Ω(n log n)의 공통 하한을 가지지만, worst-case 보장 여부, 공간 효율, 구현 복잡도, 키에 대한 전제 조건에서 뚜렷한 차이를 보인다. 키의 구조에 대한 추가 가정을 허용하면 이 하한을 초월한 선형 시간 정렬도 가능하다.

## Evidence

- **[[insertion-sort]]**: worst/average case 모두 θ(n²). 인접 원소만 교환하는 알고리즘 중 최적(Theorem 4.1)이나, 전체 알고리즘 중 최선이 아님. In-place, 구현 단순.
- **[[quick-sort]]**: average O(n log n), worst O(n²). 랜덤 pivot으로 평균 성능을 기대하며, in-place 구현 가능. Combine 단계가 trivial하여 실용적 상수 인자가 작음.
- **[[mergesort]]**: guaranteed worst case θ(n log n). 균등 분할(n/2)로 항상 안정적인 복잡도를 보장하나, O(n) 추가 메모리 필요. 안정 정렬 구현 용이.
- **[[heapsort]]**: worst case 2n log n + O(n) (일반), n log n + θ(n log log n) (Accelerated). In-place이며 worst case 보장. Accelerated 버전은 `fixHeapFast` + `bubbleUpHeap`으로 약 2배 속도 향상.
- **[[radix-sort]]**: field 수가 상수일 때 θ(n) — 선형 시간 달성. 단, 키의 구조/범위에 대한 추가 가정 필수. 비교 기반 Ω(n log n) 하한을 초월.
- **정렬의 응용 가치**: 비정렬 데이터 탐색은 θ(n), 정렬 데이터 탐색은 θ(log n)이 최적이므로, 반복 탐색이 예상되면 정렬 비용은 충분히 회수된다.

## Counterevidence

- [[radix-sort]]처럼 키에 대한 추가 가정을 허용하면 비교 기반 Ω(n log n) 하한을 초월할 수 있다 — 하한은 "비교만 사용"이라는 조건 하의 하한이지 절대적 하한이 아니다.
- [[quick-sort]]는 worst case가 O(n²)이지만, 실제 구현에서 Combine이 trivial하고 캐시 효율이 좋아 평균적으로 [[mergesort]]나 [[heapsort]]보다 빠른 경우가 많다.
- Accelerated Heapsort는 일반 Heapsort 대비 비교 횟수를 약 절반으로 줄이지만(`fixHeap` 2h → `fixHeapFast` h + log h), 구현 복잡도가 크게 증가하여 실용적 이점이 상쇄될 수 있다.
- [[insertion-sort]]는 O(n²)이지만, 거의 정렬된 입력에서는 inversion이 적어 실제로 빠를 수 있다.

## Conclusion

| 알고리즘 | Worst case | Average | In-place | 추가 조건 |
|---|---|---|---|---|
| Insertion Sort | θ(n²) | ~n²/4 | 예 | 없음 |
| Quick-Sort | O(n²) | O(n log n) | 예 | 없음 |
| Mergesort | θ(n log n) | θ(n log n) | 아니오 | 없음 |
| Heapsort | 2n log n + O(n) | — | 예 | 없음 |
| Accelerated Heapsort | n log n + θ(n log log n) | — | 예 | 없음 |
| Radix Sort | θ(n) | θ(n) | 아니오 | 키 구조 필요 |

단일 "최선"의 정렬 알고리즘은 존재하지 않는다. 선택 기준:
- 소규모·거의 정렬된 데이터: [[insertion-sort]]
- 평균 성능 중시 + in-place: [[quick-sort]]
- Worst case 보장 + 안정 정렬: [[mergesort]] (추가 메모리 허용 시)
- Worst case 보장 + in-place: [[heapsort]]
- 키 구조가 알려진 특수 상황: [[radix-sort]] (선형 시간 달성)

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.1–50)
