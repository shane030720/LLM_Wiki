---
title: Longest Prefix Matching
category: concept
tags: [networking, routing, forwarding, algorithm, TCAM]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Longest Prefix Matching(최장 프리픽스 매칭, LPM)은 IP 포워딩 테이블에서 목적지 주소와 매칭되는 항목이 여러 개일 때, 가장 긴(가장 구체적인) prefix를 가진 항목을 선택하여 포워딩 결정을 내리는 알고리즘이다. [[cidr]] 기반 인터넷 라우팅에서 필수적으로 사용된다.

## How It Works
1. 포워딩 테이블의 각 항목은 목적지 prefix와 출력 링크 인터페이스를 매핑한다.
2. 수신된 패킷의 목적지 IP 주소를 각 테이블 항목의 prefix와 비트 단위로 비교한다.
3. 매칭되는 항목이 여러 개이면, prefix 길이가 가장 긴 항목을 선택한다.
4. 매칭되는 항목이 없으면 default 경로(0.0.0.0/0)를 사용한다.

예시 포워딩 테이블:
```
Destination Address Range          Interface
11001000 00010111 00010***          0
11001000 00010111 00011000          1
11001000 00010111 00011***          2
otherwise                           3
```

- 목적지 `11001000 00010111 00011000 10101010`:
  - Interface 1 prefix (24비트)와 Interface 2 prefix (21비트) 모두 매칭
  - 더 긴 prefix (24비트) 선택 → Interface 1로 포워딩

- 목적지 `11001000 00010111 00010110 10100001`:
  - Interface 0 prefix (21비트) 매칭
  - → Interface 0으로 포워딩

### 하드웨어 구현: TCAM
- **TCAM (Ternary Content Addressable Memory)**: 0, 1, don't-care(*)의 세 가지 값으로 동시 비교 가능
- 테이블 크기와 무관하게 단 1 클록 사이클에 조회 완료 (content addressable)
- Cisco Catalyst: ~1M 라우팅 테이블 항목을 TCAM에 저장
- 소프트웨어 구현 대비 압도적으로 빠른 조회 속도 (메모리 기반 trie와 비교)

## Key Properties
- [[cidr]] 환경의 가변 길이 prefix를 올바르게 처리하기 위한 필수 알고리즘
- prefix 길이가 길수록 더 구체적이고 우선순위가 높음
- [[route-aggregation]] 에서 집약 경로와 구체적 경로가 공존할 때 올바른 포워딩 보장
- TCAM으로 O(1) 시간 조회 가능
- IP 포워딩은 hop-by-hop 기반으로, 각 라우터가 독립적으로 LPM 수행

## Relationships
- [[cidr]] — LPM이 필요한 가변 길이 prefix 체계
- [[route-aggregation]] — 집약 경로와 구체적 경로 간 우선순위를 LPM이 결정
- [[ip-forwarding]] — LPM이 사용되는 포워딩 과정
- [[router-architecture]] — LPM이 수행되는 입력 포트; TCAM이 구현

## Open Questions
- IPv6에서 128비트 주소에 대한 TCAM 용량과 전력 소비 문제가 있다. 소프트웨어 기반 LPM(patricia trie 등)과의 성능/전력 trade-off를 어떻게 최적화할 것인가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
