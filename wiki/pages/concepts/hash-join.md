---
title: Hash Join
category: concept
tags: [database, join, algorithm, hashing, equi-join, partition]
sources: [raw/데이터베이스/Query Processing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Hash join은 equi-join과 natural join에 적용 가능한 join 알고리즘으로, hash function을 이용해 두 릴레이션을 동일한 partition으로 분류한 후 같은 partition 내에서만 join을 수행한다. 재귀 partitioning이 필요 없는 일반적인 경우 I/O Cost는 O(N/B)로, 대용량 비정렬 릴레이션에 대한 join 알고리즘 중 가장 효율적인 부류에 속한다.

## How It Works

### 개요

Hash function h를 사용해 join attribute 값을 {0, 1, ..., H} 구간에 매핑한다.
- r의 각 튜플 t_r → partition r_i, 여기서 i = h(t_r[JoinAttrs])
- s의 각 튜플 t_s → partition s_i, 여기서 i = h(t_s[JoinAttrs])

Join 조건을 만족하는 두 튜플은 반드시 동일한 hash 값을 가지므로 r_i는 오직 s_i와만 비교하면 된다. s는 **build input**, r은 **probe input**이라 한다.

### 알고리즘 단계

**1단계 — Partitioning:**
1. hash function h로 s를 H개의 partition으로 분할하여 디스크에 기록 (각 partition에 output buffer 1블록 할당)
2. 동일한 방식으로 r을 H개의 partition으로 분할

**2단계 — Build and Probe (각 i에 대해):**
1. (Build) s_i를 메모리에 로드하고 별도의 hash function으로 in-memory hash index 구성
2. (Probe) r_i의 튜플을 디스크에서 하나씩 읽어 in-memory hash index로 매칭 튜플 탐색
3. 매칭된 (t_r, t_s) 쌍을 결과에 출력

### Partition 수 H 결정

각 s_i가 메모리에 들어갈 수 있도록 H를 설정한다.
- H = Θ(N_s / M) 으로 선택
- probe 릴레이션의 partition r_i는 메모리에 맞지 않아도 됨

### Recursive Partitioning

H > M/B인 경우 (s가 매우 크거나 메모리가 작을 때):
- M/B - 1개의 partition만 생성한 후 각 partition을 다른 hash function으로 재귀적으로 분할
- 필요 passes: O(log_{M/B}(N_s / B)) — [[external-merge-sort]]의 merge pass 수와 구조 동일
- 실제로 거의 발생하지 않음: 블록 크기 4KB, 메모리 2MB 기준으로 1GB 미만 릴레이션에서 불필요

### Overflow 처리

Partition skew (일부 partition에 튜플 집중) 또는 불량 hash function으로 인해 s_i가 메모리를 초과할 때:
- **Overflow resolution**: 해당 partition s_i를 다른 hash function으로 재분할하고 r_i도 동일하게 분할
- **Overflow avoidance**: build 단계 전에 partition을 더 잘게 나눈 후 결합
- **Fallback**: overflow된 partition에 block nested-loop join 적용
- 대량 중복값이 있는 경우 두 방법 모두 실패 가능

### Cost

| 조건 | I/O Cost |
|------|---------|
| 재귀 partitioning 불필요 | O(N_r/B + N_s/B) ≈ O(N/B) |
| 재귀 partitioning 필요 | O((N_r/B + N_s/B) * log_{M/B}(N_s/B)) |
| build input이 메모리에 완전히 적재 가능 | O(N_r/B + N_s/B) ≈ O(N/B) |

재귀 partitioning이 불필요한 일반 경우의 실질 비용: partitioning에서 각 릴레이션을 읽고 쓰는 2회 linear I/O + build/probe에서 각 릴레이션을 읽는 1회 linear I/O = 총 3회 linear I/O.

**예시**: instructor (100블록) ⋈ teaches (400블록), 메모리 20블록  
→ 5개 partition, partitioning 1 pass, build/probe 1 pass  
→ 총 3 × (100 + 400) = 1,500 block transfers

## Key Properties

- Equi-join과 natural join에만 적용 가능; inequality join (A > B)은 지원 불가
- Build input으로 항상 더 작은 릴레이션을 선택 (s_i가 메모리에 들어가야 하므로)
- 사전 정렬이 불필요하여 merge-join 대비 일반적인 상황에서 유리
- Partition skew가 성능에 치명적; 심각한 중복값 존재 시 overflow로 인해 degradation 발생
- 두 phase(partitioning + build/probe)에 걸쳐 각 튜플이 디스크에서 2회 읽힘(partitioning 후 다시 읽음)

## Relationships

- [[join-algorithm-comparison]] (nested-loop join, merge-join 등 다른 알고리즘과의 비용 및 조건 비교)
- [[external-merge-sort]] (recursive partitioning의 pass 수 분석이 external merge sort의 merge pass 수 분석과 구조적으로 동일)
- [[query-processing]] (query processing에서 join 연산의 대표적 구현체; 비용 모델 기반 동일)

## Open Questions

- Partition skew를 partitioning 단계에서 사전에 감지하거나 완화하는 효율적인 방법은?
- Hash join과 sort-merge join의 실제 성능 우열을 결정하는 임계 조건(메모리 크기, 정렬 여부)은?
- Parallel hash join에서 data skew가 load balancing에 미치는 영향과 대응 방안은?

## Sources

- raw/데이터베이스/Query Processing.pdf
