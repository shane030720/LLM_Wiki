---
title: Orchestrator
category: concept
tags: [agent, orchestrator, agentic-coding, subprocess, pool]
sources: [raw/시스템 분석 실습/6. Agent pool and Orchestrator.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Orchestrator는 에이전틱 시스템에서 에이전트 풀(Agent Pool)의 정의 파일을 읽고, 현재 목표에 적합한 에이전트를 동적으로 선택하여 독립적인 subprocess로 실행하는 제어 주체(control agent)이다. 고정된 파이프라인과 달리 Orchestrator는 런타임에 어떤 에이전트를 어떤 순서로 실행할지 결정한다.

## How It Works

1. **풀 정의 로딩**: `pool/*.json` 디렉토리에 저장된 에이전트 정의 파일(id, role, system_prompt, input/output 스펙, tools, constraints 등)을 읽는다.
2. **목표 분석**: 주어진 Task 또는 사용자 요청을 분석하여 필요한 에이전트 조합을 결정한다.
3. **컨텍스트 파일 생성**: 에이전트 행동을 제한하기 위한 컨텍스트 파일(`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`)을 프로젝트 루트에 생성·배치한다.
4. **subprocess 실행**: 선택된 에이전트를 독립적인 subprocess로 실행한다. 각 에이전트 결과는 반드시 격리된 subprocess를 통해 생성된다.
5. **결과 수집 및 라우팅**: 에이전트 출력을 수집하고, 필요 시 다음 에이전트의 입력으로 전달(route)한다.

```
Orchestrator
 ├── reads: pool/plan-agent.json
 ├── reads: pool/review-agent.json
 ├── creates: CLAUDE.md (constraints)
 └── spawns subprocess → Plan Agent
                     → Review Agent (with plan output as input)
```

## Key Properties

- **동적 선택(Dynamic Selection)**: 풀에 등록된 에이전트 중 목표에 맞는 것을 런타임에 선택한다. 파이프라인 순서가 코드에 하드코딩되어 있지 않다.
- **독립성 보장**: 각 에이전트는 반드시 독립 subprocess로 실행되어 컨텍스트 오염을 방지한다.
- **제약 위임(Constraint Delegation)**: Orchestrator 자신이 에이전트 행동을 직접 제어하는 것이 아니라 컨텍스트 파일(`CLAUDE.md`, `AGENTS.md`)을 통해 에이전트에게 규칙을 전달한다.
- **확장성**: 새 에이전트를 `pool/` 디렉토리에 JSON으로 추가하면 Orchestrator가 자동으로 인식하고 활용 가능하다.
- **부담 분산**: 기존 Sub-Agent 방식에서 Main Orchestrator에 과도하게 집중되던 처리 부담을 분산시킨다.

## Relationships

- [[agent-pool]] — Orchestrator가 읽고 관리하는 에이전트 정의 집합
- [[agent-specification]] — `pool/*.json` 파일의 에이전트 정의 스키마
- [[subprocess]] — Orchestrator가 에이전트를 실행할 때 사용하는 격리 실행 메커니즘
- [[agent-state-machine]] — Orchestrator가 추적하는 각 에이전트의 런타임 상태
- [[planner-reviewer-pipeline]] — Orchestrator 없이 고정 순서로 동작하는 대비적 패턴. Orchestrator가 해결하려는 한계의 원형
- [[pipeline-design-patterns]] — Orchestrator가 동적으로 대체·확장하는 정적 파이프라인 패턴들
- [[agent-session-control]] — 세션 단위 에이전트 제어와 Orchestrator의 관계

## Open Questions

- Orchestrator 자체가 실패했을 때 복구(recovery) 전략은 무엇인가?
- 여러 Orchestrator가 동일한 Agent Pool을 공유할 때 동시성 충돌을 어떻게 처리하는가?
- Orchestrator의 에이전트 선택 로직을 LLM 추론에 맡길 때와 규칙 기반으로 처리할 때의 트레이드오프는?
- `pool/*.json`의 `constraints.sandbox` 권한 수준을 Orchestrator가 동적으로 조정할 수 있는가?

## Sources

- raw/시스템 분석 실습/6. Agent pool and Orchestrator.pdf
