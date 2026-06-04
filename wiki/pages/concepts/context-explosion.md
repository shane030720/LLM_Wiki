---
title: Context Explosion
category: concept
tags: [mcp, tool-calling, agent, context-window, tradeoff]
sources: [raw/시스템 분석 실습/8. Model Context Protocol.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Context Explosion이란, AI 에이전트에 연결된 도구(tool)의 수가 증가할수록 각 도구의 스키마·설명이 컨텍스트 윈도우를 채워 넣어, 모델이 올바른 도구를 추론하거나 선택하는 비용이 기하급수적으로 커지는 현상이다. [[mcp]] 환경에서 수십~수백 개의 tool이 등록될 때 전형적으로 나타난다.

## How It Works

1. MCP 서버에 등록된 모든 tool의 name, description, input schema가 `tools/list` 응답으로 반환된다.
2. 에이전트는 각 요청마다 이 목록 전체를 컨텍스트에 포함시켜 어떤 도구를 호출할지 추론해야 한다.
3. 도구 수가 늘어날수록 프롬프트 토큰이 증가하고, 모델이 불필요한 도구 설명에 주의를 분산시켜 정확도가 떨어진다.
4. "맥가이버 나이프"에서 못을 뽑는 도구 하나를 찾기 위해 모든 도구의 기능을 순차 추론해야 하는 상황과 동일하다.

## Key Properties

- 도구 수에 대해 컨텍스트 토큰 비용이 **선형 이상**으로 증가한다.
- 단순한 토큰 낭비가 아니라 **추론 품질 저하**를 수반한다 — 관련 없는 도구 설명이 노이즈로 작용한다.
- [[mcp]] 자체의 구조적 문제라기보다 **도구 설계 밀도(granularity)**와 **도구 선택 전략**의 문제다.
- 완화 방법: 도구를 카테고리별 MCP 서버로 분산, [[orchestrator]] 패턴으로 전문 서브에이전트에 위임, tool description 최소화.

## Relationships

- [[mcp]] — Context Explosion은 MCP의 대표적인 tradeoff로, 도구 통합의 편의성과 맞교환된다.
- [[orchestrator]] — 전문 서브에이전트로 도구 집합을 분리하면 각 에이전트의 컨텍스트 부하를 줄일 수 있다.
- [[agent-pool]] — 역할별 에이전트 풀을 구성하면 개별 에이전트가 보는 도구 수를 제한할 수 있다.
- [[system-prompt]] — 도구 목록은 시스템 프롬프트 또는 메시지 컨텍스트에 삽입되므로, 컨텍스트 윈도우 관리 전략과 직결된다.

## Open Questions

- 도구 수가 몇 개를 넘어야 실질적 성능 저하가 발생하는가? (모델·도구 복잡도에 따라 다를 것으로 추정)
- RAG 기반 dynamic tool retrieval(사용 가능한 도구 중 관련 도구만 선택적으로 컨텍스트에 주입)이 표준 해법이 될 수 있는가?
- [[mcp]] 표준 자체에서 도구 필터링이나 카테고리화를 공식 지원할 계획이 있는가?

## Sources

- raw/시스템 분석 실습/8. Model Context Protocol.pdf
