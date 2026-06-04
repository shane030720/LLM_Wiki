---
title: Computer Network
category: concept
tags: [network, node, link, packet, bandwidth]
sources: [raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Computer Network는 통신 채널(communications channel)로 상호 연결된 범용 컴퓨터들의 집합으로, 그 안에서 정보가 이동하는 시스템이다. Tanenbaum은 "단일 기술(a single technology)로 상호 연결된 자율적(autonomous) 컴퓨터들의 집합"으로 정의하며, Newman은 더 추상적으로 "노드(node)들이 링크(link)로 쌍 단위로 연결된 구조"로 정의한다. Peterson & Davie는 전화망·TV망 등 특수 목적 네트워크와 대비하여, 컴퓨터 네트워크가 범용 데이터를 처리한다는 점을 강조한다. 특정되지 않은 네트워크 및 서버의 집합을 클라우드(cloud)라 부르기도 한다.

## How It Works

컴퓨터 네트워크는 두 가지 핵심 구성 요소를 기반으로 동작한다.

- **Nodes (노드)**: 네트워크에 연결된 장치들. PC, 서버(server), 스위치(switch), 브리지(bridge), 라우터(router) 등이 해당한다.
- **Links (링크)**: 노드 간 물리적·논리적 연결. 광섬유(optical fiber), 동축 케이블(coaxial cable), 무선(wireless) 매체로 구현된다.

데이터는 패킷(packet) 단위로 분할되어 링크를 통해 전달되며, 라우터가 패킷을 목적지 방향으로 전달(forward)한다. 전송 속도는 대역폭(bandwidth)으로 측정된다.

인터넷의 관점에서 네트워크 구조는 세 계층으로 구분된다.

- **Network edge**: 클라이언트와 서버 등 호스트(host)로 구성된 끝단. 서버는 주로 데이터 센터에 위치한다.
- **Access networks**: 유선·무선 통신 링크로 구성된 접속망.
- **Network core**: 상호 연결된 라우터들로 이루어진 핵심망. "네트워크의 네트워크" 구조를 형성한다.

## Key Properties

- 범용성(general-purpose): 특정 데이터 유형(음성, 영상 등)에 국한되지 않고 모든 종류의 데이터를 전달
- 자율성(autonomy): 각 컴퓨터는 독립적으로 동작하며 상호 연결됨
- 패킷 교환(packet switching): 데이터를 패킷 단위로 분할하여 전달 — 회선 교환(circuit switching)과 대비됨
- 대역폭(bandwidth): 링크의 데이터 전송 속도를 나타내는 지표
- 확장성 문제: 모든 접속 ISP를 직접 연결하면 O(N²) 연결이 필요하여 계층적 구조가 필요함

## Relationships

- [[internet]] — 컴퓨터 네트워크의 가장 큰 구현체; 전 세계적으로 상호 연결된 "네트워크의 네트워크"
- [[network-protocol]] — 네트워크 내 통신 규칙을 정의하는 체계; 네트워크 동작의 근간
- [[internet-standards]] — 네트워크 프로토콜과 절차를 공식화하는 표준 체계

## Open Questions

- Peterson & Davie의 정의는 전화망 등 특수 목적 네트워크를 포함하는 반면, Tanenbaum은 범용 컴퓨터만을 대상으로 한다. 5G 코어망이나 IoT 전용망은 어느 정의에 속하는가?
- 클라우드(cloud)를 "특정되지 않은 네트워크 및 서버의 집합"으로 정의할 때, 현대의 cloud computing 개념과 어떻게 구분할 것인가?

## Sources

- raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf (pp.15–21)
