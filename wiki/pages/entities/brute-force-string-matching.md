---
title: Brute-Force String Matching
category: entity
tags: [algorithm, string, pattern-matching, brute-force]
sources: [raw/알고리즘/CH11 스트링 매칭.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview
Brute-Force Pattern Matching(완전 탐색 패턴 매칭)은 패턴 P를 텍스트 T의 모든 가능한 이동(shift) 위치에 대해 순차적으로 비교하는 가장 단순한 문자열 매칭 알고리즘이다. 일치가 확인되거나 모든 위치를 소진할 때까지 반복 수행한다. 전처리 과정이 없으며 구현이 단순하다.

## Capabilities
- 전처리 없이 즉시 실행 가능하며, 추가 자료구조가 불필요하다.
- 모든 알파벳 Σ에 대해 동작하며 범용성이 높다.
- 알고리즘:
  ```
  for i ← 0 to n − m        { 가능한 모든 shift 시도 }
    j ← 0
    while j < m and T[i + j] = P[j]
      j ← j + 1
    if j = m
      return i               { i 위치에서 일치 }
  return -1                  { 일치 없음 }
  ```
- 짧은 텍스트나 단발성 탐색에서 오버헤드 없이 사용 가능하다.

## Limitations
- 시간복잡도 O(nm): n은 텍스트 길이, m은 패턴 길이
- 최악의 경우: T = "aaa...ah", P = "aaah" 처럼 반복 문자열로 구성된 텍스트에서 발생하며, 이미지 데이터나 DNA 서열에서 현실적으로 나타날 수 있다.
- 불일치 발생 후에도 이전 비교 결과를 전혀 활용하지 않아 중복 비교가 발생한다.
- 영문 텍스트처럼 다양한 문자가 섞인 경우에는 실용적 성능이 나쁘지 않으나, 알파벳이 작은 데이터에서 취약하다.

## Relationships
- [[string-matching]] (이 알고리즘이 해결하는 기본 문제 정의)
- [[knuth-morris-pratt-algorithm]] (중복 비교를 failure function으로 제거하여 O(m+n)으로 개선한 알고리즘)
- [[boyer-moore-algorithm]] (두 가지 휴리스틱으로 실용적 성능을 크게 향상시킨 알고리즘)

## Sources
- raw/알고리즘/CH11 스트링 매칭.pdf
