# HTTP Working Group Interim Meeting Agenda - September 2021

    WebEx
        Meeting number: 161 816 3363
        Password: transportfer
    Meeting chat
    Minutes requires datatracker login

Taking minutes? See our guide

## 28 September 2021, 21:00-23:00 UTC

2 Hours
### Administrivia

- 3 min - Blue sheets / scribe selection / NOTE WELL
- 2 min - Agenda bashing

###  Active Extension Drafts

- 20 min - Alternative Services
- 10 min - Boostrapping WebSockets with HTTP/3
- 10 min - Client-Cert Header
- 50+ min - Signatures (slides)

#### Alternative Services (bis)

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

#### Boostrapping WebSockets with HTTP/3

ryan: websockets over H3 is just like H2; defines settings that match H2 and sets flags for document

ryan: no feedback and issues, happy to hear feedback

mnot: go to WGLC?

martin: not sure about "request cancelled" for reset, worth spending a little bit more time on that. "request cancelled" means "no processing occurred" which is only kinda true. other than that it's good.

mike b: isn't that request rejected?

martin: maybe? need to work that out

ryan: file an issue and solve it on github

mnot: (martin) will do as WGLC issue

lucas: websockets H2 draft uses cancel error code, H3 doc maps the error codes from that; can discuss on the issue

#### Client-Cert Header

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

#### HTTP Message Signatures

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

---
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

2 Hours
### Administrivia

- 3 min - Blue sheets / scribe selection / NOTE WELL
- 2 min - Agenda bashing

### Active Extension Drafts

- 15 min - Safe Method With Body
- 10 min - Targeted Cache Control
- 10 min - Digest Fields
- 10 min - Priorities
- 50 min - Cookies

## Proposals

TBD