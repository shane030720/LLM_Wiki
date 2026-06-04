---
title: Internet
category: entity
tags: [internet, isp, tier1, ixp, history, infrastructure, cloud]
sources: [raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Internet(대문자 'I')은 전 세계적으로 상호 연결된 ISP(Internet Service Provider)들의 집합으로, "네트워크의 네트워크(network of networks)"라 불린다. 소문자 internet은 임의의 상호 연결 네트워크를 지칭하고, 대문자 Internet은 현재 운영 중인 공개 인터넷을 가리킨다. 공개 인터넷(public Internet)과 사설 인트라넷(private intranet)은 구분된다. 2023년 기준 약 150억 개의 장치가 연결되어 있다.

**역사적 발전 연대기:**

- **1961–1972 (패킷 교환 원리 태동)**: Kleinrock의 큐잉 이론이 패킷 교환의 효율성을 이론적으로 증명. 1964년 Baran이 군사 네트워크에서 패킷 교환 개념 제안. 1967년 ARPA(Advanced Research Projects Agency)가 ARPAnet 구상. 1969년 첫 ARPAnet 노드 운영. 1972년 NCP(Network Control Protocol) 도입 및 최초 이메일 프로그램 등장. 당시 ARPAnet은 15개 노드.
- **1972–1980 (인터네트워킹 태동)**: 1970년 하와이에서 ALOHAnet 위성 네트워크 운영. 1974년 Cerf와 Kahn이 네트워크 상호 연결 아키텍처 제안. 1976년 Ethernet이 Xerox PARC에서 개발. 1979년 ARPAnet 200 노드 달성. Cerf & Kahn의 설계 원칙(최소주의·자율성, best-effort 서비스, stateless 라우팅, 분산 제어)이 현재 인터넷 아키텍처의 토대를 이룸.
- **1980–1990 (프로토콜 표준화)**: 1983년 TCP/IP 배포, DNS 정의. 1982년 SMTP 이메일 프로토콜 정의. 1985년 FTP 프로토콜 정의. 1988년 TCP 혼잡 제어(congestion control) 도입. 국가 네트워크(CSnet, BITnet, NSFnet 등)가 확산되어 10만 개 이상의 호스트가 연결됨.
- **1990–2000s (상업화 및 웹의 등장)**: ARPAnet 해체. Berners-Lee가 HTML/HTTP 기반 웹(WWW) 개발(Bush의 1945년 하이퍼텍스트 개념 계승). 1994년 NCSA Mosaic, 이후 Netscape 브라우저 등장. 1990년대 후반 웹 상업화. 2000년 닷컴 버블. P2P 파일 공유, 인스턴트 메시징 등 killer app 등장. 네트워크 보안이 전면으로 부상. 약 5천만 호스트, 1억 명 이상 사용자. 백본 링크가 Gbps 속도에 도달.
- **2005–현재 (규모·SDN·모바일·클라우드)**: 광대역 가정용 접속(10–100 Mbps) 확산. 2008년 SDN(Software-Defined Networking) 등장. 4G/5G, WiFi 고속 무선 접속 보편화. Google, Meta, Microsoft 등 대형 서비스 사업자가 자체 네트워크를 구축하여 Tier-1·Regional ISP를 우회. 기업들의 클라우드(AWS, Azure 등) 서비스 확산. 2017년 인터넷 연결 모바일 장치 수가 고정 장치 수를 초과.

## Capabilities

- **분산 애플리케이션 인프라**: 웹(Web), VoIP, 이메일, 게임, e-commerce, 파일 공유 등 다양한 응용을 지원하는 통신 인프라
- **신뢰성 있는 데이터 전달(reliable data delivery)**: 출발지에서 목적지까지 손실 없이 전달 (TCP 기반)
- **Best-effort 데이터 전달**: 신뢰성을 보장하지 않는 전달 방식 (UDP 기반)
- **프로그래밍 인터페이스**: 애플리케이션이 인터넷 전송 서비스에 연결·사용할 수 있는 "hooks" 제공; 우편 서비스에 비유되는 서비스 옵션 제공
- **계층적 ISP 구조를 통한 전 세계 연결**: 어떤 두 호스트도 서로 패킷을 전달할 수 있는 경로 보장

**인터넷 구조 계층:**

| 계층 | 예시 | 역할 |
|------|------|------|
| Tier-1 ISP | Level 3, Sprint, AT&T, NTT | 국제·국가 규모 상업 ISP; 서로 peering |
| Regional ISP | 지역 통신사 | 지역 접속망과 Tier-1 ISP 연결 |
| Access ISP (Local ISP) | 가정·기업 인터넷 제공업체 | 최종 사용자의 인터넷 진입점 |
| IXP (Internet Exchange Point) | 과거 NAP(Network Access Point) | 여러 ISP가 직접 상호 연결(peering)하는 교환 지점 |
| Content Provider Network | Google, Meta, Akamai | 자체 사설 네트워크로 Tier-1 ISP 우회, 콘텐츠를 사용자 근처에 제공 |

## Limitations

- 접속 ISP 간 직접 연결은 O(N²) 연결을 요구하여 확장성 부재 → ISP 계층 구조와 IXP로 해결
- Best-effort 서비스 모델은 QoS(서비스 품질) 보장이 어렵고, 네트워크 혼잡 발생 가능
- 인터넷 구조는 경제적 논리와 국가 정책에 의해 진화하여 설계 일관성 부족
- 자발적 프로토콜 준수에 의존하므로 보안 취약점이 구조적으로 내재될 수 있음

## Relationships

- [[computer-network]] — 인터넷은 컴퓨터 네트워크의 가장 큰 구현체
- [[network-protocol]] — TCP, IP, HTTP, DNS, SMTP 등 수많은 프로토콜 위에서 동작
- [[internet-standards]] — IETF RFC를 통한 자발적 표준 준수가 인터넷 운영의 기반

## Sources

- raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf (pp.22–40)
