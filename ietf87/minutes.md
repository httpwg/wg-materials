# Minutes

HTTPbis Working Group - IETF 87, Berlin

## Wednesday Session

### HTTP/1.1 Issues

We discussed a number of issues in Trac, including #470, #475, #458, #345, #455
and #486. No decisions were made, but the editors were able to discuss their
status and allocate owners; expect proposals to be incorporated in the next set
of drafts and/or discussed on list.

### Known Startup State for HTTPS

Gabriel presented to see if we agreed that we need to request TLS provide a 
mechanism for conveying the startup state for HTTPS; however, we did not yet
reach consensus on this, as it was felt it needs more discussion.

### HTTP/2 Issues

We did a run-through of the open issues to triage them for the upcoming Hamburg
discussions. In this process, we were able to close a number as already
incorporated in the -04 draft.

We agreed that for isssue #174, it should change to MUST.


## Friday Session

Note well reviewed. Mark review the agenda: HTTP and Encryption, HTTP/2 with a
Transport Eye (Allison Mankin), 20 Min Flow Control, 20 Minutes Priorities, 20
min Initial Congestion Window 20 Min General Discussion/Other issues. He notes
that the primary reason for the meeting was to give a joint meeting with the
Transport Area, but because of recent events he and the Security ADs felt that
it was timely to have a short discussion (time bound to 15 minutes) on
encryption. The transport discussion will follow.

### HTTP and Encryption

Next Presentation, also by Mark, begins, on HTTP & Encryption. HTTP/1.1 has no
Mandatory to Implement to Security; that was an artifact on how long its been
around (Larry Masinter disagrees with this characterization; the rational for
allowing connections to remain un-encrypted was the same then as now. This
discussion was delayed). SPDY introduced Madatory to Use Security; this was
discussed for HTTP2.0; the working group declined, because of use cases like
back end services. The status quo is: Server Chooses whether encryption is used
or not--if the server does not offer encryption with an https URL, the client
cannot use it. It is an assymetric relationship.

There is new information; there are widespread deployments of sniffers. More
details have since been released. As Chair, Mark felt that this was enough to
re-open the discussion. He suggests a few proposed actions--these are the start
of the discussion, not an ending. Martin notes that the scheduling conflict of
TLS being against this working group means that many who care are not present.
Mark splits the discussion into HTTP/1.1 and then 2.0. Mark notes that there
are limits on what we can do for 1.1. He proposes that we document the
asymmetry and the consequences; while it does not do more than describe the
issue, since we are re-describing the properties of the protocol, it would be
good to do. See slides for the proposed additions, but “servers out to
implement and prefer HTTPS”. That’s not necessarily adequate, but more might
come from TLS as they document the security properties of their protocol. He’s
not looking for lots of discussion, but a sense of the room of publication of
something like this. Two hums: do we want to pursue documenting this in the
security considerations in the 1.1 drafts (probably in the first document in
the series)? Alternately is that not a good idea?

Gabriel notes that the choice not to send packets is always packets. Larry
notes that he believes this is political theatre--there is no technical
judgement that you can apply here. We should focus on the technical work here.
Mark agrees that there may be a bit of political action here, but notes that
the security considerations already have many corner cases reflected, and doing
those and not this seems odd. Barry asks if there are implementations that do
not implement HTTPS? Yes.

First Hum: is this an interesting discussion for documenting in our HTTP/1.1
document? Strong Hum. The reverse: a much weaker but still present hum. Mark
says that we will continue on the list, but will cut it off if it becomes a rat
hole.

Proposed HTTP/2.0 discussion of the same topic begins. New issue, since this is
a new protocol. Mark wants to introduce the idea of equal power; a client can
negotiate/require use of encryption for HTTP URIs. He would like this
discussion to become more explicit. The second piece is proxy
discover/interactions. The interposing proxies need an answer for this; the
user needs to understand what is happening and have an opportunity to say that
no, this is not what is happening. We need to think more carefully about
protocol interactions. This is *NOT* about enabling man-in-the-middle
interception of encrypted traffic. The documentation of HTTPS is for end-to-end
security and that will not change. Liaison with TLS and W3C may be required.
For the HTTP 2.0, he would like to take those hums.

Larry Masinter notes that the topic was mandatory to implement security, but
some of what he said was not the same. Mark says “mandatory to offer” is closer
to what he said. Larry said proxy behavior taxonomy may be necessary. Mark
notes that if we disenfranchise proxy use cases, we will have deployment
problems. Gabriel Montenegro believes that encouraging the use of encrypted
capabilities is wonderful, but he wants to understand if this disallows parties
speaking without encryption? Mark clarifies that if both parties truly want to
use a clear channel, it should be possible. Greg Maxwell notes that it may be
useful to distinguish between security and encryption--e.g. authentication may
require other costs over and above those of encryption. Bob Briscoe of BT. He
hasn’t been involved since 1995, but had come for the transport bit. He wonders
if from the proxy point of view the least it can do is stop the bits flowing
(client present this to a user--the proxy says “use me or you are out of luck”).

Who believes that these issues are worthy of further discussion: Hum in
support:strong hum. Hum against: silence. Good, and we are now at the end of
the alloted time for this.

### Transport Joint Meeting

Next topic, Allison Mankin’s presentation, “HTTP2.0 with a TSV Eye”.

Allison introduces herself as the TSV technical advisor to the WG. Motiviation;
the transport area decided it would like someone with TCP to follow the work,
but this is still an individual’s perspective. She hopes to foster a
constructive, ongoing relationship. She introduces her “phrase book” for
traveling between areas. Puts up examples “hop-by-hop, flow control, streams”,
even transport (e.g. optical transport vs. transport protocol). That means that
the ability to skim is limited--review needs time.

She then puts up the 5 myths format. Myth 1--that http 2.0 might not address
and mitigate the use of many concurrent TCP connections. Myth 2--that HTTP 2.0
may try to appropriate/duplicate windowing and data management roles of TCP.
Myth 3- that HTTP 2.0 may try to move congestion control and avoidance into the
application, possibly replacing TCP with a streamlined transport without native
congestion control and congestion avoidance. Myth 4-- that prioritization in
HTTP 2.0 is related to (and/or clashes with) priotization implemented in
various transport and lower layer protocols. [Mic lines were asked to stand
down, so that the story can complete; note that others may have other views]

Goes into Myth Busting. For Myth 1, notes that HTTP/2.0 work so far clearly
does reduce the need for concurrent TCP connections and the working group is
focused on this. For Myth 2, the frame and streams mentioned do not match the
transport concepts--they serve application processing needs; this is a
travelers’ phrase book problem. Myth 3, HTTP2.0 has flow control functions;
this is not the same as CA/CC. This is *application service flow*, not the flow
of the transport. This allows the system to serve well-recognized HTTP
intermediaries. Some of this text is confusing to those coming with a transport
eye, but this is still a myth we can bust. For Myth 4, these are not associated
with QoS, and are not described in a way that matches up with transport types
*but* there is some language connecting priority frames connect to the
bandwidth delay product, so it may be something to examine for transport folks.

Myth 5 (the bonus myth) is that HTTP 2.0 leads to the replacement of TCP by a
new transport. Are there discussions of replacing TCP as the substrate of HTTP?
Yes, there are discussions of this, but the HTTP 2.0 work item is unequivocally
tcp-mapped. The initial congestion window experiments were removed from the
spec. TCP-Minion and QUIC are both coming along. TSV has long acknowledged that
applications can ask for things which are not the basic byte stream. SCTP,
PR-SCTP DCCP are actually representations of the transport aim to meet the
needs of other customers. So work of this type is not a problem.

Allison also compliments the WG on its intensive work style. Frequent interim
meetings, github working methods, and the development of a state diagram for
the stream lifecycle. There are still points for TSV review. GoAWAY and
RST_STREAM; this still in need f review. TSV style review of the risks of
off-path attack in general--the area is sadder but wiser about these. TSV style
review of data integrity issues, e.g. binary and compressed headers. Weak TCP
checksum failure probably furthers case for “TLS everywhere” in the HTTP2.0
world.

Going forward, TSV needs close listening, close reading of the review. Also
looking at research on SPDY versions may help TSV folks; pace of innovations
should be resonant to TSV folks. Finally, A gratuitous photo fo TIergarten
tapir (see slide for the photo)

Mark thanks Allison for her presenation and the mic lines filled--most of the
technical topics are queued up for later sections.

Eliot thanks Allison as well. He notes he has seen at least one person do even
more just-in-time presentation (3 seconds in advance). For the weak TCP
checksum issue, TLS is not required, so we cannot rely on it. Allison says it
may be a carrot for using TLS, not a full requirement. It should come up. Mark
steals the front mic, and notes that some folks have considered asking for a
checksum for the headers themselves.

Bob Briscoe wants to go through 3 of the myths from a different view. The first
one--slowing the growth of more flows; there is a problem the other way around.
It is not about HTTP is doing, it is about what TSV is doing to incentives
using more flows (e.g. in RMCAT measuring whether two flows are getting
fairness, rather than looking at session level. AQM presents a similar issue
(e.g. in fq_codel)). In message flow control myth, notes that TSV *does* have
expertise there as well and may be able to help. Allison notes that the
document notes that it can evolve and more work is needed. On the question of
stream handling, Bob reiterates that there is a lot of work in TSV on this
topic, and he wonders if we will end up duplicating. Early recognition of this
is useful. Bob also notes that there is a lot of work on latency going on,
TCPMaint is where most of that is going on, but AQM as well. TCP fast open,
work on reducing the length of slow start; there has been work on TLS false
start as well.

Jim Gettys cannot overemphasize of the impact and collateral damage that HTTP
has already imposed on the internet, limiting RTCWEB and other work. Points to
his blog, which describes the way in which HTTP1.1 was deployed gamed the
system in its own favor. Bufferbloat and HoL are well known, but the damage to
everything but web browsing is very heavy. We have to drain a swamp. We don’t
want to be here again in 10 or 15 years to stop another gaming of the
transport. He really wants people to understand minion and its potential
deployment path--he believes that the work can serve the web really well, and
it has a straightforward deployment strategy. It will give you a lot of what
the web needs. Cross-fertilization between that work and this needs to go
forward.

Michael Tuexen continues the theme and wants the cooperation between this
working group and the transport. In particular, what features and services
would be valuable is really needed (byte stream? something else?). Other things
are on the table: quic, sctp/udp. Mapping from candidates to services needed,
then deployment considerations.

David Black here as a STORM co-chair. There is already precedent with a weak
checksum (iscsi defines its own checksums). He suggests that there is an
opportunity to have a header checksum and a data checksum; this works well
through proxies. These checksums are defenses against flaky behavior, not
malice. If you want the latter, you need something else, e.g. TLS.

Larry Masinter--of what you discuss, measurement may be the critical one; we
need to see that http2.0 will be better in the real world. Transport has more
experience measuring in this area and cross-fertilization would be good.
Gabriel Montegro sees two subdivisions of this dialog--what is TSV doing
independently of us (e.g. general services work). The other is describing our
layering more explicitly so that it becomes easier to re-layer on other things.
A different dialog would be when HTTPbis is doing “transport-like things”, we
can get help from TSV on approaches. Flow control is one example, as the
principles and algorithms may be common or pluggable. The other point is what
you mentioned about window shrinking--both TCP and SCTP strongly discourage
window shrinking (should not, not must not). In the web, there is confusion
when it does happen; that may also be something we can take in and learn from.

Michael Sharf, co-chair of TCPM, emphasizes that it is a bi-directional
relationship; we need insight from you for evolving TCP (and TCP is still
evolving). TCP recently published an experimental RFC for increasing the
window. We also have the work on fast open, which may fit well here, since it
is focused on latency. We are interested in input there, especially on the
semantics for applications. Input is very well. Lastly, we have a working group
item on congestion window validation. These may be of interest to you, and may
be a place of

Martin Stimmerling plus ones Michael’s words, but also wants to reinforce that
you need to work on what’s there--looking at minion and quic is great, but we
need to run on what’s there. Mark notes that the timing with minion is
problematic as adopting it now would give best results, but it is not ready.
Jana thanks folks for this meeting. He wants to say transport that we’ve been
shy about talking about APIs, and that may have been a problem. We create
exhaustive but not very useful lists of transport features. We need application
developers to see APIs in clearer terms and expose them in clear terms--a
service model. Gorry Fairhurst notes that API discussions are *not* banned;
David Black plus one’s. As a Transport AD, Spencer pointed out that Jana did a
touchdown sign with both hands when he got that statement. Michael came up to
say that TCPM was rechartered and that API work is in scope. Much rejoicing in
the room.

Jim Gettys points out that this interaction showed the value of flow queueing.
He then reiterated that a lot of this reinforces the language issues; we need
common vocabulary.

Roberto Peon notes that *deployed* features are the first order bit looked at
by applications; is it there and will it be available are more important than
any other features. SCTP, if it had gotten past the chicken and egg, would be
used today. Roberto also noted that we have had implicit rather explicit APIs.

Mirja Kuehlewind notes that she has tried to follow the HTTPbis work, but it
has been hard because there is so much going. Mark Nottingham pointed to the
wiki and github pages.

Michael Tuexen went back to the *services* view; exact socket options may be
too detailed a question. The key question is whether the service is available.
That may be available in ways that are not direct APIs--e.g. SCTP over UDP. A
list of service requirements may be important for deciding if they can be made
available, rather than what the socket options are. Mark wonders if there is a
list of available services; Michael pointed to a previous set of slides (and
audio stream). Mark looks for stuckees to own chasing this? Michael says he
will be happy to help. Janardhan Iyengar suggest that we have taken a jab at
this in minion, but it would be great to generalize that. Will Chan asks what
it is that TSV wants HTTPBIS would describe? He feels like the elephant in the
room might be QUIC. He wonders if folks are looking at this services question
because folks are wondering why people went to QUIC.

Michael Tuexen says HTTPBis needs to say “here are the features that we need”
that are important enough that we would consider changing the transport
protocol. Will Chan notes that we have not done that within HTTP so far--we are
building on TCP. Mark Nottingham notes that he feels a wish list exercise might
be a time sink for his working group; he feels it should be transport area,
hopefully not for selfish reasons. Gorry notes is is Transport and Services, so
it would be good to restore the S. He also says that it would be good to have
that list with a focus on what is really needed, not a wish list.

Martin says we have offered QUIC time at the TSVWG, and they have been told
they will come, but later.

Andrew McGregor notes that there is knowledge in AQM on how to make
message-based transports work well, and it may be useful to coordinate there.
He also notes that splitting the agenda and publishing different conflict lists
would be useful.

Roberto notes that he has a list here, and he can send it out, but he believes
transport people know all of it and are working on it, but it needs to get
deployed.

Patrick McManus knows the transport area and has been active there, but he is
here as an HTTP 2.0 guy. In that guys, he notes that the effort is to work with
TCPs that are in the wild. Those are the transport equivalent of our middlebox
discussion--what can we do in those constraints? Mark agrees that this is a
good point. Patrick also notes that we can still work on these and share data,
but note that deployment and iteration is critical.

Will Chan then presents some data on initial congestion window data. Data not
on agenda, but will be uploaded. He shows a slide of data from Chrome’s beta
channel users (not all uses, but a small set that have opt-ed in to sharing
anonymized data). Roberto notes that “small” is relative, but statiscally
significant group. Will explains the SPDY setting that was a persistent setting
used when there was a successful, graceful close. Chart limited to stable
connections (100kbs or more of data). The x-axis is CWND in packets; the y-axis
is the percentile (histogram). Notes that SPDY connections are initialized to
32, which is the default for SPDY. Lars asks if this available as a CDF? Yes,
that’s the next graph. Shows the data. Patrick McManus notes that they have
“extremely” similar data. Allison notes that a fairly significant number have a
reduced window by the end of the session (initial congestion window of 32,
except when information is present which otherwise colors the data). A lot of
the reason it is below 32 is because of that.

Larry asks if there is data from mod_spdy or others? Will Chan says that Google
does not have that data. Lars Eggert notes that TCPM had a large discussion on
this and came up with 10? Why is that Google is using 32 for this instead of
iw10? Basically because it is trying to compare experience with a multi-tcp
connection experience of 50 or so because of domain sharding; that’s 500 at
iw10, vs 32. Martin suggests that this discussion should continue in TCPM,
instead of here. Will Chan takes an action to have it done--he may pass it to
Jerry or someone else.

Jim Gettys goes back to collateral damage creating head of line blocking in
sigle queue devices--creates 100s of milliseconds of latency in broadband
scenarios. If you want RTCWEB to work, you need to get this solved. Will Chan
notes that we are providing a platform--if the apps on the top of the platform
try to game the system. Jana notes that host limits on the connection provide
limits 6 doing 4 wouldn’t be much better and it can be much than 6 connections.
We can talk about this, but it is a problem worth solving.

Bob Briscoe hides a possible myth or fallacy about the ability to use a large
congestion window. This is a clocked window at the termination, but not clocked
at the restart. If you have a server interface capable of pacing, that you
could get some of this advantage back. Will Chan notes that we have already
removed this from HTTP 2.0; Bob notes that it would be good if we can get it
back. Will agrees, but he clarifies that the existing mechanism was flawed, and
that he recognizes.

Eliot Lear asks if this based on IP address? No. Will clarifies that this is
essentially a cookie--the client connects based on a stored setting.

Martin Thompson possible exhibits a bias that some web applications may not
have the same characteristics because of the server distribution--for many
people this will be within low RTT. Jokes about CDNs ensue. Mirja reiterates
that this is a TCPM topic, and it is scary that it is being presented here for
the second time. Mark clarifies that this is the first HTTPbis has seen the
data. Mirja is concerned that a solution coming from other groups may not have
the right data.

Will notes that Google runs lot of experiments. Jerry Chu notes that he has
been working with this data and he has been trying to share it. They are
working on pacing now as a result. Mark asks for continuing that information
sharing.

Martin will invite the HTTPBis folks to come to the transport area meeting.
Mark says thanks and encourages clear agenda items to encourage participation.

Then next meeting is Hamburg, next week.

