# HTTP Working Group Minutes - IETF 116


## Tuesday, 28 March 2023

### Active Drafts

#### [Message Signatures](https://datatracker.ietf.org/doc/draft-ietf-httpbis-message-signatures/) - Justin Richer - _(no slides)_

Justin: Report from researcher, updating examples with a PR, will drop a note to the list when the PR is ready. Couple of places where we need to be more specific about which octets to use. Needs normative changes, but more clarification of intent. Don't think a new WGLC is needed, but chairs will determine that.

Mark: From my standpoint, what I want to see is the PRs and have people look at them, new draft that sits for a few days to see if people are happy, but we won't have a formal WGLC or IETF LC, unless we or the AD change the requirement.

Julian Reschke: Mostly agree with that. Bit concerned with statement that it is not a normative change. (This was about https://github.com/httpwg/http-extensions/issues/2417)
Justin: Not what I said, it is a normative change.

Tommy: It's a normative change, but not an implementation breaking change 
Justin: Somebody will probably have to change the implemenetation. I will.

#### [Cookies](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis) - Steven Bingler - [slides](cookies.pdf)

Same-site cookies and redirects [#2104](https://github.com/httpwg/http-extensions/issues/2104)

Steven: Turned on and broke a bunch of sites, working to turn it on again safely
Added some metrics, weren't so useful. If anyone's aware of specific cases of breakage, I'm very interested.


Internal whitespace in cookie names and values [#2262](https://github.com/httpwg/http-extensions/issues/2262)

Steven: Ready for last call once issues are closed

What's next? CHIPS, Cookie Spec Layering - Want to untangle the mess from other specs.


#### [DNS Aliases Proxy-Status](https://datatracker.ietf.org/doc/draft-ietf-httpbis-alias-proxy-status) - Tommy Pauly - [slides](alias-proxy-status.pdf)

Tommy: Small draft for adding a proxy status parameter. Proxy status = header we already have i.e. how things are going. Would like to know the full CNAME chain, especially where servers may be doing CNAME cloaking to obfuscate that they're redirecting you to a known tracker or a server for which you would like to apply a specific policy.

Open issues:
- Add reference to structured fields [#2476](https://github.com/httpwg/http-extensions/issues/2476)
- Refer to AI_CONNONNAME [#2358](https://github.com/httpwg/http-extensions/issues/2358)

Tommy: Wrote PRs for these issues right before, so please go look at those PRs. Will revise the document to include those changes. Would love to hear from Ben (if online) about proposed change.

Ben Schwartz: That seems like a fine resolution to me. I think this draft is in good shape. I'm sending a new issue right now because I think the escaping rules are not totally right, but should be fine.
Tommy: Thanks, that's the kind of review we want.

Alessandro Ghedini: We've implemented it, and after the current issues are fixed, it's probably ready to go to next phase.

Tommy: Thank you. Want individual implemeters of this, so we've tested it.

Lucas Pardue: Had a quick review before the session, you mentioned that you can skip putting in the full chain if you can't get it. Is that generally applicable? Are there other reasons you might not put in the full chain?
Tommy: Good point, we could go as far as saying you SHOULD include the full chain if you can get it, the reason you wouldn't fulfill that SHOULD is if you cannot get it for some reason. Can't see why you would omit things from this, that's just hostile to the client and at that point you wouldn't include that option at all. 
Lucas: If you were to start dropping things, could you still achieve the same goals as what you're trying to do?
Tommy: Any hint you can give to the client is helpful. 

Chris Wood: How do you deal with CNAME cloaking right now if you are not going through a proxy? 
Tommy: Libraries are able to do DNS on the client and look at the full CNAME chain.
Chris: Clients will do DNS and inspect it and do the evaluation based on that?
Tommy: Right, so in the process of loading a page, when we do DNS we will get the whole chain and if any of those names match a list we can send it through a relay or apply cookie policy, etc.
Chris: If DNS resolution is subverted and there are items in that chain that don't match the list or that make it otherwise inaccurate, that's still an issue?
Tommy: Right, there are definitely cases where attempts can be made to get around it. Goal when going through the proxy is to see the full chain and the IP address so that you can see the full set of information. 
Chris: Took a quick look at the security considerations. Might need to say what could 
Tommy: Correct, it's also the DNS that the proxy is doing, would make sense to document that. Could you file an issue?
Chris: Sure

Mark Nottingham: Have you considered using an inner-list instead of a comma separated string?
Tommy: I think so.
Mark: That would mean doing less parsing
Tommy: I think we looked and couldn't do it, but let's double check

Mark: Sounds like we should be able to do WGLC before the next meeting.

#### [Unprompted Authentication](https://datatracker.ietf.org/doc/draft-ietf-httpbis-unprompted-auth) - David Schinazi - [slides](unprompted-auth.pdf)

David: Happy to do this talk in room 401. 
_General eye roll, mild amusement, and slow claps_

David: Adopted in the WG last month. Core idea: use TLS key exporter as a nonce. Gives property that don't need to ask server for the nonce.

Since last IETF: Shape of the header. Ben Schwartz pointed out why we can't use new schemes. Now we use new header and 2 new schemes.

[Issue #2240](https://github.com/httpwg/http-extensions/issues/2240)
Put new ID in first draft, but not well received, so reuse TLS registry for signature schemes and hash algorithms. 
Maybe should define a new IANA registry, since it's cheap. Seeing one thumbs up.

Jonathan Hoyland: I think we should bite the bullet and create a new registry
Sean Turner: We've got like three hash function registries already. Can't you take one over, add a column, and call it quits. See RFC 8122, there are other ones as well, will send you a link.
David: Under HTTP or TLS? 
Sean: Standalone. I'll send you a link.

Ben Schwartz: If this is being reopened, I want to support using string values instead of trying to create numeric values
David: Okay, thanks.

Martin Thomson: What did we do in Justin's signature draft? There are 2 things: the hash map version of this. 

Maybe you want a generic MAC algorithm in the registry, which gets in the way of what Sean said, although I liked that idea. What if there's another algorithm that you want to use. If JSON's got a signature registry that is very good and well-specified, then why make a new one.
David: On signatures, we were fine, but for hash, we weren't.

Martin: Can you put "none" in there as well? What happens if you have an "s" and "h" in here? 
David: If you put them together in the same registry, you can get rid of Signature and HMAC and just have one new thing, which is cleaner.

Justin Richer: The registry that just got brought up for HTTP message signatures, is well specified, but is very specific. Does have both signatures and key-based MAC type stuff in it. One of the benefits of this, based on input from CFRG, is that the algorithms need to be fully specified with all parameters specified. All the math needs to line up for this to show up in the registry. We also didn't use the JWA registry. Lots of reasons why we didn't. Main one is that the algorithms were designed for a specific other context and that may not apply here.
If you want to use the JWA algorithm, here's how to map them to what we need on the HTTP side. Functional mapping of these inputs and outputs and how you plug them together. Registry exists but deliberate choice. Haven't read this draft, so 
David: Thank you, would be happy to chat.
Justin: One last point, if you do go down the road of defining something, there is an IANA registry for hash algorithms, which is buried and which I discovered independently for a different draft. It says SHA-256 means this very specific thing in this section of this RFC.

Alex Chernyakhovsky: I understand why assymetric key signatures. I'm confused why there's a HMAC. Wondering if there is a specific use-case or can we kill the feature and simplify our problem?
David: Feedback from Ben S. asking why we don't add HMAC, someone might need it.
Alex: I think that's a terrible idea. I think we should not be exposing HMAC for this. 
David: Not unreasonable, if you have a shared key you could pass it in regular basic auth.
Alex: Don't see benefit of shared secret.
Ben Schwartz: I don't have any objection to that, the point I was trying to make was moot because we have a system where Unprompted-Auth can take arbitrary auth schemes. 
Alex: Would it be okay as a compromise for now to say that we don't do it now and someone can specify it in the future? 
David: Totally fine with that. Does anyone think that's a bad idea?
At this point, should use the TLS 1 that's not orphaned.
Martin: Signature algorithms that were deprecated, signature schemes that you want
Alessandro: Solution is use signature that, so if someone uses HMAC, they define a new registry.
David: Or they write a new draft to pull this all in

David: Everyone okay with dropping the hash, and using the TLS signature scheme? I'm getting thumbs up.

[Issue #2432](https://github.com/httpwg/http-extensions/issues/2432)
David: Just focus on using an authentication scheme. Seeing some thumbs up.
Mark Nottingham: Use of tools is a framework. Up to scheme designer, to define how you're using them. Are there user-agents out there when they see a 401 with a scheme that they don't recognize, do they do something bad. 
David: In this case, we would never send a 401 here, since if you don't have it then we send a 404 because we "totally don't know what you're talking about"
Mark: Then it's probably fine. Don't see concern from HTTP standpoint?

Tommy: This is more of a question to the room. We have Authorization and we have Proxy-Authorization. Imagine sometimes you might want to do it to a proxy. 
David: That's an argument to use the for reusing both of those others.
Tommy: In that case, should we call out that you can use it in both of those. 
David: I think it's mainly that the proxy one is hop-by-hop?
Tommy: Can we avoid wading into that by saying here are the existing ones.

Ben: If we go to use the authorization header, want clear text that by prior arrangement that clients are allowed to use any scheme in unprompted fashion. Don't want to say we're defining 2 new special schemes without using prior arrangements.
David: I see what you're getting at, but no, there are some auth schemes that you wouldn't want to be able to use unprompted that have multiple back-and-forth legs. Happy to take an action item to take a 
Ben: If we have a separate header, it's clearly okay for this document to say that it is permitted to use this header with any auth scheme that is technically feasible. 
David: I'll double check that there's no text we're banning unprompted for basic and digest, and if they are banned, that puts 
If it's already okay to send digest unprompted with Authorization, then I think that is fine, but I don't think this document should add it for those things. 
Ben: If we're not doing a new header, then I think we've got a whole different document.

Martin Thomson: I think the direction to move to Authorization and Proxy-Authorization is a good one and you should do that. You should very much name the draft the way that Ben suggests, that's what it is: it's channel-bound signature authentication, maybe keep unprompted in the title. To say anything about how 401 works would be an update to 9110, but that's unnecessary because that document says what it needs to say. The idea that you can take a 401 from some other context and put it somewhere else, that's fine but people can do that without help from us and you've already got a broad scope in this document.
David: Makes sense. Thanks.

Jonathan: Mentioned that this is channel-bound. Not sure how proxy authentication would be checked if you are doing channel-bound auth because proxy doesn't have the correct key. The server doesn't have the right key
David: There is a section in the doc about that.

Mike Bishop: +1 Martin, this does not need to update 9110, the text that you need is already there, quote that and observe that authentication can be sent without a 401 and that that is this case.

[Issue #2428](https://github.com/httpwg/http-extensions/issues/2428), [Issue #2429](https://github.com/httpwg/http-extensions/issues/2429)

David: Draft is empty for this right now. Don't love adding a full URL to the context. Wouldn't get header compressed anymore.
Proposal is to add signature/hash algorithm, key identifier, and origin, but not URL.

Alex Chernyakhovsky: One of the problems that we had with exporters is that it deals with the connection and not the stream. I'm not sure we want everyone to all get the same keying material. Why not include stream ID? 
David: That's exactly what this is about. Stream ID at the HTTP layer is gross. I don't see value in that separation, doing it by origin gives you a nice security model. Doing path or stream ID is effectively the same.
Alex: Nervous about that, feels weird that you could have system proxy i.e. Envoy that multiplexes a bunch of different clients that would have been different connections under H1, now they would all get the same identifier for the same origin. I really don't like that.
David: Sure, so you don't like it, but what's the impact?
Alex: Problem that would have different identifiers under different
MT: Wanted to respond to Alex. Nice idea, but impossible because we construct requests without knowing what the stream ID is.

Chris Wood: What are the ideal security properties for this thing, has analysis been done to demostrate that what is in the draft satisfies those properties.
David: Main use case is for MASQUE. In terms of the security analysis, can you help me with the analysis?
Chris: I was going to ask Jonathan to help
Jonathan: This is the plan

Kazuho Oku: Now that we are moving to using the Authorization header, would it make sense to use Realm (already defined for Basic) instead of the URL? If we don't, then the scope of the header becomes different than the Authorization header.

[Issue #2439](https://github.com/httpwg/http-extensions/issues/2439)

David: Currently use the nonce. Repsonse that reusing the nonce is terrible idea, but inclined to keep it, so if you have an issue with that please respond on the thread.


## Friday, 31 March 2023

### Active Drafts

#### [Resumable Uploads](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload) - [slides](resumable-uploads.pdf)

Marius Kleidl: if client receives 5xx and doesn't indicate upload complete, may be intermediate proxy - should be retried. 

Martin Thomson: having indicator from proxy would be unusual. In case where you get error from proxy and it indicated that you completed upload, I would ignore it. I would be looking for 2xx before paying attention to it. Regarding label on request, as used by server, is statement about conclusion of process. Whereas client saying it has concluded before it has even started the process is odd. 

Kazuho Oku: generally good idea to provide response. Probably more sense to put in the body. Probably add section that response has to come from server..


#### [Structured Field Values Bis](https://datatracker.ietf.org/doc/draft-ietf-httpbis-sfbis) - Mark Nottingham

Martin Dürst: There are few HTTP header fields where there is a need to have non-ascii characters. HTTP header from start were defined as latin 1. Dissappointed that when discussed on the list, editor said they have problems with their email and non-ascii characters - they should update their software. Other editor said we shouldn't use non-ascii when not necessary. 

Mark Nottingham: I don't think I said I'd prefer it be a mess. I have reservations about making it too easy. People reach for unicode by default - which in many contexts is a good thing, but in HTTP header processing it is more complex/nuanced than most people realize. Not against enabling if we need to enable it. Current solution is to use binary or string with percent encoding. Another solution would be to add a new type to structured fields to handle unicode characters. There are arguments for and against that. Concern here is that when we opened up this work that we scoped it pretty tightly. Adding it not terribly difficult. Do we do it now while spec is open and reduce number of times we need to iterate or wait for next iteration to give us enough time to iterate properly?


Martin Thomson: we should do this. Let's talk about the issue right now. Shove unicode into header? Let's have a discussion about each of these options, time permitting.

Mark Nottingham: I agree with you - the right thing to do here to is to define a new type. Problem here is that this is a contentious topic

Martin Thomson: I think we have this discussion. Launch wglc and see if we can address. We can always edit it in


Martin Dürst: I'm fine with either to do it in a quick thing after this or to do it with this if can be done quickly. Personally prefer UTF-8, not just unicode. If people say we want something different, let's do that if we can reach consensus.


Julian Reschke: Want to reiterate that we found that the extensibility model of structured fields is not at clear as we thought it was. Modifying structured fields and their implementations was harder than expected. I'm confused that Martin (T.) is saying that UTF-8 is not the only sensible option. Propose people come to working group with proposal.

Tommy Pauly: What I'm hearing is: lets do the last call and in parallel kick off proper technical discussion.


#### [Retrofit Structured Fields](https://datatracker.ietf.org/doc/draft-ietf-httpbis-retrofit) - Mark Nottingham

Mike Bishop: My inclination would be that if it's going to be fairly complex to do it and know that we're right, we're too late in the process to do that. May be worth doing as a separate draft. Don't want to hold this one up.

Tommy Pauly: I appreciate that new auth schemes and the existing ones can have different interior formatting. Fixing is tricky. As we're defining new auth schemes, can we give advice? Give something for new specs to reference. 

Mark Nottingham: we could define the fields and define the mappings for a digest and bearer. Give guidance for new schemes. Trying to be completist about it is a lot of work and risk. Brings up background concern that I think we can address. By defining these mappings, we're defining that future extensions to those fields are going to work. The whole concept is if you fail processing, you fall back to processing as non-structured-field. When doing cookie work, checked with those folks that they were comfortable representing relevant fields as structured fields. Need to to some work here to make sure relevant teams are comfortable with what we're deciding.

Julian Reschke: don't understand why we need auth scheme mappings for structured fields. Currently same type of grammar as cache-control

Mark Nottingham: what if one of the tokens is an integer?

Julian Reschke: why not the same for cache control? I think we're overcomplicating the issue.

Mark Nottingham: there are a lot of auth schemes that aren't well documented. I'm concerned that one of them will pass a token that's e.g. the number one followed by a bunch of characters and will fail to parse as a structured field. Regarding cache-control, we control the registry so we know what's out there.

#### [Alternative Services](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc7838bis)

Alex Chernyakhovsky: looks a lot like quic server migration. would be cool to do this with h2.

Mike Bishop: DNS does not play in certificate matching. Start with origin, looking for resource at particular URL. Always looking for cert in origin on URL.

Alex Chernyakhovsky: That sounds fine.

**"Desirable security properties"**

Martin Thomson: I think DNS SVCB draft before changing to remove ECH, was very good at talking about things in this particular area. Should frame like clients have a policy when presented with options. If you connect to a server, you get QUIC, and you like QUIC, you might decide that you don't entertain alternatives that don't support QUIC. Same may apply for ECH. If would like to retain ECH, may choose not to go to alternative to avoid regression.

David Benjamin: Works for HTTPS records. Problem with stickiness, if a server wants to turn something off - how does policy work with that? Might need to be careful about bounding. For multi-homed services, security already the least secure protocol / tls version etc. so switching to alternative is no worse

Martin Thomson: I'm only talking about action you take when you see new header field. Only talking about decision for replacing connections.

David Benjamin: what we decide for stickiness for this thing will impact our options.


Eric Orth: having trouble imaging a case where client wants to downgrade from ECH. Draft should say the client should not be asked to downgrade.

Eric Kinnear: always a chance that you can't get to where the server asks you to go. Not worth putting a ton of energy into defining policy because client may not be able to reach alternative for other reasons.

Tommy Pauly: If we're in this edge case where all alternatives have nice properties from original. Original may end up dropping capability (e.g. ECH). May want to include suggestion to query for original name to see if the property has dissappeared everywhere.


**Stickines on Return Visits**

Benjamin Schwartz: instead of needing to concatenate all RRs into single RR set, ...

Mike Bishop: Might be cleaner than current design

Erik Nygren: Another approach would be to have a svcparam that's a label that would exist on both the original and the alt services. Label would need to match between two for stickiness. May be some adversarial cases - should think through them. Mismatch = don't use.

Mike Bishop: Which record would you put that on?

Erik Nygren: All of them would have it. Would require that the host returning the alt-svcb would all have the label.

Martin Thomson: Erik's idea is reasonable and we should explore. Option we chose here is a little weird. May be able to do something more direct and explicit. The way that we've built some of the stickiness here is necessary. For example, if we have a server that returns an alternative on every single response - we don't want the client trying an alternative on every single request. Not particularly happy with the option we have. Using names for invalidation here is awkward.

Alex Chernyakhovsky: Think stickiness is a bad idea from a load balancing perspective. We have DNS, anycast, or client mapping type load balancing. In DNS and client mapping case. With stickiness we have a hard time moving around clients. Have questions around how long does the information last, do we have a limit of number of redirects. This becomes an active control channel for load balancing and introduces a lot of complexity.

Mike Bishop: Current draft says if you takest latest alternative, but don't repeat. 

Alex Chernyakhovsky: Need to be careful not to DoS client

David Benjamin: if there's even optional stickiness, do we have issues with previous question about downgrade?

Mike Bishop: No because of re-resolution

Tommy Pauly: I do think we need some stickiness. I think we can get rid of alt-only. I always do DNS again for origin. In that list I get back multiple options that I am allowed to use - I don't just have to pick the highest priority one.

**Path Forward**

Eric Orth: I like a lot of this draft, but hearing from implementors that this isn't worth the complexity.

Lucas Pardue: Of the possible options here, I think we just change 7838bis draft.

Eric Kinnear: Second what lucas said. 

Eric Rosenberg: Eager to implement this.

Erik Nygren: Before going and adding this complexity make sure we have critical mass of folks that want to implement this. What would make this attractive enough to bring folks over the line?

Martin Thomson: Hearing from some that operate large infrastructure say that it's not worth it, but we're not taking the same position if this would improve things for clients. 

Tommy Pauly: Support implementing this on client side.


### Other Topics

#### H2/H3 WebSockets discovery and detection - Lucas Pardue [slides](https://datatracker.ietf.org/meeting/116/materials/slides-116-httpbis-discovering-websockets-over-h2-and-h3)
[draft-momoka-httpbis-settings-enable-websockets](https://datatracker.ietf.org/doc/draft-momoka-httpbis-settings-enable-websockets/)
[draft-damjanovic-websockets-https-rr](https://datatracker.ietf.org/doc/html/draft-damjanovic-websockets-https-rr-01)

Martin Thomson: you've been given url that points at this name. Multiple HTTP version are available and only some have the desired capability.

Lucas Pardue: h1 different from h2 and h3 because of multiplexing and takover of connection.

Tommy Pauly: we would be losing a round trip because we need to see that CONNECT request fails. Is the round trip justified here?

Lucas Pardue: In my opinion, it is worth it. Not good strong signals to send to client what the issue is.

Bhavana Shankar: How difficult would it be to fold some of these steps into alt-svcb?

Lucas Pardue: It's in the upcoming slides

Nidhi Jeju: What if different protocols supported on different paths?

Lucas Pardue: good point

**Current Problem with just extended CONNECT knowledge**

Mike Bishop: started off saying this is a general problem with extended CONNECT, but then went specifically to websockets. Need general solution to general problem

Tommy Pauly: concerned about precedent for tons of settings. Don't think this is a practical issue

Benjamin Schwartz: don't have any real objection to either of these because they're narrowly tailored to the websocket problem. I don't see it as a real problem - websockets are being replaced in favor of webtransport. We should be leaning into solutions that don't require client to figure out which versions support which features. Websockets are a reasonable exception.

Bhavana Shankar: agree that this needs to be solved because stickiness to websockets is not going to go away any time soon. Didn't understand how you would pick the application layer protocol to use. That should be addressed as well.

Eric Kinnear: Using RR is tempting. This is optimizing an edge case, let's actually optimize it. Seems a little "iffy".

David Benjamin: Agree with Ben overall, we should get out of heterogenous situation. Right answer is go in alpn.

Mark Nottingham: getting feeling that this is in scope for group. Let's take it to the list. Maybe we can form a design team.

#### [Template-Driven HTTP CONNECT Proxying for TCP](https://www.ietf.org/archive/id/draft-schwartz-httpbis-connect-tcp-01.html) - Ben Schwartz - [slides](template-driven-connect-proxy.pdf)

Mark Nottingham: Do you intend to deprecate original CONNECT mechanism?

Benjamin Schwartz: Can't conceive of deprecating. Perhaps we can recommend

Mark Nottingham: support adoption

David Schinazi: Don't see the need for this. Already have CONNECT implemented. Probably wouldn't implement something new if we already have something that works. Now you have two ways to do things. This will make things more complicated. Against adoption.

Benjamin Schwartz: configuration easily distinguishable

David Schinazi: no longer objecting, I'm neutral

Martin Thomson: this is a vastly superior design, I'm in favor

Tommy Pauly: Agree with Martin, I do support this. Let's add that you're allowed to send data before getting a response

Kazuho Oku: seems like the use case that there could be multiple connect endpoints on a server. Can we get the same effect by using authorization? Claify use case?

Benjamin Schwartz: extended connect capable CDN that's forwarding request to origin. Masque able to routed through CDN this way, but we don't have an equivalent for tcp.

#### [HTTP Availability Hints](https://www.ietf.org/archive/id/draft-nottingham-http-availability-hints-00.html) - Mark Nottingham