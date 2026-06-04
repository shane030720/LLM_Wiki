---
title: Boyer-Moore Algorithm
category: entity
tags: [algorithm, string, pattern-matching, boyer-moore, heuristic]
sources: [raw/알고리즘/CH11 스트링 매칭.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview
Boyer-Moore 알고리즘은 Robert Boyer와 J Strother Moore가 고안한 문자열 매칭 알고리즘이다. 두 가지 휴리스틱(looking-glass, character-jump)을 결합하여 특히 영문 텍스트에서 brute-force보다 현저히 빠른 실용적 성능을 보인다. 최악 시간복잡도는 O(nm + s)이나, 실제 일반 텍스트에서는 매우 우수한 성능을 발휘한다.

## Capabilities
- **Looking-Glass Heuristic**: 패턴을 오른쪽에서 왼쪽 방향으로 비교한다.
- **Character-Jump Heuristic**: 불일치 문자 T[i] = c 발생 시
  - P에 c가 있으면: P 내 c의 마지막 출현 위치에 맞추어 P를 오른쪽으로 이동
  - P에 c가 없으면: P[0]을 T[i+1]에 맞추어 P를 완전히 이동
- **Last-Occurrence Function L(σ)**: 알파벳 Σ의 각 문자에 대해 P에서의 마지막 출현 인덱스를 저장 (없으면 -1)
  - 예: P = "abacab" → L(a)=4, L(b)=5, L(c)=3, L(d)=-1
  - O(m + s) 시간으로 전처리 가능 (m: 패턴 크기, s: 알파벳 크기)
- 알고리즘 (이동량 결정 로직):
  - j ≤ 1 + l 인 경우: i ← i + m − j 만큼 이동 (Case 1)
  - 1 + l < j 인 경우: i ← i + m − (1 + l) 만큼 이동 (Case 2)
  ```
  L ← lastOccurrenceFunction(P, Σ)
  i ← m − 1, j ← m − 1
  repeat
    if T[i] = P[j]
      if j = 0: return i             { match }
      else: i ← i − 1; j ← j − 1
    else                             { character-jump }
      l ← L[T[i]]
      i ← i + m − min(j, 1 + l)
      j ← m − 1
  until i > n − 1
  return −1
  ```
- 영문 텍스트 등 알파벳이 크고 패턴과 일치하지 않는 문자가 많을수록 큰 점프가 자주 발생하여 매우 빠르다.

## Limitations
- 최악 시간복잡도 O(nm + s): T = "aaa...a", P = "baaa" 같은 경우에 발생
- 이미지나 DNA 서열처럼 알파벳이 작고 반복 패턴이 많은 데이터에서 최악에 가까운 성능이 나타날 수 있다.
- KMP의 O(m+n) 이론적 최적 보장에 미치지 못한다.
- Last-occurrence function 저장을 위한 O(s) 추가 공간이 필요하다.
- 두 가지 휴리스틱을 모두 올바르게 구현해야 하므로 brute-force나 KMP보다 구현 복잡도가 높다.

## Relationships
- [[string-matching]] (이 알고리즘이 해결하는 문제)
- [[brute-force-string-matching]] (Boyer-Moore가 실용적으로 대체하는 기본 알고리즘)
- [[knuth-morris-pratt-algorithm]] (동일 문제를 O(m+n) 최적으로 해결하는 대안 — 이론적 보장 면에서 우월)
- [[string-matching-algorithm-comparison]] (세 알고리즘의 성능 트레이드오프 분석)

## Sources
- raw/알고리즘/CH11 스트링 매칭.pdf
