```markdown
---
title: Database Technology Evolution
category: synthesis
tags: [database, history, big-data, ai, nosql, relational-model]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Thesis

데이터베이스 기술은 데이터 규모와 활용 패턴의 변화에 따라 순차적으로 진화해왔으며, 관계형 모델이 핵심 기반으로 유지되면서도 빅데이터·AI 시대를 맞아 새로운 패러다임으로 확장되고 있다.

## Evidence

- **1960년대 이전**: 자기 테이프(magnetic tape)를 이용한 순차 접근 데이터 처리; 직접 접근(random access) 불가
- **1960~70년대**: 하드 디스크 등장으로 직접 접근 가능; hierarchical model, network model 등 다양한 데이터 모델 사용; 고수준 질의 언어 부재 — 단순 질의에도 상당한 코딩 노력 필요
- **1970년**: Ted Codd가 [[relational-model]] 제안; IBM의 System R 프로토타입과 UC Berkeley의 Ingres 프로토타입([[postgresql]]의 전신)으로 이어짐; Turing Award 수상
- **1980년대**: 관계형 DB 상용화; SQL 산업 표준화; 병렬·분산·객체지향 DB 등장
- **1990년대**: 대규모 의사결정 지원 및 데이터 마이닝; 멀티 테라바이트 데이터 웨어하우스; 웹 커머스 등장; MySQL, PostgreSQL 등 오픈소스 RDBMS 확산
- **2000년대 초**: XML/XQuery 표준; 인터넷 붐으로 데이터 폭증
- **2000년대 후반 (빅데이터 시대)**: Google BigTable, Yahoo Pnuts, MapReduce, Hadoop 등 거대 분산 스토리지 시스템 등장; 단일 컴퓨터의 처리 한계 → 분산 컴퓨팅 부상
- **2010년대 이후 (AI 시대)**: ML 시스템에서 데이터 관리의 중요성 재부각; 고품질·대용량 학습 데이터 필요; Generative AI 등장으로 임베딩(embeddings) 저장·검색을 위한 Vector DB 필요성 증가
- **현재 및 미래 (Learned Knowledge 시대)**: AI 모델이 지식을 학습; knowledge base로의 진화 가능성 논의 중

## Counterevidence

- 관계형 DB는 빅데이터 시대에 한계를 노출했음에도 불구하고 DB-Engines 랭킹에서 여전히 상위를 지배 → NoSQL이 RDBMS를 완전히 대체하지 못함
- SQL은 NoSQL 진영에서도 SQL-like 언어(Hive, SparkSQL, BigQuery 등)로 재등장 → 비절차적 질의 언어로서의 SQL의 근본적 유용성은 유지됨

## Conclusion

데이터베이스 기술은 파일 시스템 → 관계형 모델 → 빅데이터/NoSQL → AI/Vector DB 순으로 진화했다. 각 시대마다 새로운 패러다임이 등장했지만, 관계형 모델과 SQL은 핵심 기반으로 지속적으로 살아남고 있다. 현재는 AI 시대의 요구(대규모 임베딩 저장, 지식 관리)에 맞는 새로운 데이터 관리 방식이 요구되면서, 관계형 모델을 보완하는 방향으로 진화가 이루어지고 있다.

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
