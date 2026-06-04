---
title: TCP Retransmission Timeout (RTO)
category: concept
tags: [tcp, rto, rtt, ewma, retransmission, karn, exponential-backoff]
sources: [raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Retransmission Timeout (RTO)는 TCP 송신자가 전송한 세그먼트에 대한 ACK를 기다리는 최대 시간이다. RTO가 만료되면 해당 세그먼트를 재전송한다. RTO는 측정된 RTT(Round-Trip Time)의 지수 가중 이동 평균(Exponential Weighted Moving Average, EWMA)과 변동(variation)을 기반으로 동적으로 계산되며, RFC 9293은 RFC 6298의 알고리즘을 MUST로 요구한다.

## How It Works

### RTT 구성 요소

실제 RTT는 다음 요소의 합이다:
- Forward trip time: 송신자 → 수신자 전송 시간
- Receiver processing delay: 수신자의 패킷 처리 및 ACK 생성 시간
- Backward trip time: ACK가 수신자 → 송신자로 돌아오는 시간
- Sender processing delay: 송신자의 ACK 처리 시간

이 값들은 실제로 측정이 어렵고 시간에 따라 변하므로 통계적 추정이 필요하다.

### SmoothedRTT 추정 (EWMA)

SmoothedRTT = (1 - alpha) x SmoothedRTT + alpha x MeasuredRTT

- 전형적인 alpha = 0.125 (1/8)
- 초기값: 첫 번째 측정에서 SmoothedRTT = MeasuredRTT
- 과거 샘플의 영향이 지수적으로 감소하므로 최신 측정값에 더 민감하게 반응한다.
- 교재 표기: RTT_S (Smoothed RTT); Kurose-Ross 표기: EstimatedRTT

### RTTVAR 추정 (변동 추정, EWMA)

RTTVAR = (1 - beta) x RTTVAR + beta x |MeasuredRTT - SmoothedRTT|

- 전형적인 beta = 0.25 (1/4)
- 초기값: 첫 번째 측정에서 RTTVAR = MeasuredRTT / 2
- RTT 변동성의 추정치로 RTO 계산의 안전 마진 역할을 한다.
- 교재 표기: RTT_D (RTT Deviation); Kurose-Ross 표기: DevRTT

### RTO 계산

RTO = SmoothedRTT + max(G, K x RTTVAR)

- K = 4 (전형적인 값)
- G = clock granularity (클럭 해상도)
- 초기 RTO: RFC 6298 기준 1초 (구 RFC 2988 기준 3초)
- RTTVAR를 "안전 마진(safety margin)"으로 사용하여 RTO를 SmoothedRTT보다 크게 설정함으로써 불필요한 재전송을 방지한다.

### Karn's Algorithm

- 재전송된 세그먼트에 대한 RTT 샘플은 SmoothedRTT/RTTVAR 업데이트에 사용하지 않는다.
- 이유: 재전송 후 도착하는 ACK가 원본 전송에 대한 것인지 재전송에 대한 것인지 구별할 수 없기 때문이다 (Retransmission Ambiguity Problem).
- 재전송이 발생하지 않은 세그먼트에 대한 ACK를 받은 후에만 RTT 측정을 재개한다.

### Exponential Backoff (RFC 6298 Algorithm 5.5)

- 타임아웃으로 인한 재전송이 발생할 때마다 RTO 값을 두 배로 늘린다.
- RTO의 최대값을 설정할 수 있다(MAY).
- 연속적인 재전송 실패 시 네트워크 혼잡에 대응하는 역할을 한다.

## Key Properties

- SmoothedRTT와 RTTVAR 모두 EWMA 기반이므로 계산이 단순하고 실시간 갱신이 용이하다.
- RTO를 너무 작게 설정하면 불필요한 재전송 → 네트워크 혼잡 악화.
- RTO를 너무 크게 설정하면 ACK 손실 후 긴 대기 → 처리량 저하.
- Karn's Algorithm은 재전송 이후 RTT 추정이 오염되는 것을 방지한다.
- Exponential Backoff는 네트워크가 혼잡할수록 재전송 빈도를 낮추어 congestion collapse를 방지한다.
- alpha=0.125, beta=0.25, K=4는 Jacobson/Karels 알고리즘에서 도출된 실용적인 값이다.

## Relationships

- [[tcp-error-control]] — RTO 만료는 TCP 오류 제어의 타임아웃 기반 재전송 트리거이다.
- [[tcp-sliding-window]] — RTO 타이머는 슬라이딩 윈도우의 SND.UNA(가장 오래된 미ACK 세그먼트)에 연동된다.
- [[tcp]] — RTO 계산은 TCP 신뢰성 메커니즘의 핵심이다.
- [[tcp-three-way-handshake]] — SYN+ACK 수신 시 첫 번째 MeasuredRTT가 측정된다.
- [[tcp-timestamps]] — Timestamps 옵션을 사용하면 더 정밀한 RTT 측정이 가능하다.

## Open Questions

- TCP Timestamps 옵션([[tcp-timestamps]])을 활성화하면 재전송 시에도 RTT를 정확히 측정할 수 있는가? Karn's Algorithm을 대체할 수 있는가?
- 네트워크 경로가 급격히 변경될 때 SmoothedRTT와 RTTVAR가 빠르게 적응하지 못하는 문제를 어떻게 해결하는가?
- RFC 6298에서 RTO 상한은 어떻게 권장되는가? (일반적으로 60초 이상 권장)

## Sources

- raw/컴퓨터네트워크/Week 06 TCP Sliding Window.pdf
