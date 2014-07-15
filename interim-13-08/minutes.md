# Minutes of the August 2013 HTTPbis Interim Meeting

* [Agenda](https://github.com/http2/wg_materials/blob/master/interim-13-08/agenda.md)

Chair: Mark Nottingham 

Participants:
* Patrick McManus (Mozilla)
* Larry Masinter (Adobe)
* Hasan Khalil (Google)
* Roberto Peon (Google)
* William Chan  (Google)
* Julian Reschke (Greenbytes)
* Alexey Melnikov (Isode)
* Carsten Bormann (Universität Bremen)
* Leif Hedstrom (Apple)
* Martin Thomson (Microsoft)
* Fred Akalin (Google)
* Lars Eggert (Netapp)
* Jan Algermissen (NORD)
* Brian Raymor (Microsoft)
* Reza Jalili (Adobe)
* Rob Trace (Microsoft)
* Jun Fujisawa (Canon)
* Hirotaka Nakajima (W3C)
* William Chow (Mobolize)
* Herve Ruellan (Canon)
* Kalyani Bogineni (Verizon)
* Tatsuya Hayashi (Lepidum)
* Mike Belshe (Twist)
* Gabriel Montenegro (Microsoft)
* Jeff Pinner (Twitter)
* Emile Stephan (Orange)
* Stephen Ludin (Akamai)
* Shigeki Ohtsu (IIJ)
* Yosuke Funahashi (Keio)

Remote:
* Gabor Molnar
* Eliot Lear (Cisco)


## Monday

### Berlin Meeting Summary

In the next month or so outstanding issues on HTTP/1.1 should be closed. 4
weeks IETF LC, then 4 weeks till IESG telechat after

A new issue about use of TLS in HTTP/1.1 and HTTP/2.0

Server have control about whether a connection is encrypted or not. Clients
don't have much control. This need to change

A joint session with Transport Area people. Alison presented HTTP/2.0 issues
from Transport prospective.

It was a lively discussion. Transport people want to help HTTPBis.

### Draft -04 Implementation

Mark is showing wiki with the list of known implementations

Mark is asking about compression and draft quality in general

Patrick: 2 flow controls - not clear about the difference

Continuations are broken

Compression is not hard to implement. Implemented in 2 days (both sides), 400 lines of C++.

No obvious bugs in the compression. Variable length encoding was better understood after the code was written.

ALPN versa NPN - the ordering of protocol is opposite.

Hitting some limit which causes bugs. ALPN can just cause timeouts

"Hello world" is running between Google, Microsoft and Mozilla implementations.

2 laptops sacrificed to HTTP2 development so far :-)

Mark N: need a separate mailing list for developers?

People not convinced. Just use existing bug tracking (e.g. in GIT)

Patrick is generally happy

Fred from Google: no surprises. It would have been nice to test the base spec without compression.

Doing SPDY 2, SPDY 3 and HTTP/2.0 in the same code base is tricky

Jeff (Twitter): a continuation frame modifies information in previous frames.

Hassan: I haven't implemented continuations yet. Do we even need them? There is one use cases for them.

Continuations only apply to headers. Should we just have a new frame type ("more headers") instead of the continuation bit.

Roberto: restrict use of continuation to HEADERS

It would be good for a new op code that omits duplicate information (e.g. priority)

The latest HTTP/2.0 requires libraries to know whether they are client side or server side in more places.

State transition table (html5.ohtsu.org) - people found it to be useful

Akamai: implementation in Perl from scratch. It was very easy. Compression was quite complicated (lots of small details).

Window update: need to always send two: one per connection and one per stream
Which seemed to be a bit verbose

Some disagreement on whether always sending 2 window updates is needed

Jeff: (Compression) Inserting a single big header (over 4Kb) will cause connection close (4Kb buffer for all headers). But writing a stupid implementation is too easy.
Akamai implementation is a proxy

Roberto: did anybody not implement flow control?

Patrick: disabled flow control on some stream and not others. An interesting case to test.

Markn N: who did NPN? 7 hangs

ALPN: 5 hands

Upgrade: 3 hands

Akamai person is Steven

Mark is editing implementation wiki

Barry: is there a reference to the implementation wiki in the HTTP/2.0 draft?

<Barry Leiba> "Implementation Status" is, I believe, the title for the section.  See RFC 6982

<Barry Leiba> I think for this, I suggest putting in a note that −04 was the first draft version for which implementations were encouraged, and that [this URL] contains the list of implementations and details of those implementations.  That's all you need: small and simple.

Microsoft OpenTech contributed ALPN patch to OpenSSL, but it was not integrated yet. OpenSSL people are quite conservative/slow.

<Barry Leiba> BTW, response to "circular references suck": Circular normative references suck.  But the reference from the http2 draft to the implementation page is not normative.  'snot a problem.

Roberto: different NPN/ALPN strings "I really want to use this" versa "this is for testing"
Discussing finer points about large scale testing and deploying experimental code

<Eliot Lear> can't servers simply query their base at that hour to opt in?

Hasan: a variety of different applications/uses is better than just increase in the number of test users (without introducing new uses).

Microsoft has no "experimental" channel. Probably will delay supporting this in IE by default until the spec is more stable. It is hard to deprecate features, due to customer demand.

Discussion about how to identify particular implementations. Are we adding user-agent strings where HTTP/2.0 version is used (in ALPN)?

Roberto: Add a new GOAWAY with "don't use this string again when talking to me" or "fallback to HTTP/1.1"?

Hasan: But GOAWAY might not fix flow control bugs. It would be nice to know client string at the beginning of a HTTP/2 session.

Mark N.: closing the discussion about implementation experience.

Martin: I sent some comments to ALPN authors about strings which are different from what HTTP/2.0 draft says.

Gabriel is talking about another TLS extension for conveying settings. At the moment there is no agreement among HTTPBis participants about whether this is the way to go.

Mike: should we ask TLS WG to reevaluate the ALPN versa NPN decision (i.e. to go back to NPN), because of new privacy awareness. I.e. NPN encrypts the choice of protocol names.

Patrick: ALPN might be tricky to deploy (the bug he mentioned earlier), prefer NPN.

Mark. N. is trying to shut down the discussion about NPN versa ALPN because HTTPBis is not the right forum.

And the TLS WG mailing list is.

Martin: the list of TLS 1.3 requirements talk about encrypted negotiation and fewer round trips. 

Which seems what people want.

Mark: "we love the TLS WG :-)"

### Issue # 1 (Upgrade mechanism)

(Issues are in github)

"Transport mapping" filter

### Issue 172

"Set a baseline for TLS implementations".

Martin: we would like to require SNI TLS extension

Are specifying a profile of TLS?

Minimal version of TLS to support?

Mark N: "MUST send SNI" - any objections?

No RC4

TLS 1.2 is required, but this might evolve over time

Twitter: we use 1.0 and 1.1/1.2 are current disabled.

### Issue # 133

"GOAWAY status code or similar meaning "don't use HTTP/2 when reconnecting" would be good"

Patrick: is this flag persistent?

Google people: no

Patrick: this is a cookie that identifies a user?

Others seem to disagree.

Patrick: it is a bit persistent between connections. Privacy team in Mozilla will object.

Jeff: most of my clients would not respect the feature. For clients I control, I can do this in other ways. Not convinced.

Steven: not high enough on a priority list.

Jeff: my expectations is that we are dealing with evil clients that try to consume resources.

Roberto: this is useful to deal with permanent problems in clients (or clients + server combination)

Is this for debugging purposes or long term purposes? Hasan: both

Mark N.: "can clients can just ignore this code?" Others: yes, it is unenforceable.

Mike: not much objection, but don't see much point

Steven: the number of implementation that will be intelligent about this feature is going to be small, in comparison to naive implementations who would just do user-agent blocking

Eliot: need to document this feature better if it is to be included

Mark. N. going around the room asking who and how is going to use this

Close the issue. Google people can play with this feature in SPDY 4. Then this can be discussed again.

###  Issue #215

Side discussion about mapping to TCP minions

Hasan: compression is THE biggest performance win. Even for mobile devices

Mark N.: reasonable happy with compression, but need to play more with it.

Most people who implemented compression didn't implement eviction.

People are asking for a test suite

Action item: Herve to start test corpus. Roberto will help.

### Issue #23

Roberto: have a different compression context for :<header-field>s and the rest? This will help proxies to inspect/extract specific header fields

<molnarg> An idea: if we would require headers to appear in alphabetical order in header blocks (and nothing else would change compared to current spec), then 1) ':' headers would always come first 2) it would be possible to implement a streaming decoder 2) it is possible to implement a streaming encoder, if its input is in alphabetical order (otherwise first you would have to reorder them).

<molnarg> okay, agree that hard to enforce

### Issue # 187

"String Literal"

<Barry Leiba> Discussing issue 11 in the compression spec.

<Barry Leiba> Contemplating closing the issue.

Talking about disabling stream control


## Tuesday

Most of Tuesday was spent on interoperability testing between implementations.
At the end of the day, we discussed what was learned during the interop session.

## Wednesday

### Martin Thompson - Draft Overview
 
#### Host header
There are conflicts with host headers with FQDNs.  Section has been re-written to say just use :host.
- Why not use host instead of : Host?  Answer is to be compatible with compression.
- Reason fields.  Use header fields instead.
 
#### Limiting Push Promise
- There will be some state on client for each push promise.
- This raises question of should we be able to turn off Push Promise completely.
- Use case for mobile client and use case for proxy is very different.
- Proxy would like to be able to see the list of push resources and then selectively allow pushed resources instead of inlining.
- Proxy Scenario discussion:
·         Client: Set MAX_CONCURRENT_STREAMS (MCS) to 0, set push promise to ON. 
·         Server: Sends Push Promise (PP).
·         Client: sends RST for headers that are cached
·         Client: sends MCS to open streams for other headers.
·         Server: Pushes remaining resources.

- Option 1: Blend MCS=0 to disable PP
- Option 2: Allow PP when MCS=0
- Option 3: Add in an explicit setting for disabling PP

What is the behavior of MCS=1?  With a setting of 1 you can expect pushes.  Unlimited number.  One at a time.

Mark: Opinion is make turning off PP explicit.
Potential solution is Even vs odd stream ID connection flow control.

Mark:  Either make an explicit option for disabling PP or change the spec to clearly define behavior (all PP with MCS=0)

Decision is open an issue to change the spec to clearly define option 2 (allowed to send PP with MCS=0).
 
### Mark - Next steps
 
#### Document schedule

- Updated implementation draft in 2 weeks.

- Do a virtual interop a couple of weeks later over Jabber.  Set aside a day for this.
 -Jeff - Compressor is the part that needs to most work.
 - 2nd interop event over Jabber on week of September 7th, focus on header compression.

- Get drafts out by the 21st.  Header Compression and draft.
Need a HC test suite - Mid September (20th)

- Herve, Fred, Roberto, Jeff - work on interop harness.
 
Long discussion on dates for next face to face interim meeting

- Lots of issues with Halloween and TPAC.

- North American interim in mid-October instead of attached to IETF.  October 9-11.

- Day of Issues, Day of interop, 1/2 day of review.  Continental US.  Probably not east coast.
 
November - Vancouver IETF

Zurich in January - Interim.  Hosted by Cisco.

London in March - IETF, Schedule an interim around this.

Melbourne in April / May - Does not make enough sense

Toronto - IETF in summer - Mozilla offered to host Interim if necessary.

Honolulu in November - IETF
 
What do we need for the October interim?
- Need 2nd implementation draft
- Compression harness
- What metrics do we want to collect?
 
Discussion on merging or separating compression spec.
- Consensus to stay separate, with same schedule for IESG.
- Call the spec HPAC (HTTP 2 Header Compression)?
 
Issues list is up to date.
-05 will not be for implementation.
-06 will be implementation draft 2.  target is August 21st.
-06 will reference HPAC draft 02.
 
New business: are we doing a press release on this meeting?  Answer is not from the Working Group.  Some companies may blog.
 
Outcomes for Mark:
- Re-arrange materials to make it more obvious what is going on here.
- Write a blog entry on what went on here.
 
Implementation testing:
- Adding granularity to the implementation list to show what features are supported.
- Creating an "HTTPbis dev ops" list.
 