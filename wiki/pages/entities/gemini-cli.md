---
title: Gemini CLI
category: entity
tags: [cli-tool, ai-agent, google, coding-assistant]
sources: [raw/시스템 분析 실습/2. SDLC pipeline in Vibe coding.pdf, raw/3. Agents subprocess calling.pdf, raw/4. Plan_mode Sequential and Parallel agents.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## What It Is

Google이 개발한 CLI 기반 AI 코딩 에이전트. Gemini 모델을 기반으로 하며, 터미널에서 자연어 명령으로 코드 작성, 분석, 수정을 수행한다. Google Workspace 및 Google Cloud 생태계와의 연동이 강점이다.

## Key Capabilities

- **파일 시스템 접근** — 프로젝트 파일 읽기/쓰기
- **코드 생성 및 분석** — 자연어 명령으로 코드 작업
- **MCP 지원** — MCP 서버를 통한 외부 시스템 연결
- **Google 생태계 연동** — Google Drive, Docs, Cloud와 통합 가능

## Configuration

**기본 실행:**
```bash
gemini "이 코드의 버그를 찾아줘"
```

**Subprocess에서 호출:**
```python
cmd = ["gemini", prompt]
result = subprocess.run(cmd, capture_output=True, text=True)
```

**OS Cron을 통한 Loop 구현:**
```bash
# crontab -e
0 9 * * 1-5 gemini "analyze log.md and create weekly_summary.md"
```

## Compared To

| 속성 | Gemini CLI | Claude Code | Codex CLI |
|------|-----------|-------------|-----------|
| 개발사 | Google | Anthropic | OpenAI |
| YOLO Flag | N/A | `--dangerously-skip-permissions` | `--yolo` |
| Native Loop | OS Cron | CronCreate | OS Cron |
| MCP 지원 | Yes | Yes | Limited |
| Plan Mode | No | Yes (Shift+Tab) | No |
| Google 연동 | 강점 | 제한적 | 제한적 |

## Limitations

- Claude Code의 CronCreate 같은 Native Loop 없음 → OS cron 사용 필요
- Plan Mode 미지원
- YOLO 모드에 해당하는 권한 생략 플래그 없음

## Relationships

- [[claude-code]] (주요 비교 대상 CLI 도구)
- [[codex-cli]] (동일 카테고리 OpenAI 도구)
- [[subprocess]] (Python subprocess로 Gemini CLI를 파이프라인에 통합)
- [[agentic-coding]] (Gemini CLI가 agentic coding 파이프라인에서 사용 가능한 도구)
- [[mcp]] (Gemini CLI가 MCP 클라이언트로 외부 시스템 연결)
- [[loop]] (OS 스케줄러와 연계하여 반복 작업 구현)

## Sources

- raw/2. SDLC pipeline in Vibe coding.pdf
- raw/3. Agents subprocess calling.pdf
- raw/4. Plan_mode Sequential and Parallel agents.pdf
