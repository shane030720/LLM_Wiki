---
title: Process Description
category: concept
tags: [process-modeling, dfd, systems-analysis, documentation, structured-english]
sources: [raw/시스템 분석 이론/ch05-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Process Description은 DFD의 개별 프로세스에 부여하는 텍스트 기반 보충 문서이다. DFD 다이어그램만으로는 표현하기 어려운 복잡한 내부 로직, 조건 분기, 계산 규칙 등을 명시하여 분석가와 개발자가 프로세스의 정확한 동작을 이해할 수 있도록 한다.

## How It Works

Process Description은 DFD의 primitive process(더 이상 분해되지 않는 leaf 프로세스)에 주로 작성된다. CASE(Computer-Aided Software Engineering) 도구는 각 프로세스에 대한 설명을 쉽게 입력·관리하는 기능을 제공한다.

### 기법 선택 기준

- **단순한 로직**: 자연어 서술로 충분
- **복잡한 조건 분기나 계산 로직**: 아래 세 가지 형식적 기법 중 하나를 선택

### Structured English

자연어와 프로그래밍 언어의 중간 형태로, IF-THEN-ELSE, WHILE, FOR EACH 같은 제어 구조를 사용하여 프로세스 로직을 서술한다. 특정 프로그래밍 언어 문법에 종속되지 않아 기술적 배경이 없는 이해관계자도 읽을 수 있다. [[pseudocode]]와 유사하나 좀 더 자연어에 가깝다.

### Decision Trees

의사결정 로직을 트리 구조로 시각화한다. 조건(condition)이 분기 노드가 되고, 각 분기의 결과(action)가 리프 노드가 된다. 상호 배타적인 조건이 여러 단계에 걸쳐 중첩될 때 직관적으로 표현 가능하다.

### Decision Tables

조건(conditions)과 행동(actions)을 행렬 형태로 배열한 표다. 조건의 모든 조합과 그에 따른 동작을 체계적으로 열거하여 누락된 경우나 모순된 규칙을 발견하기 쉽다. 조건의 수가 많고 조합이 복잡할 때 Decision Tree보다 유리하다.

### Alternative Data Flows와의 관계

프로세스가 조건에 따라 서로 다른 data flow를 출력하는 경우(alternative data flows), DFD에는 두 data flow를 모두 표시하고, Process Description에서 IF 조건을 설명하여 언제 각 flow가 발생하는지를 명시한다.

## Key Properties

- DFD 다이어그램을 대체하지 않고 보완(supplement)하는 문서
- Primitive process(leaf process)에 주로 작성
- 로직 복잡도에 따라 자연어부터 Structured English, Decision Tree, Decision Table까지 단계적으로 선택
- CASE 도구와 통합되어 DFD 프로세스와 설명이 하나의 저장소에서 관리됨
- Alternative data flow(조건 분기 출력)의 발생 조건을 명확히 기술하는 주요 수단

## Relationships

- [[dfd-elements]] — Process Description은 DFD의 Process 요소에 첨부됨
- [[dfd-hierarchy]] — 분해가 완료된 primitive process에 Process Description이 작성됨
- [[data-flow-diagram]] — Process Description은 DFD를 보완하는 문서
- [[pseudocode]] — Structured English는 pseudocode와 유사한 형식을 사용

## Open Questions

- Structured English, Decision Tree, Decision Table 중 어떤 기법을 선택하는지에 대한 명확한 기준(조건 수, 로직 깊이 등)은 아직 체계화되어 있지 않으며 분석가의 판단에 의존하는 경우가 많다.
- CASE 도구 없이 Process Description을 관리할 때 DFD와 설명 간의 동기화(sync)를 어떻게 유지할지는 실무 과제로 남아 있다.
- AI 기반 요구사항 분석 도구가 보편화될 경우, 전통적인 Structured English 방식이 자연어 처리(NLP)로 대체될 가능성이 있다.

## Sources

- raw/시스템 분석 이론/ch05-1.pdf (p.21–23)
