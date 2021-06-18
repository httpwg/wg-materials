
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

#### Issue 826 - h2 and h3 have slightly different registry policies. Reconcile?

Dropping experimental ranges from H2 makes these pretty close. Mark will examine and propose resolution.

#### Issue 849 - Cory proposes not discussing this in the H2 spec, and leaving the question to Semantics.

Also possible to reiterate that Content-Length SHOULD NOT be included.

Mark:   If we say SHOULD NOT, need to discuss what the presence means.

Martin: If we say how to handle it, it's probably going to contradict what H2 says more generally. If anything, MUST NOT send. Better to say nothing.

#### Issue 863 - Mitigate small window update attacks?

Martin: We already have text in Security Considerations for the DoS risk; don't need a protocol mechanism.

#### PR 861 - Rules about things that look malicious are incomplete.

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


### Digest Headers

[Slides](https://httpwg.org/wg-materials/interim-21-06/digest.pdf)

MT: How do content-codings interact with content-digest?

Roberto: basically, the algorithms currently result in hashing the bytes of the representation content *after* content coding; there are the "id-" prefixed algorithms (eg. id-sha256) that operate on the representation (or content) *before* the application of content coding. WRT content-codings, [Digest and Content-Digest work in the same way](https://github.com/httpwg/http-extensions/blob/main/draft-ietf-httpbis-digest-headers.md#resource-representation-and-representation-data-resource-representation).

Lucas: Good progress and feedback since last interim. Content-Digest is a path to resolving payload vs representation differences. More work required for the PR: https://github.com/httpwg/http-extensions/pull/1543. Some help (esp. regarding IANA process) is requested.

Mark: Happy to help (as chair)

Justin: Looks like Content-Digest is heading in the right direction. Makes it simple for checksumming bytes when chunking data to send using standard HTTP APIs. Allows addressing common and uncommon use cases. Supportive of the proposal.

Mike: Content-MD5 was inconsistently implemented in response to partial responses. One header for each possibility addresses most use cases, and hopefully avoids ambiguity this time around. Supportive of the proposal.

Manu: We're implementing the proposal for Content-Digest. Some future w3c specs are looking at using it. Regarding #1532, hoping to get new digest algorithm (multibase and multihash) into the registry. What's the best way forward?

Mark: Need specification published and reviewed. These are generic mechanisms, not HTTP specific, so maybe the HTTP WG would not adopt for sake of registration. Since these may have security implications, this might go through SECDISPATCH for further triage.

Lucas: Digest and Content-Digest are complementary to one another. Should be able to download files by ranges and verify each chunk by Content-Digest, and then the whole data by Digest, for example.

Mark: Two headers is a wonderful thing. Want to review the header names offline. Thanks for the work!

Lucas: Will send email out to the list pointing to the PR.

Mark: When the PR is ready, we'll be ready for WGLC.

### Signing HTTP Messages

[Slides](https://httpwg.org/wg-materials/interim-21-06/signatures.pdf)

(Proposal for date-based names)

Manu: Date-based proposal for algorithm identifiers stems from developer confusion induced by long names. Trying to give developer's some sort of idea about the age of the algorithm.

Roberto: RFC7696 provides insights about naming and identifiers for algorithms.

Chris: Not in favor of date-based proposal. What are the requirements? Punting to developers and applications is not the best idea.

Justin: Purpose is to give meaning and a reference to developers (to grep through a document to figure out how to implement an algorithm). Not in favor of date-based proposal.

Annabelle: Date/year is being used as a proxy for "quality" of the algorithm, but that's a poor proxy. We should not be optimizing to make decisions by application developers easier.

Manu: Discussing two extremes. Developers that know they need to use RSA or ECDSA, but not sure about other parameters.

Justin: Algorithms do NOT identify the parameters. (That's done separately.)

Manu: Algorithm identifiers map to parameter sets.  You want to nudge people to the more recent version of an algorithm.  If they are named in this way, you nudge people to later things.

Annabelle: Have no assurance that "newer" is better.

MT: Negative value in this proposal.

Mark: Reminder -- this is not a security group. (Probably best to have this conversation elsewhere)

Justin: Happy to loop back to security folks for more help/assistance. (Chairs will assist)

(Next Steps)

Annabelle: One goal of the draft is to tolerate HTTP message transformations in transit between endpoints. Via header may accumulate content in transit, so signing this header may not work well. Need a mechanism for this, else we can't sign it. Applies to other headers too, e.g. Cache-Status and Proxy-Status.

(More Next Steps)

Manu: Some implementation work underway with developers to test this out. See: https://github.com/w3c-ccg/http-signatures/issues/1

## Proposals

### Alt-Svc bis

[Slides](https://httpwg.org/wg-materials/interim-21-06/altsvcbis.pdf)

MT: Alt-Svc work in the DNSOP working group is good, and the WG here needs to be aware of it. (See https://github.com/MikeBishop/dns-alt-svc/pull/329/files.) Would like to have that discussion in this WG. That might mean holding the HTTPS record until coordination is complete. Minimally, we should take this to the HTTP mailing list.

Mark (no hat): Alignment is required. Implementers have concerns about this since not many people (really) know how it works. Wary of adding new features such as path scopes. Would be more interested in a simpler, concise design that we can all interoperate on.

Lucas: Was not aware of discussions happening in DNSOP WG. Brought some ideas for consideration, but not all need to be done here.

Mike: Need to resolve the ECH and Alt-Svc discussion. Would also be good to update Alt-Svc such that it can be supported across browsers. Unclear if path-scoped Alt-Svc is the right solution for content served elsewhere on a per-path basis. Maybe could be done out-of-band? Perhaps just focus on laying groundwork for future work on this path.

Tommy (chair): Bringing to the HTTP WG would be good. Should we have a focused call on Alt-Svc issues?

Erik: +1

Mark: Will work on adoption call within the next week or so.

### Targeted Cache Control

[Slides](https://httpwg.org/wg-materials/interim-21-06/targeted-cc.pdf)

ChrisL: Good work. Many people are reimplementing this in their own way. Creates a low barrier to entry.

Mark: That's the goal! 3rd party frameworks like Wordpress or Drupal can drop in the header and target caches as needed.

ChrisL: Caching and proxy software can have a simple check for the header. Good engineering overall.

Tommy (chair): Hearing no objections, will proceed with adoption call.

### Cache Trailers

[Slides](https://httpwg.org/wg-materials/interim-21-06/cache-trailer.pdf)

MT: (missed)

Mark: Caching is the appropriate granularity for updates in the trailer. Browsers and things consuming trailer fields may not do so for performance or security reasons.

Roy: May need a way to update the status code. There might be other ways for a server to say content is no longer useful, but that's separate from caching.

Mark: This can be part of the information that's conveyed (similar to warning header?). Need concrete (not general) behaviors for this to be useful.

Roy: One is a generalization of the other.

Mark: Comes down to how this is spelled and the scope of the updates. Fine with generalizing as long as it's actionable.

Kazhuo: Model is to send response with limited caching scope and the promote to wider scope. If that's a goal, then limiting to caching makes sense.

Mark: Senders may want to be cautious first (and cache less). (There are other examples and use cases, too.)

Roberto: If an intermediary strips off the trailer, what happens?

Mark: Good question! Consequences of that would need to be weighed against people using this trailer. If overcaching is a big issue and the trailer might be stripped, then perhaps this might not be used. May need to give guidance on when the trailer is applicable as it's subtle.

MT: (side note about discussion regarding mechanism -- can happen elsewhere)

Mark: Sounds like there's interest. Tommy to confirm.

Tommy (chair): Might need more time to bake.

### Binary HTTP Messages

[Slides](https://httpwg.org/wg-materials/interim-21-06/bhttp.pdf)

Julian: Why do we need this?

MT: OHTTP needs to encrypt things in some binary format.

Kazuho: Why do we need fixed and indeterminate lengths?

MT: Open question for me too.

Lucas: We need to do this somewhere if OHTTP is to be a thing.

Mark: If OHTTP goes ahead, HTTP should probably do this work. Else, we need to see if there are other use cases that might work. Having a version-independent representation of the messages would be interesting.

Lucas: What's the relationship between this and binary structured headers?

Mark: They're separate.

MT: Separate. Lots of space in the first byte for other forms. One could create a different form of message that might take binary structured headers, and would be more efficient. That's for the future now.

Alan: Is there any aim to make these smaller in the future?

MT: Thought ASCII was a feature. Appealing since it's simple.

Alan: Could make things smaller, but not everyone wants to write that code. Just a consideration for the future.

Mark (chair): Tommy and I will talk to the ADs and flag that if OHTTP moves forward then the HTTP WG should work on this.

