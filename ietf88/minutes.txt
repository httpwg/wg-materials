# HTTPbis Working Group Minutes

IETF 88, Vancouver


## Monday Session

### HTTP/1.x

#### draft -24 change summary [Julian Reschke]


#### IETF LC summary

Julian says, that the issues received were mostly editorial issues. All those
issues received were addressed.

Julian notes that editorial feedback from APPSDIR and SECDIR, plus IANA
feedback; no individual issues raised. Unless new issues come up, we are ready
to move on in the process.

Barry notes that they did a short IETF LC, so that they would have comments for
the meeting. The IESG will get plenty of time, to avoid hasty and unfortunate
reviews. Mid-December telechat targeted. After that, RFCs! And life will be
good.

Mark confirms for Barry that there are no document references which would cause
an RFC editor blockage.

Mark also approved of Barry's bowtie


#### LC issue discussion / overview

(too many hashes already)

##### #507 SHOULD vs ought to on integer parsing

Julian recorded this as a design issue because this hadn't be considered.

Roy is OK with MUST on the content-length, that's a framing issue. p5 is
different because it is an optional feature and if this fails, the thing breaks.

Barry is concerned that even for an optional feature, this needs to be defined
so that it can work. He is also concerned about this turning into a security
problem (integer overflow, etc...)

Mark: describes a cached 206 and the potential consequences of overflow in that
case. Agreement that this might cause corruption.

Roy: OK with MUST

Conclusion: Make both MUST.

##### #519 conneg + proactive and reactive

Roy: Henry has studied the use of 300 and 406 status codes and found that they
aren't used. This doesn't mean that reactive conneg isn't used. Roy thinks that
Henry hasn't read and understood the argument, and is instead arguing from the
TAG. Roy doesn't see anything that he can fix.

Mark: Henry may be suffering a misaprehenshion that reactive == 300, when that
is made clear elsewhere in the spec.

Conclusion: close, no fix.

##### #432 cacheability of status codes

2^31 for max-age currently, why not 2^31-1. Do we leave this as-is and have
this special case (2^31 exactly), or do we reduce the limit, or do we leave the
max off.

Barry suggests that once you explain it, you can do anything.

Roy: this is so arbitrary. We don't know why.

Stuart Cheshire: it's MAX_INT but probably a mistake

Roy: is't not a mistake.

PHB: this is NaN for integers, maybe

Speculation ends.

Stuart: change it

Mark: changes cause interop problems

Conclusion: we'll explain, but leave unchanged.

##### On 2119 language

Mark doesn't want to rathole on this, but notes that HTTP is using its own
dialect and using it consistently.

Julian notes that the fact that this is the issue that is raised most often, so
the spec must be pretty good.

##### -25 drafts

As soon as possible. Then IESG comments. Then maybe another iteration. Plan is
to reach the RSE in January.

((what was the 2147483648 issue??))


#### Issue #512, APPSIDR review

There is a 2147483648 (2**31) maximum for the delta-second value. APPSDIR
wondered why this wasn't 2**31 - 1. As this is a historical value (apparently
for creating a kind of NaN value for integers), decision is to keep it (to
prevent breaking existing implementation), but add a note about it.

### HTTP/2.x

#### Seattle Interim meeting summary

https://github.com/http2/http2-spec/wiki/Implementations

#### Draft changes and open questions [Martin Thomson]

#### Issue 1: Upgrade Mechanism

Mark talks about Alt-Svc, Upgrade
(https://tools.ietf.org/html/draft-nottingham-httpbis-alt-svc-00)

Mike Bishop: whether we do this or not, it's not something for the spec. Talks
about Upgrade and the feature not well known where the server can advertise
support for HTTP/2.0 (as well as responding to client requests to upgrade).

Mark got the impression that there were lots of corner cases with Upgrade.

Mike: The performance problem is actually worse if you need to create a new
connection.

Mark: Caching the information avoids that problem.

Mike: That's possible in other cases.

Stuart: Modular design requires separation. Performance often requires that
those barriers are broken.

Mark: Breaking the strong tie between locator and server is desirable,
particularly because the HTTP/2.0 connection could be long lived and parking
connections long term can present a problem for servers who need to offload
clients.

Dan Druta: concerned about lack of transparency.

Will Chan: the client is able to choose

Ted Hardie: there are a lot of potential corner cases here, and despite a
desire to avoid corner cases, it might be that you haven't avoided those. Maybe
we can talk about alternative services that are delivered at the same host.
That makes a lot of the problems go away. Separating same-host and
different-host might reduce the complexity inherent in the solution.

Mark: just a small thing, security considerations.

Ted: distinction is important between certificate of www.example.com and
certificate that is valid for www.example.com

Mark: Still thinks that the connection characteristics will require that later
thing.

Ted: HTTP/2.0 only, which might require new URI scheme

Mark: you had me up until you said "new URI scheme"

Gabriel M: Agrees with Ted, the CDN issues are not specific to HTTP/2.0.
Concerned about putting risk on our current schedule. For just the in-the-clear
upgrade, this doesn't buy anything over the existing (i.e., Upgrade) solution
in the draft.

Mark: issues with upgrade: blocking while upgrade goes

Ted: two ports on the same host is not something that we worry about, it's the
different host scenarios that cause concerns.

Gabriel: Origin issues

Gabriel: maybe this is another option for dealing with discovery of HTTP/2.0,
so that you can avoid Upgrade

Will: Channelling jpinner: this isn't in major deployments yet, but would like
to restrict this to stuff that people use

Will: maybe something more like ALternate-Protocol (no host shift) is
interesting.

Will + Patrick McManus: Chrome and Firefox aren't interested in HTTP/2.0 in the
clear.

Rob Trace: Microsoft is interested in HTTP/2.0 in the clear.

Mark: we're not ripping Upgrade, though we may if it turns out to be poorly
implemented

Mark: question is whether we want to bring alt-svc (or a reduced form) into the
spec in order to gain experience with it

Patrick: There are some problems in the draft; Patrick offers to help with the
draft

Patrick: There are a ton of corner cases in Upgrade. Two objections are: it's
not going to work, and it's not going to be secure.

Eliot Lear: Questions relate to the caching of the response, in particularm
when you start going HTTP/2.0 directly on some port, what happens when you move
location.

Mark: if you detect a network change, then clear your cache

Julian: Theory on why clients do not implement Upgrade: on other clients it
requires writing both HTTP/1.1 and HTTP/2.0 both, which for testing clients is
a big burden.

Roberto: this affects both HTTP specs, and it makes the most sense as a
standalone. Maybe you want to downgrade from HTTP/2.0 to HTTP/1.1

Mark: preparing for an adoption hum

Ted: maybe revise before continuing,

Mark: proposes that he and Patrick revise the doc based on the discussion and
the editors will add a reference to the spec for that.

Mark: call for input from implementers to determine if it is implementable and
addresses the issues

#### Issue 270: Priority Levelling

Talked about this lots. Might have to delay this one.

Martin: propose that we move this faster

Will: wanted to collect data that provides justification for the complexity;
unable to do this because SPDY/4 is vapourware

Mark: we need to get this soon, maybe we ship without a fix

Roberto: maybe an educated guess at what is best is better than nothing

#### Issue 95: Frame Type Extensibility

Martin: Issues around negotiation of extensions

Roberto: we want to be able to experiment, but we don't know about what those
experiments might look like

#### Issue 292: Cookie Crumbing

Mike: James Snell had a proposal around this

Mark: cookies were always special fro the outset, but we never documented it

Mark: some people didn't want to do this, but he wasn't convinced by those
arguments

Roberto: doesn't like NULL being treated specially

Mike: intermediaries might reorder

Martin: we can require that intermediaries preserve order

Roberto: it's easy, you decompress, then compress, but ensure that you compress
in order

Julian: why?

Mark: nulls are being used to concatenate headers into a single header

Roberto: nulls were one way to preserve order, double toggle ensures that you
can always control the order that headers are emitted by the decompressor

Roberto: if we do nulls, that shouldn't be a compressor problem

Roberto: we aren't likely to get any more data on this, so we should decide

Mark: AD?

Barry: are you assuming that cookies will be used the same way in HTTP/2.0 as
one [yes, transition]

Mark: maybe we should have a chat with Adam Barth

#### Issue 266: Strings in the compressor should be huffman encoded

302 to #304

Roberto: I added Huffman, but it's not negotiated and the way we do that is ALPN

Mark: why does this need to be negotiated?

Roberto: negotiation saves you from complexity

Martin: plunge the knife in and we can see if the patient squeals too loudly

Conclusion: plunge the knife in

#### Issue 216: Alternate Reference Sets

Herve':

Roberto: simple and better than the original proposal and it seems to
accomplish the goal

Mark: let's do it


## Tuesday Session

### ALPN review [Stephan Friedl and Andrei Popov]

Stephen Friedl presenting

WG member are encouraged to review and provide feedback.

Wan-Teh Chang: This won't work with session resumption.

Stephen Friedl: It will not work unless you renegotiate.

EKR: You can't change the cert and ALPN codepoints, but you can resume.

Michael Tuexun: Is there a reason you don't provide this for a general
mechanism?

SF: You need to register the name.

MT: I want some binary data in there, is there a reason you did it this way?

SF: We did it because the port number is not reasonable to have different

Roberto Peon: This is there to negotiate the protocol, of anything else would
be very strange.

Mike Bishop: There is another extension that can be used for passing arbitrary
application data, but I cannot recall the RFC number

(RFC 4680)

Sean Turner: If we're going to make it expert review, should it be only
security or only apps or some combination?

Yoav Nir: Expert review should be in security because it can be used for other
protocols.

Eliot Lear: When my mother offered chocolate or vanilla, I always took both.

Mark Nottingham: I was concerned about how registration works, but I think
we're ok there now.

### HPACK review [Roberto Peon]

Actions by the Security folk to review and analyze. Mark and Stephen to discuss
how to get adequate review, now that the documents have settled down.

EKR: Is it correct that the attack is effectively a brute force attack if you
can't guess the secret. Are you saying that is weaker now?

Roberto Peon: I'm saying that was weaker when you are using a stream compressor.

EKR: The minute you guess the entire thing you're done.

EKR: You are assuming the secret is a high-entropy value.

Stephen Farrel: Do we know someone good at analyzing it?

RP: There are a few people have looked into it. It was not about HPACK, but on
the general use of Huffman.

Stephen Farrell: What is the timeframe that an analysis is useful?

RP: It's always easy to compress nothing.

NM: For the WG, we wanted to finish this up by next year, and we're on track.
We are getting implementation experience. If we get this done by middle of next
year, and it explodes, then we'll have problems. But this is something we can
get fixed with HTTP/2.1 or its successor. This protocol needs to be easier to
version.

Stephen Farrel: So we really want analysis within the next six months.

Yoav Nir: This table needs to be in both the client and server, and needs to be
rather large. It's possible that the table might not be optimal in the future.

RP: We could just go with plaintext encoding, or we use another table or
version the protocol. We know that it's possible to transmit a new table, but
we're not sure it's really worhtwhile right now.

EKR: On the threat model, most of the chosen plaintext attacks have exploited
some functionality of protocol to repeated induce response. As you suggest,
cookies could use arbitrary entropy. What we need to be observant about is
other forms of data that are lower entropy that you can get clients to send
repeatedly, like credit cards, passwords, and PINs.

RP: I agree the smaller the thing the easier it is. If I have to guess a PIN,
then I think their security model is already broken.

EKR: We are changing the security model somewhat.

NM: I think it's worth explain our proposal on cookie crumbs.

RP: We're looking at breaking cookies, but it's not clear this is making things
easier or harder. If the encoder is naive and puts a small secret on its own,
then you've reduced the total secrecy.

Jim Rosekind: IFirst interesting to note that the uncompressed case calls for
the client to ask repeatedly, and some servers will get pissed off about that.

JR: Second thought is about using the static table. If the result took a data
set, and you run this numerous times and analyse the space you actually need to
explore.

RP: That was something the paper I talked about earlier, one could pare down
the state space based on the bits on the wire. It was a very small reduction --
it was still exponential.

Stephen Farrel:  I'm wondering if the headers would be impacted by this.
RP: One of the things about having a compressor like this is people might use
larger secrets, because the cost is less.

Paul Hoffman: I think you'll need to solicit for those reviews outside of just
security.

Stephen Farrel: Between us we should try to find some way of getting review.

Lucy Lynch: There are a lot of people around that have experience in this, but
not exactly in the same problem space.

Jim Rosekind: when you look at this pseudo random cookies that actually use a
pattern. Using a greater amount of entropy can reduce the benefit from huffman
encoding.

RP: With all due respect, you're wrong (-: This is generally base64 encoding,
so it's already reduced.

JR: You're right that is using a reduced input set, but the tables might not
favor some of the inputs.

YN: I thought one of the goals is to change to use binary encodings.

RP: We can't quite do that because of interop problems with 1.1

RP: Right now, the Huffman tables are different for requests and responses. The
differences are noticable, and we've have talked about using a third table for
cookies, but we haven't seen a good benefit there. We haven't actually seen the
compressiong being larger so far.

JR: It is much more plausible if you're using ASCII characters in unif ways,
but once you bring in the english language it gets easier.

RP: I agree but we haven't tried that yet for complexity reasons. We haven't
made an issue for that yet.

Martin Thomson: There's plenty of places that such things show up, not just
cookies.

RP: Part of the problem for attackers is you don't know where the secret is.

### Encryption and HTTP/2 + Opportunistic Encryption

 Mark Nottingham presenting

** NOTE: slides are _NOT_ on the materials page**

Ted Hardie: One of the big questiosn from yesterday was why would anyone want
an HTTP/2 connection that was plaintext. If we can go from two states to two by
eliminating the cleartext then we're in a better place.

#### Alternate Proposal for Discovery

Paul Hoffman presenting

Use DNS to determine if the server for http: likely has a TLS equivalent,
instead of using HTTP headers. The two are not necssarily orthogonal. This is a
mechanism difference, not a conceptual difference.

Phil Haram-Baker: In my proposal, you can find the information in DNS because
that's what DNS is for. The guidance could be used for multiple services.

MN: And that's why we described this in two separate layers. One is what to do,
the other is how to figure out if you can.

RP: We experimented with something like this a long time ago, and I'm not
interested in hearing about the mechanisms, but I'm much more interested in
knowing if this increases our overal security. I'm not sure this actually
increases the aggregate security. This third level might actually decrease
security because it confuses users. It might make people thing that
opportunistic encryption is good enough when it actually isn't. I used to think
this was a good idea.

William Chan: I talked to various people on the Chrome team, and there some
concerned about the relaxed mode. We're more interested in doing authentication
always, even for HTTP: I am quite excited for encryptiong HTTP URIs.

NM: I would love to have the authentication. If we can good get good
deployment, then it's great. From a se

EL: Concerned this introduces a new form of MitM. If yu have this header, that
now says you can use relaxed, a MITM can insert the header or replace a 301
with a header, and the server thinks it has an encrypted tab but is really
sending data through the MITM.

EL: Why would the attacker not just proxy HTTP, and I'm just saying this is
another avenue. I'm also not sure we understand the consequences of adding a
new primative about saying "don't bother to verify the certificate" and
confusion about unathenticated encryption versus authenticated encryption.

Salvatore ??: I am worried we are putting to many things together, and changing
things on the fly. It might be too much to manage.

NM: I think this is been kind of implicit in everything we do, because we might
be switching to a new connection protocol.

YN: I think there is value protecting against passive attacks. Active attacks
are 10x more expensive. I don't see much point in having authentication for
HTTP because we have HTTPS. Having encryptiong wihtout encryption has some
value, as long as user-agents don't say you've got protection.

Larry Masinter: I was thinking about cases where encryption might introduce
excessive overhead, and one is delivery of video. There is value in encrypting
the headers, though.

MN: This is a negotiation -- the client can request it, and the server can
offer it.

RP: It is incorrect to say there is not benefit to encrypting video. It is
useful for the content provider and for the distributer.

Tim Bray: I tell most people to just use TLS. For you information, the
arguments against encryption are becoming less and less convincing. I think we
should keep pushing the rock uphill because we're starting to win.

MN: One of the conclusions we have is whether server authentication needs to be
lumped in. Does that mean we push everyone to just use HTTPS, or is there still
benefit to HTTP.

Rohan Mahy: A lot of concerns are about what the user experience. To me it's
clear -- if you are doing HTTPS, then here's the list of things to get the
green locked icon. if it's HTTP, then there's no immediate indication. You just
do it, and not tell enybody about it in the default case.

NM: By the way, that's what's in the draft.

Alissa Cooper: We should think of this as a gift to users (-:

Ted Hardie: I like the idea of not giving the browesr a signal of opportunisitc
encryption. But users are not the only side in this. There are classes of
software that might provide a false sense of security. We can get a benefit,
but it might cost us some authenticated encryption, and that is a serious
problem. I think we should just do HTTP/2.o is always authenticated encryption.
If we can't get to server authentication always, then make it hard or hidden to
do opportunistic.

Brian Dixon: From the perspective of opportunistic, it should be acceptable to
use self-signed, but still require authentication. This might lower the bar,
but this might still be of benefit.

Patrick McMannus: People don't always have all the information about what the
protection there is if we rely on HTTPS only, so having encryption always is a
good thing. I think it's better to require authenticated, since we really just
get one chance. But if all we can really do is HTTP-relaxed, then it's still
moving the bar forward.

??: Most browsrs give you a place to enter certain configuration options on a
per-host basis. While I don't think we should expose this to users, but I think
there is benefit.

Johan ??: I'm a little skeptical of doing encryption at this level. Especialy
as it plays with DNS.

Richard Barnes: Unauthenticated encryption is the new plaintext. This means
that the worst case is that you are protected from passive attacks. We should
shoot for authenticated encryption. If our goal is to increase the number of
places that authentication and integrity protection is increased, I'm not sure
these goals get us there. If we require authentication, it means people need to
get the proper credentials at scale, but we're not there right now.

Christian Huitema: I am skeptical about the amount of protection you really
get. I am concerned about the case where we first send the request in
cleartext, with all of the potential traffic analisys information exposed, is
not providing any benefit. We should think about the security considerations
about this, and maybe have other ways of determining this information, or
require another trip in order.

NM: We did talk about this in Seattle, and if people are going to do this for
security purposes, then you would block this data. Such as sending a very
minimal amount of infomration in an exloratory request or use DNS.

RP: I want to point out why people don't deploy HTTPS. It's not because of the
cost of getting certs, but because HTTPS is significantly slower. People doing
commerce are very interested in performance, and are unlikely to deploy unless
HTTP2/ with TLS is as fast or faster. Our experimentation at Google has shown
that HTTPS is as fast or faster for a large number of cases.

RP: < note taker missed it >

Stephen Friedl: I agree with Roberto. I don't trust locks on my browsers, and
heaven forbid I explain to laymen. The only way to do this is HTTPS (with
authentication) only. No more HTTP. And we should be rigorous about it. I am in
the camp to push everything to HTTPS except for the small set of cases where it
doesn't make sense. For ALPN, we should be more formal of how to register the
types.

Rob Trace: I would like to have a secure web, but there is a long list of
corner cases where it's applicable to have HTTP plaintext. It's hard to claim
this is a security feature, since you still have to treat the content in and
out as insecure.

EKR: Is HTTP/2-over-TLS only still on the table?

MN: It appears that the position of HTTP/2. over only TLS is too extreme.

EKR: Doing nothing is stupid. What I think we're arguing about is whether
having the relaxed version lowers the bar too much. I think determining how
many would do the right thing, or at least do opportunistic is tricky and we
don't know. I think opportunistic TLS is worth doing.

MN: People have expressed concern about confusing people about the security
state, and I don't think that will be the case. Server admins will open a
browser and look for the indicators. If there are none, then they don't think
they have any protection. As for commernce, I'm not sure that's an important
thing anymore. What's important is what happens out-of-the-box. If any
encryption requires doing more than installing the software then people won't
be doing it most times.

EL: One of the thigns I was thinking about was to do the discovery inline
instead of a referall mechanisms. I think having all the security and HTTP
people helps informs the discussion for perpass. A few people made some
economic assertions, these are interesting questions for researchers to look
into. Also, the IRTF meeting is discussing how to get researchers and those
willing to pay for it together.

PHB: The original goal for HTTPS was to have the same level of trust for people
buying things online as buying things in a store. So not turning on the lock if
you haven't authenticated is good. Deploying opportunistic TLS increases the
work attacks have to do which is good. But for the other attacks, where someone
could downgrade someone from HTTP/2 to HTTP/1.1. Do you really want to
re-encrypt YouTube vidoes each time?

AUDIENCE: YES

PHB: Once you get past that, you are really talking about doing strong crypto
or crappy crypto. You could probably collapse the work factors to one or two
choices.

Keith Moore: The decision this WG is making has a long term effect. I think we
need to look beyond the current threat or the past threats. Right now active
attacks are harder than passive attacks. But if a passive attack is feasible,
then an active attack is also feasible. I'm not sure there's a benefit to do
opportunistic because you can be downgraded, unless you can absolutely prevent
it.

TH: What Keith said, but also this is an estimation problem (as EKR pointed
out). We are taking the current state and adding opportunistic encryption,
which prevents FireSheep. Does adding opportunistic reduce the number of times
people get good certs?

EKR: If we provide the unauth mechanism, [EKR line noise]

TH: If we ask "should HTTP/2.0 be TLS-only?" we might come to a different
conclusion.

RP: My definition of commerce might be very different of yours. Pintrest
doesn't actually sell anything, but they still add value. Commerce doesn't
always mean adding things to a cart and checking out. Pintrest doesn't have a
competitor right now, but latency matters. Second, it is far easier to add
authentication later than to remove unauthentication later. If we weaken it by
adding this third thing it will be hard to fix.

??: Trying to protect against just the passive attack is silly. One thing is
very clear is that if I have a HTTP URI, I want to try to use it in a secure
way. If I use it in a secure way, I want to really be secure.

MN: If we did do opportunistic, do you want to see mitigation of downgrade
attack. [Yes]

Stephen Farrel: I think there's value in trying to mitigate the passive attack,
so I think the do nothing option is really stupid. Trying to insist on HTTPS
everywhere is not feasible or scalable. I think the third option is the right
approach.

MN: I think we have an opportunity to improve performance with HTTP/2

Will Chan: One barrier I've heard is about mixed content. Even though I'm a big
fan of telling people to just use HTTPS, but I need third-party ads and what do
I do? While I want to got HTTPS only, I think there's still a lot of benefit
because it reduces the barrier of entry.

EKR: I think you should consider option 0, and you consider TLS for HTTP/2
always. I think we should do something, and having some option for the server
to indicate it only wants to do the authenticated mode. Is it ok to have mixed
content? We need to consider the policies that are involved in these cases.

PHB: I think a lot of the argument is over a choice that doesn't exist. One is
whether you have authenticated cert or not, since the IETF doesn't strongly
define what authenticated really means. The only choice that can be made is
whether the client can be allowed to turn off its root criteria.

Roy Fielding: I don't think you can require HTTP/2 to be encrypted always,
given all the places that HTTP servers are deployed. I could get behind that if
you use HTTP you use a secure transport protocol, ether it's TLS or SSH or
something. I don't think it's a technical argument, but there is a social
argument that you can and probably should make.

#### What does the WG Want?

Mark Bishop: Just want to be clear, that for 2 and 3 that there's an option to
go better, but no requirement.

LM: One considerations is if users would be presented with information about
those connections. Which of these include those dialogs/information? And what
is the performance impact?

Dixon: To clarify server auth, it should include both CA-based and DANE-based.

Rohan Mahy: I don't know what #3 means with the word somehow, especially in a
technical context.

Gabriel Montenago: Remember what the desired final state is to increase the use
of valid TLS. Where is that in these choices? I think plaintext has an
important place in the world.

Barry Leiba: You should be looking for who cannot live with some of these.

0) Don't know (yet)

[strong humms for can't live with]

1) Do nothing - hope that hTTPS gets more adoption

[strong humms for can't live with]

2) Opportunistic encryption w/o server authentication for HTTP URIs - just for
passive attacks

[ less strong for can't live with ]

3) Opportunistic encryption with server authentication AND downgrade protection
(somehow) for HTTP URIs; no requirement upon HTTP/2.0 when not available

[ weakest for can't live with ]

4) Requre secure underlying protocol for HTTP/2.0 (at least in web browsing)

[ weaker for can't live with ]
