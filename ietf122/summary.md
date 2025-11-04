**Session Date/Time:** 18 Mar 2025 06:00

```markdown
# httpbis

## Summary

This httpbis session covered several active drafts, including the query method, Connect TCP, optimistic HTTP upgrade security considerations, resumable uploads, and secondary certificates.  Key discussion points included the handling of URL parameters in the query method, the signaling of FIN vs. RESET in Connect TCP, strengthening security recommendations for optimistic upgrades, choosing the correct HTTP method for appending representation data in resumable uploads, and how to handle large secondary certificates. Decisions were made to revise text in several documents.

## Key Discussion Points

*   **Query Method:** Discussion centered on the meaning of URL parameters alongside the query method and how they interact with location headers.  The consensus was that the entire URL, including parameters, identifies the resource, but specific server implementations may interpret them differently. Also, a terminology sweep of the query document is needed.
*   **Connect TCP:**  The session explored options for signaling FIN vs. RESET, specifically whether to introduce a new capsule type ("final data") or rely on transport shutdown.  Arguments were made for and against the new capsule type, considering future extensibility and potential attack vectors.
*   **Optimistic HTTP Upgrade Security Considerations:** The discussion focused on strengthening security recommendations for proxies dealing with clients that don't properly handle non-200 responses.  The primary question was whether to use "must" or "should" for closing connections upon rejection, balancing security and potential compatibility issues.
*   **Resumable Uploads:** The main topic was whether to switch from the PATCH method (with `application/partial-upload`) to POST for appending representation data. Concerns about existing implementations were weighed against semantic arguments.
*   **Secondary Certificates:**  The session considered how to handle large secondary certificates in HTTP/2, where the maximum frame size may be insufficient.  Options included waiving the frame size limit or using a dedicated stream. The session favored a dedicated stream to permit prioritization.

## Decisions and Action Items

*   **Query Method:** Julian to perform a terminology sweep of the document for consistency.  Authors to resolve the URL parameter issue with the guidance from the discussion.
*   **Connect TCP:** Ben to review PR #2949 (which contains the "final data" capsule suggestion) and reopen the issue for discussion on the mailing list. A timebox for discussion was agreed upon.
*   **Optimistic HTTP Upgrade Security Considerations:** Ben to rewrite the section with stronger guidance (possibly "must") and a carve-out for cases where the server has high confidence in its client pool. Ben to address whether this guidance needs to be reflected in RFC 9112.
*   **Resumable Uploads:** No changes to the HTTP method for representation uploads. Authors to keep PATCH method.
*   **Secondary Certificates:** Investigate the dedicated stream solution in more detail. Mike to offer assistance in exploring different directions and design details on the mailing list. The authors are asked to come up with design suggestions.

## Next Steps

*   **Query Method:** Once the issue is resolved and the terminology sweep is completed, the document will be submitted for Working Group Last Call.
*   **Connect TCP:** Mailing list discussion on PR #2949.
*   **Optimistic HTTP Upgrade Security Considerations:** Ben to circulate revised text.
*   **Resumable Uploads:** Proceed with the document as is.
*   **Secondary Certificates:** Mailing list discussion to present various design choices for a dedicated stream-based solution, with assistance from Mike.


---

**Session Date/Time:** 21 Mar 2025 06:00

# httpbis

## Summary

This session covered several active drafts and proposals, including No Very Search, Incremental HTTP Messages, Unencoded Digests, Delete Cookie, HTTP-Only Cookie Prefix, the New Cookie Spec, and Client Hints Visibility. Key discussions revolved around adoption readiness, potential complexities, and the balance between performance, privacy, and implementation feasibility.

## Key Discussion Points

*   **No Very Search:**
    *   Ready for last call according to the presenter.
    *   Discussion on Google's multiple implementations vs. limited external deployments.
    *   Need for more client-side cache implementations.
    *   Consideration of marking the draft as updating RFC 9111.

*   **Incremental HTTP Messages:**
    *   Debate on the complexity of tri-state modes (incremental preferred, not preferred) versus a simple "hard fail" approach.
    *   Whether to include signal mechanism for intermediaries.
    *   Definition of "incremental" in terms of time and byte limits for buffering.

*   **Unencoded Digests:**
    *   Proposal for adoption and publication.
    *   Question on whether another digest header would add confusion.
    *   Use case tied to Signature-based SRI work.

*   **Delete Cookie and HTTP-Only Cookie Prefix:**
    *   Adoption requests for both drafts.
    *   Discussion on folding them into the larger, in-progress cookie specification revision.
    *   Interest in how these changes touch components like partition cookies and third-party cookie blocking.

*   **New Cookie Spec:**
    *   Proposal for adoption.
    *   Integration with Fetch and the Cookie Store API.
    *   Need for advice from the group regarding server objectives, particularly around cookie deletion.

*   **Client Hints Visibility:**
    *   Should the problem be addressed?
    *   Does implementation using Aliphites and Access Frame justify adopting as a draft?
    *   Discussion of TLS draft adoption as prerequisite.
    *   Concern about adaptive content, the responsibility for adaptation, and associated privacy implications.
    *   Doubts on a frame signalling this.
    *   Concrete use cases that unlock benefit the user and benefit the client need to be clear

## Decisions and Action Items

*   **No Very Search:**
    *   File an issue for formally marking the draft as updating RFC 9111 and discuss more with Mark.
    *   Continue working in group last call, while parking for a short time
*   **Delete Cookie and HTTP-Only Cookie Prefix:**
    *   Run an adoption call on each individual draft
*   **New Cookie Spec:**
    *   Chairs (Tommy and Mark) to initiate the adoption process.

## Next Steps

*   **All:** Review discussed drafts and provide feedback on the mailing lists.
*   **Client Hints Visibility:** Share the use cases with the group and updates from any conversations with W3C.
