---
title: DFD Elements (DFD 구성 요소)
category: concept
tags: [dfd, process, data-flow, data-store, external-entity]
sources: [raw/시스템분석/ch05-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

DFD Elements는 Data Flow Diagram을 구성하는 네 가지 기본 요소로, Process, Data Flow, Data Store, External Entity로 이루어진다. 각 요소는 비즈니스 프로세스에서 데이터의 변환, 이동, 저장, 그리고 외부와의 상호작용을 각각 담당하며, 이들의 조합으로 완전한 DFD가 구성된다.

## How It Works

### 1. Process (프로세스)

특정 비즈니스 목적을 위해 수행되는 활동 또는 기능이다. 수동(manual) 또는 자동화(computerized) 방식 모두 가능하다.

필수 구성:
- 번호 (Number) — 계층 내 위치를 나타냄
- 이름 (동사구, verb phrase) — 수행하는 행동을 기술
- 설명 (Description)
- 최소 하나의 입력 데이터 흐름
- 최소 하나의 출력 데이터 흐름

Logical Process Model에서 포함 대상: 계산, 의사결정, 정렬/필터/요약, 보고서 생성, 다른 프로세스 트리거, 저장 데이터 CRUD

### 2. Data Flow (데이터 흐름)

단일 데이터 또는 논리적으로 묶인 데이터의 집합으로, 항상 Process에서 시작하거나 끝난다. "움직이는 데이터(data in motion)"에 해당한다.

필수 구성:
- 이름 (명사, noun) — 구현 방식이 아닌 데이터 내용을 기술
- 설명 (Description)
- 하나 이상의 Process와의 연결

표현 방식:
- **Data Flow**: 실선(solid line) + 화살표 — 프로세스의 입출력 또는 Data Store의 생성/삭제/업데이트
- **Control Flow**: 점선(dashed line) + 화살표 — 데이터를 담지 않고 프로세스를 트리거하는 흐름 (예: "주간 급여 처리 시각")

### 3. Data Store (데이터 저장소)

나중에 사용하기 위해 어떤 형태로든 저장되는 데이터의 컬렉션이다. Data Flow가 "움직이는 데이터"라면, Data Store는 "정지한 데이터(data at rest)"에 해당한다.

필수 구성:
- 번호 (Number)
- 이름 (명사, noun) — 비즈니스가 저장하고자 하는 "사물(things)"을 기술
- 설명 (Description)
- 프로세스 모델 전체에서 하나 이상의 입력 데이터 흐름 (업데이트 또는 신규 데이터 추가)
- 프로세스 모델 전체에서 하나 이상의 출력 데이터 흐름 (데이터 검색)

### 4. External Entity (외부 엔티티)

시스템 외부에 존재하는 사람, 조직, 또는 시스템으로, 시스템에 데이터를 제공하거나 시스템으로부터 데이터를 수신한다. 시스템의 경계(boundary)를 정의하는 역할을 한다.

필수 구성:
- 이름 (명사, noun)
- 설명 (Description)

## Key Properties

- 네 가지 요소가 반드시 결합되어야 완전한 DFD 구성 가능
- **Syntax 규칙**: 모든 Data Flow는 반드시 하나 이상의 Process와 연결되어야 하며, Data Store ↔ Data Store 또는 External Entity ↔ External Entity 간의 직접 연결은 불가
- **Syntax 규칙**: 모든 Process는 최소 하나의 입력과 하나의 출력을 가져야 함
- Data Flow 이름은 내용(what) 기술에 집중하며, 구현 방식(how)은 명시하지 않음
- External Entity는 시스템 범위 밖에 위치하므로 내부 구현을 표현하지 않음

## Relationships

- [[data-flow-diagram]] — 네 가지 요소가 조합되어 구성하는 다이어그램 기법
- [[process-model]] — DFD Elements가 속하는 상위 모델링 프레임워크

## Open Questions

- Data Store의 물리적 구현(파일, 관계형 테이블, NoSQL 컬렉션 등)은 Logical DFD에서 명시하지 않으나, Physical DFD 전환 시 어떤 기준으로 매핑할지 가이드라인이 필요하다.
- Control Flow와 Data Flow의 구분이 모호한 경우(예: 이벤트 트리거가 데이터 페이로드를 포함할 때) 처리 기준에 대한 추가 논의가 필요하다.

## Sources

- raw/시스템분석/ch05-1.pdf (Dennis, Wixom, Roth — Systems Analysis and Design, 2019, Ch.5)
