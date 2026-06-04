---
title: TCP/IP Architecture
category: concept
tags: [networking, tcp-ip, internet, layering, hourglass, end-to-end, rfc]
sources: [raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP/IP 아키텍처는 인터넷의 기반이 되는 프로토콜 스택 아키텍처로, RFC 1122에서 정의한 인터넷 아키텍처를 구현한다. 현대 교재(Tanenbaum, Kurose/Ross, Stallings, Forouzan)에서는 5계층 하이브리드 모델(Application, Transport, Network/Internet, Link, Physical)로 표현되며, IP(Internet Protocol)가 좁은 허리(narrow waist)를 형성하는 모래시계(Hourglass) 구조를 가진다. 장애 대응 견고성(robustness)과 다양한 네트워크에 대한 유연성(flexibility)을 설계 원칙으로 삼는다.

## How It Works

**5계층 구조 (Kurose/Ross 기준):**

| 계층 | 역할 | 대표 프로토콜 | PDU |
|------|------|-------------|-----|
| Application | 네트워크 애플리케이션 지원 | HTTP, IMAP, SMTP, DNS | Message |
| Transport | 프로세스-투-프로세스 데이터 전달 | TCP, UDP | Segment / Datagram |
| Network (Internet) | 출발지에서 목적지로 데이터그램 라우팅 | IP, 라우팅 프로토콜 | Packet (IP Datagram) |
| Link | 인접한 네트워크 요소 간 데이터 전달 | Ethernet, 802.11(WiFi), PPP | Frame |
| Physical | 물리 매체 상의 비트 전송 | (코딩 방식) | Bit |

중간 노드별 계층 구현 범위:
- 라우터(router): Link + Network 계층까지 처리
- 호스트(host): 전체 5계층 처리

**Hourglass Model (모래시계 모델):**

IP가 좁은 허리(narrow waist)를 형성하여 상위/하위를 연결한다:
- 상위: FTP, HTTP, TFTP, DNS 등 다양한 응용 프로토콜이 TCP 또는 UDP를 통해 IP를 공유
- 허리: IP — 단일 공통 네트워크 계층
- 하위: Ethernet, WiFi, SONET 등 다양한 링크 기술이 IP 아래에 위치

IP는 서로 다른 링크 계층 프로토콜을 사용하는 서브네트워크(subnetwork) 간 상호연결을 가능하게 하며, 호스트-투-호스트 메시지 전달 문제를 프로세스-투-프로세스 서비스 문제와 완전히 분리한다.

**End-to-End vs. Hop-by-Hop:**

특정 프로토콜 기능을 구현하는 두 가지 방식:
- End-to-End (E2E): 기능을 통신 종단(source/destination)에서만 구현
- Hop-by-Hop (HBH): 각 라우터(hop)에서 기능을 수행
- 참고: 인터넷에서 'hop'은 일반적으로 라우터에 의한 store-and-forward 작업의 한 발생을 의미

## Key Properties

- **엄격한 레이어링을 강제하지 않음**: 일부 애플리케이션은 정의된 전송 계층을 우회하고 직접 IP 또는 서브네트워크를 사용할 수 있다.
- **RFC 1958 아키텍처 원칙** ("목표, 도구, 지능"):
  - 목표(goal): 연결성(connectivity)
  - 도구(tool): IP(Internet Protocol)
  - 지능(intelligence): 종단(end-to-end), 네트워크 내부가 아님
- **설계 철학** (David D. Clark, 1988 ACM SIGCOMM):
  - "We reject kings, presidents, and voting. We believe in rough consensus and running code."
- **새 프로토콜 제출 요건**: 프로토콜 명세(specification)와 최소 하나(가능하면 둘)의 구현체(implementation)가 필요
- **4계층 모델과의 차이**: 일부 교재(RFC 1122 원본)는 Link + Physical을 합쳐 4계층으로 표현; 현대 교재는 5계층 하이브리드 모델 사용

## Relationships

- [[osi-reference-model]] — OSI 7계층 모델과 비교되는 실용적 인터넷 아키텍처; Session/Presentation Layer 없음
- [[protocol-layering]] — TCP/IP는 프로토콜 레이어링 기법의 실제 구현이며, 비엄격 레이어링의 대표 사례
- [[internet]] — TCP/IP는 인터넷의 기반 프로토콜 스택; 인터넷 아키텍처의 핵심 설계 원칙을 구현
- [[network-addressing]] — TCP/IP의 각 계층은 MAC 주소(Link), IP 주소(Network), 포트 번호(Transport) 사용
- [[internet-standards]] — RFC 1122, RFC 1958 등 IETF RFC를 통해 아키텍처 원칙이 문서화됨

## Open Questions

- End-to-end argument의 현대적 적용: NAT, CDN, 미들박스(middlebox), 5G 네트워크의 확산으로 순수한 E2E 원칙이 얼마나 유효한가?
- Hourglass 구조가 IPv6 전환, QUIC, 새로운 네트워크 아키텍처 도입을 얼마나 저해하는가?
- "rough consensus and running code" 원칙이 현대의 대규모 인터넷 거버넌스에서 여전히 작동하는가?
- 5계층 모델과 원래의 4계층 모델(Link = Data Link + Physical) 중 어느 것이 현대 네트워크를 더 잘 설명하는가?

## Sources

- raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf
