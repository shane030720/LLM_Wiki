---
title: TCP Congestion Control
category: concept
tags: [tcp, congestion, aimd, slow-start, network]
sources: [raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Congestion Control은 TCP 송신자가 congestion window(cwnd)를 동적으로 조정하여 네트워크 혼잡을 스스로 감지하고 전송률을 제어하는 end-end 메커니즘이다. 명시적 네트워크 피드백 없이 패킷 손실과 ACK 수신 패턴을 통해 혼잡을 추론하며, AIMD 원칙과 Slow Start를 결합한다.

## How It Works

### Congestion Window (cwnd)

TCP 송신자는 다음 조건으로 전송을 제한한다:

```
LastByteSent - LastByteAcked < cwnd
```

- cwnd는 바이트 단위로 관리되며 네트워크 혼잡 상태에 따라 동적으로 조정됨
- 수신자 버퍼 제약(rwnd)은 이 페이지에서 충분히 크다고 가정
- 대략적인 TCP 전송률: cwnd / RTT (bytes/sec)

### AIMD (Additive Increase Multiplicative Decrease)

TCP 혼잡 제어의 핵심 원리로, 사용 가능한 대역폭을 탐색(probe)하는 톱니 패턴(sawtooth behavior)을 생성한다.

**Additive Increase (가산적 증가):**
- 패킷 손실이 없는 매 RTT마다 cwnd를 1 MSS씩 증가
- 혼잡 회피(Congestion Avoidance) 구간에서 선형적 증가

**Multiplicative Decrease (승산적 감소):**
- 손실 이벤트 감지 시 cwnd를 감소
- Triple Duplicate ACK 감지 시 (TCP Reno): cwnd를 절반으로 감소
- Timeout 감지 시 (TCP Tahoe): cwnd를 1 MSS로 감소

AIMD는 분산·비동기 알고리즘으로, 네트워크 전체 흐름률을 최적화하고 안정성(stability) 특성을 갖는 것이 수학적으로 증명되어 있다.

### Slow Start

연결 초기 또는 timeout 이후 cwnd를 빠르게 증가시키는 단계:
- 초기 cwnd = 1 MSS
- ACK를 받을 때마다 cwnd를 1 MSS씩 증가 → 매 RTT마다 cwnd가 두 배로 증가 (지수적 성장)
- 초기 전송률은 낮지만 지수적으로 빠르게 증가함

### ssthresh (Slow Start Threshold)와 Congestion Avoidance

Slow Start에서 Congestion Avoidance로 전환하는 임계값:
- cwnd가 ssthresh에 도달하면 선형 증가로 전환(Congestion Avoidance 시작)
- 손실 이벤트 발생 시 ssthresh = 손실 직전 cwnd의 절반으로 설정

### TCP Tahoe vs TCP Reno

| 구분 | TCP Tahoe | TCP Reno |
|------|-----------|----------|
| Triple Duplicate ACK 처리 | cwnd = 1 MSS, Slow Start | cwnd = cwnd/2, Fast Recovery |
| Timeout 처리 | cwnd = 1 MSS, Slow Start | cwnd = 1 MSS, Slow Start |
| ssthresh 설정 | 손실 전 cwnd의 절반 | 손실 전 cwnd의 절반 |

**Fast Recovery (TCP Reno 추가 기능):**
- Triple Duplicate ACK 감지 시 Slow Start로 돌아가지 않고 cwnd = ssthresh + 3 MSS로 설정
- 추가 Duplicate ACK마다 cwnd를 1 MSS씩 증가
- 새로운 ACK 수신 시 cwnd = ssthresh로 설정하고 Congestion Avoidance 재개

### TCP Fairness

**공정성 목표:** K개의 TCP 세션이 대역폭 R의 병목 링크를 공유할 때 각 세션은 평균 R/K의 전송률을 가져야 함.

AIMD의 공정성 달성 메커니즘 (이상적 조건 하에서):
- Additive Increase: 처리량 공간에서 기울기 1의 방향으로 이동 → 동등 대역폭 분할선에 수렴
- Multiplicative Decrease: 손실 시 처리량을 비례적으로 감소 → 동등 분할선 방향으로 수렴

이상적 조건: 동일한 RTT, 고정된 세션 수, Congestion Avoidance 구간만 고려.

**공정성의 한계:**
- UDP 기반 멀티미디어 앱은 혼잡 제어를 적용받지 않아 TCP 세션과 대역폭 경쟁 불공정 발생
- 애플리케이션이 다수의 병렬 TCP 연결을 열면 (예: 웹 브라우저) 추가 대역폭 점유 가능

## Key Properties

- cwnd는 네트워크 혼잡 신호에 따라 동적으로 조정되는 핵심 제어 변수
- Slow Start: 지수적 증가로 빠르게 가용 대역폭 탐색
- Congestion Avoidance: 선형 증가로 조심스럽게 추가 대역폭 탐색
- ssthresh: Slow Start와 Congestion Avoidance 전환점
- Triple Duplicate ACK는 timeout보다 경미한 혼잡 신호로 취급 (Reno에서 더 보수적인 대응)
- AIMD 톱니 패턴(sawtooth)은 대역폭을 지속적으로 탐색하는 구조적 특성
- TCP 공정성은 동일 RTT, 고정 세션 수 등 이상적 조건에서만 보장

## Relationships

- [[congestion-control-principles]] — TCP 혼잡 제어가 구현하는 end-end 접근법의 일반 원리
- [[tcp-sliding-window]] — cwnd와 함께 전송 제한을 결정하는 수신자 측 rwnd 윈도우
- [[tcp-flow-control]] — cwnd와 구별되는 수신자 버퍼 보호 메커니즘
- [[tcp-retransmission-timeout]] — Slow Start 재시작을 트리거하는 timeout 메커니즘
- [[tcp-error-control]] — Triple Duplicate ACK 감지와 재전송 메커니즘
- [[tcp]] — 혼잡 제어가 구현되는 전송 계층 프로토콜

## Open Questions

- TCP CUBIC (Linux 기본값)은 Wmax 직후 빠른 증가 후 점진적 접근 방식으로 클래식 AIMD보다 높은 처리량을 달성하는데, 이것이 네트워크 전체 공정성에 미치는 영향은?
- Delay-based congestion control(BBR 등)은 패킷 손실을 강제하지 않고 RTT 측정으로 혼잡을 감지하는데, 손실 기반 TCP와 혼재할 때 공정성 문제가 발생하는가?
- 무선 네트워크에서 채널 오류로 인한 패킷 손실을 혼잡으로 잘못 해석하는 문제를 TCP 혼잡 제어는 어떻게 처리해야 하는가?

## Sources

- raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf
