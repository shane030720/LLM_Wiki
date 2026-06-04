---
title: System Request
category: concept
tags: [sdlc, requirements, project-management, systems-analysis, project-initiation]
sources: [raw/시스템 분석 이론/ch01-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

System Request는 SDLC(Systems Development Life Cycle)의 Planning Phase 중 Project Initiation 단계에서 Project Sponsor가 작성하는 공식 문서로, 새 정보 시스템 개발의 비즈니스 근거와 기대 가치를 정의한다. 이 문서는 steering committee(운영 위원회)의 승인 여부 결정을 위한 표준화된 정보 제출 수단이다.

## How It Works

Project Sponsor가 비즈니스 필요성(Business Need)을 인식하면 System Request를 작성하여 조직의 steering committee에 제출한다. 이 문서는 세 가지 역할을 수행한다:

1. **공식화 강제**: 스폰서가 막연한 아이디어를 구체적으로 문서화하도록 유도
2. **정보 수집 프레임워크**: 초기 프로젝트 정보를 일관된 형식으로 정리
3. **심의 표준화**: steering committee가 여러 프로젝트 요청을 동일한 기준으로 비교·평가할 수 있도록 정보 구조 통일

System Request 제출 후, 조직은 이를 바탕으로 Feasibility Analysis를 수행하여 프로젝트 추진 여부를 결정한다.

## Key Properties

System Request의 5가지 필수 구성 요소:

- **Project Sponsor**: 프로젝트를 주도하는 책임자. 전반적인 비즈니스 요구사항을 명시하고 비즈니스 가치를 결정하며, 프로젝트의 driving force 역할을 한다.
- **Business Need**: 프로젝트가 해결해야 할 비즈니스 문제 또는 기회. 비즈니스 이니셔티브 지원, 인수합병, 고통 지점(point of pain) 해결, 신기술 활용, BPM 결과 등이 원인이 될 수 있다.
- **Business Requirements**: 새 시스템이 반드시 충족해야 할 기능적 요구사항의 초기 목록
- **Business Value**: 프로젝트 완료 시 기대되는 유형(tangible) 및 무형(intangible) 가치
- **Special Issues or Constraints**: 예산, 일정, 기술 호환성 등 프로젝트 수행에 영향을 미치는 특수 조건 및 제약

## Relationships

- [[sdlc]] — Planning Phase의 Project Initiation 단계에서 System Request가 작성되고 제출된다
- [[feasibility-analysis]] — System Request 제출 후 수행되는 후속 분석으로, System Request의 내용을 근거로 기술적·경제적·조직적 타당성을 검토한다
- [[systems-analyst]] — System Request를 검토하고 분석 전략 수립에 활용하는 주요 역할자
- [[requirement-engineering]] — System Request의 Business Requirements 항목은 이후 상세 요구사항 수집 활동의 출발점이 된다
- [[business-process-management]] — BPM을 통해 식별된 Business Process Automation/Improvement/Reengineering 필요성이 System Request의 Business Need로 이어진다
- [[project-estimation-and-planning]] — System Request 승인 후 작성되는 Project Plan(work plan, staffing plan)과 연계된다

## Open Questions

- 조직마다 System Request의 형식이 상이할 수 있는데, 산업 표준 템플릿이 존재하는가, 아니면 조직 내부 표준만 존재하는가?
- 소규모 또는 긴급 프로젝트에서도 항상 공식적인 System Request가 요구되는가?
- Agile이나 RAD 방법론처럼 반복적·점진적 접근 방식에서는 System Request가 어떤 형태로 대체되거나 간소화되는가?
- Project Sponsor가 존재하지 않거나 불명확할 경우 프로젝트 승인 프로세스는 어떻게 진행되는가?

## Sources

- raw/시스템 분석 이론/ch01-1.pdf
