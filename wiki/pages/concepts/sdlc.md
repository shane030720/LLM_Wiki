---
title: SDLC (Software Development Life Cycle)
category: concept
tags: [software-engineering, process, requirements]
sources: [raw/시스템 분析 실습/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

소프트웨어 개발의 전 과정을 단계별로 구조화한 프레임워크. Planning → Analysis → Design → Implementation 4단계로 구성되며, 에이전틱 코딩은 각 단계에서 AI 에이전트가 co-operate하는 방식으로 SDLC를 보장한다.

## How It Works

1. **Planning** — 무엇을 왜 만드는가 (System Request, Feasibility Analysis)
2. **Analysis** — 무엇이 필요한가 (요구사항 수집, 분석 모델)
   - 비즈니스 요구사항: 왜(Why) 만드는가
   - 사용자 요구사항: 무엇(What)을 달성하는가
   - 기능 요구사항: 어떻게(How) 동작해야 하는가
3. **Design** — 어떻게 만드는가 (아키텍처, 인터페이스, DB 설계)
4. **Implementation** — 실제로 만든다 (코딩, 테스트, 배포)

**System Request 구성요소:** Project Sponsor(누가), Business Need(왜), Business Requirements(무엇을), Business Value(가치), Special Issues/Constraints(제약)

## Key Properties

- **요구사항 명세 도출 과정** — 변수(비즈니스규칙, 품질속성, 제약사항, 외부인터페이스, 보안사항) → 요구사항(15개 분야) 도출
- **체계적 문서화 필수** — 단순 Quick Sort 시각화 도구조차 체계적 요구사항 없이는 사용자 기대를 충족하기 어려움
- **바이브 코딩에서의 적용** — Spec First, Code Later 패턴으로 SDLC를 간소화하여 적용
- **에이전틱 코딩에서의 적용** — 각 SDLC 단계별로 에이전트가 협력하며 단계 보장

## Relationships

- [[agentic-coding]] (SDLC를 에이전트로 보장하는 패러다임)
- [[vibe-coding]] (SDLC를 생략하거나 간소화하는 패러다임, Spec First로 부분 보완)
- [[spec-driven-development]] (SDLC의 Analysis 단계를 구조화하는 방법론)
- [[plan-mode]] (SDLC Planning/Analysis 단계와 대응하는 에이전트 모드)

## Open Questions

- 소규모 애플리케이션에서 SDLC 전 단계를 에이전트로 대체할 수 있는가?
- 요구사항 도출(Elicitation) 자체를 에이전트와 협업하는 최적의 방법은?

## Sources

- raw/2. SDLC pipeline in Vibe coding.pdf
