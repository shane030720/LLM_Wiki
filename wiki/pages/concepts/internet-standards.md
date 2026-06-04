---
title: Internet Standards and Standardization
category: concept
tags: [standard, ietf, rfc, w3c, ieee, sdo, de-facto, de-jure]
sources: [raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Standard(표준)은 "어떤 것을 수행하는 방식에 대해 널리 합의된 방법"이다. 인터넷 표준(Internet Standard)은 IETF(Internet Engineering Task Force)가 작성·발행하며, 자율적으로 상호 연결된 네트워크들의 국제 협력체인 인터넷이 개방형 프로토콜과 절차에 대한 자발적 준수(voluntary adherence)를 통해 host-to-host 통신을 지원하는 기반이 된다. 현재 공식 인터넷 표준 목록은 RFC Editor 웹사이트(https://www.rfc-editor.org/standards)에서 확인할 수 있다.

## How It Works

**인터넷 표준 개발 절차:**

1. **Internet-Draft**: IETF에 제출하기 위해 개발 중인 명세. 아직 공식 RFC가 아님.
2. **RFC (Request for Comments)**: 인터넷 당국의 권고를 거쳐 발행. 각 RFC는 편집·번호 부여 후 전체 공개됨.
3. **Proposed Standard**: 안정적이고 충분히 이해된 명세로, 인터넷 커뮤니티의 충분한 관심을 받으며 여러 그룹이 구현·테스트한 단계.
4. **Internet Standard**: 철저히 테스트되어 인터넷 실무자들이 준수하는 최종 표준. 과거에는 중간에 Draft Standard 단계가 있었으나 RFC6410에 의해 폐지됨.

**표준의 유형:**

- **De jure standard (공식 표준)**: 공식 SDO 절차를 거쳐 채택된 표준. 예: PDF/A는 2005년 ISO 19005-1:2005로 공식 표준화.
- **De facto standard (사실상 표준)**: 공식 절차 없이 업계와 사용자들에게 광범위하게 채택된 표준. 예: PDF는 1993년 등장 시 de facto 표준이었다가 이후 de jure 표준이 됨.

## Key Properties

**반드시 기억해야 할 3대 SDO (Standard Development Organization):**

- **IETF (Internet Engineering Task Force)**: 인터넷 표준(RFC) 개발의 핵심 기관. 개방적·자발적 참여 방식으로 운영.
- **W3C (World Wide Web Consortium)**: 웹 표준(HTML, CSS, XML 등) 개발 기관.
- **IEEE (Institute of Electrical and Electronics Engineers)**: 전기·전자·컴퓨터 분야 표준(예: IEEE 802.11 WiFi, IEEE 802.3 Ethernet) 개발 기관.

기타 SDO: ISO, IEC, ANSI, ITU-T, ETSI, EIA 등.

**규제 기관 (Regulatory Agencies):**

- **KCC (방송통신위원회, Korea Communications Commission)**: 한국의 방송·통신 서비스 규제. 「방송통신위원회의 설치 및 운영에 관한 법률」에 근거.
- **FCC (Federal Communications Commission)**: 미국의 주간(interstate)·국제 통신 규제 기관.
- **유럽**: EC(유럽위원회), ETSI, CEPT 산하 ECC(Electronic Communications Committee)가 무선 장비 및 주파수 관련 규제 환경을 협력하여 관장.

## Relationships

- [[network-protocol]] — 프로토콜이 표준화 과정을 통해 Proposed Standard 또는 Internet Standard로 공식화됨
- [[internet]] — 인터넷은 IETF RFC 기반의 표준 자발적 준수를 통해 전 세계적으로 동작 가능함

## Open Questions

- Internet-Draft가 RFC로 발행되지 못하고 폐기될 경우, 실무에서 이미 구현된 기술은 어떻게 처리되는가? (예: 사실상 표준으로 운용되는 비표준 구현체 문제)
- Draft Standard 단계 폐지(RFC6410) 이후, Proposed Standard에서 Internet Standard로의 전환 기준과 속도가 실제로 어떻게 변화했는가?
- De facto 표준이 de jure 표준보다 실질적인 영향력이 더 큰 영역(예: 소셜 미디어 API, 컨테이너 이미지 포맷)에서 표준화 기관의 역할은 어떠해야 하는가?

## Sources

- raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf (pp.44–46)
