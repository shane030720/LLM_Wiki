---
title: SQL Data Types and Schemas
category: concept
tags: [sql, data-type, schema, index, large-object, vector, database]
sources: [raw/데이터베이스/Intermediate SQL.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

SQL은 기본 스칼라 타입(varchar, numeric 등) 외에도 기본값(DEFAULT), 인덱스(INDEX), 대용량 객체(Large Object Type), 벡터 타입(Vector Type) 등 다양한 데이터 타입과 스키마 기능을 제공한다. 이를 통해 다양한 애플리케이션 요구사항에 맞는 스키마 설계가 가능하다.

## How It Works

**DEFAULT 절**

속성에 기본값을 지정하여, 삽입 시 해당 속성을 명시하지 않으면 기본값이 자동으로 사용된다.

```sql
CREATE TABLE student (
    ID        varchar(5),
    name      varchar(20) not null,
    dept_name varchar(20),
    tot_cred  numeric(3,0) default 0,
    PRIMARY KEY (ID)
);
```

**CREATE INDEX**

테이블의 특정 속성에 인덱스를 생성하여 검색 성능을 향상시킨다. 인덱스는 논리적 스키마의 일부가 아닌 물리적 최적화 수단이다.

```sql
CREATE INDEX studentID_index ON student(ID);
```

**Large Object (LOB) 타입**

- `CLOB (Character Large Object)`: 대용량 텍스트 데이터 저장에 사용한다.
  - 예: `book_review CLOB(10KB)`
- `BLOB (Binary Large Object)`: 이미지, 동영상 등 대용량 바이너리 데이터 저장에 사용한다.
  - 예: `image BLOB(10MB)`, `movie BLOB(2GB)`

**Vector 타입**

벡터 데이터를 저장하는 타입으로, AI/ML 임베딩 벡터 저장에 활용된다.

```sql
embed vector(3)
```

## Key Properties

- DEFAULT는 [[sql-integrity-constraints]]의 `SET DEFAULT` 연쇄 작업과 연동된다.
- 인덱스는 SQL 표준에 포함되지 않는 경우가 많으며 DBMS별 문법 차이가 있다.
- CLOB/BLOB은 일반 속성처럼 처리되지 않고, 별도의 스트리밍 접근 방식을 사용하는 경우가 많다.
- Vector 타입은 현대 AI 데이터베이스(예: pgvector)에서 임베딩 기반 유사도 검색에 핵심적인 역할을 한다.

## Relationships

- [[sql-integrity-constraints]] (DEFAULT는 FOREIGN KEY의 `SET DEFAULT` 연쇄 작업과 연관된다)
- [[sql-views]] (인덱스는 뷰 쿼리의 물리적 실행 성능에 영향을 미친다)

## Open Questions

- SQL 표준에서 인덱스 생성 문법은 어떻게 정의되며, DBMS별 구현 차이는 무엇인가?
- Vector 타입을 활용한 근사 최근접 이웃 검색(ANN)은 어떤 인덱스 구조(예: HNSW, IVFFlat)로 구현되는가?
- CLOB/BLOB의 최대 크기 제한은 DBMS마다 어떻게 다른가?

## Sources

- raw/데이터베이스/Intermediate SQL.pdf (p.27)
