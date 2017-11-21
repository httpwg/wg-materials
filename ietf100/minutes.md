# HTTP WG Meeting Minutes - IETF100, Singapore


## Monday, 13 November 2017

_11:00-12:00 Morning session I, Collyer_


### Proposed Work

#### Secondary Certificates - Mike Bishop

Currently can't handle if  a server can possess more than one cert and similar for the client for h2 (client certs not allowed)

How to enable clients that wish to use client certs? same mechanism could be used for server side as well. using exported authenticators

Server can assert other domains for which it can present chained certs. client can request those.

Allows coalescing more broadly. also an option for SNI encryption (by first going to some intermediate SNI and then using the real cert subsequently)

Depends on exported authenticators which is going to WG LC in TLS. Right time to ask: adopt this here now?

Ted Hardie: on SNI encryption, what is the overlap with similar discussions in TLS?

Martin Thomson: this would be complementary to what TLS does. This would be for http (other protocols could benefit from the approach, though).

Ted hardie: I'd suggest adding discussion on how it interacts/affects http origin concept

_fair number of folks have read it._

MT: Nick Sullivan has some implementation experience (previous version). 

Mike Bishop: some testing in Akamai. 

Mnot: seems likely we should adopt it now, we've been discussing for a while. Will confirm on the list.

#### Bootstrapping WebSockets with HTTP/2 - Patrick McManus

rfc6455 (websockets) is very H1-specific. websockets community don't want to maintain an H1 stack just for websockets.

discussed at http workshop in London in June. Approach: minimal solution of tunneling websockets within h2.

scope here: websockets initiation within h2. (masking, etc, out of scope)

h2 opt-in extension to create an extended CONNECT for a new tunnel not through a proxy but to the ORIGIN, to use a different protocol (6455)

6455 metadata moved outside the tunnel to revamp the startup. 

stakeholders expressed interest to implement.

MT: generally like the approach. Seems as simple as possible.

Mike Bishop: this complements the previous presentation as features we left out of h2, which we need to correct now.

Mnot: some discomfort. looking into the server side as it may be more complex there. not that an opt-in extension won't allow this, but is it practice we wish to encourage? Think we should adopt this, but need to keep a critical eye on this.

Patrick: I'd include this option in the first flight of the server settings.

MT: with tls 1.3 won't have worst performance (but no 0-RTT), but an extra RTT with TLS 1.2.

Mnot: to take it to the list to confirm adoption

#### HTTPter scope of work - Mark Nottingham

revising 723X.

separate out version-independent aspects of HTTP. Last similar effort took 8 years, need to keep this tight. And move to internet standard.

Patrick: this could be beneficial, yes.

Ted H: parallel work (in quic) to specify HTTP over another transport. Seems like both efforts at the same time might lose some opportunities. how do these relate?

Mnot: that other work can't change semantics of HTTP. And this work has been portrayed as helpful for that other effort by clarifying the interface. This could be good as long as it finishes in a reasonable amount of time.

Ted H: If this had been done before that work started, it coiuld have had a good effect, but it may be late to provide that benefit and instead might take energy away from that which should be a concerted effort. Could now result in additional delay.

Mnot: I suspect this will have to happen anyway for quic.

MT: part of the motivation is to help quic. but would not publish this before quic is done. Some concern about how we're handling versioning. 

Patrick: should be mostly clarifying, no?

mnot: timeline? can be as aggressive as the WG wants us to be. We could be mostly done in a year, but not to publish before quic.

MB:as editor of http-over-quic: this would be really helpful for that work. we don't have a way to version the semantic layer. if we were to create one there's questions about this so I share some concern if we go there.

Jeff Hodges: how does this relate to h2?

Mnot: don't think we need to modify it (except to point at new references). It's fairly independent.

Alexey Melnikov as AD: no objections on this work. Like what has been said about timelines.

Patrick: gauging interest. not many hands. 

humm: twice as much humming for pursuing this.


### Related Work 

#### Variants - Mark Nottingham

Current variant via Vary is very coarse grained . draft-httpbis-key draft can target different parts of the header to use a secondary cache key.

but very complex. so new proposal:
    
draft-nottinghham-variants: lists all available variants for any given axis of negotiation (all langs for A-L or all encodings for A-E). Works well for known axes of negotiation.

Fastly has a less general form of this already in use.

Asking for feedback, not adoption at this point.

MT: even a sparsely populated matrix allows to determine if something is outside the cache.

Brian Call: looks good to know what variants are supported at the server

Harald: vs vary header?

Mnot: still use vary as some caches may not handle Variant, etc

Patrick: this could be used for h2 push

Mnot: Think we need further experimentation. It is an important space, and key does not seem satisfactory.



#### 451 New Protocol Elements - Shivan Sahib

making internet censorship more transparent

ietf99 hackathon developed some plugins to examine usage patterns

recommendation to add a blocking-authority and a geographical scope of the block

MT: on geo block per country code. would this replicate the blocking-authority information? If keeping both fields, might wish to add more info into geo-block. But doing so leads to a huge mess.Link relations might solve it by pointing to the right document somewhere that has the info.

??: censorship is too general a term. similar with geo, leads to questions of jurisdiction, etc.suggest changing should to must (provide justification)



## Friday, 17 November 2017

_9:30-11:30 Morning session I, Canning_


### Active Drafts

#### [Expect-CT](https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct)

Emily sent a summary.

MNot: Seems like a bit more implementation experience would be useful


#### [Early Data in HTTP](https://tools.ietf.org/html/draft-ietf-httpbis-replay)

MT: I think this is a done.  Lots of input from the WG with 3 implementations.  Seems to work and TLS 1.3 is about to go out.

EKR: Basically Ready

Tommy Pauly: Do we want a mention of TFO/TLS?


#### [Random Access and Live Resources](https://tools.ietf.org/html/draft-ietf-httpbis-rand-access-live)

MT: For an experimental draft, this is plenty of testing.  

Darshak Thakore: Should we go to last call for this?

Mnot: Should we give more time to give implementers more implementation experience before last call?

MT: Document and testing is high enough quality that this doesn't need to be experimental.

MNot: Would like to get Apache, CDNs, Varnish team themselves to take a close look at this as well.

Ted Hardie: How does this work if the beginning of the content expires?  How do you know the last possible moment you can go back to?

Craig Pratt: As long as there's some overlap, you should get partial content.

MNot: Ted's question brings up the next question.  Now that we're comfortable with the safe, do we think this will be cache-friendly?


#### [Structured Headers for HTTP](https://tools.ietf.org/html/draft-ietf-httpbis-header-structure)

MNot: Putting aside the details, is this the general direction we're trying to go in?

Kazuho: I really like this draft and think it's a good direction.

Patrick McManus: Asks how many people have read the current draft and the former?  Like 6 people.  

MT: A lot more folks who aren't here have read the drafts.  Thinks this draft is much more promising than the other draft.

Patrick McManus: Previous feedback was this was 'too big' and this was an effort to narrow the scope of this.

Mnot: Encouraged by the level of engagement on the list.

Michael ?: Was there any reason not to have a length?  Thinks 

MT: If we were to retroactively apply the rules to new headers, you probably should use these practices.

Julian Reschke: Relayed from jabber: I think this goes into the right direction. Would be good to decide on adoption soon.

Yoav Weiss: Better structure would provide much better HPACK compression and relieve the pressure to give new params short names to save bytes. 


#### [Cache Digests for HTTP/2](https://tools.ietf.org/html/draft-ietf-httpbis-cache-digest)

Sebastian Deckers: Is there any intent to add signalling when a cache entry is inserted or expired?

Kazuho: The server can assume once a resource is pushed or requested, it should be in the client cache.

Mike Bishop: A single simple filter seems like the right approach and it's not supporting multiple.  On the 

MNot: Yoav, are you wearing your 'Chrome' hat?

Yoav: To some extent yes.  Chrome and Akamai.

MNot: If there's a good chance of getting browser implementations, that'd be a good development and I could take my name off the draft.

Sebastian Deckers: Did an experimental prototype with a service worker, and the results were very positive.  Thinks we should move forward.

Patrick McManus: Labeled as experimental.  Kazuho, what would you like to do?

Kazuho: Best option would be a or c.  

Mnot: Does it make sense to publish document with headers and service workers and keep it experimental?

Yoav: Replacing GCS with Cuckoo filter seems like a good change for reasons mentioned.  Not seeing GCS being adopted.

Sebastian Deckers: No real opinion on GCS vs Cuckoo, but do have a hackathon experiment to compare them.  If that helps?


#### [Client Hints](https://tools.ietf.org/html/draft-ietf-httpbis-client-hints)

Update from Ilya Grigorik, who is not here today.

MT: There was a conversation about the Geolocation header?  Where are we going long term?  Geolocation is an awesome test, but a terrible thing to add.

EKR: What is the experiment?

Yoav: Regarding geolocation and privacy, at some point we need to distinguish between active content and passive content.  Add something to feature policy to select 3rd parties instead of everyone.

EKR: This obviously has a privacy implication, and everything you leak has implications.  

Mnot: In terms of geolocation, we should not be adding new things to this document.

Yoav: Re EKR's points, this is not about sending user private info everywhere.  

Brad Lassey: If the user is opting into providing information, how is that an unintentional leak?

MT: If the site asks for something once, then it's now being provided on every request forever.


#### [RFC6265bis: Cookies](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis)

Mike is not online.

MT: Having a discussion internally about cookie expiration.  Different browsers have different policies.  Be nice to have more consistent strategy across user-agents.


#### [BCP56bis](https://tools.ietf.org/html/draft-nottingham-bcp56bis)

MNot & Patrick McManus: Read the doc, want some feedback.  Important to communicate the knowledge and experience this group has to other working groups.

Xavier Marjou: Does this document best practices for REST APIs?

Mnot: Target audience is IETF WGs that want to use HTTP

Ted Hardie: 


### Related Work

#### [Compression Dictionaries for HTTP/2](https://github.com/vkrasnov/h2-compression-dictionaries)

Patrick McManus: Motivation is obvious, trend towards smaller resources means within-stream compression does not work as well.

Everyone is a bit nervous about whether this is dangerous.

Asked for external review, but have not been able to get anyone to sign up to say this is ok in this case.

Yoav: Tried to analyse the risks and potential mitigations.  Mitigating attacks across origin is the simplest, the client can say that's illegal.  

Less obvious about same-origin secret leaks.  Most of the time the attacker can just fetch the secret content, so this isn't an extra leak.

If the origin does protect against pages fetching information directly, 

Could restrict this to non-credentialed fetches.  That would restrict the usefulness, but it'd be better than nothing.

?? from Google working on shared Brotli, which is similar work in this space.

MT: Patrick summarised this from the outset, lots of uncertainty here.  

Ian Swett:  Do we have an idea of how well shared dictionaries work compared to cross-stream compression?

Yoav: They address different use cases.  Shared dictionaries work well for large websites with similar content.  His proposal addresses 'bundling' use cases where resources compress really well bundled together.

Out of band shared dictionaries can give better performance, but are not necessarily as good in all cases.

MT: Performance of this is very persuasive.

Lode Vandevenne: Google's compression team working on shared brotli.  Also have a draft spec available?  https://github.com/google/brotli 

MT: The proposal as written is a patch on the FETCH spec.  Sort of makes it incomprehensible as a result.

