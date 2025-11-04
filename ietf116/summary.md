**Session Date/Time:** 28 Mar 2023 06:30

# httpbis

## Summary

The httpbis working group met to discuss several ongoing drafts, including cookies, DNS aliases in the Proxy-Status header, and unprompted authentication. Discussions focused on clarifying existing issues, incorporating feedback, and outlining future directions.

## Key Discussion Points

*   **Message Signatures:** A potential normative change related to encoding and retrieving octets was discussed. The consensus was to update examples and clarify intent. A PR will be created and circulated for review, with a new draft released shortly thereafter.
*   **Cookies:** The editor provided an update on draft-ietf-httpbis-rfc6265bis-11 and changes going into -12. Open issues include whitespace in cookie names and values (specifically Htabs) and same-site cookie handling during redirects. A timeline for working group last call was discussed (aiming for prior to IETF 117).
*   **DNS Aliases Proxy Status Header:** Two open issues were identified and pull requests were created. Discussions centered on including the full CNAME chain in the next-hop-aliases parameter and addressing potential skipping rules, as well as a discussion around the threat model. The goal is to finalize the draft and enter working group last call before the next meeting.
*   **Unprompted Authentication:** Several issues were discussed:
    *   Registry for signature and hash algorithms. The group will investigate existing IANA registries and potentially create a new one if necessary.
    *   Concerns were raised about adding HMAC support. It was agreed to drop HMAC support for now and focus on signature schemes. Existing TLS signature schemes may be used.
    *   Reusing the existing Authorization header was discussed. The group will investigate potential issues with user agents not recognizing new schemes and will consider renaming the draft to reflect its focus on channel-bound authentication schemes.
    *   Discussion around exporter contexts with the proposal being to include the algorithm in use, the key identifier as well as the origin.

## Decisions and Action Items

*   **Message Signatures:**
    *   Justin will update examples and clarify intent in a PR.
    *   A new draft will be released after PR review.
*   **Cookies:**
    *   Stephen will continue to work on resolving the same-site redirect issue.
    *   Working group last call to be targeted for before IETF 117.
*   **DNS Aliases Proxy Status Header:**
    *   Tommy to revise the document to include the PR and additional reviews.
    *   Ben to create issue for skipping rules that are not totally right
    *   Chris to file an issue outlining how the Proxy is doing DNS, and what are the implications.
    *   Discuss list vs string format after the meeting.
    *   Tommy will include the full CNAME chain in the next-hop-aliases parameter.
    *   Target working group last call for before the next meeting.
*   **Unprompted Authentication:**
    *   David will investigate existing IANA registries for signature and hash algorithms.
    *   David will drop HMAC support.
    *   David will use the existing Authorization header and look into proxy authorization, but also ensure that existing protocols will continue to work.
    *   David will check there are no explicit bans on using Basic or Digest without four zero one.
    *   David will add context information in the Tls key exporter including which algorithm, key identifier, and origin and excluding URL.
    *   David will talk with Jonathan (from Cloudflare) on security analysis.
    *   David will reuse realm instead of URL.
    *   Comment on issue that is about adding context string next to nonces.
    *   Name the draft after "channel bound"

## Next Steps

*   The discussed PRs and drafts will be updated and circulated for review.
*   The chairs will monitor the progress on these documents and determine the next steps, including whether to initiate working group last calls.
*   The working group will continue to discuss the outstanding issues on the mailing list.


---

**Session Date/Time:** 31 Mar 2023 00:30

# httpbis

## Summary

The httpbis working group met to discuss several draft specifications, including uploads, structured fields, retrofit headers, and an alternative to Alt-Svc.  A new proposal regarding Websocket discovery and detection was presented.  The group also discussed modernizing HTTP proxies. Several decisions were made to proceed with working group last calls on certain specifications while continuing discussions on others.

## Key Discussion Points

*   **Uploads Draft:**  Discussion focused on the use of server-generated upload tokens, the `Upload-Incomplete` header, and error handling for incomplete uploads.  Retry behavior on 500 errors and naming conventions were also debated.

*   **Structured Fields Draft:** Addressed the issue of non-ASCII characters in strings.  Options were explored, including adding a new type to handle Unicode characters. A decision was made to initiate working group last call while continuing discussions on the non-ASCII character issue.

*   **Retrofit Headers Draft:**  Debated retrofitting the Authorization and WWW-Authenticate headers. Concerns were raised about scheme-specific information and implications for future extensions.  A middle ground was proposed to define mappings for basic and digest authentication initially, with the possibility of other schemes defining their own mappings.

*   **Alternative to Alt-Svc (DNS-Based):** Mike Bishop presented an alternative to Alt-Svc that relies on DNS SRV and HTTPS records.  Discussion centered on the loss of the ability to point directly to IP addresses, the requirement for alternatives to be equivalent or better, and the stickiness of alternatives. Several participants voiced concerns about the complexity. There was also discussion on a new service parameter.

*   **Websocket Discovery and Detection:** Lucas Pardue presented a new proposal about how to best serve WebSockets over H2 and H3. Discussion centered on how clients will discover the versions that the server supports, latency, and the desire for solutions that do not require clients to figure out which version supports which features.

*   **Modernizing HTTP Proxies:** A proposal was presented to modernize HTTP proxies using a mechanism similar to connect UDP and connect IP.

## Decisions and Action Items

*   **Structured Fields Draft:**
    *   **Decision:** Initiate working group last call.
    *   **Action Item:** Mark Nottingham to publish the current draft and start the last call process.
    *   **Action Item:** Start technical discussions about non-ASCII characters.
    *   **Action Item:** Form a design team to come up with a proposal for handling non-ASCII.

*   **Retrofit Headers Draft:**
    *   **Decision:** Further resolve the issues on Authentication and authorization before last call.
    *   **Action Item:** Mark Nottingham to investigate the Auth schemes further before moving on.

*   **Alternative to Alt-Svc (DNS-Based):**
    *   **Action Item:** Investigate service parameter names in DNS.
    *   **Action Item:** Continue discussion on stickiness and label usage on the mailing list.
    *   **Decision:** Adopt the draft and Obsolete 7838 with it, and keep this separate work item.

*   **Websocket Discovery and Detection:**
    *   **Action Item:** Form a design team to further discuss and refine the proposals. Kenrick to be the point of contact for credit coordination.

*   **Modernizing HTTP Proxies:**
    *   **Action Item:** Take the discussion to the mailing list and possibly initiate a call for adoption.

## Next Steps

*   Continue discussions on open issues for each draft on the mailing list.
*   Publish updated drafts with agreed-upon changes.
*   Initiate working group last calls for stable drafts.
*   The next meeting will take place at IETF 117.
