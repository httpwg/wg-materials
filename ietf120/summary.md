**Session Date/Time:** 22 Jul 2024 20:00

# httpbis

## Summary

The httpbis working group meeting covered three active drafts: resumable uploads, identifying query results, and cache groups. There was also a presentation about communicating proxy configuration and provisioning domains in the `int` area, and a discussion about it's relevance to the group.

## Key Discussion Points

*   **Resumable Uploads:**
    *   Discussion on discovering upload limits upfront using OPTIONS requests and its potential integration with CORS pre-flight requests.
    *   Debate about including an advisory `Upload-Length` header in creation requests to inform the server of the total upload size. Concerns about backward compatibility with existing servers were raised.
    *   Discussion on integrity checks using the `Digest` field and whether its use aligns with the intended purpose of the integrity preference fields defined in RFC.
*   **Identifying Query Results:**
    *   Debate on whether to use `Location` or `Content-Location` headers to identify a gettable resource for a query and it's caching behavior. A proposal to allow both `Location` and `Content-Location` headers, each serving distinct purposes, was discussed and generally favored.
    *   Discussion on whether or not to allow cached query responses to be reused for subsequent requests, similar to the behaviour already allowed with `POST` requests. Concerns were raised around security implications.
*   **Cache Groups:**
    *   Discussion regarding a revision that removes speculative invalidation. A request for review and a call for implementation were made.
*   **Communicating Proxy Configuration and Provisioning Domains (Int Area Presentation):**
    *   Overview of the `int` area document about discovering proxy configurations using provisioning domains. The document leverages an HPS-protected JSON file associated with a way to reach a network.
    *   Discussion on how to handle the `protocol` field, and consider a HTTP-prefix.
    *   Discussion on the two bootstrapping mechanisms, and network discovery.
    *   Discussion about integrating legacy types of authentication, like "unprompt off."
    *   Concern was raised about the use cases for pack files that defines exceptions, and discussed how the document allows the same, through the split DNS config.

## Decisions and Action Items

*   **Resumable Uploads:** Marius to follow up with Lucas on the use of integrity preference fields. Marius will add a hint about backward compatibility with existing servers.
*   **Identifying Query Results:** Julian and Mike to work on a proposal that defines the behavior of both `Content-Location` and `Location` headers. The chairs will add Mike to the draft's authors.
*   **Cache Groups:**  Working group to review the draft for last call.
*   **Communicating Proxy Configuration and Provisioning Domains:** Consider using `HTTP` prefix to better distinguish it from socks.

## Next Steps

*   Continue discussion and refinement of the Resumable Uploads and Identifying Query Results drafts.
*   Proceed with working group last call for the Cache Groups draft pending review.
*   Follow up on action items and continue work on open issues.


---

**Session Date/Time:** 24 Jul 2024 20:00

```markdown
# httpbis

## Summary

This httpbis session covered a range of topics, including security considerations for HTTP upgrade, server certificate authentication, privacy proxy enhancements, cache performance improvements, and resource versioning. Discussions focused on technical details, implementation challenges, and the potential for standardization.

## Key Discussion Points

*   **Optimistic HTTP Upgrade:**  Debate over deprecating the HTTP upgrade token in the IANA registry and whether the draft should address this. The group also discussed extending the scope to include HTTP Connect. Recommendations to restrict upgrade tokens to GET and avoid request bodies. Concerns about TLS upgrade token safety and the potential for misinterpretation of TCP streams.

*   **Secondary Certificate Authentication:**  Discussion regarding the ability for clients and servers to agree on the used certificate. The group also addressed the ability to send exported authenticators in multiple frames for HTTP/2 and potential solutions like continuation flags or certificate compression.  A decision to rename the frame from "certificate" to "server certificate".

*   **Privacy Proxy Wrap-up Capsule:** Presentation of a new capsule type to signal clients to switch privacy proxies gracefully during maintenance or resource exhaustion.  Discussions centered on distinguishing between relays and use cases beyond privacy proxies, with proposals to leverage go-away signals.

*   **No Very Search:**  Presentation of the No Very Search header for optimizing cache performance by allowing servers to indicate which query parameters do not affect the response. Discussion included data on performance improvements and potential adoption by CDNs.

*   **Revised Cookies:** Presentation on the Cookie Store and refactoring cookies for better integration with browser specs (HTML and Fetch) rather than describing browser behavior.

*   **HTTP Resource Versioning:** Proposal for a general versioning architecture for HTTP resources, including headers for specifying versions and parents to track history. Discussions focused on use cases like incremental RSS updates, Git repository hosting, and resumable uploads, as well as compatibility with existing HTTP features and potential implementation challenges.

## Decisions and Action Items

*   **Optimistic HTTP Upgrade:** The group will rework the section regarding TLS upgrade token to avoid strong claims, suggesting it be reworked. Ben will update the text and bring it to the group.
*   **Secondary Certificate Authentication:** The group will follow up on the GitHub issue regarding sending exported authenticators in multiple frames. Decision to rename the "certificate" frame to "server certificate".
*   **Privacy Proxy Wrap-up Capsule:** Discussions to continue and David to modify his draft a bit.
*   **No Very Search:** The group will take the proposal to the mailing list for further discussion, and potential CDN adoption.

## Next Steps

*   **Optimistic HTTP Upgrade:** Ben will update the TLS upgrade token section of the draft.
*   **Secondary Certificate Authentication:** Follow up on GitHub issue and update draft to rename frame.
*   **Privacy Proxy Wrap-up Capsule:** Continued discussion and draft revisions.
*   **No Very Search:** Discussion on the mailing list regarding CDN adoption.
*   **Revised Cookies:**  Chairs to reach out and determine next steps for cookies.
*   **HTTP Resource Versioning:** Participants to review the draft and provide feedback on the mailing list. Michael will consider the suggested framework and testing recommendations.
