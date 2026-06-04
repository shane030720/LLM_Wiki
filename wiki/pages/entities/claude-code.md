---
title: Claude Code
category: entity
tags: [cli-tool, ai-agent, anthropic, coding-assistant]
sources: [raw/시스템 분析 실습/1. Vibe coding and Agent coding.pdf, raw/2. SDLC pipeline in Vibe coding.pdf, raw/3. Agents subprocess calling.pdf, raw/4. Plan_mode Sequential and Parallel agents.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## What It Is

Anthropic이 개발한 CLI 기반 AI 코딩 에이전트. 터미널에서 자연어 명령으로 코드 작성, 파일 수정, 테스트 실행, 디버깅을 수행한다. Claude 모델을 기반으로 하며 강력한 파일 시스템 접근 권한과 에이전트 기능을 제공한다.

## Key Capabilities

- **파일 시스템 접근** — 프로젝트 전체 파일 읽기/쓰기/삭제
- **Bash 실행** — 셸 명령어 실행 (테스트, 빌드, 배포)
- **웹 검색** — 최신 문서 및 패키지 정보 검색
- **Plan Mode** — `Shift + Tab`으로 읽기 전용 계획 모드 진입
- **CronCreate** — 반복 작업 스케줄링 (Loop 지원)
- **MCP 연동** — MCP 서버를 통한 외부 시스템 연결
- **Hook 지원** — 생명주기 이벤트에 스크립트 연결
- **세션 관리** — `--resume <id>`로 이전 대화 재개

## Configuration

**YOLO Mode (권한 확인 생략):**
```bash
claude --dangerously-skip-permissions
```

**JSON 출력 모드:**
```bash
claude --output-format json -p "요약해줘"
```

**시스템 프롬프트 지정:**
```bash
claude --system-prompt "당신은 코드 리뷰어입니다" -p "이 코드를 검토해줘"
```

**Subprocess에서 호출:**
```python
cmd = ["claude", "--dangerously-skip-permissions", "--output-format", "json"]
result = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
```

## AGENTS.md / CLAUDE.md 통합

Claude Code는 프로젝트 루트의 `CLAUDE.md`와 `AGENTS.md` 파일을 자동으로 읽어 행동 규칙과 작업 방식을 학습한다:
- `CLAUDE.md` — 스키마, 규칙, 구조 정의
- `AGENTS.md` — 에이전트 운영 플레이북

## Compared To

| 속성 | Claude Code | Codex CLI | Gemini CLI |
|------|-------------|-----------|------------|
| 개발사 | Anthropic | OpenAI | Google |
| YOLO Flag | `--dangerously-skip-permissions` | `--yolo` | N/A |
| Native Loop | CronCreate | OS Cron | OS Cron |
| MCP 지원 | Yes | Limited | Yes |
| Plan Mode | Yes (Shift+Tab) | No | No |

## Relationships

- [[plan-mode]] (Claude Code의 내장 기능)
- [[hook]] (Claude Code의 설정으로 Hook 등록)
- [[loop]] (Claude Code의 CronCreate로 Loop 구현)
- [[mcp]] (Claude Code가 MCP 클라이언트 역할)
- [[subprocess]] (Python subprocess로 Claude Code를 프로그래매틱하게 호출)
- [[agentic-coding]] (Claude Code가 agentic coding의 주요 실행 도구)

## Sources

- raw/1. Vibe coding and Agent coding.pdf
- raw/2. SDLC pipeline in Vibe coding.pdf
- raw/3. Agents subprocess calling.pdf
- raw/4. Plan_mode Sequential and Parallel agents.pdf
