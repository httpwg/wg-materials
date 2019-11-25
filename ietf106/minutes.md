HTTPbis Session 1
(Minutes by Felix Handte: w@felixhandte.com)

Related work in other fora.
Comments:
- Martin Thomson: "HTTP request signing: why isn't this already in httpbis?"
- Mike Bishop: "there's also something in dnsop"

Thanking outgoing chair Patrick McManus for his service

HTTP Priority Design Team update
Presented by Ian Swett
- Simpler can be better!
- Design team recommendation: draft-kazuho-httpbis-priority-03
- Applies to both H2 and H3
- Mike Bishop: "chrome H2 scheme is not full tree"
- Martin Thompson:
    - "I thought I'd like this more than I do."
    - "Headers express priorities, but then you talked about them in frames."
- MNot: "the question here is whether to proceed with adoption"
- Mike Bishop:
    - "Header vs. frame: if you want to allow reprioritization, you must have a frame. Is a header hop-by-hop or end-to-end? We settled on frames talk about this hop and headers talk about other hops"
- Seph: "Are there website characteristics that match different pri schemes better or worse?"
- Roy Fielding: "What about my messages, about using just a header field? Not interested in the complexities in the current draft."
- Martin Thompson: "I agree with Roy [...]"
- Roberto Peon: "Origin is oftentimes HTTP/1.1, even when client is talking to terminating revproxy with H2/H3."
- Kazuho: "We are discussing how to convey signal, not semantics. Let's close the semantics issue."
- MNot: "We don't have consensus. Where should this discussion proceed?"
  - "Call for adoptoin?"
- Martin Thompson: "Hop-by-hop or end-to-end is core. We should resolve before adoption."
- Ian: "Resolving this is hard."
- MNot: "Interim meeting? Colocated with QUIC interim?"
- Ted Hardie: "Acquiring more rooms at the quic interim may be hard"

http-core Status
Presented by Roy Fielding
- Most of the work is moving paragraphs around
- Two open errata/issues
- Issues to discuss now
  - Presented by MNot
- #258: tighten language around DELETE request bodies
  - let DELETE follow GET? a req body is bad
  - let DELETE follow OPTIONS? a req body is undefined
  - Julian Reschke thinks it's more like OPTIONS; can we also clarify when an intermediary is allowed to drop a body? Julian doesn't think they're allowed to.
  - Martin Thompson are we trying to preserve these use cases or maintaining backwards compatibility with the spec? In terms of interop, DELETE req bodies are pretty close to useless.
  - Seph: "disallowing bodies is dangerous. pushing all bodies into POST makes other methods useless"
  - Tommy: "if we're going to allow bodies, they must have defined semantics"
  - Consensus: DELETE should behave like GET
- #165: updating stored headers
  - Reviewing discussion on github issue
  - Martin Thompson: "are set-cookie in the list because they're handled elsewhere before they're cached?"
  - Next step: "put together a conservative list"
- #163: clarification of weak validators:
  - Martin Thompson: "TIL the validator applies only to the body bytes. Can we make that clear?"
- #128: quoted cache-control directives
  - Julian Reschke: "we're not ready, this is a normative change you're proposing"
  - MNot: "we failed to communicate to implementors, the spec should reflect reality"
  - MNot: "maybe we should just open bugs against browsers and intermediaries"
- #252
- #30: field-name syntax
  - Roy: "let's eliminate them"
- #99: scope of Retry-After
  - Guidance for future headers: think carefully about scope
- #237 / #194: QUIC and https://

RateLimit Headers
Presented by Roberto Polli
- Roberto Peon: "this and priorities share some characteristics, same kind of hop or end-to-end scope question" "ratelim, esp. + cache poisoning = dos"







Thursday, 21 November 2019, Afternoon Session I (Core)

Administrivia
3 min - Blue sheets / scribe selection / NOTE WELL
2 min - Agenda bashing


# Other WGs

## SECDISPATCH - Mark

Request signing discussion; draft will be forthcoming for WG review.
Information about credentials used on forward hop from CDN

## DNSOP - Tommy

SVCB/HTTPSSVC adopted by dnsop; bikeshedding on names will happen on their list.
On track to finalize format and early allocation of codepoint soon.  Please look at encoding in next few weeks.

# Priorities Redux - Ian
10 min - HTTP Priorities
Terser names for things to save bytes, but concept of priority expression is unchanged
One scheme conveyed two ways:
    Header is end-to-end (initial prioritization, server override)
    Frames are hop-by-hop (reprioritization, difference from headers)
Setting indicates preference to use "urgency" vs. HTTP/2 style settings
Draft revised last night to reflect current technical discussion.  CFA ~now.
MT questions whether we need reprioritization, but that's not an adoption blockers.
Robin Marx points out that frame is not just for reprioritization, but also hop-by-hop.
MNot suggests virtual interim for hashing this out.


# Extension Drafts

## Digest Headers - Lucas Pardue

Was Resource Digests
Recap of draft:  Header field with digest of the message payload

Last IETF, Roy asked for people's use cases for Resource Digests.  Not in draft yet, but will discuss.
-01 changes:  Editorial, discuss state-changing methods, reboot of IANA registries, and relationship with SRI

### Change 1:  State-changing methods
Julian clarifies that POST and PATCH are not special cases; Lucas says this is already a general principle.
Discussion about whether digest should always refer to the complete representation for generality

### Change 2:  IANA
Adds "recommended" column; MD5 is now deprecated

### Open Issues

Issues 936/937:  Discussion of how validators specify a resource
MNot:  This language reflects concepts HTTPbis moved away from.  Roy can help align with modern terminology.
LPardue:  Yes, updating the language is the point of this doc.  Please help.

Issue 851:  Using Digest in signatures
Do we need further guidance?
MT:  This gets really hairy.  Not everything is needed.
Roberto Polli (later):  This draft started because I messed up signing content; the definition wasn't clear.  It's worth including this guidance.

Issue 852:  Threat model
MT:  This is tricky.  On one level, make sure this hasn't been modified, but the hash could also be modified.  Stay away from that; focus on building blocks.

Issue 849:  Digest of empty representations
An empty representation might not have an empty message; what specifically is the digest referring to?
MT:  Follow the same rules of what you're taking the digest of.  This isn't a special case.

Issue 850:  BNF of "parameter"
MNot:  Should be something in core you can reference

MNot:  Editors are soon going to be ready for wide review.

## Client Hints - Yoav Weiss (remote)

Several changes based on feedback; biggest is to remove the separate Accept-CH-Lifetime and tied to Session Cookie lifetime instead

Some pending PRs, but close to being done.  Want feedback on anything that's still needed.
Want to expand discussion of security (what MUST NOT be defined as a hint, for example) and discuss the "Sec-" prefix

MT:    Sec prefix sets sites from setting the value themselves in code, particularly in cross-origin requests.  Server might be unprepared.
  Coupled with the desire to have these fields on the first request.
Yoav:  Want to avoid preflights.
MT:    Discussion with Anne van Kestren about origin policy et al.; would prefer to put my effort there, even if that means preflights for these.

Yoav:  Specific use cases for user-land client hints?
MT:    Service worker trying to populate cache wants save-data version for various reasons.  Could come up with others.
Yoav:  What about same semantics for Sec- and non-Sec hints, and server decides what to accept?
MT:    Would rather solve the problem than carry baggage like that forever.  Sec- prefix is a blunt instrument.

Would like to see draft move further along soon.  Chrome will ship UA-CH soon, and would like to see this hooked into origin policy documents.

MT:    You don't define any actual CH instances in this document.  We could advance the architecture doc without settling the Sec- prefix debate.
Tommy: Can you do a PR with that soon?  And the other PR should probably get more details.
MT:    Let's publish the document essentially as-is.  We'll never be totally happy, but the disagreements are policy, not technical.

## Cache-Status - MNot

Redux of X-Cache would have led to lazy implementations getting it wrong.  Made some changes to expose more information.
Notable change:  The primary token is the identity of the cache, and the parameters are the things it wants to expose.

If people are comfortable, we might want to make the same change elsewhere.

Please read and review.

Alessandro G.:  Also close my PR.
Chris Lemmons:  Please allow for extensible information about types of hits (memory, disk, etc.)

## Proxy-Status - MNot

Issue 801:
    Assuming we make the same change as Cache-Status, we don't need to take the proposal to split this into two headers.
    
Issue 808:
    Currently, "errors" are reflected by HTTP status codes.  Replaced with error codes in the draft.
    Having misgivings about this approach, so looking for feedback.
    
    ???:  What happens when there's a new status code?
    MNot:  Register both places.
    Piotr: Switch to key/values and give the raw status code.
    
    Roberto Polli:  Status message could change, even if status code doesn't.
    MT:  Makes sense to record the status code you got; there can be other codes for non-request errors that can occur.  
         Putting everything in the TOC is scary.

## Variants - MNot

Added sketch of how varying on cookies might work.  PLEASE review this.

Existing issues are manageable.  Then we can publish as Experimental, since there's not a lot of implementer interest.  Or are people implementing?

MT:  WPack is depending on this; this should be standards-track.  If we go Experimental, we'll need to revise pretty quickly.
MNot:  If need be, we can also flip the draft later.
Jeffrey Yaskin:  We're using Variants with a draft number in WPack.  If we make changes post-RFC, we need a new header name instead.

Will keep for a while and wait for experience.  If there's implementation experience, great.  WPack experience isn't dispositive for the web.

## BCP56bis - MNot

Got a comment from Fluffy; need to rev the draft.
Fairly large revision recently based on the feedback on revisions of URI ownership RFC; give guidance, be less normative about requirements.
Please do review, but there's another editorial pass coming.
We'll need to do another WGLC.

## Secondary Certificates - Mike Bishop

Draft stable, but can't progress until we have more implementations

MT, Pat McManus:  Don't want to advance without implementations, but don't want to drop the draft.  Fine to keep this around.
???:  We have an old client-server implementation, but haven't touched it lately.

## Structured Headers

Lots of tests in the test suite, and parsers are coming.  Number representation is still thorny.
MT:    Support the move from float to decimal.
MNot:  Proposal is a name change only.
MT:    Uh-oh.  Last time, we prefered a fixed-decimal representation, even though it prohibits some unlikely uses.
MNot:  Most active spec contributors aren't here, so that limits our ability to discuss here.
       Want to be able to map things that are used in current headers, so q-values is the highest priority.
MT:    That doesn't need a huge dynamic range.
Chris Lemmons:  Does anyone use more than two digits for q-values?
Roy:   Three.
MT:    We need to make a choice about times, but maybe not solve that now.
MNot:  There's backporting thing that are at 1-second resolution, but then there are proposals at millisecond-timing.
       Not clear that's a good idea, but those could be an integer instead of a floating point anyway.
       How do people feel?

(Smattering of applause)

Will make a proposal on list to move to a fixed point, but want feedback on that idea.

Hum on whether to switch to fixed-point for all fractional representations:  Strong + 4 on Jabber
Hum on whether to retain floating point:  Some

Chris:  Worth noting that floating-point proponents are mostly not here.
MNot:   I need to go engage with them.  Don't think anyone already using SH is using decimals.
Robert Peon, Facebook:  Lots of hardware doesn't even have floating-point units; would have to convert to fixed-point.
Julian:  Can drop fractions entirely; define an extension later is needed.
MNot:   Would rather retain so q-values can be represented.
MT:     Also makes it easier to integrate into the spec and ensure proper parsing
Julian: q-value can be sent as a 4-digit int.
Jon Lennox:  If the only use is q-values, what about a tighter specification for numbers between 0 and 1?
MNot:   Not much harder, but more useful to allow a wider range.
Julian: The goals for this spec seem to change periodically.  Is backporting a goal now?
MNot:   Not in this spec, but in a future spec.

Otherwise, the spec is almost ready to go.  Please review; WGLC in 2019 is ideal.  Clock is ticking.

RPeon:  Priorities wants to depend on this, as do several others.
Julian: We said that the URI type isn't needed because backporting isn't a goal.
MNot:   No, we said that it was hard to define with good interop.

## 6265bis

Lots of open issues.  Will talk with editors about how to get this moving.

# New work

## Compression Dictionaries - Felix Handte

Dictionary-based compression gives added wins, and we want to save bytes.
Drawback that stopped previous attempts was security.  Need to understand security properties before we can ship one.
Draft explores security risks and mitigations.

Two categories:
    CRIME/BREACH/HEIST-style:  Compression across attacker-controlled and secret contexts permits guess-and-check
      Dictionary is vulnerable to this, if the dictionary is a secret
    State-based vulnerabilities:  Need to create, distribute, negotiate, and retire dictionaries; implications of how you do those.

MNot:  Lack of this has been our barrier to standardizing dictionaries before; this is great to have.
Roy:   Want this for other things as well.  Please adopt.
Felix: Tried to keep it generic, but it motivates work in this WG.

MNot:  Will work with the ADs; maybe goes to SecDispatch?

## Transport Information Header - James Gruessing

Response header that exposes information about the current connection -- RTT, server's cwnd, etc.

Ian S: Did you consider this as a request header as well, to let responses vary based on connection properties?
Ian S: This seems like a hop-by-hop header.
Chris Lemmons:  The browser already has access to this.  Isn't this an end-run around the browser's decision not to expose in JS?
James: W3C NetInfo doesn't expose everything, and can't get server-side info.
Ted H: Assuming this isn't going to inform the OS network stack?
James: Don't plan to.
Robin Mark:  This is a very coase signal, only one per request.  Is it useful?
James: Can include multiple samples per response, but definitely coarse.  Useful enough for some things, but you wouldn't use it to drive a transport.
Yoav W:NetInfo exposes rtt and speed as client perceives them, but will likely go away for privacy reasons.  How are you planning to expose this?
James: JS can see headers.
Yoav W:Think about the privacy properties.
Tommy: +1 on privacy.  This seems overbroad; target the scenario more precisely.  Inaccurate at the start of a connection and trailing as you get further in.
Ian S: Can't get cwnd locally, because it's the peer's info.  But why standardize?  Server controls both headers and JS.
James: Because lots of implementations do this differently.
Lucas: With intermediaries, might want to expose info about other hops as well.
Chris: Sounds like browser has explicitly decided not to expose this info to JS.
Pat M: What's the relationship between this an Server Timings?
       Interpretation of cwnd will vary between congestion controllers; delivery rate might be more portable.

MNot:  How many digits of precision do you need in that timestamp?  (General laughter)

# Core Redux - Issue 986

    Mid-stream trailers (issue referred from QUIC WG) could be used in multiple situations:
        Progress indications
        Mid-stream timing
        Non-critical metadata to avoid blocking important body
        Long-poll metadata
        

Envoy proxy already has an H2 extension for the METADATA frame (camping on a code point; boo!)

Ian S: I know who wrote this, and we support it -- if we support trailers.  Call these "middlers".
RPeon: Is this for H2? H3? H1?
Roy:   This is H2; H3 already has an issue and sent it here.
RPeon: Semantics here get interesting, and will take a while to figure out.
       Is the location significant?  Do they have to be forwarded?  Do they have to be forwarded in the same location?
Roy:   Want to co-edit with me?
RPeon: "I can try, but good luck."
Robin: Looks interesting in terms of Priority updates.
MT:    Not useful for priority, because the stream will be gone by the time you want to send updates.
       Please don't camp on code points.
       Without negotiation, can't use full HPACK.
Julian: Should we consider assignment of frame type numbers?
Roy:   Camping happens all the time.
MNot:  Don't have strong feelings about the wire encoding.
       Looks interesting, but the history of trailers is (redacted).  Implementation is really trailing.
       I'm worried if we introduce something "like" trailers neither this nor trailers will succeed.
Piotr: Originally designed as replacement for hop-by-hop headers
Mike Bishop:  Early trailers are fine.  Lots of trailers at different times is potentially challenging.
Lucas: +1 -- how do I know when the set of trailers is done?
Roy:   Modifying spec to reflect Fetch, to keep headers and trailers separate.
RPeon: If there's not demarcation between sets, then repeated updates could be misinterpreted.

MNot:  Who is interested?
(lots of hands)
Tommy: Where does it live?
MNot:  Issue on core; potential H2/H3 extension.







