---
title: Middlebox
category: concept
tags: [networking, middleware, NAT, firewall, SDN, NFV]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Middlebox(미들박스)는 출발지 호스트와 목적지 호스트 사이의 데이터 경로 상에서 표준 IP 라우터의 정상 기능 이외의 기능을 수행하는 모든 중간 장치를 의미한다 (RFC 3234, "any intermediary box performing functions apart from normal, standard functions of an IP router on the data path between a source host and destination host"). NAT, 방화벽, 로드 밸런서, 캐시 등이 포함된다.

## How It Works

주요 미들박스 유형과 배치 위치:

| 유형 | 기능 | 배치 위치 |
|---|---|---|
| NAT | 사설 IP ↔ 공인 IP 변환 | 가정, 기업, 4G/5G 네트워크 |
| Firewall / IDS | 패킷 필터링, 침입 탐지 | 기업, ISP, 서비스 프로바이더 |
| Load Balancer | 트래픽을 여러 서버로 분산 | 데이터센터, CDN, 기업, 모바일 |
| Cache | 콘텐츠 캐싱으로 대역폭 절약 | ISP, 모바일 네트워크, CDN |
| Application-Specific | 특정 애플리케이션 처리 | CDN, ISP |

### 기술 진화 트렌드
- **초기**: 전용(proprietary) 폐쇄형 하드웨어 솔루션
- **현재 흐름**:
  - Whitebox 하드웨어 + Open API: 범용 하드웨어에 오픈 소프트웨어 탑재
  - Match+Action 기반 프로그래머블 로컬 액션
  - **SDN (Software-Defined Networking)**: 중앙집중식 제어 및 설정 관리 (프라이빗/퍼블릭 클라우드)
  - **NFV (Network Functions Virtualization)**: 화이트박스 네트워킹·컴퓨팅·스토리지 위에서 가상화된 네트워크 기능 제공

### "IP Hourglass의 Love Handles"
인터넷 아키텍처는 IP를 중심으로 한 모래시계(hourglass) 구조를 지향하지만, 미들박스의 확산은 이 모래시계의 중간 허리 부분에 "love handles"(군살)이 생긴 것으로 비유된다. 즉, IP 계층에 NAT, 방화벽, 캐시 등이 끼어들어 [[end-to-end-argument]] 원칙이 약화된 상태를 의미한다.

## Key Properties
- 표준 IP 라우터 기능 이외의 작업 수행 (by definition)
- [[end-to-end-argument]] 원칙을 위반하는 존재
- 인터넷의 모든 레벨(가정, 기업, ISP, 데이터센터)에 편재
- 소프트웨어 혁신과 차별화 방향으로 발전 (NFV, SDN)
- [[packet-scheduling]] 및 버퍼 관리 등 QoS 기능도 미들박스에서 수행 가능

## Relationships
- [[end-to-end-argument]] — 미들박스가 도전하는 인터넷 설계 원칙
- [[network-address-translation]] — 가장 광범위하게 배치된 대표적 미들박스
- [[network-layer]] — 미들박스가 주로 동작하는 계층 (상위 계층도 관여)
- [[packet-scheduling]] — 로드 밸런서 등 미들박스의 스케줄링 기능

## Open Questions
- SDN과 NFV의 발전으로 미들박스가 더욱 유연하고 프로그래머블해지면, end-to-end 원칙은 더 이상 의미가 없어지는가?
- 클라우드 기반 SDN 제어 평면을 사용하는 미들박스에서 단일 장애점(single point of failure) 문제를 어떻게 해결하는가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
