---
title: Network Connecting Devices
category: concept
tags: [switch, router, hub, bridge, repeater, stp, networking, layer2]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Network Connecting Device는 호스트 또는 네트워크 세그먼트를 상호 연결하여 더 큰 네트워크나 인터넷을 구성하는 장치를 총칭한다. 동작하는 계층에 따라 물리 계층(Repeater/Hub), 데이터 링크 계층(Bridge/Switch), 네트워크 계층(Router)으로 분류된다.

## How It Works
**Repeater (리피터):**
- 물리 계층 2-포트 장치
- 한 포트에서 수신한 신호를 증폭하여 다른 포트로 전달
- 필터링(filtering) 기능 없음 → 오류 신호도 그대로 전달
- 능동 소자(전원 필요); 수동 소자인 Tee connector(BNC)와 구별됨
- 네트워크 확장에 단순하고 저렴하지만 확장성 제한

**Hub (허브) / Multiport Repeater:**
- 물리 계층 다중 포트 장치
- 한 포트로 수신한 신호를 나머지 모든 포트로 전달(broadcast)
- 필터링 기능 없음 → 연결된 모든 노드가 하나의 collision domain 형성
- 100 Mbps까지 주로 사용; Gigabit Ethernet 이후 스위치로 대체됨

**Bridge (브리지) / Layer 2 Switch:**
- 데이터 링크 계층 장치
- 1983년 DEC의 Mark Kempf가 발명; 1990년 Kalpana이 최초 멀티포트 Ethernet 스위치 출시
- MAC 주소 학습(self-learning): 수신 패킷의 source MAC 주소를 포트와 매핑하여 forwarding table 구성
- 목적지 MAC 주소 기반 선택적 전달(필터링) → collision domain 분리
- 투명성(transparency): 호스트는 브리지/스위치의 존재를 인식하지 못함
- Broadcast domain은 여전히 공유
- 종류: transparent(IEEE 802.1D 기준), unmanaged(관리 인터페이스 없음), managed(CLI/Web 설정 가능)
- Layer 3/4/7 스위치: 상위 계층 헤더까지 디코딩하여 트래픽 필터링 가능

**Spanning Tree Protocol (STP):**
- 1984년 Radia Perlman(DEC)이 제안, IEEE 802.1D로 표준화
- 물리적 루프가 있는 토폴로지에서 MAC address learning의 루프 문제(loop problem) 방지
- 일부 포트를 차단(blocking)하여 논리적 트리 토폴로지 구성
- 일부 저가 스위치에 STP 미구현 → 실제 환경에서 브로드캐스트 스톰(loop) 발생 가능
- IEEE 802.1D 기준 투명 브리지는 forwarding, self-learning, loop prevention 3가지 기능 필수

**Router (라우터):**
- 물리·데이터 링크·네트워크 계층 모두에서 동작
- 물리 계층: 신호 재생성
- 데이터 링크 계층: MAC 주소 확인; 패킷 전달 시 source·destination MAC 주소 변경
- 네트워크 계층: IP 주소 기반 라우팅 결정
- 각 인터페이스마다 별도의 MAC 주소와 IP 주소 보유
- Broadcast domain을 분리 (브리지/스위치는 broadcast domain을 분리하지 않음)

## Key Properties
- 동작 계층이 높을수록 더 정교한 필터링·라우팅 가능
- Bridge/Switch: collision domain 분리 (broadcast domain은 공유)
- Router: broadcast domain까지 분리
- Hub/Repeater: 필터링 없음, 단일 collision domain 유지
- 투명 브리지의 3대 필수 기능: forwarding, self-learning, loop prevention

## Relationships
- [[ethernet]] — 이 장치들이 Ethernet 망 구성에 사용됨; CSMA/CD는 hub 환경에서 특히 중요
- [[packet-switching]] — 라우터가 packet switching의 핵심 장치로 동작
- [[access-network]] — 홈·기업·데이터센터 access network 구성에 스위치·라우터 활용
- [[osi-reference-model]] — 장치의 동작 계층을 OSI 모델 기준으로 분류

## Open Questions
- Layer 7 스위치(Application Delivery Controller)는 어떤 기준으로 트래픽을 분류·전달하는가?
- STP의 수렴(convergence) 시간 문제를 개선한 RSTP(Rapid STP)와 MSTP(Multiple STP)는 어떻게 동작하는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
