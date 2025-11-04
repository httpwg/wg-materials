**Session Date/Time:** 09 Nov 2023 14:00

# httpbis

## Summary

This httpbis meeting covered several active drafts and proposals. Key topics included Compression Dictionary Transport, Cookies, Unprompted Authentication, Query Method, Retrofit Structured Fields, Cash Groups, and the Qpex Static Table version TLS extension. The meeting focused on discussing ongoing issues, potential solutions, and future directions for each topic.

## Key Discussion Points

*   **Compression Dictionary Transport:**
    *   Discussion on replacing the custom wildcard implementation with URL pattern.
    *   Consideration of adding "match desk" to match on fetch destination.
    *   Proposal to reduce the default TTL to 7 days.
    *   Discussion on sorting the accepting coding header and requiring dictionary versions to include support for non-dictionary versions.
    *   Adding dictionary source URL and eTag for the dictionary.
*   **Cookies:**
    *   Discussion on the SameSite cookies and redirects issue and the ongoing experiment in Chrome.
    *   Consideration of potentially removing the SameSite redirect requirement for now to allow the spec to progress.
*   **Unprompted Authentication (Signature HTQ Authentication Scheme):**
    *   Decision to keep the current design and not switch to exported authenticators.
    *   Discussion on the exporter context parameters.
    *   Status of implementation and future steps.
*   **Query Method:**
    *   Call for design team participants to speed up progress on the open issues.
*   **Retrofit Structured Fields:**
    *   Announcement of another working group last call for a week to confirm non-ASCII string formats.
*   **Cash Groups:**
    *   Brief overview of the new cash control mechanism to group together responses.
*   **Qpex Static Table version TLS extension:**
    *   Proposal to define the qpact static table in a registry.
    *   Enable new headers to get added to the table.
    *   Negotiation scheme using a TLS extension.
    *   Discussion on whether this should be a TLS extension or use ALPS.
    *   The need for performance data and governance on selecting headers was strongly highlighted.

## Decisions and Action Items

*   **Compression Dictionary Transport:**  Patrick to consider feedback regarding URL and eTag.
*   **Cookies:**  Decision to remove the SameSite redirect requirement from the spec if a solution cannot be found soon.
*   **Query Method:** Form a design team and coordinate with Julian.
*   **Retrofit Structured Fields:** Kick off another short working group last call.
*   **Qpex Static Table version TLS extension:** Collect performance data and consider governance on selecting headers.

## Next Steps

*   **Compression Dictionary Transport:** Continue discussion and refinement of the draft.
*   **Cookies:**  Await results of Chrome experiment and decide on the SameSite redirect requirement.
*   **Unprompted Authentication:** Update implementation and continue interoperability testing.
*   **Query Method:** Form the design team and schedule a Telco.
*   **Retrofit Structured Fields:** Kick off the working group last call.
*   **Cash Groups:**  Encourage review and contributions to the spec.
*   **Qpex Static Table version TLS extension:** Collect performance data and further explore the design options.


---

**Session Date/Time:** 10 Nov 2023 12:00

```markdown
# httpbis

## Summary

This httpbis meeting covered a variety of topics, including updates on active drafts for resumable uploads and connect TCP, as well as discussions on several proposals: security considerations for optimistic HTTP upgrade, reverse HTTP transport, secondary cert authentication of servers, braid, and per-resource event protocol.  The meeting focused on technical details, implementation considerations, and potential next steps for each of these areas.

## Key Discussion Points

*   **Resumable Uploads:**
    *   Discussion around the appropriate media type for PATCH requests used in resumable uploads, with options including `application/octet-stream`, a new media type like `application/offset+octet-stream`, and potentially leveraging "partial put" semantics.
    *   Debate regarding how to handle responses in the context of transparently upgrading regular uploads to resumable uploads, particularly concerning lost responses and error codes.
    *   Review of a proposal to use informational responses (104) to carry upload progress, including discussion on whether location header should be mandatory.
    *   Interoperability with HTTP Digest and whether the draft should specify behavior when checksums don't match for interrupted PATCH requests.
*   **Connect TCP:**
    *   Discussion of adding a default template to Connect TCP, mirroring the approach in Connect UDP and Connect IP.
    *   Consideration of the document's relationship with optimistic upgrade, particularly whether that work should be adopted before last call on Connect TCP.
    *   Motivation of the work. Lack of host name specification in legacy Connect.
*   **Security Considerations for Optimistic HTTP Upgrade:**
    *   Discussion around the security implications of optimistic transmission in conjunction with HTTP upgrade.
    *   Guidance for creating new upgrade tokens, particularly concerning the interaction of attacker-controlled data and the upgrade payload.
    *   The existing issue with Connect UDP
*   **Reverse HTTP Transport:**
    *   Exploration of reverse HTTP transport, where the origin server acts as a transport client.
    *   Discussion of potential standardization of this pattern to address limitations with proprietary implementations.
    *   Concerns about role reversal and the interaction with H3.
*   **Secondary Cert Authentication of Servers:**
    *   Discussion about scope and the use cases of secondary server certificates.
*   **Per Resource Event Protocol (PREP):**
    *   Overview of PREP and its simple multi-part message format.
    *   The desire for event format negotiation.
    *   Discussion on the benefits of PREP, in constrast to other push protocols.
*   **Braid:**
    *   This proposal to change the core scope of HTTP to also include synchronization.
    *   Discussion of the concept of state synchronization in HTTP and the Braid HTTP draft.
    *   Discussion to the adoption of subscription model and CRDT.

## Decisions and Action Items

*   **Security Considerations for Optimistic HTTP Upgrade:** The working group showed support for the adoption of the draft. A call for adoption will be made on the mailing list.
*   **Connect TCP:** Take the discussion to the issue tracker to discuss template default values.
*   **Secondary Cert Authentication of Servers:** Take the discussion to the list to discuss implementation interest.

## Next Steps

*   **Resumable Uploads:** Continue discussion on open issues, particularly those related to media types, response handling, and checksum verification.
*   **Connect TCP:** Take the discussion on the pros and cons of a well-known URI Template to the github issue.
*   **Security Considerations for Optimistic HTTP Upgrade:** A formal call for adoption will be sent to the mailing list.
*   **Reverse HTTP Transport:** Continue discussion on the mailing list regarding the direction and scope of the proposal, particularly considering the feedback regarding alternative approaches and existing solutions.
*   **Secondary Cert Authentication of Servers:** Take the discussion to the mailing list to discuss implementation interest, next a call for adoption.
*   **Per Resource Event Protocol (PREP) and Braid:** Initiate discussions on the mailing list to explore the individual component standards to support subscriptions, HTTP patch and CRDT and if the effort can be decomposed.
