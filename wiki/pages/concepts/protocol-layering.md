---
title: Protocol Layering
category: concept
tags: [networking, layering, protocol, encapsulation, abstraction, service, interface]
sources: [raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Protocol Layering은 네트워크 기능을 순서가 있는 계층적 추상화 집합으로 조직화하는 소프트웨어 공학적 기법이다. 각 계층(layer)은 직접 하위 계층이 제공하는 서비스에만 의존하며, 자신은 상위 계층에 더 추상적인 서비스를 제공한다. 네트워크 통신의 복잡성을 지적으로 관리 가능한 단위로 분해하고, 하위 계층의 구현 세부사항을 은닉(black box)하여 모듈화를 달성한다.

## How It Works

**레이어링의 동기:**
단일 엔티티(프로그램)에 모든 네트워크 기능을 구현하는 것은 과도하게 복잡하며, 전문화된 환경(예: 청각/시각 장애 상황)에 필요한 추가 기능을 유연하게 수용하기 어렵다. 레이어링은 통신 기능의 순차적 특성(sequential nature)과 흑박스(black box) 추상화의 단순성 때문에 네트워크 분해(decomposition)에 특히 적합하다.

**핵심 개념:**

- **Service**: 한 계층이 바로 상위 계층에 제공하는 기능의 집합(primitives)
  - Ethernet: 비신뢰적 서브넷 유니캐스트/멀티캐스트/브로드캐스트 데이터그램 서비스
  - IP: 비신뢰적 종단간(end-to-end) 유니캐스트 데이터그램 서비스
  - TCP: 신뢰적 종단간 양방향 바이트 스트림 서비스

- **두 종류의 인터페이스**: 각 프로토콜은 두 가지 인터페이스를 정의한다
  - **Service interface**: 로컬 객체가 해당 프로토콜에 수행할 수 있는 작업을 정의
  - **Peer interface**: 동일 계층의 프로토콜 피어(peer) 간에 교환되는 메시지의 형식과 의미를 정의

- **Protocol Graph**: 상위-하위 계층 프로토콜 간 메시지 전달 관계가 만들어내는 그래프. 하드웨어 레벨을 제외한 대부분의 피어-투-피어 통신은 간접적으로 이루어지며(하위 계층 프로토콜에 메시지를 전달함으로써), 이 의존 관계가 그래프를 형성한다.

- **Encapsulation/Decapsulation**: 각 계층은 데이터에 헤더(header, 일부 계층은 트레일러(trailer)도 추가)를 붙여 하위 계층으로 전달하고, 수신 측 동일 계층에서 이를 제거한다. Protocol graph의 각 레벨에서 반복된다.

## Key Properties

- **Layer N invariant**: "목적지의 Layer N은 출발지 Layer N이 전송한 메시지의 정확한 사본(exact copy)을 수신한다. 출발지의 하위 계층이 추가한 헤더 및 모든 수정사항은 목적지의 하위 계층이 제거해야 한다."
- 각 계층은 직접 하위 계층이 제공하는 서비스만 사용할 수 있다 (인접 계층 원칙).
- 두 저자(Tanenbaum vs. Peterson & Davie)의 프로토콜 정의는 다르지만, service interface와 peer interface라는 핵심 요소는 공통으로 포함된다.
- Protocol 정의 (Tanenbaum): "같은 계층 내 피어 엔티티들이 교환하는 패킷 또는 메시지의 형식과 의미를 규정하는 규칙 집합"
- Protocol 정의 (Peterson & Davie): "서비스 인터페이스(service interface)와 피어 인터페이스(peer interface)를 동시에 정의하는 추상 객체"

## Relationships

- [[osi-reference-model]] — OSI 7계층 모델은 프로토콜 레이어링 기법을 표준화한 대표적 구현체
- [[tcp-ip-architecture]] — TCP/IP는 프로토콜 레이어링을 실용적으로 구현한 인터넷 아키텍처; 엄격한 레이어링을 강제하지 않음
- [[network-protocol]] — 프로토콜은 레이어링의 기본 구성 단위; service interface와 peer interface로 구성
- [[network-addressing]] — 각 계층은 서로 다른 주소 체계(물리/논리/포트)를 사용하여 식별을 수행

## Open Questions

- 엄격한 레이어링(strict layering)과 유연한 레이어링 중 어느 것이 더 적합한가? TCP/IP는 엄격한 레이어링을 강제하지 않으며 일부 앱이 IP를 직접 사용한다.
- SDN(Software-Defined Networking), NFV(Network Function Virtualization) 등 현대 기술에서 전통적 계층 모델의 경계가 흐려지고 있는데, 레이어링 모델은 여전히 유효한가?
- Peterson & Davie 정의에서 "프로토콜은 추상 객체"라는 관점과 Tanenbaum의 "규칙 집합"이라는 관점 중 어느 쪽이 현대 네트워크 구현을 더 잘 설명하는가?

## Sources

- raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf
