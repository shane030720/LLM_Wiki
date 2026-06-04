---
title: Packet Delay
category: concept
tags: [delay, latency, queueing, transmission, propagation, networking]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
패킷이 소스에서 목적지로 전달되는 과정에서 각 노드(라우터)에서 발생하는 총 지연을 Nodal Delay라 한다. 총 지연은 네 가지 독립적인 요소의 합으로 표현된다:

d_nodal = d_proc + d_queue + d_trans + d_prop

## How It Works
**1. Processing Delay (d_proc):**
- 비트 오류 확인 및 출력 링크 결정에 소요되는 시간
- 일반적으로 수 마이크로초(microsec) 이하로 매우 작음

**2. Queueing Delay (d_queue):**
- 패킷이 출력 링크의 큐에서 전송을 기다리는 시간
- 라우터의 혼잡(congestion) 수준에 따라 크게 변동
- 유일하게 예측 불가능한 지연 요소

**3. Transmission Delay (d_trans):**
- d_trans = L / R (L: 패킷 길이(bits), R: 링크 대역폭(bps))
- 패킷의 모든 비트를 링크에 밀어 넣는 데 걸리는 시간
- 패킷 크기와 링크 속도에만 의존

**4. Propagation Delay (d_prop):**
- d_prop = d / s (d: 물리 링크 길이, s: 전파 속도 ≈ 2×10^8 m/sec in 유선)
- 마지막 비트가 링크를 통해 이동하는 데 걸리는 시간
- 물리적 거리에만 의존

**Packetization 예시 (store-and-forward):**
- N = 4 홉, R = 9600 bps, 최대 패킷 크기 P = 1024 bits, 헤더 H = 16 bits, d_prop = 0.001초/홉
- 3200 bits 메시지 → 패킷 수 = ceil(3200 / (1024-16)) = 4 패킷 (패킷 1~3: 1008 bits payload, 패킷 4: 176 bits payload)
- 전송 지연: T = 1024/9600 = 0.1067초 (패킷 1~3), T' = 192/9600 = 0.02초 (패킷 4)
- 파이프라인 효과로 D1 = N×d_prop + N×T, D2=D3=T, D4=T'
- 총 지연 d = 0.4272 + 0.1067 + 0.1067 + 0.02 = 0.6606초

## Key Properties
- Transmission delay와 Propagation delay는 서로 독립적: 전자는 패킷 크기·대역폭 의존, 후자는 물리적 거리 의존
- Packetization은 메시지를 분할해 파이프라인 전송을 가능하게 하여 전체 지연을 줄임
- Queueing delay만이 네트워크 혼잡 상태에 따라 동적으로 변화
- 중간 스위치가 2개인 경로: 총 지연 = 3×d_prop + 3×d_trans + 3×d_proc (queueing 무시 시)

## Relationships
- [[packet-switching]] — store-and-forward packet switching 환경에서 이 4가지 지연이 발생
- [[network-performance-metrics]] — RTT는 이 지연 요소들의 왕복 합산 결과
- [[network-connecting-devices]] — 라우터의 처리 능력이 d_proc와 d_queue에 영향

## Open Questions
- Queueing delay를 정확히 모델링하는 방법(M/M/1, M/D/1 큐 이론)은 무엇인가?
- 실제 인터넷 환경에서 각 지연 요소의 평균적인 비율은 어떻게 되는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
