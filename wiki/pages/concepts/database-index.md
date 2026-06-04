---
title: Database Index
category: concept
tags: [index, database, search-key, data-structure, query-optimization]
sources: [raw/데이터베이스/Indexing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

데이터베이스 인덱스는 원하는 레코드를 효율적으로 찾기 위해 설계된 보조 데이터 구조다. `(search-key, pointer)` 형태의 인덱스 엔트리들의 집합으로 구성되며, 원본 파일보다 훨씬 작은 크기를 유지하여 전체 파일을 순차 스캔하지 않고도 빠른 레코드 접근을 가능하게 한다.

## How It Works

**Search Key**: 파일에서 레코드를 조회하는 데 사용되는 하나 이상의 속성. 반드시 Primary Key일 필요는 없다.

쿼리 실행 시:
1. 인덱스 파일에서 해당 검색 키를 탐색
2. 인덱스 엔트리의 포인터를 통해 실제 레코드에 직접 접근

**두 가지 기본 인덱스 유형**:
- **Ordered Index**: 검색 키가 정렬된 순서로 저장됨. 등치(equality) 및 범위(range) 쿼리에 효율적.
- **Hash Index**: 해시 함수를 사용해 검색 키를 버킷에 균등 분배.

**복합 검색 키(Composite Search Key)**: 두 개 이상의 속성으로 구성된 검색 키. 사전식 순서(lexicographic ordering) 사용:
- `(dept_name, salary)` 인덱스는 `dept_name = X AND salary = Y` 또는 `dept_name = X AND salary < Y` 쿼리에 효율적
- `dept_name < X AND salary = Y` 쿼리에는 비효율적 — 첫 번째 조건만 만족하는 다수 레코드를 fetch함

## Key Properties

- 인덱스 파일 크기는 원본 파일보다 훨씬 작음
- 성능 평가 지표:
  - **Access time**: 원하는 레코드 접근 소요 시간
  - **Insertion time**: 새 레코드 삽입 시 인덱스 갱신 비용
  - **Deletion time**: 레코드 삭제 시 인덱스 갱신 비용
  - **Space overhead**: 인덱스 구조가 차지하는 추가 공간
- 파일이 수정될 때마다 해당 파일의 모든 인덱스를 갱신해야 함
- 블록 fetch 비용: 약 5~10ms (메모리 접근 ~100ns 대비 약 10만 배)

## Relationships

- [[ordered-index]] — 정렬 기반 인덱스의 구체적 유형 (Dense/Sparse, Primary/Secondary, Multilevel)
- [[b-plus-tree]] — Ordered Index의 가장 널리 사용되는 자기 균형 트리 구현체
- [[b-tree]] — B+-Tree의 변형으로, 비리프 노드에도 레코드 포인터를 저장하는 구조

## Open Questions

- 데이터 타입, 쿼리 패턴(등치·범위·복합 조건), 갱신 빈도에 따라 최적 인덱스 유형이 달라지므로 인덱스 선택은 데이터 엔지니어의 핵심 설계 역량에 해당한다.
- 복합 검색 키의 속성 순서는 지원 가능한 쿼리 패턴을 직접 결정하므로, 실제 쿼리 분포에 따른 키 순서 설계가 중요하다.

## Sources

- raw/데이터베이스/Indexing.pdf
