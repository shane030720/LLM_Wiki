---
title: Structured Systems Development
category: concept
tags: [sdlc, waterfall, v-model, parallel, methodology, structured]
sources: [raw/시스템분석/ch02-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Structured Systems Development은 SDLC 기반의 전통적 개발 방법론 범주로, 한 단계(phase)가 완료된 후에야 다음 단계로 이동한다는 원칙에 기반한다. 각 단계를 철저히 수행함으로써 정확하고 높은 품질의 결과를 보장하는 것이 목표이며, Waterfall Development, Parallel Development, V-Model의 세 가지 접근법이 포함된다.

## How It Works

### Waterfall Development
단계에서 단계로 순차적으로 이동하며, 한 단계의 산출물(deliverables)이 다음 단계의 입력으로 흘러들어 가는 구조다.

- 강점: 시스템 요구사항이 구현 시작 전에 명확히 정의됨; 요구사항이 "동결(frozen)"되어 이동하는 목표물이 없음
- 약점: 시스템의 가시적 증거가 나타나기까지 오랜 시간 소요; 시작부터 종료까지 전체 기간이 길다

### Parallel Development
프로젝트를 동시에 작업 가능한 subproject들로 분할하여 전체 프로젝트 기간을 단축하는 방식이다.

- 강점: 전체 프로젝트 시간 단축(Waterfall 대비); 짧은 기간으로 요구사항 변경 가능성 감소
- 약점: subproject 분할 시 신중한 설계 결정 필요; 최종 subproject 통합이 복잡하고 어려울 수 있음

### V-Model
개발 단계와 대응하는 테스트 계획 단계를 V자 형태로 매핑하여 시스템 품질을 강조하는 방식이다. QA(Quality Assurance) 전문성을 프로젝트 초기에 투입한다.

- 강점: 단순하고 명확; 테스트 강조를 통한 품질 향상; 초기 QA 전문성 투입으로 시스템 품질 강화
- 약점: 경직성(rigid); 동적 비즈니스 환경에서 적용 어려움

## Key Properties
- 요구사항이 프로젝트 초반에 확정되어야 효과적이다.
- 단계 완료 후 다음 단계로 이동하는 순차적 구조를 가진다.
- 불명확한 요구사항이나 낯선 기술 환경에서는 Poor한 적합도를 보인다.
- 복잡한 시스템 및 신뢰성이 중요한 시스템에 적합하다(특히 V-Model).
- 짧은 기간 요구 프로젝트에는 Parallel을 제외하고 Poor한 적합도를 가진다.

## Relationships
- [[sdlc-methodology-selection]] (구조적 방법론 선택 기준 및 타 방법론과의 비교표)
- [[rapid-application-development]] (구조적 방법론의 느린 가시성 문제를 보완하기 위한 RAD)
- [[project-estimation-and-planning]] (단계별 산업 표준 비율은 Waterfall 단계 구성과 연관)

## Open Questions
- Parallel Development에서 subproject의 최적 분할 기준은 무엇인가?
- V-Model에서 QA 전문가가 어느 단계부터 참여하는 것이 이상적인가?
- 현대 환경에서 Waterfall이 효과적으로 적용 가능한 도메인은 무엇인가(예: 규제 산업, 임베디드 시스템)?

## Sources
- raw/시스템분석/ch02-1.pdf (pp. 10–16)
