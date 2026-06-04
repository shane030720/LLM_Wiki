---
title: B+-Tree Index
category: entity
tags: [b-plus-tree, index, tree, data-structure, database]
sources: [raw/데이터베이스/Indexing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

B+-Tree는 데이터베이스 인덱싱을 위한 자기 균형 트리(self-balancing tree) 자료구조로, 1970년 Rudolf Bayer(1939~현재)와 E. McCreight가 발표한 논문 "Organization and Maintenance of Large Ordered Indexes"에서 소개되었다. 현재 거의 모든 관계형 데이터베이스 시스템(IBM DB2, Informix, MS SQL Server, Oracle, Sybase, SQLite, MySQL, PostgreSQL, Tibero 등) 및 파일 시스템(NTFS, EXT4, ReiserFS, XFS, JFS, ReFS, BFS 등)에서 표준 인덱스 구조로 채택되어 있다.

[[ordered-index]]의 Multilevel Index가 가진 구조적 한계(파일 성장에 따른 overflow block 생성, 주기적 전체 재구성 필요)를 자동화된 국소적 재구성(local reorganization)으로 해결한다.

## Capabilities

### 구조적 속성 (B = 노드의 최대 포인터 수)

- 루트에서 리프까지 모든 경로의 길이가 동일 (완전 균형)
- 루트도 리프도 아닌 내부 노드: ⌈B/2⌉ 이상 B 이하의 자식 수 유지
- 리프 노드: ⌈(B-1)/2⌉ 이상 B-1 이하의 검색 키 값 보유
- 루트가 리프가 아닌 경우: 최소 2개의 자식
- 트리 높이: N개의 검색 키에 대해 최대 log_{⌈B/2⌉}(N)

### 노드 구조

**리프 노드 (Leaf Node)**:
- `P1, K1, P2, K2, ..., P_{B-1}, K_{B-1}, P_B` 형태
- `Ki`: 검색 키 값 (K1 < K2 < ... < K_{B-1})
- `Pi` (i = 1..B-1): 검색 키 Ki를 가진 파일 레코드 또는 버킷에 대한 포인터
- `PB`: 다음 리프 노드를 가리키는 포인터 (리프들이 연결 리스트를 형성하여 범위 쿼리 지원)

**비리프 노드 (Non-leaf Node)**:
- Multi-level sparse index 역할
- P1이 가리키는 서브트리의 모든 키 < K1
- Pi (2 ≤ i ≤ B-1)가 가리키는 서브트리의 키: K_{i-1} ≤ key < Ki
- PB가 가리키는 서브트리의 모든 키 ≥ K_{B-1}

### 쿼리 (Lookup)

검색 키 값 V를 가진 레코드 탐색 절차:
1. C = 루트
2. C가 리프가 아닌 동안: V ≤ Ki인 최솟값 i를 찾아 해당 자식으로 이동 (없으면 마지막 비-null 포인터로 이동)
3. 리프 도달 후 Ki = V인 포인터를 통해 레코드 접근

**효율성 비교** (B = 100, N = 1,000,000):
- B+-Tree: 최대 log_50(1,000,000) = 4회 노드 접근
- 균형 이진 트리: 약 20회 노드 접근
- 노드 접근마다 디스크 I/O(약 20ms)가 발생하므로 차이가 실질적으로 큼
- 노드 크기는 일반적으로 디스크 블록 크기(약 4KB)와 동일하며, B는 약 100 (인덱스 엔트리 40바이트 기준)

### 삽입 (Insertion)

1. 삽입할 검색 키가 위치할 리프 노드 탐색
2. 리프에 공간이 있으면 `(key, pointer)` 쌍 삽입
3. 리프가 가득 찬 경우 **노드 분할 (node split)**:
   - B개의 `(key, pointer)` 쌍을 정렬 후 두 노드로 분배: 앞 ⌈B/2⌉개를 원래 노드에, 나머지를 새 노드에
   - 새 노드 p의 최솟값 키 k와 `(k, p)` 쌍을 부모 노드에 삽입
   - 부모 노드도 가득 찬 경우 비리프 노드 분할이 루트 방향으로 재귀적으로 전파
   - 최악의 경우 루트가 분할되어 트리 높이가 1 증가

### 삭제 (Deletion)

1. 리프 노드에서 해당 `(key, pointer)` 쌍 제거
2. 노드 엔트리 수가 최솟값 미만이 되면:
   - 형제 노드와 합쳐서 단일 노드에 수용 가능한 경우: **병합 (merge)** — 두 노드를 하나로 합치고 부모에서 구분 키 삭제 (재귀적으로 전파 가능)
   - 수용 불가인 경우: **재분배 (redistribute)** — 형제 노드에서 포인터를 빌려와 부모의 구분 키 갱신
3. 루트가 하나의 자식만 남으면 루트를 삭제하고 해당 자식이 새 루트가 됨

### B+-Tree File Organization

실제 데이터 파일을 B+-Tree 구조로 구성하는 방식:
- 리프 노드가 레코드 포인터 대신 실제 레코드를 직접 저장
- 리프 노드의 최솟값 채움 보장 유지
- 공간 활용 개선 전략: 분할/병합 대신 2개의 형제 노드를 재분배에 참여시켜 각 노드가 최소 ⌊2B/3⌋개의 엔트리를 보유하도록 함

## Limitations

- 삽입/삭제 시 노드 분할·병합에 따른 추가 연산 오버헤드와 공간 오버헤드 발생
- B+-Tree File Organization에서 레코드가 이동하면 해당 레코드를 가리키는 모든 Secondary Index의 포인터를 갱신해야 함 → 해결책: Secondary Index에 레코드 포인터 대신 Primary Index의 검색 키를 저장하고, 조회 시 Primary Index를 경유해 레코드에 접근 (조회 비용 증가, 단 노드 분할 비용 감소)

## Relationships

- [[ordered-index]] — B+-Tree가 해결하는 Multilevel Index의 한계 (overflow block, 주기적 재구성 필요)
- [[database-index]] — B+-Tree가 구현하는 인덱스 개념의 상위 범주
- [[b-tree]] — B+-Tree를 기반으로 비리프 노드에도 레코드 포인터를 추가한 변형 구조

## Sources

- raw/데이터베이스/Indexing.pdf
