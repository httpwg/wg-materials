<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Session Summary: 20260724-0700](#session-summary-20260724-0700)
- [HTTPBIS](#httpbis)
  - [Summary](#summary)
  - [Key Discussion Points](#key-discussion-points)
    - [1. Working Group Documents](#1-working-group-documents)
      - [Resumable Uploads for HTTP (`draft-ietf-httpbis-resumable-upload`)](#resumable-uploads-for-http-draft-ietf-httpbis-resumable-upload)
      - [Cookies: HTTP State Management Mechanism (`draft-ietf-httpbis-layered-cookies`)](#cookies-http-state-management-mechanism-draft-ietf-httpbis-layered-cookies)
      - [The Preliminary Request Denied HTTP Status Code (`draft-ietf-httpbis-pre-denied`)](#the-preliminary-request-denied-http-status-code-draft-ietf-httpbis-pre-denied)
      - [Secondary Certificate Authentication of HTTP Servers (`draft-ietf-httpbis-secondary-server-certs`)](#secondary-certificate-authentication-of-http-servers-draft-ietf-httpbis-secondary-server-certs)
      - [Template-Driven HTTP CONNECT Proxying for TCP (`draft-ietf-httpbis-connect-tcp`)](#template-driven-http-connect-proxying-for-tcp-draft-ietf-httpbis-connect-tcp)
    - [2. New Proposals & Presentations](#2-new-proposals--presentations)
      - [HTTP Signature Keys](#http-signature-keys)
      - [RESET_STREAM_AT in HTTP/3](#reset_stream_at-in-http3)
      - [HTTP/1.1 Request Smuggling Defense](#http11-request-smuggling-defense)
      - [OHTTP: PFS & Key Configuration](#ohttp-pfs--key-configuration)
  - [Decisions and Action Items](#decisions-and-action-items)
  - [Next Steps](#next-steps)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



**NOTE**: _this is a non-normative, AI-generated summary supplied only for convenience; it does not necessarily represent an accurate record of the meeting. See the minutes for the authoriative record. See [the source](https://ietfminutes.org/) for more information._
    


# Session Summary: 20260724-0700

# [HTTPBIS](../wg/httpbis.html)

## Summary

The HTTPBIS Working Group met to discuss several active working group drafts and new proposals. Updates were presented on resumable uploads, layered cookies, preliminary request denied status codes, secondary server certificates, and CONNECT-TCP proxying. Additionally, the group discussed new proposals regarding HTTP signature keys, the use of `RESET_STREAM_AT` in HTTP/3, cryptographic request smuggling defenses for HTTP/1.1, and Perfect Forward Secrecy (PFS) and key configuration updates for Oblivious HTTP (OHTTP).

---

## Key Discussion Points

### 1. Working Group Documents

#### Resumable Uploads for HTTP (`draft-ietf-httpbis-resumable-upload`)
* **Presentation**: [Resumable Uploads](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-resumable-uploads-00) by Marius Kleidl.
* **Discussion**:
  * Marius Kleidl reported that since the Working Group Last Call (WGLC) last July, 90 issues were opened. 82 have been resolved, leaving 8 open (mostly editorial/clarifications).
  * Major changes since version -11 include:
    * Removing normative language regarding final response loss.
    * Clarifying how a server stops an upload prematurely.
    * Removing the section on integrity digests (due to unclear semantics and lack of deployment experience).
  * Browser integration discussions (HTML forms, Fetch API) took place at a recent workshop. A tracking issue (#3498) is available for WHATWG-related concerns (cross-origin resource sharing, cookies, and content security policies).
  * Lucas Pardue noted in the chat that the removed integrity text could potentially start a new Internet-Draft.
  * Marius Kleidl and Tommy Pauly discussed implementation status; Apple's networking stack is updated, and other implementations plan to follow. No major interop-breaking changes are expected.

#### Cookies: HTTP State Management Mechanism (`draft-ietf-httpbis-layered-cookies`)
* **Discussion**:
  * Mark Nottingham provided an update. RFC 6265bis is in the final review stage (AUTH48). 
  * The layered cookie specification (`draft-ietf-httpbis-layered-cookies`), which refactors the cookie specification to split wire-format HTTP behavior from browser fetch specifications, remains in progress. No major updates were reported as the authors are on holiday, with a fuller update expected in November.

#### The Preliminary Request Denied HTTP Status Code (`draft-ietf-httpbis-pre-denied`)
* **Discussion**:
  * Mark Nottingham led the discussion on assigning a status code. Status code **419** is under consideration.
  * Although Laravel currently squats on 419, a migration path exists for them. Mark Nottingham argued that refusing standard status codes due to proprietary squatting creates a bad precedent.
  * There was support in the room for 419. Mark Nottingham will send an explicit proposal to the mailing list. If no objections are raised, the draft will proceed to WGLC.
  * *Chat Log Notes*: Ted Hardie noted that "IANA now discourages suggested values." Martin Thomson clarified that while he provided feedback to the `ianabis` session that this is unwise for certain registries, the advice still stands for registries without inherent collision resistance, such as status codes.

#### Secondary Certificate Authentication of HTTP Servers (`draft-ietf-httpbis-secondary-server-certs`)
* **Discussion**:
  * Mark Nottingham stated that all outstanding issues have been addressed. The chairs intend to kick off a 3-to-4-week WGLC to allow ample review time during the holiday season.
  * Mike Bishop (author and Area Director) supported initiating the last call and committed to doing a fresh review.

#### Template-Driven HTTP CONNECT Proxying for TCP (`draft-ietf-httpbis-connect-tcp`)
* **Presentation**: [CONNECT-TCP](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-connect-tcp-00) by Ben Schwartz.
* **Discussion**:
  * Ben Schwartz summarized the updates in draft-12, which resolved 19 WGLC issues raised by Eric Nygren and Willy Tarreau.
  * One remaining open issue concerns abrupt closure, shutdown signaling, and resource utilization (mitigating DOS risks where TCP states hold resources open for minutes). Ben Schwartz believes the changes in draft-12 resolve this and requested final feedback.
  * David Schinazi suggested assigning provisional capsule types early to ease implementation pain. Tommy Pauly agreed to coordinate early registry allocation with IANA during the shepherding process and requested a draft-13 revision to incorporate these numbers.

---

### 2. New Proposals & Presentations

#### HTTP Signature Keys
* **Presentation**: [HTTP Signature Keys](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http-signature-keys-00) by Justin Richer.
* **Discussion**:
  * Justin Richer presented a proposal to transport keys associated with HTTP Message Signatures (RFC 9421) using the `Signature-Key` header.
  * Supported key schemes include Header Web Key (HWK), Jacket JWT, JWKS URI, Self JWT, and X.509. Key updates include an `Accept-Signature` header parameter and enhanced error messages.
  * The proposal has active open-source implementations in TypeScript, Rust, Go, .NET, and Elixir.
  * Dennis Jackson remarked that the draft contains significant security-relevant text and will require careful coordination with the Security Area.
  * Ted Hardie noted that Section 4.6 (coexistence with `WWW-Authenticate`) feels underspecified and needs clearer guidance for clients supporting both.
  * **Poll**: Are you interested in working on this  in HTTPBIS? — yes: 16, no: 0, no_opinion: 20 (total: 70).

#### RESET_STREAM_AT in HTTP/3
* **Presentation**: [RESET_STREAM_AT in HTTP/3](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-reset-stream-at-in-http3-00) by Martin Seemann.
* **Discussion**:
  * Martin Seemann presented on using the QUIC `RESET_STREAM_AT` extension (currently in IETF Last Call) within HTTP/3. It allows a sender to reset a stream while guaranteeing reliable delivery of data up to a specified offset. It is widely implemented in browsers for WebTransport.
  * Proposed HTTP/3 use cases:
    1. *Connect Proxying*: Ensuring data received before an upstream connection error is reliably delivered.
    2. *HTTP Field Errors (RFC 9114)*: Allowing a server to transmit a detailed `400 Bad Request` body describing header validation failures before resetting the stream.
    3. *Request Rejection*: Reliably transmitting headers for rejected requests.
  * Mike Bishop advised against combining this with the "request rejected" error code because sending an HTTP response body implies the request *was* processed. However, Mike Bishop noted it would solve a critical issue in Server Push where unidirectional streams are reset before metadata (the push ID) is read.
  * Ben Schwartz and David Schinazi cautioned that for TCP-based proxying (including `draft-ietf-httpbis-connect-tcp`), downstream TCP stacks treat a TCP Reset as an immediate discard of buffered data, rendering "reliable" reset ineffective over TCP.
  * David Schinazi questioned if the proposal cleanly maps to HTTP semantics, arguing that a stream reset represents an unrecoverable failure. Tommy Pauly suggested the draft focus on concrete client actions and debuggability.

#### HTTP/1.1 Request Smuggling Defense
* **Presentation**: [HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding -01 version of draft](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http11-request-smuggling-defense-using-cryptographic-message-binding-01-version-of-draft-00) by Eric Nygren.
* **Discussion**:
  * Eric Nygren presented a mechanism to defend against intermediary/downstream request desynchronization using a cryptographically bound hop-by-hop counter.
  * The -01 version introduces an explicit threat model and key negotiation via ALPN or an in-band header using SHA-256 or SipHash-2-4.
  * Ben Schwartz and Kazuho Oku questioned whether the mechanism can be implemented on top of unmodified HTTP/1.1 stacks. Eric Nygren noted that testing on popular reverse proxies (NGINX, HAProxy, Envoy) is needed to assess implementation complexity.
  * David Schinazi expressed strong support, noting that request smuggling represents a significant portion of security issues in Envoy. He suggested adding a handshake mechanism where the downstream server confirms support on the first request.
  * Chris Lemmons supported the initiative, noting that a simple, deployable patch is highly desirable for security operators.

#### OHTTP: PFS & Key Configuration
* **Presentation**: [OHTTP: PFS & Key Config](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-ohttp-pfs-key-config-00) by David Schinazi.
* **Discussion**:
  * David Schinazi presented two draft updates based on experience deploying Oblivious HTTP (OHTTP) at scale:
    1. **Perfect Forward Secrecy (PFS) for OHTTP**: Chunked OHTTP lacks forward secrecy if the gateway's long-term key is compromised. The proposal introduces ephemeral key pairs in the client request. The first flight remains non-PFS, but subsequent chunked exchanges gain PFS.
       * Dennis Jackson and Martin Thomson questioned the utility of adding OHTTP complexity over fixing/using TLS (e.g., introducing unlinkable 0-RTT in TLS).
       * David Schinazi and Christopher Wood argued that modifying TLS is extremely difficult, whereas OHTTP is highly deployable and already handles out-of-band key distribution.
       * Ben Schwartz shared that Meta uses authenticated TLS (ATLS) over chunked OHTTP for "private processing" to solve similar problems but welcome a cleaner, standardized solution.
       * Mike Bishop emphasized that any cryptographic changes must undergo rigorous security analysis and formal proofs with direct Security Area engagement.
    2. **OHTTP Key Configuration**: The current OHTTP key format is not backward-compatible when handling multiple key configurations (e.g., post-quantum transition). Additionally, there is no standardized way to signal key expiration.
       * The proposal adds `not_before` and `expiration` timestamps as extensions within the key config and defines a new content-type.
       * *Chat Log Debate*: Martin Thomson argued against `not_before`, stating "don't ship a key you aren't prepared to use." Mike Bishop, Christopher Wood, and Dennis Jackson disagreed, noting that `not_before` facilitates parallel client/server deployments and consistent key rotation (such as in Privacy Pass).

---

## Decisions and Action Items

* **`draft-ietf-httpbis-resumable-upload`**: Marius Kleidl to close the remaining 8 open issues, publish an updated draft, and prepare for a second WGLC.
* **`draft-ietf-httpbis-pre-denied`**: Mark Nottingham to send an explicit proposal to the list to adopt status code **419** and, pending no objections, prepare the draft for WGLC.
* **`draft-ietf-httpbis-secondary-server-certs`**: Chairs to initiate a 3-to-4-week WGLC on the list.
* **`draft-ietf-httpbis-connect-tcp`**: Ben Schwartz to publish draft-13 with provisional capsule allocations. Tommy Pauly to initiate early IANA registry allocation and prepare the shepherding writeup.
* **HTTP Signature Keys**: Justin Richer to address list feedback regarding WWW-Authenticate coexistence and continue refining the draft in coordination with the Security Area.
* **RESET_STREAM_AT in HTTP/3**: Martin Seemann to update the draft to clarify client-side debugging behavior and add the Server Push use case raised by Mike Bishop.
* **HTTP/1.1 Request Smuggling Defense**: Eric Nygren to coordinate with implementers of common HTTP/1.1 proxies to test implementation complexity and seek coauthors.
* **OHTTP Drafts**: David Schinazi to coordinate with Security Area directors and HTTPBIS chairs regarding the appropriate venue for the OHTTP PFS and Key Configuration drafts.

---

## Next Steps

* Launch WGLCs for `draft-ietf-httpbis-secondary-server-certs` and `draft-ietf-httpbis-pre-denied`.
* Complete the shepherding process for `draft-ietf-httpbis-connect-tcp`.
* Follow up on the list regarding the adoption of HTTP Signature Keys following the positive interest poll.
* Mark Nottingham invited volunteers to participate in the HTTP Directorate's experimental use of AI tools to assist in reviewing external HTTP-adjacent protocols against BCP 56.