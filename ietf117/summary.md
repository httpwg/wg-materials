**Session Date/Time:** 26 Jul 2023 16:30

# httpbis

## Summary

This httpbis meeting covered several active drafts and proposals, including resumable uploads, template driven HTTP connect over TCP, unprompted authentication, structured field values and retrofit, the query method, old service status, a report from the WebSocket's design team and a proposal for a header called request OTR. Key discussions revolved around versioning, dependency management, security considerations, and the overall direction of each proposal.

## Key Discussion Points

*   **Resumable Uploads:**
    *   Clarification on the usage and naming of the "upload complete" header.
    *   Multi-versioning strategy for future iterations of the draft (suggestion for header suffixes).
    *   Adoption of byte range patch draft and its potential dependency concerns.
    *   Discussion on the feasibility of using informational responses to provide upload progress.
*   **Template Driven HTTP Connect using for DCP:**
    *   Concerns regarding the term "false start" and its association with existing terminologies.
    *   Implications of optimistic transmission in HTTP 1.1, security concerns and potential contradictions with RFCs.
*   **Unprompted Authentication:**
    *   The move to using HTTP authentication schemes instead of new headers
    *   The use of TLS key exporters to generate signatures.
    *   Discussion on adopting exported authenticators instead of designing something similar.
    *   Addressing potential attacks through key rotation and binding of key IDs to public keys.
*   **Structured Fields:**
    *   Discussion on the character encoding and case normalization for display strings (percent encoding).
    *   Impact of extensions in map fields and the choice to constrain future extensions.

*   **WebSockets Design Team Report:**
    *   Prioritizing the reduction of additional round trips when establishing WebSockets.
    *   Discussion regarding server agent rollback support, 100 logical consistency between h2andh3, and hop by hop proxies
    *   Potential Solutions and Their Limitations Including
        *   DNS Record Advertisement
        *   HP Settings Advertisement
        *   ALPN Negotiation

## Decisions and Action Items

*   **Resumable Uploads:**
    *   Lock down "upload complete" as the preferred header name.
    *   Further discuss the adoption of byte range patch offline or on the issue tracker.
    *   Discuss the integration of upload progress via informational responses on the issue tracker.
*   **Template Driven HTTP Connect using for DCP:**
    *   Find a new terminology for "false start," potentially "optimistically sending."
    *   Address security concerns related to optimistic transmission in HTTP 1.1.
*   **Unprompted Authentication:**
    *   Investigate the feasibility of using exported authenticators instead of the current approach.
    *   Consider defining public keys and public ids instead of binding for authentication.
*   **Structured Fields:**
    *   Use uppercase for percent encoding based on RC 4648 with additional discussion and a second last call.
    *   The retrofit spec will be stepped back from to think about the right shape.
*   **WebSockets Design Team**
    *   The working group is asked to consider the issues related to WebSocket discovery.

## Next Steps

*   Authors to address action items and issues raised during the meeting.
*   Further discussion on the mailing lists for specific topics.
*   Another httpbis meeting to discuss remaining topics.


---

**Session Date/Time:** 28 Jul 2023 00:00

# httpbis

## Summary

The HTTPbis working group session at IETF 117 covered several topics, including secondary certificate authentication, compression dictionary transport, availability hints, cache groups, invalidation API, gateway description, and a new HTTP response header for privacy. The discussions focused on adoption and technical details.

## Key Discussion Points

*   **Secondary Certificate Authentication:** Eric presented a draft on secondary certificate authentication for HTTP servers, focusing on unprompted server authentication for H2 and H3. Jonathan raised concerns about client-side functionality.
*   **Compression Dictionary Transport:** Patrick presented an updated draft on compression dictionary transport, addressing previous privacy and security concerns. The discussion focused on the privacy protections and integration with browsers.
*   **Availability Hints:** Mark Nottingham presented an attempt to improve upon the `Vary` header with "Availability Hints." There was cautious support for exploring it further.
*   **Caching Specifications:** Mark Nottingham presented several caching-related drafts: Cache Groups, Invalidation API, and Gateway Description. Feedback varied on each draft.
*   **HTTP Response Header for Privacy:** Shivan presented a new HTTP response header aimed at improving privacy in browsers. Concerns were raised about its effectiveness and potential for misuse.

## Decisions and Action Items

*   **Secondary Certificate Authentication:** The working group showed interest in adopting the draft as a starting point, focusing on server-side authentication. Tommy created a poll to gauge interest. Result 20 for, 4 against, so the draft will be taken to the mailing list for a call for adoption.
*   **Compression Dictionary Transport:** The working group expressed interest in adopting the draft for compression dictionary transport. Tommy created a poll, which yielded positive results. Result 27 for, 0 against, so the draft will be taken to the mailing list for a call for adoption.
*   **Availability Hints:** The working group was less enthusiastic about adopting availability hints, although there was some support for exploring it further. Discuss on mailing list.
* **Caching Specifications**: No formal poll, but feedback will be taken to mailing list to drive further work.

## Next Steps

*   Post the secondary certificate authentication draft, and compression dictionary transport draft to the mailing list for a call for adoption.
*   Further discussion on the availability hints draft to gather more support and clarify use cases.
*   The new HTTP Response Header for privacy will be forwarded to the WebAppSec working group.
