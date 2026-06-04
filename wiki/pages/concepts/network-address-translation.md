---
title: Network Address Translation (NAT)
category: concept
tags: [networking, NAT, IPv4, addressing, security, middlebox]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Network Address Translation (NAT, 네트워크 주소 변환)은 로컬 네트워크의 사설(private) IP 주소와 포트 번호를 단일 공인(public) IP 주소로 투명하게 매핑하는 기법이다. 외부 인터넷에서는 NAT 라우터 뒤의 모든 기기가 단 하나의 IPv4 공인 주소를 공유하는 것처럼 보인다.

## How It Works

### 변환 과정
1. **발신 데이터그램 변환(Outgoing)**:
   - NAT 라우터는 내부 호스트의 (출발지 IP, 포트)를 (NAT 공인 IP, 새 포트)로 대체
   - 변환 쌍을 NAT 변환 테이블에 기록
2. **응답 데이터그램 역변환(Incoming)**:
   - 외부에서 (NAT 공인 IP, 새 포트)로 수신된 패킷을 변환 테이블에서 조회
   - 저장된 (내부 호스트 IP, 원래 포트)로 목적지 주소를 복원하여 전달

구체적 흐름 예시:
```
내부: 10.0.0.1:3345 → 외부: 128.119.40.186:80
  NAT 변환: (10.0.0.1, 3345) ↔ (138.76.29.7, 5001)
발신: src=138.76.29.7:5001, dst=128.119.40.186:80
응답: src=128.119.40.186:80, dst=138.76.29.7:5001
  역변환 → dst=10.0.0.1:3345 로 복원 후 내부 전달
```

### 사용하는 사설 주소 공간
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

이 주소들은 인터넷에서 라우팅되지 않으므로 내부 전용으로 자유롭게 사용된다.

## Key Properties
- 내부 기기들이 단 하나의 공인 IP 주소를 공유 가능 (IPv4 주소 절약)
- 포트 번호를 활용하여 여러 내부 호스트를 구별 (PAT, Port Address Translation이라고도 함)
- 로컬 네트워크 주소 변경 시 외부에 통보 불필요
- ISP 변경 시 내부 주소 변경 불필요
- 보안: 내부 기기가 외부에서 직접 접근 불가 (단방향 연결 개시만 가능)

### 논란 사항
- 라우터는 원칙적으로 네트워크 계층(layer 3)까지만 처리해야 하나, NAT는 포트 번호(transport layer, layer 4)를 수정
- [[end-to-end-argument]] 위반: 네트워크 레이어 기기가 엔드포인트 식별자(포트 번호)를 조작
- **NAT Traversal 문제**: NAT 뒤에 있는 서버에 외부 클라이언트가 직접 연결하기 어려움 (STUN/TURN/ICE 등으로 우회)
- IPv4 주소 부족 문제의 근본적 해결책은 IPv6이나, NAT 존재가 IPv6 전환 인센티브를 약화시킴

### 현실
- 가정, 기업, 4G/5G 셀룰러 네트워크에 광범위하게 사용 중
- "NAT is here to stay"

## Relationships
- [[ipv4-special-purpose-addresses]] — NAT에서 사용되는 사설 주소 범위
- [[end-to-end-argument]] — NAT가 위반하는 인터넷 설계 원칙
- [[middlebox]] — NAT는 대표적인 미들박스
- [[network-layer]] — NAT가 동작하는 계층 (layer 3-4 경계)
- [[transport-layer-demultiplexing]] — NAT의 포트 번호 조작과 관련된 transport layer 기능
- [[ipv6-tunneling]] — IPv6 전환으로 NAT 의존도를 줄이려는 시도

## Open Questions
- NAT Traversal: STUN, TURN, ICE 등 우회 기법이 복잡성을 크게 증가시킨다. IPv6 보급이 충분해지면 이 문제가 자연히 해결될 수 있는가, 아니면 NAT는 보안 목적으로 IPv6 환경에서도 유지될 것인가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
