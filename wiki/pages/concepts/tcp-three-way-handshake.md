---
title: TCP Three-Way Handshake
category: concept
tags: [tcp, connection, handshake, network, socket]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP 연결을 수립하기 위해 클라이언트와 서버가 세 개의 세그먼트(SYN → SYN+ACK → ACK)를 교환하는 절차. 연결-지향(connection-oriented) 프로토콜인 TCP가 데이터 전송 전에 양쪽 엔드포인트 간의 상태(connection state)를 설정하는 핵심 메커니즘이다.

## How It Works

**정상적인 연결 수립 (Three-Way Handshake)**

1. **SYN**: 클라이언트가 자신의 ISN(Initial Sequence Number)을 포함한 SYN 세그먼트를 서버로 전송. Berkeley Sockets API에서 `connect()` 호출 시 발생.
2. **SYN+ACK**: 서버가 자신의 ISN과 클라이언트 ISN+1을 ACK로 포함한 SYN+ACK 세그먼트 응답. `accept()`가 블로킹 대기 중인 상태에서 처리.
3. **ACK**: 클라이언트가 서버 ISN+1을 ACK로 포함한 ACK 세그먼트 전송. `connect()`가 반환되며 연결이 ESTABLISHED 상태로 전환.

각 SYN 및 SYN+ACK 세그먼트는 시퀀스 번호 공간에서 1을 소비하며, 유실 시 재전송된다.

**정상적인 연결 종료 (Four-Way or Combined Three-Way Handshake)**

TCP는 설계상 4-way handshake로 연결을 종료하나, 많은 구현에서 2번째와 3번째 세그먼트(FIN+ACK)를 결합하여 3-way로 처리한다:
1. `close()` 호출 측이 FIN 전송
2. 상대방이 FIN+ACK 응답 (또는 ACK와 FIN을 분리하여 응답)
3. 원래 종료 요청 측이 최종 ACK 전송 → TIME_WAIT 상태 진입

각 FIN 세그먼트(데이터 없음)도 시퀀스 번호 1을 소비한다.

**특수 케이스**

- **Simultaneous Open**: 두 앱이 동시에 active open을 수행. 양쪽이 client이자 server 역할. 4개의 세그먼트 필요(일반 3-way보다 1개 더).
- **TCP Half-Close**: `shutdown()` 함수를 사용해 단방향 데이터 흐름만 종료. 한쪽 FIN을 보내되 상대방의 데이터는 계속 수신. 두 번의 half-close가 전체 연결을 닫음.
- **Simultaneous Close**: 양쪽 모두 active close를 수행.

## Key Properties

- TCP는 unicast, connection-oriented 프로토콜로 데이터 전송 전 연결 수립이 필수
- 연결은 **4-tuple** (로컬 IP, 로컬 포트, 원격 IP, 원격 포트)로 고유하게 식별
- 연결 수립 시 SYN/SYN+ACK 세그먼트로 TCP 옵션(MSS, WSCALE, Timestamps 등)을 교환
- TCP 헤더는 옵션을 위한 공간이 최대 40바이트
- Berkeley Sockets API는 SYN 세그먼트에 앱 데이터 포함을 지원하지 않아 실제로는 거의 사용되지 않음
- 연결의 세 단계: setup(connection establishment) → data transfer(established) → teardown(connection termination)

## Relationships

- [[tcp]] (three-way handshake가 동작하는 프로토콜의 전반적 개요)
- [[tcp-header]] (SYN, ACK, FIN 플래그가 포함된 헤더 구조)
- [[initial-sequence-number]] (각 SYN 세그먼트에 포함되는 ISN 선택 메커니즘)
- [[tcp-state-machine]] (three-way handshake의 상태 전이: CLOSED → SYN_SENT → ESTABLISHED)
- [[time-wait-state]] (active close 후 진입하는 2MSL 대기 상태)
- [[tcp-options]] (SYN/SYN+ACK 세그먼트에서 교환되는 MSS, WSCALE, Timestamps 등)
- [[tcp-reset-segment]] (연결 수립 실패나 비정상 종료 시 사용되는 RST 세그먼트)
- [[transport-layer-demultiplexing]] (4-tuple 기반으로 연결을 식별하는 역다중화)

## Open Questions

- Simultaneous Open은 NAT 환경에서 hole punching에 활용되는데, 현대 NAT 장치에서의 지원 수준과 신뢰성은 어느 정도인가?
- Berkeley Sockets API가 SYN 세그먼트에서의 데이터 전송(TCP Fast Open 방식)을 표준 지원하지 않는 이유는 무엇인가?
- TCP Half-Close는 사용이 드물다고 언급되는데, 어떤 실제 응용 사례가 있는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 4–8, 10–13)
