**Session Date/Time:** 19 Mar 2024 07:30

# httpbis

## Summary

This meeting covered updates and discussions on several HTTP-related drafts, including cookie specification, signature authentication, query method, and resumable uploads. The main discussion points were the resolution of the "same site redirect chain" issue in the cookie spec, the introduction of a new header for key exporter in the signature authentication scheme, the media type and upload limits in the resumable uploads draft, and a deprecation request for HTTP signature scheme.

## Key Discussion Points

*   **Cookie Spec (6265bis):**
    *   The "same site redirect chain" issue was resolved by reverting the relevant language.
    *   Working group last call planned after updating the IANA section and a few minor remaining issues are resolved.
    *   Discussion about a more continuous evolution of the cookie spec.

*   **Signature Authentication (formerly Unprompted Authentication):**
    *   Interop testing was successful with editorial clarifications and a security review completed.
    *   Proposal to define a new header to send the exporter to the upstream HTTP server. There was much discussion around the utility of this header.
    *   Discussion and bike-shedding around renaming the authentication scheme to avoid collisions, alternatives: "hidden," "masked," "client-initiated", "unprompted" or "signature2".

*   **Query Method:**
    *   The draft has been stalled for a while. A side meeting is planned for Thursday at 5 PM local time to move it forward.

*   **Resumable Uploads:**
    *   Updates in draft version 3 included progress notifications and clarification on the use of empty requests.
    *   Discussion around the media type for patch requests, with a proposal to use "application/partial-upload".
    *   Discussion on upload limits with options for announcing them via new header fields (either multiple headers or a single dictionary header).
    *   Discussion about partial changes on patch requests
    *   Discussion about how content coding should be handled when resuming uploads. Recommendation is to omit the content encoding header upon resuming.

## Decisions and Action Items

*   **Cookie Spec:** Publish a new draft with the current set of changes, followed by a working group last call (at least 4 weeks).
*   **Signature Authentication:**
    *   Editors to discuss and choose a new name for the authentication scheme based on the working group's input and chair's guidance.
    *   David to incorporate editorial feedback, especially related to the rationale for the approach taken.
*   **Query Method:** Side meeting to be held on Thursday at 5 PM local time.
*   **Resumable Uploads:**
    *   Incorporate feedback on upload limits (optional, using relative times).
    *   Add language regarding the interpretation of "atomic" patch application in the context of resumable uploads.
    *   Deprecate the previous signature HTTP scheme

## Next Steps

*   **Cookie Spec:** Publish updated draft and prepare for working group last call.
*   **Signature Authentication:** Choose a new name and update the draft.
*   **Query Method:** Hold side meeting and make progress on resolving open issues.
*   **Resumable Uploads:** Address open issues and prepare for a new draft release.


---

**Session Date/Time:** 21 Mar 2024 23:30

# httpbis

## Summary

This meeting covered several active drafts including templated connect TCP, security considerations for optimistic use of HTTP upgrade, retrofit structured fields, cash groups, and compression dictionary transport.  Additionally, several informational presentations were given, including HTTP 3 on streams, reverse HTTP tunnels, window sizing for Z Standard Content and Coding, and best practices for link local connectivity. A key theme was balancing new features with implementation complexity and backward compatibility.

## Key Discussion Points

*   **Templated Connect TCP:**
    *   Discussion around using `TCPport` vs `targetport` for identifying connect TCP support in multi-protocol proxy templates.
    *   Concerns raised about probing for protocol support and the need for explicit usage indication.
    *   Debate over including happy eyeballs/target host list functionality, with arguments for dropping it in favor of a generic solution.
    *   Discussion of using capsules and if the protocol needs explicit inclusion or exclusion of capsules.
*   **Security Considerations for Optimistic Use of HTTP Upgrade:**
    *   Proposal to close the connection after replying with a non-upgraded response to prevent issues.
    *   Discussion on whether upgrade tokens should ever have a body.
    *   Agreement to delete `upgrade HTTP/2.0` and `upgraded TLS` from the IANA registry.
*   **Retrofit Structured Fields:**
    *   Acknowledged that progress on this spec has been light, but will resume, now that SFbis is nearly complete.
    *   Discussed the need for more real-world use cases before publishing.
*   **Cash Groups:**
    *   Discussions on refining implementation details, such as the number of labels supported per response.
    *   Debate over including revalidation feature, and the need for a solid implementation experience with it.
    *   Consideration of dropping the revalidation feature from the current draft and the option of utilizing extensions in the future.
    *   Discussion about a potential name change for the specification.
*   **Compression Dictionary Transport:**
    *   Updates on Chrome 123 including changes from draft 3 and a new origin trial for compression dictionary v2.
    *   Server is required to send the `content-dictionary` response header with the hash of the dictionary used.
    *   Discussion of specifying a single compression algorithm (Zstandard or Brotli).
    *   Concerns about linear search for dictionary matching and potential denial of service risks.
    *   Requests about moving to byte stream format for available dictionary hashes.
*   **HTTP 3 on Streams:**
    *   Presentation of an alternative to H2 via utilizing Quick on TCP to alleviate reliance on UDP and H2 implementations.
    *   Highlighted concurrency issues in HTTP/2, particularly the rapid reset attack.
    *   Advocated for reusing existing Quick/HTTP/3 implementations.
    *   Discussion on a potential HTTP 2.1 as well as HTTP 3 over TCP as options.
*   **Reverse HTTP Tunnels:**
    *   Proposal to use HTTP extended CONNECT to establish reverse tunnels instead of TLS.
    *   Arguments for flexibility in tunnel parameters and authentication schemes.
    *   Discussion on whether to support HTTP/3 and TCP relay mode.
*   **Window Sizing for Z Standard Content Coding:**
    *   Proposal to require support for at least 8MB window sizes for Zstandard content coding to improve interoperability and to prevent related issues.
*   **Best Practices for Link Local Connectivity:**
    *   Discussion about a problematic RFC 6874 standard which causes browser issues.
    *   Presentation of MDNS and Multicast DNS as alternatives.

## Decisions and Action Items

*   **HTTP Upgrade:** Delete `upgrade HTTP/2.0` and `upgraded TLS` from IANA registry.
*   **Z Standard Content Coding:** Proceed to working group last call for the draft requiring support for 8MB window sizes.
*   **Templated Connect TCP:** Revise draft.
*   **Compression Dictionary Transport:** Further discussion on concerns about linear search for dictionary matching and potential denial of service risks.

## Next Steps

*   Further discussion and potential revision of Templated Connect TCP based on feedback.
*   Continued discussion and refinement of requirements for happy eyeballs/target host lists functionality.
*   Discussion for HTTP 3 on streams to be continued as well as potential future discussion in an HTTP workshop.
*   Further exploration of security implications and implementation challenges for reverse HTTP tunnels.
*   Joint proposal between alternative solutions for reverse HTTP tunnels to be discussed eventually and for HTTP WG to be involved.
*   Proceed to working group last call for draft on Window Sizing for Z Standard Content Coding.
*   Follow-up on actions needed for Best Practices for Link Local Connectivity in relevant IETF groups.
