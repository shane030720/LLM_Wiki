---
title: Packet Scheduling
category: concept
tags: [networking, QoS, router, scheduling, queue, fairness]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Packet Scheduling(패킷 스케줄링)은 라우터의 출력 포트에서 큐에 대기 중인 패킷들 중 다음에 링크로 전송할 패킷을 결정하는 정책이다. 스케줄링 정책은 서비스 품질(QoS), 공정성, 대역폭 보장, 네트워크 중립성 등에 직접적인 영향을 미친다.

## How It Works

### 1. FCFS / FIFO (First Come, First Served)
- 도착 순서대로 전송
- 구현이 단순하나 트래픽 유형 간 차별화 불가
- 현실 세계 예: 마트 계산대, 버스 정류장

### 2. Priority Scheduling (우선순위 스케줄링)
- 트래픽을 클래스로 분류하고 높은 우선순위 큐를 먼저 비움
- 같은 클래스 내에서는 FCFS 적용
- 분류 기준: IP DSCP, VLAN priority 등 임의 헤더 필드 사용 가능
- 주의: 낮은 우선순위 클래스가 starvation(기아) 상태에 빠질 수 있음

```
[High Priority Queue] → 먼저 전송
[Low Priority Queue]  → High Priority Queue가 비었을 때만 전송
```

### 3. Round Robin (RR, 라운드 로빈)
- 여러 클래스 큐를 순환하며 각 큐에서 완성된 패킷 하나씩 전송
- 모든 클래스에 공평한 서비스 기회 보장
- 단, 패킷 크기가 다르면 바이트 단위 공정성은 보장되지 않음

### 4. Weighted Fair Queuing (WFQ, 가중 공정 큐잉)
- Round Robin의 일반화
- 각 클래스 i에 가중치 wi 부여
- 사이클 내에서 `wi / Σwj` 비율만큼 서비스 할당
- **클래스별 최소 대역폭 보장** 가능
- QoS 구현의 핵심 메커니즘

예시: 세 클래스에 w=(5, 3, 2)이면, 각각 50%, 30%, 20%의 대역폭 할당

## Key Properties
- 스케줄링은 [[router-architecture]] 의 출력 포트에서 수행
- 버퍼 관리(drop policy: tail drop, priority drop)와 함께 혼잡 시 동작을 결정
- WFQ만이 각 flow/class에 최소 대역폭을 보장하는 메커니즘
- **네트워크 중립성**: ISP가 특정 트래픽을 우선처리하거나 throttle하는 것이 스케줄링 정책으로 구현됨
- 실제 구현에서는 DRR(Deficit Round Robin) 등 변형 사용
- ECN(Explicit Congestion Notification)과 RED(Random Early Detection)은 패킷 marking 기반 혼잡 신호 기법

## Relationships
- [[router-architecture]] — 스케줄링이 적용되는 출력 포트
- [[congestion-control-principles]] — 패킷 스케줄링과 혼잡 제어의 상호작용
- [[tcp-flow-control]] — 스케줄링 정책이 TCP 성능에 미치는 영향
- [[network-layer]] — 스케줄링이 동작하는 계층

## Open Questions
- 네트워크 중립성(Network Neutrality): 기술적으로 스케줄링 정책이 콘텐츠/애플리케이션별 차별을 가능하게 한다. 이를 법적·규제적으로 어떻게 제한하거나 허용해야 하는가? (미국 FCC 2015 Open Internet Order 참조)

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
