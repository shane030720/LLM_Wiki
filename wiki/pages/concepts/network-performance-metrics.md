---
title: Network Performance Metrics
category: concept
tags: [throughput, bandwidth, rtt, bdp, bottleneck, networking, performance]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
네트워크의 성능을 정량적으로 평가하는 주요 지표들의 집합이다. 핵심 지표로 Throughput(처리량), Bandwidth(대역폭), Round Trip Time(RTT), Bandwidth-Delay Product(BDP)가 있으며, 각 지표는 서로 다른 측면의 네트워크 성능을 나타낸다.

## How It Works
**Throughput:**
- Instantaneous throughput: 특정 시점에서 송신자에서 수신자로 비트가 전달되는 속도(bits/sec)
- Average throughput: 더 긴 시간 구간에 걸친 평균 전송 속도
- End-to-end throughput은 경로상 가장 느린 링크인 bottleneck link에 의해 결정됨
  - Rs < Rc이면 throughput = Rs (서버 측 링크가 병목)
  - Rs > Rc이면 throughput = Rc (클라이언트 측 링크가 병목)

**Bandwidth:**
- 엄밀한 정의: 전송 매체가 단위 길이당 일정 감쇠 이하를 유지하는 주파수 범위
- 컴퓨터 네트워킹에서의 일반적 사용: 정보가 전송될 수 있는 최대 속도(= 링크 용량)
- Aggregate bandwidth: 네트워크가 공급하는 총 데이터 대역폭
- Effective bandwidth(= throughput): 네트워크가 애플리케이션에 실제로 전달하는 대역폭

**Round Trip Time (RTT):**
- 네트워크 요청이 출발지에서 목적지로 갔다가 다시 돌아오는 총 시간
- 측정 방법(데이터 크기 등)과 네트워크 환경(혼잡도)에 따라 달라짐
- 소규모 데이터 전송: RTT가 전송 완료 시간의 지배적 요소
  - 예: 1 byte 파일, 1ms/1Mbps → 완료 시간 ≈ 1.008ms; 100ms/100Mbps → 완료 시간 ≈ 100ms
- 대규모(bulk/elephant) 데이터 전송: throughput이 지배적 요소
  - 예: 1 GB 파일, 1ms/1Mbps → 완료 시간 ≈ 2.38시간; 100ms/100Mbps → 완료 시간 ≈ 85초

**Bandwidth-Delay Product (BDP):**
- BDP = Bandwidth × Delay (보통 RTT를 delay 대표값으로 사용)
- "파이프 안에 존재하는" 데이터의 양(bits)을 나타내는 개념
- 예: 100 Mbps × 10 ms = 1 Mbit
- TCP 버퍼 크기 결정의 경험적 기준(rule of thumb)
- BDP는 첫 번째 비트가 목적지에 도착하기 전에 송신자가 전송할 수 있는 데이터 양을 나타냄
- 네트워크를 "파이프"로 시각화할 때 파이프의 용량에 해당

## Key Properties
- Bottleneck link: end-to-end 경로에서 throughput을 제한하는 가장 느린 링크
- 전송 완료 시간 ≈ RTT + (데이터 크기 / Throughput) (단순화된 모델)
- BDP가 클수록 "high bandwidth-delay product network" → 많은 데이터가 in-flight 상태
- 네트워크를 파이프로 비유할 때: 완전 활용을 위해 in-flight 데이터 양 ≥ BDP 유지 필요

## Relationships
- [[packet-delay]] — RTT는 packet delay 요소(처리·큐잉·전송·전파)들의 왕복 합산
- [[packet-switching]] — throughput과 queueing 지연은 packet switching 환경에서 발생
- [[multiplexing]] — 링크의 aggregate bandwidth는 multiplexing으로 자원을 공유한 결과

## Open Questions
- BDP 기반 TCP 버퍼 크기 조정이 실제 성능 향상에 얼마나 기여하는가?
- 400 Gbps 이상 초고속 링크에서 BDP가 수십 GB에 달할 때 프로토콜 설계에 어떤 영향을 미치는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
