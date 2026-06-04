---
title: Multi-CLI Agent Setup
category: concept
tags: [agent, cli, pattern, agentic-coding, skill]
sources: [raw/시스템 분석 실습/4. Plan_mode Sequential and Parallel agents.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Multi-CLI Agent Setup은 Claude, Codex, Gemini 등 서로 다른 CLI 기반 AI 에이전트를 동시에 운용하면서 각 에이전트의 [[skill]] 레지스트리에 상대방 에이전트를 특정 역할(Implementation, Review 등)로 등록함으로써, 외부 오케스트레이터 없이 CLI 레벨에서 간단한 다중 에이전트 협업 체계를 구성하는 방식이다.

## How It Works

1. **역할 분리 등록 (Mutual Skill Registration)**
   - Claude의 Skill에 Codex를 "Implementation 담당"으로 등록한다.
   - Codex의 Skill에 Claude를 "Review 담당"으로 등록한다.
   - 이로써 각 에이전트는 자신이 수행하기 어렵거나 비효율적인 작업을 상대 에이전트에게 위임할 수 있다.

2. **Heavy User 프로파일**
   - Claude + Codex + Gemini 세 CLI를 동시에 활용하는 사용자는 통합 `Agent_CLI_Subprocess_API.md` 참조 문서를 사용하여 각 도구의 [[subprocess]] API 호출 방식을 관리한다.
   - 각 CLI 도구별 전용 cheatsheet(Claude, Codex, Gemini)와 통합 cheatsheet(Heavy User)가 병행 운용된다.

3. **작업 흐름**
   - 기획/설계 단계: [[plan-mode]]를 지원하는 에이전트가 계획 수립
   - 구현 단계: Implementation 역할 에이전트(예: Codex)가 코드 작성
   - 검토 단계: Review 역할 에이전트(예: Claude)가 코드 리뷰 및 피드백
   - 각 단계에서 [[handoff]] 파일(마크다운)을 통해 컨텍스트가 전달된다.

## Key Properties

- **오케스트레이터 불필요**: 별도의 상위 오케스트레이터 없이 CLI Skill 등록만으로 역할 분리 달성
- **저비용 구성**: 기존 CLI 도구의 Skill 기능만 활용하므로 추가 인프라 불필요
- **역할 전문화**: Implementation(코드 생성)과 Review(검토/비판) 역할을 서로 다른 모델에 할당하여 각 모델의 강점 활용
- **Subprocess 기반 통신**: 에이전트 간 호출은 [[subprocess]] API를 통해 이루어짐
- **Handoff 파일 중심**: 각 라운드 또는 에이전트 전환 시 마크다운 파일에 작업 내용을 기록하여 상태를 인계

## Relationships

- [[skill]] — 각 CLI 에이전트의 Skill 레지스트리에 상대방을 등록하는 메커니즘
- [[subprocess]] — 에이전트 간 CLI 호출을 가능하게 하는 통신 기반
- [[handoff]] — 에이전트 간 컨텍스트 전달에 사용되는 마크다운 파일 산출물
- [[sequential-agent]] — 구현 → 리뷰 → 수정의 순차 파이프라인 실행 패턴
- [[parallel-agent]] — 여러 CLI를 동시에 운용하는 병렬 구성 변형
- [[agentic-coding-patterns]] — 이 설정이 속하는 상위 패턴 분류
- [[claude-code]] — Implementation/Review 역할 중 하나를 담당하는 에이전트
- [[codex-cli]] — Implementation 역할을 담당하는 에이전트 예시
- [[gemini-cli]] — Heavy User 프로파일에 포함되는 세 번째 CLI 에이전트
- [[pipeline-design-patterns]] — 다단계 handoff 파이프라인과의 연관

## Open Questions

- Codex와 Claude 간 역할을 동적으로 전환(Implementation ↔ Review)하는 것이 가능한가, 아니면 Skill 등록 시 고정되는가?
- Heavy User 프로파일에서 세 에이전트(Claude + Codex + Gemini)의 역할을 어떻게 최적으로 분배하는가?
- Mutual Skill Registration 패턴이 순환 호출(Claude → Codex → Claude → …)로 이어질 위험이 있는가, 이를 방지하는 메커니즘이 있는가?
- 각 에이전트가 생성하는 handoff 파일의 포맷을 표준화하면 도구 간 호환성이 향상되는가?

## Sources

- raw/시스템 분석 실습/4. Plan_mode Sequential and Parallel agents.pdf
