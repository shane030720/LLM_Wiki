---
title: TCP Server Operation
category: concept
tags: [tcp, server, connection-queue, port, backlog, socket]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP 서버가 들어오는 연결을 처리하는 방식의 총체. 포트 번호 관리, 4-tuple 기반의 동시 연결 식별, 연결 큐(incoming connection queue) 관리를 포함한다.

## How It Works

**동시 처리 서버 모델**

대부분의 TCP 서버는 동시(concurrent) 처리 방식을 사용한다:
- 새 연결 요청이 도착하면 서버는 연결을 수락하고, 해당 클라이언트를 처리할 새 프로세스 또는 스레드를 생성
- 이를 통해 서버는 항상 다음 연결 요청을 받을 수 있는 상태 유지

**4-tuple 기반 연결 식별**

서버의 한 포트(예: 22번)로 여러 클라이언트가 동시에 연결될 수 있다. 각 연결은 4-tuple로 고유하게 식별된다:

```
(서버 IP, 서버 포트, 클라이언트 IP, 클라이언트 포트)
```

예시 (`netstat -a -n -t` 출력):
```
LISTEN:      :::22  :::*
ESTABLISHED: 165.246.43.170:22  163.152.162.146:16137
ESTABLISHED: 165.246.43.170:22  121.172.41.30:16140
```

서버 포트는 동일(22)하지만 클라이언트 엔드포인트가 달라 각 연결이 구분된다.

**연결 큐 (Incoming Connection Queue)**

OS는 내부적으로 **두 개의 연결 큐**를 관리한다:

1. **SYN_RCVD 큐**: TCP가 SYN+ACK를 보냈지만 앱이 아직 accept()하지 않은 연결. `net.ipv4.tcp_max_syn_backlog`(기본값: 1000)로 크기 제어.

2. **ESTABLISHED 큐**: TCP의 3-way handshake가 완료되어 ESTABLISHED 상태이지만 앱이 아직 `accept()`를 호출하지 않은 연결. 앱이 `listen()` 호출 시 지정하는 **backlog** 값(0 ~ `net.core.somaxconn`, 기본값: 128)으로 크기 제어.

**Linux의 연결 큐 처리 규칙**

1. SYN 도착 시 `net.ipv4.tcp_max_syn_backlog` 초과 여부 확인. 초과 시 연결 거부.
2. ESTABLISHED 큐가 가득 찬 경우, TCP는 SYN에 즉시 응답하지 않고 앱이 `accept()`를 호출해 공간을 확보할 때까지 대기.
3. `net.ipv4.tcp_abort_on_overflow`가 설정된 경우, 큐 오버플로우 시 RST로 새 연결 거부 (기본값은 off; 일반적으로 권장하지 않음).

**중요한 함의**: Berkeley Sockets API에서 앱이 `accept()`를 통해 연결 도착 통보를 받을 때, TCP의 3-way handshake는 이미 완료된 상태.

**로컬 IP 주소 제한**

서버는 INADDR_ANY 대신 특정 로컬 IP를 바인딩할 수 있다. 이 경우 다른 IP로의 연결 요청은 TCP 모듈 수준에서 거부된다 (LISTEN 상태에서도 특정 IP만 허용).

**외부 엔드포인트 제한**

RFC 793의 추상 인터페이스는 특정 클라이언트만 수락하는 passive open을 지원하나, Berkeley Sockets API는 이를 직접 지원하지 않는다. 서버는 `accept()` 후 클라이언트 IP/포트를 확인하여 필터링해야 한다.

## Key Properties

- 서버의 well-known 포트(예: 22)가 여러 연결에서 공유될 수 있음 — 4-tuple이 연결을 고유 식별
- `netstat -a -n -t`로 서버의 모든 TCP 엔드포인트 상태 확인 가능
- ESTABLISHED 큐 크기(backlog)는 앱이 느릴 때 연결 폭발을 완충하는 버퍼 역할
- Modern Linux: backlog는 ESTABLISHED 연결 수만 제어 (전통적으로는 두 큐의 합)
- SYN Flood 공격은 SYN_RCVD 큐를 고갈시켜 정상 연결을 차단하는 방식으로 동작

## Relationships

- [[tcp-three-way-handshake]] (3-way handshake 완료 후 ESTABLISHED 큐에 진입)
- [[tcp-state-machine]] (LISTEN, SYN_RCVD, ESTABLISHED 상태가 큐 구조와 대응)
- [[tcp-reset-segment]] (큐 오버플로우 시 RST로 연결 거부하는 경우)
- [[transport-layer-demultiplexing]] (4-tuple 기반으로 패킷을 올바른 소켓으로 전달)
- [[tcp]] (TCP 서버의 전반적인 동작 원리)

## Open Questions

- backlog 값을 크게 설정하는 것이 SYN Flood 공격에 대한 부분적 방어가 될 수 있는가? SYN Cookie와 비교했을 때의 장단점은?
- `net.ipv4.tcp_abort_on_overflow`를 기본적으로 끄는 이유는? 큐가 찼을 때 RST 대신 침묵(silently drop)하는 것이 클라이언트 경험에 더 나은 이유는?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 56–62)
