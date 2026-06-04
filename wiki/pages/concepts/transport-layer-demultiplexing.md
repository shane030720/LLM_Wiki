---
title: Transport Layer Demultiplexing
category: concept
tags: [transport-layer, demultiplexing, multiplexing, tcp, udp, networking, socket]
sources: [raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Transport Layer Demultiplexing(역다중화)은 수신 호스트가 도착한 transport-layer segment를 올바른 소켓(socket)으로 전달하는 과정이다. 반대로 Multiplexing(다중화)은 송신 호스트가 여러 소켓으로부터 데이터를 수집하고 transport 헤더를 붙여 network 계층으로 전달하는 과정이다. UDP는 destination 정보만을 이용하는 connectionless demultiplexing을, TCP는 4개의 식별자를 모두 사용하는 connection-oriented demultiplexing을 사용한다. 두 방식은 동일한 destination port를 가진 segment를 서로 다른 소켓으로 분리할 수 있는지 여부에서 본질적으로 다르다.

## How It Works

### Multiplexing (송신측)
송신 호스트는 여러 소켓으로부터 데이터를 수집하고 transport 헤더(source/destination port 번호 포함)를 추가하여 network 계층(IP)으로 내려보낸다. 이 헤더 정보가 수신측 역다중화에 사용된다.

### Connectionless Demultiplexing (UDP 방식)
- UDP 소켓 생성 시 목적지 IP 주소와 목적지 port 번호를 지정해야 한다.
- 수신 호스트는 도착한 UDP segment의 destination port 번호만을 확인하여 해당 포트의 소켓으로 segment를 전달한다.
- **동일한 destination port를 가진 UDP datagram은 source IP 주소나 source port 번호가 달라도 동일한 소켓으로 전달된다.**

### Connection-oriented Demultiplexing (TCP 방식)
RFC 793에 따르면 소켓, 시퀀스 번호, 윈도우 크기 등 각 데이터 스트림의 상태 정보 조합을 connection이라 한다. TCP는 다음 4-tuple로 소켓을 유일하게 식별한다:

1. Source IP address
2. Source port number
3. Destination IP address
4. Destination port number

수신 호스트는 이 4-tuple 모두를 사용하여 TCP segment를 해당 소켓으로 전달한다. 그 결과 서버는 동일한 destination IP·port(예: 포트 80)로 들어오는 여러 TCP segment를 서로 다른 소켓으로 역다중화할 수 있다. 각 소켓은 서로 다른 클라이언트와의 연결에 대응한다.

### 포트 번호와 소켓의 관계
- 각 segment는 source port와 destination port를 포함한다.
- IP 주소와 포트 번호의 조합을 endpoint 또는 socket이라 한다(TCP 문헌 및 RFC 793에서 유래).
- 한 쌍의 socket(local socket + remote socket)이 각 TCP connection을 유일하게 식별한다.
- 이 개념은 네트워크 트래픽 모니터링에서 연결 추적의 핵심이다.

## Key Properties

- **UDP**: 2-tuple(dest IP, dest port)로 역다중화. 서로 다른 출처의 데이터라도 같은 port이면 동일 소켓으로 수렴한다.
- **TCP**: 4-tuple(src IP, src port, dest IP, dest port)로 역다중화. 동일한 destination port를 가진 segment라도 출처가 다르면 서로 다른 소켓으로 분리된다.
- "Connection-oriented"와 "connectionless"라는 용어는 1981년 Lyman Chapin과 John Gurzick이 OSI reference model connectionless addendum 초안 작성 중 만들어낸 것이다(Piscitello & Chapin, 1993).
- 각 소켓은 독립적으로 식별되므로, 서버 하나가 수천 개의 동시 TCP 연결을 유지할 수 있다.
- Host는 IP datagram을 수신하면 그 안의 segment에서 port 번호를 추출하여 올바른 소켓으로 전달한다.

## Relationships

- [[multiplexing]] (다중화는 역다중화의 반대 과정이며, 동일한 전송 계층에서 함께 수행됨)
- [[tcp]] (4-tuple 기반 connection-oriented demultiplexing을 사용하는 프로토콜)
- [[udp]] (2-tuple 기반 connectionless demultiplexing을 사용하는 프로토콜)
- [[tcp-header]] (Source Port, Destination Port 필드가 역다중화의 핵심 식별자)
- [[osi-reference-model]] (connection-oriented / connectionless 용어가 처음 정의된 맥락)

## Open Questions

- 동일한 destination port로 들어오는 수많은 TCP 연결을 서버가 효율적으로 관리하기 위한 소켓 테이블 구현(예: connection table 크기, 4-tuple lookup 속도)은 고성능 서버 설계에서 중요한 엔지니어링 과제로 남아 있다.
- 같은 4-tuple을 가진 TCP 연결이 재수립되는 경우(TIME_WAIT 상태 이후) 이전 연결의 지연 도착 segment와 새 연결의 segment를 어떻게 구별할 것인지는 TCP 구현의 세부 과제다.

## Sources

- raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf
