---
title: Systems Development Life Cycle (SDLC)
category: concept
tags: [sdlc, process, information-systems, methodology, lifecycle]
sources: [raw/시스템분석/ch01-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Systems Development Life Cycle(SDLC)는 정보시스템을 계획·분석·설계·구현하는 일련의 단계로 구성된 표준 개발 방법론이다. 하나의 선형 순서가 아니라 지속적으로 반복되는 순환 구조(ongoing systems planning)를 가지며, 시스템이 노후화되면 새로운 프로젝트가 다시 시작된다.

## How It Works

SDLC는 네 가지 주요 단계로 구성된다:

1. **Planning Phase (계획 단계)**
   - Project Initiation: 시스템 요청서(System Request) 작성 및 예비 타당성 분석(preliminary feasibility analysis) 수행
   - 프로젝트 계획 수립: 작업 계획(work plan)과 인력 배치 계획(staffing plan) 포함

2. **Analysis Phase (분석 단계)**
   - 기존 시스템과 문제점 연구
   - 요구사항 수집 및 분석, 신규 시스템 개념 도출
   - 분석 모델(analysis models)로 신규 시스템 기술
   - 시스템 제안서(System Proposal) 작성 → 스폰서·운영위원회의 Go/No Go 결정

3. **Design Phase (설계 단계)**
   - 설계 전략 결정: 자체 구축(Build) / 구매(Buy) / 아웃소싱(Outsource)
   - 아키텍처, 인터페이스, 데이터베이스, 프로그램 설계
   - 설계 요소를 System Specification으로 통합
   - 운영위원회의 Go/No Go 결정

4. **Implementation Phase (구현 단계)**
   - 시스템 구축: 프로그래밍 및 테스트(검증·확인)
   - 시스템 설치: 교육(training), 신규 시스템으로의 전환(conversion)
   - 지속적인 시스템 지원(ongoing support)

순환 구조: 구현 완료 후 시스템이 노후화되면 다시 Planning으로 진입하는 사이클이 반복된다.

## Key Properties

- 단계별 산출물이 명확함: System Request → System Requirements → System Specifications
- 각 단계 전환 시 운영위원회의 Go/No Go 의사결정 관문(gate) 존재
- 선형 순서처럼 보이지만 실제로는 지속적 순환(ongoing cycle) 구조
- 타당성 분석(feasibility analysis)은 프로젝트 전 기간에 걸쳐 재평가해야 함

## Relationships

- [[systems-analyst]] (SDLC의 각 단계를 주도하는 핵심 역할)
- [[feasibility-analysis]] (Planning Phase에서 수행되며, 이후 단계에서도 재평가됨)
- [[business-process-management]] (IS 프로젝트의 필요성을 발굴하는 선행 방법론)

## Open Questions

- Agile, Scrum 등 반복적(iterative) 개발 방법론과 전통적 SDLC(waterfall)의 관계 및 차이점은 어떻게 되는가?
- Go/No Go 결정 기준이 명시적이지 않은 경우 어떤 기준으로 판단하는가?
- 클라우드 환경에서 Implementation Phase의 전환(conversion) 절차는 어떻게 달라지는가?

## Sources

- raw/시스템분석/ch01-1.pdf (pp. 5–10)
