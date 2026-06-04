#!/usr/bin/env python3
"""Wiki Agent - LLM Wiki 질문 답변 에이전트 (CLI용)

사용법: python wiki_agent.py "<질문>"
"""

from pathlib import Path as _Path
import sys as _sys
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
from llm_provider import stream as llm_stream, web_search as llm_web_search
import sys
import re
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent / "wiki"
PAGES_DIR = WIKI_DIR / "pages"

SYSTEM_PROMPT_WIKI = """너는 LLM Wiki 질문 답변 에이전트야.

답변 우선순위:
1순위: 제공된 wiki 페이지 내용을 기반으로 답변 (출처: 파일명 명시)
2순위: wiki에 없으면 웹에서 조사해서 답변 (출처: URL 명시)
3순위: 웹에서도 못 찾으면 "찾을 수 없습니다" 답변

규칙:
- 항상 어떤 출처를 사용했는지 명시
- 여러 과목에 걸친 질문도 통합해서 답변 가능
- wiki 내용과 웹 내용이 충돌하면 wiki 내용 우선
- 답변은 한국어로, 핵심 용어는 영어 유지
- 추측이나 훈련 데이터 기반 답변 금지 — 반드시 제공된 자료만 사용

답변 형식:
### 답변

[한국어 답변 내용]

**출처:**
- (wiki) pages/.../파일명.md
"""

SYSTEM_PROMPT_WEB = """너는 LLM Wiki 질문 답변 에이전트야.

wiki에서 관련 내용을 찾지 못해 웹 검색으로 답변한다.

규칙:
- 웹에서 조사한 내용을 기반으로 답변
- 출처 URL을 반드시 명시
- 답변은 한국어로, 핵심 용어는 영어 유지
- 찾을 수 없으면 "찾을 수 없습니다" 답변

답변 형식:
### 답변

[한국어 답변 내용]

**출처:**
- (web) https://...
"""

# 한국어 불용어 — 키워드 매칭에서 제외
_STOPWORDS = {
    "이란", "무엇", "인가", "하는", "이고", "이다", "이며", "이면",
    "에서", "에서는", "이란", "이란", "이란", "에서", "으로", "이란",
    "이고", "이며", "하고", "하며", "하면", "하는", "하여", "해서",
    "이란", "이면", "이고", "이다", "이며", "이면", "이고", "이란",
    "은", "는", "이", "가", "을", "를", "과", "와", "의", "로", "으로",
    "에", "에서", "까지", "부터", "도", "만", "이나", "아니",
}


def find_relevant_pages(query: str, max_pages: int = 5) -> list[tuple[Path, str]]:
    """질문 키워드로 관련 wiki 페이지를 찾는다. 파일명·태그·제목에 가중치를 부여한다."""
    if not PAGES_DIR.exists():
        return []

    all_kw = re.findall(r"\w+", query.lower())
    keywords = {kw for kw in all_kw if len(kw) >= 2 and kw not in _STOPWORDS}
    if not keywords:
        return []

    scored: list[tuple[int, Path]] = []
    for page in PAGES_DIR.rglob("*.md"):
        raw = page.read_text(encoding="utf-8", errors="replace")
        lower = raw.lower()

        # 파일명 매칭 (가중치 3)
        stem_score = sum(3 for kw in keywords if kw in page.stem.lower())

        # 태그 매칭 (가중치 2)
        tag_m = re.search(r"tags:\s*\[(.*?)\]", lower, re.DOTALL)
        tag_score = sum(2 for kw in keywords if kw in tag_m.group(1)) if tag_m else 0

        # 제목 매칭 (가중치 2)
        title_m = re.search(r"title:\s*(.+)", lower)
        title_score = sum(2 for kw in keywords if kw in title_m.group(1)) if title_m else 0

        # 본문 매칭 (가중치 1)
        body_score = sum(1 for kw in keywords if kw in lower)

        total = stem_score + tag_score + title_score + body_score
        if total > 0:
            scored.append((total, page))

    scored.sort(key=lambda x: x[0], reverse=True)
    result = []
    for _, page in scored[:max_pages]:
        result.append((page, page.read_text(encoding="utf-8", errors="replace")))
    return result


def run(question: str):
    pages = find_relevant_pages(question)

    if pages:
        page_section = "\n\n---\n\n".join(
            f"## 출처: {p.relative_to(WIKI_DIR)}\n\n{content}"
            for p, content in pages
        )
        prompt = (
            f"## 질문\n{question}\n\n"
            f"## 관련 Wiki 페이지\n{page_section}"
        )
        system = SYSTEM_PROMPT_WIKI
    else:
        print("[wiki에서 찾을 수 없음 → 웹 검색 중...]", file=sys.stderr)
        search_results = llm_web_search(question)
        prompt = (
            f"## 질문\n{question}\n\n"
            f"## 웹 검색 결과\n{search_results}"
        )
        system = SYSTEM_PROMPT_WEB

    for chunk in llm_stream(prompt, system=system):
        print(chunk, end="", flush=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python wiki_agent.py \"<질문>\"")
        print("예시:  python wiki_agent.py \"RAG와 벡터DB의 차이점은?\"")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    run(question)
