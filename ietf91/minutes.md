
# HTTPbis Minutes: IETF91

## Tuesday

Mark: today we have a discussion of our current work.
httpbis
altsvc
oppsec
tunnel
open issue in http/2, two of them
one is security related
we'll hold a ???

tomorrow: couple of new proposals
kent from martin
origin cooes
general discussion of proxies, few different drafts.
any agenda bashing?  noone..  Okay.

rfc7238bis a document to republish ?? code
no changes are meaningful in the document, mere updates.

Advice from AD that this is not the best way to update, so we were asked to hold
on to that.

Barry, feel free to say anything if you'd like.
Barry passes.
Mark continues.
Hopefully we'll figure it out soon, hopefully no controversy, just the mechanism.

Next: AltSvc.  Split it off HTTP/2.  Few issues.  How has read the draft?  Few hands.
Mark pulls up github open pull requests with AltSvc label.
Security considerations 36: tracking using the alt-svc host name.  Mark: I think
it's just an editorial issue.  Just to make sure we understand the privacy
issues.
Eric raised Alt-Scv-Used granularity.  Originally Boolean, for privacy issues to
prevent client fingerprinting.
Eric Nygren proposed effectively a bitmask, to denote the reasons alt-svc was
used, like load balancing or protocol upgrate etc.  I guess the idea is to make
load balancing algorithms easier.

Julian at floor mic:  Maybe we should give up to address privacy in this header
field, because even not having it wouldn't help, there are wys to identify the
client anyway, like redirecting the clinet to a client-specific service.

Next speaker at floor mic:  privacy issues is meaningless if we have any
entrophy.  I'd like to hear from those with a more agressively privacy-centric
viewpoint on this.

Mark:  Any comments, Patrick?
Patrick:  Not a useful one.
Mark:  I guess the only qualitative difference is that when you use the .... on
the wire it becomes more evident on the wire, whereas here it is completely
inside the header, which is more convenient in terms of tracking.  Playing
devil's advocate, if we allow this to be a wide open field, tracking becomes
evident from an implementation viewpoint.
Patrick:  Why does Erik need this?
Mark:  Is Erik here?  No.  I don't know why he wants this.  Load balance?  In a
highly distributed system, it becomes very difficult to have this state
replicated, so having it in the request makes it easier, but there are privacy
issues.

Erik arrives.  Mark puts him on the spot.
Erik: one motivating usecase is when a clien connects to a server, a server
would have some sense of how the client got here in the first place.  Use cases
can be debugging, diagnostics.  Also load balancing.  Depending on how the load
balancer works, if it is feedback-based, you need to feed this back into the
load balances, and without this indicator it would be impossible.  If privacy
considerations were not there, the most straightforward would be just to echo
the alt-svc record that made the client go here.  WIth privacy issues, is there
something between full string and Boolean?
Mark: what prevents you from putting this into the hostname of the alt-svc?
Erik: because it is not in the request header.
Martin Thompos: I think this is we are struggling more with the usecases than
with the embodiment of the mechanism.  The suggestion that eliminates the amount
of ....  Julian suggested earlier that we try to eliminate the inforation, but
the only way to address privacy adequeately is to totally eliminate this from
the header.  I gussest that we go way back to the start and just pack in the
alt-svc record that prompted this redirect.
Mark:  Erik said that thes header is not replicated .  It is true on IPv6, but
on IPv4 you have to use one address per identifier.
Martin:  Wu should pu the entire header of information instead of reducing it
down to one bit or two.
Mark:  Privacy leak is fairly small.
Martin: If the workaround is that Erik provieds one IP for every clien he wants
to track, he has a mechanism to track every client regardsless of alt-sv-used
header. As long as this exits, we have a mechanism anyway.
Mark: The other thing is that I think this is reasonable.  THe question is thif
iplementor bluk send this, they have a way to trakck clients anyway.
Patrick: If we make is MUST send, but SHOULD send the alt-svc token, so that a
client in an enhanced privacy mode can send one bit only.
Mark: You are an implementer, if you say that, that makes me comfortable.
Martin: Then there will be no incentive for severs to build infrastructure to
track clients.
Erik: Just being careful, ...
Hasan: For Erik and everyone on server side: if you need this for load
balancing, do your clients get a degraded service when they are in this enhanced
privacy mode?
Erik: Depends if the majority are in such mode or not, but I haven't thought
through the ramification.
Hasan: I don't think many people have thought through the ramifications, that
scares me.  Looks like we have two engagement modes.
Martin: When people engage in one of these modes, they take some cost.
Continuity of services.  Degradation is different.
Mark: WHat would Hasan's proposal would be?
Hasan: I don't like the idea of proposing indicators like this at all.
Erik:  I think one helpful thing would be other implementors chiming in.  Once
you start digging into usecases here, a lot of details start showing up, and not
having indicators would make it more difficult.
Mark: I am concerned that we do not have many privacy-minded people here, we
have to work more on this on the list.  We have Erik's proposal, we have full
alt-svc hostname, and we have nothing.  This is a pretty broad spectrum.
Patrick:  This is already in my client code on pre-release channel, and we will
keep it there until there is consensus.
Hasan:  I thin kthere is only one person on server side who is interested in
this (referring to Erik), and this is not how we should come up with standards.
I don't think other server implementers are seeing such issues.  Maybe that
means that this is not a problem we need to solve.
Martin: My personal preference is not to risk privacy issues.  Can we >.... ?
Mark:  THis is not in the core spec.  How many layers can we go?
Erik:  If you are on the same host, it's a lot less interesting.  Impact and
privacy potentially start showing up when you redirect to other hosts.
Ryan (?):  It is very interesting, for redirecting to closer hosts.  This could
be very helpful.

Mark types out the options on the screen.
Hasan: My point is not that there are not many people interested, but that there
is only one person driving the discussion, and only two implementations.  This
is not a standard yet.
Mark:  That could be said of many things.  Welcome to the IETF.
Hasan: I think we have a higher bar.
Mark:  We need to talk more about this on the list.  I'll ask for a hum.
no alt-svc-used: few hums
1-bit: no hum
multi-bit: one hum
full hostname: few hums
1-bit or full-hostname: few hums
doesn't know: most hums

Barry:  anybody can't live with one of this options?
Martin: Given the subject matter, I don't think so.
Erik: The first one, no alt-svc-used, is the only one that would keep us from
implementing the changing the hostname usecase.
Mark: anything else?  No.  Let's move on.

Mark: align opp-sec and alt-svc.  Do we want to cover this here or can we  move
on?  It this more appropriate in the opp-sec section?
Associating alt-svc with an origin.  I think this is straighforward, this is
editorial, doesn't require meeting tiem.
Unexpecting alt-svc frames, similar.
Cache invalidation.  So this I guess is more fundamental.  WE have a cache off
of different hosts.  A new value is an invalidation semantics, or addition to a
pool?  It is currently not quite clear.
Martin:  The obvious fall is that we are requiring this for multiple sources.
We need to make sure authentication is covered, so that different sources cannot
invalidate each other's alt-svc fields (?)
I think this is almost editorial.  Maybe one set can replace another set.  I
mean if x tells you something, it does not invalidate what y has told you.
Erik: A key part would be ...  In the last draft, header and frame had different
semantics.
Audience: We fixed that.
Mark: let's take it to the list.

Mark: positive indicator of ...?  We don't have a way to indicate semantics on
the wire in HTTP/1.
Martin: The challange here is that there is no clear indication that this would
be respected.  Both parties make it very clear that they understand what is
going on.  I'm not sure we need to pursue this immediately.
Mark: A security indication "hree be dragons' is probably good enough for now.
Martin: I know so much code out there that looks at the connectino, is it TLS,
then proceeds to do things.  THis opens up attack vectors.
Mark: document this in security considerations, and worry about it in the future.

Mark: Julian?
Julian: We hwant to have enough ... so that the frame can carry multiple
indicators.  Frame carry the same load as http header field, otherwise http/2
implementations will need to have two frames whereas one field would be
sufficient.

Mark: alt-svc, i would like to ship this very soon, it would be nice to clean up
these issues, hopefully go to WG last call on this.  Barry, is this okay with
you?  Barry nods.

Mark: any other discussion on alt-svc?  No.  Next up is opportunistic security.
Relatively few issues.
#30 strongly authencited (as origin). editorial.

persuite requirements #26.  Martin, you have a comment?
Martin: I don't think there is any value to us in expanding cyphersuites.  If we
decide to do that, we should carry that decision here as well.  It's just one
code path, it's a lot simpler.  THe other one is that we are building these
opp-sec profilies to look idenitical to an observer so that they would not be
motivated in trying to break this.  It would be a great advantage to have the
exact same profile.
Patrick: The whole point of opp-sec is to identify the protocol.  It is fragile.
Mark: close we no action.  Problems?  Okay, closed.

Align alt-svc and opp-sec.
Mark: Erik, you want to walk us though this?
Erik: it was on the list.  the issue is two separate graphs from each other, can
be implemented separately.  In opp-sec, you don't have to have strong
authentication.  You have no way to signal to the browser that the
authentication might not be valid.  If the browser wants that but is
uncomfortable with opp-sec, but heartfailing, it is not a good state.  It would
be better to align them.  The problem is that someone can just strip out alt-svc
entries entirely to force to stay on http/1.1.
Mark: We talked with Patrick on this, but we didn't talk about putting something
in the alt-svc advertisement.
Martin: I think that point is a key on it. It is unpleasant to spend time and
effort, but you havn't actually busted anything.  The reason I argued is that
the decision to authenticate or not is downstream from this process. To have
something upstream is independent (?).  A commitment a server can make to
clients that it can/should be authencitaed in the future, we are expeirmenting
this.  I would treat shis as an editorial exercise.  opp-sec can give you a
surprise.  And than there would be no protocol machine, and I like having no
protocol machinery.
Erik: If getting certificates becomes magically so much easier than today,
browsers can start ignoring alt-svc with noauth tags.  Then things will
magically work without issues.
Martin: I suggest the opposite.  When everyone has a certificate, we can have an
auth tag in the future.
Mark: extensibility?
Patrick: feedback metric.  I'd rather this wasn't in the draft.
Erik: THe question is sending noauth sending over a cleartext channel as opposed
to sending auth.  Any indicators that are trying to follow an alt-svc but would
require a valid certificate and would hard fail if there was no authenticity?
Martin: http and opp-sec, noone's planning to do that apart from Mozilla and
maybe from other people.
Mark: it was half-editorial anyway, we can call this editorial now.

Mark: Opp-sec and alt-svc, we'll try to get them out on the same schedule.  Next
up we have tunnel.  Folks wanted to have a spec to indicate the protocol on a
tunnel.  No open issues.  Assuming we have the editorial issues, does anyone
have any other issues to talk about?
unnamed speaker on the floor.
Mark: when you are happy editorially, we can do a WG last call on that.

Mark: HTTP/2, almost right on time.  Issues list.  #642 allow PRIORITY on stream
in any state.  Widely shared nervousness, uncertainty on the list agains drastic
changes.  Small changes instead.  Assume download for images and CSS, no way to
prioritize, group them.  It was proposed on the list, maybe by Martin, to fake
this, or add flexibility, by allowing PRIORITY to be set on any state, to create
fake groups for priorities.  Didn't see objections to it.  At this point we have
a higher bar to changes, usually broad claim, or interop or sec issues.  This is
a candidate for broad claim.  If people had a chance to look at this, please
comment.
Martin: You missed the primary case which is intermediation case, when there are
two sets of requests from different clients, and no convenient handle to group
requests, this is a convenient way.  It's unpleasant, but we already have a
requirement that some preioritization state has to be maintained anyway.
Mark: take it to the list.  And now what you have all been waiting for. 9.2.2
#612. 9.2.2. required ALPN capabilities beyond RFC7301.  Folks started to talk
about everything security related in HTTP/2.  I want to focus on this as closing
this issue and closing the spec.  Web browsers have to interop with a wide
variety of serves, old ones two, so they have to offer old ciphers too. ...Mark
reading text from the screen...  "My API doesn't support that" isn't a technical
issue.  Having said that, if noone can implement what we specify, that's a
deployment problem.  We have to balance these two.  But we do have running code
supporting 9.2.2., so we have proven that it is possible.  Question: does 9.2.2.
introduce future risks to the protocol?  Any interop issues down the road?
Non-conformance?  Presumably the server will notice and fall back to HTTP/1.
Other issue: new ciphersuites introduce uncertainty.  Also, deprecation can
cause interop problems.  I've been talking to people in person and trying to
come to a concensus.  straw-man list-informed proposal (SMLIP) is a half-decent
starting place, because it has aspects that appeal to most people. six steps:
1. make cipher suite requirements specific to TLS 1.2.  Leave ciphersuites for
TLS version up to the TLS WG.
2. Nominate a fixed list of suites instead of properties, because it is easier
for implementations.
3. Keep the required interop suite, mandatory to deploy.  Already implemented a
few times, not constraining.
4. Clarify that requirements apply to deployments, not implementations.  Because
libraries interact in a complicated manner, deployments include configuration
etc.
5. Relax requirement to generate INADEQUATE_SECURITY, not controversial based on
conversations.
6rk. Require support for TLS-FALLBACK_SCSV with TLS1.3+

unnamed floor mic person (Sam?): I care a great deal about the ability of adding
a cipher.  Less concerned about removing, we can just stop advertizing.  I get
the problem.  I have a small proposal: have a list of whitelisted ciphers that
are guaranteed, set a requirements.  Solving ciphersync, have a blacklist of
ciphers, and allow INADEQUATE_SEC to be generated.  My point is  that if there
is a cipher you never heard of, don't generate INADEQUATE_SEC.
Mark: To reiterate, you want a blacklist instead of whitelist on point 2?
unnamed: Maybe both.  For people who prefer to emit INADEQUATE_SECURITY, this
would make it easier.
Erik: Propose that a cipher not on that list and ALPN token h2, that you have to
support that for h2.
Kathleen (?): blacklist scares me, how big can it get?  Typically we start with
black and later get to a whitelist.
Sam: blacklist would never grow, it would be current IANA registry minus
whitelist.  We have a set of properties that we would like to implement for
ciphers today, except that we decide it's too complicated.  To avoid the
ciphersync problem, we want to help people to understand which cipher are good
and which are bad.
Erik: Propose that a cipher not on that list and ALPN token h2, that you have to
support that for h2.
Kathleen (?): blacklist scares me, how big can it get?  Typically we start with
black and later get to a whitelist.
Sam: blacklist would never grow, it would be current IANA registry minus
whitelist.  We have a set of properties that we would like to implement for
ciphers today, except that we decide it's too complicated.  To avoid the
ciphersync problem, we want to help people to understand which cipher are good
and which are bad.  We need to enumerate... We would have the fixed blacklist.
Mark: to make sure, a peer would use the blacklist as a basis to generate
INADEQUATE_SEC if they want to.
Sam: YEs, and if they don't care, they don't worry about the blacklist.
Martin: I think Sam's suggestion of knowing what good and bad are, we should
throw them in an appendix because the list is gonna be long.
Mark: okay, so if it's not on the blacklist, you MUST NOT generate
INADEQUATE_SEC on that basis?  Why whitelist as well?
Martin: Because there are ciphers that are known to be good, there are ones
which are known to be bad, and some are unknown.
Sam: Having a blacklist would help to make it blazingly easy to implement.
Mark: You want the whitelist to be a registry?
Sam: I don't care.
Erik: Have an appendix.  Do this or that.
Sam:  No.
unnamed speaker: Let's get back to technical discussion. .........
other unnamed speaker:  I'm really confused.
Sam: Erik, when you first got up here, you said if it's not on the bad list, and
if you advertise it, then you have to be using it with h2.  If you advertize
something that is not on the bad list, you'd better be willing to use it with
h2.
GCM is on the good list, CBC is on the bad list for H2, but will be used in the
foreseeable furute.  So the client should simultaneously advertize these.
Sam learns that the server does not advertise cipher, but the client does, and
asks why does the whole thing matter then.
unnamed: And the server might be older than the time the cipher turned out to be
broken.
Mark: And then that's why the list needs to be static.
Third unnamed speaker: Let the TLS WG worry about this.  And what happens after
INADEQUATE_SECURITY?  It is up to the client.  Do they start over with a
different security set, or do hard fail?
Mark: The server administrator will notice when deploying and testing, so I've
been told.  TLS WG chair and former security AD said we can have this discussion
in this WG if we want, it has been done before.
unnamed speaker:.....
Mark: Sam, to clarify, you suggest that if the cipher is on the blacklist, then
peer MAY omit INADEQUATE_SECURITY, otherwise it MUST NOT.
Sam: Right.
Mark: and blacklist is fixed and in HTTP/2 spec.
Roy Fielding (?): I don't care who prepares the list, as long as the HTTP
standard can refer to something that is independent and moves over time.  It is
not under the realm of HTTP.
Mark: I though that we agreed that the list should be fixed.
Roy: For deployment.......
Mark: how do people feel?  Anybody insists on whitelist?
unnamed speaker:  Mark, you had technical reservations about a blacklist.
Mark:  I'm blanking on it.
Barry: I want to ask Roy why you don't want the blacklist in the spec but in a
separate document?
Roy:  It should be separately reviewed by TLS people and library implementors
and people concerned with TLS interop.  Also, HTTP/2 runs over many things, TLS
is only one of them.
Patrick: The failsafe is that the client should offer ... in addition to offer
HTTP/2.  More broadly speaking this is a plausible work forward.
Ryan Sleevi: Responding to Roy, we have a UTA WG trying to retrofit TLS to
deployments.  With respect to blacklist, I am concerned about the
implementation, the IANA registy, and TLS WG.  WIthout IETF review, the
blacklist is also a moving target, and it doesn't solve the problem of the
whitelist being a moving target.
Sam: My impression is that we were gonna have the whitelist in 9.2.2.  There
will be future bad ciphers, just don't offer them.  The blacklist is only for
cipher that have to be offer for compatibility with old servers, but should not
be used with HTTP/2.
Mark: I wanna pop up the stack.  I am balancing the discussion with the desire
to finalize the standard very quickly.  If we put too many things on the list,
and the list is too agressive, that might be still better than having no section
9.2.2.
unnamed: The first issue is whitelist versus blacklist.  The second issue is if
should be fixed in spec or dynamic, or a set of properties.
Mark: Noone was arguing for a dynamic list.
unnamed: Ryan was.
Ryan: 9.2.2. language is acceptable, and it captures the point.
unnamed: So third question is this language about MAY and SHOULD and
INADEQUATE_SECURITY, I am not happy, but am willing to go with it.
Mark adds to document "Peers MUST NOT negotiate BAD"
unnamed: Final question, is it gonna be in the spec, or who is going to figure
it out.
Mark: I am looking for words to convince me that you are not in rough with this.
Roy: It doesn't work that way, the negotiation takes place before we find out it
is HTTP/1 or HTTP/2.
Mark: This is exactly the issue.
Roy: Because the alternative is going back to HTTP/1.1.  I'd rather let the
first generation of user fall then have this stupidity.
Barry clarifies.  To avoid the extra delay, you are bundling this.  I am willing
to talk this or that ciphersuite, but if it's h2, then only these.
Sam:  So, Roy, what needs to happen, is there are many ways to implement it.
One way is that for the server to prefer...  The other is ALPN. (?)
Mark: Let me highlight that implementers may assume that the burden is on them,
but it might as well be on administrators.
Roy: As long as it moves back into the area of TLS deployment.
Ryan: I would also only like to see HTTP/1.1 used with reasonable ciphersuites.
Unfortunately we have a large number of deployments holding back deprecation.
HTTP/2 has little deployment right now, but will very soon see large deployment.
I am pushing for stringent requirements on ciphers because this is an
opportunity to enforce good ciphers, and because HTTP/1.1 bad ciphers are very
difficult to get rid of because of wide deployment.
Roy: .....
Mark: I'm surprised to hear that from you, because historically you always
focused on specs and not implementation.
Roy: No, the end user deploys Apache, for example, and then they have TLS, and a
set of intermediaries.  But they are totally outside of control.  In order for
us to depoly HTTP/2, we cannot change this relationship, we cannot force them to
change their TLS.  They are both deployment requirements.
Patrick: With regards to that last line of though, the HTTP/2 already requires
that for deployment.  You cannot run your OpenSSL stack with h2, it doesn't have
the necessary functionality.  Other point, broader prospective: old, bad
protocol stacks don's retire themselves.  If h2 allows all existing behaviour
that h1 has, we'll have to expect some set of that behavior.  The reason this
came up is that ... deployed h2 and Firefox said INADEQUATE_SECURITY.  Finally,
h1 and h2 with asymmetric requirements, well, they don't behave the same on the
wire.  There is a lot more information in the leading bytes of h2 than in h1.
Roy: Good ciphers are already preferred 99.9% of the time.
Mark: I am aware that we don't have all stakeholders in the room. Who thinks
this on the screen is a good idea?  Many hums.  Bad idea?  No hums.  Don't know?
Fewer hums.  We'll take this to list.  As chair, my main interest is to shut it
down.  We'll meet again tomorrow.


## Wednesday

httpbis notes:
==============

Seen the notewell, no more opinions on 9.2.2

Kaoru Maeda on "HTTP/2 local activities in Japan"
* HTTP/2 conference in Tokyo 2014, Nov. 3, 2014
* 30 minutes to write an HTTP/2 client

Applause in the room ; no questions at the mic. 
Mark Nottingham (MN): nghttp2 is considered a reference implementation. Language barriers make it hard to get the contributions from Japan back into our work.

Next up: client authentication over HTTP/2: draft-thomson-httpbis-cant-01

* TLS 1.3 - no renegotiation
* HTTP/2 forbids renegotiation
* Renegotiation used for spontaneous client authentication
* Use a 401 code to force client to start a new 

AS: Can do the reconnect 
EKR: what is this DN and SHA-256 in the 401? 
MT: something from the chain. 
EKR: maybe something bound like token binding?
AP: Token binding is not authentication. It's something you can use *after* authentication
Ben Kaduk (BK): this is reminiscent of Kerberos. 
Yukata Oiwa: why use WWW-Authenticate header when the rest of the mechanism is not shared with other HTTP authentication mechanisms.
YN: What about HTTP/2 over TLS 1.2? 
MT: We expect that the client will renegotiate immediately after the the handshake on the second connection, and the server takes this as a signal to send a certificateRequest.
MN: Are we ready to adopt this?
MT: Stephen Farrell (hope I got the right number of r's and l's) has questions about expanding the scope.
MN+MT would rather not.
MN: 
 + Who thinks we should adopt this draft? semi-strong hum
 + Who thinks we should not: silence
 + Who doesn't know: somewhat weaker hum

Salvatore: why do this over HTTP/1?
MN: for HTTP/1 over TLS 1.3 and it might be preferable when this ends up.

Next up: Origin Cookies
No presentations - please read the drafts

Next up: proxies

draft-nottingham-web-proxy-desc

Using wpd to configure network proxies: draft-loreto-wpd-usage
Salvatore: mock proposal for client to use different proxies present in the same network and offering different services. Important for telecom because we use diff-serv, and we want diff-serv using different proxies.
Dan: creates an incentive to label resources so they go through the proxy, they get dispatched effectively. Very little work on the UA side. This is not for discriminating traffic and has little privacy issues, because it's about classes of traffic, not specific resources.
MN: has been problematic for HTTP for a long time. There is concern that WPD or something like it will not kill other proxy configuration methods, but be added as another one. If we want to do this work, it should be big - not just publish an experimental thing. What do the client implementers think?
Rob (Microsoft): pushback on WPD. May not have the functionality that exists in PAC today. We'll keep track, but not much interest.
?? (Firefox): Current state of the art is not great - multicast resolutions for WPAD; origin stealing, etc. Even if all we do is annotate .pac, it's useful.
Ryan Sleevi (Chrome): Like Rob. We are invested in proxy discovery, but worried about making yet another method. Will continue to follow.
MN: I hear you, maybe WPD was premature. If clean-up of .pac is the right direction, that's good 
RS: (nods)
?? : WPAD is terrible. initiating trust is a hard thing.
Elliott Lear (non-browser): agrees with Rob. Need something with scale. not just downloading a list of hosts.
Kathleen Moriarty: proxies / middle-boxes are considered evil. Gives another point in the protocol to monitor.
MN: one of the motivations. Not a lot of constraints on security. Can require a cert for the proxy that couldn't be required before.
MN: how to move this further? pacv2? mini-workshop?  interim meeting?

Larry Masinter: seems you have an agreement of use cases and problem statement. Perhaps publish that?
MN: worried about that becoming a tar-ball of everybody's wishes.
Brian?: positive thing to do. Workshop would be better than 1 hour every three months.
YN: Why do we need proxies if we want everything to be HTTPS (TLS)
Patrick: Can we get traction? If we still have a portion of the web that will remain HTTP, maybe it's genuinely useful.
EL: hotel networking - an area for us to work, captive portals. proxies are used for this purpose.
Dan: Ignoring this is bad. People will do some things and they will complain. With standards we can get something working.
?? (Verizon): very interested in traffic optimization because of volume caps for mobile phones. Standardizing this would be good.
KM: channeling Stephen: we should trust all the service providers 
Patrick: HTTPS is e2e, but TCP is not. Explicit proxies can have a role in optimization.
Ted Hardie : aren't we fighting the last war? NFV now distributes the work that used to be done by proxies. Deserves more thought. There are proxies that are like split-ua and some that are not, and they should not be treated the same way.
MN: historically, when we say proxy we mean an intermediary that is configured on the UA.
TH: even taking this model, this doesn't reflect reality. If we assume it's an on/off. Are we treating this as monolithic. Proxies are acting not (only) on behalf of the UA but on behalf of the network.
Dan: network-aware proxies vs cloud or split-ua proxies. 
Hannes: We need information on what this intermediary is, who owns is, what it does.
LM: we've been discussing it for 20 years. If we don't write it down, we'll keep discussing it another 20 years. Do a workshop, publish a report. At least do that. Write down something.
MN: we've started to.
MT: institutional memory is terrible. In 2 years we forgot the design rationale for HTTP/2. Not sure there's a lot of value in a workshop report. Has concern about what Ted said. Things may exist in a chain of intermediaries. The only mechanism we have is the choice of the first intermediary we send the request to. The decision between e2e and going through intermediaries is all-or-nothing. Not sure what it takes to make that decision. No good answer yet.
Joe Sallowey: plugging i2nsf - BoF tomorrow. Some of the topics relate to provisioning middle-boxes.

MN: will talk to Barry about that.

Next up: Presentation by Will Chow: WPD proxy discovery

TH: it's unworkable. Sending the network authority of origin authority is open to MITM
DKG: push back on the idea that poor people need less security.
MN: want to add that interception proxies are the state of the art. We need something more secure, more usable. This conversation will no doubt continue.

MN: that is all we have. Some potential new work items. Have HTTP/2 to finish.

MN: Might not meet in Dallas. Thank you all

