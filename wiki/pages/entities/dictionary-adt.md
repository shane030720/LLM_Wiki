---
title: Dictionary ADT
category: entity
tags: [dictionary, data-structure, associative-storage, adt]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Dictionary(딕셔너리) ADT는 identifier(식별자)와 associated information(연관 정보)를 저장하고 검색하는 일반적인 연관 저장 구조다. key-value 쌍의 모음으로, 기본 ADT 명세에서 식별자 간에 특정 순서(order)를 요구하지 않는다.

## Capabilities

- **Insert**: (identifier, associated information) 쌍 삽입
- **Delete**: 특정 identifier에 해당하는 항목 삭제
- **Lookup / Search**: identifier로 연관 정보 검색 및 반환
- 해시 테이블, 이진 탐색 트리(BST), 균형 BST(AVL, Red-Black) 등 다양한 방식으로 구현 가능
- 심볼 테이블, 캐시, 데이터베이스 인덱스 등 다양한 응용에 활용

## Limitations

- 기본 ADT 명세에서 식별자 간의 순서가 정의되지 않아 범위 쿼리(range query)는 기본 지원 아님
- 구현 방식에 따라 성능 특성이 크게 달라짐 (해시 테이블 평균 O(1) vs BST O(log n))
- 동일 identifier를 가진 여러 항목의 처리 방식이 ADT 수준에서 명세되지 않음

## Relationships

- [[abstract-data-type]] (Dictionary는 ADT로 정의됨)
- [[union-find]] (원소-집합 식별자 연관 저장 측면에서 개념적으로 연관)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (p.11)
