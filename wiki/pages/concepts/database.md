```markdown
---
title: Database
category: concept
tags: [database, data-management, storage, persistence]
sources: [raw/데이터베이스/Intro to databases.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Database는 대규모의 구조화된 데이터(large collection of structured data)의 집합이다. 단순한 파일 시스템과 달리 데이터를 장기적으로 외부 메모리(SSD, 클라우드 스토리지 등)에 영속적으로 저장하며, 파일 시스템이 해결하지 못하는 데이터 중복·무결성·동시성·보안 문제를 체계적으로 해결하기 위해 등장했다. 데이터 구조(Data Structures)가 즉각적인 계산을 위해 RAM 내 알고리즘 효율을 최적화한다면, 데이터베이스는 장기 영속 저장과 다양한 접근 패턴에 최적화된다.

## How It Works

데이터베이스는 세 가지 추상화 계층(abstraction levels)을 통해 동작한다.

- **Physical level**: 레코드가 실제 디스크에 어떻게 저장되는지 기술
- **Logical level**: 데이터베이스에 저장된 데이터와 데이터 간 관계를 기술 (데이터 타입, 구조 정의)
- **View level**: 응용 프로그램에서 데이터 타입 세부사항을 숨기고, 보안상 일부 정보(예: 직원 급여)를 감출 수 있음

Schema와 Instance의 구분:

- **Schema**: 데이터베이스의 논리적 구조 정의 — 프로그래밍 언어의 type 선언에 해당
  - Physical schema: 물리적 수준에서의 설계
  - Logical schema: 논리적 수준에서의 설계
- **Instance**: 특정 시점의 데이터베이스 실제 내용 — 변수의 현재 값에 해당
- **Physical Data Independence**: 물리적 스키마를 변경해도 논리적 스키마에 영향을 주지 않는 능력; 각 레이어 간 인터페이스가 명확히 정의되어야 유지됨

## Key Properties

- 대용량 데이터를 외부 메모리에 영속 저장
- 데이터 중복(redundancy) 및 불일치(inconsistency) 방지
- 고수준 질의 언어(SQL)를 통한 데이터 접근 — 새 작업마다 프로그램을 새로 작성할 필요 없음
- 무결성 제약조건(integrity constraints)의 명시적 선언 및 시스템 수준 강제
- 원자적 업데이트(atomicity) 보장 — 트랜잭션 단위 처리
- 다중 사용자 동시 접근(concurrent access) 지원 및 일관성 유지
- 접근 제어를 통한 보안 관리

## Relationships

- [[relational-model]] (데이터베이스에서 가장 널리 사용되는 데이터 모델)
- [[database-management-system]] (데이터베이스를 저장·관리·접근하는 소프트웨어)
- [[sql]] (데이터베이스를 기술하고 조작하는 표준 질의 언어)
- [[entity-relationship-model]] (데이터베이스 스키마 설계 시 사용하는 개념적 모델)
- [[transaction-management]] (원자성과 일관성을 보장하는 데이터베이스 메커니즘)
- [[query-processing]] (SQL 질의를 실행 결과로 변환하는 내부 처리 과정)

## Open Questions

- 파일 시스템과 데이터베이스의 경계는 현대 클라우드·오브젝트 스토리지 환경에서도 여전히 유효한가?
- Vector DB 등 AI 시대의 새로운 데이터베이스 유형이 기존 관계형 모델을 보완하는 수준에 그칠 것인가, 아니면 대체할 것인가?

## Sources

- raw/데이터베이스/Intro to databases.pdf
```
