# Minutes of the June 2013 HTTPbis Interim Meeting

* Agenda: https://github.com/http2/wg_materials/blob/master/interim-13-06/agenda.md
* Current draft: http://tools.ietf.org/html/draft-ietf-httpbis-http2-03
* Issues list: https://github.com/http2/http2-spec/issues?milestone=&page=1&state=open

Chair: Mark Nottingham 

Participants:
* Jeff Pinner (Twitter)
* Michael Schore (Twitter)
* Martin Thomson (Microsoft)
* William Chan (Google)
* Roberto Peon (Google)
* Gabriel Montenegro (Microsoft)
* Stephen Ludin (Akamai)
* Shakesh Jain (Akamai)
* Herve Ruellan (Canon)
* Leif Hedstrom (Apple)
* James Snell (IBM)
* Mike Belshe (Twist)
* Brian Raymor (Microsoft)
* Allison Mankin (Verisign)
* Ben Niven-Jenkins (Velocix)
* Grant Watson (Velocix)
* Kalyani Bogineni (Verizon)
* Barry Leiba (IESG)
* David Morris (XPASC)
* Hasan Khalil (Google)
* Josh Aas (Mozilla)
* Fred Akalin (Google)
* Ryan Hamilton (Google)
* Vikas Panwar (Yahoo!)
* Emile Stephan (Orange)
* Rob Trace (Microsoft)
* Ilya Grigorik (Google)
* Chandra Yeleswarapu (Verizon)
* Dan Sun (Verizon)
* Brian Libonate (Verizon)
* Ted Hardie (Google)
* Dan Wing (Cisco)
* Aruna Balasubramanian (University of Washington)
* William Chow (Mobolize)

## Thursday

### Administrivia 

Mark Nottingham welcomed the group and kicked off the introductions.

Mark discussed the agenda, noting that the base approach is going through the
open issues, with the proviso that anything that the group felt was not likely
to need attention might be deferred. Questions about whether controversial
issues (e.g. compression) should be brought forward; confirmation that
compression would be dealt with. Alison Mankin asked about the transport area
coordination and how to raise issues; Mark replied that raising them on the
list or in the issues tracker were both appropriate.

Mark then displayed the Note Well, reminding folks of the IETF IPR rules. He
then went into other ground rules for the meeting. This is an interim meeting;
we can make decisions in the room, but then they need to be checked on the
list. We don’t want to rule people out, though; here we give editors direction,
take the decisions to the list. We plan to develop an implementations draft in
the very near future. Mark notes that he hoped we’d be a little bit further
along at this point, and he feels that we have to a draft suitable for
implementation in the very near future. We may be doing the interoperability
testing work in the Hamburg meeting time frame.

### HTTP/2 Draft Review

Martin then started to talk about the draft. Things of note: the terminology
has shifted from session to connection; we moved from talking about NPN to
ALPN. The header and priority work have been added; the priority frame is not
in the -03, but is in the working copy. Header continuation is in the published
draft. Dave Morris mentioned that there were ease of implementation issues that
needed some clean up; Martin agreed and suggested that they get rolled up into
a session. Mark has editorial feedback, but none of it affects the wire
protocol. Martin notes that for editorial stuff, a pull request on github and
request for change is easy. Mark is happy at this point to give editors
largesse, but when it is much more baked; then changes will need scrutiny by
the working group. Now is about velocity, not details-level changes.

### HTTP/2 Issues

#### Upgrade Mechanism

The first issue is the upgrade mechanism. A basic upgrade mechanism is in
place; https uses ALPN and http the Upgrade mechanism. Do we need a DNS
mechanism? Mark’s question--what are we going to test in our first round of
interop testing? ALPN is defined, but is it widely implemented? (No ALPN in
python, for example). Will asks about open SSL--there’s a patch, but it hasn’t
made the made the main branch yet. The simplest thing to test is a direct test
(no upgrade); do we want to test the upgrade dance? Do we want to deploy the
DNS record for texting? Question about the magic byte sequence; magic string
over SSL seems to work well for twitters clean. That is good enough to initiate
an HTTP2.0 connection. That seems to work. Mark asks if we need to try the
upgrade dance? It seems to have an enterprise use case, so there are folks who
want this. It’s easy enough, so it is in. How about DNS? Not clear that we’re
ready for that. Eliot’s not here, but Dan notes that folks don’t yet see what
problem that solves. There are problems it could solve (e.g. HTTP over UDP
deployment); it optimizes out some things that the server doesn’t support. It
may not solve a current problem, but it avoids later happy eyeballs-style
multiple stream attempts. If testing the DNS, what do we test? Eliot’s record
is a new record type, or could use TXT. There is also an experimental range,
but it runs the risk of support issues in the current DNS infrastructure. Ted
notes that this leads you down the TXT forever mode. Will Chan channeled
Patrick McManus saying that it might help avoid an upgrade dance and reliance
on ALPN. Gabriel noted that there is also work on web discovery and wondered if
things like web finger might be applicable. Maybe this could be included there?
Mark says he is hearing some interest in DNS or other discovery mechanisms, but
not hearing certainty about it. Gabriel says that it is a hint, but you still
have to test the path--it can’t be relied upon until the connection path
confirms. Roberto notes that it is a hint and not required to make the protocol
go; it has a lower priority. (Engineering resource prioritization, not
functional issue). Mark suggests we put the DNS hint on the side and revisit
the issue in Hamburg. Don’t want to leave it too long, as DNS deployment may
take some time, but the 2-3 months til Hamburg should be okay. Will said there
is some interest from Google, but it is only some.

#### Advertising Settings During Negotiation

Next issue is about getting the setting on initial upgrade dance (sending
SETTINGS frame content as part of the Upgrade Get). Jeff asks whether it is in
instead of the 1.1 header and whether it should send another SETTINGS frame
post-Upgrade? Mark suggests that it should be both, since there is some
potential for implementations that don’t get the first data. Jeff says he is
fine with “in addition”, but not “instead”. Question about whether they need to
be the same? Sense of the room was that they did not need to be the same, but
that some syntax was needed to allow for both to be understand. Action to
Gabriel Montenegro to make a proposal for text to resolve Issue 51 along these
lines. Mark asks whether this goes into the first round of interop testing?
Proposal that if this is being tested as part of the Upgrade dance, someone
testing that should implement that. After discussion, agreed that if this
header is agreed to, it will be a MUST implement. Roberto highlighted that it
should be in early implementations or early testing (without it) might give bad
results. Alison, Gabriel, and Roberto discussed how “complete” this needed to
be; Alison was saying that this initialization data was likely to alleviate
some of the transport worries. Others raised concerns that it can’t be held
until all the transport issues were resolved, or there were going to be delays.
First draft needed for the next iteration of testing, with understanding that
the spec is still in flight, so it might change.

#### Pre-Upgrade Requests

Martin will incorporate stream ID 1, priority 0 as defaults. No resolution of
the status of the stream; half-closed from the sender side is the current
proposal. Roberto prefers it not be half-closed; Jeff prefers that it match the
http semantics for POST (without a body it is final, with a body it is not).
Mark suggest that a client not send “change protocols” until you complete a
message (no changing while a message is in flight). This means if you are
“POST”ing as the first message, you will have trouble with the upgrade. Martin
is not sure that he sees Roberto’s problem, but agrees that you won’t be able
to interleave requests. Gabriel notes that for a lot of this, there will be no
upgrade.

Resolution: HTTP/1.1 request must be complete before clients starts sending
HTTP/2. This will block further requests on the connection until the upgrade is
effective.

#### Magic Syntax

The desiderata are “small as possible, multiple of 4 bytes”. Probably don’t
want to prefix an existing method name. STA and RT? Besides the color of the
bikeshed, is everyone happy? Apparently, folks are. Martin notes that this can
also be changed in later drafts, but empirically the first looking like HTTP
1.1 and the second not is a key bit.

Mark then asks whether the token that reflects the HTTP profile to appear in
the magic string? No, that’s the job of the SETTINGS frame.

#### Registry of Opaque Strings

Eliot Lear was given an AI in Tokyo to propose text for a registry of tokens
that could be used to identify things to upgrade to. Alison Mankin asks if
these will be recognized by TLS? A general registry.

#### Cross-Protocol Attacks

When you upgrade a protocol in the clear, there are some intermediaries that do
not recognize the upgrade and continue to believe that the previous version is
in play. If an attacker can control both ends, it may be possible to cache
poison or otherwise influence the intermediaries.
(http://w2spconf.com/2011/papers/websocket.pdf) Gabriel notes that no
handshaken version considered by websockets ever actually saw a version
vulnerable to this attack; he suggests it would be over-reacting to the
proposed attack. Martin notes that there are protections in the handshake that
limit this; he’d suggest that it belongs in a Security Considerations section,
but not require a protocol change. Roberto notes that this is actually an
HTTP1.1 attack, not an HTTP2.0 attack. Suggest this will get shifted to the
1.1bis work. 

Action item to Mark Nottingham to check this against HTTPbis.


Question on whether anyone is planning on implementing Upgrade?  Is everyone planning on using ALPN?  No on in the room said yes.  Jeff notes that they will reserve the right to do so, but only for redirects.  Mozilla will not.  Microsoft Open Tech plans to.  Jeff reinforced that we need to have it done in the spec as it may become important once large-scale deployment begins.  Mark notes that we’ve always known that specific implementations may only use specific upgrade methods (e.g. over TLS).

#### Frame Layout - Reserved Bit

We have this bit with no semantics. Mark is suggested we leave this in, not
defined. Martin notes that there are a couple of other reserved bits.
Resolution is to retain this as-is. Alison asks what the considerations were
for roll-over? Jeff notes that this is fine for them--they roll over by sending
a go-away frame, drain gracefully, and it starts up gracefully. Jeff notes that
shifting to a 32 bit frame will not change things enough to matter.


#### Frame Semantics - Opaque Data in RST_STREAM and GOAWAY

Hasan noted that for debug-ability that throwing opaque data in RST_STREAM and
GOAWAY, with the stipulation that any data should be completely opaque--neither
end should act on that data. No media type, no language, no content-type, no
string encoding. Roberto has a slightly different focus--the most important
thing is that the browser does not interpret the data (no dialog to the user,
e.g.). Martin could stipulate that it be UTF-8; it could be binary. What size
limit? Length for a frame size is a reasonable limit. Easy to ignore. Jeff is
more comfortable with GOAWAY than RST_STREAM. Doe we want a frame specific
flage that could be used to indicate additional data. Roberto says he feels
that this is reasonable; Hasan says that he doesn’t seem that it is necessary.
James said that a non-buggy implementation doesn’t need this. Roberto asks if
the flag is “please log”. Mike asks what happens if we don’t do this? There was
discussion on what use cases were appropriate for use of this. Mike asked if it
was a Google special, for the use of companies that controlled both client and
server. Hasan said that it might be useful for Twitter or others for user
bringing the data back to the customer support take. Other similar things are
in HTTP now (Akamai and twitter use similar techniques now). Mark says that
RST_STREAMS are very common, so there could be lots of data, so this could get
to be a big log. Hasan notes that it doesn’t have to be logged; it could be
dropped on the floor. Will describes how the about:net-internals does this now.

Mark asks whether anyone is against this? Mike notes that he prefers the spec
to be as clean as possible, and this is not that valuable, but he’s willing to
let it go. A speaker asks about the unlimited amount of data. Others are also
concerned about this issue. Question about whether the client could indicate to
a server that it will not be saving the data--this would incent the servers not
to send it. Mark notes that he has no particular concern about that, but we now
have a large number of configurable pieces to this protocol. Mike asks for a
concrete statement of what a browser should do with this data. What would the
specification say? “May log to disk” seems to be the answer. Mark suggests we
put this in now and mark it as “at risk”; it may then get taking out later.
David Morris says that he bets it won’t come out. It’s very useful for
debugging. Putting it in the GOAWAY but not RST_STREAM is being proposed by
Jeff; otherwise we have a large thing going into the middle of the stream.
Alison asks if the stream id is enough, or you need a nonce. Plenty of data to
correlate with at this point. Will Chan notes that this can be problematic when
you have a backend working through a reverse proxy. Jeff continues to feel
uncomfortable about RST_STREAM.

Action Item:  Hasan Khalil will provide text to Martin for a opaque data on both GOAWAY and RST_STREAM, but both will be marked as at risk.  

#### Stream ID in GOAWAY

Text has been added about this.  Jeff asks whether the sending of GOAWAY is marked SHOULD.  

Action Item to Martin: to clarify RFC 2119 status for the sending of GOAWAY.


#### Ping Payload

This again is a debugging issue; you may need to send data to get an actual
latency measure. Jeff has the same issue with PING with RST_FRAME opaque data;
it is an arbitrarily large amount of data in the middle of the stream. There is
no flow control for PING at the moment; Hasan notes that Google saw it as DOS
vector. They limit PING to two outstanding or two data frames. Jeff notes that
Twitter uses it for liveness on switching networks. Hasan notes that they send
it before and after a request, to test for liveness. David Morris says that it
doesn’t need to be unbounded; lower than a frame size, but not empty (e.g. a
timestamp). Mike notes that he’s not sure about sending ping packets. Roberto
notes thats keepalive is a must have, but ping is a nice to have. There is some
utility. If it is a keepalive, do we need a response (ping/pong). Martin notes
that it could be a “possible PONG”, which keeps the nat binding. 

Resolution: fix PING at 8 bytes.


#### The FINAL Flag

Jeff reviews the issues. He knows we want to describe a frame layer for HTTP2.0
that is much simper, with some of the semantics moved up a layer. Mark has
sympathy in refactoring the spec. Martin has come to a similar conclusion. Mark
agrees that it should be on the path, but asks whether it is critical to the
draft at this time. Jeff believes that is critical for an implementation draft,
as they had difficulty implementing the spec as is. Jeff has a bullet point
list for things to be done and he (and James) would volunteer to help. Martin’s
[preso on the
structure](https://skydrive.live.com/redir?resid=B3CBDA49A25BB9DC!722&authkey=!A
GlyRpsh7_9 vR0o) was then presented.

Many legos were consumed in bringing us this information. Discussion of how to
break up the spec in layers based on the deck and work done by Jeff and James.
The group sent a task force for the -04 draft (or at least before the next
meeting). This is largely conceptual, but there are some concrete layer
changings that need to happen. Gabriel also notes that the group had a “nice to
have” requirement for websocket compatibility that would likely get easier.
Before the group assignment, the group discussed who the stream initiation
worked; it’s not as clear cut as a negotiated system would imply, because the
streams aren’t negotiated (as that is too slow). In addition, pushing can cause
stream to appear out of order. After reviewing the state machine and stream
mechanics, Martin proposed limiting streams AND processing. The stream limit
imposed by receiver only applies to stream that the sender is responsible for
creating; the conjugate stream is not counted by default. At the HTTP layer,
force the client to limit requests. Martin, does that make sense? Jeff says
that what he’s thinking of is simpler than this, but along the same lines. Jeff
thinks that the stream lifecycle is a bit simpler, though push_promise does not
fit the model well, since the Push_Promise doesn’t count against the limit (but
the open stream does, even though it starts as half-closed). Roberto says that
it sounds good to him, and he can carve out time if needed.

Will asks for further disambiguation between HTTP layer requests and
stream-level accounting at the framing layer. He poses a hypothetical: the
client sends a 100 requests; if there is a limit on open streams, can it send
additional request immediately does it have to wait? It has to wait until it
gets at least one response. Essentially at the framing layer, there is nothing
special about frames initiated by the Server; at the HTTP semantic layer, there
is a limitation that says servers do not initiate streams until a push_promise
has been sent. The next issue in Martin’s deck was whether a specific set of
messages opened a stream or whether sending any message opened a stream. HTTP
would require HEADERS or HEADERS+PRIORITY, but not a limitation at the
streaming/framing layer. During the discussion, there was a proposal that the
frame structure could change to use a flag for priorities so that it was a
“HEADERS” only that opened a stream. Martin then presented an issue related to
early arrival of RST_STREAM. If a RST_STREAM is received for a stream that has
not arrived, it is an error; but what happens when this is in the stream layer
because of PUSH_PROMISE? The group did a dive into the resource
allocation/state management discussion. A question about how this works in an
intermediary came up about how to manage the outstanding number of streams
allocated and there was a quick answer that there were two sides to the
intermediaries interaction with the limit--one to the upstream, and one to the
downstream; this was then deferred to later discussion of PUSH. Martin then
brought up the WINDOW_UPDATE issue (#104). Base issues is that data is flow
controlled, but headers are not flow controled. Can we flow control header
frames? Roberto says that he would prefer to fill up the TCP socket with
metadata rather than data, since he can then react to data on what is coming
up. Jeff is asking whether we flow control frames on the streams (you can’t
flow control the frame types *about the streams* as they impact the stream
lifecycle).

Mark notes that some of these issues are editorial, but many of the are more
than editorial. We need a task force for this.

Action Item to the layering task force: Jeff, Martin, Roberto, Hasan, James,
Herve, Mike Belshe to come back with a pretty baked proposal in the next couple
of weeks. They suggestion is to use Martin’s slide deck as a potential guide
for what has to happen.

#### Frame Extensibility

Martin and Jeff discussed extensibility. Jeff notes that if we truly believe
that we can version quickly, then we get the appropriate agreements on what
frame types mean. Otherwise, the dropping of unknown frame types may get
unexpected comments. But naming frame types (on a stream, about a stream, etc.)
may make things easier as that will set expectation on what characteristics it
has.

Will noted that there were not browser folks on the task force and asked if there were a possibility to add one.  Discussion moved offline.

#### SETTINGS Persistence

The group then discussed SETTING persistence. Roberto gave a DOS-based use
case. Mike asks for more detail. There are some good guys in the midst of bad
guys; he wants to limit the number of streams (e.g. 10 instead of a 100). If
someone does not obey that request, he treats them as a bad guy and drops them.
Will asks if there are other motivating reasons than DOS? There are other small
motivations, but this is the big one. He suggests that we raise the issue and
see if there are other approaches (e.g. ALPN). Herve askes how long is this
expected to last? Not well specified, close the browser. James suggests that it
would be possible to include differential data in “GOAWAY” that says use the
current settings; that allows you to send a settings frame updating the limit,
then send the GOAWAY. Roberto says that would work, but ALPN choice would be
better. A speaker from Akamai notes that persisting settings, like other ways
of learning about the server, seems like an optimization that’s currently in
line with how we’re going. Roberto says his big issue is simply the DOS attack
and continuing discussion on how to resolve that is a fine. Mark suggests that
the go-away flag here is simply a way to get the restart with new settings and
doesn’t have the baggage of “settings persistence”. A question about whether
there were general use cases where a specific server would like to keep this in
all situations, not just under dos. Mark says that this is part of the
discussion on how many tunable knobs this has. Mike Belshe noted that this also
contributes to possibility of more browser fingerprinting; he likes James’s
proposal better. Mike is sure that this tool may help, but there may be other
tools that do as well we fewer privacy implications.

Mark: returning to the questions: keep settings persistence? James’s proposal?
addressing with ALPN/TLS handshake? sending settings in a HTTP header? do
nothing here?

Does anyone object to taking settings persistence out? who wants to pursue
james proposal 5 or so; alpn 10 or so. who wants to do nothing? AI: action to
James to make a proposal for Go-Away flag. AI to Gabriel for ALPN.

#### Discovering Maximum Frame Size

Maximum frame size. The people asking for further constraints are usually
embedded. Roberto points out that maximum frame size has nothing to do with
resource consumption on any platform. Streaming of data works regardless of
frame size with the same amount of resources. James submits that we not specify
any frame size limits in the specification, beyond limits based on frame length
field.

Should maximum frame size be negotiable? Nobody says yes.

Should frame size differ from current 16bit length? Several hands raised,
indicating that the frame size should be lowered. Motivation here is stated as
preventing poor implementations. Patrick has observed, in the wild, servers
that send response bodies entirely in a single DATA frame, which is clearly
sub-optimal.

Proposal: Fixed 14bit maximum frame size packed in zero-padded 16bit frame
length field. Passed.

Should the Layering Task Force have a timeline? Mark: If we don’t have
something from them within two weeks, I’m going to be very upset.

#### Header Compression

Roberto and Herve have worked jointly on a draft:
draft-ruellan-http-header-compression-00. Plan today is to talk through the
joint draft and see how we feel about it. James has put in some work as well,
but we’re going to push on that for now. If we can’t make a decision at this
meeting about header compression, Mark’s inclination is to get a first draft
out without header compression if necessary, in order to avoid blocking on it.

Basic overview: header table, Delta2 diff encoding, HeaderDiff wire syntax. The
header table mapss name/value pairs to indices. It’s limited in size (default
of 4096B). It uses LRW for eviction. Diff encoding uses the previous header set
as a reference. Wire syntax uses either indexed representation or literal
representation (either not indexed/persisted, indexed as new value, or indexed
as a replacement for an existing entry). There’s an ACK for table size
reduction instructions, which is done using HEADER on stream 0.

Question on whether it’s useful to be able to reduce the table size. Roberto:
absolutely yes, as most of the time we’re going to want large tables, but
certain circumstances may force us to clamp down on that. Also, the reduction
step is only necessary for reducing the receive header table, as on the send
side the reduction is trivial with no additional semantics/frames.

Roberto: Coding complexity of table size reduction is low. There’s a single
buffer into which you put your key/value pairs. When you’ve run out of size,
you’ll need to use LRW to remove key/value pairs. In the event of a table size
reduction, this same logic applies. The logic must be implemented anyway; table
size reduction just provides one more entry point to it. James: This seems like
an abuse of HEADERS. If we have to have an ACK, let’s do it with SETTINGS. An
ACK frame type might be the better way to go, which could apply to SETTINGS
among other things.

Herve: Things missing from the current proposal include huffman coding and
typed encoding. James: The typed encoding that I’m working on should work
across codecs. Also, regarding Huffman coding, we need to think about utf8
handling. Martin: The way that Roberto did it indexed on byte, not character,
so we’re safe. Mark: Technically, HTTP headers are byte streams. Roberto: As
long as we’re byte-aligned, byte-based Huffman coding will work fine. Roberto
considers the introduction of a flag for literals indicating whether or not
Huffman coding is used.

Decision on Huffman coding: we’ll address it when we address typed encoding.

Leif: Is it possible to share compression contexts across several connections,
at the server? Collective answer: not really. On the send side, maybe, but it
would be suboptimal at best. Roberto: the security implications are dangerous.

James: Is it possible to drop the differential encoding and just use the
reference set as a set of literals to reference when necessary? Roberto: We’ve
discussed this already. The compression efficiency gain once differential
encoding is used is very substantial. James is sufficiently convinced that it’s
a useful feature, just worried about complexity and getting it right.

Is the initial set worthwhile? We should find out by way of experimentation.

The current compression draft, draft-ruellan-http-header-compression-00, will be used in the initial implementation draft and is hereby adopted by the group. It will require some editing but nothing major. Huffman encoding is not included for now.

#### Cacheability of Server Push

Mark: We need a security model for this. Martin: There’s some text in the draft for this. Mark: How does the browser do a good job caching without all synthesized request headers? Roberto: We should include all of the headers for the synthesized request in the PUSH_PROMISE. James: The current spec states that all headers are copied from the original request to synthesized requests, excepting host, scheme and path.

Action item on Mark to talk to Martin about caching, push, and security.

#### No-Push Default

On turning push off by default, we’re punting. Will obtain implementation experience first.

#### PUSH_PROMISE Stream Priority

On PUSH_PROMISE stream priority, this devolves into the same case as HEADERS versus HEADERS+PRIORITY. To be addressed by the Layer Task Force. The difference with PUSH_PROMISE is that there’s no race.

#### Prioritisation

On prioritization in general, there needs to be a default priority. Suggested outcome: if the priority is not otherwise specified by the server for push, it is assumed to be one lower than the priority of the associated request. This will not be discussed with the Task Force and is otherwise ready for the editors.


Will asks which clients actually care about this. Use case is as follows: client visits a page including tons of pushed resources. Client viewport changes, causing resources visible within that viewport to be of higher priority. Client sends PRIORITY frames for those resources to bump up the priority.


Leif asks about how PUSH_PROMISE is handled by intermediaries. Roberto: It’s up to you entirely. Lots of talk about push and how it relates to session lifetime. To be discussed by the Task Force.


Lots of discussion about trailers. General consensus is that HEADERS after DATA are permissible to discard. Open for later discussion. James wants to do checksumming over the course of the stream of DATA frames rather than a streaming single checksum confirmed at the end.  HTTP semantics for HTTP2 will not include handling of HEADERS between DATA.


The group broke to allow the Layering TF to work for a period of time at the end of the day.


### Friday

The group resumed 9:25 on June 14.

#### Layering TF Initial Report

Martin outlined the layering the Task Force had discussed/agreed/proposed.

TF have defined state machine for stream creation/destruction.

PUSH_PROMISE puts stream into HalfClosed state straight away

If stream is HC or Closed then it counts towards MAX_STREAM limit, but if
PUSH_PROMISED is just Reserved (not seen HEADERS for pushed resource yet) that
does not count towards MAX_STREAMS

Martin went over Request/Response for Client, Server initiated streams &
PushPromise. Talked about how the TF had separated frames "on a stream" vs
frames "about a stream". Proxy MUST maintain frame order within a stream.

Mark - HTTP/1.1 doesn't describe how proxy operates in any detail. Question if
that is good thing or not, could argue it is a good thing.

David Morris - Would like to have a stream initiator also send PUSH_PROMISE for
a stream it has initiated - use case is avoid multipart MIME POSTs so instead
can say "this POST is associated with this other previous POST".

(Some discussion on this & ordering requirements for PUSH_PROMISE)

James - need PUSH_PROMISE delivered before stream creation/headers

Ted - Concern is PUSH_PROMISE frame is an about frame with no ordering
guarantee.

Martin - Only guarantee is frames on a stream are ordered relative to each
other. frames on different streams are not necessarily ordered relative to each
other.

ReqHeaders on PUSH_PROMISE is about stream one but HEADERs is about stream 2 so
no ordering guarantee and HEADERS could arrive before RequestHeaders!

Jeff - PUSH_PROMISE are not end to end, nothing to stop intermediary not
passing it on.

Martin - Could put PUSH_PROMISE on PROMISED stream. Problem that introduces is
that it forces a transition into HalfClosed state and the stream is open now
and counting towards MAX_STREAMS.

Jeff - Be careful because what we're saying is we need ordering at HTTP layer
so we're playing around with the frame layer and we should't do that.

Ted - PUSH_PROMISE have two characteristics: 1 is about & 1 is "on" the stream.
That creates a new classification but gets the result you want. Jeff is right
avoid the layering violation but problem is it is not HTTP frame semantics.

Jeff - already have restriction in framing layer as once sent HEADERS have to
be in order because of the compression context.

James - What happens at next hop?

Roberto - Doesn't matter as intermediary is not forced to emit PUSH_PROMISE

Ted - If it drops yes, but unless you have dual nature ….

Jeff - Are you concerned non-HTTP intermediary

Ted - Just a frmaing intermediary.

Roberto -= In that case as currently define there could be an ordering problem.
Assuming intermediary is HTTP intermediary right now. If start layering other
non-HTTP on top it is a problem.

Roberto - Would be nice to have framing intermediary and can do that with small
change.

Martin - Let's work out details on the list

Mark - layering i useful for implementation & writing spec but we've gone to
such immense lengths to do and so convoluted with PUSH_PROMISE etc I'm
skeptical if we can make it truly layered, but great as editorial convenience.
In terms of having this magically frameing layer only intermediary that would
be nice but I'm not convinced it's possible yet.

David - missed what he said

Jeff - intermediary can order frames onto wire.

David - doesn't work until have guaranteed ordering on PUSH_PROMISE>

James - best we can do right now is ….

Mark - On/About split. Editorially should use different terms as on/about is a
little loose.

Martin - Will do something in next 2 weeks, if don't get that will still get a
-04 but might have some gaps.

Action Item: James & Jeff will sit together and get frame definition written up/finished.

James - already have pull request for PING frame and will do HEADERS later
today.

(discussion on sending PUSH_PROMISE before HEADERS on associated stream)

Mike - There has always been the race between a server PUSH_PROMISING a
resource and the client issuing a GET for it anyway. If you're a server and
decide to PUSH then you take on risk you might have to use double resource to
send PUSH and respond to GET for same resource/representation.

Mark - Is re-spinning achievable in next 2 weeks.

Martin - Something is achievable but might not be everything

Mark - I'd like the spec to be in a state where folks can start implementing in
2 weeks.

Jeff - Mike/I was looking at this and reckon we can have a working server on
Tuesday.

James - Can easily get written up in implementable way.

Martin - we need to recognise we're sending stuff without knowing it is needed,
e.g. PUSH_PROMISE just need to accept that and make appropriate tradeoff in
implementation.

#### Prioritisation (Continued)

Issue 7

Will - this is done.

James - why 31 bit issue

Will - that is a separate issue

james - but why so big

Will - changed in tokyo because …

Roberto - when experimenting original level of priorities wasn't big enough

Mark - general thing is need space to experiment so we made it large, might 
make it smaller based on experience.

Mark - Prioritisation itself is still Work In Progress

#### Priority 

Mark - This is closed already.


Mark - Anything else to dices or we need implementation experience before we
can do more

Will - Jeff is on board with SPDY prioritisation (relative ordering based on
streams) but do not have data.

Jeff - have enough room in spec to do it, all defaulted text fits in with it
e.g. zero is highest priority, etc. There is everything there to experiment
without changing the draft

Mark - Need more time for experimentation.

Mike - What didn't come out in Tokyo is there is a starvation problem.

Will - we discussed on mailing list

Jeff - If re-prioritise don't get starvation

#### Trailers

Martin - already have text saying ….

Jeff - that was in SPDY2 stuff

James - so if it shows up we ignore it?

Mark - Issue here is in HTTP/1.1 you cvan declare list of headers that will
appear in headers

Jeff - Should is not a requirement, only requirement is cannot include
Content-Length etc

Mark - Little more subtle than that unfortunately

Mark - I need to dig into this, if it's no longer an issue I'll go and close it

Jeff - weird one about TE is TE is end-to-end anyway. Is hop by hop header but
if want it have to propagate it end to end.

#### Handling Expect/continue

Mark - I need to do the same thing here. From discussion general approach should be to write how intermediary should handle expect/continue

#### Indicating the End of a Header Block

Mark - covered by what discussed yesterday

James - Can still have headers that exist at stream layer but don't propagate
to HTTP layer

Mark - How left it was 1:many header blocks & 0:many data blocks (in case there
is a body) and cannot have HEADER blocks (that get propagated to HTTP)
interspersed in Data blocks. Then any Header blocks after data blocks get
propagated as Trailers and cannot send any more Data blocks after that.

mark - Semantics of Trailers being what they are means an implementation could
just drop on floor & not forward.

(some discussion on how to tell a HEADERS frame is Trailers and not
interspersed with DATA)

Roberto - Would need to set FIN on last HEADERS frame.

Jeff - can we just kill Trailers

Mark - People in room may not use, but people in wild are e.g. for signatures.
So not comfortable with killing them

Hassan - boils down to boundary between what we do for HTTP & what we do for
framing layer for others things. I'm of opinion we're doing HTTP here, if
people want to do crazy API crap they can figure out how to do that themselves.

Mark - but we are killing a feature available in HTTP.

Jeff - HTTP says it can be dropped so if intermediary is HTTP then I would say
that is one of the cases you can drop.

Jeff - If we're dropped chunked encoding then we've already dropped Trailers as
they only apply to chunked encoding.

David - ALso enables you to not know the content length before sending the data.

Roberto - chunk extension & Trailers, how someone speaks HTTP1.1 is your
business. All were saying is if you send what ??? is proposing if receive
HTTP/1.1 with Trailers we're not going to forward them.

Mark - If we spec that we should expect a level of pushback Roberto - let's do
it & if pushback is hard enough we can put it in.

hassan - I think we should also specify that people should just drop on floor,
if that's going to be de facto anyway and folks writing spec agree it's a silly
thing to have so let's just say that

Mark - had discussion on trailers yesterday & now we're getting rid of them.

Stephen - would like ability to send metadata on object/stream after it has
started. James - can still send HEADERS frame at streaming layer it just has no
HTTP semantic.

Mark - This is making me very uncomfortable as we're talking about lots of info
that is not surfaced to the HTTP layer

Hassan - what is quite doable is saying this is not part of HTTP semantic. At
framing layer don't say what is allowed or not.

Roberto - interesting problem as charted to do stuff at HTTP semantic layer and
is something at that layer now. We're saying we can support these semantics
just not at HTTP layer

Mark - that divergence is what concerns me

Jeff - can describe a mapping and can surface extra header content that is
arbitrary but we'll not map to message response same as PUSH_PROMISE doesn't
map. That means when parodying 1.1 to 2 Trailers get dropped. When speaking
HTTP2 end to end might get some HEADERS frames along the way

Mark - I would be much more conformable…sound sleek you want chunk extensions
so why not find a way to map into chunk extensions

Roberto - it is keepalive, chunked/Trailers were interesting but not useful
enough for widespread use. If we do it should be required part of spec/API and
that way has a good chance of being useful

Mark - but requiring a new API outside of what HTTP is

Roberto - yes

Jeff - HTTP connection: keepalive is the same.

Mark - As WG chair we are chartered berry explicitly

Martin - maybe discuss independently of each other, removal of trailers &
removal of support of trailers.

David - worries me on deployment

Roberto - my experience of trailers on internet is they don't work even if you
send them as the feature is broken.

hassan - tell your customers, hi, it's a crappy feature you can't use, new
version doesn't even use that crappy feature

David - in my case it's working and you're breaking that so I can't use your
product. You will probably have this surface after you've tried to sell it to
me.

Roberto - I have no implementation experience for this

Stephen - use in limited extent to closed clients and not seen any big issues
but always treated is an optimisation for hashing not required.

James - for all my cases having it at streaming layer is fine don't need to
surface to HTTP latter

Mark - Don't hear any technical arguments to not have it in spec but I'm
hearing people say don't put it in spec because we know better. had same
discussion in httpbis and although we've deprecated things didn't do that for
Trailers so why should this groups do that

Roberto - as chair are we required to have this as part of charter

Mark - don't know

martin - Would be up to WG

Mark - Could take a question to mailing list to ask if folks OK to drop

Roberto - you said chance extensions are residual

Mark - yes did that in 1.1 as no interop

Hassan - so we're exercising our discretion to drop that as it doesn't work

Roberto - question about trailers - is it the same situation

Mark - Impression of room - there are people who be happy if they went away but
folks won't "lie down in the road" to kill them, so if get pushback
(technically informed) should keep.

Jeff - fine but if keep can't intersperse, must be after last data frame

James - last HEADER block that is trailers.

Roberto - Only trailers if last frame of headers block has a FIN & drop
intermediate ones.

Jeff - If we can that I'm happy I just don't want to buffer

Roberto - won't require any more buffering than you need to do anyway

Jeff - Get that meant at HTTP layer

Action Item: james to write up draft/text for Trailers. & also request/response ordering
of HTTP1.1 mapping.

Hassan - if didn't have trailers already & someone suggested it we would shoot
it down which is why I don't think we should do it.

(discussion on how to distinguish hear from trailers on HEAD with no body/data
frames)

James - if can dump is simpler but if we need it this is how to do it but need
that decision first

Mark - let's move on then


#### Rejecting Non-Idempotent Requests

James - need to very clear on text on this.

Mark - Does everyone understand what this is about? In HTTP1.1 you can get into
state sometime where you don't know if someone has processed request, but we
have more flexibility to identify that case with 2.0 which is valuable but not
possible in HTTP1.1 semantics.

James - Only thing is making sure that REFUSED_STREAM is used correctly

Action Item: James to review text to make sure he is happy.

Jeff - if resizing push promise you can always refuse it means I'm dropping on
floor & not processing, you can't force someone to send/not send.

Roberto - Can change error code name

Martin - refused talks about processing & really refers to whether it is safe
or not. PUSH_PROMISES are always inherently safe.

(discussion on safe vs idempotent)

Roberto - something we discussed in lobby is "Thou shalt only PUSH idempotent
request at HTTP layer). For HTTP layer will always be using cancel and refused
as no useful meaning at that layer.

Jeff - say something blanket & simple - at framing layer if get stream I don't
want I refuse it, if at HTTP layer I cancel it & that keeps the implementation
simple.

(discussion of refused vs cancel) - Cannot guarantee you will always know if
server as processed but when get refused stream you know it definitely hanse't

James - I want idempotent handle really clear

Martin - that makes me say don't use REFUSED stream for pushes, need to use it for something very specific. Then don't have any of this muddy problem.

Jeff - so when do you want to issue RST_STREAM

Martin - if don't want it send it when you discover you don't want it.

James - if getting more data than you want may want to cancel it. there are
legitimate reasons for refusing PUSHs

Martin - you're attaching a semantic to this that I don't think exists.

Mark - someone might want to say I didn't store in cache but I might in fitter
versus I will never put this is cache.

James - for idempotent requests refused stream & cancel are basically the same.

Martin - yes so I can choose to restrict REFUSED to very particular cases

Mark - this is going in circles, not blocking us write now, someone to write up

Action Item: James to write up text

#### SETTINGS Bandwidth, RTT, Restrans Rate

Mark - talk about all these settings frames together

Mark - Who is interested in keeping them around? Can we drop last 4 headers
frames (U/L, D/L B/w, RTT, Download_retrans_rate)?

Will - not even implemented in chrome

All - Yes


##### SETTINGS_CURRENT_CWD

Alison - can have background behind thinking

Mike - when we did it de facto was cwnd of 2, now default is 10 but we were
trying to figure out how to have HTTP protocol with fewer connections & when
ran that against standard HTTP with many connections had imbalance of win so
could't compare. Once move initial cwnd up to 10 need for this is mitigated as
can get 15KB of data rather than 3KB with cwnd of 2. My own feeling is since
TCP team did manage to react and switch to 10 as default it mitigates this from
HTTP2 and means we can just get rid of it. other thing is the big guys are
tweaking this on their own as they see fit. I would probably kill unless there
is data showing it is sufficient benefit of having. I put into chrome the idea
of persisting this as on lossy links cwnd was going low but other folks had
clean links with cwnd and wanted folks to restart with that high cwnd so does
hep but might be less now cwnd is 10. Will might have data from chrome
experiment

Will/Roberto - data is no good as systematic error in the collection

Leif - is opposite true - start high and move low?

Roberto - never want to try and cause congestion

Mike - complex topic. For HTTp2 spec if gains are marginal, no demonstrable
benefit we should cut it, if chrome guys have new data that would be cool

Alison - Have some things similar to this but never been used

Roberto - you suffer as for security reasons we end up putting this in kerne'
and windows takes ages to update kernel so what is cycle of experimentation

Alison - Have existed since late 90s

Mike - With HTTP we were putting in flags to experiment.

Roberto - big problem right now is seeing data that 16 is correct win but is
not correct cwnd across all traffic scenarios (e.g. in India, when under DoS
etc)

Mike - Also very content specific - If I'm sending big things may want one
thing, if I'm google and optimise all my content may get a different optimal
cwnd.

mark - important to distinguish server vs client side

Roberto - not talking client side at all

Roberto - is server could tell client please cache this value and pass it back
to me then that is what we would do today

Alison - Don't want to use few RTTs to get to value?

Roberto - No

Leif - Are you open to DDoS here

Roberto - no I have much bigger issues to worry about under DDos than this.

Leif - Could take out small ISPs network?

Roberto - No

Jeff - Dumb Q, when cwnd was 2 this made sense but now does it give HTTP2
benefit over 1.1

Mike - question is do we need the flag?

Jeff - we've seen performance gains without the flag

Hassan - Defer discussion until we have data

Will - I have data. When we measure SPDY conns over 1200KB of data so fairly
long lived for web browsing, win from server to client at end of connection (on
google.com) has median of around 32 (SPDY only not all HTTP connection), start
at 32 for SPDY.

Mike - So if start at 32 and end at 32 that means it doesn't change.

Alison - what is data set

Will - Chrome users accessing google.com that have opted into experiment.

Will - cumulative up through 0-16 is 33% - 1/3 are somewhere between nothing &
16. Up to 50% is 32, unto is 75% is 52 unto 90% is 74 and unto 100% is allay
unto 200.

Mark - that is what your algorithm has chosen to use, not that there wasn't any
congestion

Will - I'm just presenting thew data, everything we have modified we have
contributed to linux kernel

Mike - (Asked question I missed)

Will - We don't have that, no longer have the histograms

Hassan - If opine of group that would like more data Google can go back and get
more data.

Will - Happy to take out as I'm happy to experiment with it in SPDT.

Jeff - would like ti out as would like more data before people start using it

Roberto - would need to hack kernel to do this.

Roberto - have to convince a bunch of people first & client support is
problematic.

Mike - if get rid of this is setting just MAX-STREAMS

??? - And flow control

Mike - Damn if was only MAX_STREAMS we would get rid of it

Mark - On onw hand no consensus to keep in, on other hand want experimentation
to happen. If folks other than goggle want to experiment I'd like to facilitate
that.

Aruna - we are experimenting with this looking at different initial cwnd and
tcp & tcpdump data to figure out, so would like to have data in 2-3 weeks.
Doing with SPDY as well as HTTP. Would be happy to share data


Stephen - You don't have client so would be good to work with Mozilla/Chrome on
that?

Mark - One path is to leave it in, gather data, use it & have this discussion
again as already have joint session with TSV in Berlin

Jeff - We've removed persistence so does this give you anything

Roberto - not agreed to drop persistence

james - I have two pull requests: 1 to do comeback code & other is around
persistence.

Will - do not need this for experiments.

Alison - Lack of definition for how long to persist is worrying transport
folks, these things are very variable, e.g. can't even tell if path is still
HTTP2, transport is same.

??? - question - is last value used with server more likely to be correct than
the default value?

Roberto - seen initial cwnd has been too higher for locations in India where 2
really is the best value.

Alison - cwnd that you reach & cwnd you start out with. What I'm wondering is
it something that expresses better is tuning an initial cwnd to the history of
the path.

Roberto - that is the intent.

Ted - are you bikeshedding to change name

Alison - Yes "Initial CWIN hint"

Mark - Forgot to mention Alison is our TSV area technical advisor.

Alison - I think making it absolutely clear what the purpose is, we've had many
tries at saving a hint which is very different to saving a snapshot. I think
getting that across would make a big difference when communicating with TSV
area.

Mark - need more data, need to explain more clearly, do we want to keep in spec
to allow experiments or take it out

James - can experiment without it being in this draft

Alison - if de-mystified with documentation & caveats that is best

Mark - can experiment, go into Berlin & have discussion with TSV area based on
that data

Hassan - this is precisely what we meant by some features being "at risk"

(Discussion on how to work it without setting persistence)

Mark - if want interop need to specify

Ted - go back to Alison, way was experimented was using cwnd as initial cwnd
and could be different algorithm and can experiment with ways to generate hint
and I like that more than just taking a snapshot.

hassan - then leave as implementation detail

Roberto - we messed it up & implemented your idea, the data was useless as do
not have enough ways to segment out data. You need persistence for this, it
doesn't have to be general settings persistence but has to be what server told
you before or you can't run successful experiments.

Mark - Roberto you're proposing we make setting persistence spefici to this?

Roberto - acceptable for purpose of experimentation but more work

Mike - I have another idea, I hear the argument - same as a year ago. lot of
experimentation that hanse't been described but I'm pretty sure per results
that will come will be mediocre, no evidence it will be a win, would like to
help team move faster. only way to do that is to start pulling these hairs out
and we need to starting killing stuff. So lets take this out and let the google
guys experiment and if it is beneficial we can put it back in.

Dan - could do on server based on IP address

Roberto - No

Mark - Doesn't work at yahoo/Google scale

Mark - We have very short amount of time between now & berlin, berlin is
opportunity to have this discussion with TSV, we have a lot of work to get to
place we can implement for interop so lots of work over next 2 months. Who is
going to implement what we're doing and be able o include cwnd experiments in
implementation

Will - need to understand concerns, e.g. will it make it faster, doe sTSV think
it is wrong. If don't know concerns then don't know what data/metric we need

Alison - might be pressure because have meeting in berlin but there are a few
other things TSV people want to talk about like windows being reduced. So don't
need the discussion in berlin on the proviso that data is being gathered. This
looks a but like a transport protocols to be honest. Point is just panning we
have to talk about this again in Vancouver rather than Berlin is fine.

Mark - Thats i skinned of where I'm going. have compressed schedule, should't
pile on more unless folks are desperate to do something right now.

Action Item: Cut cwnd from spec & setting persistence with knowledge we can add
it back later as experiment.

Alison - If want to keep could put in separate internet-draft?

Mark - we will take out & other things may happen.

Roberto - been contentious, one path I've gone down is can always put it in a
cookie or some header and I've been hesitant to do so as I think it should be
visible and using cookie (which is probably encrypted) destroys that visibility

Mark - Going to take out, if someone brings data & proposal that shows gain to
add it back in we can do that.

Roberto - I will raise bloody hell until we have something that let's me deal
with artifacts

Mark - bloody hell noted Sir!

James - pull request I have adds a comeback error code for GOAWAY.

#### TCP Exclusivity

Martin - draft says HTTP2 runs over TCP and I think that is right thing.
Doesn't stop people layering on other things but not our focus.

Mark - yes can ignore for time being, relies on outcome of layering Task Force

Ted - when people done similar things in past would you consider them separate
to HTTP or implementation reports?

Mike - way went with TC is folks wrote separate spec.

Ted - Basically still writing as if someone can replace the transport without
deeply tying to TCP constructs. In some way like idea that don't write that it
must be on top of TCP.

Jeff - reliable in order.

Mark - need to write spec so it is easier to write for other transports but
when negotiate for HTTP that will map to TCP & TCP only and have a different
mapping it is a different ken.

Ted - if put in spec, this one or Eliot's it needs to be somewhere.

Barry - way to approach in spec is "requirements on transport protocol are.."
and "this document defines HTTP over TCP"

Alison - have to think whether write it differently if had protocol that was
very good at delivering out of order.

Mark - Right.

Mark - tension if want to factor out & make it possible for anything that is
huge task that is likely to fail.

Ben - Why not do nothing, layering separation gives us utility in HTTPbis and
if folks want other transports they can do that themselves we don't need to do
that work for them,

Barry - would like something in protocol doc to give people hint at what they
need to consider

Mark - if was having for 1.1 document would have an appendix "considerations if
writing this sort of extension/ampping"

Barry - think it more as things we thought about

Mark - don't want to have to write justification for everything

Alison - Ted is there utility in such an appendix?

Ted - potentially valuable but framing/layering discussion has surfaced you're
doing two things at once- changing underlying layer to HTP semantics and some
HTP semantics 1.1 to 2.0 trabsistion allows you to consider to have different
semantics

Mark - only in constrained ways

Ted - making sure which ones you're doing is a key part of the spec.

Mark - Of course

Mark - Don't disagree question why we need to talk about this right now?

Ted - if simplest is to write a consideration for other transports section in
appendix/other draft let do that to take it off critical path.

Gabriel - ….. if we're charted for over TCP let's do that and should not be on
critical path

Mark - have language on this in charter so can short-circuit discussion -

Action Item: Ted will write some text

Mike - every word we put in we have to review etc if we don't need the words
let's take it,

#### Jefff's Issue

Jeff- would lit to move zeroing out length to HTTP layer not framing layer so I
can tunnel TLS etc.

General agreement that is fine.


### Wrap-Up

 
#### Issues List Review
 
* Moved settings in upgrade off of critical path
* Added settings persistence to critical path
* Martin: Goal to get all Layering TF items done in next 2 weeks.
* Leave persistence out of the draft, deferring Comeback to later discussion.  Once use case is clear, the we will come back and debate this.  Hasan / Roberto to come up with proposal for persistence / Comeback.
* Do not remove the persistence flag bits.
* Mark:  Defer all extensibility discussions.
* Signal acceptance of Settings frame.  Mark has preference for new Frame type.  Deferred to future discussion.
* General objection to complication.
 
 
#### Germany Meetings

* Likely meeting is Thu-Fri in Berlin.  Interim is in Hamburg is Mon-Tues.
* Suggestion is that we do some interop testing in Munster over the weekend.  Pushback to working on the weekend.
* Other suggestion is to do interop in Hamburg.  Take one day and do interop.
* Goal is to have the next draft on 7/4.
 
#### Implementation and Testing

* Are we writing a test suite?
* Alison:  Test flow control before Berlin would be very powerful.
* Jeff, Hasan, Roberto: HTTP 2.0 Flow control works.  Tested and deployed.
* Mark:  Need to represent all the SPDY and Flow control implementation and testing experience in Berlin.
* Who will implement HTTP 2.0 in Berlin for interop:

 * Twitter: Will likely have port 443, Likely NPN on the web implementation.  Twitter client will not have it yet. Unlikely to have a client
 * Mozilla: Will have "something". NPN.
 * Chrome: Will have "something" on a local build.  NPN.
 * Google Server:  Will bring up a server somewhere, as close to the draft as possible.  Likely ALPN, NPN and forced on this port.
 * Microsoft: Contributed ALPN to Open SSL yesterday.  MS-OpenTech will have a server.  Not IE.
 * Akamai: will try and have a server.
 * Mark: Python client side and server side:
 * James: Java client
 * Reach out to Open SSL group on reviewing ALPN contribution
 * Shared testing framework
 * Main issue is who will do the work?
 * Good idea to have a client and server test suite for interop testing.
 * Fred:  Possibly adapt SPDY suite to HTTP 2.0.
 * Mozilla:  intern adding HTTP 2.0 to Node.js
 * Biggest problem is resourcing and then maintaining after "summer of code"
 * Better if there are multiple entities working on test suite.
 
#### Future interim Meetings

* For November, meet somewhere close to Vancouver the week before.  2.5 days.  Some interop testing.  October 30 - Nov 1.
* At least one more interim, potentially Zurich in January / February.
* Early March in London. 
* Another interim if needed post London, potentially Australia
