<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Session Summary: 20251105-1430](#session-summary-20251105-1430)
  - [Summary](#summary)
  - [Key Discussion Points](#key-discussion-points)
    - [Connect TCP Reset Handling](#connect-tcp-reset-handling)
    - [Resumable Uploads (Marius)](#resumable-uploads-marius)
    - [Unencoded Digest (Lucas Pardue)](#unencoded-digest-lucas-pardue)
    - [Secondary Certificates (Eric Garbardi)](#secondary-certificates-eric-garbardi)
    - [Cookies](#cookies)
    - [Detecting Outdated Proxy Configuration (Yaroslav from Ziegler)](#detecting-outdated-proxy-configuration-yaroslav-from-ziegler)
    - [Unbound Data Frames in HTTP/3 (Yaroslav from Ziegler)](#unbound-data-frames-in-http3-yaroslav-from-ziegler)
    - [HTTP/1.1 Request Smuggling Defense (Eric Nigrin)](#http11-request-smuggling-defense-eric-nigrin)
  - [Decisions and Action Items](#decisions-and-action-items)
  - [Next Steps](#next-steps)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



**NOTE**: _this is a non-normative, AI-generated summary supplied only for convenience; it does not necessarily represent an accurate record of the meeting. See the minutes for the authoriative record. See [the source](https://ietfminutes.org/) for more information._
    


# Session Summary: 20251105-1430



## Summary

The HTTPBIS Working Group held its only session for this IETF, covering updates on several active drafts and discussing new proposals. Key discussions included refining Connect TCP behavior for connection failures, addressing open issues in Resumable Uploads, and preparing the Unencoded Digest and Secondary Certificates drafts for Working Group Last Call. A new proposal for Origin-Bound Cookies received strong positive feedback and will be integrated into the Layered Cookies draft. The group also considered a mechanism for detecting outdated proxy configurations and an optimization for HTTP/3 data framing. Finally, a significant discussion was held on potential defenses against HTTP/1.1 request smuggling.

## Key Discussion Points

### Connect TCP Reset Handling

*   **Problem:** The last open Pull Request for the Connect TCP draft addresses how to translate TCP connection failures, particularly half-open streams and FIN/FIN-ACK handling, into signals over HTTP streams.
*   **Proposal (Ben Schwartz):** For HTTP/2 and HTTP/3, the behavior involves signaling a stream error. For HTTP/1.1, the proposal suggests using a TCP shutdown without a `close_notify` TLS alert. This is at the "should" level due to known difficulties in reliably manipulating TLS shutdown behavior across different implementations.
*   **Discussion:**
    *   Alan Friend questioned the criticality of reliable half-close for protocols over Connect TCP, given HTTP's own challenges with it. Ben Schwartz clarified that the "should" level acknowledges this.
    *   Ben Schwartz explained that defining this for HTTP/1.1 provides consistency for gateways translating between HTTP versions, which may receive HTTP/3 or HTTP/2 stream errors and need an equivalent HTTP/1.1 representation.
*   **Action Item:** The working group is requested to review the PR and provide feedback. Chairs will follow up with Martin Thompson, who had raised alternative views. Lucas Pardue, Alan Friend, and Cazoo Hill volunteered to review.

### Resumable Uploads (Marius)

The draft received significant feedback during its Working Group Last Call, resulting in 28 open issues, with four requiring group discussion.

1.  **Retrieving Lost Responses:**
    *   **Problem:** If a client completes an upload but fails to receive the final server response due to a network interruption, it lacks a robust recovery mechanism.
    *   **Proposal:** The server should cache or regenerate the final response after upload completion and allow the client to refetch it using an empty `PATCH` request, mirroring the completion mechanism.
    *   **Discussion:**
        *   Alessandro Gettini suggested "regenerate" might be a more accurate term than "cache" as servers might not strictly cache the response.
        *   Austin raised concern that this is a generic problem for long-running `POST` requests, suggesting a more general solution might be appropriate rather than an upload-specific one.
        *   Ben Schwartz found the use of a zero-length `PATCH` request for a null modification "funny" and questioned its semantic alignment with `PATCH`, especially regarding metadata like M-time.
        *   Katsuhiko Oku preferred a minimal solution specific to uploads, not a generic resumption scheme.
        *   Mike Bishop suggested a generic approach where a server could provide an interim resource URL for clients to query later.
    *   **Outcome:** Further discussion is needed to refine the proposal.

2.  **GET Requests on Upload Resources:**
    *   **Problem:** RFC 9110 couples `HEAD` and `GET` responses. The draft uses `HEAD` for synchronizing state but does not explicitly define `GET` behavior for upload resources.
    *   **Proposal:** If an upload resource receives a `GET` request, it should generate a successful response that includes the same upload-related headers as a `HEAD` request. The content of the `GET` response is application-dependent.
    *   **Outcome:** No concerns were raised from the working group; the proposal appears acceptable.

3.  **Client Offset Jump Forward:**
    *   **Problem:** Can the client's upload offset (number of bytes received by the server) increase without the client explicitly transferring bytes (e.g., if the server fills in parts of the representation from an existing hash, or in a distributed upload scenario)?
    *   **Discussion:**
        *   Mike Bishop viewed a hash pointer as an "out-of-band upload path" where the client *did* upload the bytes. He suggested not forbidding such behavior but also not detailing implementation specifics for distributed clients.
        *   Lucas Pardue emphasized accepting the reality of such jumps rather than ignoring them, and that wording should accommodate this without re-evaluating the protocol's design principles for simplicity and serial operations.
    *   **Outcome:** The group will work on refining the text to accommodate this reality without expanding the scope into distributed client implementation details.

4.  **Granularity Requirements:**
    *   **Problem:** Some legacy storage systems require data to be appended in specific granularities (e.g., multiples of 50 MB). The current draft allows arbitrary chunk sizes. Implicitly, servers could discard trailing bytes, but clients wouldn't know.
    *   **Proposal:** Explicitly define and communicate granularity requirements from the server to the client.
    *   **Discussion:** Lucas Pardue noted this is effectively a new feature request introduced late in the process. He suggested postponing explicit support for granularity, letting implicit handling (server discarding trailing bytes) suffice for now, and gathering deployment experience.
    *   **Outcome:** The working group agreed to defer explicit support for granularity, with implicit support being sufficient for the current draft.

*   **Action Item:** Marius will continue integrating feedback and refining the draft.

### Unencoded Digest (Lucas Pardue)

*   **Status:** The draft currently has zero open issues.
*   **Action Item:** The chairs will initiate a Working Group Last Call. Reviewers are requested to read the draft.

### Secondary Certificates (Eric Garbardi)

*   **Problem:** The primary remaining issue is the complexity of sending large exported authenticators over HTTP/2, which might require multiple frames and introduces head-of-line blocking concerns. HTTP/3 inherently handles this better.
*   **Discussion:**
    *   Several alternatives were discussed but added significant complexity.
    *   Martin Thompson had previously noted that HTTP/2 frame size is negotiable.
    *   The discussion leaned towards accepting the limitation for HTTP/2 and not introducing complex workarounds, especially given HTTP/3's better suitability for such use cases.
    *   Alessandro Gettini and Cory both strongly advocated to "just close this" issue.
*   **Decision:** The working group generally agreed to close the issue with no changes, effectively limiting the mechanism's optimal use for HTTP/2.
*   **Next Steps:** Eric will produce a new draft reflecting any minor editorial work. A Working Group Last Call will follow, potentially in parallel with final editorial changes.

### Cookies

*   **RFC 6265bis Update (Mike Bishop):** The `HTTP/1.1, Semantics and Content` draft, which updates RFC 6265, was approved by the IESG about six months ago. After a brief hiatus, the primary editor is back, and final updates are in progress. It is expected to be sent to the RFC Editor within the next week.

*   **Layered Cookies & Origin-Bound Cookies (Johann Schwoerer, Ahmadijian Fakhuri):**
    *   **Context:** The "Layered Cookies" draft refactors cookie mechanisms to better align with browser specifications (e.g., `SameSite`). It has incorporated the HTTP-only prefix proposal.
    *   **Origin-Bound Cookies Proposal (Ahmadijian Fakhuri):** This new draft aims to enhance cookie security by binding cookies to their specific port and scheme.
        *   **Problem:** Current cookies exhibit weak confidentiality (e.g., secure site cookie sent to insecure scheme) and weak integrity (e.g., insecure site setting a malicious cookie for a secure site on a different port).
        *   **Proposal:** Introduce `Port` and `Scheme` attributes for cookies. New cookies will be bound to the port and scheme of their setting origin. Existing/legacy cookies without these attributes will retain current behavior. A `Domain` attribute on a cookie will relax port binding (but not scheme binding) for compatibility. The proposal would eventually obsolete the `Secure` attribute.
    *   **Discussion:**
        *   David Benjamin lauded the proposal, stating it "fixes one of the original sins of the cookie header" and reduces reliance on HSTS lists for scheme-related attacks.
        *   There was a general sense of enthusiasm in the room, with many expressing that this is how cookies "should have been done the first time."
*   **Decision:** The working group found the proposal promising.
*   **Action Item:** The editors should begin incorporating the Origin-Bound Cookies proposal into the new Layered Cookies draft for broader working group consideration.

### Detecting Outdated Proxy Configuration (Yaroslav from Ziegler)

*   **Problem:** There is currently no push mechanism for proxies to inform clients about outdated proxy configurations, leading to reliance on periodic polling and potential issues with stale configurations.
*   **Proposal:**
    *   A client sends a `Proxy-Config-Source` request header containing the URL of its proxy configuration source (optional) and a `Fetched-Timestamp`.
    *   A proxy responds with a `Proxy-Config-Stale` response header (boolean) indicating if the client's configuration is stale.
*   **Revisions in Latest Draft:** The mechanism is now restricted to `CONNECT` methods to ensure clear separation of headers intended for the proxy from those for the origin, preventing privacy/security leaks. The URL in `Proxy-Config-Source` is now even more optional, accommodating configurations pushed by management systems.
*   **Open Questions/Feedback:**
    *   **Proxy providing a different location:** Yaroslav expressed security concerns about a rogue proxy redirecting clients.
    *   **New header vs. `Proxy-Status` parameter:**
        *   Tommy Pollard (individual) suggested `Proxy-Status` is more about the intermediary's status, whereas `Proxy-Config-Stale` concerns the client's state. A new header seemed more appropriate, unless reframed as the proxy declaring *its* knowledge of the client's config state.
        *   Jim Taff supported a new header, citing the "dogpiling" problem with existing headers like `Link`, and noting Structured Fields make new headers easier.
    *   **Need for a standard:** Ben Schwartz questioned if there's sufficient demand for a standard, given this is detailed control plane information typically vendor-specific. Yaroslav and Jim Taff affirmed the real-world problem in multi-vendor environments, especially with PAC files and the need to prevent excessive polling.
*   **Outcome:** There is appetite for this work within the working group.
*   **Next Steps:** The chairs will initiate a Call for Adoption for this draft. Further discussion on the specific header name (`Proxy-Config-Stale` vs. `Proxy-Status` parameter) is expected.

### Unbound Data Frames in HTTP/3 (Yaroslav from Ziegler)

*   **Problem:** `DATA` frames in HTTP/3, while useful for indicating data completion and start, often do not align with the segmentation of underlying protocols (e.g., WebSockets, encapsulated TCP). They add 3 bytes of overhead per frame, increase implementation complexity, create unnecessary state, and can introduce latency due to buffering. They are particularly "useless" when trailers are not used.
*   **Proposal:** Introduce an optional "unbound data frame," a simple zero-length indicator negotiated through settings. This frame would signify that the remainder of the QUIC stream is raw data, allowing applications to avoid the H3 `DATA` frame overhead. It cannot be used if trailers are planned.
*   **Discussion:**
    *   **Benefits:** Potential for 3 bytes/frame savings, more importantly, avoiding unnecessary memory copies in high-performance zero-copy frameworks.
    *   **Concerns (Ben Field, Ben Schwartz):**
        *   Moves HTTP/3 towards a general-purpose transport, blurring lines with WebTransport.
        *   Requires implementations to know *upfront* whether trailers will be used, which is often not the case for generic HTTP APIs. This limits its applicability to very narrow, application-specific use cases (e.g., gRPC, which relies on trailers, would not benefit).
        *   Ben Schwartz suggested an alternative: indirecting the data onto a *new* QUIC stream, turning the original stream into a control channel, which might achieve similar benefits without compromising trailer support.
    *   **Complexity (Alessandro Gettini):** Questioned if the performance gains justify the additional complexity of a new frame type and conditional logic.
    *   **Scope (Katsuhiko Oku):** Suggested reframing the draft to make it specific to `CONNECT` method use cases (i.e., for non-hypertext data), rather than a generic HTTP/3 extension, to avoid re-litigating fundamental HTTP/3 framing decisions.
    *   **HTTP/2 vs. HTTP/3 (Ben Schwartz):** Noted this mechanism could only apply to HTTP/3, as HTTP/2 framing is fundamentally different.
*   **Outcome:** Valuable feedback was received.
*   **Next Steps:** Yaroslav will explore the alternative of indirectly streaming data to a new QUIC stream and/or reframing the proposal as a `CONNECT`-specific extension. A new revision may be brought to the next meeting.

### HTTP/1.1 Request Smuggling Defense (Eric Nigrin)

*   **Problem:** HTTP/1.1 continues to be a source of request smuggling vulnerabilities, often due to implementation differences between intermediaries and origin servers. Unlike HTTP/2 and HTTP/3 which explicitly separate control and data (e.g., stream IDs, pseudo-headers), HTTP/1.1 lacks robust in-band mechanisms to prevent such confusion attacks.
*   **Proposal (Proof-of-Concept):** Introduce an in-band, protected signal, such as a new `Request-Binding` header containing a request serial number. An origin server receiving a request with a missing or out-of-order serial number could then abort the request cleanly. The protection for this signal could come from TLS exporters or other out-of-band keying mechanisms.
*   **Desired Solution Properties:** Easy to implement, low overhead, auto-negotiating (drop-in), and robust protection of request serials (and potentially other sensitive headers like `Host` or `Path`).
*   **Discussion:**
    *   **Importance:** Ben Field and Alessandro Gettini agreed this is an important problem worth solving due to ongoing vulnerabilities.
    *   **Trusted Environments:** Ben Field raised the need to address scenarios like Kubernetes ingresses where TLS might not be end-to-end to the final host, requiring alternative binding mechanisms (e.g., pre-configured keys in trusted environments).
    *   **Source of Problem (Katsuhiko Oku):** Suggested the problem lies more with intermediaries observing HTTP/1.1 and making forwarding decisions, rather than HTTP/1.1 itself.
    *   **Fundamental Tensions (Ben Schwartz):** Expressed skepticism about this category of solutions, arguing that a negotiated solution (requiring both parties to upgrade) goes against the core problem of one party being unable to upgrade. He suggested stronger, one-sided recommendations like disabling HTTP/1.1 connection reuse for intermediaries in smuggling-risk contexts (while maintaining performance with connection pools), or other non-negotiated approaches.
    *   **Counter-Arguments (Eric Nigrin, Alan Friend):** Disabling persistent connections (for one-sided solutions) would introduce performance downsides like slow start and congestion control (though less relevant for IPC). For CDN-to-origin scenarios, a lightweight, drop-in solution could still be highly valuable, even if negotiated. Alan Friend supported the idea as a "hammer" to incentivize safer H1.1 usage or migration to H2.
*   **Outcome:** There is strong interest in continuing the discussion.
*   **Next Steps:** The discussion will continue on the mailing list to refine approaches. Eric Nigrin called for co-authors or individuals interested in helping with this work.

## Decisions and Action Items

*   **Connect TCP Reset Handling:** The working group will review the Pull Request. Chairs will engage Martin Thompson for his feedback. Lucas Pardue, Alan Friend, and Cazoo Hill volunteered to review the PR.
*   **Resumable Uploads:** Editors will incorporate feedback regarding lost responses and offset jumps. The working group decided to postpone explicit support for granularity requirements for now, considering implicit handling sufficient.
*   **Unencoded Digest:** The chairs will issue a Working Group Last Call. Members are encouraged to review the draft.
*   **Secondary Certificates:** The H2 framing issue will be closed with no change. Eric Garbardi will prepare a new draft with any necessary editorial changes, to be followed by a Working Group Last Call.
*   **Origin-Bound Cookies:** The proposal received positive feedback. Editors are tasked with incorporating it into the new Layered Cookies draft for the working group's consideration.
*   **Detecting Outdated Proxy Configuration:** The chairs will conduct a Call for Adoption for this draft, with further discussion expected on the appropriate header (new header vs. `Proxy-Status` parameter).
*   **Unbound Data Frames in H3:** Yaroslav will explore alternative proposals, specifically the idea of redirecting data to a new QUIC stream and/or reframing the proposal as a `CONNECT`-specific extension, and will likely bring a new revision for future discussion.
*   **HTTP/1.1 Request Smuggling Defense:** Discussion will continue on the mailing list. Eric Nigrin called for potential co-authors or helpers to advance this work.

## Next Steps

*   Working Group Last Call for "Unencoded Digest" and "Secondary Certificates".
*   Continued iteration on "Resumable Uploads" and "Unbound Data Frames in HTTP/3."
*   Call for adoption for "Detecting Outdated Proxy Configuration."
*   Further discussion and potential drafting work for "HTTP/1.1 Request Smuggling Defense."
*   The community-run HTTP Workshop is scheduled for next year, the week before the Vienna IETF meeting, for informal protocol discussions. More information can be found at [httpworkshop.org](httpworkshop.org).