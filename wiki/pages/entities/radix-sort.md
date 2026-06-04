---
title: Radix Sort
category: entity
tags: [sort, algorithm, non-comparison-sort, linear-time, bucket]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Radix Sort(기수 정렬)는 키를 직접 비교하지 않고, 키의 각 자릿수(field)를 기준으로 버킷(bucket)에 분배하고 결합하는 과정을 반복하는 정렬 알고리즘이다. 핵심 통찰은 최하위 자릿수(least significant digit)부터 처리하면, 각 pass 이후 버킷 내 재정렬이 불필요하다는 점이다.

**주요 단계**:
1. `distribute(L, buckets, radix, field)`: 현재 field를 기준으로 각 원소를 `maskShift(field, radix, key)` 결과 버킷에 삽입 — θ(n)
2. `combine(buckets, radix)`: 버킷 0부터 순서대로 연결 리스트를 합쳐 새로운 리스트 반환 — θ(n)
3. field 0(최하위)부터 numFields-1(최상위)까지 반복

**데이터 구조**: 연결 리스트(linked list)를 사용하여 버킷 간 이동을 O(1)에 처리

## Capabilities

- **시간 복잡도**: field 수(numFields)가 상수일 때 θ(n) — 비교 기반 정렬의 하한 Ω(n log n)을 초월
  - 각 pass: distribute θ(n) + combine θ(n) = θ(n)
  - numFields가 상수이면 전체 θ(n)
- **공간 복잡도**: θ(n) 추가 공간 (링크 필드 포함, radix ≤ n 조건)
- 키의 구조를 활용하는 비교 외 연산(field 추출, `maskShift`)으로 하한을 돌파

## Limitations

- **키에 대한 추가 가정 필요**: 키의 구조 또는 범위를 미리 알아야 한다 — 범용 정렬로 사용 불가
  - 예: 고정 자릿수 정수, 고정 길이 문자열 등에만 적용 가능
- radix(기수)가 클수록 버킷 수가 많아져 공간 사용량이 증가한다.
- `maskShift` 연산 정의가 키 구조에 종속적이므로 구현의 범용성이 낮다.

## Relationships

- [[sorting-algorithm-comparison]]: 비교 기반 정렬의 하한을 초월하는 알고리즘으로 비교 분석; 추가 가정의 대가로 선형 시간 달성
- [[insertion-sort]], [[quick-sort]], [[mergesort]], [[heapsort]]: 모두 키 비교만을 기본 연산으로 사용하는 비교 기반 정렬 — Radix Sort와 근본적으로 다른 접근 방식

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.42–50)
