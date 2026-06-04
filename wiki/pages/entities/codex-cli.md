---
title: Codex CLI
category: entity
tags: [cli-tool, ai-agent, openai, coding-assistant]
sources: [raw/시스템 분析 실습/2. SDLC pipeline in Vibe coding.pdf, raw/3. Agents subprocess calling.pdf, raw/4. Plan_mode Sequential and Parallel agents.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## What It Is

OpenAI가 개발한 CLI 기반 AI 코딩 에이전트. 터미널에서 자연어 명령으로 코드 작성 및 파일 수정을 수행한다. GPT-4o 등 OpenAI 모델을 기반으로 하며, YOLO 모드(`--yolo`)를 통해 권한 확인 없이 자동 실행을 지원한다.

## Key Capabilities

- **파일 시스템 접근** — 프로젝트 파일 읽기/쓰기
- **코드 생성 및 수정** — 자연어 명령으로 코드 변경
- **YOLO Mode** — `--yolo` 플래그로 모든 권한 확인 생략
- **단일 프롬프트 실행** — `-p` 플래그로 비대화형 실행

## Configuration

**YOLO Mode:**
```bash
codex --yolo "모든 테스트를 실행하고 실패한 것을 수정해줘"
```

**단일 프롬프트 실행:**
```bash
codex -p "이 함수를 리팩토링해줘"
```

**Subprocess에서 호출:**
```python
cmd = ["codex", "--yolo", "-p", prompt]
result = subprocess.run(cmd, capture_output=True, text=True)
```

## Compared To

| 속성 | Codex CLI | Claude Code | Gemini CLI |
|------|-----------|-------------|------------|
| 개발사 | OpenAI | Anthropic | Google |
| YOLO Flag | `--yolo` | `--dangerously-skip-permissions` | N/A |
| Native Loop | OS Cron | CronCreate | OS Cron |
| MCP 지원 | Limited | Yes | Yes |
| Plan Mode | No | Yes (Shift+Tab) | No |

## Limitations

- Claude Code의 CronCreate 같은 Native Loop 없음 → OS cron 사용 필요
- Plan Mode 미지원 → 읽기 전용 계획 단계 없음
- MCP 지원이 Claude Code 대비 제한적

## Relationships

- [[claude-code]] (주요 경쟁/비교 대상 CLI 도구)
- [[gemini-cli]] (동일 카테고리 Google 도구)
- [[subprocess]] (Python subprocess로 Codex CLI를 파이프라인에 통합)
- [[agentic-coding]] (Codex CLI가 agentic coding에서 사용 가능한 실행 도구)
- [[loop]] (OS 스케줄러와 연계하여 반복 작업 구현)

## Sources

- raw/2. SDLC pipeline in Vibe coding.pdf
- raw/3. Agents subprocess calling.pdf
- raw/4. Plan_mode Sequential and Parallel agents.pdf
