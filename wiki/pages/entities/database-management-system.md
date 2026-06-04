```markdown
---
title: Database Management System (DBMS)
category: entity
tags: [dbms, database, storage-manager, query-processor, transaction]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

DBMS(Database Management System)는 데이터베이스를 저장·관리하고 접근을 용이하게 하는 소프트웨어다. 전통적으로는 Oracle이 대표적이었으나, 현재는 Spark, Hadoop HBase, Google BigTable, Hive, Cassandra 등 다양한 시스템을 포함한다. DB 엔진은 크게 **Storage Manager**와 **Query Processor** 두 가지 주요 컴포넌트로 구성된다.

## Capabilities

**Storage Manager**: 데이터베이스와 운영체제 사이의 인터페이스
- OS 파일 시스템과의 상호작용
- 효율적인 데이터 저장·수정 (인덱싱, 해싱)
- 담당 이슈: storage access, file organization, indexing and hashing

**Transaction Manager**: Storage Manager의 핵심 서브컴포넌트
- 장애 발생 시 데이터베이스의 일관성(consistency) 보장
- 원자성(atomicity) 보장
- 예) 은행 계좌 이체는 전부 완료되거나 전혀 실행되지 않아야 함
- Transaction = 단일 작업을 위한 일련의 연산들

**Query Processor**: SQL 질의를 실제 실행으로 변환하는 3단계 파이프라인
- Parsing and translation: SQL → 내부 표현으로 변환
- Optimization: 가장 효율적인 실행 계획 선택
- Evaluation: 최적화된 계획 실행
- 좋은 실행 계획과 나쁜 실행 계획의 비용 차이는 극도로 클 수 있음

## Limitations

- 파일 시스템 대비 설정·운영 복잡도가 높음
- 단순 순차적 데이터 처리에는 파일 시스템이 더 가볍고 효율적일 수 있음
- 초대용량(빅데이터) 분산 처리에는 전통적 RDBMS만으로 한계 존재 → Hadoop, Spark 등 별도 시스템 필요

## Relationships

- [[database]] (DBMS가 관리하는 대상)
- [[relational-model]] (관계형 DBMS가 구현하는 데이터 모델)
- [[sql]] (DBMS가 파싱·최적화·실행하는 질의 언어)
- [[transaction-management]] (DBMS 내 원자성·일관성 보장 메커니즘)
- [[query-processing]] (DBMS 내 질의 처리 파이프라인)
- [[postgresql]] (오픈소스 관계형 DBMS의 대표 사례)

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
