# HTTP Working Group Minutes - IETF 99

## Wednesday, 19 July 2017 Afternoon Session I (13:30-15:00)

*Meeting began at 13:30*

Blue sheets going around. 


### State Management Bis (Mike West)

MT: Point of that draft (draft-thomson-http-omnomnom) is principles by which you'd set policy. What Chrome does is a subset and could change over time. Need to allow for changes in the environment. A framework for UAs to set policy. Happy to talk about what these policies might look like

MNOT: Is this good, or do you want more definitive.

Mike West: It's good.

### Expect-CT (Emily Stark)

Will ship in Chrome 61 in September

Two open issues

Expect-CT reports ought to trigger Cross-Origin Resource Sharing (CORS) preflights.

Send them (that is what Chrome does now)

Stuff report into whitelisted text?

Knowingly violate CORS?

Nick Sullivan: can the report be on the same hostname as what triggered the CORS?

Emily: draft doesn't say. Chrome doesn't allow

MT: We never got to conclusion. Would like to. Why isn't it possible to put the origin in teh origin for the preflight?

Emily: not what origin is. 

MT: it's the origin that generated the URI

E: if evil.com includes a source from victim.com, victim.com needs to opt-in. So evil.com in the origin header.

MT: Expect-CT comes from the victim. Doesn't matter who initiates the request

E: Report URI can be arbitrary.

MT: victim.com doesn't want to send reports. It's not a cross-origin request. Perceive it as the thing that set the policy should be considered the origin.

MT: Talking past each other on the list

E: Will think about it more and talk on the list. 

MT: Alternative is for the person setting the Report CT on their own origin. Number of different ways to skin that cat.

Chair: leave this issue open?

E: The draft says nothing in particular about sending CORS.

MT: Would like to see a plan for a solution. Here or in another document. May be appropriate to say nothing about CORS.

Chair: is there an issue for this on the fetch spec?

### Header common structure (Mark for Poul-Henning)

Mike West: JSON has tooling everywhere. Easy to use. Good to use that.

Julian: main issue - not making progress.

Patrick: a little patience

Michael Bishop (via MeetEcho): Agree that parts are missing but think it's salvageable.

Chairs: need to talk to Poul-Henning and huddle

Mike West: have a good understanding of security properties, no problem with using existing JSON parsers

MT: Current draft came from a place where it was aspirational about its goals. Maybe can be salvaged, but would like to see goals articulated first. 

Mark: Started discussion on the list. Need to establish goals and get consensus on them.

### Cache digest (Kazuho Oku)

DKG: Haven't read the draft. Are you expecting the client to remember this for the life of the resumption ticket?

KO: Yes. Life of the session ticket.

DKG: This header is synced and retained?

KO: Yes.

Mike Bishop: Interested but no immediate plans. see how it goes. What size do you need for acceptable false positive readings?

Mark (explaining): what size for a reasonable false positive rate?

KO: We have a small size. 100 bytes for now.

MT: Last than half the HPack state. I thought they were fairly small.

MT: Should be published as Experimental. Has been sitting and not changed in a while. It's an experiment on top of an experiment (server push)

?? from Chrome: Interested. Hard to implement with our current cache implementation. Low probability of being required.

J. Iyengar (Google): Agree with Martin. Should be experimental.

Mark: Worse case, if a browser tries and it doesn't work, we've burned one identifier

MT: Can we move the origin frame to later?

### Random access and live content (Darshak)

(about 6-10 have read the draft)

Will get data


### Replays in HTTP (MT)

Victor: we don't have a standardized method to comm between gateway and server. Early data feels weird in this context. 

MT: The origin server is aware of LB or CDN. Not sure about this concern

Victor: Mostly an observation that feels weird.

MT: Difficult when constructing a message to know the status of the wire. This allows the clients to send the message twice.

Subodh: If I had some data, don't need a separate API for early data.

MT: "handshake complete" is the mark

Kazuho: ??

Nick Sullivan: Support this draft. What about TLS interception proxies.

MT: Nothing I can do about this

DKG: Semantics for 4xx. You as a server need to know the complete architecture. Need to identify the request that cannot be sent.

DKG: Permission to retry means it is safe to retry. It's not that we're not processing because it *could* be replayed.

MT: That's the critical guidance that I don't feel confident about

DKG: IF we're going to have 0-RTT we need this.

**hums**

* How many read the document: low hum
* Do you favor adopting: mid hum
* Oppose: crickets


### Origin (anything more to discuss?)

draft-ietf-httpbis-origin-frame-03

"Clients MUST NOT consult the DNS to establish the connection's authority for new requests"

No WG consensus yet.

Patrick: Consensus on that existing DNS provision of 7540 is a weak second factor. Difference of opinion about how valuable.

Mark (editor): we haven't specified the exact stack for verifying a certificate.

MT: Right advice is to acknowledge that DNS is important, recognize that the privacy benefits are significant, and leave it to the UA to determine whether a particular request can be made to this server. Normalization comes with time. Value in the MUST NOT DNS statement. Servers should not have to make DNS servers

Mark: Uncomfortable when you say servers relying on this property.

EKR: How can the server rely on this?

DKG: Agree. Can't make it a MUST NOT.

Mike Bishop: Echo concern. Don't want a MUST NOT. Clients MAY do other things, have some guidance. That's a smarter path. Also must harmonize with the other draft.

EKR: The weak second factor is the network path associated with DNS. Say you got it over DNSSEC, we don't trust routers entirely. Three postures:
- what's in the draft
- Encourage to do second factor (but not specify)
- Take no position

EKR: should specify possibilities.

Victor: cannot promise that they will handle in a certain way. From UA perspective there is no viable strategy no DNS queries is bad. Should document what might be a second factor.

??: would like to see what is the second factor.

Ben Schwartz: Having even an open-ended extension field in ORIGIN would be useful

Erik: Using something not specific for privacy seems bad.

MT: push back on holding this one because we might want to do something to the origin frame. It's orthogonal. The DNS requirement is a policy decision we made by accident. Should not rely on this so thoroughly. Sad.


### BCP56bis (Mark)

Explosion of use of HTTP for other things 

Jana Iyengar: Makes sense to consider what is needed to make HTTP a good substrate. Things are baked into it that don't scale, like latency.

Jana Iyengar: Is this the community?  Are the people doing it here, or are they just using a library and not knowing what's inside.

Mark: JMAP are an example. They're here. We can help give them guidance. There's a lot of people in this WG who can help

Jana Iyengar: Might be some people that you want to invite.

MT: like the general goals. Push back on Jana. HTTP is not a dumb transport protocol. Want the document how to use it. Has been (ab)used as a transport protocol.

Mark: Roy Fielding knows whenever you call it Hypertext Transport Protocol.

AR: JMAP is a good example

Alexey: Good to have a checklist about what you should do and when.




## Wednesday, 19 July 2017 Afternoon Session II (15:20-16:50)

*scribe note: "(?)" signifies I was not sure re accuracy of what was captured*

### HTTP/QUIC (Mike Bishop(mb))

#### slide 7: need to get agreement wrt what we need to ask of QUIC 

martin thomson(mt): the question is on the agenda there

mb: not aware of any new reqs

mnot: focus on single stream vs multiple stream issue

#### slides 8 & 9

need to decide between one or two streams 

MT: we should use one stream - race conditions (my term -ed.) with two streams
need to understand the hpack cancellation prob will be there until we solve it explicitly

Jana: the push_promise use case speaks for one stream
in quic WG, know we can make things work with single stream

subodh: supports one steam

ian swett: supports one stream. 

#### slide 11: shoehorning HPACK

HPACK alternatives: QPACK, QCRAM, HPACK w/ zero dynamic table size

QPACK is more wire-format focused

see the drafts on slide 11

MT: would much prefer QPACK

qcram has various issues he has observed

charles'buck'krasic(cbk) (qcram draft author): open to removing one of the things MT objects to - table eviction (?). Does not have data yet on whether it helps at all

Alan Frindell: my experiments didn't show it moving the needle that much, but I'd like to run more experiments

cbk: have data on # streams over the lifetime of connection, in practice almost not one raised table sise beyond 4k. need more data

ian swett: have detailed comments to address in person
would rather stick with hpack for now
but premature to pick direction wrt this now

mnot: wait until Seattle to make decision?

[ "seattle" is an upcoming interim meeting ]

### slide 13: settings and handshake

ian swett(is): we can put the settings in the 0-rtt msg

mb: yeah, tho [settings frame essentially as good (?)]

thardie(th): (1) <missed it>

(2): if client settings in clear, need to describe the implications
so maybe more appropriate to keep quic settings sep from http settings

ekr: settings in clear + only sent once is unfortunate
am not persuaded this would be a good change

jana: agree w/ekr
http & quick settings have different privacy properties

dkg: this privacy tradeoff is poor one

mb: ok, will update issue in github

### slide 14: integrated errors

mt: the proposal here is to forbid quic to close specific streams
app needs to be able to kill connection due to its own errors

cbk: for hpack case  could have errors that should result in closing connection

jana: there is no quic error that will cause quic to close stream
it seems odd here for app to close connection
quic has signalling stream, app should do that to signal needs and quic can then close stream

mb: perhaps could convey such on signalling stream

mt: hazard is the connection continues during time the close-conn processing is occurring
having quic being aware means quic machinery will be doing lots of stuff instead of just going away

Charles 'Buck' Krasic 4:04 it seems very likely to me that some HPACK/QPACK/QCRAM errors will necessitate closing the connection.

jana: [seems to agree w/MT]
we should have this discussion in the quic WG too

### slide 15: priorities and placeholders

mb: FF implements priorities using idle streams which are never used

patric mcmanus(pm): individ:
have a table of grouping orders to do this?

mt: the ? stream id does not allow us to do this
would have possibility of DoS because the stream is just a placeholder, and other party can just open streams up and consume resources on ur end
dont think u avoid the unbounded state problem by doing this

cbk: i head it said a few times some unhappiness w/h2 priority scheme, so http/quic ought to address the h2 priority scheme?

mnot: head expressed most is we want to keep this as close to h2 as possible, but we will assess this as we go along...

mt: sticking to that philosophy means we should be open to possibility of re-engineering the priority scheme, but we have lots of balls in air, thinks other issues are more important....

mnot: folks have expressed to not do opportunistic changes here

mb: even this is quic wg doc, we want to be responsive to h2 folks
sound like wrt priorities, h2 folk are ok not changing this now....  (?)

### slide 16: HTTP/2 Divergence

mnot: finds the current registry lang to be confusing so would prefer to have them separated

mt: at the point that we made the decisions to make q/http subtly different than h2 we did make a new protocol
some h2 things can be ported to q/http, but having an explicit signal that things like extensions will not just wqork in both prots q/http and h2

ekr: pushed back on this last time, how do we make sure "that" happens?

mnot: trying to enforce that via registries does not seem to work

mt: one of the things trying to preserve here are some reasonably similar semantics between h2 and q/http (aka "hq" ?)
ought to have strong guidance to implementations that they should consider both h2 and q/http

mnot [ essentially agrees w/MT )

cbk: [ essentially agrees ]

ekr: do you think it would be possible to see a PR that does these things in slide 16?

mb: have one, need to update it, even update IANA guidance that one does not update one registry w/o updating the other appropriately

mnot: also have the experts be same on both registries

mb & mnot & ekr: [ agreed on some approach to registries that I missed the details of :( ]

### slide 17: Authority

aka issues with origin in sense that TCP is assumed under http: and https: schemes

mt: the URI spec(s) define port as just a port, not a tcp or udp port

we are treading close to updating 7230...

we might get to updating 7230

jana: we do not need to update https yet, it is interesting but you know other endpoint speaks quic but not tcp (how?)

ekr: iepg meeting on sunday, discussed confusion between tcp and udp and ports

thardie: are you working with IANA to clarify status of port 443 ?

mnot: current register of port 443 replied, iesg is considering a more wholistic approach to this issue. if you look at well known ports we have this issue a lot.

ekr: iesg should just have control of ports

thard: iesg does not nec. have that power, iana is suggesting a "release and catch" approach, but if want another mech, there is a doc that needs updating

mnot: has discussed with joe touch

alexei m: port reassign is doable, some doc coming on it (?)
 
 
## julian reschke: HTTPtre

https://github.com/httpwg/wg-materials/blob/gh-pages/ietf99/ietf-99-httptre.pdf

mnot: not start this now, right?

jr: yes. tho wonder who might be interested in contributing to such an effort...

jr: maintenance is never as exciting as new work...

mt: we have issues open in wg repo, some will require discussion, how deal with that? cant just be in background without interaction

mnot: some will req discussion, manageable set

mt: the 723* effort was hard unglamorous but quite useful important work, concerned that such a maintenance effort would sap cycles from the new work

mnot: there is work in browsers, eg fetch(), where they have questions/input and we can't ignore that

pm: [ agrees ]
