# IETF101: 20 March 2018 HTTP WG Meeting Minutes

*Scribe: Bron Gondwana*


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Active Drafts](#active-drafts)
  - [BCP56bis: revision of use of HTTP as a substrate](#bcp56bis-revision-of-use-of-http-as-a-substrate)
  - [Bootstrapping Websockets](#bootstrapping-websockets)
  - [Random access and live content - Craig Pratt (remote)](#random-access-and-live-content---craig-pratt-remote)
  - [Secondary Certificates: Mike](#secondary-certificates-mike)
  - [Expect-CT: Emily can't be here.](#expect-ct-emily-cant-be-here)
  - [Header Common Structure - Mark Nottingham](#header-common-structure---mark-nottingham)
  - [Cache Digests for HTTP/2 - Kazuho Oku](#cache-digests-for-http2---kazuho-oku)
  - [Client Hints](#client-hints)
  - [Cookies](#cookies)
- [Related Work](#related-work)
  - [Origin-Signed Exchanges: Jeffrey Yasskin, Chromium](#origin-signed-exchanges-jeffrey-yasskin-chromium)
- [Proposed Work](#proposed-work)
  - [HTTPtre: Julian Reschke](#httptre-julian-reschke)
  - [Preserving SNI privacy (yep, again)](#preserving-sni-privacy-yep-again)
  - [Variants](#variants)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Active Drafts

### BCP56bis: revision of use of HTTP as a substrate

* Mark: good progress - more examples, more review required
* Reviews have been positive - useful outside this group

### Bootstrapping Websockets

* Issue 471: consider using ALPN (currently using Upgrade)
  - Martin Thompson
    - inherent problem with this proposal,
      don't know that server supports HTTP/2.
    - to use this design, have to choose HTTP/1.1
  - Nick - Akamai
    - is it worth having an H2 w connect ALPN token.
    - response: have resisted bundling options at
      request time.
  - Ben - Google
    - Chrome has an implementation, rough but seems to work
    - 2 servers: hghttp2 and libwebsockets.
    - server implementors have tested with Chrome, it works
    - 3rd server in dev, doesn't work yet.
    - supports recommendation: no server level ALPN
    - to respond to "in advance" doesn't know server supports
      h2/websocket.  Inclined to send request regardless of
      response from server - will fail anyway
  - Martin - Mozilla
    - in TLS/1.3 server can send settings first anyway.  Temporary
      problem, not dire

* Is modifying CONNECT REASONABLE?
  + in every codebase, connect is handled in a different codepath
    already.
  + alternative: new method rather than CONNECT
  - Mark Nottingham
    - want to make sure that we consciously do this: having a protocol
      specific setting override standard HTTP method behaviour
  - Julian Reschke
    - what's the process for defining new pseudo headers?  H2 spec says we
      can't define new pseudo headers?
    - answer: 7540 is clear that settings mechanism can override behaviour
  - Martin
    - sending this new pseudo-header in a request to a server you haven't
      received settings from.  Predict: explosions.  Whole connection would
      break, not just the websockets bit.
    - answer: can fix with TLS/1.3 so we know what to send!
    - suggestion: change use of exiting pseudo-headers instead?  So only
      the connect stream would fail.
  + resolution: this is negotiated - negotiations require a round trip
  + there is no solution
  - Alan - Facebook
    - also have this issue
  - ? - Akamai
    - currently H2 spec says "if you have an unknown header, must treat it as
      a stream error, NOT a connection error"
  - Martin
    - yeah, we kinda screwed up there, but it's OK!

QUESTION to the room: does anyone have any problems with modifying CONNECT?  Nope.


### Random access and live content - Craig Pratt (remote)

New standard went out last night - not significantly different to previous,
mostly editorial.

Q: what's left before last call?
* thanks for rattling cages - got feedback.
* expected changes in shift buffers - and that's where they happened
* one question out there: will answer on mailing list, has clear answer
* don't expect to add anything to the draft
  - Martin
    - suggest: WGLC now
    - lots of people have paid attention to it
    - Mark: 2 weeks should be fine
* from Jabber:
  - Tom Peterson
    - see question on mailing list about 416
    - answer: while server may internally use circular buffer to represent
      shift buffer, shouldn't be a concept of resetting.
    - can't internally have a concept of resetting if it's going to be cacheable
    - Martin Thompson: great answer, don't need to write it down


### Secondary Certificates: Mike

Adopted last time.  Have merged it.  Exported identifiers (TLS group)

Open issue: handling cases where the client wants to offer a cert because
it expects the server to want it.  How we're using frames on streams that
may have already ended.  On h2 it's OK, over QUIC doesn't, because it's
already gone.

- Martin Thompson
  - a lot of activity on this in TLS.  Until that's resolved, this can't
    be buttoned down.
  - Mark: happy to let it bubble along while TLS iw working on it.
  - Patrick: important to future of HTTP, so get it on your radar.
- Lance - Google
  - it's a rethinking of how we think about the TLS crypt
  - one thing not addressed in the draft - client risk (might want to look
    at DNS).
  - talking to server operators: potentially allows widespread attack if you
    can obtain a compromised certificate.
  - right now you can use BGP detection, etc.   Not possible with secondary certs
- Erik
  - Risk now: if you can compromise DNS + BGP and a cert, you can attack
  - with this: only need a compromised cert
  - Mark: relaxation of DNS was done with Origin spec
  - Erik: speaking about server's ability to see if there's compromise
  - with this, no way to detect
  - Mark: can you suggest text.

- CT: works for illegitimate certs
- but: with stolen cert (server key)
  - can't discover compromise easily with this

Mike: don't have advice for detecting key compromise

* rotate keys more frequently!

* Option: add something to certs that say "don't let me be applied used
  in one of these"

* ANOTHER POINT: describes a single connection.
  - doesn't handle multiple connections when only one has been upgraded.
  - Mike: would be happy to receive some text about it, but generally
    you might have multiple connections which are valid for another
    server.

- Ian - Google
  - would also like the idea of opt-in.
  - different domains have different risk profiles

More to talk about, not going to WGLC any time soon!



### Expect-CT: Emily can't be here.

no comments


### Header Common Structure - Mark Nottingham

- Martin Thompson
  - limits are good
  - if you used all of this, then you'd have other problems

- ?
  - always have the option to extend the spec
  - Mark: push back on this, if you get more than 256 items, hard error
  - point is to have a generic implementation.  Don't want to allow override of limits
  - Mark: could define structured-headers-2

- ?
  - not sure that this would do any good
  - we already have guidance on headers, an nobody follows them already
  - who enforces?
  - Mark: parser will raise an error only if over 1024
    - software then needs to check 'only want 5'

- John Lennox
  - clearly defaults are great
  - ability for specific sub behaviour
  - Mark: could just do a non-common header, or define new common-2

- Julien
  - maybe would make sense to think about length limits in a different way than
    currently.
  - maybe just specify whole size of header field?
  - Mark: want to think about it, make sure assumption is going to hold

- Jeffery Yaskin
  - Chrome has a prototype already
  - Mark: YAY - shrieked!  Patrick insists this is in.
  - currently specified as http list syntax - HTTP spec specifies
    how to handle multiple headers

- Brent/Brand?
  - was going to comment in discussion about strings, but:
  - URIs?  Common data type, should they have separate representation?
  - suggest: maximum length of string take URI into account


### Cache Digests for HTTP/2 - Kazuho Oku

2 open issues (plus 1 editorial issue not covered today)

* Server indication is per-connection
  + use ORIGIN frame?

* require clients to cache the info?
  + currently a MAY

- Patrick
  - ORIGIN - fairly serious deviation from definition

- Alexandro
  - don't think it should be per-origin - it's a per-server thing

- Mike Bishop
  - main case where you want to spell it out - wildcard subdomains
  - ORIGIN doesn't have wildcard support
  - would need to enumerate all possible domains

- Mark Nottingham
  - if not caching, ORIGIN makes sense
  - Patrick: didn't envisage that ORIGIN would be just a bunch of settings
  - maybe new frame type would make sense, but how do you cache it?

Explore on the list

- Hugo
  - just to add to the complexity of this, can conceive of servers which are
    authoritative for and would like to cache for...
  - Patrick: agreement on this, question is whether ORIGIN is correct approach

Question:
+ remove etag/stale support?
+ most URLs the block rendering are long-term cacheable.
+ proposal: remove stale support

- Alexandro
  - agree that removing would be better
  - complication: if HTTP2 stack is separate from cache.  If you don't know etag
    you would just ignore it anyway


### Client Hints

- ?
  - confused about status and direction
  - seems like "could include ANYTHING" in there, e.g. geolocation
  - Mark: have shied away from adding everything in there - would have
    security-privacy considerations
  - Second Q: stuff about lifetimes/revocation.  "is this how we're going
    to do permissions?"

- Martin Thompson
  - don't like lifetime thing, but consider self to be in the minority.
  - got up here to say: changes on slide don't make me happy about security.
  - what made him happy: changes to considerations have made him happier.
  - opposed to geolocation because don't understand how to control that info.

- Eric
  - consideration 3 cuts in 2 directions.  If you can store cookies and javascript, can already shove this data in a cookie!  If you can do that, why do we need the header?
  - only difference is for first hit

- ?
  - Preload scanner - well before javascript executes
  - taken offline

Not going to WGLC terribly soon


### Cookies

No update.  Hopefully wind up soonish.


## Related Work

### Origin-Signed Exchanges: Jeffrey Yasskin, Chromium

- 10 minutes on presentation - 10 min for discussion!

- Roy Fielding
  - like the idea, but hate the idea of a 7 day validity window.
  - would prefer to be unbounded
  - ability to sign public documents for a long time overrides
    value of javascript

- Lucas
  - Signatures vs Cavage draft
  - no idea how widespread they are in the real world
  - Mark: impression, used by non-browser APIs

- Eric
  - technical issue: spent time reasoning about security properties,
    and can't.  That makes him uncomfortable!
  - have statically signed object appear in the origin makes uncertain
  - can probably work through for same origin - origin substitution
    would be bad.
  - To clarify: this working group not adopting

- ?
  - OCSP status of certificate and 7 day limit
  - but - CAB forum, that's a maximum, could be shorter.  Also caching.
  - answer: have had requests to make it both longer and shorter!
  - think: will stop trusting at the shorter of this and cache-control headers

- ?
  - mentioned more aggressive checking
  - e.g. Javascript can't run, or can't have origin, until signature verified online
  - answer: haven't figured out exactly when browser should verify

- Nick Doty - UC Berkeley
  - what should server do after they screw up and sign something stateful.
  - should stop signing new ones
  - can use Clear-Site-Data header to clear everything if known to have
    been attacked.
  - but, if not fetching anything, sure - clients will have to wait 7 days
    before knowing they have bad data.

Mark: Not considering adopting now, but that might change.


## Proposed Work

### HTTPtre: Julian Reschke

Notion: review HTTP/1.1 ONE MORE TIME

- Martin Thompson
  - it's our responsibility to maintain documents, not necessarily strive for
    perfection!
  - might not need to go to full standard

Patrick - Chair comment: would like to see this work

- Mike Bishop
  - as author or semantic layer draft, would love to see it in the spec
  - as HTTP/QUIC would love this too
  - timeline: if we want QUIC docs to be done by the end of this year, this
    won't be done by the end of the year.  Assume don't want to hold HTTP
    over QUIC, so would be referencing documents that are quickly replaced.

- Mark:
  - with QUIC hat on, sure
  - but: would like to get this done FAST.  Intend to spend a lot of time
    on this, and want to get it done ASAP.  Hopefully this year.

- Julian: would be shocked if this isn't done before QUIC.

Show of hands: 15 people willing to work on this!

- Brad Shorten
  - please, fewer documents
  - nightmare right now

Either 2 documents or 3 documents.

HUM: "if you want working group to take on draft-bishop-decomposing-http
and produce fewer documents".

Shift over to BIS repo and rename it, preserve issues list.


### Preserving SNI privacy (yep, again)

- Erik
  - question about 0-RTT version for *.github.io
  - could get cia.github.io in that case.

Patrick: generally sympathetic with work.  ALT-SVC might have some things
to say about sni.  Not sure if update required.

- ?
  - is your intent that this is widely deployed, or only for specific clients?
  - A: think alt-svc and DNS could be a performance win, so expect it to be used
  - A: hiding SNI, would be an implementation choice, could cost more
  - Q: issue with SNI, can still have your connection replayed
  - A: ? cover both cases.  If you don't get right cert back, then will have to
    make the second round-trip

- ?
  - Host header point: SNI check was used to check if cryptographic context, but
    still using Host header to direct to correct backend.
  - alt-svc will be used first, then will know what other names can be used.

- Martin Thompson
  - Akamai are looking at using SNI for validating ownership of domains
  - this would be a landmine for them.
  - what's the relationship between expiration times and RRSET
  - A: draft says expiration times must match

- Erik
  - it's OK if SNI and Host header don't match already.

Authors: are you asking us to adopt these drafts?
  - no outstanding issues
  - would appreciate adoption

- Martin Thompson
  - they're not ready (as a speaker for the NO hum)
  - would like to see more discussion on the list

### Variants

Adopt?

- Martin Thompson
  - relay from Jabber - Tom Peterson
  - appears spec denormalises or writes off value of quality indicators

about 10 people have read draft

- Roy Fielding
  - asked on list?
  - A: Got a bunch of responses.  Seen

HUM: in favour of adoption, to be confirmed on the list.

Have parked Key - assumption is that this replaces Key.  No objections.

Roy Fielding as co-author of key, no objection
