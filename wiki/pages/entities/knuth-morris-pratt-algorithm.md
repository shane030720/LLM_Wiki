---
title: Knuth-Morris-Pratt Algorithm
category: entity
tags: [algorithm, string, pattern-matching, kmp, failure-function]
sources: [raw/알고리즘/CH11 스트링 매칭.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview
Knuth-Morris-Pratt(KMP) 알고리즘은 Donald Knuth, Vaughan Pratt, James Morris가 고안한 문자열 매칭 알고리즘이다. 패턴을 텍스트에 대해 왼쪽에서 오른쪽으로 비교하되, 불일치 발생 시 failure function을 이용해 이미 일치한 정보를 재활용함으로써 불필요한 비교를 건너뛴다. 전체 시간복잡도 O(m+n)의 이론적 최적성을 보장한다.

## Capabilities
- **Failure Function F(j)**: P[0..j]의 prefix 중 P[1..j]의 suffix이기도 한 가장 긴 것의 길이로 정의된다.
  - 예: P = "abaaba" → F = [0, 0, 1, 1, 2, 3]
  - 불일치 발생 시 j ← F[j-1]로 설정하여 패턴을 지능적으로 이동한다.
- Failure function 전처리: O(m) 시간, O(m) 공간
- 매칭 알고리즘: O(n) 시간 (while 루프 최대 2n회 반복 — i 증가 또는 shift 증가가 항상 보장)
- 전체 시간복잡도: **O(m + n)** (이론적 최적)
- 알고리즘:
  ```
  F ← failureFunction(P)
  i ← 0, j ← 0
  while i < n
    if T[i] = P[j]
      if j = m − 1: return i − j    { match }
      i ← i + 1; j ← j + 1
    else if j > 0
      j ← F[j − 1]                  { failure function 적용 }
    else
      i ← i + 1
  return −1
  ```
- Failure function 계산도 KMP 알고리즘과 동일한 구조로 O(m) 내에 처리한다.

## Limitations
- Failure function 저장을 위한 O(m) 추가 공간이 필요하다.
- 실용적인 영문 텍스트에서는 Boyer-Moore보다 느린 경우가 많다 (character-jump 같은 큰 점프 기회 활용 불가).
- 역방향 비교(오른쪽에서 왼쪽)를 활용하지 않아 일부 상황에서 비효율이 존재한다.

## Relationships
- [[string-matching]] (이 알고리즘이 해결하는 문제)
- [[brute-force-string-matching]] (KMP가 개선하는 기반 알고리즘 — 중복 비교 제거)
- [[boyer-moore-algorithm]] (동일 문제를 휴리스틱 기반으로 해결하는 대안 — 실용 성능 비교 대상)
- [[string-matching-algorithm-comparison]] (세 알고리즘의 성능 트레이드오프 분석)

## Sources
- raw/알고리즘/CH11 스트링 매칭.pdf
