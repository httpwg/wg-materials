**Session Date/Time:** 23 Jul 2025 07:30

# httpbis

## Summary

The httpbis working group met to discuss several active drafts and the possibility of rechartering the group. Key topics included Layered Cookies, the QUERY method, Resumable Uploads, Incremental HTTP Messages, and a proposal for detecting outdated proxy configurations. Discussions covered technical details, potential implementation challenges, and alignment with existing standards.

## Key Discussion Points

*   **Rechartering:** The group discussed updating the charter to reflect current activities focused on maintaining and developing HTTP extensions. The proposed charter update removes references to completed core work.
*   **Layered Cookies:** An update was provided on the layered cookies draft, which aims to abstract browser-specific requirements. Feedback was requested on reconciling client and server requirements.
*   **QUERY Method:** The discussion focused on defining selected representations and handling conditionals for the QUERY method. There were differing opinions on whether to treat QUERY like GET or POST for conditional requests. The impact on caching was also discussed.
*   **Resumable Uploads:** An update was provided on the resumable uploads draft, which is nearing completion. Interoperability testing and production experience were highlighted. A working group last call was requested.
*   **Incremental HTTP Messages:** The group discussed updates to the incremental HTTP messages draft, which clarifies the use of the incremental header field for bi-directional byte streaming. A working group last call was requested.
*   **Detecting Outdated Proxy Configurations:** A new proposal was presented for detecting outdated proxy configurations using a client header and a server response header. The discussion covered potential use cases, security considerations, and alternative approaches.

## Decisions and Action Items

*   **Rechartering:** The group will continue discussions with the area director regarding the proposed charter update.
*   **QUERY Method:** Julian and Mike will continue to work on defining selected representations and handling conditionals for the QUERY method, considering the impact on caching.
*   **Resumable Uploads:** The working group will start the process for a last call on the resumable uploads draft.
*   **Incremental HTTP Messages:** The working group will start the process for a last call on the incremental HTTP messages draft. Editors will look for client implementation information to include in the draft.
*   **Detecting Outdated Proxy Configurations:** Yaroslav and team will continue refining the proposal, taking into account the feedback received during the meeting. The HTTP request proxying draft from Ben Schwartz may influence it.

## Next Steps

*   Continue discussions on the mailing lists for the QUERY method, proxy configuration detection, and other relevant topics.
*   Begin working group last calls for the Resumable Uploads and Incremental HTTP Messages drafts.
*   Hold the next httpbis meeting on Friday to discuss additional active drafts.


---

**Session Date/Time:** 25 Jul 2025 12:30

# httpbis

## Summary

The HTTPbis working group discussed several active drafts and new proposals. The discussions focused on Unencoded Digests, Secondary Certs, TCP Connect, and Version Translation of the Capsule Protocol. A new proposal for HTTP Request Proxying was also presented. Key themes included addressing implementation challenges, clarifying specifications, and evaluating the need for standardization in specific areas.

## Key Discussion Points

*   **Unencoded Digests:**
    *   Discussion on parameterization of digest fields and potential inconsistencies between the new and old drafts.
    *   Consideration of options including doing nothing, filing an erratum, or issuing a BIS to update existing RFCs.
    *   Clarification that unrecognized parameters should be ignored by default according to Structured Fields.
*   **Secondary Certs:**
    *   Discussion on handling large secondary certificates over HTTP/2 and potential head-of-line blocking issues.
    *   Consideration of a new stream type or server certificate promise frame similar to server push.
    *   Alternative proposal to focus on HTTP/3 over QMux due to limitations of HTTP/2.
    *   General sentiment to keep the specification simple and address more complex issues later if necessary.
*   **TCP Connect:**
    *   Discussion on new connection closure rules and handling of TCP FIN and RESET flags.
    *   Considerations for resource exhaustion attacks and recommendations for limiting receive windows.
    *   Recommendations to avoid HTTP 1.1 were discussed.
    *   Detailed discussion on how to signal resets across different HTTP versions, especially in HTTP 1.1.
*   **Version Translation of the Capsule Protocol:**
    *   Proposal to declare that capsule protocol requests can be translated freely across HTTP versions.
    *   Discussion on potential restrictions on future upgrade tokens.
    *   Concerns about web transport and the need for exceptions or alternative solutions.
    *   Debate on the value of automatic translation versus explicit specification.
    *   Discussion on MTAU in datagram translation and potential codex.
*   **HTTP Request Proxying:**
    *   Presentation of a proposal for templated proxies to address limitations of traditional forward proxies.
    *   Concerns about the security implications of delegating all identity to the proxy.
    *   Alternative suggestions like oblivious HTTP.
    *   Discussion about use cases for proxy usage related to client version incompatibilities.

## Decisions and Action Items

*   **Unencoded Digests:**
    *   The authors will prepare a PR with recommended text changes to ensure consistency.
    *   The working group to decide whether it needs last call
*   **TCP Connect:**
    *   Authors will prepare a PR to simplify text regarding TLS alerts and abrupt stream closure.
    *   The specification to be prepared for working group last call after PR is submitted.
    *   The group should aim to schedule an interrupt test.
*   **Version Translation of the Capsule Protocol:**
    *   Authors to continue discussion on the mailing list based on feedback received.

## Next Steps

*   Authors of each draft to incorporate feedback and prepare updated revisions.
*   Discussion on Version Translation of the Capsule Protocol to continue on the mailing list.
