# HTTPBis WG meeting


## Tuesday

*Minutes by Paul Hoffman*

## Administrivia

Mark did agenda

Julian Reschke sugggested an additional topid

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
May want to take on Proxy.pac in the future. Can the proxy adverise
opportunistic encryption? Maybe not worthwhile

(?1): Could open to attack

Mark: Should publish this at same time as HTTP/2

## draft-hutton-httpbis-connect-protocol

Andrew Hutton: Use in the WebRTC environment

Martin: All we need is a TCP connection when fireall policy permits it. Be able
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
