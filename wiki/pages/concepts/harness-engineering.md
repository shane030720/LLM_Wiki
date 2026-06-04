---
title: Harness Engineering
category: concept
tags: [agent-design, infrastructure, best-practice, context-engineering]
sources: [raw/시스템 분析 실습/7. Harness and Skills.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

프롬프트나 모델 자체를 넘어, 에이전트가 실행되는 외부 환경(도구, 데이터, 검증 파이프라인, 안전 장치)을 구조적으로 설계하는 기술. Prompt Engineering → Context Engineering → Harness Engineering으로 이어지는 AI 개발 패러다임의 세 번째 진화 단계.

## How It Works

**패러다임 진화:**

```
Prompt Engineering   → 좋은 질문 작성 기술
Context Engineering  → 좋은 컨텍스트 구성 기술
Harness Engineering  → 에이전트 실행 환경 구조 설계 기술
```

**Harness의 4가지 구성 요소:**

| 컴포넌트 | 파일/역할 | 목적 |
|----------|-----------|------|
| **Contract** | `TASK.md` | 에이전트가 달성해야 할 목표와 완료 기준 |
| **Procedure** | `Skill` (SKILL.md) | 특정 작업을 수행하는 방법 |
| **Journal** | Log / MCP | 에이전트 행동의 기록과 추적 |
| **Preference** | `PROFILE.md` / `AGENTS.md` / `CLAUDE.md` | 에이전트 행동 방식의 선호도 설정 |

**Contract (TASK.md) 구조:**

```markdown
# TASK.md
## Status: IN_PROGRESS
## Goal
사용자 요청에 따라 X를 구현한다.
## Done-when
- [ ] 단위 테스트 통과
- [ ] 코드 리뷰 완료
- [ ] 문서 업데이트
## Log
- 2026-05-26 10:00: 시작
- 2026-05-26 10:15: 1단계 완료
```

**Contract-Driven Iteration 원칙:**
- "Contract 없는 Procedure는 무한 루프"
- "Procedure 없는 Contract는 죽은 문서"
- 에이전트는 Done-when 기준을 모두 충족할 때까지 루프

**AGENTS.md Harness 템플릿 요소:**
- Session Start Checklist
- Ingest/Query/Lint 워크플로
- 역할 배분 테이블
- 긴급 복구 절차
- 로그 엔트리 템플릿

## Key Properties

- **환경 중심 설계** — 에이전트 능력보다 실행 환경의 구조가 품질을 결정
- **재현 가능성** — 동일 harness로 다른 LLM에서도 동일 결과 기대
- **인간-에이전트 인터페이스** — Contract와 Journal로 인간이 에이전트 상태를 이해하고 개입 가능
- **확장성** — Skill 추가만으로 에이전트 능력 확장 (harness 구조 변경 불필요)

## Limitations

- 초기 harness 설계에 상당한 시간과 노력 필요
- 과도하게 구조화된 harness가 에이전트의 창의적 문제 해결을 제한할 수 있음
- 소규모 작업에는 harness가 오버엔지니어링

## Relationships

- [[contract-driven-iteration]] (Harness Engineering의 Contract 컴포넌트 구현 패턴)
- [[skill]] (Harness Engineering의 Procedure 컴포넌트 구현)
- [[agentic-coding]] (harness engineering이 agentic coding의 실행 환경을 구조화)
- [[agent-pool]] (pool의 JSON 설정이 harness의 Preference 컴포넌트)
- [[mcp]] (MCP가 harness의 Journal 컴포넌트를 외부 시스템과 연결)
- [[hook]] (Hook이 harness 실행 중 특정 이벤트에 자동 반응)

## Open Questions

- Harness 품질을 자동으로 평가하는 메트릭은?
- 팀 규모에 따른 최적 harness 복잡도의 경계는?

## Sources

- raw/7. Harness and Skills.pdf
