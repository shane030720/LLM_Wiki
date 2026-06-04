---
title: FastMCP
category: entity
tags: [mcp, framework, python, tool-server, agent]
sources: [raw/시스템 분석 실습/8. Model Context Protocol.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Overview

FastMCP는 [[mcp]](Model Context Protocol) 서버를 Python으로 빠르게 구축할 수 있도록 설계된 프레임워크다. 개발자가 함수 단위의 tool 핸들러를 정의하면 FastMCP가 MCP 명세에 맞는 HTTP 엔드포인트(`/mcp`, `tools/list`, `tools/call` 등)를 자동으로 노출한다. Anthropic 생태계 내에서 [[mcp]] 서버 개발의 사실상 표준 구현체로 사용된다.

## Capabilities

- **Tool 등록 간소화**: Python 데코레이터(`@mcp.tool`) 방식으로 tool을 선언하면 입력 스키마 생성과 라우팅을 자동 처리한다.
- **`tools/list` 자동 생성**: 등록된 모든 tool의 name, description, input schema를 MCP 명세 형식으로 반환한다.
- **`tools/call` 핸들링**: AI 에이전트가 tool을 호출할 때 인자 파싱 및 핸들러 디스패치를 담당한다.
- **로컬 서버 실행**: `127.0.0.1:8000`과 같은 로컬 주소에서 HTTP MCP 서버를 실행할 수 있다.
- **SQLite 등 백엔드 연동**: tool 핸들러 내부에서 임의의 저장소(SQLite, 파일 시스템 등)와 자유롭게 연동 가능하다.
- **실습 예시 도구**: `memo.create`, `memo.get`, `memo.list`, `memo.update`, `memo.append` 같은 CRUD tool 구현에 활용된다.

## Limitations

- MCP 서버 단위로 도구 집합이 정의되므로, tool 수가 많아지면 [[context-explosion]] 문제가 발생할 수 있다.
- HTTP 기반 로컬 서버 위주로 설계되어 있어, 분산 환경이나 인증이 요구되는 프로덕션 배포 시 추가 설정이 필요하다.
- Python 생태계에 한정된 서버 구현체이므로, 다른 런타임(Node.js, Go 등)에서는 별도 MCP SDK가 필요하다.

## Relationships

- [[mcp]] — FastMCP는 MCP 서버 사양을 구현하는 프레임워크이며, MCP 프로토콜 위에서 동작한다.
- [[context-explosion]] — FastMCP로 구축한 서버에 tool이 많이 등록될수록 이 문제가 심화된다.
- [[orchestrator]] — FastMCP 서버는 [[orchestrator]] 패턴에서 worker 에이전트가 호출하는 tool 공급자 역할을 한다.
- [[claude-code]] — Claude Code 등 MCP 호환 에이전트가 FastMCP 서버와 직접 연동하여 tool을 사용할 수 있다.

## Sources

- raw/시스템 분석 실습/8. Model Context Protocol.pdf
