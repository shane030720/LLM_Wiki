---
title: Plan Mode
category: concept
tags: [agent-mode, workflow, review, implementation]
sources: [raw/시스템 분析 실습/4. Plan_mode Sequential and Parallel agents.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트가 파일 읽기와 검색만 수행하고 파일 수정을 차단하는 읽기 전용 실행 모드. 구현 전에 계획을 수립하고 사용자 승인을 받기 위한 게이트. 잘못된 구현을 되돌리는 비용을 줄이는 핵심 안전 장치다.

## How It Works

**진입 방법:**
- Claude Code에서 `Shift + Tab` 으로 Plan Mode 진입
- 프롬프트에 "plan mode로" 또는 "먼저 계획을 세워줘" 요청
- AGENTS.md에서 에이전트 역할로 지정

**Plan Mode에서 허용/차단:**

| 허용 | 차단 |
|------|------|
| 파일 읽기 | 파일 생성·수정·삭제 |
| 디렉토리 탐색 | 코드 실행 |
| 코드베이스 검색 | 외부 API 호출 |
| 계획 문서 작성 | 패키지 설치 |

**산출물 (Plan Mode Output):**

| 파일 | 내용 |
|------|------|
| `Plan.md` | 단계별 구현 계획, 작업 분해 |
| `Review.md` | 계획의 리스크·불확실성 검토 |
| `TODO.md` | 구체적 태스크 체크리스트 |

**워크플로:**

```
Plan Mode 진입
  → 코드베이스 분석 (읽기만)
  → Plan.md / Review.md / TODO.md 작성
  → 사용자에게 계획 제시
  → 사용자 승인 (yes / 수정 요청)
  → Plan Mode 종료
  → 구현 시작
```

**SDLC 대응:**
- Plan Mode ↔ Planning + Analysis 단계
- 구현 전 모든 아키텍처 결정과 작업 분해를 완료
- 승인 없이는 Implementation 단계로 진입 불가

## Key Properties

- **사용자 승인 게이트** — 계획 단계와 구현 단계 사이의 명시적 체크포인트
- **비파괴적 탐색** — 에이전트가 코드베이스를 자유롭게 탐색하되 변경 불가
- **SDLC 보장** — Analysis/Design 단계를 강제하여 성급한 구현 방지
- **Spec-First 실천** — spec-driven-development와 결합하면 Plan Mode가 PRD를 계획으로 전환하는 단계가 됨

## Limitations

- 복잡한 코드베이스에서 Plan Mode가 너무 오래 걸려 사용자 대기 시간이 늘어날 수 있음
- 계획이 구현 중 변경될 경우 Plan.md와 실제 코드 간 동기화 문제 발생
- 작은 수정 작업에는 오버헤드

## Relationships

- [[spec-driven-development]] (spec 생성 후 plan-mode로 전환하여 구현 전 검토)
- [[sdlc]] (SDLC Planning/Analysis 단계와 대응하는 에이전트 모드)
- [[vibe-coding]] (vibe coding에서 plan-first 접근으로의 전환 수단)
- [[sequential-agent]] (Plan Mode 단계가 sequential 파이프라인의 첫 번째 단계로 사용됨)
- [[harness-engineering]] (Plan.md, Review.md, TODO.md가 Contract 컴포넌트의 기반이 됨)
- [[contract-driven-iteration]] (Plan Mode 산출물이 Contract 문서의 초안이 됨)

## Open Questions

- Plan Mode의 계획 품질을 자동으로 평가하는 기준은 무엇인가?
- 팀 협업 환경에서 여러 구성원이 Plan Mode 산출물을 리뷰하는 워크플로는?

## Sources

- raw/4. Plan_mode Sequential and Parallel agents.pdf
