# HTTPBis WG meeting

## Monday

### Adam Langley: [HTTP/2 and Proxies](http://httpwg.github.io/wg-materials/ietf90/agl-proxies.pdf)

In the beginning, we started SPDY with the question, "How do we get this going over the network?"

The answer was TLS.  67% of people could get through using an Upgrade: Header.  86% could use a different port.

"We came dangerously close of not being able to have an HTTP2"

These numbers were for Chrome on Desktop.

Crypto is defending the end to end principle.

"We can't build a sane Internet without end-to-end cryptography."

User-consent is a failure. You can't ask the user about questions they don't
understand.

Filtering is done on the client.

Installing a root certificate proves that you own the machine. We do not see
MITM proxies doing updates.

So long as they are they are detectable, we let it go.

Hasan: the numbers to get QUIC through were pitiful.

Parental control filtering is supported in Chrome at the end point.

General thrust of Adam's point: filtering doesn't break SSL/TLS.

(Mark smacked down someone with a kitkat.)

### Peter Lepeska: [Trusted Proxy and the Cost of Bits](http://httpwg.github.io/wg-materials/ietf90/trusted_proxy_cost_of_bits.pdf)

Internet.org says that the Internet must be 100x cheaper.

For satellite you need some form of "acceleration" to get a reasonable user
experience.

We're looking at a mobile browser marketshare map. Opera Mini dominates in
places where access is very expensive. So you need compression to gain access
at all.

But it's effectively a man in the middle. And so there's a tradeoff.

"Not everyone has the option of being a data hound." - Gigaom. Access is the
first thing you need. Then fast enough experience. And maybe then there's
privacy.

Encryption almost doubled last year. Within a few years at this rate the
majority of the web will be encrypted.

The #s would be higher if we included SPDY proxies.

Making TLS mandatory in HTTP2 should accelerate the curve.

In January, when Yahoo switched to HTTPS, their plaintext response quadrupled
from 4 to 16 seconds.

CNN with Google compression proxy is 50% slower than without.

Peter shows an example of a notification to turn on or off. They're working on
UI treatments.

Or we ship our users a CA and we are a man in the middle.

CDNs don't go far enough, because the caches aren't near enough to the users.
And they only cover those who use CDNs.

Randy: This isn't what people say they want.

Nathanial Borenstein: Users will say they will pay any price for security as long as it's free.

Ted Hardy: Opera Mini has similar architecture to Chrome SPDY proxy.
    
Peter: except that opera mini decrypts TLS.

### Salvatore Loredo: [Explicity Authenticated Proxy](http://httpwg.github.io/wg-materials/ietf90/ExplicitAutProxy.pdf)

We are not proposing HTTPS traffic.  Only HTTP.

Aim is to provide better user experience.

Detection of malware

Network operators can take into account network characteristics when they have
access to the content.

TLS is one way to have end-to-end cryptography, but there are others, including
object level encryption.

Traffic is increasing faster than we can upgrade capacity.

Regulated industry, and must respect privacy of data.

And so we need some building building blocks

1st building block is a proxy certificate.

We need a proxy discovery mechanism.

We need a mechanism to opt in or opt out of a proxy,

Ericsson is working with Opera to implement.

Yoav: If i take my mobile phone mobile, how does it do discovery, and what can
the user do to make an informed intelligent decision?

Sal: it would be in the access network.

Adam Langley: why would people implement this for only HTTP?

Peter: another way to do a SPDY proxy.

Peter Lepeska: HTTP URIs over TLS.

EKR: would this be to cover opportunistic security/encryption?

Sal: we're still thinking about that.

EKR: do you use a separate ALPN identifier?

### Mark: [Proxies in HTTP](http://tools.ietf.org/agenda/90/slides/slides-90-httpbis-8.pdf)

summarized "proxies are useful"

summarized "proxies  are dangerous"

The issue for me is going from a 2 body problem to a 3 body problem.

And now there are split browsers.

In HTTP we explicitly allow intermediaries to do things.

Changing proxy expectations and requirements and the nature of HTTPs would
overturn the current consensus.

We don't have to standardize that which we object to.

We usually mess up in policy.  Justify decisions on technical decisions.  

Let's enable the tussle.

But we can't change the nature of the protocol.

We do create law when we create these standards.

So what can we do?

Some of the outcomes may not be standardization outcomes.


### Discussion
    
Eliot: thanks presenters. Proxy.pac needs substantial work, not scalable

Peter Lepeska: If you're going to be an MITM proxy, you're not able to hand the
original cert back to the user. That's bad. Can we do something better?
    
PHB: saying that you're not going to think about an issue doesn't make it go
away. nervous about "we only do end to end"

Sean Turner: imagine the headline: HTTP enables man in the middle.

Joe Hildebrand: it might be possible to separate out these things from this WG
if we have appropriate extensibility in the protocol.

Ted Hardie: it's important to recognize the needs of the origin server to treat
information as confidential.

Cullen: there's a lot that can be done in this space. re compression, there's
nothing you can do to speed up a system where they don't care about it at the
origin. But caching is different and we should look at approaches.

mnot: W3C has sub-resource integrity, but there is pushback because it leaks
information.

Daniel Kahn Gillmore: Network operators should not get in the way of the users
having secure connections. The capabilities of proxies for legitimate purposes
are indistinguishable from those that are illegitimate.

Yoav: doesn't think that he could make an informed decision, regardless of the
UI.

Sumandra: is there a way to split that which requires protection versus that
which does not? Example: a movie. Possibly could do optimization on the exposed
data.

mnot: we've talked about doing frame-by-frame selection of encryption. The
feedback is that the complexity is unmanageable. More recently we've talked
about adorning TLS with some meta-information.

Joe Holland:  We do policy.  Maybe annotations might be interesting?

Roland Zink: concerned about devices without a UI

???: As a network operator in 60 countries we're under a legal obligation to
block certain URLs. How do we do that?

Adam Langley: That's censorship. You get the domain name in the clear, but you
may have a problem blocking individual URLs. What about SPDY proxies? That's
different. We've not gotten a lot of interest from proxy vendors in terms of
reducing the information they have.

Peter Lepeska: when the two ends say they don't want information decrypted,
then we don't want to decrypted.

Chris: anyone with a squid box can be a point of censorship, and can be gotten
around.

William Chow: tradeoffs and choices may be different for different parties.

Dan Druta: no one solution is going to fix all the problems and scenarios.
three body is already there, and perhaps it's 3, 4,5 body scenario. and
sometimes some of those bodies (or their intention) collide. TLS does not allow
for fine-grain control over flows, and there is a need for that.

Martin Nielson: this really comes down to who you trust?

PHB: clarification: it's incumbent on the advocate to prove they're not going
to make things worse. anything that happens should happen with the consent of
the Internet user.

Wendy Seltzer: want to introduce the notion of "affordances". don't give users
an option that will simply be turned against them.

Craig T: responding to PHB, + the content provider

Alissa Cooper: it's a mistake to think that users chose that browser for its
performance characteristics. Same thing for SPDY proxies. we're here because
encryption is increasing.

Chris Bentzel google: Have you seen that there are market forces at play where
users would go to different sites [based on performance]?

Hassan: do we know why opera mini is so popular? opera mini is pre-installed on
a lot of equipment by carriers. this is not a choice that people are making.

2nd: i've not heard any proposals for origin servers can have a say. google
would be disinclined to implement anything that doesn't take into account
origin requirements.

EKR: there was a proposal some time ago to take into account proxies, and it
was received in a very negative way. we have a difficult time sorting what the
user is consenting to and what is being done to his data.

Joel Jaeggli: on the market share #. looks like opera comes with the phone.

martin nielson: 10% of browsers installed with opera. main reason is not for
compression, but for caching.

Stephen Farrell: thanks for not breaking TLS. how could you use TLS and solve
caching problems? can we avoid the term "trusted proxy"?

Julian: intercepting proxies are much easier to deploy. maybe that is something
to work on.

Erik Nygren, Akamai: we need to be careful to separate http/https. We need some
reasonable compromise for HTTP.

Dave Nielson: Google's proxy is like any other proxy.  It can see [HTTP].

Hassan: Google's only being a little hypocritical. We're only doing HTTP URIs.
If you're running chrome, we can see what you do.

Julian: it might be useful to have a proxy users can choose in places like
Chrome.

Mark (summarizing): 

* HTTPS is inviolate
* Maybe some interest in opt in to soften that
* Some interest in adorning TLS
* Interest in normalizing what an intercepting proxy is
* Interest in encrypted caching.
* Open issue on how opportunistic security interacts with a proxy

Dan Druta: why isn't the proxy certificate a good building block? Maybe we need
a taxonomy for proxies.

Tony Hansen: We had OPES. RFC 3238 discusses OPES services in general. OPES is
all about proxying.

William Chow: servers today that want to support SPDY. TLS is used as a
reliability mechanism for SPDY as a primary consideration.

Sanjay from Verizon: operators need to be able to engineer their traffic, and
what is the balance between OE and network engineering.


## Tuesday

*Minutes by Paul Hoffman*

## Administrivia

Mark did agenda

Julian Reschke suggested an additional topic

WG has changed its home page - https://github.com/http2

Ted Hardie points out that pull requests need to see a Note Well

Maybe will do an HTTP FAQ

## Existing HTTP RFCs - Julian Reschke

Want to go Internet Standard in ~2016

Need to agree which errata should be accepted into the document

Mark wants to set up a repo for errata and things that need clarification

### RFC 7328

Can either publish a new RFC or ask or the status to be changed to Standards
track

Barry Leiba wants to just change without a new RFC

Rob Trace says that IE will look at implementing it

Mark: a decent amount of take-up

### RFC 5987

Non-ASCII for headers

Needs to be revised to work with the new RFCs

Private draft? WG draft? Barry prefers in the WG.

Mark proposes adopting with intended status of Internet Standard

Martin Thomson wondered why bother going to Internet Standard

Julian wondered why not

Timing: should this be done before bis-bis? Probably will wait.

### RFC 6266

Implemented in all browsers

Only tiny edits are required

Intended status of Internet Standard

Timing: should this be done before bis-bis? Probably will wait.

## HTTP/2

Discussion at interim in NYC

A few new issues recently

WG LC soon, but with a longer time than normal to help get implementation
experience

Issues were shown on the screen; Some new requests will be post 2.0

Martin: discussion yesterday what will be mandatory in TLS 1.3. Probably will
only be ECDH, not ECDH. Inadvisable to do something different than the TLS WG

Ekr points out that the two MITM lists are not the same

Cullen Jennings: If a fully compliant server does not interop with a fully
compliant client, we have failed

Martin: earlier versions of IE don't match what Firefox requires. Is hoping
that "yes we can find a way forward"

Mark: can we not say MITM but just good for interop?

Ekr: Doesn't know of any jurisdiction where there are restrictions against PFS.
Not removing stuff from the TLS 1.2 MITM. For TLS 1.3, PFS is your heartburn.
You have lots of options, ask your ADs.

Rich Salz: You're using a cipher name as a shorthand for the feature you want. Leave it at "ciphers that have these properties"

Mark: Just have an MTI for TLS 1.2, not 1.3. 

Martin: That would technically work.

Barry: You should align with the UTA TLS BCP document

Mark: We need to future-proof


### [Issue 526](https://github.com/http2/http2-spec/pull/526
)

Hervé Ruellan: Open issue. When the server sends a response, it might might
push several resources to the client that depend on the original request. This
is coming from Dash. How can a client use the priority information from the
server. Dash has not settle on how to do push

Mark: new feature changes on the wire format for this one 

Mark indicates that it will close with no action

Hervé might propose this as an extension

Mark: Will close everything out soon

Mark: Getting more operational advice

Mark: HTTP/3 is an interesting discussion, but not WG work within the next year
Let's work HTTP/2 out fully

## draft-nakajima-httpbis-http2-interop-survey

Hiro Nakajima: Figure out which features are and are not implemented. Will do
more complex testing, make a dashboard. Wants more feedback from the WG

Mark encourages client and server implementers to work with Hiro

## draft-ietf-httpbis-alt-svc

Went through open issues

Couple of implementers interested in this

Julian thinks the issues can be worked out offline

Beef up the use cases

Wants people who are interested to be able to do it with their HTTP/2

Editors will sit down together this week

Paul Hoffman asked if folks wanted to test all aspects, not just OE

Mark said yes

## draft-ietf-httpbis-http2-encryption

Has some naming issues

Let people experiment in August or September

How to deal with proxies: in a connection, outside, or let the client decide

Patrick wants the client to be able to choose; Deployment decision / political
decision

This might be something that proxies might want to use as well

Mark: Need to think about discovery

(?1): User agent may be associated with more than one proxy. Need to get
implementation experience from Google about SPDY proxies

(?2): May want do make a distinction of which proxy to use on a per-URI basis.
May want to take on Proxy.pac in the future. Can the proxy advertise
opportunistic encryption? Maybe not worthwhile

(?1): Could open to attack

Mark: Should publish this at same time as HTTP/2

## draft-hutton-httpbis-connect-protocol

Andrew Hutton: Use in the WebRTC environment

Martin: All we need is a TCP connection when firewall policy permits it. Be able
to say "This is a WebRTC flow"

Ted: The WebRTC WG can adopt this

Cullen: Needs a change to support this. This increases the WebRTC connection
rate by .2% - 1%. If you have two WebRTC clients and you add this technique it
increases it a small amount. What does this do to the performance of proxies?
After 1.5, it pegs the CPU. Operators will turn off proxies. Wants to change
response header to say "proxying OK"

Andrew: then no one will use this protocol

Justin (?): On Google Hangouts, 1% of the people coming through TCP come
through a proxy. This has been common practice in Hangouts, Skype, etc. If you
require this, no one will include the field. Wants the opposite: client tells
the proxy it is about to do. Cullen's cost/benefit is upside down

Ted: came to the opposite conclusion of Cullen. The header is omitted now: this
is a baby step

Ekr: The HTTPbis WG issue is whether or not the connection should self-identify
what would be done with the tunnel. Don't tell people to reject if you don't
know what it is

Cullen: Does this pose much hardship for the HTTP protocol?

Mark: No HTTP people have said that it's an issue. CPU-bound is not a problem
for proxies. Ill-intentioned people will continue to do what they do

Stuart Cheshire: Any client application can identify what they are doing.
Developers don't have an incentive to make their application work worse by
self-identifying

Martin: Wants to make the option available

(?3): Tunnel administrator will have a white list of what is acceptable to
allow through. So watch what you wish for

Martin: The person who lets this through will see the ALPN from the TLS
ClientHello

(?4): The only useful reason for this is to do QoS on outbound connection

Mark: We are seeing ALPN tokens used a lot, without much analysis of the
effects. Doesn't hear much pushback. Will take it to the list. Most concerning
is protocol evolution impact.

## Proxy discussion and history

Little desire for adoption

Eliot Lear: Wants to document in an Informational RFC

Mark: Wants it

Julian: Captures use cases

Dan Druta: So we don't have to do it in 10 years again

Mark: Adopt the document without sections 5 and 6

Eliot: We will revisit in 10 years

What are the questions?

Martin: Difference between a living document and an RFC

Eliot: If people are concerned about the consensus point, this could be an IAB
document

Mark: Do a bit of cleanup, call for adoption

## Header Field Parsing

Julian: Gave this three years ago. Most header field parsers are broken. Header
fields can be repeated. Had a chance to make the header fields more consistent,
didn't do that.

Mark: likes the idea

Other folks like it for other uses as well

## draft-reschke-http-cice

Julian: Content encodings are often gotten wrong

Ted: Has concern when this might appear in other places. Semantics are clearer
if it comes in 4xx, confusing if in 2xx (but possibly valuable). Prefers a
different status code

MarK: Different meaning in the request vs. response, makes him twitchy
