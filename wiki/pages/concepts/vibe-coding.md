---
title: Vibe Coding
category: concept
tags: [coding-paradigm, llm, prompt-engineering]
sources: [raw/시스템 분析 실습/1. Vibe coding and Agent coding.pdf, raw/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

자연어로 목표와 제약을 전달하면 LLM이 코드를 생성하는 개발 패러다임. 개발자는 코드 구문을 직접 작성하는 대신 청사진 설계, 프롬프트 엔지니어링, 검증 및 디버깅에 집중한다. Andrej Karpathy가 2024년 4분기에 명명했으며 2025년 3분기까지 주류 트렌드였다.

## How It Works

1. 자연어 지시 — 목표와 제약(기술 스택, 제한 사항)을 LLM에게 전달
2. 개념적 구조 전달 — 데이터 모델, API 구조, 전체 계획을 설명
3. 점진적 개선 — v1 → v1.1 → v1.2 방식의 반복적 수정
4. 분위기(vibe) 전달 — 스타일, 우선순위, 트레이드오프를 자연어로 전달

개발자의 인지 부담은 저수준 구현 세부사항에서 **창의적 문제 해결 · 사용자 경험 · 시스템 아키텍처**로 이동한다.

## Key Properties

- **Single Conversation 구조** — 단일 대화 세션에서 One-Shot 또는 반복 요청
- **문서화 방식** — PRD/SRS를 붙여넣거나 링크하거나 생략 가능
- **인간의 역할** — Prompt Engineering에 집중
- **적합한 규모** — 소규모 애플리케이션에 최적화
- **SDLC 단계** — 단순 루프(구현 → 확인 → 수정)

## Limitations

- 코드 규모가 커질수록 일관성·검증·운영에서 기술 부채가 빠르게 누적됨
- Karpathy 본인이 "AI가 만든 변경을 Accept All로 밀어붙이는 방식"이라 평가하며 한계를 지적
- 체계적인 요구사항 명세 없이는 사용자가 기대하는 결과를 내기 어려움

## Relationships

- [[agentic-coding]] (vibe coding의 한계를 극복하려는 후속 패러다임)
- [[spec-driven-development]] (vibe coding의 효과를 높이는 베스트 프랙티스: Spec First, Code Later)
- [[sdlc]] (agentic coding은 SDLC 단계별 co-operation을 강조하며 vibe coding과 대비됨)
- [[plan-mode]] (vibe coding에서 plan-first 접근으로의 전환 수단)

## Open Questions

- 바이브 코딩이 유효한 영역(프로토타이핑, 소규모 도구)과 그렇지 않은 영역의 경계는 어디인가?

## Sources

- raw/1. Vibe coding and Agent coding.pdf
- raw/2. SDLC pipeline in Vibe coding.pdf
