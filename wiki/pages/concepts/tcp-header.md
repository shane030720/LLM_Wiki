---
title: TCP Header Structure
category: concept
tags: [tcp, header, protocol, networking, segment]
sources: [raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP Header는 TCP segment의 앞부분에 위치하는 제어 정보 블록으로, 기본 크기는 20바이트이며 옵션 포함 시 최대 60바이트까지 확장된다. 헤더에는 포트 번호, 시퀀스 번호, ACK 번호, 플래그, 윈도우 크기, 체크섬 등 TCP의 신뢰성·흐름 제어·연결 관리에 필요한 모든 제어 필드가 포함된다. TCP segment는 IP datagram에 캡슐화되어 전송된다.

## How It Works

TCP 헤더의 각 필드와 동작은 다음과 같다.

**Source Port / Destination Port** (각 16비트)
송신·수신 포트 번호를 나타낸다. IP 헤더의 주소와 결합하여 연결을 유일하게 식별하는 4-tuple을 구성한다. IP 주소와 포트 번호의 조합을 endpoint 또는 socket이라 하며(RFC 793), 이 개념이 Berkeley Sockets API의 기원이다. 한 쌍의 socket(local + remote)이 각 TCP connection을 유일하게 식별하므로 네트워크 트래픽 모니터링의 핵심 정보다.

**Sequence Number** (32비트)
해당 segment의 첫 번째 바이트가 전체 데이터 스트림에서 갖는 byte offset을 나타낸다. 패킷 번호가 아닌 바이트 단위 오프셋임에 주의한다. 0부터 2^32-1까지 사용하고 순환(wrap around)한다. 연결 수립 시 SYN segment는 무작위로 생성된 ISN(Initial Sequence Number)을 담으며, SYN bit 자체가 시퀀스 번호 1개를 소비한다. 따라서 첫 데이터 segment의 시퀀스 번호는 ISN + 1이다.

예시: 5,000바이트 파일을 1,000바이트씩 5개 segment로 전송하고 첫 바이트 번호가 10,001이면, 각 segment의 시퀀스 번호는 10001, 11001, 12001, 13001, 14001이다.

**Acknowledgment Number** (32비트)
수신자가 다음으로 수신하기를 기대하는 바이트의 시퀀스 번호(마지막으로 성공적으로 수신한 바이트 번호 + 1)를 나타낸다. ACK 비트가 설정된 경우에만 유효하며, 연결 수립 및 종료 segment를 제외한 대부분의 segment에서 유효하다. TCP는 원래 cumulative positive acknowledgment를 사용하는 sliding window 프로토콜로 정의된다. 현대 TCP에는 SACK(Selective Acknowledgment) 옵션이 추가되어 수신자가 순서 밖으로 받은 데이터를 발신자에게 알릴 수 있다.

**Header Length** (4비트)
헤더 길이를 32비트 워드 단위로 표현한다. Options 필드가 가변 크기이므로 이 필드가 필요하다. 4비트 제약으로 최대 60바이트 헤더가 허용된다.

**Flag Fields** (8비트)
구형 구현은 하위 6비트만 이해하나, 현재는 8비트 모두 사용된다.
- CWR(Congestion Window Reduced): 발신자가 전송 속도를 줄였음
- ECE(ECN Echo): 이전 혼잡 알림을 수신했음
- URG(Urgent): Urgent Pointer 필드가 유효함(거의 사용되지 않음)
- ACK(Acknowledgment): ACK Number 필드가 유효함(연결 수립 이후 항상 설정됨)
- PSH(Push): 수신자가 데이터를 즉시 애플리케이션에 전달해야 함(신뢰성 있게 구현·사용되지 않음)
- RST(Reset): 연결 초기화(보통 오류 발생 시 연결 강제 종료)
- SYN(Synchronize): 시퀀스 번호를 동기화하여 연결을 초기화
- FIN(Finish): 발신자가 해당 방향의 데이터 전송을 완료했음

**Window Size** (16비트)
ACK 번호부터 시작하여 수신자가 수용할 의향이 있는 바이트 수를 나타낸다. 흐름 제어(flow control)에 사용된다. 기본 최대값은 65,535바이트이나, Window Scale 옵션을 사용하면 고속·장거리 네트워크에서 더 큰 윈도우와 향상된 처리량을 달성할 수 있다.

**Checksum** (16비트)
TCP 헤더, 데이터, IP 헤더 일부를 포함한 pseudo-header를 대상으로 계산하는 오류 검출 코드다. 발신자 계산과 수신자 검증이 모두 필수(mandatory)이며, UDP의 pseudo-header 방식과 유사하다. Pseudo-header에는 source IP, destination IP, 프로토콜 번호(6), TCP 세그먼트 길이가 포함된다.

**Urgent Pointer** (16비트)
URG 비트가 설정된 경우에만 유효하다. Sequence Number 필드에 더하면 긴급 데이터의 마지막 바이트 시퀀스 번호를 구할 수 있는 양의 오프셋이다.

**Options** (가변 길이)
일반적인 옵션으로는 MSS(Maximum Segment Size), Timestamps, Window Scaling, Selective ACKs(SACK) 등이 있다.

**Data 부분 (선택적)**
TCP segment의 data 부분은 선택적(optional)이다. 헤더만 있는 순수 제어 segment는 연결 수립·종료, 데이터 ACK(pure ACK), 윈도우 업데이트(window update) 등에 사용된다.

## Key Properties

- 기본 헤더 크기 20바이트, 옵션 포함 최대 60바이트
- 4비트 Header Length 필드로 인해 최대 헤더 크기가 60바이트로 제한됨
- Checksum은 발신자 계산·수신자 검증이 모두 필수(mandatory)
- Sequence Number와 ACK Number는 패킷 번호가 아닌 byte offset 기반
- 연결 수립 이후 거의 모든 segment에 ACK 비트가 설정됨
- Pseudo-header를 통해 IP 계층 정보(주소 등)를 간접적으로 체크섬에 포함시켜 잘못된 라우팅 감지
- Window Size 필드만으로는 고속 네트워크에서 처리량이 제한되므로 Window Scale 옵션이 필요함

## Relationships

- [[tcp]] (이 헤더를 포함하는 TCP 프로토콜)
- [[transport-layer-demultiplexing]] (Source/Destination Port 필드가 역다중화의 핵심 식별자로 사용됨)
- [[multiplexing]] (포트 번호 필드가 다중화·역다중화의 기반)
- [[udp]] (UDP도 pseudo-header 방식의 체크섬을 사용하며 유사한 포트 번호 구조를 가짐)

## Open Questions

- TCP 체크섬(16비트)이 대용량 데이터 전송에서 충분한 오류 감지 능력을 갖추는지에 대한 논란이 존재한다(Stone & Partridge, 2000). 애플리케이션 수준의 강한 CRC나 미들웨어 계층(RFC 5044)을 추가로 적용해야 하는지 여부는 여전히 설계 시 고려 사항이다.
- Window Scale 옵션 없이는 16비트 Window Size 필드로 인해 고속·장거리 네트워크에서 처리량이 제한된다. 이는 TCP 설계 초기 인터넷 규모를 예측하지 못한 결과다.

## Sources

- raw/컴퓨터네트워크/Week 04 TCP Introduction.pdf
