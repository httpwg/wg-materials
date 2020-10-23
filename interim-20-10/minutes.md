# HTTP WG October 2020 Interim - Draft Minutes

_Scribes, plese see [our guidelines](https://github.com/httpwg/wiki/wiki/TakingMinutes)_


## 20 October 2020, [13:00-14:30 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HTTP+Working+Group+October+2020+Interim+Session+I&iso=20201020T13&p1=%3A&ah=1&am=30)


### HTTP Core

([slides](ietf-httpbis-2020-10-httpcore.pdf))
Julian: presenting...
* Big reorg of documents
    * caching doc
    * messaging
    * semantics 
        * All versions of HTTP regardless of wire format
        * Roy did major reorganization of this last month
* Status
    *  All errata but one addressed
* Github issues summary (see slides)
    * What's left is editorial
* Getting close to WG LC
* A few remaining non-editorial issues
* Question on structure of semantics
mnot:
* I have a test suite which tests browser and proxy caches
* I found a few issues and filed
* (Demo) this view gives you a side by side of issues and text
* no decent interops on 304s, we need to have a good think about it
* issue 478 isn't editorial, support for invalidation on location and content-location is really poor
* Firefox, Squid and nuster conform, but no one else does
Tommy: When do we want to target last call
mnot: Roy and I are meeting once a week now. We're making good progress. I think around IETF 109. Certainly by end of year
Julian: confirm
Tommy: due to the length of these we'll have a long LC. Please take a look asap



### [Extensible Prioritization Scheme for HTTP](https://tools.ietf.org/html/draft-ietf-httpbis-priority)

([slides](priority.pdf))
Lucas: presenting... maybe? moving on, we will come back. And we're back
* there was debate of headers vs frames, why not both?
* we have concensus to move on with
* latest draft is -02
* -01 had a priority update frame, did we need it?
* concensus to land frames as well, we can land the breaking change to update the frame
    * we've replaced the initial bit field to encode the type, but that's encorported into the frame type now
    * frame code point(s) changed to avoid interop problems from using the existing frame type concurrently with the new one
* no way to specify the version of prioritization in this spec
* added consideration for server scheduling
* removed instruction about intermediary fairness
* considerations for when clients use PRIORTY_UPDATE
* open issues
    * within the stream limit 1261
        * problem introduced by priorty update frame
        * in H3 this is easier because stream limits are managed directly
        * H2 is more complicated because it is in terms of concurrency, not trying to redefine that
        * rephrased as "within the stream limit"
        * Should be mostly editorial changes
        * Feedback welcome
    * default priority of a pushed request 1056
        * we have a merging of priority signals
        * in the case of server push, both signals are from the server
        * but if there is no signal, what is the default?
        * ommiting the priority for normal requests has a default of urgency 3, non-incremental
        * different options possible, unclear which is the best
        * the server can't use PRIORITY_UPDATE frame to signal push priority because it can't be sent from server->client

mt: The first option (same as associated stream) is fine. The request order implies priority. If the push comes after the request that triggers it, that works with H2
Lucas: We have some more explicit guidance on ordering in the text. Good observation
Robin: Not sure I agree. What do you mean by the default? Both urgency and incremental?
Lucas: I don't know. Are you asking if the push should be incremental?
Robin: We don't give explicit guidelines of how to handle incremental vs non-incremental in the same bucket, so could get priority inversion when choosing option 1.
Lucas: this comes back to ordering. There are few ways to skin this cat. I think the right answer is to describe the problems that come from exhaustion. The question with relation to push is a good one, we can probably get the wording right.
Robin: If we don't give explicit guidance, I'd suggest option #2

Kazuho: The problem with option 2 there could be other streams that come before the stream that triggers the push and other streams at the same urgency level, so could lead to other issues. At the same time writing down the problems ...
mt: Kazuho is right, Robin also correctly points out problem of choosing incremental vs non-incremental. The right thing to do is to point out the issues. From the chat you have no strict ordering of pushes but we have push IDs that can be inserted between non-push streams and schedulers can use stream ID-based ordering. 
Lucas: this is probably best done on github
Tommy: one question on scheduling. Do we want to target a particular time for lc of this doc?
Lucas: H3 is getting towards last call, but there's not strict dependency, this is non-blocking. For real deployment it will be important to get this in though. Implemenations need something practically. Want to finish this asap.  




### [Signing HTTP Messages](https://tools.ietf.org/html/draft-ietf-httpbis-message-signatures)

Annabelle: presenting
* Talking about creating durable signatures over fragments of an HTTP message
* Attaching a signature looks different now
* Adopting structured fields
    * changes how we attach 
    * a few other changes we'll get to later
* We're going from one header field to two
* Signature input is a dictionary of a list of tokens
* can provide meta data for multiple signatures
* key=signature identifier, value=covered content
* switched to \*request-target rather than (request-target) since that no longer conflicts
* new content identifiers
    * can specify a specific member of a dictionary
        * can have multiple dictionary identifiers
    * list prefixes specifies it is sigin the fist *n* members of a list


ekr: This is an incredibly general mechanism. Can be self contradictary. I don't understand how this can be secure
Annabelle: Let me understand. 
ekr: The semantics of composition is undefined
Annabelle: they are defined, but I didn't include it in the slides
ekr: (example) unless we have specifications of HTTP headers, we can't have deterministic semantics
Annabelle: The utility will depend on the context. What needs to be signed depends on the context. If you depend on the whole header being signed, you should be enforcing that the whole header being signed
ekr: This requires extensive annalysis, but in our experience that doesn't happen. So I don't think we should create a document with that property
Annabelle: can we goto the next slide to demonstrate how this can be useful
ekr: I don't dispute that it can be useful
Annabelle: your concern is that people will only sign fragments but not sign pieces that change the semantics
ekr: we see similar issues in signed email, because no one understands what the headers there mean and how they're signed.

Julian: can you tell us about the reason for splitting it into two headers?
Annabelle: previously unstructured. Most parameters were additional named strucutres and you had one signature. One of which was the headers param which had a string of identifiers that will be signed. What prompted the split was a few different things. We want to support multiple signatures and have signatures sign over other signatures. We also want to be able to sign the input for a signature. Which creates a compelling reason to split the two out so the signature input cna reference itself. Interested in feedback on if there are other ways to capture those requirements

Cory:  Pseudo header elements. Any reason to not use those?
Annabelle: I believe there isn't a perfect overlap there. it is possible that with this change that that may not be relevant anymore. might be worth looking back at that. would force us not to use the token format because tokens can't begin with \:
Cory: ___
Annabelle: the canonicalization of the ___ is to ___
Cory: I think binary basic items aren't don't have a single cannonicalization. There may be some ambiguity that might be worth calling out.
Annabelle: thanks

Justin Richer: (coeditor) to respond to ekr. that's the entire purpose of signing a piece of a message that can be modified in transit. The enforcement of only trusting the signed portions needs to happen at the application layer. We have experience in how this can be implemented correctly and also how it can go wrong (OpenID 2). Unless we are signing the entire message as an immutable block we are going to have to deal with this problem space.
EKR in comments:  My point is that this is a bad idea.
Justin: I don't agree. It can go wrong, but that doesn't mean we should ignore it
mnot: we have headers that it is useful to have headers where entities can add to it and sign it. It can also be misused and dangerous where it is misused. Also, I'd love to give feedback on structured headers.

Jeffrey: I agree with ekrs concern. Signed excchanges require that everything is signed. I like that you got counter signtures with this mechanism. I think this draft needs an explicit call out that derivied protocols should only use the signed portions
Annebelle: That's a good call out. There isn't guidance for profiling specifications. Security considersations is a section that hasn't gotten attention.

(timing discussion)
Annabelle: presenting
* discussion on expiring and creation time
* outcome is two proposed concepts
    * expiration time is the signer telling hte verifier what they think is the expiration time. bounding the accountibility for the signature. not a strict requirement on the verifier. verifier may have longer or shorter times for many reaosns such as clock skew, async apps, the verifier has tigher constraints for any reason (such as compliance requirements)
* next steps
    * alg and keyid confusion, suggestion to use *jose?*, will respond
Sam Weiler: I noticed that you see that what key you're using is out of scope. How does a verifier know what algorithm a message had been signed with.
Annebelle: where?
Sam W: e.g, 3.2.1
Annebelle: the selection is out of scope. A profiling spec that builds on this would likely have a key selection registration and selection mechanism. We can add a section to add clarity to that.
Sam W: what happens when someone forges a signature with an algorithm that isn't widely used. How do we deal with downgrade attacks?
Annabelle: We haven't specified how a verifier specifies what they will accept. There are cases where it is useful for a verifier to spefiy ahead of time what they will accept, but that can happend out of band. We need to have those constraints. But not obvious we need that in this draft.




### [Digest Headers](https://tools.ietf.org/html/draft-ietf-httpbis-digest-headers)

([slides](ietf-httpbis-2020-10-digest.pdf))
Roberto: presenting...
* renamed
* header that is allowed to send a checksum used by
    *  MICE content-coding
    *  signed exchanges
    *  banking APIs
* changes (see slides)

mnot: we're running out of time
Roberto: presenting...
* open issues (see slides)
* open issue #970
    * for POST and PATCH digest is computed on payload body
    * Jullian suggests to extend the behavior to all methods

Justin: This interlocks with HTTP signatures and this is progressing well. I need to sit down and read the draft. Do you think we can see some alignment between the algorithm spec that digests use and the one that signatures use
Roberto: We removed everything that is below sha256 so I belive there is no issue about legacy. Algorithms are managed externally, but we are glad to work on that to make sure the specifications can integrate.
mnot: getting close to WGLC, so people should have a read
Roberto: thoughts on issue 970
mnot: it is pretty complicated, need to think about it offline

### [RFC6265bis](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis)

mkwst: presenting...
* Draft status
    * 20 open issues
    * 19 are relatively strait forward
    * 1 is larger, we'll talk about it later
    * a couple bugs worht defering
    * nothing we can do them in the doc as it exists (see slides)
    * some others that are stale and we think we can close (see slides)
    * some need investigation, such as the test suite (wp-test, browsers and spec disagree). Specificly around same-site. Bulk of short term effort will be here.
    * Changes to cookie implementations in the wild that should flow into this doc. Should we do that in this draft? or punt to a future doc?
* these are wrapped up in a doc called cookie incrementalism
* some hve shipped in implementations
* 3 seem ready to folkd in
    * SameSite by default
    * requiring secure for SameSite=None
    * Schemeful SameSite (taking the scheme into account in addition to domain)
    * (engine implemation table)
* We have tests for each of these (table with results)
* WPT doesn't turn on these flags, table is wrong
* we've catagorized the bugs, so we have a path forward
* is it worth it to bring in some of the changes that are shipping in the wild or we are more interested in closing this document out so it reflects relatity of a couple months ago

mnot: goal is to reflect reality. I think it is entirely reasonable for the WG to add a few things left. If there are any implemntors that say anythnig please say so now.
ekr: we don't want to ship things that are in IDs and not in the actual draft. We would be in favor of folding them into the main draft and also shipping the draft.
Julian: I'm on the opposite side, ship the stable spec and define new things in a new revision
Thommy: we have opinions on both sides. Let's get a written up proposal and have a discussion on list.
mkwst: the cookie incremenatlism is written as a set of PRs, so that will be pretty strait forward


## 22 October 2020, [13:00-14:30 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HTTP+Working+Group+October+2020+Interim+Session+II&iso=20201022T13&p1=1440&ah=1&am=30)

David Schinazi and Cory Benfield will be your minute takers today.

### [HTTP/2bis](https://datatracker.ietf.org/doc/html/draft-thomson-httpbis-http2bis)

([slides](http2v2.pdf))

Note from minute taker: let the record show that the 2 in these slides is glorious.

Cory Benfield: this is a good idea, support - kill midders

David Schinazi: Proposed adding removing server push to the list of changes.
https://github.com/martinthomson/http2-spec/issues/16

Mike Bishop: Wants to address errata, if the doc is open anyway let's do some more, no new features.

Julian Reschke: Update references to the core doc, even if it's only an exercise. Martin to take under advisement.

Yoav Weiss: Opposed to removing priorities from H2. They are implemented and deployed in some places: opposed to removal before new priorities mechanism in place. Martin is open to exploring a wide range of soft-deprecations instead of hard-removal.

Lucas Pardue: Supports this work, willing to contribute. Proposes including HPACK in this effort, e.g. add a new static table.

Ian Swett: on priorities, a middleground approach is good - we should reference the new priorities draft. Also, should we change the ALPN because of existing broken servers (e.g. WebSocket over h2 breaks some servers they abort on SETTINGS). Also we use midders in production so if we remove them we would like a way to negotiate them as an extension.

Alan Frindell: We use push in non-Web contexts so we'd like to keep it. HPACK is probably fine as is.
Mike Bishop: also likes push in non-Web. Changing the HPACK static table would be a breaking change.
Dmitri Tikhonov: +1 to Alan: HTTP/2 is not just for the web, either
Bence Béky: +1 to Cory's and Alan's preference to not change HPACK
Cory Benfield: Not worth re-entering queue, but I agree with not removing push. Push is very straight forward to not use: just don't use it. You can delete the code, set the ENABLE_PUSH setting to zero, and just largely forget it exists, so I'm not motivated to delete it from the spec.
Daniel Stenberg: I'm +1 on keeping push and keeping HPACK as-is

Mark Nottingham: there is clear interest here, let's work on this as a WG. Perhaps move Martin's repo to a WG repo. Not hearing anyone saying we shouldn't do this effort.
Tommy Pauly: agrees

### [HTTP/2 extensions for HTTP/3](https://datatracker.ietf.org/doc/html/draft-bishop-httpbis-altsvc-quic)

([slides](https://httpwg.org/wg-materials/interim-20-10/H3_pollination.pdf))

Martin Thomson: Proposes reopening RFC 7838 (AltSvc) and 8337 (ORIGIN) as bis documents to revise them and include QUIC. Julian Reschke notes that AltSvc has no errata, ORIGIN has one. Mike doesn't see the need for a bis on ORIGIN but is open to one for AltSvc.

Mark Nottingham: Nervous about opening these documents up for bis due to concerns about strong feeling around some of the areas the drafts tackle.

Lucas Pardue: the origin errata is mine? It's not really worth a bis imo

### [GREASE for HTTP/2](https://tools.ietf.org/html/draft-bishop-httpbis-grease)

([slides](https://httpwg.org/wg-materials/interim-20-10/H3_pollination.pdf))


Mark Nottingham: Will a new ALPN token be necessary?

Chair consensus is to take this to H2bis.


### [HTTP Grease](https://tools.ietf.org/html/draft-nottingham-http-grease)

No slides.

Question for the group: is this an interesting direction for us to go in?

Jeffrey Yasskin: This document says it's important not to say which field names are reserved for greasing: why?

Mark Nottingham: This prevents receivers from special-casing reserved fields

Tommy Pauly: Would client implementations participate in experimenting here?

David Schinazi: As a client implementer, Chrome would do participate, at least in the beta channels. Would prefer to GREASE in stable but the web may not be healthy enough to tolerate it.

Julian Reschke: In general this is a good idea. This was somewhat triggered by Yoav's difficulty deploying client hints: can he update?

Yoav Weiss: We've seen a lot of problems in beta/canary/dev. Fixed most of these. Still being rolled out to stable. Generally: what David said.

Mike Bishop: This is a great idea, but this is a new kind of GREASE that is very different from previous GREASE work. Should this doc be experimental?
Mark Nottingham: We want this doc to be authoritative on the topic, experimental weakens that

Martin Thomson: It's more valuable to have a place to discuss this and reach out to WAFs than to publish an RFC

Julian Reschke: Perhaps we should modify the core specs to be more explicit about saying that headers can have many shapes, even if we don't call it GREASE

Mark Nottingham: Happy to hear that clients are going to experiment. Doc isn't the priority, we can pause it for 6 months
Tommy Pauly: We can coordinate in experimental channels

### [Client Hint Reliability](https://tools.ietf.org/html/draft-davidben-http-client-hint-reliability)

([slides](https://httpwg.org/wg-materials/interim-20-10/client-hint-reliability.pdf))

Lucas Pardue: On the topic of ALPS, SETTINGS aren't the only way to extend HTTP. You could use new frames. I like the idea of improving negotiation of extensions but limiting ourselves to SETTINGS might be too limiting.
David Benjamin: Let's use frames in general.
Cory Benfield: It seems a bit unfortunate to have ALPS be yet another way to exchange data. Maybe we should fix SETTINGS instead?
David Benjamin: A lot of complexities there, using half-RTT for SETTINGS works in theory but causes many implementations problems in practice. ALso we'd need a new ALPN.
Mike Bishop: This reminds me of Alt-Svc. Perhaps we could add this to the HTTPS record?
David Benjamin: DNS is not authenticated in practice today.
Mike Bishop: Instead of extended SETTINGS, just use a new frame each time.
David Benjamin: Unfortunate that there are less frame codepoints than SETTINGS identifiers.
Sam Weiler: We could define this as "only with DNSSEC".
David Benjamin: Chrome doesn't support DNSSEC so that's a no-op for us. Also, DNS has different lifetimes than HTTP/2 connections so they could fall out of sync. It also doesn't save any round-trips over ALPS, so doesn't seem worth it.

Tommy Pauly: Next steps?
David Benjamin: We'll need to figure out what lives in HTTP vs TLS WGs.

### [Search Method](https://tools.ietf.org/html/draft-snell-search-method)

([slides](ietf-httpbis-2020-10-search.pdf))

Mark Nottingham: Basically a +0.5, we have customers interested in caching POST
David Schinazi: we have a use-case that wants POST over 0-RTT, so maybe having a way to specify idempotency could be nice
Mark Nottingham: let's chat more I think you can already do that today
David Schinazi: sorry, I need more caffeine
Martin Thomson: this is interesting, but I haven't seen interest from many parties in the 5 years where this has existed
Mark Nottingham: I think there's sufficient interest from what I've seen
Roberto Polli: Having a way to make explicit if a request is safe is very important. If we build it they will come.
Nick Harper: Having a way to say that a request is safe is important, I'm not sure that SEARCH is the right answer to that though. Maybe SAFE_POST might be easier.
Julian Reschke: The motivation for picking SEARCH was that there is existing code out there that already knows that it's safe and idempotent. If we use a new method we'll have to write more code.


