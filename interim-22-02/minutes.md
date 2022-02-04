

# HTTP Working Group Interim Meeting Minutes - February 2022

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [1 February 2022](#1-february-2022)
  - [Active Extension Drafts](#active-extension-drafts)
    - [Signatures](#signatures)
    - [Issue #1905](#issue-1905)
    - [Digest](#digest)
    - [Cookies](#cookies)
  - [Wrap up](#wrap-up)
- [3 February 2022](#3-february-2022)
  - [Active Extension Drafts](#active-extension-drafts-1)
    - [Alternative Services](#alternative-services)
    - [Client Cert Header Field](#client-cert-header-field)
    - [QUERY Method](#query-method)
    - [Binary Representation of HTTP Messages](#binary-representation-of-http-messages)
  - [Proposals](#proposals)
    - [Geohash Client Hint](#geohash-client-hint)
    - [Retrofit Structured Fields](#retrofit-structured-fields)
  - [Other](#other)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## 1 February 2022

Congrats to H2 for IESG approval!

### Active Extension Drafts

#### [Signatures](https://www.ietf.org/archive/id/draft-ietf-httpbis-message-signatures-08.html) 

([Slides](https://httpwg.org/wg-materials/interim-22-02/signatures.pdf)) - _Justin Richer_

Justin Richer [JR] running us through the slides.

On Crypto Updates slide. Martin Thomson [MT] says: raw encoding fine with `r||s`. On non-determinism, there is some work happening in CFRG (background: fault injection can be used to break implementations of deterministic algorithms; mixing randomness in can help).

On Implementation Status slide: Lucas Pardue [LP] says: something to consider for EDM program implementations work.

On Relationship to Signed HTTP Exchanges, on the matter of their signatures draft that is expired Mark Nottingham [mnot] says: we are coordinating with WPACK on finding a resolution.

Live demo of https://httpsig.org/, very brave.

LP: relationship between Digest and Signature. Strong links but don't want to step across the line of saying too much about the other spec in one or the other. Profiling algos doesn't seem too good either.

JR: There are gaps in each draft that the other one covers, but they are not the only way. We can mention the other document but not preclude other options. Suggest editors of both drafts work together.

LP: Sounds good.

#### Issue #1905

https://github.com/httpwg/http-extensions/issues/1905

"Related response" feature.

JR: Question to WG. Do we need related response at all. It's a bit difficult to explain, draft would be simpler without it. 

JR: On the ticket Yaron suggest a "@related" format. Annabelle and I investigated this before and it got messy quickly if you want it to be deterministic. Opted not to do it and stick to a limited middle ground.

mnot: need to get up to speed but from what I heard I'm taken to how to calculate a cache key. We've had key and variants, etc. An ability to state that this response is related to this request seems like it would be beneficial. I'll take a look into this.

MT: theres things in response that don't make sense without a request. I thought of HEAD. There's weird things in the protocol that don't make sense without the context of the requests. There's things that benefit from the request. I don't think signature can be complete without something like this. Maybe "related response" isn't the best phrase for this.

mnot: +1 weird name

Anabelle Backaman [AB] in chat: could use a SF param like "req"

JR: not good at naming things but we can to figure things out

#### [Digest](https://www.ietf.org/archive/id/draft-ietf-httpbis-digest-headers-07.html) 

([Slides](https://httpwg.org/wg-materials/interim-22-02/digests.pdf)) - _Lucas Pardue_

Was mostly done, in WGLC, had a diversion :)

Got deep feedback from a few people in WGLC
    - structured fields came up (again)
    
Plan is to answer the SF question once and for all
    - might need another WGLC

Have 4 headers currently
    - all use the same syntax as RFC3230

not all algorithms use base64 (sha does, CRC doesn't)

not compatible with structured fields, no retroactive fit
    - it's close but "token" != "key"
    - 90% of cases would probably pass but some would be dropped by SF parser


3 options for SF:

1: don't do anything
    - stick with what we're doing now, legacy formats
    - deprecate a few things
    - align with HTTP terminology
2: three headers
    - legacy headers use legacy format, updated terms
    - two new headers (and want- versions) as SF
    - "representation-digest" is the same as "digest" but uses SF format
3: two headers
    - pretend that "Digest" is toxic ☢️
    - don't update anything about it
    - only define new headers using SF
    - tries not to touch 3230, but isn't totally isolated
    
comparing formats:
    - main difference on the wire is colons around binary representation
    - (oversimplification - some algs use different encoding; would probably use sf-binary for all algs)

"pick one and move on"

Julian: Thanks for making the options available to look at. If we can switch to structured fields it's a great plus. Option 2 gives us everything. Authors are familiar with users of old field.

Lucas: Not wanting to express bias. I'm not invested in old Digest implementation, could just ignore it. Even if we just updated it (option 1), implementors would ignore it. Maybe people would realize what they were doing was wrong. If we don't go through the effort of wrangling semantics into old docs, people will not understand and will ignore things. None of these headers are too different.

Annabelle: If people using the existing headers today make no code changes, do they gain anything from option 2? (seeing a "no") If I have to make code changes, why wouldn't I just use new header fields?

Lucas: I'll take that as rhetorical. We're not changing Digest unless you're doing it wrong already. What you'd change is the input you'd run the value over.

Roberto: The point here is that there is a wide ecosystem using Digest. They should not change the input or syntax. I noticed in this ecosystem, API providers were doing it wrong. "The specification is not clear, we don't understand the HTTP semantics, we don't know if we're wrong". Started to listen only after draft process started. This is how public banking works, it's a slow process. It's important to update 3230 to push for integration of new fields.

Annabelle: Aren't we obsoleting 3230?

Justin: Strong support for option 2

Mark: don't have strong feelings about this. Concerned about option 2, feels like we're sending a confusing signal. This can harm interop. We should be thinking in long term, not short-term pain. Obsoleting 3230 is painful but it sends a clar signal that you don't use something anymore. more than anything, want to send a really clear signal. Also concerned that an updated definition of digest would cause problems, b/c you're not clear whether you're using the old or new semantics. Preference for option 3. If we go with 2, be very clear how to use Digest, maybe put it in an appendix.

Lucas: Have tried to talk about representations. Need to talk about  how to pick one, what to do if you see two. Hard enough with multiple algorithms, there are more things you need to speak to.

Mark: Representation-Digest is a long name

Martin: I was originally in favor of option 2, but option 3 is more now. Maybe appendix talking about Digest.

Seeing support for option 3 + appendix.

Roberto: If we go with 3, must deprecate. If we switch, Digest users won't see it and ignore it. Would be happy if everyone would switch. Which is the best strategy for the actual ecosystem? You could switch fields, but after your ecosystem agrees.

Tommy: What I hear people suggesting, with 3+appendix, is that people are sympathetic to migrating. Could you (Roberto) live with option 3 + blurb?

Roberto: This is hard, I was trying to fix Digest for gov't agency. But if there's a strong opinion, I will try to motivate this in some way.

Lucas: defining a new "q" parameter, copying what's in HTTP semantics? do we want to define that in a general HTTP way? Second, IANA: do we use the same table and update it or do we leave the old table and make a new one?

Mark: I think this will come up if we do the retrofit work.

Tommy: This is useful discussion. Have good indication of WG feelings.

#### [Cookies](https://www.ietf.org/archive/id/draft-ietf-httpbis-rfc6265bis-09.html) 

([Slides](https://httpwg.org/wg-materials/interim-22-02/draft-ietf-httpbis-rfc6265bis.pdf)) - _Steven Bingler_
 
Steven: Going over current status. 12^H^H11 open issues, one maybe to defer (along with 12 already deferred)

two broad categories: clarify specific behavior, add notes about specific situations

Deferred work: how to handle when public suffix list changes
    - browsers should be careful not to send invalid cookies
    https://github.com/httpwg/http-extensions/issues?q=is%3Aissue+is%3Aopen+label%3A6265bis+-label%3A6265bis-defer
    
Discussion:

Justin: signatures for cookies? 
    - will tag the issues

Johann: issue 1707; added tests to see how browsers behave with utf8 and punycode

Martin: we define HTTP as carrying octets, carrying octets outside of ASCII range is risky

Martin: recommend a-labels or punycode, recommend against utf8

Mark: martin pls update issue so we don't lose state
    - martin (doing it now)

Johann: would defer to steven as cookie owner

Steven: seems fine to disallow unicode characters
    - we internally convert to punycode and handle it in that space

Tommy: broad question to the editors: scheduling?

Steven: can devote more time over the next month or two

John W: third party cookies; are you happy with where that landed?

Mark: happy with where that text is now (in PR). Most is descriptive text as current state of play. Only one recommendation, to restrict if possible.

Jon: agree

Steven: was ambivalent, now agree

Mark: case insensitivity; is it real?

Steven: seems to be, would want to see more web platform results

Mark: would be good to see it more explicitly

Steven: agree; only in this space a few years, anything to help someone process this is worthwhile



### Wrap up

Mark: seems like we're making good progress on all these specs!







## 3 February 2022


### Active Extension Drafts

#### [Alternative Services](https://httpwg.org/http-extensions/draft-ietf-httpbis-rfc7838bis.html) 

_Martin Thomson_ ([slides](https://httpwg.org/wg-materials/interim-22-02/alt-svc.pdf))

- A different design is likely needed to deal with the DNS TTL and Alt-Svc max-age interaction. Interest from some folks in exploring that avenue.
- David will file an issue to explore QUIC VN, Alt-Svc, and SVCB interactions. 
- Are we working on Alt-Svcbis or a new form of Alt-Svc? (With a new header name?)

#### [Client Cert Header Field](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-client-cert-field) 

([slides](https://httpwg.org/wg-materials/interim-22-02/client-cert.pdf)) - _Brian Campbell_

- Presenting the client certificate chain (separately from end-entity certificate) using structured fields may be difficult; Martin to open an issue to resolve. 
- Using one header may be helpful in cases where one header is stripped but the other is not.
- Punting on certificate chain ordering requirements to TLS is likely best; taking discussion to an issue.

#### [QUERY Method](https://httpwg.org/http-extensions/draft-ietf-httpbis-safe-method-w-body.html) 

([slides](https://httpwg.org/wg-materials/interim-22-02/query.pdf)) - _Julian Reschke_

- Issue #1917 - Conditional Query. Notetaker had to step away. Lucas took over and missed much of the discussion before this point and during the discussion of this issue. Sorry.
    - What does selected representation mean for QUERY?
    - MT: Mismatch with how we think about content-negotiation in other places? Here its more nuanced. That's ok.
    - mnot: agree with MT. We have to consider and document all of these. USers are going to come along and say "It's liek GET except query params go in body". Document it all or it will be a mess.
    - julian: agree. QUERY specifies things that do ot apply to POST. If the outcome is we can define things clearly and retrofit them to HTTP, that is a  good outcome. QUERY should not be special, it's just another method.
    - mnot: lets decide if a QUERY relates to a selected-representation. That'll help.

TODO(caw): revisit this section based on recording

#### [Binary Representation of HTTP Messages](https://httpwg.org/http-extensions/draft-ietf-httpbis-binary-message.html) 

([Slides](https://httpwg.org/http-extensions/draft-ietf-httpbis-binary-message.html)) - _Martin Thomson_

- Couple of implementations exist; padding resolved server-side challenges.
- Will proceed with WGLC but with an extended deadline to allow for more feedback.

### Proposals

#### [Geohash Client Hint](https://datatracker.ietf.org/doc/draft-pauly-httpbis-geohash-hint/) 

([Slides](https://httpwg.org/wg-materials/interim-22-02/geohash.pdf)) - _Tommy Pauly_

- Threat model needs explanation and elaboration in the draft; hints can be spoofed. (This point is noted in the draft.) Privacy Pass might be better suited for security or access-control decisions.
- Use of ClientHints (continuously sampled value) may not be good for privacy. Using less bits for the geohash is a "crude" masking technique. Geolocation privacy has been considered in the past.
- Presentation of ClientHint could be gated by permissions. That could contribute to the client fingerprint surface. Worth discussing the tradeoff.

#### [Retrofit Structured Fields](https://mnot.github.io/I-D/draft-nottingham-http-structure-retrofit.html)

 _Mark Nottingham_

- Some support for the draft. Setting foundation for future work.

### Other

- Almost 50k messages on the list! There may be a prize for the person who tips the scale. 
- No WG meeting at 113. Possible informal meeting in person.