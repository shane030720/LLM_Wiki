---
title: Network Layer
category: concept
tags: [network, routing, forwarding, data-plane, control-plane, sdn, best-effort]
sources: [raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Network Layer(네트워크 계층)는 인터넷 프로토콜 스택의 3계층으로, 송신 호스트에서 수신 호스트까지 데이터그램(datagram)을 end-to-end로 전달하는 역할을 담당한다. 인터넷에 연결된 모든 장치(호스트, 라우터)에 구현되어 있으며, IP(Internet Protocol)가 핵심 프로토콜이다. 송신 측은 세그먼트를 데이터그램으로 캡슐화하여 링크 계층으로 전달하고, 수신 측은 데이터그램을 열어 세그먼트를 전송 계층으로 전달한다.

## How It Works

### 두 가지 핵심 기능

- **Forwarding(포워딩)**: 라우터의 입력 링크로 들어온 패킷을 적절한 출력 링크로 이동시키는 로컬·단일 교환기 수준의 동작
- **Routing(라우팅)**: 출발지에서 목적지까지 패킷이 취할 경로 전체를 결정하는 네트워크 전체 수준의 동작; 라우팅 알고리즘이 사용됨

### Data Plane vs Control Plane

| 구분 | 범위 | 역할 |
|------|------|------|
| Data Plane | 라우터 단위 (로컬) | 입력 포트에 도착한 데이터그램을 출력 포트로 포워딩하는 방법 결정 |
| Control Plane | 네트워크 전체 | 출발지 호스트에서 목적지 호스트까지의 end-to-end 경로 결정 |

### Control Plane 구현 방식

1. **Per-router control plane**: 각 라우터에 라우팅 알고리즘 컴포넌트가 내장되어 라우터 간 상호 협력으로 포워딩 테이블을 계산하는 전통적 방식
2. **Software-Defined Networking (SDN)**: 원격 컨트롤러(Remote Controller)가 모든 라우터의 포워딩 테이블을 중앙에서 계산한 뒤 각 라우터에 설치; 제어와 데이터 평면이 분리됨

### Best-Effort Service Model

인터넷 네트워크 계층은 "best-effort" 서비스 모델을 채택한다:

- 데이터그램의 성공적 전달 **보장 없음**
- 전달 타이밍·순서 **보장 없음**
- 사용 가능 대역폭 **보장 없음**
- ATM의 CBR(Constant Bit Rate), ABR(Available Bit Rate), Intserv(RFC 1633), Diffserv(RFC 2475) 같은 QoS 모델과 대비됨

Best-effort가 성공한 이유:
- 메커니즘의 단순성 → 광범위한 배포 및 채택 가능
- 충분한 대역폭 프로비저닝으로 실시간 애플리케이션(인터랙티브 음성, 영상)도 "대부분의 경우" 수용 가능한 성능 제공
- CDN·데이터센터 복제 등 애플리케이션 계층 분산 서비스가 보완
- TCP 혼잡 제어가 탄성(elastic) 트래픽 조절에 기여

## Key Properties

- 인터넷의 모든 호스트와 라우터에 구현됨
- 라우터는 통과하는 모든 IP 데이터그램의 헤더 필드를 검사
- IP는 비신뢰적(unreliable), 비연결형(connectionless) 데이터그램 서비스를 제공
- 신뢰성·순서 보장이 필요하면 상위 전송 계층(TCP 등)이 책임
- SDN에서는 컨트롤 에이전트(CA)가 라우터에 상주하며 원격 컨트롤러와 통신

## Relationships

- [[osi-reference-model]] — 네트워크 계층이 정의된 참조 모델 (Layer 3)
- [[tcp-ip-architecture]] — 인터넷 프로토콜 스택 내 네트워크 계층의 위치
- [[ipv4-datagram]] — 네트워크 계층의 프로토콜 데이터 단위
- [[internet]] — best-effort 네트워크 계층 위에 구축된 글로벌 인터넷
- [[tcp-congestion-control]] — 네트워크 계층 best-effort의 한계를 상위 계층에서 보완하는 예
- [[protocol-layering]] — 계층별 서비스 모델과 인터페이스 정의

## Open Questions

- SDN의 중앙화된 컨트롤러는 단일 장애점(single point of failure) 문제를 어떻게 해결하는가?
- Best-effort만으로 5G·IoT 시대의 초저지연 애플리케이션(자율주행, 원격 의료)의 QoS를 충분히 보장할 수 있는가?
- Intserv(RFC 1633)와 Diffserv(RFC 2475) 같은 QoS 메커니즘이 왜 인터넷에서 널리 채택되지 않았는가?

## Sources

- raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf
