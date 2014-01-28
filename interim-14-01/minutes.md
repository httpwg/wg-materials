# HTTPbis Working Group Interim Meeting Minutes

22-24 January, 2014 - Zurich, CH

Chair: Mark Nottingham

Participants:
* Eliot Lear (Cisco)
* Martin Thompson
* Leif Hedstrom (Apple)
* Gabriel Montenegro (Microsoft)
* Peter Lepeska (Viasat)
* Brian Raymor (Microsoft)
* Rob Trace (Microsoft)
* Hasan Khalil (Google)
* Roberto Peon (Google)
* Will Chan (Google)
* Patrick McManus (Mozilla)
* Shigeki Ohtsu (IIJ)
* Salvatore Loreto (Ericsson)
* Herve Ruellan (Canon)
* Bryan Call (Yahoo!)
* Hirotaka Nakajima (W3C)
* Jeff Pinner (Twitter)
* Dan Wing (Cisco)
* Barry Leiba (Huawei)
* Emile Stephan (Orange)
* Alexey Melnikov (isode)
* Eric Rescorla (Mozilla)
* Dan Druta (AT&T)
* Jeroen de Borst (F5)
* Adrian Cole (Square)
* Richard Barnes (Mozilla)
* Dan Sun (Verizon)
* Saurabh Kulkarni (Akamai)
* Stephen Farrell
* Sean Turner
* Brian Smith (Mozilla)
* Daniel Stenberg (Mozilla) (remote)
* Julian Reschke (Greenbytes) (remote)

## Wednesday

### Issue 339

Jeff proposing to have one Huffman table rather than 2

Roberto: better compression when separate tables for requests and responses

Is this discussion worth breaking the schedule?

Jeff: symmetric is good for push

Patrick: not much time left

Adrien: prefer one or sepate table for cookies.

Jeff: propose -06 with one table, -07 with separate cookies?

Consensus is next implementation draft will be one table for request response
and one table for cookie and set cookie. Base 64 encoded table.

Patrick: Should we consolidate HPACK into HTTP 2 document?  

Mark: Table this discussion until tomorrow.
 
### Issue 340 and 341 (related)
 
For 341 add a new opcode in HPACK to signal table size change.
One drawback is that it will make changing to a new compressor difficult.

Roberto suggested a new frame instead of opcode

Roberto OK with Inline

Adrien: +1, this moves the responsibility inside of HPACK

Herve: would like to keep issues to empty table without resetting size

Herve/Roberto to write up changes

This allows closure of 340.
 
### Issue 220
 
Request to stay away from this.

Do not have time for HTTP 2.  Close.
 
### Issue 335

Will: What should the browser do?

Use a heuristic to wait and then close and re-connect

Suggestion that max streams = 0 is page error

Proposal 1 is to add text to clarify max streams = 0

Browsers will have to determine how to interpret.

### Issue 95

Hasan: Extensions, are highly desirable.  Could prevent future versions of SPDY

Will: Can do extensions over ALPN?

Hasan: there are a lot of use cases.

Martin: cannot do ALPN because proxies may drop connections. Extension frames
could be stripped without detrimental effects on protocol.

Use blocked resource extension for trial extension.

Rob, anyone interested in creating test cases for extensions?

Defer consensus on Mike Bishops draft until tomorrow.

Homework for everyone.
 
###  Issue 119
 
No interest in implementation for this.  Closing.
 
###  Issue 184
 
Jeff: No matter what, server has to deal with DOS and the race condition for
shrinking window.

Roberto: Close the issue and deal with it down the road if this is a real
problem.
 
###  Issue 323
 
Room generally OK with the change from HTTP2.0 to H2.

Not a significant problem either way.

Dan:  how do we deal with HTTP 2.1?

Room: use major versions for new protocols.
 
### New Issue - Padding
 
Adding padding to HPACK for CRIME prevention

Need to be able to pad both headers and body for requests and responses.

Padding must be respected by flow control
 

## Thursday

### Issue 350: END_MESSAGE

Pinner suggests that this is something useful for layering message-based
protocols on top of HTTP 2 framing. Useful when using HTTP 2 framing with a
different negotiation mechanism (different ALPN string) but without having to
adapt the framing layer at all.

### Server Push

Lots of people trying to convince themselves that this is useful.

### Issue 207: Numerical constants

Let's make these contiguous. Decided to do so just before next draft cut.

### Issue 352: Require flow control

Pinner suggests that END_FLOW_CONTROL is bogus. Implementations will get it wrong and hide it, otherwise. Consensus on this point.

### Issue 351: Comma and NUL for header splitting

Thomson proposes using comma just like HTTP 1.1.


## Next implementation draft

Suggestion is draft10 after this meeting.

## Next interims

Nottingham suggests one-day interim Saturday following London IETF.

Nottingham also suggests another interim in northeast US around June 5-6.

### Issue 270 Prioritization

Chan suggests the same old scheme he's been suggesting all along.

Pinner discusses synchronized state.

### Issue 95 Extensibility

Hum was 50-50.

Decided against. Unhandled SETTINGS MUST be ignored, though.

### Issue 356 THE SETTINGS ARE TOO DAMN HIGH!

Thomson says there is lots of wasted space in SETTINGS. Let's fix that.

### Issue 350 END_MESSAGE again

Now that extensibility is a non-starter, Pinner is pushing this.

Still undecided.

## Friday

### Padding

https://github.com/http2/http2-spec/issues/344

Thomson: Intent to specify what padding looks like, but not how to use it,
beyond some security considerations

Turner: Need to provide advice that will prevent the really bad stuff from
happening

-- Will find someone to work on writing this

Pinner: There is also a concern about intermediaries changing frames / padding

Peon: Here be dragons

### Massive headers in DoS considerations

https://github.com/http2/http2-spec/issues/343

Peon: Would be nice to have a solution to bound this problem

Pinner: Client can send tons of headers, but not sure why it's more than othe
DoS

Peon: Comes down to knowing the client is malicious or not

Pinner: This isn't really Security Considerations, it's just DoS

Rescorla: Seems worth documenting how http/2 has worse DoS properties than
http/1

Thomson: On balance generally better, but there are some cases where it's worse

### Cross-origin policy for pushed resources insecure

https://github.com/http2/http2-spec/issues/248

Nottingham: The point is that the server needs to respect cross-origin
restrictions

Peon: Browsers should not accept push except as authorized

Nottingham: There's a latent issue about connection coalescing generally

Peon: Need to say that no gateway should allow a push that's not authoritative

McManus: Current text is different for "http:" and "https:", ok with that?

Wing: Generally, "if you would go to that host for the resource..."
-- Covered by additional text in 10.4

### User experience for TLS

https://github.com/http2/http2-spec/issues/319

Eliot: Russ and Hannes brought this up in the IAB, but it hasn't gone very far

Rescorla: Don't see any difference from the situation in http/1

Nottingham: Might get something from W3C, but haven't heard anything

Pinner: Why is this issue here?

Nottingham: Mainly as a placeholder in case we want to reference something...
but none are emerging

Rescorla: If there were something, it would be WEBSEC, not this

Turner: It's out of scope

Closed with no action; mnot will let W3C know

### Baseline for TLS profile 

https://github.com/http2/http2-spec/issues/172

Thomson: Compression stuff could go here

Turner: Changing TLS is out of scope, profile all you want

Rescorla: Could have (1) mucking with TLS, (2) general recommendations, (3)
specific HTTP recommendations. Would hope things would be more general

Pinner: We already have some http-specific things (v1.2, etc.)

Thomson: Were looking for advice on whether some more generic things were being
worked on elsewhere

Turner: UTA is trying to add 

Rescorla: What is AD guidance for draft-sheffer-tls-bcp

Farrell: Just want it done

Rescorla: Suggest referencing that, and we'll get it done soon somehow

Nottingham: Normative or informative reference?

Thomson: If it's standards track, normative; start with informative now

Peon: Might be lacking an error code for "you're violating the minimum security
profile" ... to deal with cases where you can't reject at TLS layer or want to
provide more info

Pinner: But the server would have to be non-compliant in order for this to be
useful

McManus: There are still cases where this could be helpful

Nottingham: Reference draft-sheffer-tls-bcp informative or normative. If people
have problems with that draft, go to the relevant WG

Rescorla: Keep in mind whether you want additional restrictions for http/2

Nottingham: Do we have a timeline?

Rescorla: Would like to have it adopted by London, done by EOY

Nottingham: Need it faster; probably going to IETF LC with this by Toronto

Rescorla: Current major issue is around EC recommendations, might just get
deleted

Lear: Is the intent for draft-sheffer-* to start using normative language?

Turner: Not really necessary

Pinner: So do we need to update our recommendations?

Thomson: Need to say "Do that, AND ..."

Nottingham: Should we go ahead and require 1.2? Will that rule out
implementations?

Thomson: Every stack has 1.2 in it

Rescorla: Are you saying that if you offer ephemeral and server selects RSA,
you should fail?

Pinner: Yes

Turner: Don't worry about timeline; if http/2 needs this, we will get it done

Nottingham: The only thing I'm concerned about is the IPR stuff ...

Nottingham: How detailed does this need to be? 

Pinner: "Ephemeral ciphersuites with no compression", then people can figure it
out... think draft-sheffer-tls-bcp has more details

Rescorla: Maybe just set a security level

Smith: If we're going to allow non-EC, need to set a security level

Chan: Need some recommendations about how to deploy EC

Pinner: Think AGL's problem was that things might not be really ephemeral if
you use resumption / tickets

McManus: That sounds like an issue for draft-sheffer-tls-bcp

HUM: Should we require ephemeral?
    -- Require them: Fairly strong
    -- Not require: None
    -- Doesn't know / care / need more info: one

Nottingham: Pretty strong consensus

Thomson: Will make a pull request

Smith: Allow TLS false start?  Assumed OK, but not explicit

Rescorla: In favor of reducing RTTs, but have gotten a lot of static from
security folks about false start; e.g., Matt Green thinks it's terrible...
this is a bad moment in history to be insufficiently careful with TLS

Smith: People are looking at SPDY implementations that can do false start

Rescorla: Would be OK, but just want to note that it's not a no-brainer

Peon: Worth a try

Rescorla: Could say that servers must not choke on false start data + [big
warning box]... don't reference false start, just say they must accept/buffer
application layer data
    
[[ morning break ]]

Nottingham: During the break, there was some discussions that requiring that
tolerating false start would mean servers had to implement false start

Rescorla: Not really quite the same

Trace: IE does false start by default, and there's not some massive
blacklist... >90% success rate

### TLS Man-in-the-middle

https://github.com/http2/http2-spec/issues/317

Nottingham: Is there any activity to mitigate this?

Barnes: CT can help...

Rescorla: The clients permit this by continuing even in cases where it can tell
that there is a MITM

Chan: There are cases where we can't tell

Rescorla: If the client does its own cert validation, then the client is always
aware of a MitM. If MitM certs chain to a normal TA, that's bad, and CT can
detect that; if not, then the client has to explicitly override pins

Smith: Might recommend being careful about caching things where there might be
a MitM

Nottingham: We were liberal with opening security issues after Vancouver; can
close if we want

???: MitM is ultimately going to be an issue for http/2 deployment

Smith: Caching and connection coalescing could both be affected 

Nottingham: Do we want to specify coalescing in http/2 more closely than http/1

Smith: Better to open it and gauge interest

Nottingham: Will open

Peon: Think this is pretty well specified alerady

Thomson: "You can coalesce if [TBD]" <-- should say something about that

Peon: Don't think these things will close in the next years

McManus: Could we have just some informative text?
    
### HTTP2 and http:// URIs on the open Internet

https://github.com/http2/http2-spec/issues/314

Thomson: There's been a huge confusion of terminology on OE

Peon: What we say here doesn't really matter, it's what clients implement

Chan: But the spec might affect what clients implement

Nottingham: Asked for proposals a long time ago. The only proposal so far is
status quo. Are there other proposals?

Pinner: Our proposal is that HTTP2 is only over TLS

Chan: Would agree if there were any chance of that succeeding

Thomson: Nobody is going to be willing to *remove* HTTP/1.1 for "http:" URIs

Peon: This should not be a security question, just an interop one... there are
various negotiation mechanisms; don't really have one for this right now

Trace: Disagree, multiple implementations of Upgrade

Peon: Regardless of whether an HTTP URI gets carried over TLS, it provides no
reliable security benefit

Peon: If we close with no action on this, then we'll need to open another bug
to describe how "http:" requests get sent over TLS

Rescorla: That would be broader than HTTPS-only; anyone want to stand up for
that?

Smith: Think there's some value in considering HTTPS-only

Pinner: HTTPS has other baggage than TLS; happy to be TLS-only, but not
HTTPS-only

Smith: Any time we say we're going to prefer HTTP to HTTPS, need to think about
why

Peon: If you have a TLS connection, there's no harm in carrying HTTP over it

Smith: If HTTPS referer stripping is a problem, we need to consider revising
the web security model to make HTTPS more usable

McManus: There are other examples of how HTTPS does different things beyond TLS

Nottingham: So it sounds like we want to allow http:// requests to go over TLS
Pinner: Yes

Nottingham: Please raise an issue

McManus: You said that the sense of the room was supporting but not requiring,
test that?

Thomson: Conclude that http:// URIs are allowed over TLS connections?

Chan: OK with this, as long as it's not a security thing

McManus: Thought you wrote a blog post that said Chrome wanted http/2 for
https:// only

Chan: For http:// URIs, currently fine with Alternate-Protocol. Roberto's
proposal is different in terms of signaling

Nottingham: You're OK with http:// over TLS as long as they don't change
security context?

Chan: OK with what we have in Chrome right now, which is largely the same

Julian: Sounds like we are using http:// over TLS not for security reasons but
upgrade reasons; what does that mean when the certificate check fails

[General acclamation]: We'll get to that later

Rescorla: Confused now. Seems like we're doing some that has security value,
but we're pretending that it doesn't

Trace: From a user's perspective on the box, http:// origin over TLS cannot be
trusted

Rescorla: This is going to be relevant when we get to unauthenticated

Nottingham: Think we can close this issue with no action, because we're not
going to constrain how http:// URIs are done in http/2

Rescorla: Thought Brian was still hoping for https:// only

Smith: [[ missed ]]

Pinner: Separate drafts for Upgrade / Alt-Protocol, etc. vs. the wire format of
the protocol

McManus: There's a certain attraction to that, but what's in the main doc tends
to get more attention

Pinner: There's going to be a lot of variation in what gets implemented

Nottingham: Maybe describe Upgrade in the base spec?

Smith: If there are a lot of implementations of Upgrade, may not be worthwhile

Lear: Specs that don't tell you how to get to it tend to not do well

Rescorla: Understand we are closing the issue of whether it's OK to use http://
URIs at all

Nottingham: http:// URIs can be used with http/2, in the clear and over TLS

### Orphaning http:// URIs

https://github.com/http2/http2-spec/issues/320

Nottingham: Closed in light of prior discussion

### Opportunistic Encryption

https://github.com/http2/http2-spec/issues/315

Rescorla: 1) http URIs always over TCP 2) http URIs can go over TLS w/ cert
checks. 3) http URIs can go over TLS w/out cert checks

Peon: There's also a question of whether it needs to be signaled

Nottingham: Who thinks we shouldn't be walking down this road?

Chan: Fine sending http: URIs over TLS in certain circumstances

Trace: Value in specifying this; as you look to convert promises in encrypting
all traffic... MS has not formed a strong opinion about this one way or
another... good with specifying this as long as it's not required

Chan: Some concerns about specifying it... Main concern is getting people to go
all-HTTPS

Lear: What change is being proposed to the spec?

Khalil: People are going to want to be able to force http: requests off of TLS
... if there is a mechanism for a server to indicate that, people can opt out

Rescorla: We've discussed several discovery mechanisms (1) Alt-Service, (2)
implicit discovery (speculative TLS), (3) implicit with force down

Khalil: No, this is an enhancement to any discovery mechanism

Rescorla: If you pull up a TLS connection and send a request with an HTTPS URI,
would this message be useful?

McManus: Alt-Service can point you to other places, load balance, etc.

Khalil: You can only send http: URIs to an https: host if you are already
speaking http/2

Nottingham: I've never spoken to you before, and I have a URI, what do I do?

Khalil: One possibility is to just try to open an http/2 over TLS connection

Peon: And use http/1 as an alternative

Pinner: And this only works with default ports

[[ Concern about unnecessary probing, ]]

Khalil: Suppose you're in an environment where you have an http/2 over TLS
connection...

Nottingham: OK with that, as long as refusal gets pinned

McManus: Getting too many connections from the Internet is water under the
bridge

Pinner: Need to have a way to do this for domains that don't have HTTPS

Peon: If using http:// URIs has additional cost, that might be a good incentive

[[ clarification of topics to discuss over lunch ]]

[[ Lunch break ]]    

#### Recap

Nottingham: Will not constrain the set of http:// URIs over http/2

Rescorla: Thought we said TCP was OK, still discussing TLS

Nottingham: We agreed there were no MUST NOTs; discussing whether we define
http over TLS now

Nottingham: Is http: over TLS something we should specify at all?

Chan: Maybe. No unauthenticated, maybe authenticated... Chrome has implemented
HTTP URIs over authenticated TLS... like it as a deployment strategy, but can
be a hindrance for HTTPS adoption

Rescorla: Why don't you like unauthenticated?

Chan: Downgrade attack

Rescorla: If this is only deployment, why does downgrade matter?

McManus: For you as an individual, this is not a security feature; for the
Internet, it is

Jeroen: For middleboxes, would like to have an indicator of auth vs. unauth

Khalil: Let's discuss discovery first, since it will bound a lot of these
problems

#### Discovery

Nottingham: Encryption in HTTP/2?  Anyone want it?

[[ nope, off the table ]]

Existing connections

Khalil: Login page / 1x1 image for bootstrap

Rescorla: You could also be speculative

Peon: That's different

Khalil: I look at existing connection sharing as an add-on to Alt-Svc ...
http/2 servers operating on TLS connections MAY receive http: requests ... they
MUST respond with a response or an error code

Nottingham: That's a concern if adversarial parties are on 80 and 443

Smith: HSTS already sort of depends on those folks not being adversarial

Nottingham: So if you own port 443, you own the domain

HUM: Comfortable with existing connections as a starting point -- Many in favor

Rescorla: Surprised that Chan is not humming against this

Chan: You're saying you MAY do this, so OK

Rescorla: Anything between MAY and SHOULD doesn't matter, we expect people to
use this

Chan: Is this the "opt-out" approach? Don't think we should default to making
people opt out

Peon: As stated, a browser MAY do this. Some may decide to use opt-out, others
not

Rescorla: But the server has to always opt out, since the browse MAY send http:
over TLS

McManus: Could also have server opt in

Trace: As a server implementor, I like that

Khalil: I'm fine with having an opt-in bit

Pinner: But you have to have the opt-out too, because clients can disobey

[[ stopping more detailed discussion, to return later ]]

Peon: A client may send an http: query on an existing connection iff settings
have been received and settings indicate that http: is OK

#### Speculative connection

McManus: If I did this, how would know I wasn't doing existing connections


#### DNS

Thomson: There haven't been any concrete proposals for this

Rescorla: Future-proof: "settings frame or other to-be-defined announcement"

Nottingham: We might need a frame that says "I am authoritative for X"
    -- [[ not for us ]]

#### Alt-Protocol / Alt-Svc

Trace: As specced, there's some stuff I object to

McManus: Rename to "routing information in an HTTP header"

Pinner: If I send this in a 301 to the same URI, browser will reconnect over
http/2

Rescorla: Two transitions here: 1) http->https -- this is just 302. 2)
http->http over TLS

Rescorla: What are people not liking about what Jeff is saying?

Smith: Feel like you're trying to change the security model. Suppose the
browser doesn't speak http/2 at all, then it's plaintext

Pinner: I don't have to support plaintext... simply asking how this mechanism
would have clients behave

Rescorla: How do you distinguish between IE6 (no http/2) and Firefox?

Pinner: Might say that we don't serve IE6

Peon: Hear Jeff saying that he needs to advertise "I accept http-schemed
things" and have the client follow that instruction

Thomson: This is refusal, as above.  

Smith: Feel like you're changing http/1 semantics

Nottingham: Seems like there's interest in an in-band hint. Should be optional
for the client as to when they use that hint

Chan: If this becomes the "flip this bit for more secure HTTP", that deters
HTTPS

Farrell: Any data behind that assertion?

Chan: No, just assertion -- just like the claims of benefit

Chan: Like in-band stuff in terms of interop. Concerned that people will use it
for privacy reasons. Pointing out cost, not saying that it overwhelms the
benefit. Seems like rough consensus among Chrome team is that there's no net
benefit

Rescorla: So even if we do have a definition of http: over TLS... but there's
no way to get there in practice

Nottingham: Authenticated / unauthenticated. In the alt-protocol model, you
don't need to be authenticated if it's on the same host

Smith: Which server operators are interested in using unauthenticated?

Peon: They're not here, because they're the long tail

McManus: You see tons of comments on blogs about not wanting to be on the PKI

Peon: We could do auth-only at first, then add unauthenticated later

Pinner: Would a self-signed cert with TACK/Constellation count as authenticated?

Rescorla: Authenticated == valid for HTTPS, same for say, DANE

Smith: Wondering whether people want to also consider a new way of doing 
authentication. Like TACK

Rescorla: Those would apply to HTTPS as well.  It's orthogonal.

Peon: The only option that allows us to continue to rev the protocol unmolested
is auth-only

Rescorla: This is an advisory mechanism anyway, so you can take it back

Stephen: We're at like 30-40% of the web with certs that verify
... if the interop mechanism are important, you need the other 70%
... if someone is arguing for auth in order to get interop, that's not true

???: We're a service provider, and SSL is raising load times. Would like to
optimize the traffic that the content provider wants us to optimize. If it's
plaintext, it says "make me faster". Unauth could be the flag that says "I want
some protection, but I don't care". Deploying TLS move forward proxy functions
into reverse proxies. That's suboptimal; you don't know my network

Thomson: Why would we block any effort on alternative auth?

Farrell: The other point on alternative auth is that 100% PKI coverage is also
magical

Rescorla: Would like to discuss unauthenticated some more. This comes back to
Will's cost/benefit. What will get the most deployed functionality we think is
interesting in a realistic period of time. Two different value propositions:
Better security, better deployment situations

Peon: Not true, because middleboxes

McManus: Think the extensibility question is mostly a corner case. The question
of how to get the other 60% is more important. If things are bad, we can un-do
it

Barnes: There is a trade-off, you lose the people that don't want to do PKI

Thomson: We had a long discussion on the list about signaling unauth. This is a
decision by the client. No need to signal, only helps the intermediaries

Chan: Lots of server operators don't understand authentication

Smith: This is all speculation about peoples' impressions

Farrell: The deployment of web PKI is not speculation

Trace: We don't have a desire to do unauthenticated. Authenticated is a lot
more likely

Gabriel: Another issue with unauthenticated is that servers trigger on TLS

Rescorla: Same problem for authenticated, since you're not checking scheme

Thomson: Also, use refusal to opt out

Nottingham: Are any implementors interested in experimenting?

McManus: We are experimenting, not yet in a mainstream build

Pinner: We are probably not

Thomson: Some browsers are not going to implement plaintext HTTP. If we don't
have support for http: URIs, we don't get network benefit; Even more so if we
forbid unauthenticated mode

Peon: I would beat Hassan if he attempted to do unauthenticated

Chan: We would probably not do anything more than we already have. Though
Stephen has a grad student interested in implementing in Chromium

Trace: Not a priority for us; focused on HTTPS + Upgrade

McManus: Not doing Upgrade, of course HTTPS, probably auth and unauth

Pinner: Might get a lot of interest from folks who are not here

Nottingham: Where we are right now: Not going to say anything about
opportunistic yet; Nottingham and McManus will continue experimenting; Will
make changes to create refusal mechanism


### Discussion of Proxies

Lear: IAB has a draft on filtering. Could see a lot of filtering if we're not
careful.

Druta: We have a need for proxying. Are there improvements in the protocol to
make this better.

Peon: Proxies have two main purposes: (1) object distribution (2)
filtering/monitoring solution spaces need not overlap

Lear: Some other reasons too

Peter: Service providers don't need to make the case and people seem to
understand why this is needed. This is already extremely easy for us. We can
work to offer some UI prototypes to make this clear to the user.

Druta: Need to address cascading proxies.

Peter: EKR said he could work on the plumbing.

EKR: Yes, we know how to separate confidentiality from privacy and also inform
origin server.

Mnot: ???

Smith: Would like to find alternate approaches for the network optimization use
cases. Shouldn't inspect where you don't need to inspect.

Peter: Maybe solve as many use cases as possible w/ alternative models. Proxies
may still be needed but shouldn't block dicovery of other models

Peon: My proposal didn't include discovery b/c I wanted to make it hard.

Mcmanus: Discovery is broken, but not sure we should fix it.

Smith: If people want to work through reqts, I would help

Druta: How do we address immediate need?

Smith: Don't see an acute need to fix problem right away.

Will: Same thing

Trace: Same thing

Mnot: Similarities to subresource integrity

Chan: Incentives still aren't right.

Mnot: Don't see how to disallow existing transparenty proxies

Chan: Neither do I

Peon: Not really urgent... no implementation experience at all

Mnot: This doesn't block HTTP2

Peon: More interested in solving CDN problem. In many cases physical security
of devices close to the user is less than that of the core data centers. How do
we manage the certs?

Thomson: Also want to outsource to CDN. Delegation...

Peter: Same problem with planes...

EKR: Problem here is that people can't guarantee what clients are going to do

[Discussion of whether people will adopt this type of solution or just continue
to do insecure stuff.]

Peon: want to terminate TLS close to the user.

Mnot: are people working on this?

EKR/Thomson: Matt Miller for XMPP