# HTTP Working Group Minutes - IETF 119

## Tuesday, 19 March 2024

_17:30 - 18:30 Session IV - P2_


### Active Drafts

#### Cookies

- Fixed same-site bug in spec, but turned out sites relied on it so have reverted the spec change. Will try to do it again in the bis bis (bisque?).
- Remaining issues are small. Almost ready for WG last call.
- mnot thinks substantial last call (4 weeks+)

#### Unprompted authentication

- Since Prague, have 4 independent, open-source implementations, and have done an interoperability test. It worked (barring Http level mismatches)!
- Security analysis done. Proved the authentication properties; doesn't really have any other properties. Proving how it binds to TLS. The model assumes TLS is secure (let's hope, eh?). Link to report will go in the chat.
- Defining a new field to use with intermediaries.
- Mike Bishop disagrees it's similar to client certs.
- As long as the backend trusts the intermediary, it should be fine.

Martin Thomson: who validates the cert? Not the intermediary - it's passing it through to the backend. But how do you know it's not modified on the way through? You don't, you have to trust it.

Jonathan Hoyland: security assumption is the exporter key is channel binding, so you can publish it without damaging security.

Bike shedding time: what should we name this auth scheme? There's already another draft with this name! We should probably rename. How about "UnpromptedSignature"? 

mnot: Can we name it for the benefit to the user? e.g. "Hidden"

Justin Richer: Naming things is hard. RFC9421 dropped the use of the current name, so could use it. But… it's already used by Mastodon and a big bank. So maybe don't. Getting away from signature is a good idea: that' just how it does it, not *what* it's doing.

Benjamin Schwartz: Couldn't find anything in the draft to say why we shouldn't just use BASIC auth for this. Maybe going through those reasons would help to name it.

Jonathan Hoyland: Likes "Unprompted".

Peter Thomassen: Suggests "Unsolicited".

Other than the name, mainly just editorial work to do, then WG last call.

Jonathan will get open-sourcing approval from the company and share the link to formal analysis artifacts on the list.

#### QUERY Method

- Work a bit stalled.
- Will be discussed at a side meeting instead.

#### Resumable Uploads

- A few implementations exist, both server and client.
- Still need to define a media type for the PATCH requests. Perhaps `application/partial-upload`.
- How do clients discover server limits? Could announce them in header fields in response to POST and HEAD requests. Either multiple headers, or one header with a dictionary value. But this would require a registry.

mnot: Would recommend using a single header as they are all related. Does not imply you need a registry - can just put it in the RFC and say you need to update the RFC to add anything.

Lucas Pardue: Similar to rate limit headers?

Yaroslav Rosomakho: expires as a timestamp. Why are we not using a more common date format?

mnot: There is a discussion about this somewhere.

Martin Thomson: Prefer this does not use absolute times, as there are 2 clocks in the protocol and they never agree. Also means you can have a static expression of policy, which is simpler and compresses better.

mnot: Any pushback on whether we should do this in general? No.

Martin Thomson: All the header fields need to be optional, because servers may not have a policy or may not wish to express it.

Lucas Pardue: Is this something that should just be resumable uploads, or for any uploads?

Marius Kleidl: Mostly specific to resumable uploads.

Interrupted PATCH requests: semantics we want are slightly different to the RFC definition for PATCH.

mnot: Strictly should update the PATCH spec, but can probably just do some careful wording here to avoid that.

Martin Thomson: Agreed. Can go further and just say that any change in flight you will not see the partial change when querying the resource from elsewhere, which won't violate the RFC.

mnot: From a strict semantic standpoint not sure that's true, but everyone is fine with the spirit of it.

mnot: Could even raise a technical errata against PATCH.

How do you handle content encoding if you get interrupted and have to resume?

Mike Bishop: I think even though we often produce it on the fly, it's saying this resource is GZIPed JSON. So if you upload half of it, you are uploading half the gzipped thing. The partial upload is just resuming the upload of the gzipped resource.

Martin Thomson: The way to think about this is the representation you are sharing in the resumption is just the bytes of the original, so there can't be new content encoding.

Martin Thomson: It's well defined if you add content-encoding to the PATCH, but don't do that, it's gross.

Lucas Pardue: if bogus clients *do* do this we can detect it, as we have digests.

mnot: Maybe we need some guidance on how to hold it.

Marius: Still some more open issues, but hope to finish up before too long.

David Schinazi: On the topic of deprecating the old Siganture HTTP auth scheme, should we mark it deprecated in the IANA registry? The only way to do it is in an RFC draft.

mnot: Let's have a chat about that.

Finished on time, meet again later this week. Until then, adieu.

## Friday, 22 March 2024

_09:30 - 11:30 Session I - M4_


### Active Drafts

_See also the [extensions listing](https://httpwg.org/http-extensions/)_

#### [Templated Connect-TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp) - Ben Schwartz (remote) / [slides](https://httpwg.org/wg-materials/ietf119/connect-tcp.pdf) 

3 issues to discuss: 

1. `tcp_port` ([Issue #2713](https://github.com/httpwg/http-extensions/issues/2713))

Tommy Pauly (individual): We have a discussion and document in intarea for discovery of getting a JSON file with configuration of the proxies you support. That's one way to disambiguate things, if you get a proxy URL and you don't know what it is, you can ask it for that file and it will help tell you. I'm not suggesting that we point to that from this document, but overall that is a solution space fir a separate usage indication. 

Ben: That's limited to provisioning domains? 

Tommy: The doc in intarea is saying that every proxy has its own implicit PvD, you just ask it for a well-known URI and it can tell you about the specific protocols it has.

Ben: I'm personally neutral on this question. I think probing is pretty ugly, I find this quite unfortunate. It's also a little weird to have a proxy but not know what it supports, fetching something via the proxy to find out how to use the proxy gets complicated. Seeking input on that.

2. Happy Eyeballs and `target_host` lists

Tommy Pauly (individual): Apologize for having opinions. In the camp of dropping this, as far as I know this isn't something that anyone has a lot of experience with. Would like to see this parallel across the various proxy methods. UDP may not work, but can also have variants that are aware of QUIC. There's a chance for a Happy Eyeballs related WG that this could be discussed in. I would go for dropping the feature and then, for extensions, we do have the ability to add other headers, we can use capsules, would like generic solution.

Eric Kinnear:  We should not over-rotate on the syntax, but we should focus on making sure we have parallel capabilities across the connect types. UDP still knows how to handle A and AAAA responses coming back, can still do the "regular" thing there.

Jonathan Hoyland: I haven't followed this at all, but why can't you send a URL to the server and let it handle Happy Eyeballs, DNS, UDP, everything. 
Ben: Yes, it would be a hostname and it can resolve and that will be the same as today. If something isn't coming from the server, can you give the server a set of things you got from DNS and let it do the same thing.

3. Capsule protocol

Tommy Pauly: I'm okay with leaving it for a later thing, although I would like to do that quickly, but I'm concerned that if we do not mention the capsule protocol at all that we could have implementations that set it and have a different interpretation, so we may want to prohibit the use of it until we have it defined somewhere else. 

Martin Thomson: If we don't tell people that it's a capsule protocol, then it's not, and you've effectively prohibited it anyway. I think that's the default.

Ben: We can put in a non-normative reminder. 

Martin: We're also not transporting elephants, I wouldn't bother.

David Schinazi: I think it could be cool to use capsule for this, I don't think "maybe use capsule" is viable at all. When we defined the capsule header, we decided it meant nothing, you don't have to send it, you can't use it for any kind of negotiation. Our only two options are to say it doesn't use capsules, it's like regular CONNECT, or it uses capsules all the time and we introduce a DATA capsule. Or we negotiate via another header (suggestion by MT). I don't feel too strongly though.

Mike Bishop: Do we have a use case for capsules with this? If we don't and we can't envision one, let's not build it until we do. Martin, I admire your optimism but we say lots of obvious things in QUIC, we can do it here too.

#### [Security Considerations for Optimistic Use of HTTP Upgrade](https://datatracker.ietf.org/doc/draft-schwartz-httpbis-optimistic-upgrade/) - Ben Schwartz (remote) / [slides](https://httpwg.org/wg-materials/ietf119/optimistic-http-upgrade.pdf)

Lucas Pardue: I know this is focused on CONNECT, but I had a case with someone who was seeing an issue with plain-old "I'll make an HTTP/1 request to a server" and it failed and they didn't know what to do, their answer was to close the connection since the whole thing was completely blown. Wasn't an upgrade, was just a POST. Is that already covered? 

Ben: Malformed? 

Lucas: Configured proxy would try to pass request to upstream, which wasn't there, so you'd get an error, proxy couldn't process anything further

Ben: That should be unambigious from the gateway's perspective, it should be able to read and process and entire post request. 

Mark Nottingham: Would like to talk about that after the session.

#### [Retrofit Structured Fields](https://datatracker.ietf.org/doc/draft-ietf-httpbis-retrofit) - Mark Nottingham

Mark Nottingham: We've been lightly parking this for a while as we completed sf-bis, that's now mostly done. Returning to this. There are a few issues to work through. The thing that caused us to park this was that it's very abstract, talking about mapping existing fields into structured fields. We're not entirely sure what the sharp edges are until we actually use them. This is a status update that we're going to start trying to get this one moving again. Any discussion/comment?

Martin Thomson: I'm kinda curious as to whether you have any thoughts about what getting moving looks like? 

Mark: Half-baked thoughts, we can talk all day. 

Martin: Thinking then, wonderful.

Mark: Yes.

Mark: I feel like a lot of people nod and say this is good, but we have to get it right if we want to do it here.

Mark: MT is nodding, for the record.


#### [Cache Groups](https://datatracker.ietf.org/doc/draft-ietf-httpbis-cache-groups/) - Mark Nottingham

Mark Nottingham: Straightforward, there is implementation experience with the concept. Details for requirements need to be worked out, did some survey.

Mark: If a group has a resource that is revalidated, assume that everything else in that group is also revalidated. Thinking of dropping since we have no impelementation experience with this at all, nor any measure of demand. But that makes me think that maybe we need an extension mechanism.

Mark: Otherwise, I think we're pretty much ready for WGLC, interested in opinions. 

Martin Thomson: Change the name if you're not going to do revalidation?

Mark: See David's bikesheds from Tuesday. Different vendors call this different things, didn't want to favor any one vendor, but am open to new names. 

Martin: Sole purpose is invalidation, maybe worth working that in to make it clear.

#### [Compression Dictionary Transport](https://datatracker.ietf.org/doc/draft-ietf-httpbis-compression-dictionary) - Patrick Meenan (remote) / [slides](https://httpwg.org/wg-materials/ietf119/compression-dictionary.pdf)

Lucas Pardue: A thought on the last point, who's using filesystems these days with cloud object storage. I don't know about this stuff, but legit question.

Patrick: What's been done before is the request header of the available dictionary could have been tacked onto the URL and tried as a request using edge functions that are already available. If the origin added the hash to the end of the filename, that would just work.

Lucas: I just wonder how often it is that a server receiving requests for a path has to remap into object storage IDs. Maybe that's an easy thing that people are already doing. 

Patrick: Fundamentally very similar to storing .gz files for pre-gzipped files.

Martin Thomson: I know this isn't an implementation/deployment report. I'm curious about the split between the use of this for deltas and I have an arbitrary dictionary that's going to match a ton of stuff. I see the former as being relatively straightforward to implement and the latter being far more complex. When you said "you have to do a linear search through all the patterns in order to find something", that rang alarm bells for me. 

Patrick: On the client side, it has to use linear search, if you're not using match-dest and you match all requests. For example, if you have 10 dictionaries, given a request there is no way to have a lookup without looking through each pattern. You're limited to the global number of patterns that you're going to have on an origin. If you have 1,000s on a single origin that could start to become a problem. 

Martin: Do you have a solution for that problem? That sounds like a real problem. 

Patrick: Not really. You could probably do things on the client side to optimize for shared prefixes on the paths if the paths are all relative and you could make it a little faster. It's very similar to the service worker pattern matching, and you allow arbitrary patterns that aren't just a prefix, it's hard to be more optimal than that. It applies to both delta and dynamic case, since both have to run the pattern matching.

Martin: We probably need to talk about this a little bit, that sounds like a Denial-of-Service vector to me. 

Patrick: That would be an origin denying service to itself, since it's the only one that can set things for itself, but they could be multiple teams that don't talk to each other. 

Martin: Client does the work, though. 

Patrick: Only when talking to that origin, it only looks at the ones that came from that origin. It's scoped by site, so the site and origin combined is the partitioning boundary for the dictionaries. 

Mark Nottingham: Martin, can you open an issue if you think there's something there after some more thinking? 

Martin: I will.

### Other Topics

#### [HTTP/3 On Streams](https://datatracker.ietf.org/doc/html/draft-kazuho-httpbis-http3-on-streams) - Kazuko Oku and Lucas Pardue

Yaroslav Rosomakho: Interesting proposal, I think it's unlikely to achieve its goal of allowing applications to run solely on HTTP/3 stacks. Today, majority of enterprises block UDP because they have proxies/firewalls and things that want to man in the middle TLS. Those things are not capable of inspecting QUIC. If you're introducing a new way to send HTTP with new ALPN, then those things will still not allow that ALPN to come through.

Lucas Pardue: Not going to disagree there, if we change the wire image of H2 to do some of the stuff that we're talking about, then that will also be a change and those same people will have that same problem. If we're stuck with all the broken stuff, that's not great. If it's H2 that's H2-and-a-bit and it looks like QUIC, or if it's H3 and it goes over TCP, those boxes will continue to break things. I'm also aware of middleboxes that have added support for intercepting HTTP/3 and QUIC, and that's totally up to them.

Yaroslav: What I'm trying to say is that you will still need to maintain two stacks.

Tommy Pauly (individual): Been thinking a lot about how clients without UDP can access QUIC and UDP generally. How do we think about this: I'd like to challenge us to think of it more like a proxy, like we're just going to run QUIC over a TCP-based proxy or a tunnel in order to bypass the thing that's blocking QUIC. That's something you can do today, you can run CONNECT-UDP over HTTP/2. It has inefficiencies, absolutely, but it lets you access the thing. Can offer a legacy translation proxy, will leave you with end-to-end HTTP/3. We are always going to be accepting some performance regressions. We want to find ways to decrease the performance regression, perhaps we tell QUIC about reliable substrate, already encrypted substrate, ways to reduce harm of the performance regressions. One of the benefits of that lets us keep migration and multipath with the end-to-end QUIC. I don't think you're in a good place if it's not compatible with end-to-end QUIC.

Mark Nottingham (individual): I like this proposal. Has a lot of promise in simplifying the stack and unblocking work in the future. Most of the benefits that it brings go to implementers and specifiers. Most deployments, there's not a strong reason to adopt this. If there's not a strong reason to upgrade a protocol, people won't upgrade. We have to conclude that there are going to be a lot of HTTP/2 deployments out there. We might be in a world that's more bifurcated, we don't want to ignore the major HTTP/2 deployments because we're all paying attention to this. MASQUE and other things are used by a very small set of entities on the internet. Larger deployments still need attention that are much more "regular".

Lucas: It's non-trivial to create a way to speak QUIC and have it be scalable and robust. There's a lot of work beyond turning it on. Being able to focus a feature set on H3 and make that easily deployable for services is important.

Mark: I agree, and so I think this is one possible future. Is someone going to do the apache module for this. If there's an actual, natural upgrade path, then I'm much more interested.

Alan Frindell: Thank you for bringing this work. Taking a step back, I think the QUIC-on-streams protocol is valuable and has a lot of use cases, even if you ignore HTTP entirely. There's not a great way to do multiplexed streams on TCP right now. HTTP/2 is close, but not great. I think there are a lot of use cases for this protocol that go beyond what people are maybe thinking about here. We've basically decided what a modern transport interface looks like, and it looks a lot like QUIC. WT over HTTP/2 is basically this, just less efficient. Supportive of this work and I know that it's not possible to remove H2 for everyone, but Meta would likely remove H2 support if we had this.

Martin Thomson: I think it was on slide 6 that you talked about retrofitting QUIC flow control to HTTP/2. You observed a few things about why that didn't work out, it was that there just wasn't enough interest. I'm concerned that this is adding code to solve a problem of having too much code. Without an incentive to upgrade, we're in this really awkward position. If nobody ever upgrades and don't have time to invest in the development of an entirely new stack. We're in a situation where we have to keep H2 alive anyway. Adding more stuff to the pile is not necessarily something that I'm enthuastic about. I like the design, I like the idea, I like the promise that this has, but I don't think until we have more reason to do it that this is something we should be pursuing. If we had HTTP/4, and there was some new thing that we wanted to do over TCP, then fine. Maybe the MoQ people want to fall back to TCP, and that's enough justification, but we don't necessarily have to do it for HTTP at that point. Along the same lines as others earlier, this is a great idea, but the great idea has a huge activation energy. I want to make sure that we can justify that. 

Lucas: To respond quickly, I agree with those points. I think it would be interesting to see how it goes.

David Schinazi: +1 to everything MT said, I was much more opposed to this in the QUIC session and then we had lunch and now I understand better. I've distilled the disagreement to fundamental assumptions. If this allows you to get rid of HTTP/2, then this makes a lot of sense. If you're a browser or a cloud provider, you're going to need to keep HTTP/2 support forever. Another assumption, can you use HTTP semantics to be version independent. Incentives will be the hard part.

Eric Kinnear: Started out very dubious. Tunneling QUIC is nice, but you still need to be better than HTTP/2, which that isn't. I do like having migration and multipath work. Question is if we think we _have_ to do something to fix HTTP/2. Development of entire new stack -- we're still investing in H2 if we keep that going. Keep HTTP/2, but we then have to implement a pile of "new" things on top of it as well.

Kyle Nekritz: I'm very sympathetic to the problem here. Very compelling for cases where you have a new protocol and you just want something that works. If you have a middlebox that's blocking things, a middlebox that upgrades would be fine to support QUIC. There's also an issue where you can have a fallback stack that doesn't have such great properties (like TLS 1.0), it makes it difficult to make an argument for security properties. Need a way to mandate using the same TLS stack with a minimal set of differences.

Mike Bishop: I feel like we really should learn some lessions from the last time we successfully deprecated an HTTP version. As mentioned, we still have a little bit of 0.9 around. I love the idea of this for a brand new protocol that is going to build over QUIC, but knows they need TCP fallback, I'd love to have a doc in the transport area where we could just shim this in. I'm very hesitant about trying to put HTTP over this. Hopefully, we get 90+% code reuse and just branch between the different paths we have to support this, but I'm concerned that that may not be the case as you iron out the things you need to ship and not just have a proof of concept. I'm not sure HTTP is the first place to do this, but I do see promise.

Ted Hardie: On slide 10, I agree with Mike on one thing: If you take this as "what if there were a transport protocol" with the understanding that it's not new, it has to run over TCP or UDP, that would get you a critical piece that gets you here. Concern is that you don't get the same thing as when you're run over UDP vs. TCP, they're different below the API and I don't think you're going to successfully unify them. Tommy's shim is cheap and easy and works today. The delta between how well that's going to do and the activation energy to get what Mike's talking about is enormous. We should live in an internet where things don't have to use TCP or UDP, we don't live there, need to deal with the ossification that we've got. If you want to run with sufficiently different behaviors for TCP in order to avoid the API problem, the ossified internet might kill you anyway -- you're running on top of TCP and not in a TCP-like way, and that's going to get you killed. That's speculative, of course, but I think the problem is "how do I deploy a new transport on the internet". We do have experience that says transport over the internet runs via UDP. 

Lucas: Can I ask you a clarification question about TCP but not in the way people are used to. 

Ted: If you're running a firewall that is doing packet train analysis or more advanced things, something that looks sufficiently different from known traffic for a known protocol will get blocked. For example, something that doesn't do request/response in a way that's appropriate.

Alex Chernyakhovsky: If we take it as sort-of-granted that it's going to make it out there, there are protocols like SSHv3 that shouldn't be on top of HTTP but need a TCP fallback. We find ourselves here in a weird position where the underlying substrate is already going to exist, what's going to stop someone from defining the ALPN to make this work and just having it work? A key success metric here is if it's trivial for users of HTTP/2 to migrate. I'm okay if we walk away with "not yet, let's get deployment data". If we get the data to show that it works and that it's as easy as we want it to be

Mark (as chair): We've never done a new HTTP version without more discussion, there needs to be more of a hurdle than normal adoption. Part of a bigger discussion about how we maintain and evolve the protocol. There are aspects of this that the community would benefit from. Perhaps at the HTTP Workshop?

Lucas: Thank you everyone for the various opinions and the really respectful conversation.

#### [Reverse HTTP Tunnels](https://www.ietf.org/archive/id/draft-kazuho-httpbis-reverse-tunnel-00.html) - Kazuko Oku

Martin Thomson: I think you need to think about the security model a lot. As a browser, I couldn't do this without a lot more work and the security model is key.

Marten Seemann: I don't quite understand how it works in HTTP/3, can we use bidirectional streams in the other direction. Let's discuss later.

Benjamin Schwartz: I think we should start with HTTP/3, will give us the right design, can come back from that to something that will work for TCP. Dispatch-wise, I think we should make a joint-proposal and the HTTP working group is going to have to be involved, but might not be the right home.

Mark: Sounds like needs to be more discussion.

#### [Window Sizing for Zstandard Content Encoding](https://datatracker.ietf.org/doc/draft-jaju-httpbis-zstd-window-size/) - Nidhi Jaju (remote) / [slides](https://httpwg.org/wg-materials/ietf119/zstd-window-size.pdf)

Martin Thomson: I think we should go straight to WGLC for this. It's small, we should just do it. It was just a bug.

Eric Kinnear: I would actually second that; thank you for doing this.  As we look at this, there is no way we could use the current value.  Somewhere in the 4-8 range.

Mark Nottingham:  Sounds like we know what we need to do next then.


#### [Best Practices for Link-Local Connectivity in URI-Based Protocols](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-link-local-uri-bcp/) - David Schinazi

Toerless Eckert: Thank you for the work, I'm all for users shouldn't have to know about IPv6 addresses. That's why an IPv6 network administrator is paid. Needs to work when DNS isn't using. People use browsers because there isn't anything else. I don't think we should retire previous doc, we should add something new and better for users. Browsers don't always support .local mDNS, we should make that mandatory, but that might not be for the IETF to do. When it comes to where 6874 is relevant, yes network operators, and also in APIs or people who use REST content and other forms of URLs. It would be lovely to figure out if there is any particular/better way to fix the origin problem for zone identifiers, in whatwg there is already work there. These shouldn't be used by users.

Stuart Cheshire: David made a joke about printers camping, that's me at Burning Man, I let people make postcards that they can mail to family and friends. Burning Man and Zip Codes. Back in the day, you could have an embedded webserver on your printer and any platform could connect to the printer over the network and see ink levels, etc. This seems natural and good, I don't want to have an app for each device in my home, I'd like to have one: a browser. I can type 192.168.x.x and it works, but it didn't work when I tried to do it via v6. I asked browser people to support it, but they said that's a nice idea and now % is weird, is there an RFC to do some of this, can we match other people? I said, that should be easy. I didn't like % escaping the %, but we don't always get what we want. So now we have an RFC, we made an RFC, and then the browser people said no. I don't understand what's going on here, I just want to check the ink levels on my printer. I am learning more about the enormous complexity inside a browser. David has proposed a really good idea which is to use .local multicast DNS. I would hesitate to propose that myself because that seems a bit self serving, but after 10 years of trying to push this rock uphill, I would say okay that would be fine. I want to use a browser in my home to communicate with devices as easily as something on the other side of the planet. 

Ted Hardie: From a dispatch point of view, needs a BoF or a short WG. People use specific syntax, for network management and in other context, you can't deprecate it. Identifying when you can/cannot use it, needs a real document. Needs some actual work to say "in this particular context, this is no longer permitted" to basically align the WHATWG URL spec with ours and have an applicability statement. You have to balance the use cases, some of them are outside of this working group. 

Ben Schwartz: Want to solve this, excited to see energy, I think this draft is super insecure, tons of exploits waiting to happen, less secure than insecure HTTP, very scary, I want to solve it. I want to live in a world where I can scan a QR code off of an IoT device and securely connect to it. I want a no-garbage domain name for a thing on my network. I think it's within our capabilities.

Bob Hinden: To reiterate, I think there's a real need for this, we're also seeing it in IPv6 environments where there is no v4, there is very little user interface. There is a real user need for this, we lived for a long time because things could fall back to v4, but that's changing quickly. Don't care how this is solved, but need a solution. 

Mark: We're seeing good convergence on solving the user facing problem here, but the solution is to realize that it's not just an address on the network, but is identity on the rest of the browser and that loops in tons more stuff. Agree with Ted, something else needed here. 

Martin Dürst: I think there are quite a lot of user problems that should be solved, but in Yokohama in a closed meeting with Bob and ... others, the fact that you can configure an IPv4 router with a browser is not something the browser people did because they thought it was a good thing, it was just something that router people discovered that you could do with a browser and they did it, so it works, but the browser ecosystem isn't keen on these "special" use cases that cause them a lot of special considerations and so-on. That's a point that's very important that the IPv6 people should understand.








