---
title: Automatic Repeat reQuest (ARQ) Protocols
category: concept
tags: [arq, error-control, reliability, network, sliding-window]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Automatic Repeat reQuest (ARQ)는 수신자가 패킷의 오류를 감지했을 때 송신자에게 재전송을 요청함으로써 신뢰성 있는 데이터 전송을 보장하는 오류 제어 프로토콜 계열이다. 수신자는 오류 없이 수신한 패킷에 대해 긍정 응답(ACK)을, 오류가 감지된 경우 부정 응답(NAK)을 전송하며, 이를 통해 송신자가 재전송 여부를 결정한다. ACK/NAK의 해석 방식은 시스템 설계에 따라 다를 수 있다.

## How It Works

ARQ는 세 가지 기본 체계로 분류된다.

**Stop-and-Wait ARQ (S&W)**
송신자는 하나의 프레임을 전송한 후 해당 프레임에 대한 ACK 또는 NAK를 받을 때까지 대기한다. Alternating Bit Protocol (ABP)이 검증된 구현 방식이다. ACK를 수신하기까지의 시간이 프레임 전송 시간에 비해 클 경우 채널 이용 효율이 매우 낮아진다.

**Go-Back-N ARQ (GBN)**
송신자는 최대 N개의 패킷을 연속으로 전송(window)한다. NAK 수신 시 해당 패킷부터 이후 모든 패킷을 재전송한다. N은 RTT(Round-Trip Time) 내에서 전송 중인(in-flight) 패킷 수이며, Bandwidth-Delay Product (BDP = Bandwidth × RTT)와 직접 관련된다. 수신자는 순서가 맞지 않는 패킷을 버리고 마지막으로 올바르게 수신한 패킷까지의 누적 ACK를 보낸다.

**Selective-Repeat ARQ (SR)**
최대 N개의 패킷을 연속으로 전송하며, "번호가 매겨진" NAK를 수신하면 해당 패킷만 선택적으로 재전송한다. ACK 수신 시 윈도우를 전진(slide)시킨다. 수신자는 순서가 맞지 않은 패킷도 버퍼에 저장해 둔다.

## Key Properties

- ACK/NAK 자체도 오류가 발생하거나 손실될 수 있다 — 이 경우 타임아웃 기반 재전송이 필요하다.
- 패킷은 손상(damage), 지연(delay), 중복(duplicate), 손실(loss)될 수 있으므로 타임아웃 재전송이 ARQ만큼 중요하다.
- ARQ는 Forward Error Correction (FEC)와 함께 사용될 수 있다.
- 실제 인터넷 프로토콜인 TCP는 NAK를 사용하지 않으며 ACK만 사용한다.
- Window size N은 BDP에 의해 결정되며, 채널 이용 효율을 극대화하려면 N이 충분히 커야 한다.
- S&W는 N=1인 GBN의 특수 케이스로 볼 수 있다.

## Relationships

- [[tcp-sliding-window]] — TCP는 GBN의 변형을 기반으로 바이트 지향 슬라이딩 윈도우를 구현한다.
- [[tcp-error-control]] — TCP의 오류 제어는 ARQ 원리를 타임아웃, 누적 ACK, 재전송으로 구현한다.
- [[selective-acknowledgment]] — TCP SACK 옵션은 SR-ARQ의 선택적 재전송 아이디어를 TCP에 적용한 확장이다.
- [[tcp]] — TCP는 ARQ 메커니즘을 트랜스포트 계층에서 구현하는 대표적인 프로토콜이다.

## Open Questions

- 데이터 링크 계층(예: IEEE 802.11)에 자체 ARQ가 있음에도 TCP가 별도로 ARQ를 구현해야 하는 이유는 무엇인가? (엔드투엔드 신뢰성 원칙 — 링크 단위 ARQ는 단일 링크의 오류만 처리하며, 중간 노드의 손실은 처리하지 못한다.)
- GBN과 SR-ARQ에서 window size의 최대값 제약이 다른 이유는 무엇인가? (시퀀스 번호 공간과의 관계)

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
