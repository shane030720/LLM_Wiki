---
title: TCP Sliding Window
category: concept
tags: [tcp, sliding-window, sequence-number, buffer, snd-una, snd-nxt, rcv-nxt]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Sliding Window는 TCP가 신뢰성 있는 데이터 전송을 구현하기 위해 사용하는 바이트 지향(byte-oriented) 슬라이딩 윈도우 프로토콜이다. 세그먼트 번호가 아닌 페이로드의 바이트 오프셋을 기준으로 윈도우를 관리하며, 수신 측 흐름 제어(rwnd)와 혼잡 제어(cwnd)에 의해 동적으로 크기가 조절된다.

## How It Works

### 송신자 측 (Sender-Side) 파라미터

- **SND.UNA (Send Unacknowledged, Sf)**: 전송되었지만 아직 ACK를 받지 못한 첫 번째 바이트의 시퀀스 번호. 송신 윈도우의 왼쪽 경계.
- **SND.NXT (Send Next, Sn)**: 다음에 전송할 바이트의 시퀀스 번호.
- **SND.WND (Send Window)**: 현재 허용된 송신 윈도우 크기.
  - Send Window Size = min(rwnd, cwnd)
  - rwnd: 수신자가 광고한 수신 윈도우 크기 (흐름 제어)
  - cwnd: 혼잡 제어 윈도우 크기
- **In-flight bytes**: SND.NXT - SND.UNA (전송됐지만 미확인된 바이트 수)
- **Available window**: SND.UNA + SND.WND - SND.NXT (추가로 전송 가능한 바이트 수)

### 송신 윈도우 동작

- **Closing (왼쪽 경계 전진)**: 미확인 첫 바이트보다 큰 n에 대한 ACK n이 수신되면 SND.UNA가 n으로 이동한다.
- **Opening (오른쪽 경계 확장)**: rwnd 증가 또는 cwnd 증가 시 윈도우 오른쪽이 확장된다.
- **Shrinking (오른쪽 경계 축소)**: rwnd 감소 또는 cwnd 감소 시 윈도우 오른쪽이 축소된다. RFC는 이미 전송된 데이터와의 충돌 가능성 때문에 이를 권장하지 않는다.

### 수신자 측 (Receiver-Side) 파라미터

- **RCV.NXT (Receive Next, Rn)**: 수신자가 다음에 수신하기를 기대하는 바이트의 시퀀스 번호. 수신 윈도우의 왼쪽 경계.
- **RCV.WND (rwnd, Receive Window)**: 수신자가 광고하는 수신 가능 버퍼 크기.

### 수신 윈도우 동작

- **Opening**: 응용 프로그램이 수신 버퍼에서 더 많은 데이터를 읽어 가면 rwnd가 증가한다.
- **Closing**: 새로 도착한 세그먼트가 RCV.NXT(다음 기대 바이트)를 채우면 RCV.NXT가 전진한다.
- **Shrinking**: Rn이 "응용 프로세스가 다음에 읽을 바이트" 포인터보다 빠르게 전진하면 rwnd가 줄어든다.
- **Steady**: Rn과 "응용 프로세스가 다음에 읽을 바이트"가 같은 속도로 전진하면 rwnd가 일정하게 유지된다.

### ARQ 배경과의 관계

TCP는 GBN(Go-Back-N) ARQ의 변형을 사용한다. 슬라이딩 윈도우 내의 패킷이 순서대로 도착하지 않으면 누적 ACK를 통해 갭을 표시하며, 타임아웃 또는 Duplicate ACK에 의해 재전송이 트리거된다. TCP는 NAK를 사용하지 않는다.

## Key Properties

- TCP는 세그먼트 지향이 아닌 **바이트 지향** 슬라이딩 윈도우를 사용한다. 시퀀스 번호는 페이로드의 첫 바이트의 스트림 오프셋이다.
- 각 TCP 연결마다 독립적인 송신 버퍼와 수신 버퍼 쌍이 유지된다.
- 송신 윈도우 크기는 흐름 제어(rwnd)와 혼잡 제어(cwnd) 중 작은 값으로 결정된다.
- ACK 번호는 누적(cumulative)이다: ACK n은 n 미만의 모든 바이트를 수신했음을 의미한다.
- TCP 헤더의 Window Size 필드가 rwnd를 전달하며, 이 필드 자체가 "수신 윈도우 필드"이다. 슬라이딩 윈도우의 크기 파라미터 SND.WND와 구별해야 한다.

## Relationships

- [[arq-protocols]] — TCP 슬라이딩 윈도우는 GBN ARQ 변형을 바이트 지향으로 구현한 것이다.
- [[tcp-flow-control]] — rwnd를 통해 수신자가 송신자의 전송 속도를 조절한다.
- [[tcp-error-control]] — 슬라이딩 윈도우 상에서 손실·중복·순서 불일치 세그먼트를 처리하는 메커니즘이다.
- [[tcp]] — TCP의 신뢰성 있는 데이터 전송의 핵심 메커니즘이다.
- [[tcp-header]] — rwnd 값은 TCP 헤더의 Window Size 필드를 통해 광고된다.
- [[silly-window-syndrome]] — 윈도우 크기의 비효율적인 소규모 변동으로 발생하는 성능 문제이다.
- [[tcp-retransmission-timeout]] — 슬라이딩 윈도우의 타이머 관리와 긴밀하게 연동된다.
- [[tcp-window-scale]] — rwnd의 표현 범위를 65535바이트 이상으로 확장하는 TCP 옵션이다.

## Open Questions

- TCP 표준 명세(RFC 9293)는 응용 프로그램이 얼마나 많은 바이트를 읽고 쓰는지를 명시적으로 고려하지 않는다. 시스템 구현 관점에서 이 값은 어떻게 관리되는가?
- Shrinking window가 이미 전송된 데이터와 충돌할 경우 어떻게 처리되는가? RFC 7323은 어떤 입장을 취하는가?

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
