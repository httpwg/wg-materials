**Session Date/Time:** 07 Nov 2022 15:30

# httpbis

## Summary

This httpbis meeting covered several topics, including HTTP message signatures, alternative services, origin H3, cookies and partitioned cookies, client certificates, and a status update from the MASK working group. Discussions focused on open issues, design considerations, and potential future directions for each topic.

## Key Discussion Points

*   **HTTP Message Signatures:** Discussion centered on handling trailers in HTTP message signatures, specifically whether to treat header and trailer fields as distinct namespaces and the implications for signing trailers. Justin Richer will add a PR to include a trailer flag.
*   **Alternative Services:** Mike Bishop presented on alt service B, an alternative to the existing alt service mechanism. Discussion focused on stickiness, DNS integration, and whether alt service B should completely replace old service. The discussion points to a general interest in https records and having some control over the use of an alternative.
*   **Origin H3:** The main topic was handling flags in the origin frame for H3, given that H3 does not have flags in the same way as H2. Participants leaned towards deprecating flag usage.
*   **Cookies:** Stephen Bingler provided a status update on RFC 6265bis, including the case-insensitive handling of cookie prefixes and open issues related to same-site cookies, internal whitespace, and clearer implementation guidance.
*   **Partitioned Cookies:** Dylan Cutler presented on partitioned cookies (CHIPS), a proposal for a new cookie attribute that would limit third-party cookies to the top-level site where they were created. The discussion covered handling partitioned cookies in unpartitioned contexts, the use of a cross-site ancestor bit, and handling cookies with the same name but different partition attributes.
*   **Client Certificates:** Mark Nottingham shared an update on Client Certificates, emphasizing open issues from Lucas Conley and that the group is nearing working group last call.
*   **MASK:** David Schinazi provided an overview of the MASK (Multiplexed Application Substrate over QUIC Encryption) working group, its goals, current status, and potential future directions, including extensions for CONNECT UDP and HTTP datagrams. The discussions highlighted the goal of creating a VPN that looks like regular web traffic.
*    **Unprompted Authentication:** David Schinazi introduced a draft on unprompted authentication using TLS key exporters.  Ben Schwartz had concerns regarding the need for the design and potential alternatives. There was some interest to explore the design in the group.

## Decisions and Action Items

*   **HTTP Message Signatures:** Justin Richer will submit a PR to add a TR flag to define trailer data sources.
*   **Origin H3:** Close the issue with no action and Kick the Can down the road
*   **Alternative Services:** Continue discussion on the alt service B draft and leave the old service best document parked.
*   **Cookies:** Close three open issues in 6265bis, go through working group last call and then start almost an immediate revision.
*   **Partitioned Cookies:** Align with spec work at the W3C.
*   **Client Certificates:** Continue working group last call, address open issues.
*   **Unprompted Authentication:** Explore issues and use cases, why the current solution is appropriate.

## Next Steps

*   Continue discussions on the mailing lists for all topics.
*   Authors to address action items and open issues.
*   Consider a call for adoption for alt service B after further discussion.
*   Potential re-chartering of the MASK working group for future extensions.


---

**Session Date/Time:** 11 Nov 2022 09:30

```markdown
# httpbis

## Summary

This was a full session covering several topics, including resumable uploads, retrofit structured fields, query, origin deployment, modern HTTP proxies, and HTTP authentication with SASL.  Key discussions revolved around technical design choices, potential dependencies, and implementation considerations.

## Key Discussion Points

*   **Resumable Uploads:**
    *   Server-generated URLs vs. client-generated tokens for identifying uploads.  The group showed a preference for server-generated URLs.
    *   Use of item potency keys for the upload creation procedure, including potential collisions. Concerns were raised.
    *   Identifying the upload creation procedure, specifically the use of the "Prefer" header. Alternative solutions using a new custom header were also proposed.
    *   Interaction between "Expect: 100-continue" and informational responses.
    *   The need for including hashes to validate the integrity of the uploaded file.
*   **Retrofit Structured Fields:**
    *   Location of compatibility modifications (specifically whitespace handling) - whether to include in structured fields spec or keep only in retrofit document. General agreement to include in structured fields spec with a compatibility flag.
    *   Differences in error handling compared to HTTP parsing.
    *   Adding mapped fields for Authorization and WWW-Authenticate.
*   **Query:**
    *   Editorial improvements needed around documentation and motivation.
    *   Defining semantics for form-based media types in relation to query.
    *   Addressing redirections, conditional queries, and caching.
*   **Origin Deployment:**
    *   The effect of congestion control window on the transfer of sub-resources.
    *   Breakdown of different protocols and their potential impact on performance.
    *   Consideration of the cache's effect (cold vs. warm) on performance.
*   **Modern HTTP Proxies:**
    *   Splitting the TCP connect and request proxying aspects of the draft. There was more support for the TCP connect proposal.
    *   Charter scope and potentially moving the TCP connect portion to the mask working group.
    *   Whether using this is enough of a good idea for all the Legacy proxy implementations to rewrite it onto this new way of doing things.
*   **HTTP Authentication with SASL:**
    *   Concerns over whether Sasol is a security protocol and should be in the security area.
    *   Integrating with browser APIs. If it is possible to do in a self-service fashion then that gives you an opportunity to demonstrate a utility without necessarily requiring everyone in the in the ecosystem to implement something.
    *   Applicability to client libraries like Curl.

## Decisions and Action Items

*   **Resumable Uploads:** The draft will be updated to reflect the preference for server-generated URLs.
*   **Retrofit Structured Fields:** The draft will be updated to incorporate compatibility modifications into structured fields spec using a flag.
*   **Modern HTTP Proxies:** Ben will create a new document that is smaller and more focused on TCP connect. They will be split out and the message proxying will be separated. The TCP connect document will be taken to the list.
*   **HTTP Authentication with SASL:** Chairs to discuss next steps.

## Next Steps

*   Authors to update drafts based on meeting feedback.
*   Continue discussion on the mailing lists, especially for adopted drafts.
*   Chair to follow up on action items and decide future steps for HTTP Authentication with SASL.
