---
title: File Organization
category: concept
tags: [file, organization, heap, sequential, hashing]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
File organization(파일 구성)은 데이터베이스의 레코드 집합을 파일(block의 시퀀스) 내에 배치하는 방식이다. 레코드를 어떤 순서와 기준으로 block에 저장하느냐에 따라 Heap, Sequential, Hashing의 세 가지 주요 방식으로 구분된다.

## How It Works

**Heap Organization**
- 레코드를 공간이 있는 곳 어디에나 배치
- 삽입이 빠르고 단순하지만, 특정 레코드 검색을 위해 전체 파일을 스캔해야 함

**Sequential Organization**
- 레코드를 search key 값의 순서에 따라 정렬하여 저장
- 전체 파일의 순차 처리(sequential processing)에 적합
- 삭제: pointer chain 활용
- 삽입: 해당 위치에 여유 공간이 있으면 삽입, 없으면 overflow block에 삽입. 어느 경우든 pointer chain 갱신 필요
- 시간이 지나면 overflow block이 쌓여 성능이 저하되므로, 주기적인 재구성(reorganization)으로 순차 순서를 복원해야 함

**Hashing Organization**
- 레코드의 특정 attribute에 hash function 적용
- hash function의 결과값이 레코드가 저장될 block을 결정

## Key Properties
- Heap: 삽입 단순, 검색 시 전체 스캔 필요
- Sequential: 순차 처리 효율적, 삽입·삭제 시 pointer 관리 및 주기적 재구성 필요
- Hashing: 특정 key로의 point lookup 빠름, 범위 검색(range query)에는 불리
- 세 방식 모두 데이터베이스의 기본 파일 레벨 구조이며, index 구조는 이 위에 추가로 구축됨

## Relationships
- [[record-structure]] (파일을 구성하는 개별 레코드의 내부 저장 형식)
- [[buffer-manager]] (파일 접근 시 block을 memory에 적재하여 I/O를 줄임)
- [[external-memory-model]] (파일 구성 방식에 따른 I/O 복잡도 분석의 기반)
- [[postgresql-storage]] (PostgreSQL 기본 테이블은 heap organization 사용)

## Open Questions
- Sequential organization에서 overflow block이 누적될 때 성능 저하의 임계점은?
- 현대 DBMS에서 세 방식 외에 어떤 파일 구성이 주로 쓰이는가?

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
