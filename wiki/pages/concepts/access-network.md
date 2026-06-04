---
title: Access Network
category: concept
tags: [access-network, dsl, cable, hfc, cellular, networking, wan]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Access Network는 최종 사용자(end system)를 인터넷의 첫 번째 라우터(edge router)에 연결하는 네트워크를 말한다. 가정용(residential), 기업용(enterprise), 모바일(cellular), 데이터센터용 등 다양한 형태로 존재하며, 기술·대역폭·공유 방식에서 차이를 보인다.

## How It Works
**케이블 기반 액세스 (HFC: Hybrid Fiber Coax):**
- 케이블 TV 인프라(광섬유 + 동축 케이블 혼합) 재활용
- FDM으로 비디오·데이터·제어 채널을 주파수 대역 분리
- 다운스트림: 40 Mbps – 1.2 Gbps, 업스트림: 30–100 Mbps (비대칭)
- 가정들이 cable headend까지 공유 배포 네트워크를 사용 → 이웃 간 대역폭 경쟁 발생
- Cable Modem Termination System(CMTS)이 headend에서 케이블 모뎀을 집선

**DSL (Digital Subscriber Line):**
- 기존 전화선(구리선)을 통해 중앙국(central office)의 DSLAM(DSL Access Multiplexer)에 연결
- 데이터는 인터넷으로, 음성은 전화망으로 분리 전송(주파수 분리)
- 다운스트림: 24–52 Mbps, 업스트림: 3.5–16 Mbps
- 각 가정에 전용 회선(dedicated line) → 이웃 간 대역폭 경쟁 없음

**셀룰러 네트워크 (4G LTE 기준):**
- SIM 카드로 사용자(UE, User Equipment) 식별
- UE → eNode-B(기지국, radio access network) → all-IP Enhanced Packet Core(EPC) → Internet
- EPC 구성 요소: MME(Mobility Management Entity), Serving Gateway(S-GW), PDN Gateway(P-GW), HSS(Home Subscriber Service)
- 이동성(mobility) 지원이 핵심 특징

**홈 네트워크:**
- 케이블/DSL 모뎀 + 라우터/방화벽/NAT + Wi-Fi AP가 단일 all-in-one 박스로 통합되는 경우 많음
- 유선: Gigabit Ethernet, 무선: Wi-Fi (54–450 Mbps)

**기업 네트워크:**
- 유선(Ethernet 100 Mbps/1 Gbps/10 Gbps)과 무선(Wi-Fi) 혼합 구성
- 스위치와 라우터를 혼합하여 캠퍼스 내 연결
- 기관 전용 메일·웹 서버 등 내부 서비스와 ISP 연결 병행

**데이터센터 네트워크:**
- 10s–100s Gbps 고대역폭 링크
- 수백~수천 대의 서버 상호 연결 및 인터넷 접속
- Content provider가 직접 운용하기도 함

## Key Properties
- HFC는 공유 매체(shared), DSL은 전용 회선(dedicated)
- 셀룰러는 이동성(mobility)을 기본 지원
- 홈 네트워크 장비는 복수 기능의 통합(integration) 추세
- 데이터센터는 국가/글로벌 ISP를 통해 인터넷에 연결

## Relationships
- [[multiplexing]] — HFC에서 FDM으로 비디오·데이터 채널 분리; DSL에서도 음성·데이터 주파수 분리
- [[ethernet]] — 기업·데이터센터 access network의 유선 기술
- [[ieee-802-11]] — 홈·기업 access network의 무선 기술
- [[network-connecting-devices]] — access network 내에서 스위치·라우터 사용
- [[packet-delay]] — access link의 속도(R)가 transmission delay에 직접 영향

## Open Questions
- FTTH(Fiber to the Home)는 HFC/DSL을 어떻게 대체하고 있는가?
- 5G 네트워크 아키텍처는 4G LTE와 핵심 구조(Core Network)에서 어떻게 달라지는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
