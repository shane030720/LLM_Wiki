---
title: Congestion Control Principles
category: concept
tags: [network, congestion, transport-layer, protocol]
sources: [raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Congestion control은 네트워크에서 너무 많은 소스(senders)가 너무 빠르게 너무 많은 데이터를 전송하여 네트워크가 처리할 수 없는 상태(congestion)를 감지하고 완화하는 메커니즘이다. Flow control(단일 송신자가 단일 수신자에 비해 너무 빠른 경우를 다룸)과는 구별되며, 네트워크 전체의 다수 송신자를 대상으로 한다.

## How It Works

### 혼잡의 원인과 비용 — 세 가지 시나리오

**Scenario 1: 무한 버퍼, 재전송 없음**
- 라우터 1개, 무한 버퍼, 재전송 없음
- 입력률 λ_in이 링크 용량 R/2에 접근할수록 지연(queueing delay)이 급격히 증가
- 최대 처리량은 R/2를 초과할 수 없음
- 비용: 용량에 접근할수록 무한대로 증가하는 지연

**Scenario 2: 유한 버퍼, 재전송 있음**
- 라우터 1개, 유한 버퍼, 패킷 손실 시 재전송 발생
- 이상적 경우(perfect knowledge): 송신자가 버퍼 가용 여부를 완벽히 알 경우, 재전송 오버헤드 최소화 가능
- 현실적 경우: 타이머가 조기 만료(premature timeout)되어 불필요한 중복 패킷(un-needed duplicates)이 전송되고 링크 용량이 낭비됨
- 비용:
  - 재전송으로 인한 추가 작업 (동일한 throughput을 위해 더 많은 전송 필요)
  - 불필요한 중복 패킷이 달성 가능한 최대 처리량을 감소시킴

**Scenario 3: 다중 홉, 다중 송신자**
- 4개 송신자, 다중 홉 경로, timeout/retransmit
- 한 흐름의 트래픽이 증가하면 다른 흐름의 패킷이 라우터 버퍼에서 드롭됨
- 상류(upstream)에서 소비한 전송 용량과 버퍼가 하류(downstream)에서 패킷 손실 시 완전히 낭비됨
- 비용: 패킷이 최종 목적지에 도달하지 못할 경우 그 경로상의 모든 자원이 낭비됨

### 혼잡 제어의 접근법

**End-end congestion control (종단간 혼잡 제어)**
- 네트워크로부터 명시적 피드백 없음
- 송신자가 관측된 패킷 손실 및 지연으로부터 혼잡을 추론
- TCP가 채택하는 방식

**Network-assisted congestion control (네트워크 지원 혼잡 제어)**
- 라우터가 혼잡 상태에 대한 직접적 피드백을 송수신 호스트에 제공
- 혼잡 수준 표시 또는 전송률을 명시적으로 설정
- 예: TCP ECN(Explicit Congestion Notification), ATM, DECbit 프로토콜

## Key Properties

- Congestion은 flow control과 다름: flow control은 수신자 측 버퍼 보호, congestion control은 네트워크 전체의 용량 보호
- 혼잡의 주요 증상: 라우터 버퍼의 queueing으로 인한 긴 지연, 버퍼 오버플로우로 인한 패킷 손실
- 처리량(throughput)은 링크 용량을 절대 초과할 수 없음
- 용량에 가까워질수록 지연이 급격히 증가함
- 불필요한 재전송(un-needed retransmissions)은 유효 처리량을 추가로 감소시킴
- 다운스트림에서 손실된 패킷에 대해 업스트림에서 소비한 자원은 모두 낭비됨

## Relationships

- [[tcp-congestion-control]] — TCP의 end-end 혼잡 제어 구체적 구현
- [[tcp-flow-control]] — 혼잡 제어와 구별되는 수신자 측 흐름 제어 메커니즘
- [[tcp]] — congestion control이 구현되는 전송 계층 프로토콜
- [[network-performance-metrics]] — throughput, delay 등 혼잡과 직결되는 성능 지표

## Open Questions

- 네트워크 지원 혼잡 제어(ECN 등)가 end-end 혼잡 제어보다 실질적으로 얼마나 더 효과적인가?
- 무선 네트워크에서의 패킷 손실(오류로 인한 손실)을 혼잡으로 잘못 판단하는 문제를 어떻게 구별할 수 있는가?

## Sources

- raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf
