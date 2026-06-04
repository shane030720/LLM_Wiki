---
title: String Matching
category: concept
tags: [string, pattern-matching, algorithm, text-processing]
sources: [raw/알고리즘/CH11 스트링 매칭.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
String Matching(스트링 매칭)은 텍스트 T(크기 n)에서 패턴 P(크기 m)와 동일한 부분 문자열을 찾는 문제다. 즉, T의 특정 위치 i에서 시작하는 길이 m의 부분 문자열이 P와 일치하는 위치를 탐색한다. 일치하는 위치가 존재하면 해당 시작 인덱스를, 존재하지 않으면 -1을 반환한다.

## How It Works
- **Alphabet Σ**: 문자열을 구성하는 문자들의 집합. 예: ASCII, {0, 1}, {A, C, G, T}
- **Substring P[i..j]**: 문자열 P에서 인덱스 i부터 j까지의 부분 수열
- **Prefix**: P[0..i] 형태의 부분 문자열 (문자열의 앞부분)
- **Suffix**: P[i..m-1] 형태의 부분 문자열 (문자열의 뒷부분)
- 탐색 방식은 알고리즘에 따라 다르며, 단순 완전 탐색부터 failure function·휴리스틱 기반의 고급 기법까지 존재한다.

## Key Properties
- 텍스트와 패턴 모두 동일한 알파벳 Σ 위에서 정의된다.
- Prefix와 suffix의 중첩 관계가 KMP 등 고급 알고리즘의 핵심 아이디어로 활용된다.
- 알고리즘 성능은 최악 시간복잡도 O(nm)에서 최적 O(m+n)까지 다양하다.
- 응용 분야: 텍스트 편집기, 검색 엔진, 생물정보학(DNA 서열 분석), 이미지 처리

## Relationships
- [[brute-force-string-matching]] (가장 단순한 O(nm) 완전 탐색 매칭 알고리즘)
- [[knuth-morris-pratt-algorithm]] (failure function을 이용한 O(m+n) 최적 알고리즘)
- [[boyer-moore-algorithm]] (looking-glass·character-jump 휴리스틱 기반 실용 고속 알고리즘)
- [[string-matching-algorithm-comparison]] (세 알고리즘의 성능 및 적용 상황 비교 분석)

## Open Questions
- 반복 패턴이 많은 DNA 서열·이미지 데이터에서 KMP와 Boyer-Moore 중 어느 쪽이 더 우월한가에 대한 실증적 비교
- 다중 패턴 동시 매칭 문제(예: Aho-Corasick 알고리즘)와의 이론적 연관성
- 알파벳 크기 s가 작아질수록 Boyer-Moore의 character-jump 효용이 감소하는 현상의 정확한 임계점

## Sources
- raw/알고리즘/CH11 스트링 매칭.pdf
