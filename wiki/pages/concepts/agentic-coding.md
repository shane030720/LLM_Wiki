---
title: Agentic Coding
category: concept
tags: [coding-paradigm, llm, sdlc, multi-agent]
sources: [raw/시스템 분析 실습/1. Vibe coding and Agent coding.pdf, raw/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스를 수행하는 패러다임. 2025년 4분기부터 주류로 부상하며, 바이브 코딩의 한계(기술 부채 누적, 일관성 부족)를 극복하기 위한 후속 패러다임이다. 에이전트가 각 SDLC 단계별로 협력하여 대규모 프로덕트까지 다룰 수 있다.

## How It Works

1. **요청 명세** — 각 에이전트에게 역할별 PRD/SRS + 적절한 프롬프트 제공
2. **에이전트 구조 확장** — Single → Sequential → Multi-Agent 구조로 작업 규모에 따라 확장
3. **SDLC 단계 co-operation** — Planning, Analysis, Design, Implementation 각 단계에서 에이전트가 협력
4. **인간은 오케스트레이터** — 에이전트에게 작업을 분해하고 분배하며 결과를 통합

에이전트 코딩은 완전히 새로운 개념이 아님; 기존에도 PRD를 주면 작업하는 도구가 존재했으나, 지금은 SDLC 전체 단계를 구조적으로 지원하는 방향으로 진화했다.

## Key Properties

| 속성 | Vibe Coding | Agentic Coding |
|------|-------------|----------------|
| 접근 방식 | One-Shot Generation | Description per each Agents |
| 문서화 | PRD/SRS Link or Paste (or None) | Appropriate Prompt + PRD/SRS |
| 인간의 역할 | Prompt Engineering | Orchestrator |
| 에이전트 구조 | Single Conversation | Single → Sequential → Multi-Agent |
| 적합한 규모 | Small-Size Application | Up to Large-Scale Product |
| SDLC 단계 | Simple Loop | Co-operation with AI after SDLC Step |

## Limitations

- Orchestrator에 과도한 부담이 집중될 수 있음 (파이프라인이 Sub-Agent 방식을 그대로 재사용하는 경우)
- 에이전트 간 의존관계와 순서를 사전에 정확히 설계해야 함
- 단일 작업에만 활용하면 파이프라인 재사용이 어려움

## Relationships

- [[vibe-coding]] (agentic coding이 극복하려는 이전 패러다임)
- [[sdlc]] (agentic coding이 보장하려는 개발 프로세스 프레임워크)
- [[sequential-agent]] (agentic coding의 핵심 구조 중 하나)
- [[parallel-agent]] (병렬 처리를 위한 에이전트 구조)
- [[agent-pool]] (에이전트를 동적으로 관리하는 패턴)
- [[harness-engineering]] (agentic coding의 실행 환경을 구조적으로 설계하는 기술)

## Open Questions

- 어느 수준의 작업 규모부터 agentic coding이 vibe coding보다 실질적으로 더 효율적인가?
- 에이전트 팀 내에서 실패한 에이전트를 어떻게 감지하고 복구할 것인가?

## Sources

- raw/1. Vibe coding and Agent coding.pdf
- raw/2. SDLC pipeline in Vibe coding.pdf
