#!/usr/bin/env python3
"""Quiz Agent - 시험 문제 출제 및 채점 에이전트

사용법:
  generate  python quiz_agent.py generate <정리노트파일> [--count N]
  grade     python quiz_agent.py grade <정리노트파일> --question "문제" --answer "내 답변"
"""

import argparse
import subprocess
import sys
from pathlib import Path

SYSTEM_PROMPT = """너는 시험 문제 출제 및 채점 전용 에이전트야.

역할 경계 (가장 중요한 규칙):
- 너는 오직 문제 출제, 채점, 오답 노트, 문제 형식 변경(서술형·객관식 등), 추가 문제 생성만 담당한다.
- 개념 설명, 원리 질문, 비교 분석, 요약 요청 등 학습 내용을 묻는 질문은 네 역할이 아니다.
- 위와 같은 위키 질문이 들어오면 반드시 이 문장으로만 답하고 절대 내용을 설명하지 마:
  "이 질문은 🧠 위키 에이전트 탭에서 해주세요. 저는 퀴즈 출제와 채점만 담당합니다."

문제 출제 규칙:
- Edit Agent가 정리한 내용 기반으로 문제 출제
- 별표(⭐) 표시된 내용에서 문제를 더 많이 출제
- 단순 암기 문제와 개념 응용 문제 모두 출제 가능
- 문제의 근거는 반드시 교육자료 안에 있어야 함
- 파일에 없는 새로운 개념으로 문제 만들지 마
- 문제와 보기는 한국어로 작성, 핵심 용어는 영어 유지

채점 규칙:
- 학생 답변을 교육자료 기준으로 채점
- 틀린 부분은 교육자료 어느 페이지를 참고해야 하는지 명시
- 오답 노트 형식으로 한국어 피드백 제공

출력 형식 규칙 (다크 테마 UI에 표시되므로 반드시 지켜야 함):
- 블록인용(>) 문법 절대 사용 금지 — 어두운 회색으로 표시되어 읽을 수 없음
- 출처·교육자료 이름은 반드시 **굵게** 표시
- 색상 지정 HTML 태그 사용 금지

문제 출제 출력 형식 (이 형식 외 추가 섹션·요약 절대 금지, 문제만 출력):
### 문제 N (⭐ 중요 / 일반)
[문제 내용]

① 보기1
② 보기2
③ 보기3
④ 보기4

**출처:** [페이지 제목] p.XX
QUIZ_ANSWER: [정답 번호와 보기 내용 전체, 예: ② 연결 지향 프로토콜]
QUIZ_EXPLAIN: [왜 이 보기가 정답인지 한 줄 해설]

---

채점 출력 형식:
### 채점 결과

- **정답:** ②
- **학생 답변:** ③ → ❌ 오답 (또는 ✅ 정답)

**오답 노트:**
- **틀린 이유:** [설명]
- **참고 자료:** [교육자료 이름] p.XX
- **핵심 내용:** [해당 개념 요약]"""


def read_notes(path: Path) -> str:
    if not path.exists():
        sys.exit(f"오류: 파일을 찾을 수 없습니다: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def generate(notes_file: str, count: int) -> str:
    notes = read_notes(Path(notes_file))
    prompt = (
        f"다음 정리 노트를 바탕으로 시험 문제 {count}개를 출제해줘. "
        f"⭐ 표시된 내용에서 더 많은 문제를 내줘.\n\n{notes}"
    )

    result = subprocess.run(
        ["claude", "--system-prompt", SYSTEM_PROMPT, "-p", prompt],
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0:
        sys.exit(f"오류: {result.stderr.strip()}")
    return result.stdout.strip()


def grade(notes_file: str, question: str, answer: str) -> str:
    notes = read_notes(Path(notes_file))
    prompt = (
        f"다음 정리 노트를 기반으로 학생 답변을 채점해줘.\n\n"
        f"## 정리 노트\n{notes}\n\n"
        f"## 문제\n{question}\n\n"
        f"## 학생 답변\n{answer}"
    )

    result = subprocess.run(
        ["claude", "--system-prompt", SYSTEM_PROMPT, "-p", prompt],
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0:
        sys.exit(f"오류: {result.stderr.strip()}")
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description="Quiz Agent - 시험 문제 출제/채점")
    sub = parser.add_subparsers(dest="mode", required=True)

    gen = sub.add_parser("generate", help="문제 출제")
    gen.add_argument("notes_file", help="정리 노트 파일 경로")
    gen.add_argument("--count", type=int, default=5, help="출제 문제 수 (기본: 5)")

    grd = sub.add_parser("grade", help="답변 채점")
    grd.add_argument("notes_file", help="정리 노트 파일 경로")
    grd.add_argument("--question", required=True, help="문제 내용")
    grd.add_argument("--answer", required=True, help="학생 답변")

    args = parser.parse_args()

    if args.mode == "generate":
        print(generate(args.notes_file, args.count))
    elif args.mode == "grade":
        print(grade(args.notes_file, args.question, args.answer))


if __name__ == "__main__":
    main()
