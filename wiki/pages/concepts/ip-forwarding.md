---
title: IP Forwarding
category: concept
tags: [networking, IP, forwarding, routing, hop-by-hop]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
IP Forwarding(IP 포워딩)은 IP 데이터그램이 목적지에 도달할 수 있도록 호스트 또는 라우터가 포워딩 테이블(Forwarding Information Base, FIB)을 조회하여 패킷을 적절한 인터페이스로 전달하는 과정이다. IP 포워딩은 hop-by-hop 방식으로 이루어지며, 각 노드는 전체 경로 정보 없이 다음 홉(next hop)만을 결정한다.

## How It Works

### 호스트에서의 포워딩
- **직접 전달(Direct Delivery)**: 목적지가 같은 링크에 연결된 경우, 라우터를 거치지 않고 직접 전달
- **간접 전달(Indirect Delivery)**: 목적지가 다른 네트워크에 있으면, 게이트웨이(next-hop router)로 포워딩. 해당하는 게이트웨이가 없으면 default 라우터로 전송

### 라우팅 테이블 크기를 줄이는 포워딩 기법
1. **Next-hop Method**: 완전한 경로 대신 다음 홉 주소만 저장 → 테이블 크기 감소
2. **Network-Specific Method**: 같은 물리 네트워크의 모든 호스트 대신 네트워크 주소 하나만 기록 → 테이블 크기 대폭 감소 (가장 일반적)
3. **Host-Specific Method**: 특정 호스트 주소를 테이블에 직접 기록 → 세밀한 라우팅 제어 가능하나 비효율적; 정책적 라우팅에 활용
4. **Default Method**: 테이블에 없는 모든 목적지를 default 라우터(0.0.0.0)로 전달 → 테이블 최소화

### 라우터에서의 포워딩
- 포워딩 테이블 컬럼: Destination, Mask, Next-hop, Interface
- [[longest-prefix-matching]] 알고리즘으로 최적 항목 선택
- 포워딩 테이블의 정확성은 라우팅 프로토콜(RIP, OSPF, BGP, ISIS)이 보장
- 가정용 무선 라우터는 라우팅 프로토콜 없이 정적 설정 사용

### 데이터그램 수신 처리 (호스트)
- 목적지 주소가 자기 자신이면: Protocol 필드에 따라 상위 계층 프로토콜 모듈로 전달
- 목적지가 자기 자신이 아니고 포워딩 허용 시: 포워딩 테이블에 따라 전달
- 포워딩 불허 또는 경로 없음: 조용히 폐기 후 ICMP 오류 메시지 발송 가능

### 멀티홈 호스트(Multi-homed Host) 모델
- **Strong Host Model**: 수신 시 목적지 주소가 해당 수신 인터페이스의 IP와 일치해야 수신 허용. 보안 강화. 현대 Windows 기본값.
- **Weak Host Model**: 목적지 주소가 호스트의 어느 인터페이스와 일치하면 수신 허용. Linux 기본값.
- 소스 주소 선택 정책도 OS마다 다름 (RFC6724 참고)

## Key Properties
- Hop-by-hop 방식: 각 라우터는 전체 경로 정보 없이 next hop만 결정
- 포워딩 테이블 = Forward Information Base (FIB), Unix의 kernel IP routing table과 동일 개념
- 라우팅(경로 계산, 제어 평면)과 포워딩(패킷 전달, 데이터 평면)은 별개의 동작
- Linux는 weak host model, 현대 Windows는 strong host model이 기본값
- 포워딩 테이블 정보를 라우팅 프로토콜이 관리함

## Relationships
- [[longest-prefix-matching]] — 포워딩 테이블 조회에 사용되는 알고리즘
- [[router-architecture]] — 포워딩이 수행되는 라우터의 하드웨어 구조
- [[cidr]] — 포워딩 테이블 항목의 prefix 표현 방식
- [[route-aggregation]] — 포워딩 테이블 크기를 줄이는 기법
- [[network-layer]] — IP 포워딩이 속하는 계층
- [[network-address-translation]] — 포워딩 경로 상의 주소 변환 장치

## Open Questions
- 멀티홈 호스트에서 소스 주소 선택 정책(RFC6724)은 OS마다 다르다. 이로 인한 비대칭 라우팅(asymmetric routing) 문제는 어떻게 해결하는가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
