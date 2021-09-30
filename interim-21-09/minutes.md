# HTTP Working Group Interim Meeting Agenda - September 2021

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [28 September 2021, 21:00-23:00 UTC](#28-september-2021-2100-2300-utc)
  - [Alternative Services (bis)](#alternative-services-bis)
  - [Boostrapping WebSockets with HTTP/3](#boostrapping-websockets-with-http3)
  - [Client-Cert Header](#client-cert-header)
  - [HTTP Message Signatures](#http-message-signatures)
- [30 September 2021, 21:00-23:00 UTC](#30-september-2021-2100-2300-utc)
  - [Safe Method With Body (Julian)](#safe-method-with-body-julian)
    - [Issue 1614 - Method Name](#issue-1614---method-name)
    - [Issue 1552 - Caching](#issue-1552---caching)
  - [Targeted Cache Control (Mark)](#targeted-cache-control-mark)
  - [Digest Fields (Roberto)](#digest-fields-roberto)
  - [Priorities (Lucas)](#priorities-lucas)
  - [Cookies (Mike West)](#cookies-mike-west)
    - [Issue 1600 - Standardize Maximum Max-Age](#issue-1600---standardize-maximum-max-age)
    - [Issue 1517 - Specify no decoding](#issue-1517---specify-no-decoding)
    - [Issue 1399 - Set-Cookie enforcement](#issue-1399---set-cookie-enforcement)
    - [Issue 1332 - Empty Domain](#issue-1332---empty-domain)
    - [Issue 1593 - Update Storage Model](#issue-1593---update-storage-model)
    - [Issue 1502 - Better specify serialization](#issue-1502---better-specify-serialization)
    - [Issue 1210 - Serialization doesn't match original string](#issue-1210---serialization-doesnt-match-original-string)
    - [Issues 1418 and 1385 - Existing Cookies when Criteria Change](#issues-1418-and-1385---existing-cookies-when-criteria-change)
    - [Issue 1288 - Service Workers](#issue-1288---service-workers)
    - [Issue 1073 - UTF-8 Characters](#issue-1073---utf-8-characters)
  - [Proposals](#proposals)
    - [ORIGIN for H3 (Mike B.)](#origin-for-h3-mike-b)
    - [Make Documents Historic](#make-documents-historic)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## 28 September 2021, 21:00-23:00 UTC

### Alternative Services (bis)

Idea: spruce up based on what we've learned using it. It started as almost experimental with different implementations but we've moved toward undstanding what it does as we use it. 

Biggest new thing: HTTPS/SVCB DNS records

Status: minimal changes from RFC7838 in -00, minor editors changes on top of it
Includes H3 definition

Would like to follow same process/direction as H2 changes

Discussion:

mnot: are the issues in scope and manageable?

martin: I'm the only one to raise things so far, nothing is concerning at the moment.

mike b: some things dicussed w/erik would be actual changes; once those are filed we'll need discussion about what goes in spec, what goes in extension, what's not interesting to wg

martin: things raised in the past are changes, but sensible and straightfoward

mnot: concerned we didn't see full implementation of alt-svc from browsers in the past; don't want to see that happen again, need to get right people involved

martin: think we can do something there

### Boostrapping WebSockets with HTTP/3

ryan: websockets over H3 is just like H2; defines settings that match H2 and sets flags for document

ryan: no feedback and issues, happy to hear feedback

mnot: go to WGLC?

martin: not sure about "request cancelled" for reset, worth spending a little bit more time on that. "request cancelled" means "no processing occurred" which is only kinda true. other than that it's good.

mike b: isn't that request rejected?

martin: maybe? need to work that out

ryan: file an issue and solve it on github

mnot: (martin) will do as WGLC issue

lucas: websockets H2 draft uses cancel error code, H3 doc maps the error codes from that; can discuss on the issue

### Client-Cert Header

mike: have done a decent period of issue gathering

mike: adopted draft with single field to communicate full cert, have asked customers about who uses certs for feedback and got varied answers, communicating full cert

mike: most things are editorial or obvious (strutured fields binary values)

mike: open question, what are all the things we should be able to send? what if raw public key, not cert? what if server wants to get the chain? do we do set of all certs, or just the hashes? don't think we need negotiation, since it's a proxy talking to a backend for which of these things you want it to add. question is: what is the universe of things we should define and what do we not bother with.

martin: two competing tensions; anything client sends to the server on first hop is something that neesd to be passed on. if client has cert chain, there's a reason for those intermediates to be in that chain and not passing them on is potentially risky. On the other hand, things like raw public key suggest use cases that aren't all that interesting, we should scope the work down and remove things that aren't absolutely needed. would avoid "full certificate chain" phrase, but everything in the TLS handshake is likely to be needed.

mike: if you want to contribute wording on which certificates, we'd appreciate that

justin: +1 to certificate chain, as I've said before. I have an implementation where we need to send the whole chain, due to multi-tenancy on the server. I agree we should not try to solve every possible permutation, but I think that the full client certificate and chain as a list makes sense. My proposal on github/list is to have two field definitions, one for cert and one for the chain. That allows us to have a list for the chain and a binary value for the cert. Simpler that way.

mike: separate structured fields would help a lot. People also talked about sending hashes of the chain. What do you think?

justin: In my implementation, we need the full cert, not just a hash.

Lucas: see https://developers.cloudflare.com/workers/runtime-apis/request  ; example of property exposed in CDN platform. 

mike: scenario is a little different, but expect the needs to be similar

mnot: 1) to justin, say a little more about hashes wouldn't be available; CDNs are likely to get a broad requirements, does use case require full certificates?

justin: the certificate chain needs to be passed to a secondary system that needs to handle the entire chain.  that system might not have access to intermediates. that means you need the whole chain to do application-level validation. it might be a bit weird, but it's real.

mnot: all the chains aren't known ahead of time

justin: we do this today with a custom extension; working on moving to this syntax.  we need all the chain.

mnot: 2) a little unusual because it's designed to be added by an intermediary and sent to origin, origin likely to vary response based on this header. Should we have text on cache considerations? downstream intermediaries don't have that info, there are implications of that.

mike: downstream cert is going to be the intermediary's cert

mike: certainly need caching text

mnot: question is what's the scope of that cache

ben schwartz: performance and efficieny don't appear anywhere in this text; especially if shipping entire certs

mike: already issue to discuss w/header compression

ben: guidance on when this is a bad idea would be good

kazuho: hashes are another property of certificate; we should refrain from optimizing by sending hashes, full certificate covers broader use case

from Martin Thomson to Everyone:    5:33  PM
intercepting proxies won't be trusted here
from Martin Thomson to Everyone:    5:34  PM
chances are, anything downstream will need to know (and authenticate) the proxy

### HTTP Message Signatures

(Justin presenting)

Summarizing signature mechanism; selecting covered elements, normalizing, generating signature output, and sending that in a structured field. The document reflects these stages.

Lots of work is needed to determine what parts of messages to sign. Signing the message entity/body itself is out of scope. Instead, you can get a digest of the body and sign that.

Components like methods have a special format, "@method" for example. Field names are referred to directly.
These are not pseudo header fields, but there is not a clean 1:1 correspondence between the concepts.

It might be worth recording the various reserved prefix values (like "@" here) somewhere (note taker: the draft? or was that a request for a registry?)

q (Todd Greer): can you sign for both GET and HEAD?

a: you can sign for either, but not both; you can choose not to sign over the method if it is not stable in your environment

Intermediaries being able to sign the contents they see/forward is a critical use case. One example is signing the client cert field that is seen/inserted.

More recently:
- Aligned to HTTP terminology
- Added specialty components (the "@" components)
- Signature negotiation (Accept-Signature)
- Dropped list prefix
- Expanded examples

q: how many people are going to get host/@authority wrong
a: some. those that aren't doing protocol switching might not see the effects of their mistake

Accept-Signature uses the same format as the signature field, to mark which components are expected to be signed.

The core spec design hasn't really changed since the original adopted work and it is compatible in many ways (other than syntax) with the original -cavage draft.

roy: are you really convinced that an @-prefix is the right way to go in terms of the names.  as you are lower-casing things, why not use uppercase instead?

justin: lowercase is easy to add for all inputs.  too much room for human error if we vary case

roy: others might choose to use @ too

justin: maybe we can carve out this space to avoid that; we could have used a colon, but that could be confused with h2 (we previously used colon and moved away from it, we also used \' at one point)

mnot: wary of having people creating different prefixes for headers.  maybe we need to sit down and write out a good abstract data model for HTTP

justin: an alternative considered was to special-case header fields (i.e., include a special indicator for header fields).  the problem is that this adds overheads, both in the serialization and also in what needs to be sent.  -cavage just treated everything as a header, but we have moved to recognize two types of things

martin: Pushing back on mnot a bit: an abstract model for HTTP would be hugely useful! But it won't be ready in time, for either this, or other work I'm doing. Semantics does clarify some parts of the model. The tricky bits are how bodies are composed, trailers, etc. Sorting out those issues will take a while.

justin: seeing some suggestions for how to manage this in chat, but we can take that offline.  I personally don't care about syntax as long as it is distinct and deterministic.  right now, any unknown syntax will just cause signatures to fail

justin: look for text on deciding how to sign and what to insist is sign in the coming weeks

justin: signing cookies is ... fraught.  signing cookies is also useful. cookies are weird and outside of the message.  

martin: If we are going to be signing cookies, we'll want to be signing specific pairs. As much as they are terrible, we need to deal with it. I think the only option is to add a special identifier for individual cookies. I don't think we'll want to sign Set-Cookie fields.

justin: specialty components are already defined to allow for requests and responses to have different treatment.

martin: set-cookie (in a response) can be treated as a regular header field

justin: before we add extra features, we need to justify them.  that keeps the spec simple. cookies are something that people will want to sign.

justin: we don't currently have a way to sign the absence of a header. You can sign an empty header, but if you could sign the absence, you could let the receiver detect if a header was added later.

mnot: point of data.  we try to discourage people from making a header with an empty value semantically significant.  people still do it though.  so you need to distinguish between not present and empty in the signature input

ben schwartz: enumerating the list of headers that are definitely not present is helpful, but you want to be able to disclaim the existence of non-enumerated headers also

justin: noted, but that goes somewhat against the ethos of the signatures work

martin: agree with Justin that this is a deliberate decision to allow headers to be inserted. The risk is that they insert something that causes a "bad" behavioral change, but that would need to be in security considerations.

justin: Definitely in security considerations. A known attack vector against partial signature schemes.

justin: people have requested EdDSA, but no one has volunteered to help write text. Please help if you care about this!

justin: what is the relationship with wpack? We didn't have response signatures before (which is fundamental to wpack), and now we do.
WG chairs need to go chat with the authors/chairs there.

martin: I think we shouldn't be concerned with wpack here. They're a bit further behind right now. We shouldn't condition this work on what happens over there.

mnot: We're not going to condition our work on that group, just a matter of communication with them.

martin: They have a different design philosophy. WPACK is about static content, whereas these signatures are about being flexible to header field changes, etc. trying to align the designs might be a mistake.

justin: Our thought has been to make simple changes that could make life easier for wpack, but not fundamental changes.

justin: Asking for implementer feedback. Many implementers are likely not as engaged in standards, so we will need to evangelize this work to get people to shift.

justin: I have a toy server implementation running that might be useful for proving out their client code



## 30 September 2021, 21:00-23:00 UTC

Issue for a fix with IANA registry in http-core docs; no feedback on list (https://lists.w3.org/Archives/Public/ietf-http-wg/2021JulSep/0435.html).  Does that mean no objections?

Consensus on call:  No objection, this is fine.


### Safe Method With Body (Julian)

Slides largely unchanged since last meeting.

#### Issue 1614 - Method Name

Initial proposal was to use SEARCH from WebDAV and relax the WebDAV-specific pieces.  Should we do this something else?

Mike B: Assuming nothing we do will break WebDAV, SEARCH seems fine.

Julian: Keeping WebDAV compliant isn't a problem, except that WebDAV doesn't define a proper media type.

Julian: SEARCH is a specific verb; we may not want the implications, but we may not want the delay of arguing over a new one.

Mark:   Fine with SEARCH, or FOO, or any other string. We need to convince developers, and some of them quibble over the verb. Proposed QUERY.

Julian: Alignment with query part of URI is a good point. Note on issue that we like it, possibly incorporate if no one screams.

Mark:   Let's try putting it in the draft, then circulate (esp. to HTTP API WG). Change now without declaring consensus.

Tommy:  Yes, let's try it. Not declaring consensus.

#### Issue 1552 - Caching

Proposal in issue:  Server can indicate Location of a GET-able version of the response.

Mark:   People who use this expect a low barrier to caching. Changing method might be too high a barrier.

Mark:   Want to say someone making a "similar" request gets the cached response; what is "similar"?

Julian: Depends on media type of request; need normalization algorithm.
Mark:   Right, so we could define normalization for JSON or XML, God help us.

Martin: Be cautious about defining normalization. Strict comparison of bytes is the baseline; note possible optimization if you understand the query format.

Mark:   Similar to Key and Variants (need to revisit in light of Structured Fields); might want something a little more flexible than byte comparisons. Weasel words okay.

Roberto:Very hard to normalize even if you know the language. Don't attempt to define here.

### Targeted Cache Control (Mark)

Pretty happy with latest version; revised text on Structured Fields.  Currently says "MAY" reuse Cache-Control parser, but debating removal of that permission.

Martin:  What's the actual difference?

Mark:    Cache-Control parsers are largely unspecified. Out of 353M responses, 0.295% are not valid Structured Fields.  Dubious they parse as Cache-Control either, but depends on your parser.

Slight leaning toward removal in chat; authors will discuss.  After resolved, ready for WGLC.

### Digest Fields (Roberto)

Nearly to WGLC; split to Content-Digest and Digest based on previous interim feedback. Both have a Want-* twin.

Editors want WGLC after this meeting; no strong opinions on remaining issues:
 - #1671 - Allow deprecated algorithms for weak consistency cases?  Pending PR from Mark. Maybe pick a different label.
 - id-* algorithms created as exit strategy for implementations with odd behavior. Retain? Move to separate draft?

Julian:  MDN claims all browsers support Digest; turns out they mean "browser doesn't die" (see also https://caniuse.com/mdn-http_headers_digest and https://github.com/mdn/content/issues/9139)

Lucas:   Browser support will be hard.

Mark:    On that note, MDN has asked our people to review their docs. Please do that.  I'll help you get connected to the right people if you need.

Mark:    Is this still compatible with legacy Digest?

Roberto: Did not introduce incompatibilities; that's why there's a second header.

Mark:    Raises questions about Structured Fields if we publish something that doesn't use it.  What is the bar?

Lucas:   Lots of temptation to "fix" things, but trying to avoid unwarranted breakage. We've deprecated parameters (which largely aren't in use anyway).  Consistency with the old one is more important for the new header.  We're living with legacy here.

Mark:    Suggests bar is existing parsers; entirely new things should use SF.

### Priorities (Lucas)

-05 published; mainly editorial, points to H2bis.

One open issue:  If you disable H2 priorities, is use of this mandatory?  Proposal:
 - H3, just use this
 - Use of both in H2 is allowed but confusing
 - Servers and clients can inform clients it doesn't use H2 priorities as an optimization

Setting renamed to SETTINGS_DEPRECATE_RFC7540_PRIORITIES. (Martin suggests SETTINGS_NO_RFC7540_PRIORITIES instead, to general acclaim.)

Propose to decouple implication that one implies the other.  WGLC now?

Martin: Submitted PR to make change; text looks fine with simple replacement.

Will merge open PRs and publish new draft by EOW.

### Cookies (Mike West)

#### Issue 1600 - Standardize Maximum Max-Age

Each UA has different bounds for unreasonably large maximum age.

John:   Special handling for Cookies set by JS in Safari, caps at a week.

Steven: Any bounds for server-set Cookies?

John:   Not to my knowledge.

Proposal is to define a reasonable max in the spec, e.g. 2 years.  Clamp to this max if specified further in future.

Martin: Browser can apply policy that's tighter than the spec, and that's fine. Consistent behavior is the real requirement.

#### Issue 1517 - Specify no decoding

Do not URL-decode cookies, e.g. __%53ecure- is not __Secure-

Existing behavior; just not written down.

Dan:    Name only, or any attribute?

Steven: Any attribute.  Will be clear about that.

#### Issue 1399 - Set-Cookie enforcement

Spec should be stricter about malformed Set-Cookie headers.

Mark:   Alignment is good, but need to test existing implementations.

Mike W: We'll write the tests.

#### Issue 1332 - Empty Domain

Convert a SHOULD ignore to a MUST.

Martin: What do browsers do?

Mike T: Chrome ignores the Cookie; others ignore the attribute.  Will consider changing Chrome after evaluating security.

#### Issue 1593 - Update Storage Model

Believe this is a symptom of a larger problem, 6265bis doesn't handle non-HTTP APIs well.  We should fix that, not this.

Mark:   Do we have an issue?  Is that under consideration?

Steven: Open to that discussion, but not filed currently.

Mark:   Who's going to do that work?

Steven: I can.

Mike T: Value in this, but we want to ship.  Let's defer to a follow-up spec.

Daniel: That goes outside HTTP, which is the topic of the spec.

Steven: We're already outside HTTP, we just ignore that in the spec.

WG will move on; Steven will propose updates separately in the future.

#### Issue 1502 - Better specify serialization

Seems very involved; might defer.

Mike W: Reasonable to defer to HTML spec.

Tommy:  Can we align more closely with what browsers are doing?

Mike W: Related to another UTF-8 discussion, but we could just drop the note for this issue.

Proposal is to drop note.  It's true, but probably belongs in a different spec.  Anne might respond in issue.

#### Issue 1210 - Serialization doesn't match original string

Nameless and valueless Cookies were a mistake.  Don't need to fix issues with using them.

Martin: Document should caution against using them, then.

Proposal is to add warning around nameless Cookies with no functional change.

#### Issues 1418 and 1385 - Existing Cookies when Criteria Change

E.g. Public Suffix List changes can mean an existing Cookie would no longer be acceptable.

Mike W: PSL is clear; what other cases are there?  Prefixes added in future specs?

Steven: Not many others.  PSL is the only one without spec changes, I think.

Dan:    Loading from the store doesn't mean the Cookie gets sent.  Spec should describe what happens on the wire, not storage.

Mike T: Do we need to say anything? User Agents already have to deal with invalid Cookies.

Martin: Can we avoid affecting / describe how existing Cookies that are stored get handled in new specs?  This can be limited to PSL.

John:   Have faced this in WebKit due to partitioned Cookies.  "Ghost Cookies" are a real thing.  For example, the max max-age behavior -- if we limit to 2 years, then find a 3-year-old Cookie?

Mark:   Do we have guidelines on what to defer and what to fix?

Mike W: We need to get the doc done. Fine to iterate on the esoteric stuff later.

Mark:   Takes more energy to do another iteration, but we do need to finish.

Proposal is to defer issue to a future revision.

Mike W: Text around Cookie Header production needs to prohibit sending invalid Cookies.  Defer the storage question.

#### Issue 1288 - Service Workers

Service Worker requests can send Cookies which would not otherwise have been sent.

Mike W: Would like to add permission for UAs to partition SW Cookies.  Initial definition of SameSite punted on Service Workers.  (But partitioning will require more spec changes.)

Martin: Make this a problem for the SW spec.

Proposal is note that UAs can handle SWs differently, but leave details to SW spec.  Mike will provide PR.

#### Issue 1073 - UTF-8 Characters

Text says ASCII-only, but many browsers allow UTF-8.

Mike W: Right thing to do, but hard. Spec is no worse if we leave it until someone has the time.

Martin: If we have IDN names in the domain, we should at least specify their encoding. Full Unicode for names and values seems fraught.

Mike W: Think Chrome support Punycode.

Martin: Does anyone take u-labels?  Punycode-only is easy; if anyone already does Unicode, we'll need to handle it.

Martin will open separate issue for IDN; proposal is to defer this issue.

### Proposals

#### ORIGIN for H3 (Mike B.)
https://www.ietf.org/archive/id/draft-bishop-httpbis-origin-h3-00.html

Spec is sitting around, still needs to be done.  Do anything?

Mark:  Call for Adoption?

General consensus, yes.

#### Make Documents Historic

Have a list of documents to propose we move to Historical.  Will send to list.

Martin: This isn't free, but probably worth doing.


