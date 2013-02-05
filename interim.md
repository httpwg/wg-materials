HTTPbis Interim Minutes (30/01/13 - 01/02/13)
=============================================


HTTP/2 initial draft status
---------------------------

Martin: one draft - SPDY with name change. new abstract into, addition of some
conclusions on upgrade/negotiation. No conclusion on TLS side yet

Still some discussion between authors on framing and how to explain etc.

Mark: need to talk about terminology as not clear in document right now.

Martin: current draft is fouled on minimal info to do an implementation but
lacking in introduction & "fluff".


Upgrade
-------

Mark: asked TLS WG to work on mechanism to upgrade within TLS which may or
may not look like NPN. Have pinged for status but not heard back.

Eliot: see no reason why to normatively block on that which you are in the
draft

Martin: that can be removed if you want to weasel around it.

Mark: If we're ready to publish and TLS WG are not ready we can take it out
and not block on it so we can take that decision (whether TLS upgrade is
normative) later.


### Version identification

Mark: are people comfortable with it?
(Text needs some cleanup but not discussing editorial stuff)

Mark would like to see it discussing things in a more fine grained way - e.g.
upgrade to HTTP/2.0 but using TLS or HTTPS etc. Might want to put that (large
set of constraints)

So could use token as a sort of "profile"

Alexey: are you suggesting some structure to token or just more extensive
list.

???: What is purpose

Have a HTTP URI and want to use HTTP/2 and TLS to retrieve resource. Client
might support 1.1 & 2.0 over TCP and 2.0 over TLS and negotiation between
client server and do we want to use the Version ID token to signal that sort
of thing?

Token could be used in upgrade, as part of NPN etc.

Eliot: I thought you were referring to the token used in the method/first
line.

Mark: that's 1.1 we may or may not do it that way

Gabriel?: some scope overlap with HSTS?

Mark: this is what are the things I can do next on this connection?

Patrick McManus: this is essentially directory/policy information for what is
available.

Eliot: more like capabilities

Mark: see as way to drive convergence - if have named 'profiles' browsers can
converge on what they support & server can do the same. People who define
'profiles' define how fine grained they are.

Roberto: discussed internal to Google. We've never seen enough demand to
actually do it, so safest thing is describe how one might accomplish it.

Mark: defining those profiles is not something HTTPBIS wants to get into but
should we leave that door open?

Eliot: don't want a lot of these things as the more you have the more interop
problems you'll have.

Martin: thing that bothers me is we're talking at two levels - top level
identification and then things that exist in protocol (e.g. foo transported
within HTTP/2). the latter is negotiated feature once decided to use HTTP/2.
Whereas what Mark is talking about is "HTTP/2 with this set of options".

Roberto: e.g. client could be browser and may want to indicate whether
want/support Websockets. Don;t want to have wasted a RTT doing something else

Martin: so Q is have this negotiation upfront, or just negotiate HTTP/2 and
let the client try these other things and have them fail like today.

???: is there a difference between upgrade on session and on a per-stream basis

Roberto: can't see this applying per stream, capability is per-session.

Will Chan: talked about it within NPN which just sees opaque strings

Roberto: killer app is HTTP so we haven;t seen a need for it up to now.

Mark: overall goal - we want to do this right once.

Roberto: so long as define a portion of this as opaque string which we don't
define right now, then we have portion of version string we can put things in
for HTTP/3 etc. E.g. can have curly braces in version string and everything in
there is opaque.

Mark: reminds me of media types - defines a format but people want to put a
scheme etc in it too and we don't do that for media types and there's a reason
for that.

Roberto: only concrete thing I can think of right now is whether websockets is
available or not.

Martin: doesn't seem to be any kind of registry for these opaque strings.

Mark: sounds like we're talking about an opaque string where we define just a
handful. Sounds like we need somebody to start running things down and
thinking through the use cases.

No-one volunteers to do that.

Belshe?: how about we don't do this at all - opaque string is not
interoperable. Unless implementation understand it it won't get used as they
don't know what to do with it. So without something concrete specifying it is
worse than specifying nothing.

Mark: have number of upgrades mechanisms. However you identify
capabilities/tokens they should be the same for the different upgrade
mechanisms - e.g. same for NPN & upgrade, etc.

Gabriel?: maybe have some text in HTTP/2 draft and then separate draft(s)
e.g. "this is how websockets us it" etc. Need to go through example use case

Mark: sound silk use case are http/1.1 vs 2.0, negotiating TLS in some
circumstances, HTTP Vs websockets. As long as mechanism addresses those use
cases that's all we need to write down.

???: Little lost, What are we trying to define?

Mark: trying to define shape of strings and place in ecosystem and couple of
mechanisms like DNS/NPN/Upgrade that use those strings. Then we'd define a
couple of use case for those strings.

Mark: might help if in our discussion HTTP/2 is used to main framing layer &
HTTP messages over that framing layer.

???: Need to be careful with websockets as that has it's own 'dance' for
negotiating capabilities.

Roberto: one of reasons we haven;t done this to date is larger you make the
string the more you slow things down.

Mark: Of all upgrade mechanisms, if already know what protocol you want to
use (e.g. HTTP vs websockets) do we need to worry about that in this exchange.

Roberto: how does content provider test the waters before deploying anything
otherwise they won't. E.g. I'm a bank I might want to say "I want to use
HTTP/2 but for X type of transaction I want to use TLS+HTTP/1.1 because it's
better known/signed off by my security guys/etc"

Eliot: this is a capability exchange and then you apply local policy.

Mark: we negotiate/advertise versions and transports?!? and then just leave it
there?

Martin: easy if we consider two use cases we have today - straight over TCP
and TLS. The one that bothers me is use of TLS to request http:// URIs, that
implies either use of another label or some other sort of signalling.

Mark: not quite as simple, e.g. if I use Alternate-Protocol.

Roberto: today if using SPDY you have accepted idea you can send both http://
and https:// schemes over same session.

Roberto: some of this string might not be useful because you may already know
- e.g.. if use NPN to negotiate you know you're already over TLS. Someone
should go through use cases and have a mechanism that defines "this part of
the string you don't interpret unless you know what you're doing" and call it
a day.

Roberto: I will try and do it but that is not a promise.

Mark: what does version part in HTTP/2 frame mean?

Roberto: that was put in because thought there may be a proxy and may be
receiving frames from different clients talking different versions and would
be cute not to have to change the framing, just forward it and the end point
can figure out what's going on, and it's turned out not to be very useful, so
we should just get rid of it.

Mark: HTTP/1 versioning is hop by hop so don't need to persist in message. If
we get rid of version in HTTP/2 message/frame some people will complain it's
not self describing. I don't particularly care I'm just commenting there will
be some pushback.

Gabriel: maybe have a mechanism so server can tell from first frame (magic
number/byte/etc) that allows server to disambiguate the protocol.

Roberto: does this come from hybi approach - if can fast fail that is a good
thing.

Mark's suggestion - do something like send a first line of "NULL * HTTP/2.0"

Patrick: if you send anything but HTTP/1 over port 80 you get ???? (a mess??)

Mark: use case as I understand it - if I have a server farm and I've only
upgraded half of it I want to fast fail. Is that use case good enough to burn
17 bytes at beginning of every connection for all time?

Belshe: proposal is get rid of version in frames and instead put something in
the beginning of the connection?

Martin: two things websockets had that protected ???? - non-ASCII and other is
look at response to upgrade that shows in the positive that server had not
only understood but had acted on the upgrade.

Belshe: one option is to always send a SETTINGs frame first

Jeff?: Basically can we kill version in the frame and then fail fast.

Roberto: like sending SETTINGS frame first, don't want to restrict ourselves
to whatever framing is guaranteed to make an existing HTTP/1 implementation
barf, e.g. if first bytes of SETTINGS frame happen to be "GET".

Will Chan - can we step back so I can understand the use case? Is it only in
enterprise setting where you know the out of band negotiation scenario or will
this be done out in the open? I don't see browsers doing this out in open.

Belshe: declare version upfront without ??? If we're going to have a magic
string or whatever upfront it should be constrained to just indicating the
version.

???: Another thing we might want is info on user agent, e.g. have a broken
version of chrome wrt SPDY and we know Chrome XYZ has this bug and would be
nice to say "this version of chrome is broken and so we're going to behave
slightly differently"

Mark: one nice thing about that is you would pre-seed the User Agent into your
compression context.

Martin: a lot of protocols have a session start message/thing.

Roberto: have 'magic bits' and then after magic bits need to make sure we have
mechanism to allow client to send settings/metadata/whatever.


### Session start message

Need some magic we send once per session/connection, question is show much.
Need to make reliable enough so it makes things fail but short enough that it
doesn't hurt us.

Mark: would be nice if had easier ways to get answers, like a 1 file python
script can put on git and have people run it in weird places like airport on
way home, etc. to gather information.

Will Chan - Happy in Chrome to do this kind of probing, we have done it in the
past.

ACTION: Come up on list of shortlist of reasonable client sequences to test.

Conclusion:
- Get rid of version field in control frames
- Invest in researching 'magic' at the beginning of a connection
- Talk more on list & get proposal for how to identify protocols
- Do some testing

Also agreed (textual) token/string should be opaque and same between all
different upgrade mechanisms. Exact format/structure still TBD. How it applies
in different situations may differ.

Eliot: registry - HTTP/2 draft explains what's required to get into registry
etc. I will volunteer to write that text.

Will Chan - two different directions of negotiation - Upgrade is client side,
NPN it's client indicates extension support and server advertises protocols
and client selects what it wants to use.

Mark/Eliot - what's the impact there?


### Alternate-Protocol

Mark: Alternate Protocol is that something folks still want to do or has it
fallen by the wayside?

Will - Don;t think there is a lot of active interest but keep in the back of
mind as alternative option. Happy not to pursue right now, but if I get
unhappy with other options I might bring it back up.

Martin: Not going to reduce to a single upgrade mechanism but would like to
keep to as few as possible.

Jeff: only thing I can think that Alternative-Protocol gives you the other
don't can be solved with a redirect (although A-P is nicer).

Belshe: redirect is not equivalent.

Implementation status - Chrome has it, Mozilla have it (but a little buggy).

Mark: Punt on A-P right now, see how things go, if browser or server folks
start to feel it is something we need we can talk about it then, but if we
don't need it that's nice as one less thing to define.

Will - would like to reserve judgement until we've discussed DNS more as it
seems to have similar properties.

Patrick - Bias towards leaving it in for now.

Mark: but we don't have text right now.


### DNS

Eliot: draft-lear-httpsbis-srvinfo

Eliot: Comparison of different use of DNS, some commonalities, some things
we should do no matter what.

Eliot: 1 motivation is to avoid a RTT, so let's avoid just moving that RTT to
another protocol.

DNS not a complete replacement for Upgrade as might not have DNS at your
disposal. Can not just assume DNS is there.

One question for the end - is discovery of transport protocol important?

Unstated design goal - if going to HTTP/2.0 then goal is for everyone to get
there eventually.

SRV as an approach - SIP makes use of it, jabber uses it, MS AD servers make
heavy use of SRV. Many folks do a zone cut at _tcp.example.com and so have two
sets of authoritative name servers so may need to ask both of them to get the
answer you are looking for. Any additional info in response is considered
non-authoritative and many clients throw it away to get authoritative info. If
don't have additional info, need to do an additional query to get that info.

Mark: summary - because of what SRV is used today, may be zone splits and
trying to minimise number of queries may not be easy.

Patrick - what is split DNS?

Mark: one DNS server inside the firewall and another outside.

Eliot: NAPTR and URI as an approach - Builds on SRV, allow transport protocol
discovery but not protocol version.

Martin: it can do using the "label" you select on.

Eliot: haven't seen that but you can layer on top of it and end up with some
capability to do something like that.

"Running a race" as an option. Browser folks are used to doing that - e.g.
Happy Eyeballs. Could do something similar for HTTP/2. Not a bad idea but on
its own you still need a capabilities advertisement.

Roberto: likely to be more expensive and end up with two connections.

Martin: depends how far through the connection (like TLS handshake etc) you
get.

Eliot: it is something to keep in mind as I think it would be handy.

Martin: what would you be racing?

Eliot: may send multiple queries for multiple info.

New record Eliot put together - SRVINFO

Couple of people raised maybe we combine protocol & version and call it
'profile' or something. There may be some tradeoffs

Because there is no domain name on right hand side have info you need as
getting A record - same domain so guaranteed to be the same authority. No risk
of required sequential lookups, may need to query in parallel for A/AAAA
record.

Are some issues not using underscores, e.g. cnn.com if someone has whole bunch
of web servers could get a very long list.

Doing some testing at Cisco, SRV is guaranteed to end up using TCP for DNS
queries because of the way Cisco do AD load balancing.

Martin: dropped weight can you explain why?

Eliot: did anyone seriously use it? Don't have opinion, if you think it's
useful send something out saying why, but I don't think it's useful
operationally.

Martin: I can write something up.

???: something you can do with weight you can't do with more priorities?

Martin: yes as priority is strictly ordered, no way to say these are all equal
priority.

Roberto: biggest issue with weight etc is not everyone respects TTL.

Eliot: tell me if you think weight is useful as it didn't seem to be to me and
others I spoke to.

Introduced instance ID - idea is have URI you are starting with and
implicitly/explicitly have a port you will connect to. That port may be
running multiple protocols. But if you want the same service on a different
port you need an index to tell you that and that is what instance ID is.

Mark: implies server has to always send something with port 80 in, so I can
say here's the 80 port with this instanceID and this other port has the same
instance ID so I know it is the same service.

Eliot: yes, need to process whole record. Meets the requirement to run
multiple servers off the same host.

Jeff: seems more like a discovery information

Eliot: it is a capabilities discovery mechanism (it is not a negotiation).

Jeff: server has no way of pulling it back once advertised

Martin: DNS TTLs.

Eliot: let's start from the premise that this isn;t the first thing you do.

Mark: hopefully when you advertise this and try a HTTP/2 connection it fails
fast so client can fallback to HTTP/1

Martin: this might be the first thing you try as a client but may not be the
first thing you deploy as a server.

Mark: raises important point - feedback i've gotten is it is important to us
to provide guidance to folks who want to deploy HTTP/2 to help hold their
hands etc. Anyone interested in helping with such a document (would be
separate document) I would love to hear from you.

Mark: Summary: There are a lot of caveats with DNS and new records etc. Not
saying we won;t do A-P because this is so great, just we're going to run with
DNS for the time being.

Eliot: have shown SRVINFO & A as parallel queries. DNS in theory supports
multiple questions in same query but don't think anyone has ever deployed it.

Mark: from web standpoint the thing I'm fundamentally connecting to is an
origin which is tuple of (scheme, URI, port), whereas this looks like
indirection layer

Eliot: actually an equivalence, not an indirection.

Will: browser optimising for latency would issue 3 queries in parallel -
SRVINFO, A & AAAA

Eliot: one thing noted in draft - absent DNSSEC it is a bad idea to mix
security models with this. Eliot - could include 'profile' (based on token
talked about earlier) that indicates that

Mark: instanceID seems convoluted. Can we simplify it?

Roberto: we did, if we put the token/NPN pattern at the end of this then we've
normalised what sysadmins have to write to configure, got rid of instance ID
as can state multiple things in that pattern?

Eliot: no but could chance instanceID for a mnemonic name.

Jeff: asked questions around how it works with CNAMEs that I missed.

Eliot: this doesn't change how you advertise certificates on hostnames for
TLS. IF you want to preserve name across then SRV does that for you.

Eliot: continuing presentation.

All this info is cached and I was viewing as positive thing, but talking to
??? he mentioned it could be negative.

Summary:
- Clients don't know where zone cuts are and you can't make assumption about that
- DNS is one of 3 approaches to provide info prior to connection (other being new URI & HTML).

Questions:

1) Is the optimisation worth it? Not a place to start, but a place to go to
but a lot of mechanism here. Eliot hasn't formed his own opinion on that yet.

Mark: not just that - increasing deployment flexibility, giving some
additional ???

Jeff: and can get to to HTTP/2 only

Eliot: not thought through how this works in a world without HTTP/1.1 I have
not thought that through and is something the draft should discuss.

2) Are people interested in using HTTP over things other than TCP?
 - Couple of people nodded their heads.

Eliot: if talking SRV then doing multiple queries (_tcp, _foo, etc) but those
would presumably be done in parallel.

Eliot: I implemented SRVINFO in BIND, so not that hard to do.

Mark: I have a home router with a DNS proxy in, is it going to filter this?

Will: 1) a new record - we see many cases where it completely fails, (2) for
substantial portion of user base are using cheap routers, e.g. issue with
Comcast where some of their (2wire?) routers will only allow 6 parallel
lookups at any time. So if for performance optimisation, it might end up being
a performance cost.

Eliot: one design goal is not to impact app performance and this isn;t
something you introduce 6 months from now. Problem is common to DNS, not this
record.

Belshe: interesting stuff but when I think about all the things we still need
to talk about then this isn;t interesting at all. Can we table and look at it
again in 6 months.

Eliot: need implementation experience so need to do that before we actually
need it, so might want to start earlier.

Mark: hearing doubts on using DNS and whether a new record is a good idea.

(break for lunch)

Any interest in using an existing record type?

Will: We have data on TXT records for latency and success rates, which
should improve if we start using it.

Will: there will be a hump that this introduces if this is a serial dependency
- we would have to start with non-blocking [non-serial]. Happy eyeballs style.

Mark: would upgrade mechanisms be interesting for prototypes and testing?

Patrick: upgrade would be one of the first things that I want to test

Patrick: (re: new record types) I'd like to get some data on success rates,
etc...

Mark: structured TXT?  How is that likely to be a problem.

Eliot: structured TXT might suffer the zone cut issue, but these would
be on an underscore prefixed sub-domain, but this doesn't have the
same sort of deployment lock-in that _tcp does.  DNS directorate loves
new record types, but there are some operational concerns.

Will: why do we care about failure rates?  We know that there are
failures (~4-5%)

Martin: I can find some more stats on DNS success rates from some
other IETF work
http://www.icann.org/en/groups/ssac/documents/sac-035-en.pdf

Patrick: Are your stats for large requests that required TCP?
Will: don't think so

Eliot: What plans do people have for TLSA?  Is DNS so hosed that we
can never get another RR defined?

Will: Relying on something from the start might not be wise, but once
we start trying to use it, as long as there are no serious problems
doing so, we can use it and things will improve.

Patrick: I'd be interested in how badly a new RR underperforms TXT.

Mark: we need to get this data and then we'll have the info to choose
between new RR and packing stuff into TXT.

Eliot: the SVCINFO to TXT encoding is simple

Will: when are we going to come back to discussing Alternate-Protocol?

Mark: we should try to get the first things done first, unless someone
feels strongly about it.


Header Compression
------------------

Tour of: https://github.com/http2

Presentation by proxy of
https://docs.google.com/presentation/d/1x8GvY-7FJi57DW9vSvjTF1QnTkzM18mXi_LQUUprZeo/view#slide=id.p


### Long brainstorming session about the goals of a compressor

Mike B: the primary goal for SPDY was latency reduction; getting
perfect or near-perfect compression isn't necessary to achieve that
end

Goals for header compression include:

- privacy 
  - CRIME ATTACK
- Latency reduction
  - head-of-line blocking?
- Compression efficiency
- CPU overhead
- Memory consumption
  - initial
  - idle
  - under DoS
  - receiver control
- implementation complexity
- proxyability
- error handling
- ability to define new headers and maintain properties above

Editors note: we will need to capture this: the header compression
algorithm (and many other aspects of the protocol) can only really be
changed by also changing the entire protocol - the theory being that
the specification and deployment of a feature like this incurs pain
roughly equivalent to an entire protocol revision.  At a minimum, we
can turn off the compressor.

On the question of header types and the registration policies for any registry.

Mark (indiv): we want to limit the number of types to avoid the need for
bespoke parsers for every new header field.

Barry: suggest standards action for new types

Mark/others: don't need that, don't want even the hint of that.


### Roberto on delta

Jeff: what are the implications for proxies

Martin: the upper bound on state at an intermediary can be defined by
the server if you use passthrough

Roberto: you can act as a server and advertise a lower limit

Martin: state for headers has implications for servers; e.g. if a
request is rejected, the server is required to parse and apply any
state changes that the request established

Roberto: yes, it's a trade-off

Jeff: is there any desire to make this non-HTTP?

Mark: I'm not encouraging this

Jeff: Reusable code for the compressor would be good; zlib is easy to integrate

Ilya: it would be good to have a good test suite

Mark: modular code would allow for reuse of portions of working
implementations in new implementations

Mark: are we interested in binary encoding?

Roberto: yes, it regularises the format, which is valuable

Jeff: SPDY already gets a number of those things, like \r\n processing

Roberto: we get rid of that with anything that we do

Mark: I'm a little concerned about how far we disappear down that rabbit hole

Jeff: key-value compression is going to get us a lot

Martin: Date changes on every request, which makes that a non-gain

James: We can encode dates down to 5-6 bytes. Even if they change
every message, that's a significant savings.

Jeff: but Date is so trivially small in comparison to Cookie

Will: James wanted to avoid having state with this

Martin: URIs can be compressed by losing the high bit

Mark: I did that

Jeff: You can't because some clients send UTF-8 text

Roberto: delta is pretty much the same as the simple thing, with 30%
extra saving from the huffman coding

Mark: I was surprised at how much could be saved by looking only one
message back.

James: Weighing in remotely.. binary encoding offers many benefits at
cost of significantly increased complexity... need to be very
careful... also, we're going to need to run lots more tests on the
delta state management.. very concerned about this in middleboxes

James: Requests are EXTREMELY redundant and wasteful of bits on the
wire. Delta does very good with those requests.

James: Looking over header stats, custom unregistered headers tend to
take up quite a bit of space. Allowing those to be binary may provide
benefits.. on the other hand, base64 and hex compresses very well. So
definite tradeoff. I'm not convinced either way completely yet tho.

Jeff: Interested in treating headers as opaque blobs, so that we don't
have to look at the contents of the header.

Roberto: looking inside can give us some benefits

Jeff: I don't want to see lots of types, so that the outer layer
doesn't have to bother with the content of the headers.  Only smaller
headers above the compressor, and enumerating types and restricting
them, might be.  Cookies are better to concentrate on.

Mark: dates were a significant proportion of the compression savings

Roberto: cookies contain significant entropy, so they don't compress well

James: If we allow cookie values to be optionally binary, we can see
*some* savings... but that's a whole can of worms I'm not sure we want
to open...

(Martin: James, we did discuss that option and there seemed to be some
enthusiasm for it.  Keep in mind that binary packing saves only 33%
over base64, which is either huge or trivial, depending on
perspective.)

James: precisely, right now I'm running tests with binary cookie
values and the savings are generally minimal. To realize real savings,
we'd likely have to reeducate devs on what "types" of values are best
to send... not a good thing imo. Like I said, not sure it's going to
be worth it for cookies...

James: However, binary coding the Set-Cookie header itself (not the
value) does yield a significant savings (up to 50% in some cases),
because of packing the date, changing httponly and secure to single
bits, etc

Patrick: cookies aren't a problem everywhere

Jeff: Changing so that we send multiple cookie headers, so that we can
compose from the ones that change and the ones that don't, then we can
save the space.

Patrick: We can do both.

James: I tend to agree to an extent. It would be beneficial to have
some of the data outside of the compressed header block.. path, host,
etc. But we cannot predict what other headers may become important
later on. So this is hard to optimize.

James: If we take a look at the header stats.. which ones are most
redundant, which ones are most variable, and optimize for the extreme
cases (dates, cookies, accept-*, p3p, etc) then we make major gains.
We don't have to optimize everything.

Roberto: delta can beat gzip on some sites (pinterest)

Jeff: delta alone is great, and we could probably stop there

Mark: you can always just send the text.

Jeff: we shouldn't be spending time on binary coding. it increases
complexity, conversions are not hard.  it should be simple

James: I agree to an extent. Not convinced we should do binary coding
either yet. It does, however, produce significantly fewer bits on the
wire, so need to prioritize requirements. Do we want optimum
encoding/compression or do we want more simplicity.  The potential
increased complexity might be too significant to ignore

James: Maybe we should stop at just binary encodings dates and
numbers? (date, expires, :status, last-modified, if-modified-since,
set-cookie expiration, etc)

Roberto: we can implement the date change and see what that gets us

Mark: date really did move the needle.

Will: does date really move the needle on latency?

Roberto: Date can comprise a significant overhead.  Especially when
you stop inlining.

Mark: Amazon data moves from 0.47 to 0.39 compression just compressing dates.

Herve: there are lots of cache check requests that generate lots of
304 responses, which include lots of dates.

Mark: Maybe we should start with delta and then we can experiment with
binary encoding.

Roberto: has a simpler implementation of delta (delta2)

Jeff: I'm going to implement a shim that looks like HTTP/1.1 to its
users, simplicity.

James: FWIW, amazon data moves to .20 compression with delta+bohe,
which includes dates, cookies, p3p, etc ... that said, delta without
bohe is also .20 on requests ... on responses, delta+bohe is .23 and
delta is .31

James: Mark, +1.. but we really do need to get a firm grasp on the
impact delta has on middleboxes before we commit on that approach. In
general (in theory) it looks ok, but there are definite risks.

James: While waiting, just another quick comment re: delta and state
management, there definitely is a significant security risk. If a
malicious sender purposefully sends junk requests targeted at the
maximum storage size specified by the receiver, the receiver could end
up being forced to store quite a bit of junk data in memory. Not sure
yet how we can deal with this.


### Herve on headerdiff

headerdiff looks fairly similar to delta in operation - table at
decoder or a size the decoder chooses; the encoder sends commands in
relation to that table

Name table is pre-populated with common header names; value table keyed
by names: as each value appears, three options for the command: add,
don't add or replace existing

deflate as optional on the already compressed stream, which makes it
faster and more compact than SPDY/3, but no good solutions for the
CRIME attack (editorial)

James: I tried many various combinations of stream compressors, every
case was subject to CRIME-type attacks. All it required were minor
variations in the approach, easily circumvented. Most compelling
approach resulted in random compression ratios, but all attacker had
to do was average those out over multiple requests. More work, yes,
but still feasible

Looks like headerdiff is slightly worse than SPDY/3, without deflate,
but adding deflate made it better.

Martin: I like the dictionary of names - from both compression and
performance perspective

Mike: the dictionary in SPDY can make a difference initially

Jeff: the dictionary can cause stuff-ups in code

Will: we shouldn't spend a lot of time on this stuff

James: There are many ways we ultimately could end up doing this.
bottom line is we need more implementation experience around alternate
header encoding and compression. To determine impact on servers,
security implications, complexity, and performance, not just ratios.
We don't have sufficient data yet to make a solid decision.

Patrick: what do we know about how this resists attacks like CRIME

Roberto: we've had people look at this (AGL) and they are ok with it,
you need to guess the entire thing, so if the cookie isn't trivial
it's very hard to attack

James: Delta is very good approach re: CRIME ... but carries other
risks. We need to determine what the trade offs are. If we stop CRIME,
but increase chance of DDOS, did we really help? Consider also that
Delta requires state to be kept around in memory for a while. If
middlebox is compromised in some other way, an attacker might not have
to use CRIME-type attack to get at the data, they could inspect memory
and read data from the compression state. More difficult, yes, because
it requires direct access to the server, but not impossible. We need
to be careful putting cookies and auth headers, etc in stored state

Mark: we'll expect drafts from Roberto and Herve on descriptions of
the latest and best algorithms that they can produce and go from
there.


Hop-By-Hop Headers
------------------

Mark: hop-by-hop headers...  Not a lot of writing into the header
block by intermediaries.  Is it OK to drop all the hop-by-hop stuff.

Will: Yes, SPDY doesn't do hop-by-hop.

(Discussion about what happened in SPDY)

Mark: please, can folks changing SPDY make issues in the WG

James: I think dropping them would fine. With SPDY framing, we have
other potential options for introducing hop-by-hop stuff later *if
necessary*. But for now, don't see any reason to keep those

Mark: we will drop hop-by-hop headers because all that is moving into
the session layer.

Alexey: why?

ISSUE: need a new issue for 100-continue

ISSUE: need a new issue for negotiation of trailers

Roberto: it's not clear when the headers are done

Mark: HTTP/2 currently allows for multiple sets of headers; the
receipt of data might be implicit signal for end of headers

Roberto: not in some cases, where data can race headers to the wire

ISSUE: need a clear delineation for the end of the header (or trailer) block

James: I can see a number of compelling theoretical cases where
multiple header blocks would be great in applications. However, we
should have a distinction between headers in the SYN_STREAM vs. header
blocks sent later in the stream

James: Keep headers related to the HTTP Request or Response in the
initial block. Allow apps to send other header blocks later, but those
serve a separate purpose... trying to come up with a good label for
them... But, in theory, I don't think we should rule out sending later
header blocks in a stream


Frame size
----------

Mark: some people want bigger frames

Roberto: smaller, please

Patrick: flow control depends on having gaps to allow pre-emption

Mike: 16k seems small

James: Opt-in for bigger frames? Require receiver to explicitly
indicate that they accept large frames as part of flow control
mechanism?

Patrick: the argument is a zero-copy argument

Mark: what about a new frame type that allows for pushing massive
amounts of bits down the pipe, no flow control, etc...

ISSUE: where do we capture all the important headers (colon headers in
SPDY, plus Host) so that they appear first?

Mike: sendfile was added specifically for web servers, let the kernel
vendors add some new APIs

James: flow control settings can indicate max frame size or support
for large frame type... syn_stream can indicate that sender intends to
send large frames?

Mike: you can use smaller frame sizes in practice, even if the maximum
size is bigger than what you might normally (or reasonably) use; we
did introduce new limits that didn't exist... in theory

Roberto: proposes that control frames have a continuation bit for when
you need to send another frame

Mark: I don't want to live in a world that has more than 16Mb of HTTP headers

Jeff: does anyone do more than 8k?

Patrick: 4k.  we don't want to get boxed in with a massive frame, I'm more
concerned about that than a protocol that stands the test of time

Mark: no one is saying that we need to make it huge

James: just noting... in header stats tests I ran, amazon data, header
values accounted for 110,743 bytes across 366 messages... that's
uncompressed data.

Mark: what is the optimum size?

Jeff: 16k (for TLS record layer) at which it is too slow

Will/Hasan: 16k is already too big for TLS

James: Can we just allow receiver to specify a maximum frame size they
will accept and go with that? Why should we try to define some
arbitrary limit? Allow it to be set as part of the flow control and
have the value tweaked over time to reflect requirements

Brian: there are some issues raised by an MS engineer regarding frame sizes

Roberto: some of these are OK, like settings;

Mike: frame size can affect latency (ed: suspicious); limiting is
arbitrary; if we need larger frames later, clamping down might be too
early

Mark: we can avoid negotiation by having a goldilocks frame

Mike: same size maximum for control and data (agreement)

Mike: too many times got burned when we placed a limit and discovered
that the limit was too low

Roberto: small frames does mean that there is a fair chance that
people will have to write continuation code (and test it)

Hasan: we will then need header value continuations for those mega-cookies

Roberto: the continuations would operate at the frame layer, you build
all your headers, encode them into a massive buffer, then chunk them
up.

James: Header bytes are small in comparison to data... not overly
worried about Cookies just yet. Nothing I've seen so far with header
data suggests that they would need to be split up among multiple
blocks for a while.. at least not in our sample data

Jeff: don't care about size, you can write an implementation that
throws stuff away

James: We need to do better at educating developers on more efficient
header definitions (look at P3P header as a bad example)... more
efficient values, means less wasted space and smaller frames.  I'm not
overly concerned with control frame sizes tho, those are easily
managed.

Mark: a single frame no longer necessarily includes the entire message

ACTION: Roberto to provide a proposal regarding frame size: 16 bit
length, +1 bit stolen from flags to indicate continuation.


Flow Control
------------

Flow control principals reviewed; no disagreement.

Stream-level flow control is not controversial.

Session-level flow control is interesting to many (and viewed as necessary to
some), but some believe it's not going to be useful, because the response to
it being exceeded won't be different (close the connection).

Resolved to spec out a proposal for session-level as well as stream-level flow
control.

ACTION: Will Chan to make proposal.

Also some discussion of a new control frame to indicate that flow limit has
been reached; optional on both sides. Not much interest, but no disagreement
yet. No one offered to make a proposal.

Agreed flow control by a receiver can be disabled by sending a very large /
reserved value.

Initial values for flow control - we need some testing. 

64k per stream and per-session seems reasonable. Will test and gather feedback.

Patrick: Can we have asymmetric defaults? Big for clients, small for servers.
Will: but client can send settings frame.
Patrick: yes, but defaults for performance.
Martin: Could be part of HTTP/2 magic.
Settings are also persisted, but only per origin.
Roberto / Eliot: It may also be interesting to put the default settings frame into DNS.

ACTION: Eliot to scope out a DNS-based "initial options" record (TXT-based?)
to avoid wasting a protocol.
- flow control window sizes
- max stream
- pointer to browser hints

Discussion of constant bit rate flow control, e.g., to control use of radio on
mobile; felt that this isn't an appropriate use of flow control.


Priorities
----------

Mark: two axis here how much interleaving Vs waiting to send back response,
right now we only have 1 axis

SPDY4 proposal - priority queue, strict between priorities but undefined for
requests at same priority.

Eliot: How many queues do you have? Answer: 8

Roberto: tab pri and pri of what is visible is hard/impossible with strict
priority. No requirement to finish high pri before sending low pri.

Roberto: rule we execute is send highest pri available thing so don't starve
low pri thing waiting to get/generate high pri thing.

Belshe: we found same prioritisation approach in browser wasn't optimal for
all sites. Room for research here.

Belshe: what is use case for strict ordering and why can't be accomplished at
app layer?

Roberto: obvious uses cases for priority e.g. switching between tabs

Mark: 3 things - bits for pri, ??? prioritisation, strict priorities

Belshe: 3 unique features - priorities, chains, groups

Jeff: if can reorder pri can the dependencies graphs/groups/etc be implemented
in browser layer by telling the protocol layer "re prioritise this stream"

Roberto: we discussed that and the implementation gets complex

Belshe: tradeoff of complexity, simple approach - 8 priorities. 2 things
thinking of adding - dependencies & groups.

Will - one approach is get rid of priorities and just have groups of
dependencies

Hasan - a weighted set of ordered dependencies

Belshe: what is use case that needs dependencies

Roberto: ???

Martin: What are you proposing we go in protocol?

Roberto: increase size of pri field to size of streamID so can put streamID in
there.

Will: and if you are new group of dependency chain that field is used as
weight

Mark: priorities is between roots? 

Answer: yes

<whiteboard discussion of proposal for weights with linked equivalency classes>

Mark: 3 things we have here:
- Expanding pri bits
- grouping
- re-prioritisation

Roberto: difficult to split up

Mark: is there something we can put in spec as experiment?

Roberto: can send proposal we have done in SPDY-DEV.

Mark: for me grouping seems attractive, re-pri seems to add tremendous amount
of complexity.

Roberto: but we didn't get to talk server push yet as that is a big motivator
for it

Mark: Document - complete proposal, use cases and how to use proposal in an
experiment?


Server Push
-----------

Will: not happy currently because chrome implementation is buggy so we don't
have much data/experience but I think server push has many motivating use
cases.

Hasan: server push is something we have already presented & clear on
motivating use cases and there is some agreement on the use cases. Now we need
to really implement & get some data to figure out how to move forward.

Jeff: we have use cases, reason we haven;t rolled out is it is buggy in chrome.

Roberto: everything before SPDY4 will be buggy because server push consumes
its own stream. Let's assume no more than 100 concurrent streams. Let's say I
want to push 125 resources, I can't. that's stupid because when I'm pushing
I'm generally doing it in sequence so max concurrency is 1.

Jeff: for Roberto's use cases want pushes done sequentially and that is broken
in spec. parallel pushes works fine.

Belshe: that is a pretty small bug, you made it sound like the whole thing is
broken.

Mark: I'm concerned because we seem to be slowly adding a whole bunch of new
control frames (not just for server push)

Belshe: one issue: do we want to reserve streams in advance?

Hasan: reserving request resources.

Jeff: <some stuff I missed>

Mark: that's clearer don't bother sending that request

Hasan: we would remove Associated-to from SYN_STREAM to PUSH_PROMISE

Jeff: like this idea. Can we take the no-op stream id for it?

Mark: Hasan to write a proposal for PUSH_PROMISE

Mark: I was unsure about push, as were other folks, e.g. web spider may not
want to have resources pushed at it, but alternative is often server inlining
and client can always squelch the push.

Patrick - some people on client side are worried about it because they pay by
the byte.

Hasan: two use cases: 1) client in australia & I don't want any push at all -
set max stream limit to 0 for that endpoint. (2) e.g. you're pushing me the
yahoo front page image & I already have that cached from a different roaming
connection, client gets push_promise and client can cancel that. There may
already be things in the socket buffer at that point

Mark: you say 1 RTT but in Australia that can be quite large.

Mark: I was circumspect at the start but you've mostly convinced me. Have
google/yahoo guys talked to their web spider guys about this?

Hasan: web spider at google doesn't currently spider over SPDY, secondly it
is easy to turn off (send settings frame with zero)

Mark: those sorts of changes need to come across so we can look to incorporate
them in the HTTPBIS spec.

ACTION on Will - Double check directionality fo max streams has made it to the
HTTP/2 spec.

Mark: I want to optimise further for cacheable content and how to handle if
that content is already in cache.

Mark: there are some people who feel web arch is based on resource being the
atomic unit of authority, so I might have different resources on server that
can't speak authoritatively about each other. There is another whether unit of
authority is same origin. You're going for latter model for server push, so we
need to fly that around a bit.

Roberto: push into cache, which is temporary cache which only exists for the
context of the document.

Mark: I don't think that's spec'd out yet. We need to make sure the security
properties are OK and clear. including way it is & is not reused - we need to
write that down properly.

Need to Note somewhere (in the spec?): We need some text for security
considerations around security model etc. for server push.

<discussion on what implementations of server push there are>

Conclusion: No one wants to kill server push but some concerns over
implementation complexity

Mark: what is minimum bar to get first HTTP2 draft out that folks can
implement for experience.

Privacy/settings - <missed discussion>

ACTION: Mike to make proposal on list 


Next Steps
----------

Began with discussion about stablization of the drafts.  Need to set
expectations that things can still change.

Discussion of SPDYv4 and  migrating features into HTTP 2.0 drafts.

Martin made the comment that the base could be used to experiment.

Unless you're changing formats.

Word alignment and sizes need to be adjusted.
Uniform length between control and data frames.
Roberto pointed out that you don't get word alignment with adding type.

### Proposed reorganised header

Length 16, type/pad 8, flags 8, c/d 1, stream id 31

Magic for the front
Martin has picked a random number

Roberto has given Martin a pointer to PUSH PROMISE control frame

Session flow control

How to turn to off push (in either direction)

Prioritization - just create a 32 bit priority field with MSB reserved.

Rajiv: what sort of changes can we expect beyond this draft?

Mark: there will be more changes

On Magic:

Magic will be sent in all cases, and will include a high order bit set,
as well as versioning information.
Eliot / Martin to start something on the mailing list.  version name to
start "http-draft-n/2.0".
Purpose of magic is primarily to fail quickly on middle boxes that
improperly respond to upgrade

Mandatory settings in front.


Timing
------

A few weeks to get the proposals shaped up

Decision needed on compression within a month

Late March for implementations

Use github for draft development

Discussion about whether everything on the list of things for the next
draft is necessary to test now.


Data to Gather
--------------

We need to discuss what kind of data we want to collect.  What questions
do we need to ask?

Header compression: collect state overhead, compression efficiency. 
Different platforms (desktop v. mobile)

[long list from Mark]
Mark would like a draft or a wiki entry about specific metrics.  Will
is willing to provide information about what is possible.

Hasan-
- errors specific to http2.0
- reset stream errors
- goaway errors
- is there garbage at the end of the frame?
- improper interpretation of diagnostics that are sent.

Hasan to send a proposal to the list.

What to do about 100/continue?  Mark will take this to the list


Testing - conformance & interoperability
----------------------------------------

Clients, servers, and intermediaries all need to be tested.

-- adapt wireshark plug-in - Hasan will submit the code to the tree. 
Hoping from support from those folks.
-- we need a standalone python tool.
-- netcat-like tool -Roberto will do the netcat-like-thing!

Roberto: We need a catalog of example sessions
Jeff: we also need error cases

Jeff has some open source java code that we could borrow from that is
based on SPDY3.
Mark is going to write up some stuff in python.

Intermediaries are hard because you have to simulate clients and servers.

Roberto: would be nice to have a stupid server that just tests  PUSH


Schedule
--------

Discussion of the value of another Interim.

When?  September-ish

Where? Melbourne/London/Toronto/Boston/Berlin


Other Business
--------------

### Challenges Deploying SPDY - Rajeev Bector

- World is very heterogeneous
- Fragmented serving architecture
- All have different software, management, etc. This is a small and big
  company problem.
- There is very little SSL in many parts of the world.

We're going to need to live with HTTP/1.0/1.1 and 2.0

Operational/administrative/technical reasons drive a separation between base
html and CDN content in many sites.

How do we leverage next generation of the web without waiting for people
to re-architect for SSL?

Wildcards have problems with 4-level domains; pages having lots and lots of
domains.

As a transition mechanism, serve base page over HTTP and then CDN
content over SPDY.

Mark: What signalling needs to be available up the stack to indicate
which version of HTTP is being used?

People would rather not sniff the UA, because it's getting more difficult

One possibility is to optimise content for SPDY, but then you need a
header or something for that.

Roberto: how about a server declaring that a bunch of domains are
equivalent.

Will: but you need a bootstrapping mechanism.

Roberto: wildcard dns?

Rajeev: you take a performance hit...

Mark: we need to address this as a transitional problem

Roberto: focus on mixed-mode use case.

Will: Issue is really getting http into the address bar.

One solution: send an HTTP request to a SPDY server and respond with
Javascript to rewrite.
