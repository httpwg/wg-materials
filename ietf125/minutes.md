**Session Date/Time:** 20 Mar 2026 01:00

# [HTTPBIS](../wg/httpbis.html)

## Summary

The HTTP Working Group (HTTPBIS) met at IETF 125 to discuss several active drafts and new proposals. Key topics included new status codes for prefetch denials, optimizations for CONNECT in HTTP/3, and progress on resumable uploads. The group also reviewed proposals for redirect and signature-key headers, and discussed the application of QPACK principles to the Media over QUIC (MoQ) protocol.

## Key Discussion Points

### [HTTP Redirect Headers](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-http-redirect-headers-01)
* **Presenter:** Dick Hardt
* **Discussion:** The proposal introduces headers (`Redirect-Query`, `Redirect-Origin`, `Redirect-Path`) to move sensitive parameters (like OAuth codes) out of the URL during redirects. 
* **Feedback:** Martin Thompson and David Schinazi expressed skepticism, noting that moving bits to headers doesn't necessarily prevent access by malicious browser extensions. Mark Nottingham highlighted tracking vector concerns. There was a general sense that this work might be better suited for the OAuth WG or WHATWG.

### [HTTP Signature-key Header](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-http-signature-key-header-00)
* **Presenter:** Dick Hardt
* **Discussion:** This proposal defines a way to carry public keys within HTTP messages for use with HTTP Message Signatures. Dick Hardt highlighted use cases for mobile app attestation and ephemeral keys. 
* **Feedback:** David Schinazi raised concerns regarding the "alg: none" type vulnerability where a receiver might trust a key provided in the header without verification. Martin Thompson found the design overly complex but acknowledged the validity of the session-binding use cases.

### [Preliminary Request Denied](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-preliminary-request-denied-00)
* **Presenter:** Mark Nottingham
* **Draft:** [draft-donnelly-httpbis-preliminary-request-denied](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-preliminary-request-denied-00)
* **Discussion:** Servers currently use 503 status codes to deny speculative prefetches (e.g., those triggered by `Sec-Purpose: prefetch`), which can alarm operational monitoring teams. The draft proposes a new status code (e.g., 4xx "Preliminary Request Denied" or "Purpose Declined") to disambiguate these denials.
* **Feedback:** There was strong support for adoption from Yoav Weiss, Nidhi Jaju, Lucas Pardue, and Guoyue Zhang.

### [CONNECT-TCP](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-connect-tcp-00)
* **Presenter:** Benjamin Schwartz
* **Draft:** [draft-ietf-httpbis-connect-tcp](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-connect-tcp-00)
* **Discussion:** The group discussed a conflict between `Proxy-Status` trailers and the CONNECT method, as HTTP/2 and HTTP/3 generally prohibit trailers on CONNECT streams. 
* **Feedback:** Mike Bishop, David Schinazi, and others argued against extending CONNECT to allow trailers. The consensus was to remove the trailer text from the draft and adhere to existing protocol restrictions.

### [Unbound DATA for CONNECT in HTTP/3](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-unbound-data-for-connect-in-http3-00)
* **Presenter:** Yaroslav Rosomakho
* **Discussion:** The proposal introduces an `Unbound-DATA` frame for HTTP/3 CONNECT requests. Once sent, the remainder of the QUIC stream is treated as raw data without further HTTP framing, reducing overhead and complexity for high-performance proxies.
* **Feedback:** Benjamin Schwartz questioned the need to mix standard DATA frames and Unbound DATA, while David Schinazi argued that allowing both is simpler for implementation state machines.

### [Resumable Uploads](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-resumable-uploads-00)
* **Presenter:** Guoyue Zhang
* **Draft:** [draft-ietf-httpbis-resumable-upload](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-resumable-upload-00)
* **Discussion:** Focus was on client retry behavior and the retrieval of lost responses after an upload is complete. 
* **Feedback:** Martin Thompson recommended keeping the retrieval of lost responses out of scope to avoid delaying the draft. The authors agreed to move toward finishing the draft by summer with non-normative guidance on retries.

### [MOQPACK](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-moqpack-00)
* **Presenter:** Alan Frindell
* **Discussion:** MoQ requires header compression for parameters but operates over WebTransport (lacking transport stream IDs). MOQPACK reuses QPACK’s synchronization logic but removes Huffman encoding and redefines static table references to use integer keys.
* **Feedback:** Martin Thompson suggested that while the synchronization concepts of QPACK (RFC 9204) are valuable, the implementation should use MoQ varints and avoid literal reuse of the QPACK spec text due to semantic differences.

### HTTP Wrap-up Capsule
* **Discussion:** David Schinazi noted a lack of immediate personal use cases for the draft and suggested parking it. However, Yaroslav Rosomakho and Tommy Pauly expressed interest in implementing it for proxy use cases.
* **Decision:** The draft will remain active. Yaroslav Rosomakho may join as an author to help drive the work forward with a constrained scope.

### Secondary Certificate Authentication
* **Status:** This work has languished. The chairs will contact the authors to determine if there is interest in continuing or if additional authorial help is required.

## Decisions and Action Items
* **Preliminary Request Denied:** Chairs will initiate a call for working group adoption for [draft-donnelly-httpbis-preliminary-request-denied](https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-preliminary-request-denied-00).
* **CONNECT-TCP:** Benjamin Schwartz will remove the text regarding `Proxy-Status` trailers to maintain consistency with H2/H3 CONNECT rules.
* **HTTP Wrap-up Capsule:** The group decided to keep the document active rather than parking it. Yaroslav Rosomakho will collaborate with the current editors.
* **Secondary Certificate Authentication:** Chairs to follow up with authors for a status update.

## Next Steps
* **Resumable Uploads:** Editors aim to resolve remaining editorial issues and refactor the draft for a final push toward completion by the summer.
* **MOQPACK:** Alan Frindell to iterate on the draft based on feedback regarding synchronization logic and integer encodings.
* **Unbound DATA:** Chairs to gauge consensus on the narrowed scope (CONNECT-only) for potential adoption.