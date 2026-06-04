---
title: External Merge Sort
category: concept
tags: [database, sorting, algorithm, external-memory, i-o-complexity]
sources: [raw/데이터베이스/Query Processing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

External merge sort는 메모리에 전체를 올릴 수 없는 대용량 릴레이션을 디스크 상에서 정렬하기 위한 알고리즘이다. sorted run을 생성하는 1단계와 이를 K-way merge로 병합하는 2단계로 구성되며, 총 I/O 비용은 O((N/B) log_{M/B}(N/B))로 in-memory O(n log n)에 대응하는 외부 메모리 최적 복잡도를 달성한다.

## How It Works

### Phase 1: Sorted Run 생성

1. 릴레이션에서 M/B 블록씩 메모리에 읽어들인다
2. 메모리 내에서 정렬 (quicksort 등 임의 in-memory 정렬 사용)
3. 정렬된 데이터를 run R_i로 디스크에 기록하고 i를 증가
4. 릴레이션 전체를 소진할 때까지 반복

- 생성되는 run 수: O(N/M)
- 각 run의 블록 수: O(M/B)
- Phase 1 I/O Cost: O(N/B) — linear

### Phase 2: K-way Merge

K = 현재 run 수 = O(N/M)

**K < M/B인 경우 (단일 패스 병합):**
1. 각 run에 1 블록의 input buffer 할당, 1 블록을 output buffer로 사용
2. 모든 input buffer의 첫 번째 레코드 중 정렬 순서상 가장 앞선 것을 output buffer에 기록
3. 해당 레코드를 input buffer에서 삭제; buffer가 비면 해당 run의 다음 블록을 로드
4. 모든 input buffer가 빌 때까지 반복

**K >= M/B인 경우 (다중 패스 병합):**
- 한 pass에서 M/B - 1개의 run씩 묶어 병합
- 각 pass마다 run 수가 M/B - 1 배 감소, run 길이는 동일 배수 증가
- 예: M/B = 11이면 한 pass에서 90개 run → 9개 run으로 축소 (각 10배 크기)
- run 수가 1이 될 때까지 pass 반복

### Cost Analysis

각 pass는 모든 블록을 한 번씩 읽고 쓰므로 O(N/B)의 linear I/O가 발생한다.

| 단계 | I/O Cost |
|------|---------|
| Run 생성 (Phase 1) | O(N/B) |
| 병합 각 pass | O(N/B) |
| 총 pass 수 | O(log_{M/B}(N/M)) |
| **전체 I/O** | **O((N/B) log_{M/B}(N/B))** |

총 비용이 O((N/B) log_{M/B}(N/B))인 이유: 각 병합 pass는 run 수를 M/B - 1 배로 줄이므로, 초기 run 수 O(N/M)을 1로 줄이는 데 필요한 pass 수가 O(log_{M/B}(N/M))이다.

## Key Properties

- M >= N이면 in-memory sort (e.g., quicksort)를 사용하므로 external merge sort 불필요
- M/B (메모리의 블록 수)가 클수록 pass 수 감소 → 전체 I/O 절약
- 각 pass의 I/O는 항상 linear이므로 병렬화 및 pipeline 적용에 유리
- Run 생성 단계에서 partial aggregate 계산을 겸하면 aggregation 연산과 결합 최적화 가능
- Merge-join의 전처리 정렬 단계로 직접 활용됨

## Relationships

- [[query-processing]] (sorting은 query processing의 핵심 서브루틴이며 비용 모델 기반 동일)
- [[hash-join]] (recursive partitioning의 pass 수 분석 구조가 external merge sort의 pass 수 분석과 동일)
- [[join-algorithm-comparison]] (merge-join은 이 알고리즘을 전처리로 사용하며 이미 정렬된 경우 비용 생략 가능)

## Open Questions

- Replacement selection 기법 적용 시 평균 run 크기가 2M/B로 늘어나 run 수가 절반으로 줄어드는데, 최악의 경우(역순 입력)와의 trade-off를 어떻게 평가하는가?
- SSD처럼 sequential/random I/O 비용 차이가 작은 환경에서도 external merge sort의 sequential I/O 우위가 유지되는가?
- Double buffering 기법으로 I/O와 CPU를 overlap하면 실질적 wall-clock time은 얼마나 줄어드는가?

## Sources

- raw/데이터베이스/Query Processing.pdf
