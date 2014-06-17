# HTTPbis New York Interim Minutes


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Thursday, 5 June 2014](#thursday-5-june-2014)
  - [Administrivia](#administrivia)
  - [[Frame type extensibility](https://github.com/http2/http2-spec/issues/95)](#frame-type-extensibilityhttpsgithubcomhttp2http2-specissues95)
  - [[Requiring Client Content-Coding Support](https://github.com/http2/http2-spec/issues/460)](#requiring-client-content-coding-supporthttpsgithubcomhttp2http2-specissues460)
  - [[Compress segments rather than frames](https://github.com/http2/http2-spec/issues/466)](#compress-segments-rather-than-frameshttpsgithubcomhttp2http2-specissues466)
  - [[Only restrict HTTP application data and header block fragment lengths](https://github.com/http2/http2-spec/issues/456) (proposal)](#only-restrict-http-application-data-and-header-block-fragment-lengthshttpsgithubcomhttp2http2-specissues456-proposal)
  - [[Need way to negotiate "no Huffman" in settings](https://github.com/http2/http2-spec/issues/485)](#need-way-to-negotiate-no-huffman-in-settingshttpsgithubcomhttp2http2-specissues485)
  - [[allow intervening DATA frames](https://github.com/http2/http2-spec/issues/481)](#allow-intervening-data-frameshttpsgithubcomhttp2http2-specissues481)
  - [[Changing the way that altsvc use is indicated](https://github.com/http2/http2-spec/issues/474)](#changing-the-way-that-altsvc-use-is-indicatedhttpsgithubcomhttp2http2-specissues474)
  - [[Flushing Alt-Svc Cache](https://github.com/http2/http2-spec/issues/444)](#flushing-alt-svc-cachehttpsgithubcomhttp2http2-specissues444)
  - [[Enabling redirects to other hosts](https://github.com/http2/http2-spec/issues/492)](#enabling-redirects-to-other-hostshttpsgithubcomhttp2http2-specissues492)
  - [[Intermediaries and Alt-Svc](https://github.com/http2/http2-spec/issues/462)](#intermediaries-and-alt-svchttpsgithubcomhttp2http2-specissues462)
  - [[Refine Prior Knowledge](https://github.com/http2/http2-spec/issues/418)](#refine-prior-knowledgehttpsgithubcomhttp2http2-specissues418)
  - [[Race condition in shutdown for proxies](https://github.com/http2/http2-spec/issues/458)](#race-condition-in-shutdown-for-proxieshttpsgithubcomhttp2http2-specissues458)
  - [[Priority for closed streams](https://github.com/http2/http2-spec/issues/468)](#priority-for-closed-streamshttpsgithubcomhttp2http2-specissues468)
  - [[Enable weight of 0](https://github.com/http2/http2-spec/issues/436)](#enable-weight-of-0httpsgithubcomhttp2http2-specissues436)
  - [[Accounting for Proxies](https://github.com/http2/http2-spec/issues/413)](#accounting-for-proxieshttpsgithubcomhttp2http2-specissues413)
  - [[State Diagram](https://github.com/http2/http2-spec/issues/484)](#state-diagramhttpsgithubcomhttp2http2-specissues484)
  - [[Privacy considerations for Alt-Svc](https://github.com/http2/http2-spec/pull/501) (proposal)](#privacy-considerations-for-alt-svchttpsgithubcomhttp2http2-specpull501-proposal)
  - [[BLOCKED should be an extension](https://github.com/http2/http2-spec/issues/500)](#blocked-should-be-an-extensionhttpsgithubcomhttp2http2-specissues500)
  - [[ALTSVC as an extension](https://github.com/http2/http2-spec/issues/499)](#altsvc-as-an-extensionhttpsgithubcomhttp2http2-specissues499)
- [Friday, June 6](#friday-june-6)
  - [[Make alt-svc an extension to the spec](https://github.com/http2/http2-spec/issues/499)](#make-alt-svc-an-extension-to-the-spechttpsgithubcomhttp2http2-specissues499)
  - [Deployment, Adoption and Roadmap](#deployment-adoption-and-roadmap)
  - [[Prioritisation as an extension](https://github.com/http2/http2-spec/issues/506)](#prioritisation-as-an-extensionhttpsgithubcomhttp2http2-specissues506)
  - [[Forbit/Permit Coalescing](https://github.com/http2/http2-spec/issues/490)](#forbitpermit-coalescinghttpsgithubcomhttp2http2-specissues490)
  - [[HTTP URIs over TLS](https://github.com/http2/http2-spec/issues/315)](#http-uris-over-tlshttpsgithubcomhttp2http2-specissues315)
  - [[TLS Renegotiation](https://github.com/http2/http2-spec/issues/363)](#tls-renegotiationhttpsgithubcomhttp2http2-specissues363)
  - [[restrict cipher suite selection](https://github.com/http2/http2-spec/issues/491)](#restrict-cipher-suite-selectionhttpsgithubcomhttp2http2-specissues491)
  - [[Service header field to SHOULD](https://github.com/http2/http2-spec/issues/502)](#service-header-field-to-shouldhttpsgithubcomhttp2http2-specissues502)
  - [[simplify padding](https://github.com/http2/http2-spec/issues/505)](#simplify-paddinghttpsgithubcomhttp2http2-specissues505)
  - [[mandatory to implement cypher suite](https://github.com/http2/http2-spec/issues/498)](#mandatory-to-implement-cypher-suitehttpsgithubcomhttp2http2-specissues498)
  - [[Remove frame-based compression](https://github.com/http2/http2-spec/issues/497)](#remove-frame-based-compressionhttpsgithubcomhttp2http2-specissues497)
  - [[Never indexed representation constraints](https://github.com/http2/http2-spec/issues/508)](#never-indexed-representation-constraintshttpsgithubcomhttp2http2-specissues508)
  - [Next Steps and Wrapup](#next-steps-and-wrapup)
  - [Operational Advice](#operational-advice)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Attendees

* Mark Nottingham - Chair
* Barry Leiba (Huawei)
* Hasan Khalil (Google)
* Will Chan (Google)
* Brian Raymor (Microsoft)
* Martin Thomson (Mozilla)
* Sanjay Mishra (Verizon)
* Daniel Stenberg (Mozilla)
* Patrick Mcmanus (Mozilla)
* Stephen Ludin (Akamai)
* Saurabh Kulkarni (Akamai)
* Mike Bishop (Microsoft)
* Tony Hansen (AT&T)
* Ilya Grigorik (Google)
* Peter Lepesky (Viasat)
* Julian Reschke (greenbytes)
* Salvatore Loreto (Ericsson)
* Jeff Pinner (Twitter)
* Gabriel Montenegro (Microsoft)
* Liliana Dinale (Ericsson)
* Emile Stephan (Orange)
* Richard Wheeldon (Cisco)
* Christoph Brunhuber (IAEA)
* Martin Nilsson (Opera)
* Herve Ruellan (Canon)
* William Chow (Mobolize)
* Daniel Sommermann (Facebook)
* Shigeki Ohtsu (IIJ)
* Dan Druta (AT&T)


## Thursday, 5 June 2014
 
Scribe: Dan Appelquist (DKA)

### Administrivia

Blue sheets, scribe selection

Please review the http 2 FAQ (http://http2.github.io/faq/), and suggest updates
 
 
### [Frame type extensibility](https://github.com/http2/http2-spec/issues/95)
 
mnot: First issue, frame type extensibility.  As an overview, a number of people have said "maybe we should rethink extensibility" because it keeps coming up.

mnot: we shouldn't open up extensibility willy-nilly.

?: there is extensibility using [...]

mnot: this is about frame type extensibility - whether we want to add a new frame type

Mike: the basic concern is if we want to add a new frame type, using the alpn string,... what combination of things to support. We want to add a new frame type and have understandable semantics if you see something you don't recognize. my proposal [] adds a tag, if you overflow the frame type space you can get an expanded frame, martin's [proposal] says you only get 16 bits... I think 16 bits is probably plenty

Tony Hansen: difference between utf8 and ucs for unicode... there is an advantage to having an algorithm stating how to expand it if you need to

Mike: the pieces we have in common - some sort of end-to-end frame that most ... if it's state-changing you have to negotiate it first. The high level idea: when you want to establish a connection you need to agree with the other party that you want to do it otherwise only use what the other party can accept.

?: when thinking through - if you have hops that are not http2 then it gets lost. If you have anything cached then it gets stripped out... put the work in to put the extension frame in ...

Mike: [for example], blocked is a useful idea for an extension...

Jeff: but it's not end-to-end

Mike: they can't have semantics that you have to have to process the response. You could throw in a hash of the content...

Jeff: where's your end to end frame layer state?

[some discussion on how this applies to streams]

WIlliam Chan: why are we bringing up extensions again compared to just using [existing mechanims]? ALPN token

mike: new things keep coming up and I don't think that's gonna stop. As we use that in the real world we'll keep finding "one more thing" we want to end.

William Chan: one thing that would be interesting: google has mentioned a few times about other things we'd like to do, if we have extensibility we could do [xyz]... we've been using existing mechanisms for SPDY experimentation.

Mike: trying to express what combination of extensions you support - you have to advertise more and more ... 

William: [question of whether these new features would require a new extensions mechanism]

Patrick: the complexity is there whatever mechanism you use.. don't feel that it makes the protocol more robust. We have a small set of state transitions within the protocol as it is. And the notion of arbitrary extensions - I'm not sure we're building anything of same robustness... I like [mike's] draft. I think we already made the right decision though - let's figure out what we want http2 to do and then when we want something different do that as 2.1, etc... we're talking about this because we don't know what we want.

mnot: i'm conscious that people here are willing to put effort in. there are lots of people who want http2 to be stable for a long period of time. I'm not sure that adding this kind of extensibility lengthens the life of the protocol.

William: If the extensions are rich enough that you could do e.g. push as an extension - that would be worth it. But [I can't see that kind of use case...]

Mike: why couldn't push be done?

[discussion on whether push could be implemented with the proposed extension mechanism]

mike: we also noticed that compressed data introduces a new flag - alt svc introduces a new frame.

Jeff: in spdy we do it as a header. [we should be considering] things that cannot be done in the current http extensibility model. For these things that are a negotiated change to the protocol - it's not transparent.

mnot: in reality to do anything interesting you have to write a new protocol - so I think we'll end up with http3, http4 - 

jeff: once you talk about negotiating extensions you don't have to put it in the spec.

mnot: "if we negotiate the setting then this frame type is not available"

jeff: yes.

Mike: we define that if you don't see a setting mentioned then it defaults to "off"...

jeff: where "off" means default behavior under http2.

mnot: the approach means you can negotiate any settings "for this hop".

jeff: the change that would be required - settings have to become "ignore if you don't understand".

martin: [question of how settings are signaled...]

martin explains how this would work with the existing SETTINGS

jeff: you can either take the delay...

wheeldon: what's the alternative to alpn in the plaintext case?

jeff: upgrade h2 ...

Mike: you can still use setting for negotiation...

jeff: for true non-interpreting intermediaries, e.g. tunnels, they can't inspect - we've said in the spec that if you see a setting you can't understand then you fail the connection - [hence that would have to change in the spec]

Martin: I think opening extensibility for frame types and settings would allow us to do the sorts of things we're talking about but nobody is screaming for an end-to-end extensibility [mechanism]. 

William: who is interested in using this? what is the concrete case? would your rather use alpn?

Jeff: all of our deployment experience has been over TLS so intermediaries treat it like a tunnel. We don't have experience with true intermediaries. Thats the only place where I think this might be useful - and we don't have experience doing that. e.g. intermediary boxes that require a firmware upgrade to handle new extensions...

mike: honestly that's a reason to get it into the spec. if you define a new alpn token the intermediary won't speak it, but if we define an extension mechanism then we can define that intermediaries "pass" extensions.

Patrick: does anyone have a plan for an extension that we're going to build and test or is this just an escape valve?

Mike: i think there are some pieces of the spec that could be implemented as an extension - e.g. blocked... 

Patrick: we've all expressed interest in winding down. I don't want to rearrange the whole spec. If we adopt it we need to be confident that it works and we don't have any candidates.

Jeff: browser to server we need to have implementation experience.

mnot: there are many things in play - you can negotiate the settings and then all bets are off - then there's the question of a "must ignore" for new frame types which is a separate question I think.

mike: I'm hearing "no" on the extension frame type.

Martin: i'd be happy without one.

Jeff: what we have experience with is "drop what you don't understand."

mnot: negotiate changes in settings but ignore what you don't understand.

jeff: what that means is that you can rfc an extensibility model - an extension extension to http2. you can have an rfc that is the extensibility mechanism.  [expands on this]

Mnot: only concern is the scenario - where everyone goes off and creates extensions and there are collisions then it could get messy.  If you are going to start creating extensions then you need to coordinate.

[roberto comment on "what is http2" - please paste someone]

roberto_peon: Thx: 'hint'-style extensions should not need negotiation before use (else they're not usable for an RT minimum), they should be ignored if not understood, though a mechanism to say 'stop' should be there (which could be the negotiation). 
roberto_peon: Extensions that change protocol semantics, of course, must need the negotiation.

martin: frame types - I don't think we can change the size of these [8 bit] - my proposal includes an IANA registry with a small experimental space.  I am updating the pull request.

mnot: in principle we agree that we want a limited extensibility mechanism along these lines.

Martin: before we say that it's the mood in the room.. i want to make sure that it's true - accepting extensibility is adding complexity. We want to make sure we're getting a good bang for the buck.

mnot: we're not saying "this is how we're going to proceed" - it's small changes to the document, not requing implementation changes... 

jeff: does that mean we take out alt svc, ...

mnot: no, because we want to get this thing done.

jeff: if these things are not removable with this extension model...

patrick: I push pack a bit - it's a significant operational change. the way that it could be used.. I'm suspicious that we're not buying enough for that complexity. I like the current model.

mike: on that basis, we could say even informative extensions need to be negotiated...

william: lots of these types of extensions we don't want to [wait for?]

mike: ... case were the client wants to send an informative frame on the first request.

mnot: i hesitate to bring it up but one factor that brings to mind - what is the future going to look like. if people think it's likely we'll be working on http3 then we could just say http2 doesn't have extensibility...   we don't need to have that conversation right now, but if we're going to have a new version of the protocol in the not-to-distant future then maybe we don't need the extensibility mechanism right now.

william: is there a value to having these extensension mechanism...

Stephen: the only argument I've heard agains the ALPN is the namespace issue...

Jeff: and the "firmware" [middlebox] issue.

mnot: that's if you believe we have a well layered...

[some discussion on streams]

mnot: what should we do now, jeff?

Jeff: i think if we think it's valuable to reconsider extensions in the spec then we should consider doing it, writing it in such a way that it's hop-by-hop, and not opening up that you can receive any frame type that you want... 

mnot: more aligned with what mike proposed.

Martin: how does varying an identifier change...?

jeff: putting everything inside a frame ties it to a steam state.

martin: no matter where you put the identifier...

mike: I think if we're focusing on the hop-by-hop case, stream0 seems a logical place... part of the goal is to "leave the door open" - the question is how tightly to shut the door on extensions.

jeff: hardware [e.g. load balancers] are going to need to do this -  if I can interpret it at stream0 then I'm writing the proxy in software and the idea of why extensibility is useful (in my mind) goes away. if we think: "http2 is going to be widely deployed - there will be middle boxes" ...

mnot: more concerning case is middle boxes that are out of control of either sender or receiver. We're flapping wildly back and forth... we've gone back and forth on this. maybe we made the right decision in zurick [to not do an extensibility mechanism]. we can't do this and stick to our timelines.

martin: (conversely) we've got people coming to us and saying "you did it wrong." this is an answer to them.

jeff: it could be saying "here's your extensibility mechanism". Lots of mailing list traffic on whether we did it wrong.

Barry Leiba: http1 succeeded because it was simple.

mnot: this is going to blow out the schedule.  

DKA: concern whether an extensibility mechanism will appease the people criticizing the process here. and the schedule is important.

Martin: we have people pushing hard on this and Id like to say "fine - understand your concerns - write an extension."

? what is the guidance of whether something should be which kind of extensions ALPN.

mnot: the answer has been to use ALPN.

mnot: pushing back - if we get through our issues list today and tomorrow then we can go to working group last call. if we do extensibility then we will blow the schedule out.

Johnny G: is there value to saying how you can use ALPN tokens...

mike: it's combinatorial explosion ...

mnot: I'm more interest in getting good itnerop of one ALPN token right now.

jeff: when you talk about 

Daniel S: couldn't the extension model be a proving ground for next generation of http?

mike: I think there could come a time where "these 5 extensions are widely deployed - http2.1 means http2 + these extensions]

Barry L: I like the idea that you can prototype extensions with alpn tokens.  As AD when you do the write up you need a good paragraph on this discussion...

mnot: where do we sit? I hear people saying "use ALPN tokens" and "we need more extensibility." Options are : leave it as alpn tokens [post-zurich] or we need to have a serious conversation about extensibility. Not something we can do in the next couple days.

mike: for me, we've had the zurich discussion and the whole time after that we've heard "maybe we didn't make the right decision."

mnot: the reality is we have to ship it.

Roberto: so... what I would love to see would be that h2 allows ignorable frame types that can't change protocol semantics and any extensions that does more than that be ... [h2e for example]. that gives us both worlds.

mnot: we would define h2e?

[now or later?]

Roberto: yes and later.

mnot: if I understand it - it would be that the only change would be to ignore frame types that you don't understand.

Mike: should we make it frame types and settings?

jeff: i would say no because we have implementation experience in the former but not the latter.

Daniel S: ignoring frames seems 

Patrick: but then these are the scenarios - the other end has a bug - this adds significant complexity. any time there's a mismatch...

mnot: take a moment - how important do people think this is in relation to time. Are we willing to blow out the schedule to get extensibility right?

martin: the answer is obviously no because getting extensibility right is impossible.

martin: there's a whole rfc on this topic...

?: I like the approach of having the lenient h2 ...

martin: that's what roberto is saying...

jeff: h2e would be defined as h2 + extensions...

mnot: but roberto's approach wouldn't make patrick happy...

?: I would propose a stricter one - h2 and h2e where you could send unknown settings and frames...

DKA: You don't know if the extensibility mechanism you've defined is the right one...

patrick: the only extensions I'm aware of  web sockets should have gone into the protocol itself... and other extensions have not materialized.

[some debeate]

patrick: the world is not beating down the door for extensions to web sockets.

gabriel: my observation - we were presumptuous in zurich about not needed extensibility. we could realize we were too presumptuous. this proposal for laying the ground work - from the pov of schedule - we could make the decision that if one more frame is to be defined then we say "no." ship http base, and extensibility later.

jeff: I think everything that has come up is something we don't want anyway.

Martin: I think we made about 20 different extensions - purely between the client and the proxy - since we have the client and the server - perfectly good to just do it but we'd prefer middle boxes to work with it...

jeff: we have a pseudo metadata model - for control channels - that's all within the framing layer. anything like that - parental control - doesn't fit in the extension model anyway. We're talking about non-semantic signaling. 

jeff: for frame layer extensibility whether it's metadata in headers ... we're defining the multiplexing and connection coalescing capabilities of the client. Saying that your 

martin: i changed my mind - i agree with mark.   if we continue to discuss in this fashion then we're not getting anywhere.

mnot: my position is informed by my experience of [how long it takes] to discuss extensibility.

martin: let's leave as is / or take a proposal

martin: i've put in a pull request.

mike: i support.

mnot: one implicit proposal : the status quo; martin's proposal; 

roberto: proposal allow unknown frametypes on h2. semantic extensions on h2-e, TBD later.

[reviewing https://github.com/http2/http2-spec/pull/493]

? : only difference I would suggest is "an endpoint may send a settings of 'i know there is a extension type of this id, please don't send it to me."

Mike: that was in my first draft but I pulled it out.

[discussion of whether you need this]

? : wI will say that google's servers would be more inclined to [support what the spec says]

mnot: let's assume that some of this strict mode would be part of martin's proposal.

? : you would send a settings strictmode=true 

martin: and once you get an ack you would be fully entitled to send protocol errors.

william: what to clients do - 

mike: semantics of strict mode would be : don't send me any frame that I haven't asked for.

mnot: this smells like a committee compromise.

mnot: so we have status quo; martin's proposal; any other proposals?

mnot: what people prefer of those two proposals? And what people can't live with either of those two proposals?

jeff: [anecode] when we did spdy we had to add a settings identifier that was not in the spec... spdy at the time had nothing about settings you don't understand. after more implementation experiences [we realized] we needed a signaling parameter.

mnot: that's good input - we need to see wether we need a [didin't hear]

mike: we intentionally do ignore unknown frame types - so at least 2 implementions have done this.

patrick: you're not dropping unknown frames...

[dropping known frames vs. known frames vs. unknown frames]

[the inevitable hum-vote]

recorded : no hums for "can't live with status quo" or "can't live with martin's proposal"

recorded : more hums in favor of martin's proposal than "status quo."

recorded : many "can't live with" Roberto's proposal.

mnot: what do people think about that 

[discussion of a change to martin's proposal and whether it's worth pursuing]

mnot: it's a settings you send that say "I don't want extensions"

mnot: I worry about the complexity it adds.

jeff: I don't think it's going to be complex... lots of things will get dropped.

[more discussion on this point]

william: [in favor of strict mode] 

mnot: if we specify the strict mode which implementers will turn it on by default?

[Yes from 3 implementers...]

mnot: does strict mode apply only to frame types or also to settings?

[consensus only frame types]

roberto: there are a couple of variations that are interesting - browsers can switch into strict mode after on RT. Whole idea is to try new stuff. So 99% of time you can be in strict mode. 

[some further debtate]

mnot: if we don't put strict mode in will you [object]

patrick: I think solving complexity with complexity is the wrong engineering path. from a committee point of view I think it's the wrong design decision... I think the status quo is the right thing. I think if we have extensibility we will have an extensibility committee which is not in the long term interest of the protocol. That way lies madness. I think the history of the extensibility mechanism of higher layer protocols hasn't been successful. [In this context] i think it's a useful attribute, but if everything's going to have it on then why bother?

martin: strict mode could be an interesting extension.

william: only way this will work is from the beginning we have some extensions.   if it's not in use from the beginning then people won't implement it.

patrick: you want people to prove it out... you're gonna have interop problems. we will not have made the protocol stronger.

mnot: my experience has been that when you have extensibility it becomes a vehicle for vendors to exert power over interop. doesn't foster interop and community.

jeff: what extensions are available in tcp? how many of these are used?

mnot: but the implementer community is different?

[discussion on tcp extensions and how useful these have been]

william: if we have extensions we get some early ones in and unless we have big implementers that are randomizing extensions then that's the only way we can keep it clean...

jeff: that goes back to taking some things like blocked out of the spec and turning them into extensions...

william: we can take some frames and move them out to extensions but unless we do the randomized extensions - let's say chrome - and then we have a name collision in the future ...

mnot: personally I agree with [patrick] on staying with status quo.

jeff: in http2 because of the interop problems we've seen we should be strict front he start. 

mnot: you stated you only want to implement across TLS - 

jeff: my concern is with load balancers, firmware, etc...

mnot: but martin's proposal would satisfy this...

mnot: does anyone think we need the negotiation mechanism for strict mode?

martin: I don't think we want it.

mnot: an alternative would be : you sent too many extensions.

jeff: it makes it so that later specs can still be compliant to h2.

mnot: anybody still want to stand up for doing strict mode.

mnot: let's re-do the hums.

[slightly more hums for "can't live with martin's proposal" and slightly more humming for "status quo". Still no hums for can't live with status quo.]

[discussion of whether people who prefer extension mechanism really can still live with status quo]

martin: who is going to have significant pain...?

mnot: we do have a mechanism now, the alpn token...

patrick: we can implement [the extension mechanism] but I still think it's the wrong decision and I think it's going to [blow] the schedule.

martin: that's why I suggested the coin toss?

mnot: it's more important to make a decision.

[a coin toss]

[The coin toss results in martin's proposal]

mnot: we're going to follow martin's proposal with a few tweaks, without strict mode. Anything else to talk about with extensibility?

Jeff: what about alt svc - ?

mnot: this is my concern - that people will use extensibility to [take things out] that they don't agree with.

martin: i think it's worth bringing up because there wasn't strong consenus on adopting these [alt svc, blocked, per-frame compression].. we now have the escape hatch [extensions].

mnot: per-frame compression is optional.

mike: in my draft in an appendix I define a compressed data frame.  

mnot: a lot of people didn't want it because they didn't want to use it.

mnot: there are a wide variety of use cases... 

jeff: padding... could be put into the extension framework... the 

[discussion now on given that we will have martin's proposed extension mechanism, what if anything needs to be brought front he core spec to become an extension]

martin: feedback that I've had is that what we have is unfortunately necessary.

mnot: moving on, incorporating martin's proposal without strict mode. and that will close that issue.

mnot: if showstoppers come along we can introduce new settings or error codes post-facto.

william: we will have defacto standards emerge...

patrick: we already have that and it's not good...

mnot: records resolution on github issue.

https://github.com/http2/http2-spec/issues/386

mnot: let's talk about websockets. Suggest we close this issue since it could be done with extensibility.- a new ALPN token.

Brian: where does that leave n-segment?

mnot: web sockets was one use case but not only one...

mnot: we have an editorial issue - we need more explanation...

mnot [ closes issue]


### [Requiring Client Content-Coding Support](https://github.com/http2/http2-spec/issues/460)

mnot: implicit gzip content-encoding makes it difficult to be a semantically interoperable HTTP/1.X<=>HTTP/2 gateway...

mnot: implicit gzip may work well for the common browsing case, but is difficult for other cases like PUT

martin: elephant in room - intermediation. often there aren't intermediaries if you are using TLS

mnot: virus scanners are the big concern

mike bishop: wininet has issues being a HTTP/1.X<=>HTTP/2 intermediary from an application perspective. e.g. content-length

mnot: etags are the bigger concern

mnot: people who want implicit gzip are the same people who want TLS

roberto: http2=>http/1.x say use a accept-encoding: http2-encoding

martin.nilsson: does it get bad if we don't have implicit a-e?

jeff: yes, relying on clients supporting gzip is good

jeff also had an alternate proposal that I missed that would remove this as a blocker.

patrick is arguing in favor of status quo, talking about browsers wanting this for performance reasons. talking about intermediaries.

mnot points out that there's a tradeoff between performance and better interop

patrick points out that the existing deployment experience hasn't revealed this to be an issue.

julian: what problem does this solve?

lots of discussion about the existing problems with accept-encoding: gzip getting stripped by intermediaries on the web

jeff: we already have the reverse problem with clients advertising gzip support but not actually supporting it

discussions about what the httpbis spec says about how to enable/disable gzip

will: (1) compression is very important for big webperf (2) this is a great hammer to get this webperf improvement for a large majority of the web

lots of people object to using *this* hammer, and question the tradeoff between webperf and interop

lots of discussion about the nature of these client side intermediaries, whether they're big virus scanner vendors, or there are a lot of less savory intermediaries

lots of discussion about UA-detection type of work on the server-side to compress responses regardless of what the client says

jeff raises the possibility of using the power of big implementations to kill connections where gzip is not supported in order to prevent intermediaries from mucking with this

mnot is writing up the consensus decision to remove implicit gzip from the spec.

will doublechecks that we have consensus on the solution, are content-providers going to actually do this?

roberto: we need a new error code or new http semantics to force downgrade to http/1.1

will keeps arguing about making sure we don't resolve the issue too soon without having a reasonable option to preserve the performance improvement

end resolution was to remove implicit gzip and google folks are supposed to put up a proposal for coming up with a ratchet / hard fail solution to move first to lock in support for compression, so any intermediary that tries to break it afterward will cause a hard fail.

### [Compress segments rather than frames](https://github.com/http2/http2-spec/issues/466)

mnot/martin restated Roberto's comments that we don't want to compress by segments because it has higher state requirements

topic: issue 480 headers and flow control

Roberto is reassessing the problem, basically that headers are unbounded (not flow controlled), which is problematic for implementations.

mnot: is a solution to just add a new error code "you're sending too many headers"?

roberto: yes, this is a solution, but there are many other solutions <rattles off a whole bunch>

mnot: what's your pref?

roberto: have a limit on the total number of headers you're allowed to have outstanding at any point

will: are you saying you want flow control for headers?

roberto: no...it'd be nice to separate out a SYN frame

will: so you want to rollback to SPDY? :P

roberto: when you are flow controlling that updates compression state, it can lead to deadlock.

roberto mentioned some solution and got booed

roberto: you know how a non-malicious client triggers this in practice? imagine an rpc protocol.

rwheeldo: more examples...e.g. stock ticker updater

will: imagining the client bug reports and creation of de facto standards because of implementation specific thresholds for sending out such a header

jeff and roberto discuss the possibility for deadlock when you have flow controlled headers. jeff points out an example of a 32KB cookie when the flow control window is 16KB, except that you can't fragment headers like we can do with DATA frames.

roberto discusses his idea of creation of a new METADATA frame that is flow controlled and doesn't change connection state.

johnny/jeff/roberto discuss further. you have to crack open the METADATA and make sure the hpack opcodes don't update state, or else you do not apply the opcode and you send an error for that stream.

mike.bishop: isn't this just a DATA frame?

roberto: yes, except it's a different opcode

roberto: we have to fix this

will: why? we've lived with it for this long.

roberto: that's because no one has tried to abuse this yet.

mnot: i'm not sure we're convinced that it's important to fix

will: what other vendors feel like this is important

<silence>

roberto: i know f5 cares about this

stephen: we just terminate the connection

roberto: we have more non-web clients

mnot: would a new frame type that carries headers that are not compressed help?

roberto: that's even more than what i proposed, but yes, that would be fine

jeff: because you can segment that

mnot: and thus it won't update state

stephen: isn't the way this works that best practices emerge, and if you go out those bounds, then your performance just sucks?

mnot: but then roberto's claim is that some people will really want to do these things

stephen: the way this works is someone debugs this use case, identifies the performance issue is because you're sending 7000 headers, and you work around this.

will: but maybe we should just accommodate this use case rather than have them have to work around this, like we do domain sharding to work around http/1.x. we are fixing those workarounds in http2.

more discussions, then around having a solution that traverses proxies

rwheeldo: clients that send a high volume of headers...i think that decent compression will take care of most of the pain of that. stupidly large headers fall into 3 camps: (1) huge stupid cookies and that's out of scope of this WG, (2) stupid large custom headers, (3) user-agents

mike.bishop: also kerberos tickets

jeff: i see encoding viewport state in protobufs and send them across as headers

hasan: i'm fine with these people having broken shit

roberto: i'll point out hasan that if you say that in the context of the gfe at google, that will cause you problems, since we see this problem, especially with number and size of cookies

hasan: we've been able to crack down on these people abusing cookies

roberto: tell that to the next acquisition that wants to go behind a gfe

martin: we do allow arbitrary header blocks...do we still want to allow those based on this discussion?

mnot: pull request 482 "Advice on dealing with large header blocks"

roberto: i wouldn't mind a bigger change here to be honest. i wouldn't mind if hpack only worked on the initial headers frame.

jeff: one way to handle this is to say that streams are created with the colon headers only, although i know this won't work for all intermediaries like gfe which may rely on other attributes for routing, and then subsequently headers get sent later.

martin: i considered this but this is a little tricky because it's not clear what headers are necessary for routing.

mike.bishop: this would really mess with the reference set

jeff: we could have different hpack frames, one for initial headers, one for subsequent ones

brian: i have a question about this pull request.

<some confusion about the pull request and a MUST, may be out of date>

roberto: there is a way that we can make hpack streamable.

jeff: if we start going down this route...

will cuts him off: maybe we should revisit whether or not we want to go down this route

jeff: is flow control of headers a big enough issue that we're willing to absorb a non-trivial rewrite

roberto: well, it depends on what you mean by a large rewrite

will: it seems like we're talking about a theoretically valid use case that we have no data or implementation experience about.

jeff: i could see how this could become a potentially valid use case

will: http/3

mnot: sounds like there's not much interest in this

roberto: so, error code?

mnot: sure

jeff: we should keep track of the things we want to revisit for in http/3, and this is the only one that i see that could drive a big architectural change.

### [Only restrict HTTP application data and header block fragment lengths](https://github.com/http2/http2-spec/issues/456) (proposal)

mnot: jeff, can we short circuit this? can we close?

jeff: i'd like to discuss this edge case to see if we can get rid of this, especially if we have padding bit flags.

jeff would prefer to remove the padding flags and use a separate padding frame

jeff: the entire reason we use padding flags is so that padding is flow controlled

jeff: i don't see any clients sending this

will: that's because a user agent doesn't have knowledge to send it. it's primarily application specific, therefore server=>client. at least until the web platform exposes a way for web apps to control request padding.

### [Need way to negotiate "no Huffman" in settings](https://github.com/http2/http2-spec/issues/485)

mnot: this was filed by michael sweet

martin: there are issues with huffman: (1) complicated to implement (2) vague concerns around maybe having security concerns that are enabled by huffman tables

martin: i don't really buy this concerns. and if we screwed up, then we rev the protocol

jeff: if you want to play with the big boys, find yourself a huffman library. close with prejudice. i think there will be plenty of huffman libraries.

mike.bishop: we've had some discussions around whether or not we'd like to be able to turn huffman off. i think we have mild preference for being able to, but we won't fight hard. on a link where we're not bandwidth constrained, but rather CPU constrained, it'd be nice to disable huffman to save on CPU.

martin: at that point, huffman isn't your biggest concern.

###[allow intervening DATA frames](https://github.com/http2/http2-spec/issues/481)

<mnot reading the issue aloud>

mike.bishop: the problem here is you have to hold onto the uncompressed data while getting the interleaving frames

roberto: the reason we disallowed interleaving frames was in order to easily reason about error cases and buffering requirements.

martin: simplifies because you can treat a header block like a single frame

johnny: why is this a perf issue?

martin: HoL blocking

###[Changing the way that altsvc use is indicated](https://github.com/http2/http2-spec/issues/474)

mnot explains to willchan what/why: it's an analog to sni and other routing info

lots of discussion about the various motivations around this: loop detection, load feedback, etc

will pushes back in order to figure out if this is really necessary, playing devil's advocate

stephen starts explaining how loop detection happens

stephen: this doesn't happen a ton, maybe a 1% case that we load balance you to somewhere else, and then another that we load balance you back.

<lots of discussion, bad scribing because willchan was busy discussing, oh good, looks like someone else scribed>


Talking about Service header field

long discussion about looping, need for the header field

Gabriel:  Can we use a hop counter?

Martin:  Hops aren't tightly bound.

Martin N:  Confirming that servers aren't expected to have differing behavior based on which service.

Mark:  No, not a use case.

Johnny:  This is the host header for Alt-Svc

Mark taking action to dig up explanation of problem case and send to list.  Better description of use cases for Service header will help us decide how to fix.

Don't have support to change mechanism header field to frame, just discussing how to define header field.

resolution: mnot to write up better motivations, willchan leaning towards being convinced

Martin:  Does the Service header need to be a MUST?  Possible privacy concerns here.

Mark:  No objection to clients who might do this for privacy reasons, but theres a performance trade-off.  SHOULD, but with explanation why this is useful.

### [Flushing Alt-Svc Cache](https://github.com/http2/http2-spec/issues/444)

Mark:  Goes beyond suspicious entries, make this a recommendation for full cache flush.

Mike Bishop:  Make sure this stays as SHOULD; issue text sounds like moving to MUST

Mark:  SHOULD

### [Enabling redirects to other hosts](https://github.com/http2/http2-spec/issues/492)

Patrick:  Frame on stream zero can already do this

Mark:  Right, so why is the header different?  Make it the same.

Johnny:  If header supports everything the frame does, why do we need the frame?

Mark:  Kind of nice to have from layer perspective, but not strongly opposed to getting rid of the frame.

Patrick:  Lets you do things as soon as a connection starts without waiting for a request.

Mark:  Yes, that's the killer feature.

Johnny:  Is it a concern that this can be done over an unauthenticated connection to begin with?

Mark:  Frame doesn't require it either, just an implementation choice right now.

Will reraised Service header stuff. These are more bits to fingerprint. Should this header be controlled by author content? XHR/fetch()/extensions/ServiceWorker/etc.

mnot/stephen: maybe a bit is good enough for loop detection

###[Intermediaries and Alt-Svc](https://github.com/http2/http2-spec/issues/462)

Martin:  Proxies will anyway.

Mark:  True, but at least we've documented that they shouldn't.

Richard:  Is there even value in using this if youre proxied?

Mark:  Yes.  Upgrade to TLS.  Note that Alt-Svc shouldn't be used to configure proxies.

Will:  Proxy could append Alt-Svc to EVERY RESPONSE to get coalesced connections and better perf for users.

Mark:  Not willing to spend time on this -- if it raises discussion, will just rip the whole statement out instead.

### [Refine Prior Knowledge](https://github.com/http2/http2-spec/issues/418)

Emile:  Tied to discovery; browser could find prior knowledge via DNS.

Patrick:  Interested, but not willing to block on it.

Mark:  Interest from the DNS community on using DNS with HTTP/2; probably a BOF on HTTP/2.  In the interest of this community to engage and help level set in Toronto, but not wanting to block the working group on this.

Richard:  Does prior knowledge mean you can make a TLS connection without ALPN if you already know?

Mark:  No, not the intention.

Martin:  Spec doesn't actually read that way; will fix.

### [Race condition in shutdown for proxies](https://github.com/http2/http2-spec/issues/458)

Daniel:  If upstream connection closes while a request is in flight, the connection will fail.  Need a way to enable this to drain; DRAINING frame, double GOAWAY, etc.  No strong feelings which approach is best.

JPinner:  Weve already implemented this, BTW.

Roberto:  Adding to spec raises the odds that a client will do the right thing on a subsequent GOAWAY.

General agreement in room that double GOAWAY is acceptable.

Gabriel:  Is there mandatory language here?

Martin:  No, one SHOULD.  Just a requirement to handle the case.

### [Priority for closed streams](https://github.com/http2/http2-spec/issues/468)

Martin:  Implicit feature that reprioritizing high-in-tree node changes the priority of everything underneath it.  One way to do this is use the original request as a placeholder for everything on a given tab/set.  This is only possible if a PRIORITY frame can be sent on a closed stream.  Currently, only on open or when possibly racing with a RST_STREAM.  Text changes this to allow PRIORITY frames at any time once the stream has been opened.  Lots of changed lines from reflow, but the change is simple.

Not trying to add new feature, just clarifying what was intended and omitted from the commit.

Mike B.:  Means retaining state for all streams as long as there are dependent requests.

Martin:  Servers can always prune, but should try to keep things that are near the root if possible.

Roberto:  Should be a max of two RTTs anyway.

Martin:  Not wanting to offer too much advice here; implementers will discover what works and what doesn't.

### [Enable weight of 0](https://github.com/http2/http2-spec/issues/436)

Herve:  Weight of zero enables pausing; useful in several scenarios such as background downloads

Mike:  If the goal is just to pause, why not use flow control?

JPinner:  Don't need an RTT to restart; restarts as soon as other data has been sent.

Tony:  Why not just use 1 vs. 256, which is what is already specified there?


Herve:  Many low-priority streams add up to a considerable share of the bandwidth.

Gabriel:  Seems like were working around a case that flow control ought to handle better; is there a shortcoming there?

Herve:  Can be solved using flow control, yes, but lose the RTT.

Roberto:  Would be equivalent if WINDOW_UPDATEs could be negative; have to wait until it drains, which may be more than an RTT.

Mike, Martin, Jeff:  Not really pausing.  Really background.

Martin:  Equivalent to "dependent on everything"

Jeff:  Priorities were designed to be proxyable; proxies that pass a weight of zero will probably stall any client that requests it.

Richard:  If there are other ways to do this and you don't actually want it, there are better ways.

Jeff:  The right way to do this is make it dependent on the more important things.

Roberto:  This is requiring a special case; not feeling comfortable.

Mark:  Not hearing much support; talked about this a number of times, probably not going to make it.

### [Accounting for Proxies](https://github.com/http2/http2-spec/issues/413)

Mark:  Have we accounted for this in all our various updates?

Martin:  Yes, we've added the text.


### [State Diagram](https://github.com/http2/http2-spec/issues/484)

Richard:  Like a tube diagram, better to have something that can be followed than something that's geographically accurate.

Gabriel:  Weve encountered this before and chosen to take the diagram out.  Maybe we should do that if its causing issues.

Martin:  In RFCs, figures are always illustrative, never normative.

Mark:  Only Greg seems to be bothered?  Does anyone share his concern, modulo some corrections to the current diagram?

**silence**

Jeff:  Consider HEADERS+CONTINUATIONS a single frame for state-transition purposes.

Roberto:  Current diagram is comprehensible.

Tony: add note about substates?

Jeff:  Nothing to do with frames, just stream lifecycles.  The substates have to do with partially-received frames.  PING doesn't show up either, because it doesn't change the state of streams.


### [Privacy considerations for Alt-Svc](https://github.com/http2/http2-spec/pull/501) (proposal)

Mark:  Creating dynamic hostnames gives an unbounded amount of entropy for tracking.  Unless the client doesn't send the Service header.

Martin N.:  Until IPv6, with a unique IP address as well as unique hostnames.

Mark:  Need something about Alt-Svc -- adding this for now.

### [BLOCKED should be an extension](https://github.com/http2/http2-spec/issues/500)

Jeff:  BLOCKED would have been an extension had extensions been available, now they are, so it should be.

Hasan:  As long as there are still enough plans to implement, no objection.

Richard:  Helps shorten the HTTP/2 spec, enables better flexibility.

Hasan:  Not planning on revving in the future, but makes a good proof of concept for extensions.

Patrick:  Extensions will be less reliable, may want to keep if you care about it getting through intermediaries.

Roberto:  Lets take the path of least resistance -- which one is that?

Hasan, Patrick:  Cant change freely anyway once its defined and implemented broadly.

Mark:  If people are balanced, creating extra documents does have extra overhead.  

Mike:  Can put multiple extensions in one document; could scale.

Hasan:  Good for proving out the extension model.

Martin N.:  Also helps reduce the size of the spec.

BLOCKED is an extension.  Mike to share source of current I-D with Hasan who will submit BLOCKED as a new draft.

### [ALTSVC as an extension](https://github.com/http2/http2-spec/issues/499)


Roberto:  If BLOCKED is an extension, ALTSVC should be too.

Patrick:  Don't want to be in the situation where we cant use it because no one implements extension

Will et al.:  Its already optional, we have all the vendors here, and it will be basically the same.


Mark:  Either way, Alt-Svc stands or falls on its own, and people who don't implement need to be convinced by experience.

Jeff:  And it unblocks the core spec.

Hasan:  And it looks better to the people who are complaining about the protocol being too complex -- marketing is important.

Daniel:  Alt-Svc seems pretty core, not clear why you say its able to stand alone.

Jeff:  We have a widely deployed protocol with all these features that works okay without Alt-Svc -- it helps, but its not required.

Hasan:  Theres a dichotomy here:  a spec-compliant client can ignore Alt-Svc, but its core to the spec.  We need to resolve that, and it will influence the direction.

Mark:  When its already optional and only about how the content is split into different documents, its an editorial reason.  Lets leave this to the editor.


Jeff:  If its core to the protocol, why isn't Alt-Svc part of the core document already?


Julian:  Theres a normative reference, so we cant move forward until Alt-Svc is done.

Decision:  Leave to Martin.  Martin wants more feedback before making a decision.  Martin has text, but no pull request yet.



## Friday, June 6


Mnot: Have left: security issues, other issue during meeting, next steps

### [Make alt-svc an extension to the spec](https://github.com/http2/http2-spec/issues/499)

(continued from Thursday)

mnot's position is that whether it's an extension or not doesn't affect adoption. Other folks had stronger objections

Patrick: This extension is a real mistake on many levels I chased a SPDY bug where I got two replies for the same stream. This is an example of wishy-washy error handling. It would need to be defined in the most broad term.

Patrick's objection is to extensions in general

Mnot: The decision yesterday was to allow extensibility

Jeff: 

Roberto: I would feel more comfortable if we said what the frames we're going to send it so we can start rejecting them as soon as possible.

Hasan: That's a discussion about the extension, not alt-svc

Roberto: People are uncomfortable with people handling this as an extension when we're not sure

Patrick: I don't like extensions and don't like the idea of moving things out into extension when we have experience from other protocols of this hurting interop

Mnot: What do we think the role of extensibility is. What is the purpose down here?

Jeff: The purpose of extensibility is to provide hints which are not part of the core protocol. For example, blocked is a hint for performance

Patrick: Blocked may be a hint ...

Jeff: If you need in in the protocol to function properly then you can't ignore

mnot: Patrick is saying that extensibility is giving him increasing discomfort
Has anyone had a strengthening of feeling overnight?

What we've been talking about with these extensions aren't really extensions. What we're doing is moving the protocol's non-verifiable behavior into "extensions"

mnot: Our charter is to improve end-user experienced latency for the common case (web-browsing)

mnot: We're talking for a moment about extensibility and our approach to it overall

jeff: from environments with high-latency (mobile.twitter.com) we see large latency reductions without the new prioritization scheme ... compression gets you a lot because you can serve requests without large rtts

will: In the app case, the business logic is largely downloaded already

jeff: packet drops are where you get the large latency requests - crowded, long routed networks

mnot: The argument for prioritization is to move hueristics out of the browser

jeff: If you had to pick between prioritization and multiplexing and you chose prioritization you'd realise you needed multiplexing

mnot: we're getting off track... Regarding extensibility I'm hearing more discomfort from Patrick but no-one else.

roberto: Uncomfortable about putting certain parts of the spec into extensions: Alt-Svc, Priority

mnot: This remains an editorial decision for Martin to handle. If we disagree. Let's take all the extension ones and flip them to editorial ... OK. let's go through them quickly

jeff: I have a number of implementors saying we're going to take the DAG priorities and drop them on the floor. We're had months of interop and no browsers are sending them.

mnot: Shipping twelve has happend but I'm not seeing much interop - complex uses of hpack, etc.

Brian R: and push

### Deployment, Adoption and Roadmap

[ we diverted to a meta-discussion ]

mnot: We have a protocol and it's still being used experimentally. SPDY is still out there and gaining traction. I'm worried it's getting entrenched. People are unwilling to deploy this in production but are willing to deploy SPDY/3.1. We'll be deploying something we don't have significant performance experience. I'm happy with this only if we ship it real soon.

martin: there are a number of things we're doing here which are highly speculative. to get experience, we either need to deploy a draft widely (which is unlikely) or say "we're done"

roberto: I'm perfectly happy to kill old versions of SPDY, why don't we relabel this spdy/5 and ship it

will: this would still be a branding issue. it wouldn't be seen as http2. If we do release something for wide deployment having it called http/2 would be a good thing.

roberto: we've given people spec and said they're not going to change 

mnot: we could make the next draft is a longer-lived one for experience only

hasan: with bug fixes only

mnot: if we ship it as h2, then it's the final protocol

jeff: it's slightly different with spdy because it's already been in live with market pressure driving it more than a spec

will: one thing that can really hurt us  is if hpack doesn't work well on the server. if that's a performance issue, they'll pick spdy over http2

roberto: there's no reasonable implementation in which hpack will be slower than gzip

jeff: you're assuming reasonable implementations

roberto: i've run tests, written code...

jeff: where are they?

mnot: we need to figure out how to set this up so it encourages deployment

[ a bunch of discussion about people's different hpack implementations ]

jeff: we need fast, interoperable compression libs

roberto: I agree but that's not what's causing us to lack experience. It just takes time to get changing drafts out there. The changes made between SPDY release were smaller. My personal preference is ship the darn thing call it "h2-near-final" or something

mike.bishop: how long are chrome's reviews. 

will: our stable channel releases every size weeks. beta every four, dev every week. to go from code to release is twelve weeks or longer

hasan: there is a canary which is the equivalent of firefox's nightly

mike.bishop: how long is it going to take to get it out to a wide enough deployment.

mnot: every month that we don't ship and spdy gains support it becomes harder to argue that we have something better. i want browsers to eol spdy ... as long as we're comfortable knowing that there are some things that aren't complete then we should look at shipping quickly

patrick:I haven't seen anything that's going to give me more confidence

martin: extensions is the biggest change

jeff: there are still issues that we need to address

johnny: we want strong interop for the major pieces. we want to start rolling it our by the end of the quarter including how we use the new priority scheme on user's machines

jeff: we had good interop on the last release. most of the changes were around hpack. since then we've added padding, changed, priority, ... It's in production but it's a thing we don't know about. When we did spdy we turned it on and off for six months before it was stable. If we ship it, it'll be months of debugging and interop.

Roberto:  interop is going to happen whether we ship it as draft or whatever

jeff: It hasn't based on previous draft

stephen: stamp it and ship it. we will learn a lot over the next couple of years

jeff: let's pull out stuff we can do as extension and get to something we can ship

mnot: patrick has said he's willing to push the button and ship. chome will ship in canary. are other implementors willing to ship it as it is now?

jeff: as it is, many of the features won't be implemented. e.g. priority is a no-op

mnot: gfe?

hasan: yes, absolutely I can put it on some machine and see it perform. i can't put it everywhere unless i can prove it won't bring down google

mnot: are we comfortable putting this out as h2 when we might not outperform spdy

hasan / martin: no

mnot: we need an exit criteria 

martin: I'd like a generous last call

jeff: if we go with something that's more complex ... people won't go with it

roberto: we need four-six months to see adoption but we don't need four-six months from today because there haven't been big changes in -12; can do 4-6 months from previous implementation draft.

mnot: we're competing with spdy. third parties who are not participating in this are shipping spdy

jeff: safari is shipping with spdy and it won't be updateable so we'll need to retain it.

rob trace: microsoft will be able to pull out spdy

mnot: there are also server implementations, nginx, jetty, ...

???: the question is whether their customer will update to non-SPDY versions

will: we're committed to the standards process and will EOL spdy.

hasan: the power is still in the browsers. os upgrades for safari are good

patrick: my advice to customer is to wait for http/2 because we'll yank spdy but they're starting not to believe me

jeff: we won't be pulling support for spdy

hasan: that's different because some of your clients aren't negotiating spdy

jeff: so are some of yours

hasan: we'll be turning off npn as well

Roberto:  If we don't make big changes we should see some big deployments in a couple of months

mnot: I've heard statements from big implementers making commitments about turning off spdy which makes me a little bit more comfortable. jeff is unwilling to annoy customers but this commitment is important to get other folks moving. we can turn our attention to : how do we ship the best protocol in a reasonable about of time. that's the context for the rest of our discussion

brian: moving stuff out to extensions sounds good

### [Prioritisation as an extension](https://github.com/http2/http2-spec/issues/506)

mnot: no discussion w.r.t. blocked, some discomfort with alt-svc, unclear with priority

jeff: some people say they won't implement prioritization

johnny: my biggest concern is if we make prioritzation as an extension, would that mean we have not prioritization in http/2. .. I think we need one true priority mechanism

roberto: doing anything as an extension implies optionality

martin: we have something we've debated for 2 1/2 year. we debated because we knew the simple scheme wasn't sufficient. we've had other proposals which weren't acceptable.

jeff: I want to see a spec out and minted within a reasonable amount of time.

???: are you saying to move to an extension and leave it?

jeff: no, if we have much better experience we can pull it back in.

Daniel Sommermann: how do we mux it through a proxy?

roberto: anything we have isn't proxyable. that isn't the world we're heading into, especially with plain text impls as well.

martin: i'm uncomfortable with putting things to the side and optionality

jeff: you cannot verify that proxies are maintaining prioritization

roberto: the difference between priority and data is that things will proceed without it but they may be slower. This scheme allows priorities to survive proxies. a lot of the things this achieves aren't visible to the client, they're just better for overall health of the system.

jeff: I'm looking to hear servers actually committing to implement it (not just google)

Stephen: akamai will do. i'm not convinced by roberto's argument but it makes me curious enough to implement it to get experience. It's in fall before it'll get anywhere

mnot: who prefers making this an extension?

jeff: I want interop

roberto: removing priorities as an extension? why? it needs to be implemented

mnot: I'm hearing from jeff that he want's to fall back to a simpler scheme

jeff: yes

??? : if you make it an extension, someone can come back with another proposal

martin: If these are the discussions they lead to, I'm against extensions now. let's mark it as at risk and acknowledge that it's less tested

mnot: then it will fail last call potentially

jeff: my concern with this is gc because you're holding onto state after things are gone. If this fails, we can drop back to the spdy implementation which isn't proxiable but has been subject to real experience. chrome has said they'll turn it on

jeff: a fallback plan scheme is that dependency must be zero. weight is priority which makes it a flat scheme

hasan: this is what gfe does now

jeff: am I the only idiot intending on making a tree with this?

hasan: if it's in the graph, gfe and chrome will make use of it

jeff: we can mark the implementation of trees as at risk

Mike: for that matter you can get away without changing the spec and making this a best practice

jeff: but you can rip out the tree stuff from the spec

mnot: are people happy with this resolution: mark it at risk

ten minute break


### [Forbit/Permit Coalescing](https://github.com/http2/http2-spec/issues/490)

mnot: ekr, the interpretation of 6066 and whether this forbids coalescing? this potentially gives us performance gains but other problems

ekr: I agree, rfc 6066 discourages this. the notion makes people queasy, sni or not

mnot: imagine we're in a situation where the cert is valid for all host being used. is there a security reason for the constraint?

ekr: this is 11 year old text. having mutually suspicious people over the same tls connection has caused problems.

mnot: this is assuming that the boundary is at a per-origin level which is not always true. the web origin model is there but in other parts the decision is made per-resource, on cookies, CORS, ...

ekr: i think of CORS as extending the origin model rather than ignoring it

mnot: it sounds if we keep it we'd need a big section in the security considerations

mike: if you make a request for a different host than in the sni you will get a 400 in iis - it's a should in the rfc, but IIS enforces it.

Mike: if we do permit coalescing, we need a way for the server to reject it.

mnot: we have alt-svc the arguments in favour: it's good for performance, it makes transitioning from sharding easier. we need security consideration and we need a mechanism for the server to say no

rsw: i'm concerned about information leaking due to identity reuse on tcp / tls connections

mnot: are we happy to leave this in?

mnot: we leave coalescing in, we have a new security section especially for different authorities on the same connection and a way for servers to say no. if we write this in the next can you get back to us by toronto, ekr?

ekr: yes, I believe so. If tls had a way to bootstrap new contexts, would this be helpful?

Mike: we're not really in favour of coalescing on http. we think tls giving us different contexts would help

mnot: I'm relucant to make the security decision in the spec because there are cases where it's safe

Gabriel:  the default should be don't

jeff: what if the cname is the same?

martin: text currently says host and port

mike bishop: should be host, port and sni name

mnot: there's a number of ways to determine this. is it ok to leave this to implementations?

mike bishop: is it worth having a way for the server to say upfront that coalescing shouldn't be used? server settings or whatever.

will: in practice it's not going to make much difference; browsers will cache after being rejected once

mnot: is it worth speccing that the connection is origin-specific as setting?

will / patrick: yes

jeffs: how's a host supposed to send this when it hasn't seen the host?

Mike:  based on the sni

?? it's just saying it doesn't support coalescing at all

mnot: do we want this or not?

jeff: no

patrick: now i'm in favour of an extension

jeff: PLEASE write that down!

jeff: I have a question regarding extensions, should we have a 32-bit space for settings?

mnot: focus!

martin: alt-svc has a status code which says "you made this request to the wrong server"

mnot: don't use this connection to talk to this server

mike: we could use that status 

mnot: are we ok with this resolution? needs some colaboration with tls wg

yes

### [HTTP URIs over TLS](https://github.com/http2/http2-spec/issues/315)

mnot: next issue, http uris over tls. we talked about it a while ago and punted. now we have some implementation experience. we need to specify how http2 adresses pervasive monitoring. if we show http over tls this would demonstrate something. we should adopt a document or spin up another to specify how to do this separate from and non-blocking for http2. I'm sure people will want it to be implemented for everything but we won't get consensus.

??? could this work for http/1? if so how?

mnot: you'd send back an alt-svc, the client wouldn't check the cert but use the connection

mnot: we have a private draft. do we want to adopt it? another option is "no, we want to do something else to address pervaisve monitoring" or "no, we don't want to address it" and deal with the consequences.

???if our story on pervasive monitoring is to get https everywher, how do we get from 30% to 100%?

mnot: our remit is that we have to have considered it and have a position

Mike: we encourage tls adoption by improving performance / behavior

Dan Appelquist: it's better to sit in the group than be implemented elsewhere

[reference STRINT workshop report: https://www.w3.org/2014/strint/draft-iab-strint-report.html]
[The STRINT report was largely supportive of "opportunistic encryption" as a mitigation
strategy for pervasive monitoring.]

mnot: it's in scope for the wg. any good reason to not adopt this doc?

jeff: an argument is that the wg puts a bigger stamp of oe being the way to deal with pm

martin n : if we do oe, proxies will start doing opportunistic decryption / interception

mnot: we have to have eenough evidence that we've discussed this and considered it.

jeff: I'm happy to take an item to sort this out after http/2 ships

mnot: what's mozilla's position if this doesn't get adopted?

patrick: doesn't really change much; still plan to experiment

dan applegate: so it's better to have the implementations tracked via this group

mnot: there's some concern i'm hearing about schedule. I'm mostly concerned that when I get to iesg review that we've done enough

Barry: the job of a shepherd write up is to give a summary of the conversation. i can't commit to what an ad may or may not say. the requirement is to have it considered and no-one can say it wasn't. .. opportunistic security is the current term. if you have a good idea of where you want to go, it can be a proposed standard rather than experimental

jeff: we have no idea how easy this will be to downgrade or how effective it will be

Richard: one thing that was discussed was sending http over tls and another was that you could ignore the cert check

lots of folks: that's what we're talking about

jeff: nothing stops clients ignore cert checks

S. Ludin: akamai will continue working with mozilla

mnot: what do people think about wg experimental?

Barry: are there objections? I hope if you take it forward it will solve a problem...

mnot: doc will be adopted. people should have a look, raise issues, ...

martin: the feedback from the security area group was "hmm"

### [TLS Renegotiation](https://github.com/http2/http2-spec/issues/363)

martin: tls had an interim meeting 2/3 weeks ago. there was pretty strong feeling that renegotiation would not be part of tls 1.3 http appears to be the only protocol to use client auth mid-session. there is talk about how to do re-keying. there's good reasons not to do renegotiation : there are assumptions made which are invalidated but may not be updated in the application. it's led to a long series of vulnerabilities, applications making bad choices. they are interested in pursuing things on a longer timescale. complicating a security protocol is something we need to be cautious off. despite the layering concerns (http needs to make assertions about tls) they're inclined for us to solve it.

client auth is a less-used part of the protocol and people may be willing to make compromises on, for example, performance. what we're looking for is a transitional story that will get to something good without tls improvements. I've written a draft which mozilla may implement. this is a new auth challenge. you send a 401 response with a challenge that says you need a client cert and the client is expected to go away and re-auth on a new connection.tls 1.3 includes features in which large parts of the handshake are encrypted so we should be ok when we hand over the cert.

mnot: if i have a server i need to cope with the idea that most browsers won't support it?

martin: if you're running http/1.1 over tls you can use the mechanism you use today .. tls is hop-by-hop

mnot: in our doc we say "don't renegotiate"

martin: you should do this before sending the preface. the question is if we have a good story for people who do want to do client cert and renegotiation.... i've updated the draft i wrote that includes hints in the handshake so the client can select the right certificate

mnot: what's the transitional story?

Mike: this is a good use-case for how can we push something to 1.1 ?

mnot: has anyone opened an issue for force-downgrade? ... #496 ... not authoritive just means not this connection

Mike: 505 is almost right, not quite; "refuses to serve this request over the major version that is used"

martin: what else is needed?

Mike: the server should "generate a representation" of what's acceptable; not UA-interpretable

martin: how about header with an enumeration of acceptable versions? alpn tokens?

mnot: mike, martin and I to go away and come back with a proposal. would people be ok with considering this?

jeff: Can it be 4XX? I can't send a 5. I don't think this is unique to my site. we break the spec and return 405 for methods we don't understand because 5s affect the failure statistics

mnot: in principle this sounds good (updates issue) ... back to issue 363. knowing we'll eventually have something better do we have a resolution?

martin: I don't think there's any good solution in this space.

gabriel: Is negotiation a must not or should not?

mnot: must not?

martin: if it's not must not, some servers will do it, clients will need to support it, ...

mnot: in which case, don't we need to protocol error?

martin: once you have a deployment of http/2 with renegotiation you'll have inertia against updating the tls stack. we want them on 1.3. We don't want folks to have incentives to stay on older tls

ekr: we want people doing the best thing and all doing the same thing

mnot: resolution. marking editor ready. 496 isn't and this is blocking

### [restrict cipher suite selection](https://github.com/http2/http2-spec/issues/491)

martin: we got some wishy-washy advice on rc4. the trend is that tls 1.3 will remove all modes other than the aead ones. those are in good shape which cannot be said for the rest. rc4 is on its way out and we have the opportunity to update the advice to aead only

Mike: what's the right forum for this? to discuss in the spec or point to something from the tls wg? this is a good idea but not http specific

martin: the problem is reference to something that is blocking

ekr: I think is a good idea. http wg should make a statement about this. if i was in uta i wouldn't say things which create a compatibility problem. i don't think there's anything you're going to come up with won't match consensus.

mnot: should we take 494, the pull request?

Stephen: I hugely want this change to happen but it feels wrong that we're doing it because it's the wrong layer but I won't fight it.

Mike: the other thing that makes me hesitant is lifetimes. tls cipher aging has happened 

???: does this take new ciphers coming down the pipe? cha-cha, etc.

ekr: tls wg has no plan to publish best practices - that's uta

mnot: I'm not hearing concerns on procedural stuff. I don't think uta's presence stops us from doing this.

martin: we need this text or something like it. It seems logical that if people are using new software they should use new cipher suites

mnot: do we want the text as a white or black list?

martin: it'll have the same effect.

mnot: will all ciphers be aead till the end of time?

martin: the text should say if an acceptable cipher cannot be selected, then http2 should not be done

ekr: the text is more or less fine

mnot: that was the last security issue.

lunch!


### [Service header field to SHOULD](https://github.com/http2/http2-spec/issues/502)

Stephen Ludin: just a binary flag that this came from a redirect would be fine, no need for entire Service header. this is good from privacy point of view

mnot: if 1.1 send as a header otherwise...

will: no, just be consistent

mnot: Service = 1 indicating an alt svc is being accessed; allow for extensibility in the field. and change name to Alt-Svc-Used. Since it is 1 bit, change to MUST as it is not as much a privacy concern.

Richard: we punted onproxy considerations yesterday, why add something for browsers to add while not specifying what intermediaries do with it

mnot: why

Richard: no guarantee, not reliable

mnot: sure, it is a header which can be stripped. sure we have to separate generation of it from consumption of it.

stephen: hope is browsers will have an incentive for perf gains

mnot: editor ready

### [simplify padding](https://github.com/http2/http2-spec/issues/505)

Jeff summarizing the issue. remove padding from header-frames and reduce padding length to 1 byte. Padding at purely framing layer does not play well with proxies at which point it may cause blocking and multiplexing/pri trouble. and HPACK has security mechanism itself already. the draft recently added.CONTINUATION.   and remove PAD_HIGH only using PAD_LOW thus removing a conditional case even if it is framing change. still allow padding on data but flow controlled, tied to a stream so easier to proxy

mnot: still not defining a padding frame type, so easier to trip firewall rules

jeff: plenty of other dos so nothing new here

roberto: so only 1 pad bit? any larger padding use a pad frame

martin: or split the data frames

jeff: could have padding -only data frames

roberto: could be more complicated

jeff: already need to know the limit for frames large enough. and this removes some conditional error checking.and no padding onheaders push promise and continuation

roberto: not sure how I feel about that

hasan; agree that padding on headers while hpack has some mechanism seemed weird to me. what is min pad on hpack?


jeff: 2 bytes now, used to be 1 byte

roberto: actually no ability to pad on hpack unless we change the spec a little bit

jeff: well you can insesrt dummy pad headers. but having lots of padding raises the aforementioned issues with no flow control and multiplexing

roberto with a padding frame a bit could indicate flow controlled or not, etc


mnot: sounds like removing pad_high has some support. the other part of the proposal requires more security review

jeff: the rest can be done inhpack, or use 0x80 which currently is not used to pad

roberto: conflation of layers, do not like it, but I am happy with padding frame with a bit for flow control

jeff: agree that no need in continuation frames?

roberto: agree, also more cpu now due to more state changes.

mnot summarizing: remove pad_high, yes. as for continuation frames, seems ok. pad_low might continue in push_promise and headers.

hasan: prefer pad frame. so add this to the conclusion

martin: not liking this issue any more

some discussion about padding usage nowadays...

Stephen: not even on our radar

martin: remove pad_high, no padding frame, 

roberto: need to ask for security review as there may be timing attacks

hasan: sharing info from security guys. have seen between 0 and 255 bytes of padding per response both http 1.1 and 2

jeff: implies pad_low is enough

hasan: yes, so agree on removing pad_high. padding remains in data, headers and push promise

Saurabh: would prefer to leave it in continuation to reduce code churn

jeff: padding for headers is not proxyable

mnot: once you are muxing all bets are off

mike: intermediary must make its own decision

mnot: so they may pass through for header-bearing frames but should maintain padding in data frames. 

hasan: google sec guys are happy with the decision including no padding in continuation

### [mandatory to implement cypher suite](https://github.com/http2/http2-spec/issues/498)

martin: tls 1.3 will have an MTI cypher suite in Toronto or so

mnot: could we punt on this until the TLS guys know more?

martin: Andrei tells me that schannel might have trouble with a couple of items here

mnot: wait till toronto

### [Remove frame-based compression](https://github.com/http2/http2-spec/issues/497)

Jeff: not compatible as this puts a sync flush context 

Mike: this was an approx. to transfer encoding but at the framing layer

Jeff: it tries to be so, but fails. but it could be an extension frame that is flow controlled

groan

Christian: issue is that there is no way to partially compress a response

mnot: nobody is going to implement this, so why do it? and now with extensibility one could negotiate an extension to satisfy your use case. actually, your point is an http general issue, not specific to http/2

mnot: no implementor interest, sec issues with proxying, potentially addressed via extension, and long term with semantic changes in HTTP. for now remove this.

### [Never indexed representation constraints](https://github.com/http2/http2-spec/issues/508)

roberto: not "sensitive" vs "not sensitive" but about the provenance. but this is not useful, too hard.

mnot: strong pushback, closed

### Next Steps and Wrapup

Mnot: how long to another rev?

martin: 1 week

mnot: hpack guys also please look over your doc to polish

mnot: and mark this as implementation draft, maybe more...

break...

mnot: mark an impl draft as something really serious. e.g., -13 marked as "h2-rc" and go to WG LC, mint it after some interop during 6 months and be done. LC could be parallel to this.

hasan: like it.

Richard: implications are?

mnot: wire protocol would not change

patrick: then why not use the "h2" token?

mnot: we only get one change of using that token, so make sure we have some interop before claiming it. 

mnot: how long will it take to take -13/lc into wide deployment?

johnny for chrome: to show up in dev? about end of Q3, but not really stable dev
patrick: early October for stable

rob for MS: end of summer Q3. IIS: the challenge is getting real services, not just test servers

daniel on Curl: shipping already

pinner on twitter: will not have on client until RFC, server: end of july

hasan: on GFE real world data by end of Q2

Stephen Ludin on Akamai: end of Q3

Hasan: mod_spdy for apache is off to apache, but are happy to help apache foundation, but they have to own it. our guy who wrote mod_spdy is only 1/4 on it max

mnot: encourage wg members to allow and help with code and info

mnot: in 1 week I can make a decision about meeting or not in Toronto

mnot: see estimate of mid to late Q3 for both client and server. so real data only till late oct or early November. so declare WG LC now on -13, sep 1 WG LC ends, start IETF LC OCT1 telechat on Dec 4, resolve discusses in Jan, so RFC by feb or so.

lots of discussion of how data will be collected, how soon, how shareable, what parts of the spec 

### Operational Advice

mnot: See draft-nottingham-http2-ops; we need to capture this, RFC is only one possibility

will: wrote the spdy best practices wiki, seems like the good type of document, 

martin: github pages are a good place

mnot: need contribution terms to be able to submit to ietf if need be eventually. will seed the wiki.

will: just copy and paste from my doc

mnot: perhaps not meeting in Toronto, perhaps not meeting in Honolulu... but there are proxy and other discussions which might cause meetings to happen, including http/3
