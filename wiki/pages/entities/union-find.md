---
title: Union-Find ADT (Disjoint Sets)
category: entity
tags: [union-find, disjoint-set, data-structure, algorithm]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Union-Find ADT(분리 집합 ADT)는 서로 소(disjoint)인 집합들의 모음을 관리하는 자료 구조다. Union 연산으로 두 집합을 합치고, Find 연산으로 특정 원소가 속한 집합의 식별자를 조회한다. 원소는 주로 정수이며, 각 집합은 집합 내 특정 원소인 leader(대표 원소)를 set id(집합 식별자)로 사용한다.

## Capabilities

- **create(n)**: n개의 싱글턴 분리 집합 {{1},{2},{3},…,{n}} 생성
- **find(sets, e)**: 원소 e의 현재 set id 반환
- **makeSet(sets, e)**: 아직 집합에 없는 원소 e로 이루어진 싱글턴 집합 {e}를 기존 집합 모음에 추가
- **union(sets, s, t)**: set id가 s와 t인 두 집합(s ≠ t)을 합쳐 새 집합 생성; 새 set id는 s 또는 t 중 하나 (경우에 따라 min(s, t) 사용)
- Kruskal MST 알고리즘, 네트워크 연결성 판별, 동치 클래스 분류 등에 활용

## Limitations

- 집합 분리(split) 연산을 지원하지 않음 — 한번 합쳐진 집합은 되돌릴 수 없음
- 집합에 속한 모든 원소를 순회하는 연산은 기본 ADT 명세에 포함되지 않음
- Path compression과 Union by rank/size 최적화 없이는 연산당 최악 O(log n) 이상의 비용 발생

## Relationships

- [[abstract-data-type]] (Union-Find는 ADT로 정의됨)
- [[dictionary-adt]] (원소와 set id의 연관 저장 측면에서 개념적으로 유사)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (pp.9–10)
