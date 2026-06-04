---
title: Agent Specification
category: concept
tags: [agent, specification, system-prompt, context, multi-agent]
sources: [raw/시스템 분석 실습/5. Agent Specifications.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Agent Specification은 LLM 기반 에이전트를 형식적으로 정의하는 구조다. 하나의 에이전트는 **System Prompt**, **Context**, **Inputs**, **Outputs** 네 가지 요소로 완전히 명세되며, 이 구조를 통해 에이전트의 역할·경계·연결 방식이 명확해진다.

## How It Works

에이전트 명세는 두 축으로 구성된다.

**System Prompt 축**
- Role: 에이전트의 정체성과 행동 원칙을 기술 (예: "너는 소크라테스식 교수로, 모든 요청에 질문으로만 응답한다")
- Inputs and Outputs: 에이전트가 수신하는 입력 형식과 생성하는 출력 형식을 명시
- Claude CLI에서는 `--system-prompt` 플래그로 주입하며, 다른 에이전트 프레임워크에서는 마크다운 파일로 주입한다

**Context 축**
- Session ID: 실행 단위를 식별하여 여러 에이전트 실행을 추적 가능하게 함
- Project Information: 현재 프로젝트의 목표·기술 스택·제약 등 배경 정보
- Hand-Off: 이전 에이전트가 생성한 출력물(예: `Plan.md`, `TODO.md`)을 다음 에이전트에 전달하는 인터페이스

실행 흐름: `(System Prompt + Context) × Inputs → Agent → Outputs`

## Key Properties

- **재사용 가능성**: Role 정의가 System Prompt에 캡슐화되어 있어 동일 에이전트를 다른 파이프라인에서 재사용 가능
- **Hand-Off 인터페이스**: 멀티 에이전트 체인에서 출력 파일이 다음 에이전트의 Context로 전달되어 정보 연속성을 보장
- **주입 방식 추상화**: CLI 플래그 또는 마크다운 파일 등 환경에 따라 유연하게 System Prompt를 주입
- **명시적 입출력 계약**: 각 에이전트의 입력과 출력이 명세에 선언되어 파이프라인 연결 오류를 사전에 방지

## Relationships

- [[system-prompt]] (Agent Specification의 핵심 축으로, Role과 입출력 형식을 담는 컴포넌트)
- [[agent-session-control]] (Session ID를 통한 에이전트 실행 단위 제어와 연관)
- [[planner-reviewer-pipeline]] (Agent Specification을 구체적으로 적용한 두 에이전트 파이프라인 예시)
- [[multi-cli-agent-setup]] (CLI 환경에서 System Prompt를 주입하는 구체적 방법)
- [[pipeline-design-patterns]] (에이전트 명세가 파이프라인 내 노드 정의에 활용되는 맥락)
- [[agentic-coding]] (Agent Specification이 agentic coding 워크플로우의 구성 단위로 사용됨)

## Open Questions

- Session ID의 범위 및 생명주기를 어떻게 정의해야 하는가 (에이전트 단위 vs. 파이프라인 단위)?
- Hand-Off 파일이 손상되거나 누락될 때 에이전트는 어떻게 복구해야 하는가?
- System Prompt를 버전 관리할 때 Context와의 결합도를 어떻게 최소화할 수 있는가?

## Sources

- raw/시스템 분석 실습/5. Agent Specifications.pdf
