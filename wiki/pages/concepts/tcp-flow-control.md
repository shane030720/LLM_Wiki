---
title: TCP Flow Control
category: concept
tags: [tcp, flow-control, rwnd, buffer, producer-consumer]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Flow Control은 수신 측 응용 프로그램이 데이터를 처리하는 속도에 맞추어 송신자의 전송 속도를 조절하는 end-to-end 메커니즘이다. 수신자는 TCP 헤더의 rwnd(Receive Window) 필드를 통해 현재 사용 가능한 수신 버퍼 크기를 광고하고, 송신자는 in-flight 데이터 양을 rwnd 이하로 제한한다.

## How It Works

### rwnd 기반 흐름 제어

1. 수신자는 수신 버퍼(RcvBuffer)를 유지한다. 기본 크기는 일반적으로 4096바이트이며, 대부분의 운영체제는 자동으로 조정한다.
2. 응용 프로세스가 수신 버퍼에서 데이터를 천천히 읽으면 버퍼 여유 공간이 줄어든다.
3. 수신자는 ACK 세그먼트를 보낼 때마다 남은 버퍼 공간(rwnd)을 헤더에 포함한다.
4. 송신자는 unACKed(in-flight) 데이터 양이 수신된 rwnd 값을 초과하지 않도록 전송량을 제한한다.
5. rwnd가 0이 되면 송신자는 전송을 일시 중단하고 수신자가 버퍼를 비울 때까지 대기한다.

### 생산자-소비자 관점 (Producer-Consumer Perspective)

흐름 제어는 생산자(Producer)와 소비자(Consumer) 사이의 속도 불일치 문제를 해결하는 서비스다.

- **Pushing 방식**: 생산자가 소비자의 요청 없이 즉시 데이터를 전달. TCP가 이 방식을 사용하므로 흐름 제어가 필요하다.
- **Pulling 방식**: 소비자가 먼저 요청한 후 생산자가 전달. 자연스럽게 속도가 조절된다.

TCP 흐름에서는 최소 두 단계의 흐름 제어 피드백이 필요하다:
- 수신자 TCP → 송신자 TCP: rwnd 광고 (세그먼트 수준, 소켓 간 피드백)
- 수신자 응용 → 수신자 TCP: 버퍼 읽기 속도 (프로세스 수준, 소켓 내부 피드백)

### 전송 윈도우 크기 결정

Send Window Size = min(rwnd, cwnd)

- rwnd: 흐름 제어에 의해 결정 (수신자 버퍼 가용량)
- cwnd: 혼잡 제어에 의해 결정 (네트워크 혼잡 상태)

## Key Properties

- 흐름 제어는 수신자의 처리 능력을 보호하며, 혼잡 제어(congestion control)와 달리 네트워크 상태가 아닌 수신 엔드포인트의 상태에 반응한다.
- rwnd = 0이 되면 "Zero Window" 상태 — 송신자는 Persist Timer를 이용해 주기적으로 1바이트 probe 세그먼트를 보내 윈도우가 열렸는지 확인한다.
- rwnd는 바이트 단위이며, TCP 헤더의 16비트 Window Size 필드를 통해 전달된다.
- 운영체제는 일반적으로 RcvBuffer 크기를 소켓 옵션이나 자동 조정 알고리즘으로 관리한다.
- 응용 프로그램의 읽기 속도가 지나치게 느리면 [[silly-window-syndrome]]을 유발한다.

## Relationships

- [[tcp-sliding-window]] — rwnd는 TCP 슬라이딩 윈도우의 오른쪽 경계를 결정하는 핵심 파라미터이다.
- [[silly-window-syndrome]] — rwnd의 비효율적인 소규모 변동이 SWS를 유발한다.
- [[tcp]] — 흐름 제어는 TCP의 핵심 기능 중 하나이다.
- [[tcp-header]] — rwnd 값은 TCP 헤더의 Window Size 필드로 전달된다.
- [[tcp-window-scale]] — rwnd의 최대값을 65535바이트 이상으로 확장한다.

## Open Questions

- rwnd = 0인 상태에서 수신자가 보내는 Window Update ACK 세그먼트 자체가 손실되면 어떻게 되는가? (Persist Timer 메커니즘으로 해결)
- 운영체제가 RcvBuffer 크기를 자동으로 조정할 때 어떤 기준을 사용하며, 이것이 흐름 제어 동작에 어떤 영향을 미치는가?

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
