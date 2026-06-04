---
title: Network Protocol
category: concept
tags: [protocol, syntax, semantics, timing, communication]
sources: [raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Network Protocol은 분산된 개체(distributed entities)들 간에 데이터 통신 또는 상태 동기화를 수행하기 위한 메시지 교환 규칙 체계이다. "무엇을 통신하는지(what), 어떻게 통신하는지(how), 언제 통신하는지(when)"를 정의하며, Syntax(구문), Semantics(의미론), Timing(타이밍)의 세 요소로 구성된다. 'protocol'이라는 단어는 원래 "국가·외교 업무를 관장하는 공식 절차"를 의미했으며, 이 정의에서 착안하여 ARPAnet 엔지니어들이 NCP(Network Control Program)의 이름을 Network Control Protocol로 변경했다.

## How It Works

프로토콜이 동작하는 환경의 전제 조건:

- 각 개체는 상대방의 상태 정보를 **불완전하게(incomplete)** 알고 있다.
- 시간에 따른 메시지 교환을 통해 통신하거나 상태를 동기화한다.

인간의 대화 프로토콜을 예시로 들면, "Hi → Hi → Got the time? → 2:00"처럼 요청-응답의 흐름이 순서에 따라 진행된다. 네트워크에서도 동일한 구조가 나타난다. HTTP를 예로 들면:

1. 클라이언트가 TCP 연결 요청(TCP connection request)을 서버에 전송
2. 서버가 TCP 연결 응답(TCP connection response)을 반환
3. 클라이언트가 `GET http://...` 요청을 전송
4. 서버가 요청된 파일(`<file>`)을 응답으로 반환

각 단계는 Syntax로 정의된 형식, Semantics로 정의된 의미, Timing으로 정의된 순서를 따른다.

## Key Properties

프로토콜의 세 가지 핵심 구성 요소:

- **Syntax (구문)**: 명령(command) 및 응답(response)의 구조. 헤더 비트(field-formatted) 형태 또는 문자열(character-string) 형태로 정의된다.
- **Semantics (의미론)**: 발행할 요청(request)의 집합, 수행할 동작(action), 각 당사자가 반환할 응답(response)의 집합을 정의한다.
- **Timing (타이밍)**: 이벤트의 순서(ordering of events) 명세 — 메시지 교환 시 각 행동이 취해지는 순서를 규정한다.

## Relationships

- [[internet-standards]] — 프로토콜은 IETF RFC 등 표준화 절차를 통해 공식 Internet Standard로 채택됨
- [[computer-network]] — 프로토콜은 네트워크 내 모든 통신의 근간; 프로토콜 없이 네트워크는 동작 불가
- [[internet]] — TCP, IP, HTTP, DNS, SMTP 등 인터넷을 구성하는 모든 동작이 프로토콜 위에서 이루어짐

## Open Questions

- Syntax/Semantics/Timing 3요소 분류는 QUIC, gRPC 등 현대 프로토콜에도 그대로 적용 가능한가, 아니면 추가적인 차원(예: 보안, 상태 관리)이 필요한가?
- 분산된 개체의 범위가 단일 기계 내 프로세스 간 통신(IPC)으로 확장될 때, 네트워크 프로토콜과 IPC 프로토콜의 본질적 차이는 무엇인가?

## Sources

- raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf (pp.42–43)
