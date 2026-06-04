---
title: Silly Window Syndrome (SWS)
category: concept
tags: [tcp, flow-control, performance, sws, nagle, clark, delayed-ack]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Silly Window Syndrome (SWS)는 TCP 슬라이딩 윈도우의 잘못된 구현으로 인해 매우 작은 데이터를 운반하는 세그먼트가 대량으로 전송되는 성능 저하 현상이다. 'silly'는 대용량 헤더 오버헤드(최소 40바이트: IP 20 + TCP 20)에 비해 극히 적은 페이로드를 운반하는 비효율적인 처리를 뜻한다. 예를 들어, 1바이트 페이로드를 담은 41바이트 세그먼트가 반복 전송되는 상황이 대표적이다.

## How It Works

### 발생 원인

**수신자 측 SWS**: 수신 버퍼가 가득 찬 상태에서 응용 프로그램이 1바이트씩 천천히 읽으면, 수신자는 매번 rwnd=1을 ACK에 포함하여 광고한다. 흐름 제어 메커니즘에 따라 송신자는 이에 따라 1바이트 페이로드 세그먼트를 반복 전송한다.

**송신자 측 SWS**: 응용 프로그램이 1바이트씩 천천히 write를 호출하면, 송신자는 ACK를 받을 때마다 매번 1바이트 페이로드를 가진 세그먼트를 전송한다.

### 해결 방법

#### 송신자 측: Nagle's Algorithm (RFC 896, by John Nagle)

1. 송신 응용으로부터 받은 첫 번째 데이터는 크기가 1바이트라도 즉시 전송한다.
2. 이후 출력 버퍼에 데이터를 누적하며 대기한다. 다음 중 하나가 만족되면 전송한다:
   - 이전 세그먼트에 대한 ACK를 수신하거나
   - 누적 데이터가 MSS(Maximum Segment Size) 크기에 도달할 때
3. Step 2를 전송 완료까지 반복한다.

핵심 아이디어: "in-flight 세그먼트가 있는 동안은 새 데이터를 누적하고 보류한다."

#### 수신자 측 해결 방법 1: Clark's Solution (RFC 813, by David Clark)

- 데이터 도착 즉시 ACK를 보내되, rwnd 값은 다음 조건 중 하나가 충족될 때까지 0으로 광고한다:
  - 수신 버퍼의 절반(at least half) 이상이 비거나
  - MSS 크기의 세그먼트를 수용할 수 있는 공간이 생길 때

#### 수신자 측 해결 방법 2: Delayed ACK

- 세그먼트가 도착해도 즉시 ACK를 보내지 않고, 수신 버퍼에 충분한 공간이 생길 때까지 ACK 전송을 지연한다.
- 단점: ACK 지연으로 인해 송신자가 불필요한 재전송을 할 수 있다.
- RFC 1122 및 RFC 9293의 요구 사항:
  - ACK 지연은 반드시 0.5초(500ms) 미만이어야 한다.
  - 최소 두 번째 full-size 세그먼트마다 또는 2 × RMSS(Receiver's Maximum Segment Size)의 새 데이터마다 ACK를 생성해야 한다.

## Key Properties

- 수신자 측 SWS는 Nagle's Algorithm만으로는 해결되지 않는다. 수신자가 소량의 데이터를 읽으면 작은 rwnd를 ACK에 포함하여 전송하고, 송신 TCP는 이 ACK를 받으면 작은 윈도우에 맞는 소규모 세그먼트를 다시 전송하기 때문이다.
- Nagle's Algorithm은 레이턴시에 민감한 응용(예: SSH 인터랙티브 세션, 실시간 게임)에서 TCP_NODELAY 소켓 옵션으로 의도적으로 비활성화된다.
- Clark's Solution과 Delayed ACK는 보완적으로 사용 가능하다.
- Nagle's Algorithm과 Delayed ACK가 동시에 활성화되면 심각한 지연이 발생할 수 있다 (Nagle-Delayed ACK 상호작용 문제).

## Relationships

- [[tcp-flow-control]] — SWS는 흐름 제어 메커니즘의 비효율적인 구현에서 발생한다.
- [[tcp-sliding-window]] — 가변 윈도우 크기 운용 시 발생하는 성능 문제이다.
- [[maximum-segment-size]] — Nagle's Algorithm과 Clark's Solution 모두 MSS를 기준으로 전송 임계값을 설정한다.
- [[tcp]] — SWS 회피 알고리즘은 TCP 구현의 필수 요소이다.
- [[tcp-error-control]] — Delayed ACK는 SWS 회피와 오류 제어 모두에 활용된다.

## Open Questions

- Nagle's Algorithm과 Delayed ACK가 동시에 활성화될 때 발생하는 40ms 지연 문제를 어떻게 해결하는가?
- 현대 네트워크에서 대역폭이 크게 증가했음에도 SWS가 여전히 실질적인 문제가 되는가? 고속 네트워크에서의 영향 범위는?

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
