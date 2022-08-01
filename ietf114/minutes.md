# HTTP Working Group - IETF 114

13:30-15:30 - Thursday Session II - Liberty D

Administrivia

3 min - Blue sheets / scribe selection / NOTE WELL
2 min - Agenda bashing
## Active Drafts

### Summary of Alt-Svc side meeting (Mike Bishop)

[Slides](https://httpwg.org/wg-materials/ietf114/Alt-SVCB.pdf)

- Mike Bishop: Client can't tell when the info carried by Alt-Svc has changed. Instead, move to SVCB in DNS. Several ways to spell this. Design team? Interim?

- David Schinazi: Apologies for missing side meeting, conflicted with the sleep working group. Seems like this is say that the use of QUIC is dependent on the HTTPS resource record in the DNS.
- Mike: Yes, that would be the result.
- Tommy Pauly: Yes, if the only way you learn about it is dynamically. 
- David: That's the only way on the web?
- Tommy: Yes
- David: Unfortunately, most OSes don't let you query HTTPS resource records. Apple does because they're on top of things, but others don't. Getaddrinfo doesn't. I can't do this in Chrome, we're trying to move everyone to Chrome's own DNS client. We can't use that on all OSes, especially ones that are complicated where there's a VPN, we fall back to getaddrinfo. We would lose QUIC if we did that. That would be a non-starter for us. I would love to be a part of this discussion, because that's an important feature for us. In the short term, that's not really the right plan. 
- Mike: In the short term, sure. That seems like an argument for being able to shoehorn it into the existing Alt-Svc. Say I accept the problems if I use one of those, but if I'm on a platform where I can't query SVCB then that's what I need to do. 
- Martin Thomson: Briefly, I understand the implications of having to implement this on a vast number of platforms where DNS is sketchy. Future is bigger than past. We want to move people in this direction, I'd be somewhat comfortable for doing this despite the fact that some people wouldn't be able to benefit.

### ORIGIN H3 (Mike Bishop)

- Mike Bishop: Resolved the one open issue on the document, addressed an eratta from the RFC. Pretty simple document. Are we ready for Working Group Last Call (WGLC)?
- Tommy Pauly: Any comments? Objections? [Sees a thumbs up, no thumbs down]
- Mark Nottingham: Does this touch origin and should we hold onto it for a little while? 
- Mike: Certainly possible to have a broader conversation about connection coalescing that'll touch origin. Could be some things that are nice to fix all-up, but we've previously agreed to not change the semantics of Origin to get the frame over. 
- Tommy: We could adopt another document to do that. 
- David: Another option could be to do the WGLC. I think that would get everyone to read it. Park after that, don't send to IESG. 
- Mark: For a limited time, that makes sense. Maybe until the interim.

### Cookies (Steven Bingler)

[Slides](https://httpwg.org/wg-materials/ietf114/Cookies.pdf)

- Steven Bingler: Published -10 with some changes. Closed some issues since then, working towards 0 in-scope issues. 4 open issues
- [#2185](https://github.com/httpwg/http-extensions/issues/2185) Cookie Octet Reality Check
    - Proposed changes: To merge uint server syntax, allow servers to create cookies that conform to more permissive requirements. Alternatively, we could edit/rephrase the relevant sections to keep people from accidentally doing the wrong things. 
    - If the former, defer since that's too big of a redesign. Latter, in-scope that's not too bad.

    - Ted Hardie: When you say that it would be a lot of work to allow more permissive things, is that something you've tried or just a gut feeling? 
    - Steven: More that it has the potential for a lot of side-effects. Would feel better if the spec had time to let people implement the new syntax and that would delay WGLC.
    - Ted: Thanks for the clarification.

    - Mark: I'm a little confused, the proposal that I made was to (garbled) from HTTP-Core which does exactly what's being talked about here and talks about a particular range of characters. Wouldn't impact implementations, just editorial change.
    - Steven: Yeah, happy to talk about it offline. We've had evidence in the past that people just skim the spec, not sure that they'd understand what obsolete is and they'd see a grammar and implement it.
    - Mark: My experience is that, if we're trying to depend against people who don't read, there's very little we can do by writing things. Alginment with core specs would be helpful.
    - Steven: I like your idea, sorry I didn't list it in the alternate solutions, open to discussing.
    - Mark: Okay, let's chat.

- [#2104](https://github.com/httpwg/http-extensions/issues/2104) Same-Site Cookies and Redirects
    - Chrome and FireFox both attempted to implement, breakage for many sites, had to back out

- [#1939](https://github.com/httpwg/http-extensions/issues/1939) Parser for Domain Attributes
    - Never specifies how to tell if something is an IP address
    - Not worth blocking on

    - Martin Thomson: #1939. Put in chat a regex for distinguishing between names and IP addresses. Pretty simple to explain. Perhaps we pull in a description by reference or just write it out. It's basically one paragraph. Will drop in the GitHub issue.

- [#1399](https://github.com/httpwg/http-extensions/issues/1399) Set-Cookie parsing algorithm

- Once in-scope issues are resolved, hoping to move towards WGLC


### Retrofit Structured Fields (Mark Nottingham)

- Mark Nottingham: One issue open. Do we want to have a representation that is also human readable, or do we want to convey and present as an integer. Most people have trouble reading that. I see both sides of this argument. 
- Easier to make sure presented correctly in tools, etc. 
- Integer is easier to parse, less overhead.

- Long term, binary representation of the structured types, where overhead isn't an issue. There, a human-readable representation is a nice thing to do.

- If we don't ever have binary structured types, no doc and no market adoption, then we're stuck with the textual representation then we do have additional overhead. 
- Also discussion in HTTPAPI if they're minting new fields, would be good to get them including structured types properly.

- Martin Thomson: I tend to think that the machine readable thing is where I would put the integer, not just because I like the ease of processing. Even the dates aren't particularly helpful when there are timezone changes, etc. It takes me ten minutes to work it out, the tools are better at that sort of thing anyway. I do like the idea of having an explicit Date type. If we go for a "profile" of the profile of ISO dates then I'm not all bent out of shape about it. The whole date thing is complicated and we don't need to do the full spectrum of options here, it could be quite simple.
- Mark: You said that you want to go the integer way but you also want a date type? 
- Martin: No, I want the integer, but if we have to do a date type we could profile it and it would be acceptible.

- Tommy: Agree with Martin that it's simpler, also when we're thinking forward to binary representation. I imagine we'll need to allow converting between textual and binary/H1 to H3. Will be less buggy to go from integer to integer than to try to handle leap seconds and make sure you don't mess up your numbers. 
- Mark: Right now, the proposal is not to account for leap seconds, just to be clear. 
- Tommy: Sure, but we can avoid the question. 

- Mark: Happy to go with integer, just want to be aware that users like HTTPAPI will go back to using string headers not structured headers.

- Justin Richer: I don't have strong feelings about this, but I think more friendly to have it be human readable. It's easier to compare two values that are date strings vs. two very large integers. As a human and as a developer. This notion of having it be an integer in the underlying data model and having a string representation matches what the rest of the structured fields do. For example, boolean is 1 or 0 but underlying that is a single bit for booleans. To me, it feels better to define it as an integer data model but with a string representation with a clear format.
- Mark: Great, that's what the PR does. 

- Mike Bishop: Looking at the PR, what's actually sent in the header is the date string. Not the fully expanded one, but a string with year-month-day. 
- Mark: In the textual representation, yes. 
- Mike: Is there a midpoint where we represent it as an integer but give it a character to say this field is a date and should be rendered as such. 
- Mark: We could do that, personally if we believe that binary structured headers is eventually a good thing, then that would give us a wire representation that is the integer that has those nice properties. When you convert it to something you show to humans, you get nice human-readable properties. What I'm getting from people who use HTTP, rather than implementing HTTP, that's a really nice property from them. If it's a really bad representation on the wire, or in tools, then they're not going to adopt.

- Eric Kinnear: Seems reasonable to assume that anyone making tools will look at a gross integer and turn it into something readable for humans. Fine to keep it as an integer on the wire and let tools convert.

- Mark: I need to make a decision. Take it to the list I guess.
- Tommy: No blocking opinions. Seems to be slight preferences for what is easier. People have different perspectives.
- Mark: I might talk to HTTPAPI and show them the PR. If they think they'd look at it for future fields, if they're not interested then maybe there's less of a point.
- Tommy: David Benjamin in the chat is strongly preferring the integer.

### Signatures (Justin Richer)

[Slides](https://httpwg.org/wg-materials/ietf114/Signatures.pdf)

- Justin Richer: Detached signature mechanism for HTTP messages. Works across HTTP versions and weird ways that HTTP exists in the wild. For applications that cannot rely on whole-message encapsulation like you get with OHAI. 
- Take HTTP message, generate signature base using a set of rules for how you take content from the message and put it into the signature. Gives output which is the signature and the list of things that got signed. Send both of those in the ~~headers~~ fields. 
- Needed to make new terminology: 
    - Message Component: Dictionary formatted structured field. Comprised of:
        - Component Name: Name of field, lowercased
        - Component Identifier: Name including any parameters
        - Component Value: Can pull single value from dictionary and sign that, for example.

    - Can combine some of those from a Message Component and get a Signature Base

- Signature process involves generating signature, verification verifies signature base. Signature can be robust across transformations between HTTP versions, etc.

- Draft moved from -08 to -11
    - Better security/privacy considerations. Relationship to digests, set-cookie, etc.
    - Lots of editorial cleanup
    - Allow binding requests and responses, useful for repudiation

- We're seeing people building and actually using this. 
    - GNAP working group is using this as the primary mechanism. I'm also the editor, so not a coincidence.
    - FAPI is an unaffiliated reference. Referenced for OpenID's "Financial Grade API" draft specification. Different use case, but cool.

- David Schinazi: by chat: Clarification question: are the normalized fields sent next to the signature, or the original ones pre-normalization?
    - Justin: You do not send the signature base at all.

- [#2133] Signature Context
    - [PR #2222] makes optional the signature parameter. Would love feedback, leaning towards that PR as the resolution here.

    - Jonathan Hoyland: I think the optional is fine, because it is effectively equivalent to just having it mandatory but somebody can put NULL in. I would say, it's better to say mandatory but can be NULL, that way you can be sure that all libararies implement it. I'd prefer that, but I don't think it makes a huge difference. 
    - Justin: None of the libraries that I've seen are that strict about the parameters. It's an extensible field set to begin with. Point taken, but what we've tried to do is instead say that if a specific application requires it, then it needs to be enumerated as part of the application's signatures.
    - Annabelle Backman: I'd be more worried about confusion on the part of developers using signatures if they have to supply parameters with a NULL value rather than just omitting it. If there are libraries that don't support optional things that are in the specification, then they're not compliant with the specification. I don't know how we can prevent them from doing that.

- [#2134] Cache
    - We're not exactly sure that to do here. Is a signature on a response from the cache meaningful? If you're responding to a signed request with a cached response, are there things you need to be aware of?
    - We're not the experts, please help us out, even if to confirm okay-ness of what's there now.

- [#2144] Server Push
    - We think this might need some text, but we just don't know.

    - Lucas Pardue: As author of the server push issue, I don't think we need to faceplant on it. In a prior life, I have a use case for this thing. Happy to contribute text if you'd like and I have time. If the server produces a response that doesn't validate the signature, what would the client do with it.

- Editors believe this is ready for WGLC.

- David Schinazi: Thanks for the clarification above, that was super helpful. This worries me because parsing HTTP fields is super hard. Doesn't look like it actually is, but the number of security vulnerabilities is astounding. Request smuggling, etc. We're signing a normalized version and sending a non-normalized version which sounds like  it's asking for trouble in that area.
- Justin: For the most part, you sign exactly what is sent across the wire. There are cases where you can opt-in to transforming that in different ways. (list of cases). For most developers it will be "take the thing off the wire and use it". Normalizing how the stack did the siganture base, which is not anything that's sent.
- David: But that's still an issue if the unnormalized text triggers the vulnerability and the normalized one doesn't.
- Justin: Because you're not parsing the signature base to get values, it's not as scary as it seems. Lots of text about that.

- David Benjamin: I want to echo what David Schinazi said about the normalization thing. Basically everything cryptographic that uses signatures. If there's any property of the message which the normalization process drops, if that thing is ever read by someone downstream, that's an opening for the attacker to change the interpretation of the message. By definition, that's a thing with this type of normalization. That will result in a security vulnerability. I understand why you wanted to do this, since you want to sign something that gets exploded into the wire image for HTTP. Safer would be to have the thing you parse be exactly the thing you sign. Perhaps take the HTTP message and express it in the binary format and then sign that. The thing that you sign needs to be the thing that you parse, or else there's room for other unsigned input to get in. That's related to where attackers can inject stuff. I noticed that there were signature parameters that can change what is even signed. How is that carried? A header? 
- Justin: No, it is very strictly defined as an ordered set of identifiers.
- David: I don't mean the format, just how you receive it.
- Justin: It's a header. Also the last line of the signature base every time.
- David: If included in the message, that limits that. Still an issue here though. 
- Tommy: Overtime, can you and David S. do a review and send those comments to the list -- analyze what's in the text and point out if there are gaps.
- David: Sounds good, if you can point out where you see signification normalization of values. As a spec author, something we try to avoid is any normalization of values beyond what's already part of HTTP, etc.


### QUERY (Julian Reschke)

- Julian Reschke: Not a lot of progress from last time, sorry. Looked at the issues, what's left to be done depends on what people expect from this specification. If they expect similar to POST, without side effects, then we're probably pretty close to done. If they are looking for something which introduces proper cacheability then more work needs to be done. Every time we look at these issues in a WG session, we get into the details and it's not simple to define these things properly. Could use a small design team to have a few sessions and make a concrete proposal for how to close the remaining issues.
- Mark Nottingham: I'd be happy to help.
- Julian: I'll try to summarize on the mailing list and invite people to volunteer. Will find a timeslot in the next few weeks. 
- Tommy: Volunteers here and on the list. 

Volunteers: 
- Mark Nottingham
- (ideally, more from the list)


## Other Topics

### Resumable Uploads (Guoye Zhang)

[Slides](https://httpwg.org/wg-materials/ietf114/ResumableUploads.pdf)

- Guoye Zhang: We are bringing our draft to the working group in the hope of standardizing resumable uploads. Want to resume when interrupted -- today this works for downloads, but not for uploads. This means that things built on top of HTTP to offer this are not all compatible.
- tus is one of the most popular resumable upload mechanisms. (example of how it works, POST yields identifier, PATCH to resume)
- Using that as a starting point. Main difference is to use a client-generated token. This reduces by one round-trip (1-RTT) when creating an upload. Also backwards compatible, if you don't support resumable upload it's just a regular POST.
- Can send intermediate 104 if you support resumable upload. Can resume with HEAD and PATH aarequests.
- Feature detection mechanism to allow upgrading regular uploads. Lots of ways to spell this.
- Upload metadata. How do we specify filename? Would be nice to use a standard header. Also media type/Content-Type. Upload creation should set the upload itself, but mailing list discussion says that we should be using a generic mediatype for the appending procedure.
- Adoption? First, is this resumable a worthwhile problem to solve in this working group? Do you think this is a good approach as a starting point?

- Alessandro Ghedini: I have a question about the client generated token. It seems like it might be a problem for a server operator where the server needs to guarantee that the token is not reused across different clients. The server might also want to encode different information in the token to avoid maintaining certain state. It would be better if there was a way for the server to generate the token.
- Guoye: The token is generated 256 bit random by client, but if you own the client you can use your own token or encode stuff in it. 
- Alessandro: So the problem arises where the server and client aren't from the same entity, this proposal is to create something interoperable. Can't assume that the server controls the client.
- Tommy: Overall impression? Interested in talking about it.
- Alessandro: Interesting problem. I think Lucas is involved in the design. We are interested in doing things that other people are interested in doing, not a lot of point if nobody is going to use it. There are potential use cases internally where we may want to tranfer big files, stuff like that. 

- Mark Nottingham: There's a trick to play here where you want to design something that's interoperable and works out of the box, but you don't want to rule out other valid uses. For example, the initial POST to get the token, perhaps it's a PUT if the client knows where it's going to be. 
- Mark (with chair hat): For proposals like this, it's important for proponents to understand that they're giving change control to the community and, while they can participate, they're not in control anymore. Encouraged to see "starting point" language. Nice to see other people have been working on this, like tus, for a long time. Seems interesting to work on and this is a good starting point.

- David Schinazi: Nice presentation, very clear and understandable. I have read the draft and I think it is a good starting point. I think there will be some tricky questions to answer, but I'd rather we do that in the working group so we build something that we can operate that everyone likes. We might have some uses for this. I'd say I strongly support adoption. 

- Alan Frindell: Thank you for the presentation and the draft. We've had our own version of this technology running for many years. I think this came up in a workshop 3 years ago. Keeps coming up, should have made a standard a long time ago. Seems like a reasonable starting point. Let's adopt and have discussion in the working group. 

- Tommy: Cloudflare and Microsoft in the chat also indicating they do something like this as well, doesn't interop. Sounds like everyone is happy with letting the working group have some design team to go figure out how this would work. Let's take this to the list, ask if we want to work on this, starting here and acknowledge that it will completely change, but let's start with this.

### GeoIP (Tommy Pauly)

[Slides](https://httpwg.org/wg-materials/ietf114/IPGeolocation.pdf)

- Tommy Pauly (sitting): We have some updates on geo-location work. David and I took feedback and revised the approach.
- Clients sometimes, but not always, want content that's relevant to their location. Assuming that you didn't use javascript APIs to share precise location. Problem that I've been experiencing, and that others are sympathetic in conversations, is that databases are often out of date. Relying on aggregation databases that aren't authoritative. Often incorrect specificity.
- Problem for privacy proxies, but also for new IPs, anything that changes location frequently. Cellular networks often, or ISPs. Manual outreach process of users complaining and then someone has to manually refresh.
- Fraught with peril, anything you send that's derived from actual location, this is a dangerous privacy foot-gun.
- Safe to do this if location is derived from IP address that you were showing anyway, but really you could just share the "correct" GeoIP entry and maybe associated feed that owns it, instead of anything more specific.
- Client behavior: Expect that clients know what IP geo they have. Can learn from ISP or carrier. Client only shares if opt-in.
- Server behavior: Can always blindly trust, clients can only screw up their own search results, for example. Could prefer the feed if it's trusted. Could check mismatches and use it as a signal to refetch from the feed. Could flag it as a place where there's a new feed that's coming online.

- Alessandro Ghedini: Interested in working on the problem. Haven't thought too much about the solution, but this is probably a good starting point. Not sure if httpbis is the spot, but leave to others to decide.

- Matt Stock: I agree this is an interesting problem to work on. One piece of particular interest to me is how to think about this in terms of satellite services where IP in terresterial network doesn't algin to traditional location. Hard to keep databases up to date. Definitely interested in exploring more.

- Brad Lassey: Definitely interesting place, support working on it.

- Martin Thomson: I'm going to disagree. I don't think this is quite right. One of the reasons that GeoIPs aren't such a problem for privacy is because they're very bad. Trying to fix that problem puts you back in the same box with geohash. When you have good geolocation and you start moving around, it introduces the ability to track them. Depends on populations in that area. That has implications for privacy that I don't think are addressed in the document.
- Tommy: Since this in reflecting information that a well-updated server database would already have, this is no more information than what they already have. Removes out-of-date that hurts the user but doesn't help the people who want to track you the most.
- Martin: I'm not going to say this is impossible, but we spent almost 10 years on this in the past and came to conclusions that it's very hard to give away any geolocation info without giving it all away. It might be less of an issue here, but the inherent problems in what you're doing might help keep people private. I don't think it's reasonable to say that you understand the privacy implications of this design.
- Tommy: My goal is to produce a document that reduces to the same privacy properties that you'd have by using that IP address in the first place. 
- Martin: You are doing this in the context of a privacy proxy, giving people privacy and now you're taking this away.

- David Schinazi: MT understands this space better than I do. If we can't figure out a tight privacy box then we shouldn't publish this. One idea I have is deployment models. For Google, we're not planning to use this through our privacy proxy. Using it _to_ the privacy proxy, instead. Using private access tokens, or other anonymous tokens, to avoid correlation between multiple requests over time. That defeats the correlation of information that you gave away. Not saying problem solved, just that it's possible to reason through it.

- Chris Lemmons: I don't think we can solve this problem, but I think we can make it better. Seems to be a good starting point.

- Erik Nygren: From past experience, not sure this is super useful. Trouble coming up with reasons/people that would use this on client and server side that aren't already in a position to take a different approach or use a different approach to get feed information in other ways.

- Brad Lassey: Good to get opinions of people here, can change accuracy based on population density. Think of it not as folks who have opted to use a privacy proxy, rather improve privacy overall by making it less painful to use a privacy proxy and thus improve privacy overall.


### Transport Auth (David Schinazi)
[slides](https://github.com/httpwg/wg-materials/blob/gh-pages/ietf114/TransportAuthentication.pdf)

- David Schinazi: So now I have to do it all versus join me as Kauth are together on this and please ignore the title transfer certification no longer going to change the transport so we just have to come up with a better one next one please so what is your motivation we want the client to authenticate itself to the server like OK great that's it yo exists top of that we want to use asymmetric cryptocurrency are exist so Valparaiso balls but we have yet another requirement that is what you want us

- David Schinazi: Motivation, want a MASQUE server that doesn't tell everyone it's a MASQUE server. Today, you use a nonce for asymmetric cryptography, which leaks the fact that you require authentication.
- Proposal, from Chris Wood back then, use a TLS Key Exporter. Not reinventing token binding. Insight is that TLS handshake has fresh random data from both endpoints and a key exporter creates pseudorandom numbers from both of those random bits. Use it to create a nonce, not a key, that the server had input to. You sign that nonce so you don't need to transmit it, server can decode it as well.

- Jonathan Hoyland: (Clarification question) Idea of nonce as only used once, what if I do one authentication that fails and then I try again, I'd use the same nonce. How do I get two nonces within one TLS session. 
- David: Good point, will need to think about that, this is why we bring it to this room. 
- Martin Thomson: Had the same thought, you don't have fresh entropy but you could. Client can provide fresh entropy each time it provides one of these assertions that it makes, then there's no key reuse problems. 
- David: Sounds like it doesn't break the other properties that we want, so that's good. 
- Jonathon: Do you actually need fresh entropy? Can't you use a counter, like this is attempt one and this is attempt two. 
- David: Yeah, that's essentially what MT is saying (MT confirms, yes).

- Intermedaries, obviously tied to TLS handshake, doesn't work through intermedaries. Intermedaries check authentication prior to sending request upstream, this is commonly done today anyways, so not seen as a big problem.

- Independent implementation by the Guardian Project. Interest from the HTTPBIS WG? Even from discussion so far, have benefited greatly from input from the WG.

- Mark Nottingham (as individual): I think this is an interesting area of work. Possibly important, even. I would be more comfortable if the draft were positioned in terms of what properties it has instead of the solution. The word "transport" is not helping you right now.
- David: Need to rename it, totally with you.
- Tommy: Right, focus the solution on properties/problem you want to solve

- Alessandro Ghedini: This reminds me of the certificate frame. Thoughts? 
- David: I haven't implemented the certificate frame myself, but this seemed way easier to get into an existing codebase. 
- Alessandro: That's a frame, this is not a frame. There are different use cases for a frame, like post-request authentication if you want. Certificate frame uses X.509 certificates. There are probably ways to use raw public keys for that as well. Certificate-frame-type solution seems more broadly useful, even beyond client authentication. 
- David: Concern with using a frame, even today HTTP/2 servers explode if they see a frame they don't recognize, even though you're supposed to be fine with that. Also prevents using HTTP/1. If I can stay far away from X.509, I'd be a happy person.
- Alessandro: Probably a way to spell that that doesn't require a certificate. 

- Alex Chernyakhovsky: Doesn't work for intermediaries. Only generally applicable if we can fix that. Didn't read that section in the draft. I think this is a footgun waiting to happen in the current formulation. This authenticates the channel, not the session, so we have additional cryptography challenges when we go to H2 and H3. Designed something internally to Google that used TLS Exporters to bind X.509 to Google-internal certificate and there was a bunch to deal with there. We'd need to discuss a bit more. 

- Tommy (chair hat): Sounds like we'd want another version of the draft that frames it a bit less as transport and more as a problem you want to solve.

### METADATA (Bence Béky)

[Slides](https://httpwg.org/wg-materials/ietf114/METADATA.pdf)

- Bence Béky: New frame for HTTP/2 and HTTP/3 called METADATA.
- Widely deployed at Google in HTTP/2, working on HTTP/3. Needed to do HTTP/3 internally between our proxies. 
- Negotiated via a SETTING. Carry HPACK/QPACK encoded key-value pairs, no dynamic table, no HTTP semantics.
- Also, thanks for all the feedback on the mailing list.

- Tommy Pauly (as individual): Having yet-another opaque blob that you can transport through here is concerning and raises a few alarms. It seems to me that the mechanism that we have that allows you to do this, we already have frames. It's sort of a frame within a frame. Makes sense for a proprietary deployment. Are there specific frames that you'd want to define? You gave some examples, could we define those as first class frames rather than another registry with a different list of frames.

- Martin Thomson: Thanks for the presentation, it's always great to get an insight. All I heard was that Google has a bunch of proprietary extensions to HTTP/2 and HTTP/3. Not seeing any way that needs interoperability. If there are things that you are doing here that you think are useful for people to use in other settings, I'd agree with Tommy, consider defining a frame for the exchange of that information on either a control stream or a request stream, whatever makes the most sense. An entirely generic bucket, I don't think is especially interesting in terms of standardization. 

- Bence: Appreciate the feedback. Unfortunately, nothing that we'd be comfortable talking about externally in terms of concrete use cases. Bringing to the WG to gauge interest and see if it sparks any similar use cases that other people are interested in. If nobody jumps up and says that they want this, then that's also an okay outcome. 

- Lucas Pardue: Thanks for bringing this to the mailing list. I think it's a good time to chat. I'm aware of use cases where people are trying to carry sidecar data along with requests. Those people have struggled with how to do this, maybe doing weird CONNECT and hacking some chunking alongside. This could have been a neater solution. Capsule kind of goes towards that, not advocating we should use capsules. The most generic thing opens up a can of worms that developers that aren't us will think they can start sending headers and doing whatever and it'll work somehow. 

- Alan Frindell: I'll offer a counterpoint. HTTP header fields and trailer fields are already generic, that's part of what makes HTTP so generic, you can just stick your own headers in there. This provides some value and we've had some use cases internally, for example timing data, stats in the middle during a long-running response. I told someone once to use push, which should tell you how it's going. 
- Tommy (off mic): How about a timing frame?

- David Schinazi: I encouraged them to come and present this to the IETF. Google is using it widely. Probably going to put into envoy, which is used outside of Google. If nobody wants it in the IETF, that's fine too. Willing to hear feedback.

- Mark Nottingham: To respond to Alan, if we do want to add something like this, we need to look it as a change in the developer-visible signature of HTTP. Right now we have request/response, header, body. If we do that it needs to be very deliberate and well thought out. Even pipelining has been hard. We did this with server push. Not a hard no, but there be dragons.

- Mark (as chair): Next steps are more discussion and maybe some clear use cases.
