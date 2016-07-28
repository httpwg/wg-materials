# HTTP WG: IETF 96 Berlin Minutes

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

  - [Monday](#monday)
    - [Specification Status](#specification-status)
    - [Opportunistic Security](#opportunistic-security)
    - [Active Drafts](#active-drafts)
      - [[Character Encoding and Language for Parameters](https://tools.ietf.org/html/draft-ietf-httpbis-rfc5987bis)](#character-encoding-and-language-for-parametershttpstoolsietforghtmldraft-ietf-httpbis-rfc5987bis)
      - [[Key](https://tools.ietf.org/html/draft-ietf-httpbis-key)](#keyhttpstoolsietforghtmldraft-ietf-httpbis-key)
      - [[Client Hints](https://tools.ietf.org/html/draft-ietf-httpbis-client-hints)](#client-hintshttpstoolsietforghtmldraft-ietf-httpbis-client-hints)
      - [[Origin Frame](https://tools.ietf.org/html/draft-ietf-httpbis-origin-frame)](#origin-framehttpstoolsietforghtmldraft-ietf-httpbis-origin-frame)
      - [[JFV](https://tools.ietf.org/html/draft-ietf-httpbis-jfv)](#jfvhttpstoolsietforghtmldraft-ietf-httpbis-jfv)
      - [[Cache Digest](https://tools.ietf.org/html/draft-ietf-httpbis-cache-digest)](#cache-digesthttpstoolsietforghtmldraft-ietf-httpbis-cache-digest)
    - [Cache-control extension: Immutable](#cache-control-extension-immutable)
    - [Issues list for opportunistic security](#issues-list-for-opportunistic-security)
    - [draft-pratt-httpbis-bytes-live-range-unit-01](#draft-pratt-httpbis-bytes-live-range-unit-01)
    - [TLS 1.3 binding into HTTP](#tls-13-binding-into-http)
  - [Friday](#friday)
    - [RFC6265bis](#rfc6265bis)
      - [Cookie Priorities](#cookie-priorities)
      - [Expiring Aggressively Those HTTP Cookies (EAT cookies)](#expiring-aggressively-those-http-cookies-eat-cookies)
      - [RFC6265bis issues](#rfc6265bis-issues)
        - [[159: allowing cookies without key or value](https://github.com/httpwg/http-extensions/issues/159)](#159-allowing-cookies-without-key-or-valuehttpsgithubcomhttpwghttp-extensionsissues159)
        - [[199: change definition of unique cookie to include host-only-flag to match browser behavior](https://github.com/httpwg/http-extensions/issues/199)](#199-change-definition-of-unique-cookie-to-include-host-only-flag-to-match-browser-behaviorhttpsgithubcomhttpwghttp-extensionsissues199)
        - [[201: SameSite: Clarify user-triggered navigation behavior](https://github.com/httpwg/http-extensions/issues/201)](#201-samesite-clarify-user-triggered-navigation-behaviorhttpsgithubcomhttpwghttp-extensionsissues201)
        - [[204: enhance title of RFC6265 to include "cookies" term](https://github.com/httpwg/http-extensions/issues/204)](#204-enhance-title-of-rfc6265-to-include-cookies-termhttpsgithubcomhttpwghttp-extensionsissues204)
    - [Potential and Related Work](#potential-and-related-work)
      - [[TCP Tuning for HTTP](https://bagder.github.io/I-D/httpbis-tcp/)](#tcp-tuning-for-httphttpsbagdergithubioi-dhttpbis-tcp)
      - [[Secondary Server-Cert Auth](https://tools.ietf.org/html/draft-bishop-httpbis-http2-additional-certs)](#secondary-server-cert-authhttpstoolsietforghtmldraft-bishop-httpbis-http2-additional-certs)
      - [[HTTP2 and IoT (Gabriel Montenegro)](https://www.ietf.org/proceedings/96/slides/slides-96-httpbis-3.pdf)](#http2-and-iot-gabriel-montenegrohttpswwwietforgproceedings96slidesslides-96-httpbis-3pdf)
      - [SDCH](#sdch)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Monday

Ted H: BOF for QUIC; goal is to break into individual work items that use IETF items better. A secure transport initially targeted at HTTPS. Wednesday Morning 10-12:30 Potsdam I

### Specification Status

draft-ietf-httpbis-encryption-encoding-02
https://datatracker.ietf.org/doc/draft-ietf-httpbis-encryption-encoding/

Chair: more WG discussion desired on HTTP Encryption Content Encoding. Ok if discussion happens before or in IETF last call.

Ekr: Initially designed as simple mechanism without clutter. Over time this has bloated, now picked up a number of features that may not be needed. But oddly limits symmetric crypto algorithms. What is the right set of design choices? What are the actual use cases? Should it be slimmed down or fattened up? Is there something existing we could reuse?

MartinT: Webpush has very narrow profile that adds a bunch of the baggage. Maybe can split that part out of the spec.

Ekr: It is not obvious to me that this is correct due to the number of pieces involved. The original version was relatively obviously correct.

MT: breaking it into pieces might be helpful

Chair: sounds like we should go back to WG last call.

MT: large number of webpush implementations are using this already.

### Opportunistic Security

[draft-ietf-httpbis-http2-encryption-06](https://datatracker.ietf.org/doc/draft-ietf-httpbis-http2-encryption/)



### Active Drafts

#### [Character Encoding and Language for Parameters](https://tools.ietf.org/html/draft-ietf-httpbis-rfc5987bis)

Julian R: RFC5987bis (see agenda for presentation)

MarkN: Thinks there may need to be more prose about motivations. Will propose something.

#### [Key](https://tools.ietf.org/html/draft-ietf-httpbis-key)

[issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Akey)

Chair: lacking implementations. Uncomfortable pushing this forward without more implementation experience. Parked until more experience/interest.

Alexey: OK so far.

#### [Client Hints](https://tools.ietf.org/html/draft-ietf-httpbis-client-hints)

[issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Aclient-hints)

Chair: Thinks we're pretty much ready to go to WG last call on our side, but waiting for work happening on fetch spec in whatWG. On hold for now. Reviews or extended WG last call are welcome now.

Julian: Client hints sort of depends on Key being there. So may at least need to change reference to be informative.

MarkN: Key is informative reference, using it is more efficient but not actually required.

Julian: Thinks use of key depends on specific text so more changes may be necessary.

RoyF (via jabber): client hints may need more work on security considerations.

Chair: Please open issue on that topic.

RoyF: https://github.com/httpwg/http-extensions/issues/215
         (but I have no idea how to add a label to an issue)

#### [Origin Frame](https://tools.ietf.org/html/draft-ietf-httpbis-origin-frame)

[issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Aorigin-frame)

Subodh: Question about origin-frame

Chair: Please open issue about that.

BenSchwarz: according to HTTP experts, don't trust responses from independent anchors - how does that apply here?

MarkN: This is issue for HTTP 2 not HTTP 1.1. HTTP 2 handles connection pools already.

Ben: Would like more guidance on whether this is OK for multiple origins on the same connection without a trust relationship

MarkN: Guidance should be in HTTP 2 itself. More guidance may be good but not for this spec.

MikeRoberts: question missed by scribes :(

MartinT: We have a pattern to build up an image of what the set of flags we have is. Can we work on a coherent pattern?

MarkN: some best practices might be a good thing to have here.

MarkN: Invite discussion about questions on this issue.

Q[name?]: Issue 212 opened.

Decision: Want to wait a bit longer on this before moving to WG last call.

#### [JFV](https://tools.ietf.org/html/draft-ietf-httpbis-jfv)

[issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Ajfv) 

Julian: summarize what's been discussed on mailing list (see slides in agenda).

JR: Question - do we try to retrofit this to existing headers and if so how to deploy

JR: problems: JSON parsers don't tell you what happens if you repeat a property - interop is scary here.

MT: How much of this is a schema-aware language (HTTP 1.1 is a schema-aware model for header names but not for content). How much of this is schema-free vs. schema-defined? People sort of understand the boundaries in JSON which is way going in that direction. Maybe step back a bit. We don't actually understand what it is we want out of this process. Need to walk that space more carefully. Thinks JSON is probably a bad idea. Perhaps we use something that exists or invent.

ErikN: Security issues around repeated headers is a concern. We could make things much worse or better with this.

MNot: it's clear that this might not end up what we thought - there is more scepticism on the list than there was even a week ago. Happy to keep the document as a placeholder to show there is an interest in dealing with the issue of how to specify HTTP headers without JR being a bottleneck. Let's pick carefully before jumping, as Martin says.

MT: Seems to be a lot of enthusiasm for fixing a lot of the problems in current header fields. But we need to have a model for how this gets deployed. Do we have a Date header and Date* header and how does that work?

MN: That can be separated as a problem. You can define a set of alternate headers, for different syntax, but then you have to negotiate still.

Chair: Needs to be a lot more discussion about that. But looks like we'll need to talk about this for a little while.

JR: Should we try to agree on the goals? We probably can't address everyone's goals in one format. Maybe we should have a meta-discussion about what is our target...

Jabber: how close are we to remaking ASN.1?

Chair: Capturing potential goals is a useful thing to do now. Will start up a wiki page.

#### [Cache Digest](https://tools.ietf.org/html/draft-ietf-httpbis-cache-digest)

no open issues

MarkN: Martin had feedback about the complexity. Hard to anticipate all the use cases for cache digest. So went a little bit shot gun on that so we can capture all those. Is open to having a higher level discussion and paring down the features if that's appropriate.

MT: Wanted to add a piece of complexity on URI normalisation

MN: Don't have that for the cache so why do it for the digest?

MT: Perhaps a conservative generation rules with maybe a few extra things to make it easier. Just nail down the whole I have this stale, I have this fresh and how you handle the model associated with that.

MN: Maybe need expand that a bit and go into use case.

MT: Seems to be a mismatch between different flags, reset, … a bit hazy

MN: Would you want to do a partial reset?

MT: What happens when you put a reset on a frame that has content in it, Etags, etc.

MT: Think this is really good stuff. Will provide some feedback around probability stuff. Would like to see this go experimental first, don't get any value out of this until people start playing with it.

MN: Would you want to send out both fresh and stale, a lot of questions there.

MT: We're intuiting everything at the moment. Would like to see experimental in 6 months rather than proposed in 3 years. Would like to see this implemented and get some telemetry data.

MN: From a process standpoint, we could publish for H2 what we call an implementation draft.
(fast back and forth, concern about burning limited number space)

MT: It's not that complex - just push it through… but can we do that with the registry policy?

MN: One of the patterns I started with a different das burn an experimental frame id. That's something we could use. 

MT: Experimental should be fine.

Kazuho: I have an implementation using headers

MN: Interest in using this for non-browser cache-to-cache communication. Squid has done this for years Not sure we should explicitly target that use case but shouldn't explicitly disabled it either.

Natasha: there were three implementations referenced on the list, all server side


### Cache-control extension: Immutable

Patrick: Goes to a design pattern where resources really never change. Facebook said this applies to a lot of traffic, maybe 20%, huge number of round-trips checking on that.
... ran a mockup with facebook, and it worked well. Published, got some tweets, people started playing, seems to work well. It's not on release but we plan to put it out and run an official experiment. Most interesting thing is interaction with max-age. Currently honour max-age, but at the end of that a non-conditional response is given. We can talk about it - that's the only topic of interest that has come up so far

MN: biggest change is the real semantic

Someone from Yahoo: We see similar numbers on this. Why aren't browsers honouring max-age?

Patrick: doesn't provide a guarantee; interpret people getting 304 as a reload on that page.

Julian: While we have you up there and talking about reload. Is there a difference between F5 and ctrl/shift F5?

Patrick: Normal reload sends a bunch of 304s on the page and shift reload reloads the content.
Channel Roy Fielding: Immutable should override things like max-age. Also, please add more instructions in tools.ietf.org to point to github drafts, etc.

MN: very hard to add things to tools without tools team.

RoyF: well, you can fix https://trac.tools.ietf.org/wg/httpbis/trac/report/1
Patrick: implemented Brotli compressed format experiment. Did this in https only, seemed to interoperate except for one anti-virus proxy bug.

Subodh: Would Immutable only make sense to deploy for HTTPs?

Patrick: we only do it for HTTPs.

MT: You also only do it for strongly-framed responses, i.e. HTTP/2 frames or Content-Length, not just a connection close.

Patrick: there are a lot of issues

### Issues list for opportunistic security

MN: Think we just forgot to close issue 162? Issue closed.


### draft-pratt-httpbis-bytes-live-range-unit-01

MN: This draft proposing new range unit. Think Roy was proposing changing this to bytes if we get data that is appropriately safe. Not only would it not give you benefits of caching witht intermediates that don't understand this new range-unit and there are bad intermediaries that only understand bytes. Need to understand which path is less risky.

RoyF (jabber): Not really a change in semantics -- just a new interpretation of syntax that is not currently used in practice. So, it might break things, but isn't changing things. ;-)

Dharsak, testing from our side, changing the semantics of byte itself was trick, we found libraries that flipped out. we foiund the safer option is to define a new unit. Are there objections to doing that?

Chair: in terms of adopting a new draft we'd consider if it's general facilities for the protocol and there is implementer interest. There is scope for scope creep if we open up that discussion, think that it is general but not sure if there is implementor interest

Julian: If there are many intermediaries that do the wrong thing, would like to know. Do you use HTTP or HTTPs

Dharsak: Both in our experience

MN: Someone when and did the research on this. Bugs were in client libraries for media. Libraries consuming streaming video which is your core use case.

Julian: Concerned with shaky relationship between byte ranges and other content codings. Like to clarify that you really can't do a byte range request on something that has been dynamically gzip encoded - the outcome is logical from the spec but not intuitive.

MN: Come up but not interest to pursue that yet.

MN: Range unit is IETF review so would be substantial pressure to do it in httpbis wg.

Chair: Will start WG discussion on list to see if there is interest in adopting this.

### TLS 1.3 binding into HTTP

ErikN: I can make the break go further away...

MT: easy to answer. a bunch of discussions about this. Interesting data about how people replay data in the real world. You have to replay POSTs. The web depends on it. The net effect of that is if you send a post request and get a 0 bytes response you have to replay. That is exactly the situation we are in with 0RTT. We are sending a message and don't know if the server got it. It can be replayed by some attacker. If it's not idempotent, it's not idempotent. If you send a $100, you've sent $100 twice. This is a vulnerability that was present already.

MN: Found that intermediaries are doing much the some. Some respect the spec somewhat, but nobody does it perfectly.

Patrick: Made mistakeDid experiment with disabling replay of POST. But learned all kinds of curious ways in which the web does require it. One web site has a persistent connection replay time of 255 ms. But bug report says it works fine in IE. Have another web site that executes that under different permissions on the server side, and just closes the connection and assumes you'll call back. Unless you're willing to replay 7 times you'll not get it.

Subodh: There's one part of the component that's still missing. The application is the only thing that knows if the data is idempotent. We need a mechanism for the application to tell the http layer that the request is idempotent. Perhaps adding a header field that says this is retry-safe. We have use cases for this not only on the client side but also on the load balancer. Could improve your latency, but can only do this if load balancer knows its safe to retry.

JR: Use PUT

Subodh: Same problem arises.

ErikN: Given the somewhat surprising nature is this worth WG effort?

MT: Some of the things Subodh was talking about are still relevant for people using HTTP not on the web. In general when people are using TLS they need to be aware of this replay problem. We have to deal with the swamp that is the web. We need to have a document that RFC ... says about idempotency, etc.

Subodh: When you specify idempotency, would it be ok if this was only applicable for secure transport?

MN: There are a surprising number of protocol facilities where that decision has been made. Need to make sure the text in HTTP spec is correct and potentially new headers. Need more discussion.


## Friday


### RFC6265bis

mnot: want to stay true to what's implemented in code select a set of proposals that reflect
implementations after content consensus, then open the cookie spec then go immediately to WGLC

Have adopted:

1. [Leave Secure Cookies Alone](http://httpwg.org/http-extensions/draft-ietf-httpbis-cookie-alone.html )
2. [Cookie Prefixes](https://httpwg.github.io/http-extensions/draft-ietf-httpbis-cookie-prefixes.html)
3. [Same-Site Cookies](https://tools.ietf.org/html/draft-west-first-party-cookies)

many folks indicated that they've read these drafts

outstanding:
 - Cookie priorities
 - expiring aggressively those http cookies

We'll talk about these issues today, and then talk about what else we can do for new areas of work

#### Cookie Priorities

mwest: cookie priorities, shipped 3y ago, didn't tell anyone.
put together a spec and didn't ship it or present it.
idea: create another level of prioritization for cookies within a context of a domain.
current spec looks at age of cookie.
this allows some ordering of eviction.
certain cookies are important, some not so much.
important for large servers that have a ton of cookies operating across many contexts.
hit the 150 cookie limit quite quickly.
prioritization allows continuing with our current network arch.
also nice to give origins a way to control how cookies are evicted.
any Qs?

mnot: would like to hear other thoughts about this from other folks

mike bishop: so long as it's only within one domain, useful.
definitely would consider imp, if it makes it to RFC

mt: torn on these ones.
only a small number of origins that have this coordination problem.
hard to be sympathetic to that.
making cookies more usable is not a goal we should have at IETF.
I'd like to ensure cookies become less usable (where the second proposal comes in).
mgmt of logins across domains, I understand.
def heard of large corporate networks encountering this problem, they just delete cookies they don't care about.
creates a war within folks in a domain.
let's not make it better... already bad and complex enough.
cookies create huge holes in our nice clean origin model.

mnot: torn on this. have seen these problems.
from a chair position, tricky.
one browser is enthused, one is lukewarm (no opposition), not interested for another

gabriel montenegro: wondering if this needs to be a proposed standard, could be informational.
may not need to be in the main spec.
what about juggling and rearrangement of cookies in cookie jar?

mnot: could be an optional extension.
bar is generally interest from two imps.

HUM: Those who would support adopting cookie priorities.
(some hums in support, some in opposition)

pete resnick (opposition): it does seem like not a good investment of WGs time
sense is give it a punt. can always bring it to the ISC and say here's what we did

mt: I have sympathy for Informational.
we've painted ourselves into a corner by insisting we're adopting these docs.
that's used as a signal to rev 6562.
less objection if this were Informational.
good to be value-neutral on whether this is good.

mnot: the current cookie spec is very algorithmic [something something problematic]

mt: need to describe how cookies are managed in a less alg way.

mnot: need to find someone willing to do the work too!

pmcmanus: echoing pete when you say that right?
this may not be a great investment of our time.

eric nygren: we have a whole set of things we're asking UAs to do on cookies.
there are things that might be nice.
this may result in divergence in support, but may not be the ones we think have the most value.

mnot: teasing this out
anyone interested in making the cookie spec more extensible?
(no one to mic)

mwest: can get behind not making this normative.
more important that there is a definition for what Chrome has been doing.
sympathetic to cookies being problematic and not making them better.
making them usable, though, seems important.
we would not be able to use Chrome if we didn't have priorities... users would be logged out more often.
Chrome is unlikely to remove this, it's important to define it.
if this group isn't interested, we can do it somewhere else.

mnot: could be individual, informational RFC to document.

wseltzer: wonder if we've heard from others who have the problem on the server op side needing. ginormous cookie stores.
do we have evidence of others that want to operate with large sets of cookies?

mt: q for mwest? did you consider giving corp.google.com a 10MB cookie jar? (No.)
point was to allow users to specify domain suffixes (damn cookies) that they consider privileged
there is a down side to that, performance
but that may create good incentives ehre

mwest: if we were going back in time, it's possible that would work.
registered domain in the browser that has a much larger jar.
would have to do some work in Chrome to distinguish the domains.
unlikely to do this now, this is deployed.
might have been valuable 3y ago.

mnot: to answer wendy: have run into this in two of my jobs.
talking to a very large customer who is excited about this.
(chair hat on)
no consensus to adopt right now.
    
#### Expiring Aggressively Those HTTP Cookies (EAT cookies)
    
mt: experiments on the use of HTTP cookies.
premise is to look at certain classes of cookies on insecure origins and apply expiration.
might be an alt policy to apply to indiv cookies.
options in the draft to deal with 3rd party/1st party secure/not secure contexts.
most aggressive version documented here.
problem that I have with this document, making a policy statement about how cookies are managed.
difficult to reconcile with the spec.
mt wrote it but ambivalent if it becomes part of 6562.

mnot: need to have a discussion about this, PM BCP requires us to consider effects of these kinds of things.
doesn't mean we have to adopt it, need to discuss.
thoughts?

mwest: interested in this from Chromes perspective.
don't think we'd adopt this exactly.
but want to do something like this.
powerful features should be restricted to secure contexts.
user auth is a powerful feature.
what is documented is more agressive than we can ship right now.
what can we do that doesn't break the internet.
less plaintext the better.

mt: this came out of a powerful features in secure contexts.
sivonen remarked this may not break things, but makes things a bit harder.
closing a tab and losing logins is not so good, too agressive.
not a breakage, just a pain in the arse for users.
we don't want to be training users to type passwords more often.
3rd party contexts is interesting... tho 3rd party origins manage logins for lotsa sites.
3rd party subresources is a more interesting case... we can in some cases deal with that via. reputation systems.
making a statement on this would be useful.

mnot: no alg, just support for implementations to do things like this.

pmcmanus: this seems ripe for specification.
if you leave it up to individuals [to something].
think this is something we should adopt, can't just experiment with this.
made this change to be compliant.
useful to get a market to move but that we can;t do individually.

brian call, yahoo!: would like to see in the draft 'should be a shorter time'.
don't need to define the time.
what's changing, what's being removed.

mwest: yes, those details would be helpful.
need to assess impacts on implementations.
would be opposed to enshrining something before we know if it's going to work.

mnot: if we can come to a place where 2 imps have systems to do these experiments, and align spec with reality, that would be great.
seems like we have decent support for working on this and discussing it further.
inclined to say we should adopt this one, thoughts concerns?

(none raised)
    
#### RFC6265bis issues

##### [159: allowing cookies without key or value](https://github.com/httpwg/http-extensions/issues/159)

mnot: interesting research on how the RFC is implemented.
lots of red boxes in testing (those are bad).
number of those red boxes are due to not having an "=" and value, those cookies are not set.
trivial changes to the spec could align with reality of imps.
have people had a chance to think and look at this? good idea?

mwest: aligns with what Chrome does. Great idea!

Julian Reschke: worthwhile to refresh our memory why we didn't define this.
Roy had an opinion

mt: looking at the table, easiest thing to do is what has been described.
one imp appears to be divergent, would like to hear from them.
that might be difficult.

mnot: we have some homework. researching history, reaching out to other imps to understand their behavior.


##### [199: change definition of unique cookie to include host-only-flag to match browser behavior](https://github.com/httpwg/http-extensions/issues/199)

mnot: (reads issue to us)
anyone had a chance to look at this?

mike bishop: from my neck of the woods. we're not compliant with the spec, but compliant with what everyone else does.
defacto standard.

mwest: this aligns with Chrome, let's not do any more work.


##### [201: SameSite: Clarify user-triggered navigation behavior](https://github.com/httpwg/http-extensions/issues/201)

mnot: (reads) MT, is this editorial-ish?

mt: thought this was designed. if someone types in a URL... probably a bug in the definition not a design flaw.

mwest: meant this to be editorial.
alg does what we expect.
need to just write it down how it works.

mnot: flipping to editorial


##### [204: enhance title of RFC6265 to include "cookies" term](https://github.com/httpwg/http-extensions/issues/204)

mnot: this seems sane.

mt: or just "Cookies"

tis what it tis

Jeff Hodges: disagree, keep the same title and jam "Cookies:" to it

mnot: will do.
    

### Potential and Related Work

#### [TCP Tuning for HTTP](https://bagder.github.io/I-D/httpbis-tcp/)

mnot: this was well-received, discussed with Transport.
still have that call for adoption open.
will publish a new draft soon from daniel stenberg.
will adopt that and start work.

#### [Secondary Server-Cert Auth](https://tools.ietf.org/html/draft-bishop-httpbis-http2-additional-certs)
    
https://www.ietf.org/proceedings/96/slides/slides-96-httpbis-2.pdf

mike bishop:
this is combination of 2 drafts from BA IETF.
client certs + opposite direction we can do server certs.
current model has some frames that are on the stream of the request.
could potentially do a cert-request cert-needed.

kaoru maeda: confusing for client/server and connection stream

(slide with the opposited direction)

mike bishop: client does request at HTTP layer, server gets cert from another and responds in HTTP layer.
Why do certs in HTTP?
we're now dealing with a multiplex protocol in h2.
when dealing with multiplex protocol an coalescing across connections, we may want to talk to more than one origin in the same connection.
don't want one cert that defines every possible origin that a client wants to talk to.
at MSFT, we don't want the same cert to cover BING and microsoft.com, etc.
http2 prohibits renegotiation [in some case].
since BA IETF, two separate drafts (client certs, off in the woods draft on how to do it).
combined into single doc.
both sides can provide a cert without being asked.
requires decalring acceptable sig methods in SETTINGS.
certs can include supporting data (OCSP, etc.).
EKR found problems.
not everything is a cert (credential field for PSK).
perhaps the symmetry is a bit much in both directions.
Biggest critique: hard to convey sig methods given 32-bit H2 SETTINGS.
possible answer: EXTENDED_SETTINGS.
could define a cert setting frame.
many cases where you don't need 32 bits, some where you need mucho more.
(describes payload layout).
(desribes EXTENDED_ vs. nominal SETTINGS).
Should we do this?

mt: don't have a client here, prefer splitting certs and [] into two, ask TLS to do crypto stuff.
maybe just park it?
WG likely to be charterd in the future that might look like HTTP/3.
may do this there.

EKR: worried that will be HTTP/2b and this is HTTP/2a.
question about certs draft: what do you believe the clients' attitude towards certs that might be in connection 1 vs. connect 2.

mbishop: since this is the same HTTP/2 connection, not sure we need to distinguish.
not sure if that exporter is the same thing

Joe Salaway: know we ran out of time to discuss in TLS.
on the cert part, that would be a good topic for TLS

nick sullivan: in TLS, there is no way to provide multiple server identities over the same connection.
if that were available in TLS, that could make sense to pull some of this into the TLS layer

EKR: the question of where this is bad/good to whether this is TLS or HTTP.
question of crypto mechanics is orth to where it happens.
we might want to take a stab at what the crypto in TLS might look like.
see what the security proofs tell us about this.
sensible to design crypto, see if there is a single set of bindings for 1.2/1.3.
then we can ask if those bindings are better.
would be unfortunate if it only worked in 1.2 or 1.3.

bishop: with the prohib. on renegotiation in 1.2, can't do some things like this there

ekr: if we were to define this in TLS 1.3, we'd need to think about how to do it in 1.2

nygren: on the server cert point, going to be important to think about what is a secondary control, e.g., DANE.
and whether or not this is a SHOULD or MUST.
want to think about how much trouble this will pose down the road.

rsalz: bothers me a bit... TLS has a variety of auth mechanisms.
different key types in there... could be probles with saying X.509 is the only way here.
and if you make it more general, then you end up doing all the things TLS does.

pmcmanus: on secondary info piece, I would expect that be definied in extension using this

Nick sullivan: echoing EKR.
any security analysis on this negotiation, should match exactly the TLS analysis.
want to mirror as close as possible.
        
#### [HTTP2 and IoT (Gabriel Montenegro)](https://www.ietf.org/proceedings/96/slides/slides-96-httpbis-3.pdf)
    
https://tools.ietf.org/html/draft-montenegro-httpbis-h2ot

(matrix of IoT node/gateway/cloud vs. LAN/Internet)
(JLH: not going to scribe the preso)
stacks customized to emerging environments often trend to standard stacks. 
e.g. wap to tcp.. zigbee to ipv6. broad standards very powerful.
h2 is the best general alternative due to infra reuse, implementations, and security focus.
perhaps quic could have less security overhead.

mt: QUIC has its own fixed header.
you'll be getting the 9 octets in addition to what QUIC has.
will be less cruft that you see in front of the TLS headers (5 octets for headers, 16 for auth).
we are planning to run a TLS 1.3 experiment which means we may lose the extra 5 octets.
this is single-digit values of octets anyway.
compatibility risks we do need to worry about.

(IoT profile for HTTP2)
header table size: 512 from 4096.
push: may want to turn on.
concurrent streams: 1 or 2 or 3 (versus infinite).
window size: few kb.
frame size: could leave large.

mt: the minimums is also the default, so reducing would be incompat with some implementations

pmcmanus: is this what an IoT thing would want to use for settings? (A: yes.).
another way to think is that these are server defaults

GM: can negotiate params.
    
pmcmanus: to clarify, this profile is not implicit, but will be negotiated?

GM: not necessarily, we'd want to be able to use prior knowledge

pmcmanus: if this is implicit, you're undermining advantages of leveraging h2 existing infra (its a fork)

bishop: GM's previous draft about profiles, where h2c (constrained) came from, you can think of this as h2 with different defaults

mt: this is interesting statement to be making... you may be preaching to the choir!

GM: to respond to, maybe this is not the best place...
if we're doing something to h2, it seems like it should be done here.
want to get max benefit

mt: benefits seem to relate to accessibility, in that when you deploy something HTTP, you will have a lot of clients you can talk to.
don't have a good solution for authenticating servers of this sort, e.g., servers in IoT.
e.g., I'm running a server in my fridge, might be nice to auth that server from an IoT node.

GM: that's being addressed (bootstrapping auth) is in almost every SDO that's working on IoT.
problem is not a lack of solns but too many

mt: do want to take advantage of existing implementations of a protocol.
inventing new pairing protocols for auth, doesn't address that you've just cut off a population of existing solns.
how do we make this protocol available to these devices w/o making a separate set of networks that look like HTTP but that are not in the same environment as most other HTTP.

mnot: we have the HTTP expertise in this room (usually).
but we may not have expertise in constrained devices, how do we get them involved.
would love to hear from our AD.
the point about auth is oft-raised.

mt: push back on assertion that we don't know constrained devices (e.g., large servers are constrained).
similar in some respects, may not have made the best optimization choices when designing h2.
settings are there, thought.

mnot: HTTP WG creating an IoT standard may be weird.

Alexi: would be worried about undermining development of [something].

[JLH: Sorry, I'm missing a lot of this]

#### SDCH 

Chaals: SDCH is shared dictionary compression.
have a dictionary, that you can use to agree on dictionary to swap out bits of payload for. dictionary words.
we would like to consider security review.

ted hardie: google folks are working on something similar

pmcmanus: is this based on BCdiff... an existing RFC for things like this.
you could use something elses, but why?
Why not? Maybe IPR concerns. If it's not brough forth by Google, that could be a problem.
there is a ton of IPR around delta-encoding.
I have a patent in this space, not owned by me, may be expired.

ted hardie: intent by google would be to disclosre IPR and do what we've done with SPDY and QUIC for licensing

mt: CRIME bothers me.
an attack on compression methods in HTTP bodies, similar attach on header fields.
chosen plaintext mixed with secret information.
BREACH too.






