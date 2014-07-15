# HTTPbis Minutes IETF 89, London

Chair: Mark Nottingham

## Session 1: March 3, 2014

Scribe:  Ted Hardie

Mark reviewed the (old) note well and a scribe is selected. Eliot Lear acted as
jabber relay.

### HTTP/1.1 Update

Julian Reschke summarized the status of HTTP/1.1 Draft 26. Julian expressed
hope that next time we can announce RFC numbers. Since Vancouver there have
been two sets of drafts, one set on lETF last call and one on IESG comments.
Review of 7 years of effort (including a picture of the editors which can be
included). 2616 subversion comments.

The IANA registries have been created and/or updated; the drafts are in the RFC
Editor queue, with 11-document cluster. Publication expected in 6 weeks or so.

Julian reviewed some of the changes which occurred (see Slide 9 of [Julian’s
deck](http://www.ietf.org/proceedings/89/slides/slides-89-httpbis-1.pdf)).
Julian then reviewed draft-reschke-http-status-308-07, which is currently in
the RFC Editor queue, but now needs updates to deal with the changes in HTTP
since it was written. Julian then discussed the steps needed to retire RFC 2617
(finishing Basic and Digest in HTTPauth).

### Zurich Interim Summary

Mark then reviewed the Zurich Interim, covering both the Interop aspects and
the security discussion. Mark notes that the group is chartered to complete
last call in April.

[http2.github.io](http://http2.github.io) is now the tracking point for
implementation effort tracking.

### Local Activity Report: Japan

Mark then noted that a large contingent of the implementation efforts are in
Japan, and there was a short Local Activity Report in Japan
(http://www.ietf.org/proceedings/89/slides/slides-89-httpbis-2.pdf). A review
of the various meet-ups was accompanied by discussion of existing tests (e.g.
the HPACK Test Case). They also mentioned http2.info, which has a set of
resources, and it will include a Japanese translation of the specification.

They will write an I-D containing a summary of the efforts so far. Mark
suggests that there might be value in cross-linking the sites or moving the
repositories to be collocated, and he thanked the presenters again for the
efforts of their community.

### Editor's Summary and Questions

Editor’s slides are:
http://www.ietf.org/proceedings/89/slides/slides-89-httpbis-3.pdf. Martin began
the review going through the summary slide (“Since -09”), which is largely
editorial work. This gives him hope that we are very close to done. He’s trying
to use this presentation to discuss how many stand between the working group
and conclusion. (See slides 4 & 5 for the list reviewed). Martin then picked a
subset of this (“The Hard Ones”). HPACK security is one; there are some issues
but there are potential ways forward. Priority has too many options. A group of
these (“The Snarls”) are things that must be pulled apart. At the time of
writing the slides there were 28 issues of which 18 were design.

### ALPN Update

ALPN update was given by Andre Popov -
[Slides](http://www.ietf.org/proceedings/89/slides/slides-89-httpbis-6.PDF)

Most of the focus was on slide 8, which reviewed the changes since IETF88. The
IESG has evaluated and approved the ALPN draft; there are minor updates
required from IESG review. The biggest change is the removal of the text which
forbad the sending of an alert unless a negotiation supporting it had occurred;
it can now be sent without negotiation. Andrew then reviewed the ALPN
Deployment *.google.com servers have ALPN enabled; Chrome and IE11 support
application protocol negotiation via ALPN. Andrew then reviewed the methods for
working around ClientHello issues; draft-agl-tls-padding describes the work
around. Codepoint for the workaround has been approved by the IESG and request
sent to IANA (IANA issue: 747903). Julian asks whether this is a common issue
[meeting interrupted by evacuation warning; meeting resumed at 13:35]. Andre
replied that it is not everyone that needs that, but if your client hello sizes
are large, you definitely need that. A question was whether IE would have the
issue with large domain names? Andre noted that it was possible, but that they
have not seen issues.

### HTTP/2 Issues

The group then started review of the [HTTP issues
list](https://github.com/http2/http2-spec/issues). Mark suggests that we start
by working on the two sets which are not as involved, in the hope that we can
make quick progress on those.

#### 422: Structured Tokens for ALPN

Roberto just raised a new issue around [structured tokens use with ALPN
tokens](https://github.com/http2/http2-spec/issues/422).

Marks first asks whether that is an issue for the HTTPbis working list or TLS.
Roberto says that this is an issue for the registry; Ted Hardie says that this
is an issue for utilization of the registry. Martin says that the concern of
over-use is not valid, because the numbers we were discussing is small. 4 or 8
are reasonable inferences for what we are talking about now, and those are
reasonable numbers.

Ekr says it is important to distinguish between conserving space in the
registry and conserving space in the client hello. Roberto says he is concerned
that is used for more than HTTP, and that it may cause issues. Mark suggests
that this issue is connected to the websockets issue which will be dealt with
later. Patrick McManus agrees that this is scoped to HTTPbis, and he believes
that the current combinatorials that this is not an issue. Will Chan agrees
that the current issues are not a problem but he believes that Roberto’s issue
is future-proofing and that we could see these combinatorials in a few years.

EKR notes that the issue here is that there is binary matching approving
something with a more complex matching semantic needs to be done now. Will Chan
agrees, but believes we do not need to block current work. The group agrees
that in the short term approach will be to restrict the characters included in
the registry entries, in order to preserve the possibility in the possibility.
Yutaka Hirano notes that they are considering defining ALPN tokens for
websockets, and the presumption is that they will abide by the token agreement
(cf. http://tools.ietf.org/html/draft-hirano-httpbis-websocket-over-http2-00).

“As long as the security properties are appropriate for the scheme” will be
added for the [mixed schemes
issue](https://github.com/http2/http2-spec/issues/421).

RESOLUTION: Constraining ALPN tokens formally isn't in-scope for this WG, but we'll endeavor not to use special characters.

#### 419: Consistency of Settings

The group then discussed the [consistency of
settings](https://github.com/http2/http2-spec/issues/419); Mike Belshe had
suggested that all settings be included in all settings frame. In HTTP/2 there
is no settings extensibility, so this may make sense. Martin prefers that there
be no particular recommendations or requirements here. Will said he doesn’t
want to bikeshed too much on this, but he would have preferred to send it
always. Roberto said he liked Martin’s suggestion. Issue deferred to the
editor’s judgement.

RESOLUTION: agreed to defer to Martin's judgement (who favoured #3).


#### 421: Mixed Schemes

The group returned to the issue of [mixed
settings](https://github.com/http2/http2-spec/issues/421).

Emile is concerned that it has happened only for five hours. Mark asks whether
there should only be one scheme per connection?

Emile proposes that the document say it is not safe to mix them.

EKR asks if we are not pre-deciding the issues Roberto raised in Zurich about sending HTTP schemes over HTTPS.  

Patrick says he believes the document is silent on this. 

Ekr is worried about us being silent on this? What do servers do? Martin says
that there are a bunch of things here. The intent is to send their HTTP queries
over their TLS connection. How do you get to the point that you are going to
get to that. He felt we were never going to actively prevent the request for
any URI over these connections. (Potentially with a “scheme unsupported” return
code).

Ekr doesn’t want this to be unspecified.

Emile wants to record that multiplexing HTTP over HTTPS may increase the
performance, but there are a lot of things in the middle path that will be lost.

Mark notes that the question is how we structure the specification over how you
determine what is safe.

Will Chan suggests that this is not the issue to decide the broadest issues
under, but he confirms that we really need to be able send multiple URI schemes
transports over a single connection.

Patrick believes that the security requirements issue needs to be resolved
separately, but it is not necessarily true that you need to fold your insecure
http over your secure transport.

Eliot notes that it is important that the service be able to indicate what it
will accept.

Mark clarifies that this issue resolution will be editorial noting that it is
possible, and leave the larger issues to a different discussion. He asks if
that is okay, and Larry Masinter is not.

Larry notes that the capability was restricted to the proxy case; Mark notes
that Roy disagrees.. Eliot asks that this simply be deferred as a design issue.
Mark does so.

#### 417: Change the way we identify plain text HTTP/2

The group moved on to [Change the way we identify plain text
HTTP/2](https://github.com/http2/http2-spec/issues/417), but Martin noted that
this might be a bike shed.

Mark notes that this might not be--does the
identifier for ALP describe the entire stack--so that there are different ALPN
identifiers for http/tcp vs. http/udp vs. http/tls.

Martin notes that Roberto was the strongest advocate for something else in this
space.

Robert says he does not want to change what we are doing now. Clarification
asked of Roberto and he agrees.

Peter Lepeska comments that this feels very ad hoc; he feels that they will
eventually need to be structured. Eventually there is going to be.

Mark reminds him that we just had that discussion. He feels it is not well
defined now; Martin notes that an alternate will make it obvious that there is
no structure.

Roberto also raised [default max
stream](https://github.com/http2/http2-spec/issues/416); Martin asked that this
be deferred until after HPACK and this is agreed.

RESOLUTION: will use two identifiers, and they will identify the stack used. Editor to choose specific ids.

#### 405: "Authoritative" Restrictions

[“Authoritative” restrictions
issue](https://github.com/http2/http2-spec/issues/405); Martin reviewed the
text in HTTP1.1 and he proposes that we references the 1.1. text directly for
this issue. 

Mark had previously expressed the desire to make it possible to change this
meaning; Martin responds that this change should require and updating RFC.

RESOLUTION: Martin to use HTTP/1 text.

#### 404: Gzip and Deflate

The group then discussed [GZIP and
deflate](https://github.com/http2/http2-spec/issues/404); SPDY had required
their support no matter what you said on the wire.

There seems to be consensus on the list to require at least one; should we
require both?

Martin’s read was that we had roughly gravitated to gzip; he’ll take that if
there is no objection.

EKR then asked whether we have worked through the security
consideration here? Exactly the same compression issues we see other places may
be present here? Note that this not required to use. Ekr says that this has the
effect of endorsing compression;

Mark asks whether his counter is to removing compression, since it is already
there.

Ekr says that we should have that discussion, and that he had the impression
that this was basically unsafe.

Patrick McManus notes that there is a security/performance trade-off and the
performance advantage is very real. The web currently runs on this, and there
is one corner case where this is an issue.

Martin asks whether security considerations text would cover the issues.

EKR suggests that they try to write such considerations and see whether the
result makes people side. Will Chan wants to re-affirm that the issue here is
that intermediaries strip out accept-encoding gzip; this makes it possible to
use without intermediaries’ activity impacting this. He feels security
considerations are necessary.

Kathleen Moriarity would like to have the discussion happen before the decision
being made.

Mark notes that there are two things going on: should we make the assumption
that gzip is present in the client; the second is should gzip being used in the
web context or not. If there are security considerations to gzip, we should
talk about them, but removing this is likely a non-starter.

Roberto said this requirement for static data is so fundamental to performance
that HTTP/1 would likely be faster if we denied its use in HTTP/2.

Julian asked if we are asking also for server support for this.

Patrick believes we could revisit the decision, but the current question was
gzip or gzip/deflate; he feels that the answer here is gzip. If we need a
separate issue for security considerations around gzip for the web, we can do
that.

EKR thinks that is satisfactory.

Bill Mills thinks that the issue isn’t solved by a security consideration, then
the issue is really about how the leakage occurs and that this needs to be
addressed; yes, it is

Peter Lepeska notes that gzip over not-TLS does not have this issue; IE11 will
support http2 over not-TLS with gzip, so this may increase the amount of data
sent in that mode. That’s valid.

For this issue: gzip only; a new issue will be opened.

RESOLUTION: gzip only + editorial massaging.


#### 424: Support for Gzip at the Server

[Support for gzip at the
server](https://github.com/http2/http2-spec/issues/424).

Martin’s understanding of this space is that something like gzip is pretty
minimal, and he’s wanted this in the past. This will get taken to the list.


#### 386: WebSockets

The group then moved to discuss the issue of
[websockets](https://github.com/http2/http2-spec/issues/386).

In Zurich, the discussion concluded that there would be no direct support for
it at this stage. If folks needed slight help to improve the layering, it might
be supported.

Mark notes that you could carry ws over the current alpn identifier, and if
that created problems, then a new alpn identifier would be created.

Salvatore Loreto, Hybi chair, noted that they don’t have much energy for this
and want to close. Can this work go into HTTPbis.

Mark noted that this made him nervous and he’d need to talk to the ADs on the
topic. Robert said that this applies to WS and other protocols, and at least as
interestingly, loadbalancing them all. We'd need the RST for unsupported scheme
thing. Mark clarifies that this was a proposal for an RST error code at the
HTTP/2 layer. Mark opens a new issue for this.

Martin is concerned that this might create trouble if things are available for
some parts of the URI path tree. There is some discussion here with respect to
the authority section of the URI; this is going down to the scheme now. He’s
wondering if that is an HTTP error. Is there a need to make this up one level?

Mark says don’t try to kill too many birds with one stone. He feels it may be
better to make an HTTP status code.

Ted Hardie argues that you want to scope that for the common case, and that the
common case is “nothing from that transport layered here”.

Mark pushes back that we actually have status codes that have a wide variety of
scopes in HTTP and this could be one of those; Ted replies that this may not be
the case for all things being layered on top.

Martin agrees that this is a scoping problem and believes that you can get the
right scope with an HTTP status code.

Will Chan notes that when they started this at Chrome, they used NPN for it, so
that there was no need for stream-level issues or errors.

EKR that this does not make sense with ALPN.

Patrick discussed how the alt svc drafts does this same indication.

EKR believes that we want some method of discovering when an existing
connection can be reused for a different scheme, and he could be talked into
many methods of making that work.

Mark believes that we don’t have a decision on this at the moment and
discussion should continue.

#### 385: Huffman Codes

Huffman codes reviewed briefly and agreed it is on track for mechanical
resolution.

#### 381: DNS-Based Upgrade

[DNS-based Upgrade](https://github.com/http2/http2-spec/issues/381) discussed. 

Eliot doesn’t think this should block HTTP/2; it sounds like nice follow-on
work; it should work for both HTTP/2 and any subsequent versions. The issue he
has on SRV is that it may require multiple queries; he’s happy to experiment
with folks who want to work on performance problems.

Roberto said that in all cases on out-of-band knowledge, the browser or client
MUST be willing to learn that it now fails. DNS is no different from having
learnt from a prior connection in-band.

Martin says that we can solve this after we send the spec to the IESG.

Patrick does not want to block HTTP/2 on this; there are some corner cases that
make this difficult; he suggests that including DNS as a potential source of
prior knowledgde and leave it at that.

Emile comes up to say that it is not his intention to block over HTTP/2; he
does, however, want to discover when content can be found on an other point.

Roberto agrees that it does not block, but you should suggest how HTTP/2 if it
is not successful. If you believe you can connect on HTTP/2 and you fail to
connect, does it fall back or not? [Note that this is not limited to this prior
knowledge source]. Needs more discussion.

Patrick notes this is addressed in alt svc; review it and discuss on Wednesday.

Martin replies to Emile’s suggestion that we’re chartered to allow for discover
ports over 80 or 443; he agrees we have items that may allow for that, but
we’re not required to provide that discovery.

RESOLUTION: this is decoupled from the HTTP/2 spec and not blocking it; we may
see more experimentation / discussion.


#### 365: Rework Opcodes

[Rework op-codes](https://github.com/http2/http2-spec/issues/365).  

Herve reviews the options.

Martin prefers option one; he believes the second would have interesting side
effects.

Roberto is ambivalent

Mark asks for comments from other folks who implement HPACK; Nick replies that
he is also ambivalent, and he is not religiously opposed to the first.

Hasan echoed Nick’s position. At best ambivalence, with a preference not to
make changes.

Herve will not lie in the road to get this, it’s not critical--a nice to have.  

RESOLUTION: Closed with no action.




## Session 2: March 5, 2014

Scribe: Eliot Lear

### HTTP/2 Issues

####: 270 Priority leveling

Herve Ruellan: Define specific values for group weights

0 = no resource should be allocated

255 = all resources

Martin Thomson: This may be a "foot gun" (a gun to be pointed at a foot)

Will Chan: Disagrees with the use case to pause connections. Suboptimal

Mnot: keep in mind null priority (all priorities) are advisory

Roberto: Pausing is served by flow control, which flows through all
intermediaries.

Next approach: Dependency-based stream ordering (see slides)

Rob Trace: what happens when you close S1? Dependencies are expressed to levels
and not to streams themselves

Mnot: high level decision: dependency-based approach or group-based approach?
This appears more complex, but may not be.

Rob Trace: looking at it, simpler to implement.

Hasan: priorities are not necessary to get the protocol correct, but to get it
more efficient. Easier for client, a little more work on the server.

Larry Masinter: (missed it)

Rob Trace: agrees dependency on server side is more complex.

Hasan: this reflects what the clients are already doing for http/1.1. For a
server, this is additional work on the server.

Mark: as compared to grouping?

Hasan: epsilon.

Martin Thomson: not just clients- can we end up in a situation where there's a
need for garbage collection.

Barry channeling Roberto: Hasan will have access to a set of requirements I
set out, but apparently not to the list that might be interesting to discuss.

Martin: there are some differences in the transitive properties. Might be nice
to be able to simply move an intermediate node to another level in the tree.

Hasan: this is the only proposal that doesn't incent gaming, and e

Peter L: explain why proxy case is not addressed.

Hasan: you lose too much information- if you have a large number of connections
and you have a finite list of groups, you'll lose information. For perfect
fidelity we would need to do a complete dependency tree, which people don't do,
but this seems like a reasonable approach.

* need to be able to prioritize within tabs.
* need to be able to react to a page load
* need to be able to prioritize among tabs.
* need to be able to prioritize video.
* need to be able to traverse a proxy without too much loss of information.
* need to not incent cheating.
* nothing should break if prioritization is not to be respected.

mnot: we need a framework to make a decision; would like to solve this today.

Will: current experience is NOT catastrophic... there could be serious issues
here. people are trying to use finer granularity. flat priority scheme causes
some issues.

Roberto: what we have right now is terrible across proxies

Mnot: consensus that what we currently have is not acceptable

Mnot: on the table

Martin: directed graph or priority levels?

Will: levels would require gaming protection. Since we don't know how many
resources are on the page and we have this large level space, i would divide
space by two or by some factor to preserve space for resources that might
come. But as the page builds, we'd do inserts. With fixed levels, you'd have to
do heuristics to guess the right thing.

Martin: need to emphasize being careful about focusing on browsers.

Mnot: not hearing progress on the issue. Doesn't see a way to make the decision.

Hasan: Client has a whole lot more information on motives than intermediary. I
as an intermediary writer view this as a server.

Rob Trace: aggregation of connections.

???: Intermediaries may not be able to use priorities

Will: we'll experiment on SPDY.

Pat: let's pick and charge ahead

Rob: let's not block.

Coin flip: Tails was dependency approach which won

RESOLUTION: going with the dependencies.


#### 373:  HPACK vulnerabilities

EKR presented

MNOT: is there a way to add additional entropy?

Julian: we could just remove authorization header from hpack

Martin Thomson: we can't just patch this with a blacklist for a set of headers,
because we don't know how people use http headers to carry stuff, and we don't
know what needs to be protected.

Martin: consider all use cases, including those of intermediaries. in cases of
connection coalescing, need to handle mutually distrustful circumstances:

Will, Martin: MAX_CURRENT_STREAMS (?) won't address this concern.

Option 1: origin isolation.

Careful it isn't perfect unless groups (or referrer) are sent along with the
request, thanks to intermediaries.

Option 2: attach a penalty

Option 4: If you're making a request, cross origin requests don't get to
compress.

Scribe: Peter Saint-Andre

Eric: risk here is that we have to kill compression entirely, which is where
we're going in TLS

Martin: you can unilaterally decide not to use the header tag

Eric: you can use Huffman coding

Martin: or not

Roberto (from Jabber): The most important thing right now is signaling that is
durable across intermediaries about the incompressibilty of something. This
requires a single bit in the headers. And by signaling I mean signaling that
something should not be compressed.

Pat: Maybe all we need an informational document or security considerations

Mark: The emerging approach I see is to add a bit indicating that a given
header is not compressible, define security considerations around that.

Eric: That seems like the best we can do.

Roberto (from Jabber): A single bit in the headers is more efficient. You don't
want to compress *any* of that data for a CORS request against one that isn't.

RESOLUTION: agreed to have a single bit in the header format indicating that it can't be compressed, and add Security Considerations about this attack, with potential options.


#### 416: Default max stream limit should be finite for security reasons

As per discussion on #373, closing 416 with wontfix.

#### 363: TLS renegotiation

Mark: what do we want to do here?

Martin: We had a discussion about this in TLS WG yesterday but it did not
conclude, but I think we can probably say no here. Might be better to look
outside TLS for this feature. Would need some kind of signal that you need to
go off and do this. There are so many issues here that I do't think we can
recommend TLS renegotiation.

Eric: Yes that would work. (1) we don't care about use case (2) we demand that
TLS solve it (3) we define an HTTP mechanism

Mark: interesting to think about how we'd layer in an HTTP mechanism

Eric: I think need to decide now which approach we're going to take

Mark: we could define an HTTP status code later

Martin: I'd like to see it as an HTTP status code. We do need to decide what
path to take. Write down the options and put it to the mailing list to start
some discussion.

Mark: my sense of the room is that we don't want to do TLS negotiation, and
find a group of interested folks to come up with a proposal.

Will: I don't like TLS renegotiation, but I'm thinking through the
implications. For example possible CDN cases. Are we setting ourselves up for
failure here? We do get bug reports about client certificates.

Eric: Even a better approach might have interop issues (not supported). I don't
think CDNs and such are target use cases here.

Mark: Not trying to develop a solution today, only figure out direction and I
think we have rough agreement that it's not TLS renegotiation.

[end of topic]

#### 315: HTTP URIs over TLS

https://github.com/http2/http2-spec/issues/315

Pat: should we be extending current usage or define something better?

Mark: before we get to WGLC we'll consider this.

Eric: my sense is that Chrome experimented with this and had good results.

Will: In our experience this doesn't break anything.

Stephen Farrell: I would encourage improvements over what we do now, this is a
way to get a good security win.

Mark: May be best to have a discussion about alt-svc overall.



#### 359: Collection coalescing

https://github.com/http2/http2-spec/issues/359

Martin: I think this is closed but we were waiting for feedback.

[end of topic]

#### 349: Load Assymetry

http://datatracker.ietf.org/doc/draft-nottingham-httpbis-alt-svc/

Mark: Do we want to put this in the main HTTP2 stack?

Martin: there are a number of things here that I consider optional, but in
general this seems to be what we need to do. I like Patrick's characterization
of this being CNAME in the HTTP world.

Mark: for high-level features I'm not hearing any major pushback

Martin: at the moment this is informational and I'd like to retain that

Mark: the load-shifting use case is important here, and ALTSVC frame is
designed to address that.

Martin: this is goaway and then come back - is ALTSVC good enough?

Mark: layering matters here, need to be careful

Rob: mandatory to implement?

Mark: not really, different scenarios

Rob: would not want to hold up the spec

Mark: agreed

Pat: not a lot of point in making it MUST

Will: I think this has to be advisory

Mark: request to shift and use that alternate service when viable, so it's not
a true goaway code

Rick: I'd like to see another field for extensibility about security features
(e.g., TLS 1.3)

Pat: the CNAME model is really good, so are routes in a routing table

Rob: major case here for load balancing - does this work better as a separate
draft to open up extensibility?

Mark: need to have some proportion of clients to support this for it to be at
all useful

Rob: as long as it's not a MUST and as long as we're not going to hold up
progress on the core spec

RESOLUTION: agreed to using ALTSVC frame for this.



##### SETTINGS_UNIVERSAL_SCHEMES

Will: this will take an RTT

Martin: I find this to be a bit weird - just send and react appropriately if it
fails, why not use NOT_AUTHORITATIVE instead?

Mark: do we want to define something here? seems so

##### Alt-Svc HTTP Header Field

Mark: same host, can't switch for security reasons

Julian: framework and header in separate document, then the frame in core?

Mark: we can talk about document organization later

Martin: if we're doing the frame, we're doing the header

#### Discovery of TLS Support for http:// URIs

Mark: cover this in our draft?

Martin: I think it's hard to avoid having this feature once we support the
other parts of this proposal

Will: why?

Martin: people will do it anyway

Will: it would just be undefined

Mark: just talking about documenting the pattern

Will: I'd rather not make a decision right now

Mark: does anyone think that's a bad idea?

RESOLUTION: support for documenting this, but not requiring it.
