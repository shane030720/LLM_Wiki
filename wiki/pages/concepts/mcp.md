---
title: MCP (Model Context Protocol)
category: concept
tags: [protocol, integration, tool-use, standardization]
sources: [raw/시스템 분析 실습/8. Model Context Protocol.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

AI 에이전트가 외부 시스템과 균일한 방식으로 연결할 수 있도록 Anthropic이 만든 개방형 표준 프로토콜. OpenAI와 Google도 채택하였으며, "AI의 USB 인터페이스"로 비유된다. 도구마다 다른 연결 방법을 학습할 필요 없이 하나의 표준으로 모든 외부 시스템에 접근 가능.

## How It Works

**USB 인터페이스 비유:**
```
기존: 각 도구마다 별도 연결 방법
  Agent → [Custom API] → GitHub
  Agent → [Custom SDK] → Slack
  Agent → [Custom DB connector] → PostgreSQL

MCP: 하나의 표준 프로토콜
  Agent → [MCP] → GitHub Server
  Agent → [MCP] → Slack Server
  Agent → [MCP] → PostgreSQL Server
```

**MCP 4계층 구조:**

```
Host (Claude Desktop, Claude Code)
  └── Client (MCP 클라이언트)
        └── Server (MCP 서버)
              └── External System (GitHub, Slack, DB...)
```

**MCP가 제공하는 것:**
- **Tools** — 에이전트가 호출할 수 있는 함수 (예: `create_issue`, `send_message`)
- **Resources** — 에이전트가 읽을 수 있는 데이터 소스
- **Prompts** — 서버가 제공하는 프롬프트 템플릿

**OOP 관점의 MCP:**
- **캡슐화** — 외부 시스템의 구현 세부사항을 MCP 서버 내부에 은닉
- **추상화** — 에이전트는 "create_issue"만 호출하면 됨 (GitHub API 세부 사항 불필요)
- **인터페이스** — MCP 표준이 에이전트-도구 간 계약 역할

**Subagent 구조와 MCP:**
```
[Orchestrator]
  → MCP Tool: spawn_subagent("researcher", task)
  → MCP Tool: spawn_subagent("implementer", task)
  → MCP Tool: collect_results()
```

**Claude Code에서 MCP 설정 예시:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "..."}
    }
  }
}
```

## Key Properties

- **표준화** — 모든 AI 에이전트가 동일한 방식으로 외부 시스템 접근
- **생태계 확장** — 누구나 MCP 서버를 구현하여 새 도구 추가 가능
- **보안 격리** — MCP 서버가 외부 시스템 접근을 제어하여 에이전트의 직접 접근 차단

## Limitations / Tradeoffs

**Context Explosion 문제:**
- MCP 서버에 도구가 많을수록 에이전트 컨텍스트가 도구 설명으로 채워짐
- 도구가 너무 많으면 에이전트가 적합한 도구 선택에 실패
- 해결책: 필요한 MCP 서버만 활성화, 도구 설명을 간결하게 유지

## Relationships

- [[harness-engineering]] (MCP가 Harness의 Journal 컴포넌트를 외부 시스템과 연결)
- [[skill]] (Skill에서 외부 도구 접근 시 MCP를 통해 표준화된 방식으로 호출)
- [[agent-pool]] (Orchestrator가 MCP를 통해 하위 에이전트(subagent)를 생성·관리)
- [[agentic-coding]] (MCP로 에이전트 생태계가 외부 시스템과 통합되어 확장)
- [[hook]] (Hook이 MCP 이벤트에 반응하여 추가 동작 실행 가능)

## Open Questions

- MCP 도구 수가 증가할수록 Context Explosion을 자동으로 관리하는 방법은?
- MCP 서버 간의 도구 충돌(동일 이름의 다른 동작)을 어떻게 해결하는가?

## Sources

- raw/8. Model Context Protocol.pdf
