---
title: TCP (Transmission Control Protocol)
category: entity
tags: [tcp, transport-layer, protocol, reliability, networking]
sources: [raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Overview

TCP(Transmission Control Protocol)는 인터넷 전송 계층(transport layer)의 핵심 프로토콜로, RFC 793(1981)에서 최초 정의되었고 RFC 9293(2022)에서 최신 표준이 확정되었다. UDP와 함께 인터넷 애플리케이션이 사용할 수 있는 두 가지 주요 전송 프로토콜 중 하나이며, connection-oriented, reliable, byte stream 서비스를 제공한다. 인터넷에서 가장 널리 사용되는 프로토콜이다.

TCP는 UDP와 동일한 network layer(IP)를 사용하지만, 애플리케이션 계층에 전혀 다른 품질의 서비스를 제공한다. 연결을 수립한 두 endpoint가 바이트 스트림 형태로 신뢰성 있게 데이터를 교환할 수 있도록 설계되었다.

## Capabilities

- **Connection-oriented service**: 데이터 교환 전 두 endpoint가 반드시 연결을 수립(handshaking)해야 한다. 연결은 두 endpoint 간 동기화된 상태(synchronized states)를 의미하며, 정확히 두 개의 endpoint만 참여한다(point-to-point).
- **Reliable, in-order byte stream**: 애플리케이션에 record marker나 message boundary 없이 8-bit 바이트 스트림을 제공한다. TCP는 바이트의 내용을 해석하지 않으며 각 endpoint가 독립적으로 읽기·쓰기 크기를 선택한다.
- **Packetization**: 바이트 스트림을 IP가 운반할 수 있는 segment 단위로 분할한다. 각 segment는 전체 데이터 스트림에서 첫 번째 바이트의 byte offset을 나타내는 sequence number를 포함한다.
- **Cumulative ACK**: 수신자가 성공적으로 받은 마지막 바이트 번호 + 1을 ACK number로 전송한다. ACK는 즉시 전송되지 않고 약간 지연될 수 있으며(delayed ACK), piggybacking 기법으로 데이터 segment에 함께 실어 보낼 수 있다.
- **Retransmission mechanism**: Go-Back-N ARQ 변형 방식을 사용하며, segment 전송 시 retransmission timer를 유지한다. ACK가 제때 도착하지 않으면 segment를 재전송한다. 여러 segment를 그룹으로 보낼 때는 단일 retransmission timer를 사용한다.
- **Duplicate and out-of-order handling**: Sequence number를 이용해 순서가 바뀐 segment를 재조립하고 중복 segment를 폐기한다.
- **Full-duplex service**: 하나의 연결에서 양방향으로 독립적인 데이터 흐름을 지원한다. 각 방향에 대해 독립적인 sequence number를 유지하며, 한 방향으로 흐르는 모든 TCP segment는 반대 방향 segment에 대한 ACK를 함께 포함한다.
- **Flow control**: Window Size 필드를 통해 수신자가 수용 가능한 바이트 수를 광고하여 발신자가 수신자를 압도하지 않도록 한다.
- **Congestion control**: 인터넷 전체를 위한 서비스로, 특정 애플리케이션을 위한 서비스가 아니다(Kurose & Ross). 원래 RFC 793에는 포함되지 않았고 이후 추가된 메커니즘이다.
- **Mandatory checksum**: TCP 헤더, 데이터, IP 헤더 일부를 포함한 pseudo-header 기반 체크섬을 계산하며, 발신자 계산과 수신자 검증이 모두 필수다. 유효하지 않은 segment는 ACK 없이 폐기된다.
- **Pipelining**: 혼잡 제어와 흐름 제어가 설정한 window size에 따라 여러 segment를 동시에 전송한다.

## Limitations

- **Delay 및 bandwidth 보장 없음**: TCP는 지연 보장(delay guarantee)이나 대역폭 보장(bandwidth guarantee)을 제공하지 않는다.
- **Point-to-point only**: 정확히 두 개의 endpoint 사이에서만 동작하며, 멀티캐스트나 브로드캐스트를 지원하지 않는다.
- **Checksum 강도 한계**: 대용량 데이터 전송 시 16비트 체크섬이 충분히 강하지 않을 수 있다(Stone & Partridge, 2000). 중요한 애플리케이션은 자체 오류 보호(더 강한 체크섬, CRC) 또는 미들웨어 계층(RFC 5044)을 적용해야 한다.
- **연결 수립 오버헤드**: 데이터 전송 전 handshaking이 필요하여 짧은 트랜잭션에서 추가 지연이 발생한다.
- **Head-of-line blocking**: 순서대로 전달하는 특성상 앞선 패킷이 손실되면 이후 패킷의 애플리케이션 전달이 지연된다.

## Relationships

- [[udp]] (동일한 네트워크 계층을 사용하지만 비신뢰적·비연결형인 대안 프로토콜)
- [[tcp-header]] (TCP segment의 헤더 구조와 각 필드 정의)
- [[transport-layer-demultiplexing]] (TCP가 사용하는 4-tuple 기반 connection-oriented 역다중화)
- [[tcp-ip-architecture]] (TCP가 속한 프로토콜 스택)
- [[multiplexing]] (TCP sender/receiver에서 수행되는 다중화·역다중화 개념)

## Sources

- raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf
