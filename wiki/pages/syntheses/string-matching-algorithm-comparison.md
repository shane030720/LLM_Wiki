---
title: String Matching Algorithm Comparison
category: synthesis
tags: [algorithm, string, pattern-matching, comparison, complexity]
sources: [raw/알고리즘/CH11 스트링 매칭.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Thesis
세 가지 주요 문자열 매칭 알고리즘(Brute-Force, KMP, Boyer-Moore)은 이론적 시간복잡도와 실용적 성능 사이에서 서로 다른 트레이드오프를 보인다. 이론적 최적성(O(m+n))은 KMP가 보장하지만, 실제 영문 텍스트에서의 실용적 성능은 Boyer-Moore가 더 우월하다. 데이터의 성격에 따라 최선의 알고리즘이 달라진다.

## Evidence
- **Brute-Force**: 시간복잡도 O(nm), 전처리 없음. 구현이 가장 단순하나 반복 패턴 텍스트(DNA, 이미지)에서 최악 성능 발생이 용이하다.
- **KMP**: 시간복잡도 O(m+n)으로 이론적 최적을 보장한다. failure function 전처리 O(m). 반복 패턴이 많은 데이터에서도 성능이 일정하게 유지된다.
- **Boyer-Moore**: 최악 시간복잡도 O(nm+s)이나, 영문 텍스트에서 "significantly faster than the brute-force algorithm"임이 명시되어 있다. Character-jump로 인해 문자 하나의 불일치만으로도 패턴 길이에 가까운 점프가 가능하다.
- Last-occurrence function 전처리가 O(m+s)이며, 알파벳이 클수록 jump 효과가 증대된다.

| 알고리즘 | 전처리 | 매칭 | 최악 | 추가 공간 |
|---|---|---|---|---|
| Brute-Force | 없음 | O(nm) | O(nm) | O(1) |
| KMP | O(m) | O(n) | O(m+n) | O(m) |
| Boyer-Moore | O(m+s) | 평균 빠름 | O(nm+s) | O(s) |

## Counterevidence
- Boyer-Moore의 최악 시간복잡도 O(nm+s)는 KMP O(m+n)보다 점근적으로 나쁘다.
- Boyer-Moore 최악 사례(T = "aaa...a", P = "baaa")는 DNA 서열·이미지 처리 등 현실적인 데이터에서 실제로 발생할 수 있다.
- KMP는 영문 텍스트에서 Boyer-Moore보다 느릴 수 있어, 이론적 최적성이 실용적 우위를 항상 보장하지는 않는다.

## Conclusion
알고리즘 선택 기준:
- **일반 영문 텍스트 또는 큰 알파벳 데이터** → [[boyer-moore-algorithm]] (실용적 최고 성능)
- **DNA·이미지 등 작은 알파벳·반복 패턴 데이터** → [[knuth-morris-pratt-algorithm]] (안정적 O(m+n) 최적 보장)
- **단순 구현 필요 또는 매우 짧은 텍스트** → [[brute-force-string-matching]] (전처리 오버헤드 없음, 구현 단순)

이론적 보장과 실용적 성능이 반드시 일치하지 않는 대표적 사례이며, 입력 데이터의 특성이 알고리즘 선택의 핵심 기준이 된다.

## Sources
- raw/알고리즘/CH11 스트링 매칭.pdf
