---
title: Router Architecture
category: concept
tags: [networking, router, hardware, switching, forwarding, queuing]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Router Architecture(라우터 아키텍처)는 네트워크 라우터의 내부 구조로, 입력 포트(input ports), 스위칭 패브릭(switching fabric), 출력 포트(output ports), 라우팅 프로세서(routing processor)의 네 가지 주요 구성 요소로 이루어진다. 데이터 평면(data plane, 포워딩)은 하드웨어로 구현되어 나노초 단위로 동작하고, 제어 평면(control plane, 라우팅)은 소프트웨어로 구현되어 밀리초 단위로 동작한다.

## How It Works

### 구성 요소

**Input Port(입력 포트)**
- 물리 계층: 비트 수신
- 링크 계층: Ethernet 등 처리
- 포워딩 테이블 조회 및 큐잉: "match plus action" 방식으로 헤더 필드를 보고 출력 포트 결정
- 목표: 라인 속도(line speed)로 처리 완료
- Destination-based forwarding(목적지 주소만 사용) 또는 Generalized forwarding(임의 헤더 필드 사용)

**Switching Fabric(스위칭 패브릭)**
입력 포트에서 적절한 출력 포트로 패킷을 전달하는 핵심 구성요소. 세 가지 방식:

| 방식 | 특징 | 병목 |
|---|---|---|
| Memory | 1세대; CPU 직접 제어, 메모리 복사 | 메모리 대역폭 (2회 버스 통과) |
| Bus | 공유 버스를 통해 입출력 포트 간 전달 | 버스 대역폭 (예: Cisco 5600, 32 Gbps) |
| Interconnection Network | Crossbar, Clos 등 멀티스테이지; 병렬성 활용 | 거의 없음; 수백 Tbps 달성 가능 |

Cisco CRS 라우터: 8개 스위칭 평면(plane), 각 평면 3단계 interconnection network → 수백 Tbps 용량

**Output Port(출력 포트)**
- 스위칭 패브릭에서 수신한 데이터그램을 버퍼링하고 링크로 전송
- 버퍼 관리(drop policy)와 [[packet-scheduling]] 정책 적용

**Routing Processor(라우팅 프로세서)**
- 라우팅 프로토콜(RIP, OSPF, BGP 등) 실행
- 포워딩 테이블(FIB) 계산 및 유지
- 네트워크 관리

### Input Port Queuing과 HOL Blocking
- 스위칭 패브릭 처리 속도 < 입력 포트 합산 속도이면 입력 큐 발생
- **Head-of-Line (HOL) Blocking**: 큐의 앞 패킷이 같은 출력 포트를 원하는 뒤 패킷들의 진행을 막는 현상 → 처리량 저하

### Output Port Queuing
- 스위칭 패브릭 전달 속도 > 링크 전송 속도이면 출력 큐 발생
- 버퍼 오버플로우 시 패킷 손실 발생
- **버퍼 크기 권고**:
  - RFC 3439 rule of thumb: RTT × 링크 용량 C (예: 250 ms × 10 Gbps = 2.5 Gbit)
  - N개 flow 존재 시: RTT × C / sqrt(N)
  - 너무 큰 버퍼는 RTT 증가(bufferbloat)를 야기하므로 주의

## Key Properties
- 데이터 평면(포워딩): 하드웨어, 나노초 단위
- 제어 평면(라우팅): 소프트웨어, 밀리초 단위
- 스위칭 속도 목표: N개 입력 포트 × 라인 속도 (이상적으로 NR)
- HOL Blocking은 입력 큐 기반 스위치의 성능 저하 요인
- 출력 포트에서 [[packet-scheduling]] 정책으로 QoS 및 공정성 구현
- [[longest-prefix-matching]] 은 TCAM으로 O(1) 조회

## Relationships
- [[ip-forwarding]] — 라우터 아키텍처에서 수행되는 포워딩 프로세스
- [[longest-prefix-matching]] — 입력 포트 포워딩 테이블 조회 알고리즘
- [[packet-scheduling]] — 출력 포트에서 패킷 전송 순서를 결정하는 정책
- [[network-layer]] — 라우터 아키텍처가 구현하는 계층

## Open Questions
- 버퍼 크기 최적화(bufferbloat vs. packet loss): 버퍼가 너무 크면 실시간 앱 성능 저하, 너무 작으면 손실 증가. AQM(Active Queue Management)으로 어느 정도 해결 가능하지만 최적 정책은 여전히 연구 중이다.

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
