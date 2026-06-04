---
title: Ordered Index
category: concept
tags: [index, ordered-index, dense-index, sparse-index, primary-index, secondary-index, multilevel-index]
sources: [raw/데이터베이스/Indexing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Ordered Index는 인덱스 엔트리들이 검색 키 값의 정렬 순서로 저장되는 인덱스다. 파일의 물리적 저장 순서와의 관계에 따라 Primary Index와 Secondary Index로, 인덱스 엔트리의 밀도에 따라 Dense Index와 Sparse Index로 분류된다.

## How It Works

### Primary Index vs Secondary Index

**Primary Index (Clustering Index)**
- 순차적으로 정렬된 파일에서 파일의 순차적 순서를 지정하는 검색 키를 가진 인덱스
- Index-sequential file: Primary Index가 포함된 순차 파일
- 검색 키가 반드시 Primary Key일 필요는 없음
- 순차 스캔에 효율적

**Secondary Index (Non-clustering Index)**
- 파일의 순차적 순서와 다른 순서를 지정하는 인덱스
- 반드시 Dense Index이어야 함
- 인덱스 레코드가 해당 검색 키 값을 가진 모든 실제 레코드에 대한 포인터들을 담은 버킷(bucket)을 가리킴
- 순차 스캔 시 비효율적: 각 레코드 접근마다 새로운 디스크 블록 fetch가 발생할 수 있음

### Dense Index vs Sparse Index

**Dense Index**
- 파일의 모든 검색 키 값에 대해 인덱스 레코드가 존재
- 조회 속도 빠름, 공간 및 유지 비용 큼

**Sparse Index**
- 일부 검색 키 값에 대해서만 인덱스 레코드가 존재
- 레코드가 검색 키로 순차 정렬된 경우에만 적용 가능
- 탐색 절차: 검색 키 K에 대해 K보다 작은 최대 검색 키를 가진 인덱스 레코드를 찾은 뒤, 해당 포인터가 가리키는 위치부터 순차 탐색
- Dense Index 대비: 공간 절약, 유지 비용 감소, 조회 속도는 느림
- 최적 전략: 파일의 각 블록마다 하나의 인덱스 엔트리 (해당 블록의 최솟값 검색 키 사용)

### Multilevel Index

Primary Index가 메모리에 맞지 않을 때 계층적으로 인덱스를 구성:
- **Inner Index**: 디스크에 저장된 Primary Index 파일
- **Outer Index**: Inner Index에 대한 Sparse Index
- 필요 시 추가 레벨 생성 가능
- 문제점: 파일이 커질수록 overflow block이 생성되고 주기적인 전체 파일 재구성이 필요함 → [[b-plus-tree]]로 해결

### 인덱스 갱신 (Update)

**삭제 (Deletion)**:
- Dense Index: 파일 레코드 삭제와 동일하게 인덱스 엔트리 삭제
- Sparse Index:
  - 해당 검색 키의 인덱스 엔트리가 있으면, 다음 검색 키 값으로 교체 (다음 값에 이미 엔트리가 있으면 삭제)
  - 해당 검색 키 값을 가진 레코드가 파일에서 완전히 없어지면 인덱스에서도 삭제

**삽입 (Insertion)**:
- Dense Index: 검색 키 값이 인덱스에 없으면 삽입
- Sparse Index: 새 블록이 생성된 경우에만 인덱스 갱신 (새 블록의 첫 번째 검색 키 값 삽입)
- Multilevel: 단일 레벨 알고리즘의 재귀적 확장

## Key Properties

- Primary Index를 이용한 순차 스캔은 효율적; Secondary Index를 이용한 순차 스캔은 각 레코드마다 디스크 I/O가 발생해 비효율적
- Dense vs Sparse 트레이드오프: 조회 속도 대 공간/유지 비용
- Sparse Index 최적 전략: 블록 단위 인덱스 엔트리
- 복합 검색 키 `(a1, a2)`: `a1 = X AND a2 = Y`, `a1 = X AND a2 < Y`는 효율적이지만 `a1 < X AND a2 = Y`는 비효율적

## Relationships

- [[database-index]] — Ordered Index의 상위 개념
- [[b-plus-tree]] — Multilevel Index의 성능 저하 문제(overflow block, 주기적 재구성)를 자동으로 해결하는 자기 균형 트리
- [[b-tree]] — B+-Tree의 변형으로, 비리프 노드에도 레코드 포인터를 저장

## Open Questions

- Multilevel Index는 파일 성장에 따른 구조적 한계를 피할 수 없으며, 삽입/삭제 시 모든 레벨의 인덱스를 갱신해야 하는 부담이 있다. B+-Tree가 이를 대체하는 이유이다.
- Secondary Index 순차 스캔의 비효율을 줄이기 위한 전략(예: 포인터 정렬 후 접근, B+-Tree File Organization에서의 Primary Key 간접 참조)이 실제 시스템에서 어떻게 구현되는지는 시스템마다 다르다.

## Sources

- raw/데이터베이스/Indexing.pdf
