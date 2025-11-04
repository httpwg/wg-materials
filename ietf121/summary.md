**Session Date/Time:** 04 Nov 2024 09:30

# httpbis

## Summary

This IETF 121 meeting covered several active drafts and new topics, including resumable uploads, query methods, cache groups, incremental HTTP messages, wrap-up capsules, capsule protocol extensions, and cookie deletion. The group discussed technical details, potential interoperability issues, and future directions for these areas. Several proposals gained support, and action items were identified for document updates and further exploration.

## Key Discussion Points

*   **Resumable Uploads:** The draft is nearing completion after recent updates and hackathon interoperability testing. Concerns were raised regarding client handling of intermediate responses (1XX status codes), and the potential need for an implementation note regarding interoperability, as well as the exposure of these codes to application developers. The use of OPTIONS for upload limit detection was also discussed.
*   **Query Method:** The meeting addressed open issues related to conditional query semantics, the `Accept-Query` header (including the choice between structured fields and the existing `Accept` header syntax), media type semantics, cache key normalization, and the use of direct vs. indirect responses.
*   **Cache Groups:** The draft is nearing completion after feedback from the last call was addressed. The chairs encouraged more participation from cache vendors in reviewing the specification.
*   **Incremental HTTP Message:** This new proposal aims to address the inconsistency in incremental delivery of HTTP messages due to buffering intermediaries. The discussion included alternative error signaling mechanisms (warn vs. fail), client behavior on receiving errors, and applicability to both requests and responses.
*   **Wrap-up Capsule:** This proposal for a mechanism to signal graceful flow termination gained support. The potential for client-initiated wrap-up and the inclusion of a retry bit in the capsule were discussed.
*   **Capsule Protocol Extensions:** This proposal aimed at fixing and improving how Capsule Protocols operate with different capsule types, the need for better error codes, and negotiation of new types was considered to need improvements. A debate on if unknown type endpoints included proxies ended with guidance and lessons learned to make sure implementations treat the packets as expected.
*   **Cookie Deletion:** A proposal to add a `Delete-Cookie` header was presented, allowing servers to delete cookies without knowing the domain and path. Discussions included deleting multiple cookies with the same name, addressing cookie confusion attacks, and whether this change should be incorporated into the next cookie revision draft.

## Decisions and Action Items

*   **Resumable Uploads:** Authors to perform an editorial pass of the draft and incorporate an implementation note regarding handling of intermediate responses. Add a test case for multiple 1XX responses to the demo server.
*   **Query Method:** Authors to proceed with the proposed solutions for open issues, leveraging structured fields for the `Accept-Query` header, and aiming for a working group last call after updates.
*   **Cache Groups:** A participant will provide a positive statement about the draft to the mailing list to support the last call process.
*   **Wrap-up Capsule:** Working group chairs to schedule an adoption call for this draft.
*   **Capsule Protocol Extensions:** Review and address proposed improvements/guidance for capsule treatment for adoption consideration.
*   **Cookie Deletion:** Authors to prepare an Internet Draft for the `Delete-Cookie` header, which will then be considered for incorporation into the next cookie revision draft. The proposed mechanisms should then be discussed and added to the BIS document.

## Next Steps

*   Authors will update drafts based on the discussions.
*   The working group will conduct adoption calls for the wrap-up capsule and capsule protocol extensions proposals.
*   The working group will continue discussions on the mailing list.
*   The next meeting will be held on Thursday to discuss additional topics.


---

**Session Date/Time:** 07 Nov 2024 17:30

# httpbis

## Summary

The HTTPbis working group meeting covered several topics, including a discussion on a draft proposing a YANG grouping for HTTP client/server configuration, the Connect TCP draft, Security Considerations for Optimistic Protocol Transitions, No Vary Search, and a new proposal for geolocation using HTTP client hints.  The main discussion centered on the use of HTTP client hints for geolocation and the trade-offs between user privacy and providing relevant location information to servers.

## Key Discussion Points

*   **YANG Grouping for HTTP Client/Server Configuration:** Concerns were raised about the draft's configuration options for explicitly selecting HTTP versions, potentially circumventing protocol negotiation mechanisms and hindering future HTTP evolution.  Consensus leaned towards removing this configuration knob.
*   **Connect TCP:**  Discussion focused on whether to mandate both "Connect TCP" and "Connect TCP Capsule" upgrade tokens, or only one. The potential for user confusion with URI templates and upgrade tokens was debated, alongside the use of capsules.  The group seemed to lean toward consolidating on a single protocol, capsule-only.
*   **Security Considerations for Optimistic Protocol Transitions:** This draft included new text related to HTTP Connect. An issue regarding proxy-initiated connection closures and their negative impact on performance and correct implementation was raised. Consideration of HTTP version applicability was discussed.
*   **No Vary Search:**  The draft, which replaces a requirement in RFC911, allows a cache to examine stored responses to determine reusability for a request. Discussion included how to efficiently implement it and concerns about the name "search".
*   **IP Geolocation:**  The main discussion revolved around a proposal to use HTTP client hints to send a coarse geolocation to servers while masking the client's IP address.  Concerns were raised regarding the potential for misuse, the interaction with VPNs, and the overall privacy implications. There was discussion of leveraging existing knowledge from the IETF's geo-privacy work.

## Decisions and Action Items

*   **YANG Grouping for HTTP Client/Server Configuration:** Authors should further discuss the community feedback and consider removing the HTTP version selection configuration options.
*   **Connect TCP:** Ben to consolidate on a single protocol, capsule-only.
*   **Security Considerations for Optimistic Protocol Transitions:** Ben to add text to address HTTP version limitations of the normative text. Eric to provide more details about issues experienced with proxy connection closures.
*   **IP Geolocation:**  The working group will not adopt the current document, but instead will further explore the requirements for geolocation in a privacy-preserving fashion.

## Next Steps

*   Authors of the YANG grouping draft to consider feedback and potential revisions.
*   Ben to update the Connect TCP draft and consolidate.
*   Ben to update the Security Considerations draft to address the HTTP version and proxy connection closure concerns.
*   Jeremy to continue working on No Vary Search.
*   Continue discussing the requirements for IP Geolocation on the mailing list.
