---
title: OSI Reference Model
category: concept
tags: [networking, osi, layering, standard, iso, 7-layer, pdu]
sources: [raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

OSI(Open Systems Interconnection) 참조 모델은 ISO(국제표준화기구)가 개발한 7계층 네트워크 아키텍처 프레임워크로, 개방형 시스템(open systems) 간 통신을 위한 개념적 상호작용 방법론을 정의한다. 각 계층은 Service(네트워크 기능), Interface(프로토콜 조작 방법), Protocol(서비스 구현체)로 기술되며, 하위 계층 서비스에만 의존하여 상위 계층에 더 추상적인 서비스를 제공하는 수직적 프로토콜 스택 구조를 가진다.

## How It Works

7개 계층이 아래(Physical)에서 위(Application)로 쌓이며, 각 계층은 하위 계층 서비스를 이용해 상위 계층에 서비스를 제공한다.

**Layer 1 — Physical Layer**
- Service: 물리적 링크로 연결된 두 시스템 사이에서 정보를 이동
- Interface: 비트 하나를 전송하는 방법 명세
- Protocol: 비트 표현 코딩 방식, 전압 레벨, 비트 지속 시간
- 예: 동축 케이블(coaxial cable), 광섬유 링크(optical fiber), 송수신기(transmitter/receiver)

**Layer 2 — Data Link Layer**
- Service: Framing(데이터 시작/끝 표시), 로컬 주소 지정 및 전달(동일 물리 매체에 연결된 피어 간 데이터 프레임 전달); 선택적으로 공유 매체 접근(shared media access), 신뢰적 전송(재전송)
- Interface: 동일 물리 매체에 연결된 기기로 데이터 단위(패킷) 전송
- Protocol: MAC 주소(MAC addresses), MAC(Media Access Control) 구현
- 예: Ethernet, IEEE 802.11
- PDU: Frame (헤더와 트레일러 모두 부착)

**Layer 3 — Network Layer**
- Service: 지정된 목적지로 패킷 전달, 세그멘테이션/재조립(fragmentation/defragmentation); 선택적으로 패킷 스케줄링, 버퍼 관리
- Interface: 주어진 목적지로 패킷 전송
- Protocol: 전역 유일 주소(globally unique addresses), 라우팅 테이블 구성, 목적지 방향으로 패킷 포워딩
- 예: IP(Internet Protocol)
- PDU: Packet / Datagram

**Layer 4 — Transport Layer**
- Service: 오류 없는 흐름 제어 종단간 연결 제공, 다수의 전송 연결을 하나의 네트워크 연결로 다중화(multiplex)
- Interface: 특정 목적지로 패킷 전송
- Protocol: 신뢰성(reliability) 및 흐름 제어(flow control) 구현
- 예: TCP(Transmission Control Protocol), UDP(User Datagram Protocol)
- PDU: Segment

**Layer 5 — Session Layer**
- Service: 세션 관리(session management), 오디오/비디오 스트림 간 동기화(synchronization)
- Protocol: 양방향 연결 설정/해제(full duplex connection setup/teardown), 재시작 및 체크포인팅, 세션 간 동기화
- 예: SMIL(Synchronized Multimedia Integration Language)

**Layer 6 — Presentation Layer**
- Service: 데이터 형식 변환(data format conversion)
- Protocol: 데이터 형식 정의 및 형식 간 변환 규칙
- 예: NFS의 XDR(External Data Representation), 플랫폼 독립적 RPC 인터페이스
- 참고: NFS는 TCP/IP 모델에서는 애플리케이션 계층 프로토콜로 분류됨

**Layer 7 — Application Layer**
- Service: 최종 사용자(end user)에게 임의의 서비스 제공
- Protocol: 애플리케이션에 따라 상이
- 예: SMTP, BitTorrent, SSH, HTTP(Web)
- PDU: Message

**Protocol Data Units (PDU):**

상위 계층 데이터를 처리할 때 데이터를 특정 단위로 분할하여 처리한다. 계층별 PDU 명칭:

| 계층 | PDU 명칭 | 특이사항 |
|------|---------|---------|
| Physical | Bit | - |
| Data Link | Frame | 헤더(Header)와 트레일러(Trailer) 모두 부착 |
| Network | Packet / Datagram | 헤더만 부착 |
| Transport | Segment | 헤더만 부착 |
| Application | Message | 헤더 없음(데이터 자체) |

중간 노드(라우터 등)는 해당 계층까지만 PDU를 처리하며, 상위 계층 PDU는 불투명(opaque)하게 취급한다.

## Key Properties

- OSI 모델(model)과 OSI 프로토콜 스택(protocol stack)은 구분된다: 모델은 개념적 상호작용 방법론이며, 프로토콜 스택(CONP, CLNP, X.400, X.500 등)은 이 모델을 준수하는 구체적 프로토콜 명세
- 오늘날 인터넷에서는 OSI 프로토콜 스택 대신 TCP/IP 스택이 실질적으로 사용됨
- Session Layer(5)와 Presentation Layer(6)는 TCP/IP 5계층 모델에서 Application Layer로 통합
- 각 계층은 Service / Interface / Protocol의 세 요소로 기술 가능
- 장치별 계층 구현 범위: 라우터는 Network Layer(1-3)까지, 스위치는 Data Link Layer(1-2)까지, 종단 호스트는 전체 7계층

## Relationships

- [[protocol-layering]] — OSI 모델은 프로토콜 레이어링 기법을 7계층으로 표준화한 구현체
- [[tcp-ip-architecture]] — TCP/IP는 OSI 7계층 대비 5계층(또는 4계층)으로 단순화된 실용적 인터넷 아키텍처
- [[network-addressing]] — Physical Layer는 MAC 주소, Network Layer는 IP 주소, Transport Layer는 포트 번호를 사용
- [[network-protocol]] — 각 계층의 프로토콜은 service interface와 peer interface를 정의

## Open Questions

- Session Layer와 Presentation Layer의 기능이 현대 인터넷 애플리케이션(TLS, QUIC 등)에서 어느 계층에서 처리되는가? TCP/IP 모델에서는 애플리케이션 계층에 통합되지만, 기능적으로는 여러 계층에 걸쳐있다.
- OSI 프로토콜 스택이 실패하고 TCP/IP가 실질적 표준으로 승리한 이유는 무엇인가? (기술적 단순성, 시장 타이밍, "rough consensus and running code" 문화 등)
- NFS XDR이 Presentation Layer 프로토콜로 분류되지만 실제로는 Application Layer에서 구현되는 것처럼, 계층 분류와 실제 구현 위치 사이의 불일치를 어떻게 볼 것인가?

## Sources

- raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf
