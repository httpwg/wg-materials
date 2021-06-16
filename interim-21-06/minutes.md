
# HTTP Interim June 2021

## Status of Core Drafts

Feedback from IESG and Last Call mostly editorial; updates expected to list for non-editorial issues.

## Active Extension Drafts

### Client Cert Header - Brian Campbell

First meeting since draft adoption
Draft -00 matches adopted draft; editor's copy has minor changes
TODOs moved into issues in GitHub

Opposing priorities:  Some want full cert chain as well; others say EE cert is too big

Martin: Authentication isn't addressed; needs to be.
Brian:  Move to Informational was partially to address this. Needs to be addressed in deployment and policed by the reverse proxy.
Mike:   Question goes to documenting existing practice. Existing practice isn't to sign the header, even though I would do it in a new protocol.

Justin: We'll be discussing how to sign on Thursday.  Doc also valuable for highlighting common pitfalls.  Would like to see a few additional abilities, like cert chain. Maybe as a second header?  "It's weird, but we should enable weird in smart ways."

Lucas:  Draft says only one value for the header. What if there's a chain of proxies?
Brian:  Probably not in scope. Trying to let back-end see what originating client is sending; treat as end-to-end where possible.

Alan:   Beware of maximum header sizes, and consider interaction with header compression.  (Raise issue?)
Brian:  Worth discussing; that's not my expertise.  Please contribute text/issue discussion.

Nick:   Large headers can get stripped; consider putting the SHA256 in a separate header that might still make it through. Authentication could be added as simply a static token provisioned on the proxy. Need to discuss security of path between proxy and origin as well; client certificate shouldn't be leaked in the clear.

### Safe method with body - Julian Reschke

Slow progress due to focus on Core drafts
Undecided whether this method should be SEARCH or not; draft name doesn't specify, but draft text currently updates SEARCH

Mark:   SEARCH is likely slightly more deployable than something new. Older versions of Squid reject unknown method names. However, widespread encryption means this is probably less of an issue. Reuse SEARCH if it doesn't have to be stretched too much, otherwise not.
Julian: Avoids a bikeshed.
Mark:   Immensely valuable. Also, caching is probably necessary, but requires media-type details.
Julian: Requires input from the interested.

Mougin: Name implies functionality. How generic is this supposed to be? Can be used for more than SEARCH.
Julian: Not restricted to searches; name is really just a name.
Mougin: Wouldn't advise use of SEARCH for a method not restricted to searching.

No issues opened yet; we should open issues for these things we want to discuss.

### HTTP/2 bis - Martin Thomson

1-2 issues only feasible if we change ALPN token. We've decided not to do that, so those issues are likely to go away.

Issue 826 - h2 and h3 have slightly different registry policies. Reconcile?
Dropping experimental ranges from H2 makes these pretty close. Mark will examine and propose resolution.

Issue 849 - Cory proposes not discussing this in the H2 spec, and leaving the question to Semantics.
Also possible to reiterate that Content-Length SHOULD NOT be included.
Mark:   If we say SHOULD NOT, need to discuss what the presence means.
Martin: If we say how to handle it, it's probably going to contradict what H2 says more generally. If anything, MUST NOT send. Better to say nothing.

Issue 863 - Mitigate small window update attacks?
Martin: We already have text in Security Considerations for the DoS risk; don't need a protocol mechanism.

PR 861 - Rules about things that look malicious are incomplete.
Mark:   Two things going on. First, server could respond with 400 instead of resetting stream. This is requirements versus options. Steer toward semantic error where possible. Second, didn't Greg want to have stricter requirements on allowed characters?
Martin: That's mostly resolved; he wants cover for stricter behavior. Really just talking about reaction now.
Mark:   I'll write up a proposal.
Mike:   H3 uses malformed mostly for framing and mapping-layer issues. Only fuzzy one is invalid characters in field names and values.
Mark:   Might want to lift text from this resolution into H3 during AUTH48.

After these issues, that's it.  We'll publish a new draft and ask for WGLC.

### RFC6265bis - Lily Chen

-08 published after last meeting
6265bis-defer label for issues which are out of scope, not reaching consensus, etc. and won't be addressed unless something changes

Issue 1531 - Truncating cookie at control character might enable attack if attacker-controlled value included in cookie. Reject instead?

Issue 1340 - Cookie size limits currently minimum. Different UAs implement differently, which makes this a fingerprinting mechanism. Considering more specific requirements.

### Extensible Prioritization Scheme for HTTP

Implementer feedback since last interim led to open issues. Most have PRs.

Issue 1429 / PR 1504 - Talk about prioritization of retransmission in HTTP/3. PR landing in next week or so; review now.

Issue 1495 / PR 1544 - Prioritization of CONNECT data doesn't quite fall into current text, but obviously should work.
Tommy: Presumably if you're prioritizing CONNECT data, it almost certainly needs to be incremental, no?
Lucas: Open to that, but it seems covered by existing text. Maybe another sentence; suggest text.

Issue 1500 / PR 1541 - Definition of which HTTP/2 elements are being superseded

Issue 1546 - Point to H2bis instead of RFC 7540? If so, should that delay WGLC?
Mark: H2bis document is almost done; WGLC them together?

Ian:    What about prioritizing H3 datagrams?
Lucas:  Datagrams are making good progress, as is this, but it seems unfortunate to couple them. A separate document seems more reasonable.
Ian:    Agreed, but where is that document? What WG does it live in?
Mark:   Would need to discuss among chairs.
Tommy:  Does the interaction need its own document, or should H3 datagrams just reference Priorities and describe how they're used?
Lucas:  It took a lot of HTTP discussion to reach this; MASQUE might get distracted by having to do the prioritization work.





