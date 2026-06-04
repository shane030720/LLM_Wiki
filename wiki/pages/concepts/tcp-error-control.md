---
title: TCP Error Control
category: concept
tags: [tcp, error-control, ack, duplicate-ack, fast-retransmit, retransmission]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Error Control은 체크섬(Checksum), 확인 응답(Acknowledgment), 타임아웃(Timeout)을 결합하여 손상·손실·중복·순서 불일치 세그먼트를 감지하고 복구하는 메커니즘이다. 수신자의 ACK 생성 규칙(RFC 5681 / RFC 9293)과 송신자의 재전송 정책에 의해 구현되며, TCP는 NAK 없이 ACK와 Duplicate ACK만을 사용한다.

## How It Works

### 수신자 ACK 생성 규칙 (RFC 5681 / RFC 9293)

**규칙 1 (피기백)**: 수신자가 데이터를 전송할 때는 ACK를 세그먼트에 피기백(piggyback)하여 함께 전송한다. 별도의 ACK 세그먼트 수를 줄여 트래픽을 감소시킨다.

**규칙 2 (Delayed ACK)**: 수신자가 전송할 데이터가 없고, 순서대로 도착한 세그먼트이며, 이전 세그먼트가 이미 ACKed인 경우: 다음 세그먼트를 최대 500ms 기다린 후 ACK를 전송한다 (in-order 세그먼트가 하나뿐일 때만 지연 허용).

**규칙 3 (즉시 누적 ACK)**: 순서대로 세그먼트가 도착했지만 이전 세그먼트가 아직 ACKed되지 않은 경우: 즉시 누적 ACK를 전송한다. 동시에 미ACK 상태인 in-order 세그먼트가 2개 이상이 되어서는 안 된다.

**규칙 4 (Duplicate ACK 전송)**: 기대보다 높은 시퀀스 번호의 세그먼트가 도착하여 갭(gap)이 감지된 경우: 즉시 Duplicate ACK를 전송하여 다음으로 기대하는 바이트 번호를 알린다. 누락된 세그먼트의 빠른 재전송을 유도한다.

**규칙 5 (갭 채움 ACK)**: 누락된 세그먼트가 도착하여 갭이 완전히 또는 부분적으로 채워진 경우: 즉시 ACK를 전송하여 새로운 다음 기대 바이트 번호를 알린다.

**규칙 6 (중복 세그먼트 처리)**: 중복 세그먼트가 도착한 경우: 세그먼트를 폐기하고 즉시 누적 ACK를 전송한다. 이전에 보낸 ACK가 손실되어 발생한 재전송에 대한 응답이다.

### 송신자 동작 (Simplified FSM)

- **app에서 데이터 수신**: 시퀀스 번호를 포함한 세그먼트를 생성하고, 타이머가 실행 중이지 않으면 시작한다. 타이머는 가장 오래된 미ACK 세그먼트(SND.UNA)에 대해 유지된다.
- **타임아웃 발생**: 타임아웃을 유발한 세그먼트를 재전송하고 타이머를 재시작한다.
- **ACK 수신**: 새로운 바이트를 ACK한 경우 ACKed 상태를 업데이트한다. 아직 미ACK 세그먼트가 있으면 타이머를 시작한다.

### 오류 제어 시나리오

1. **Normal Operation**: 순서대로 전송·수신, 규칙 2-3에 따른 ACK로 정상 동작.
2. **Lost Segment**: 갭 감지 후 Duplicate ACK(규칙 4), RTO 만료 후 재전송.
3. **Fast Retransmission**: 3개의 Duplicate ACK(총 4번 같은 ACK)를 수신 시 타임아웃 없이 즉시 재전송. 인터넷 전반의 처리량을 높이기 위한 최적화.
4. **Lost ACK**: 후속 세그먼트의 누적 ACK가 손실된 ACK를 대체하여 자동으로 해결되는 경우가 많다.
5. **Lost ACK corrected by retransmission**: 누적 ACK로 손실된 ACK를 커버하지 못할 때 RTO 후 세그먼트 재전송으로 복구.

## Key Properties

- TCP는 NAK를 사용하지 않는다. Duplicate ACK가 암묵적 NAK 역할을 한다.
- ACK 번호는 누적(cumulative)이다: ACK n은 n 미만의 모든 바이트를 수신했음을 의미한다.
- TCP 타이머는 가장 오래된 미ACK 세그먼트(SND.UNA)에 대해 하나만 유지된다.
- Fast Retransmission에서 3 Duplicate ACK 임계값은 사실상 네트워크 재순서화(reordering)와 진짜 손실을 구별하기 위한 휴리스틱이다.
- 규칙 6의 중복 세그먼트 처리는 ACK 자체가 손실되었을 때 재전송된 세그먼트를 올바르게 처리한다.
- Delayed ACK(규칙 2)는 ACK 세그먼트 수를 줄이지만 Nagle's Algorithm과 동시에 활성화 시 지연을 유발할 수 있다.

## Relationships

- [[tcp-sliding-window]] — 오류 제어는 슬라이딩 윈도우 프로토콜 위에서 동작한다.
- [[tcp-retransmission-timeout]] — RTO는 오류 제어의 타임아웃 기반 재전송을 위한 타이머 값이다.
- [[arq-protocols]] — TCP 오류 제어는 ARQ(Go-Back-N 변형)의 인터넷 구현이다.
- [[selective-acknowledgment]] — SACK 옵션을 사용하면 수신자가 비연속적으로 수신된 데이터를 상세히 알릴 수 있어 재전송 효율이 높아진다.
- [[tcp-state-machine]] — 오류 제어의 송신자/수신자 FSM은 TCP 전체 연결 상태 기계의 일부이다.
- [[silly-window-syndrome]] — Delayed ACK(규칙 2)는 수신자 측 SWS 회피에도 활용된다.
- [[tcp]] — 오류 제어는 TCP 신뢰성 서비스의 핵심 구성 요소이다.

## Open Questions

- Fast Retransmission의 3 Duplicate ACK 임계값이 왜 3인가? 고속 네트워크에서 패킷 재순서화 빈도가 높아지면 이 임계값을 조정해야 하는가?
- Fast Retransmission 이후 TCP Reno는 Fast Recovery를 통해 Slow Start 없이 혼잡 윈도우를 유지하는데, 이것이 기본 error control과 어떻게 연동되는가?
- 규칙 3에서 "2개 이상 미ACK 금지" 조건이 불필요한 재전송과 네트워크 혼잡을 어떻게 방지하는가?

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
