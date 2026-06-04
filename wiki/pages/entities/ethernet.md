---
title: Ethernet
category: entity
tags: [ethernet, lan, csma-cd, ieee-802-3, networking, wired]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Overview
Ethernet은 현재 가장 지배적인 유선 LAN 기술이다. 1970년대 Bob Metcalfe 등이 Xerox PARC에서 개발하였으며, 1980년 DEC·Intel·Xerox(DIX) 연합이 표준을 발표하고 1982년 Ethernet II로 개정했다. 10 Mbps에서 시작해 현재 400 Gbps까지 발전했고, 단일 칩으로 다중 속도를 지원한다(예: Broadcom BCM5761). Bob Metcalfe는 이 공헌으로 2022년 ACM Turing Award를 수상했다. IEEE 802.3 표준과 공존하나, 효율성 이유로 Ethernet II(RFC 894) encapsulation이 실제로 더 널리 사용된다.

## Capabilities
**물리 토폴로지:**
- Bus 토폴로지 (1990년대 중반까지): 동축 케이블 사용
  - ThickNet (10BASE5): 최대 500m
  - ThinNet (10BASE2): 최대 185m
  - 모든 노드가 동일한 collision domain을 공유
- Switched 토폴로지 (현재 지배적): 중앙 Layer 2 스위치 사용, 각 포트가 독립적인 collision domain

**CSMA/CD (Carrier Sense Multiple Access with Collision Detection):**
- 전통적 Ethernet의 매체 접근 제어(MAC) 방식
- "listen before talk": 전송 전 채널이 유휴 상태인지 감지(Carrier Sense)
- 전파 지연으로 인해 충돌이 완전히 방지되지는 않음
- 충돌 감지 시 jamming signal 전송 → 다른 노드들의 충돌 인지 용이
- 전이중(full-duplex) 스위치 환경에서는 CSMA/CD 불필요

**Ethernet 프레임 구조 (Ethernet II / RFC 894):**
- Preamble (8 Bytes): 송수신 클럭 동기화 (7 bytes 0xAA + SFD 0xAB)
- Destination MAC Address (6 Bytes): 목적지 MAC 주소; broadcast 주소 수신 시 상위 계층 전달
- Source MAC Address (6 Bytes)
- Type (2 Bytes): 상위 계층 프로토콜 지정 (IP=0x0800, ARP=0x0806, RARP=0x0835); 수신 측 demultiplexing에 사용
- Data/Payload (46–1500 Bytes)
- CRC (4 Bytes): Cyclic Redundancy Check; 오류 감지 시 프레임 폐기

**IEEE 802.3 표준과의 관계:**
- 1985년 IEEE Project 802: 물리 계층·데이터 링크 계층 표준화
- OSI Layer 2를 LLC(Logical Link Control)와 MAC(Media Access Control)으로 세분화
- IEEE 802.2/802.3 Encapsulation(RFC 1042): Length 필드 사용, DSAP/SSAP/제어 필드 추가
- STP(Spanning Tree Protocol) 활성화 스위치/라우터 환경에서 실제 802.3 트래픽 관찰 가능

## Limitations
- Bus 토폴로지: 모든 노드가 collision domain을 공유하여 확장성 제한
- CSMA/CD는 반이중(half-duplex) 환경 전제; 현대 전이중 스위치 환경에서 의미 없음
- IEEE 802.3 encapsulation은 Ethernet II 대비 오버헤드가 커 효율이 낮음
- 최소 프레임 크기(46 bytes payload) 제약: 작은 패킷은 패딩(PAD) 필요

## Relationships
- [[ieee-802-11]] — 무선 LAN 대응 표준(Wi-Fi); 상위 계층 프로토콜은 공유
- [[network-connecting-devices]] — Ethernet 스위치, 브리지, 허브 등이 Ethernet 망 구성
- [[multiplexing]] — Type 필드를 통한 상위 계층 프로토콜 demultiplexing
- [[access-network]] — 홈·기업·데이터센터 유선 access network의 핵심 기술
- [[packet-switching]] — Ethernet 프레임은 IP 데이터그램(packet)을 캡슐화

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
