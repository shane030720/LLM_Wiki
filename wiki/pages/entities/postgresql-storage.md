---
title: PostgreSQL Physical Storage
category: entity
tags: [postgresql, storage, page, heap, tuple]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview
PostgreSQL은 테이블 데이터를 파일 시스템 상의 파일로 저장하며, 각 파일은 8KB 단위의 page(block)로 분할된다. 테이블마다 별도의 파일이 생성되고, 1GB 초과 시 여러 파일로 분할된다. 데이터 디렉토리는 `SHOW data_directory;`, 테이블의 파일 경로는 `pg_relation_filepath('table_name')`으로 확인할 수 있다. 데이터베이스별 OID는 `pg_database` 시스템 카탈로그에서 조회한다.

## Capabilities

**파일 레이아웃**
- 각 테이블은 1GB 단위 파일로 분할 저장 (예: 1.5GB 테이블 → 파일 2개, 총 196,608 pages)
- 각 파일은 8KB page들로 구성
- Page가 PostgreSQL의 read/write 단위: row를 읽거나 쓸 때 해당 row가 속한 page 전체를 처리

**Page 구조**
- Page header (24 bytes): 체크섬 등 메타데이터 포함
- Row offsets(line pointers): N번째 포인터가 N번째 row를 가리키며, page 내 임의 row에 빠른 접근 가능
- Rows(heap tuples): 실제 레코드 데이터, page의 끝에서부터 채워짐
- 각 row는 단일 page 내에 저장 (너무 큰 row는 TOAST 메커니즘으로 별도 처리)

**Heap Tuple 읽기 방식**
- Sequential scan: 모든 page의 모든 line pointer를 순서대로 스캔
- B-tree index scan: index tuple에 저장된 TID(block 번호, offset 번호)를 이용해 해당 heap tuple 직접 접근. 예: TID = `(block=7, offset=2)`이면 7번째 page의 2번째 tuple을 불필요한 스캔 없이 바로 읽음

## Limitations
- 단일 row는 기본적으로 하나의 8KB page를 초과할 수 없음 (초과 시 TOAST 메커니즘 사용)
- 1GB를 넘는 테이블은 여러 파일로 분할되어 관리됨
- Page 내 row 수정 시 해당 page 전체를 새로 write (partial write 불가)

## Relationships
- [[record-structure]] (PostgreSQL의 heap page는 slotted page 구조를 구체적으로 구현한 사례)
- [[buffer-manager]] (PostgreSQL의 shared buffer pool이 page 캐싱 및 교체를 담당)
- [[file-organization]] (PostgreSQL 기본 테이블은 heap organization 방식으로 레코드를 저장)

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
