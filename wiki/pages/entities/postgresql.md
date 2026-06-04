```markdown
---
title: PostgreSQL
category: entity
tags: [postgresql, rdbms, open-source, database, sql]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

PostgreSQL은 "세계에서 가장 발전된 오픈소스 데이터베이스"를 표방하는 관계형 DBMS이다. UC Berkeley의 Ingres 프로젝트에서 발전하였으며, 해당 프로젝트의 리더 Michael Stonebraker는 Turing Award 수상자이다. 역사적으로 관계형 데이터베이스 발전의 중요한 계보에 위치하며, 현재 https://www.postgresql.org 에서 무료로 다운로드 가능하다.

## Capabilities

- SQL 표준 준수도가 MySQL보다 높음
- 복잡한 질의에 대한 성능이 MySQL보다 우수
- 공간 데이터(spatial) 질의에서는 Oracle보다 우수한 경우도 있음
- pgAdmin4 GUI 도구를 통한 데이터베이스 관리 지원
- 실행 계획(execution plan)을 그래픽으로 시각화하여 제공
- DDL/DML을 포함한 완전한 SQL 지원
- 프로그래머와 연구자들이 가장 선호하는 오픈소스 RDBMS

사용 방법 (기본 흐름):
1. PostgreSQL 설치 → pgAdmin4 실행
2. `[Create] → [Database] → mydb` 로 데이터베이스 생성
3. `mydb → [CREATE scripts]` 에서 DDL SQL 실행
4. pgAdmin4에서 SQL 질의 실행 및 시각적 execution plan 확인

## Limitations

- MySQL 대비 초기 설정 복잡도가 다소 높을 수 있음
- 단순 읽기 중심의 고속 웹 애플리케이션에서는 MySQL이 더 가벼울 수 있음

## Relationships

- [[database-management-system]] (PostgreSQL이 속하는 소프트웨어 범주)
- [[relational-model]] (PostgreSQL이 구현하는 데이터 모델)
- [[sql]] (PostgreSQL이 지원하는 질의 언어)
- [[query-processing]] (PostgreSQL의 시각적 execution plan 기능)
- [[database-evolution]] (PostgreSQL이 등장한 역사적 맥락 — Ingres 프로젝트)

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
