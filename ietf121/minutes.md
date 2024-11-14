# HTTP Working Group Minutes - IETF 121


## Monday, 4 November 2024

_09:30 - 11:30	Monday Session I - Wicklow Hall 1_

### Active Drafts


#### [Resumable Uploads](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload) -- Marius Kleidl

- Marius Kleidl: Updated all implementations to the latest draft during the hackathon, tested interop, lots of green checkmarks, nice. All clients and servers interoped well.

- Mark Nottingham: I wouldn't want to do more than put text into the draft that highlights potential issues like the one that Go ran into

- David Schinazi: As one of the people who wrote that bug into our QUIC stack some years ago, it's really easy to act on the first headers, when client hints came around we fixed it. A note would be good enough. Looking at interop results, you're in good shape, looks ready to progress to me.

- Bron Gondwana: This looks good to me, go go go, let's get it deployed.

- Yoav Weiss: In the spirit of the Go implementation issues, we recently had some issues with Early Hints where there are web exposed metrics that indicate the first interim response header. It's worthwhile as part of browsers shipping this, we should test that we're reporting the first interim header and not the last interim header, this would be a new concept. I don't know if this requires text in the RFC or is just something for implementers to be aware of. Otherwise excited about this, ship it.

- Guoye Zhang: A late addition to the draft was the OPTIONS header to detect upload limits. Are there any concerns on the server side given that that is a MUST. Can everyone support OPTIONS and OPTIONS*?
- Marius: In my experience, I was able to do it, but I don't have the viewpoint of every implementation. If it's not achievable in practice, we can also turn it into a SHOULD.

- Julian Reschke: Regarding testing multiple 1xx responses, it would be helpful to have a public resource on the web that could exercise that test case for us to point an HTTP client to. That would make it easier to raise bug reports for libraries like... Java. (PS: will update https://github.com/greenbytes/java-http-1xx-tests)
- Marius: Great idea, we have a public demo server for uploads, we could implement something like this.
- Mark: We could probably put something into the cache tests to test all the intermediaries pretty easily, I'll try to 


- Marius: Once we do the editorial pass, is it reasonable to do a WGLC soon? 
- Mark: Sounds like we're getting there. Once people take a look at the revised draft, we'll look at that.

- Darrel Miller: Just curious about client implementations. How many client libraries actually expose 1xx to application developers? Are we hoping that as we implement more of these, that will encourage people, or are there clients out there that already support this. 
- Marius: In my experience, you're in new territory. Most libraries (Go, Node.js), you can fetch intermediate responses, but sometimes it's ugly. On the web, with fetch, this is not possible. I would like to have them exposed there, but I'm not sure if we'll get there. Resumable uploads are usable without them, so you can work around it.

- Lucas Pardue: One question on the 104 status, it's not currently reserved. If we think this is ready for WGLC, but I hear other people talking about wanting a 1xx status code. Is there a way to provisionally reserve that? 
- Mark: There's a process for that in some RFC, we'll work with the AD to do that. I think we're probably ready for that.

- Julian: Regarding fetch API, I recall that we opened a ticket when we did HTTP/2 where we had almost killed the 1xx call. I think there's a ticket open, if it's not open I can open one and we can mention it to Anne. In Java, there's a weird API, but it's possible. Standard Java API clients accept this call in Java 17, but don't expose the contents of the messages. Has open ticket from me to do so.
- Marius: Thanks for the insights, that sounds like what we'll be seeing a lot with intermediate responses.

- David: For early allocation, it looks like you just need WG chair and AD approval.

#### [QUERY Method](https://datatracker.ietf.org/doc/draft-ietf-httpbis-safe-method-w-body) -- Mike Bishop

- [#2896](https://github.com/httpwg/http-extensions/issues/2896) Normalization
- Darrel Miller: I would like to comment on the decision around the syntax of "Accept-Query". Please don't not use structured fields. In HTTPAPI we're telling everybody you have to use SF. Having an exception from this group sets a bad precedent.
- Martin Thomson: I think you probably have an answer to these questions in your mind. Those are the right answers, just go ahead and do those things and we'll Last Call it once it's done. I'd like to see this wrap up, the things I've seen going on the issues list are very sensible. +1 to Darrel as well.
- Mike: I will go and do as I see fit then, thank you.

#### [Cache Groups](https://datatracker.ietf.org/doc/draft-ietf-httpbis-cache-groups/) -- Mark Nottingham

- Mark Nottingham: There are some textual changes to make that will make the spec more clear. I don't see anything that's a showstopper. If anyone else has comments, now's the time, Last Call is about done. If folks want to express support or lack thereof, that would be good. Unfortunately, we have uneven participation from cache vendors, I think those teams are often busy with other things. If you know someone working on an HTTP cache, please solicit opinions from them as these specifications go by.
- Kazuho Oku: What I've heard from my colleagues is that this looks good and can be implemented. Not sure if they will, but I've heard that it looks good.


### Other Topics

#### [Incremental HTTP Messages](https://datatracker.ietf.org/doc/draft-kazuho-httpbis-incremental-http/) -- Kazuho Oku

- Ted Hardie: I'm very much in favor of this approach, but I think you might want to consider if there's a third state. Two states: Fail and warn. In the signal, you can say "hey, if this doesn't work, I want you to fail" vs. "I want you to warn me if it didn't work". There are cases where incremental delivery is desirable, but not fully required. In general, I think this is a great idea.

- Yaroslav Rosomakho: It's a real issue in multiple environments. Most intermediaries do some kind of buffering, preventing incremental things, not because they're evil, just because they're doing important work. Instead of erroring out, it might be worth signalling back to the initiator "no, sorry, I can't do that" and let the initiator figure out what they want to do again. Instead of doing two flags, can we have the signal saying "no" and then let the originator.

- Alan Frindell: We stopped buffering any kind of post bodies a decade ago because it wasn't scalable for us. There are some things that come from that, you can't let intermedaries try again for you when upstream goes away, you have to fail all the way back to the client. We use double GOAWAY (warning goaway) to make sure there are no in-flight requests and then we send the real GOAWAY once we're sure. Big fan of the work.

- Alessandro Ghedini: We do this piecemeal, mostly when a customer complains. We do have cases where we want to disable buffering for normal browser traffic. I don't think browsers are going to set this parameter. Are there other ways to signal the incremental 

- Tommy Pauly: As coauthor and as individual. This signal is sent on both request and response. Independent signal from sender through intermediary. Need to think about a server sending it, they won't get the status code rejection. Soft vs. hard failure: Would that only apply to one direction, are there considerations for the other direction. If we assume that the client is able to do it in one direction, does the intermediary get to reject it in the other direction from the server.
- Kazuho: We do have freedom of choosing which design we like. We started with bidirectional, changed to attaching it to each message so request/response have different signals. As Tommy pointed out, the response cannot be seen by the server. I think Lucas and <...> had a proposal to send a signal to the server.
- Mark: There are a lot of aspects that need digging into. A lot of the devices that cause problems are virus scanners and other endpoints on path, and they may not engage here. Maybe we should invert to complement client -> intermediary. We've talked about this a number of times over the years. Every time it comes up, we decide not to do it because we can't make it perfect and solve every case. Maybe it's worth trying and seeing how far we get. Would be worth trying to engage those parties that are otherwise reluctant. Hearing lots of enthuaism. 
- Martin: I think reciprocal case is useful to explore. Browsers probably won't set this, we don't care about incremental delivery of uploads, those tend to be small. I think there's a use case for the reciprocal coming back, there are cases where that would improve page load performance. e.g. CSS is all in one job, but other types resources like HTML can benefit. Our performance people would be interested. Not sure what that does to intermediaries who expected this to just be for some niche use cases.


#### [The HTTP Wrap Up Capsule](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-wrap-up/) -- Lucas Pardue

(Not the last presentation)

- Alan Frindell: Supportive of this work, have not read recent version of draft, but probably ready for adoption. I think it's useful. Some ideas of what we can do with this on the client side.

- Mike Bishop: Also supportive. I think it serves a good use case. It's a GOAWAY on the inner connection that the intermediary doesn't have access to send. It can relay it to one of the endpoints that does have access to send that GOAWAY.

- Yaroslav: Very supportive of this work, I think it's a big missing piece. Would ask to consider two use cases: One when you're having maintenance and you'd like client to retry as transparently to the user as possible. Second when you're shutting things down and you don't want the client to try again. Don't want to overcomplicate things, but having a retry bit as a payload wouldn't hurt. Even without that, this is a super useful addition. 
- Lucas: I have things like what you're saying in mind as use cases, but I think we can iterate, and it's not anything that would need to be fleshed out before this WG picks up the work in my opinion. 

- Kazuho: +1 to adopt, we can decide if we need client generated signals after adopting this.

- David: Before we move on, are you going to start an adoption call? 
- Tommy: Mark and I will talk. It sounds like we have good support, we need to schedule the set of things we might be interested in adopting.

#### [Guidance for HTTP Capsule Protocol Extensibility](https://datatracker.ietf.org/doc/draft-pardue-capsule-ext-guidance/) -- Lucas Pardue

- Tommy Pauly: As individual. Another case in MASQUE, which is using H3 datagrams, we have cases in QUIC aware mode with other capsules and there are error codes of "you mismanaged the connection ID index". The error is vaguely related, but it's not at all an H3 datagram error. I would strongly support having a better one.

- Alessandro: About ignoring capsules, does the behavior change for the capsule itself? Wrap up, ignore it. For other ones, if you're using CONNECT-UDP and you're getting CONNECT-IP related stuff, that seems like a problem. Should each capsule define what to do when that happens.
- Lucas: I can think about 10 different ways to frame this.
- Alessandro: You could have a registry with a column for ignore or error if you don't understand it.
- Lucas: Sounds complicated, but I'm all for being rigid and forceful in these cases.
- Alessandro: I don't know if this has been discussed, a bit orthogonal, but should we be greasing capsules?
- David: We are. Spec for capsules recommends greasing. Chrome will do it for WebTransport for example.

- David: I think this is really important. Some of these we didn't think of. Some of these we were just lazy. Now that we have some experience, I think this is the right time. I don't know that we need a -bis on 9297, but some guidance would be good and I'm fully supportive and happy to help.

- Ted Hardie: I'm a little confused here, I wasn't clear if the "endpoints" here included proxies. 9297 is very clear on this, it says that intermedaries should forward without modification. If you're a proxy that hates progress, then sure you blow it up. From an extensibility perspective, skipping the unknown ones is still what we want. We need to figure out how to tell if the proxy chain is forwarding it unmodified and how to know if the drop point is the end. I wouldn't want a -bis that would change that without further discussion.

- Mike: Echoing what Ted said, I actually don't think this is unclear. There's a difference between unknown capsule that you don't know about vs. a known one that doesn't belong. If unknown, keep going. If known and bad, blow up.

- David: To what Ted said, we were pretty clear about endpoint being intermediary vs. destination, but then is it your HTTP stack vs. CONNECT/MASQUE stack?
- Lucas: Some of this is "HTTP Body" for my code, and folks aren't even aware of what other capabilities they have.
- David: We do it the other way around, we parse the capsules at the bottom since we have varints and I'm lazy.

- Lucas: This is written as a document that updates 9297, no strong opinion between that and a -bis.
- Mark: We'll talk about it.

#### Cookie eviction -- Yoav Weiss _remote_

- Neil Jenkins: Usually when you end up in this situation, you just want to get rid of them because something got messed up. I agree with the approach there. Underscore host hack for security sensitive cookies, everything else _shrug_, seems fine.

- Yaroslav: Current method of setting a cookie with an expiry date in the past is an afterthought, but it works. For the foreseeable future, implementers will need to do both, since there's no way to signal if you support this delete cookie feature. Not entirely sure if that's worth it, given that there is a mechanism that works today.
- Yoav: That works today if you have the domain and path. If we always had that, I agree it wouldn't be worth it. In many cases, we don't have it. I'm starting to see people encoding the domain and path into the cookie in various ways in order to have that information.
- Neil: That's a really troubled moment we've gotten into in the past, there's no way to get that information in the past. It's just impossible to remove it, you have to find the magic sequence of how you set it to be able to remove it, and the client won't tell you.

- Martin: Question is what to do with the work, seems like we have a cookie revision coming up, that seems like the right place to fold this in. I think this is great, it's the right shape, we don't need to do anything fancy here.
- Mark: In the last round, we're a little more formal around taking on new functionality. We need a draft and to do a call for adoption, and you need consensus to adopt before we'll put it in.
- Martin: That's reasonable to do, but I would suggest that this is in scope. As Neil points out, this is just annoying.

- Mark: Do you have a sense of urgency? Are you going to try to prototype?
- Yoav: I think this is pretty simple in terms of definition. I suspect it's not super hard in terms of implementation. I guess the main sense of urgency is if we want to get it into -bis. I can move on getting an I-D put together for this rather quickly if that works for folks. I don't know what the timelines for that to get adopted are, what would that look like? 
- Tommy: To clarify, we have a current -bis document that's leaving the WG and headed to the IESG. It would not be in that, but directly on its heels, we expect to adopt another -bisbis of that, and we'd want to include in that. Ideally, we don't leave that one open for quite as long. Hopefully, not a big delay. That said, we do want to get some implementation and experimentation experience.
- Yoav: That sounds great.


## Thursday, 7 November 2024

_17:30 - 18:30	Thursday Session IV - Liffey Hall 2_

Meetecho - [full client](https://meetings.conf.meetecho.com/ietf121/?session=33412) / [onsite](https://meetings.conf.meetecho.com/onsite121/?session=33412)


### AD-Requested Feedback

* [https://datatracker.ietf.org/doc/draft-ietf-netconf-http-client-server/](draft-ietf-netconf-http-client-server)

- Darrel Miller: .net, go, java APIs don't have these kinds of configuration options for used HTTP version.  Instead they have policies. Concerned that if people try to implement this in apps it will be difficult.  

- David Schinazi: Agree with Darrell.  Don't seem to be useful. goes against how HTTP works.  Should remove this configuration "knob".

- Mark Nottingham: Is more discussion needed with authors? (positive feedback from audience)

- Tommy: Handled as part of TLS negotiation.  No reason to require this.

- Darrell: services currently dont support h3.  If something wants multiplexing it should have h2.  Asking client developers to make decisions they don't need to make.

- Mike Bishop: Agree with comments on version selection. Questions usefulness of client config. Server configuration makes sense.

- Mark: This community has worked to keep HTTP semantics independent of HTTP version, and provided negotiation mechanisms to handle this.

- Lars Eggert: Many areas of IETF don't have the flexibility to negotiate versions whereas HTTP does.  HTTP doesn't need this.  People love knobs.  

- Mark: are you willing to have further conversations with authors? (positive feedback)


### Active Drafts


#### Template-Driven CONNECT for TCP](https://datatracker.ietf.org/doc/draft-ietf-httpbis-connect-tcp/) -- Ben Schwartz _remote_ ([slides](template-driven-connect.pdf))

David Schinazi: We already live in a world where we already need more than a URI. You need a separate part of your config, such as how to configure a proxy. We already have a solution for. Recommendation: whatever mechanism you use to configure your client with a proxy should include the upgrade tokens.  We should have 2 upgrade tokens, and clients or servers can choose what they implement. No "MUST implement"

Kazuho Oku: Mostly agree with David. We have 3 options including "legacy CONNECT" Wondering if people are interested in implementing 'connect-tcp'

Tommy Pauly: Agree its vague what connect-tcp means. Recommend it's always the capsule.  Puts it on par with other token based protocols. If you want no capsule, just use legacy CONNECT. This removes one of the variables

Lucas Pardue: Dont like that the server says you have to do 2 things. Want to chose whatever to do. Propose use a different protocol thing as a compromise.  As a server provider, don't want to have to support both.

Mike Bishop: Shares previous opinions.  If we know we need capsules, then lets just have capsules.  Lets go all the way and use capsules.

Mirja Kühlewind: In this design you already have 2 things (protocol and capsule-protocol fields).  If you take

Ben: That's from the capsule protocol, outside of this draft.

David Schinazi: "that's fair" emoji.  Strongly agree with ben here, but that wasn't the consensus of masque wg group at the time.  Since it was optional, we can't depend on it.

Mark: Seems like we need more discussion.

Ben: mostly likely way forward is to consolidate on a single protocol. 

Mark: I see thumbs up in the room.

#### [Security Considerations for Optimistic Use of HTTP Upgrade](https://datatracker.ietf.org/doc/draft-ietf-httpbis-optimistic-upgrade/) -- Ben Schwartz _remote_ ([slides](optimistic.pdf))

Ben: Feedback? I'm not aware of other necessary changes.

Eric Kinnear: comment on closing the connection. better if we have to do something else from security POV

Ben: clarify? is this about 407?

Eric: I'm going to reject your connect and also close everything.  Proxy authentication is degraded by this. An actual HTTP connect proxy.  Implementation impairment.  Many failure mode variants, difficult for client to understand what is really happening.

Ben:  Interesting to hear this.

Eric: We see this problems for other proxy flows as well. Good to avoid this here.

Ben: How about a request header to signal a well behaving client? (laughing audience)

Tommy Pauly: Notable new text requires some nit.  This doc is focused on advice for http/1.1.  We should be specific that this is HTTP/1.1 focused.

Mark: if you are placing RFC2119 requirements, do you also need to update RFC9110

Ben: interesting question! Not sure where we go from here.  Eric, if you have suggestions on changes to this section, that would be great.

Mark: feels like we're getting close to last-call, folks should review.

#### [No-Vary-Search](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/) -- Jeremy Roman

Mark Nottingham: The efficiency mechanism reminds me of the key header.  Cache implementers (non-browsers) need to think about this and bring anything back to the group. This is in-band now. Need time for them to digest that.

Valentin Goșu: Thank you for working on this. +1 on considerations for efficient implementations. If web sites and browser implementers don't agree this won't  help improve cache hit rate.    Thankful it is not a regex.  I think this is good.

Darrel Miller: feedback from non-browser user on naming: "search" is odd. what about another word?

Jeremy: We had other name "no-vary" at the beginning and got feedback that "search" is ok.

Mark: In this area, terminology is inconsistent across across the ecosystem.  When talking about naming, defer to editors.  AI generated pictures of bikesheds is unhelpful. :)

Mark: making good progress here

Phillip Hallam-Baker: "search" is a relic from the past

### Other Topics

#### [The IP Geolocation HTTP Client Hint](https://datatracker.ietf.org/doc/draft-pauly-httpbis-geoip-hint/) -- Ciara McMullin

Ted Hardie: appreciates the privacy focus. There has been previous work on GEOPRIV with no implementations. idea is that in addition to having the location, you have somebody who cares about the revelation of their location the idea of a maker is kind of central to that.
Once you create a header like this, there is no guarantee that people will use it.  Since many VPNs are designed to hide location, this could compromise that.

Other approach: geo feed from client. reduces number of IP addresses in IP pool, which is good.

Suspect there are others things that will be surfaced as we move forward.  Rather than adopt this, adopt a requirements process for how we do geolocation using HTTP while maintaining privacy.  

Mark: This is the beginning of a conversation to determine if we want to talk about this more.

Stephen Farrel: First, user intended, confusion of those kinds of phrases will make the conversation harder.  Second, I agree with Ted.  going through use cases and requirements is helpful before we do anything.  Maybe doing nothing is the right idea.

Kyle Nekritz: Clarify intent? reduce size of IP pool? 

Ciara: mask client IP with proxy, but pool size is not priority

Tommy: goal is to slowly wean the ecosystem off IP based geolocation.

Philip Hallam Baker: I am happy to control this as a user. Setting my preferred location is good. That header will be abused by users to see stuff they shouldn't

Yaroslv Rosomakho: There is another significant challenge which is the question of trust between proxy and destination service.  Very few destinations trust headers that proxies use to expose origin IP. We should discuss how intermediaries can sign those headers so that origin servers can trust it.

Eric Kinnear: are we in place to have separate signals for IP address and location? Today we have both. Can we make them separate?

Piotr Sikora: as a server I cannot trust this. with MASQUE can this leak the IP address?how does this work with MASQUE?

Ben Schwartz: The elephant in the room is ma  proxy server operators that will customize your location header for a free.  Proxy operators come to IETF to bypass the geolocation database providers. 

Lucas Pardue: difficult to solve, but this is good to solve

Eric Nygren: This is an important topic.  Its not just the cost of the geo providers.  IPv4 addresses is small.  Privacy proxies to convey this  In some cases trust is not necessary such as weather.  In other cases like content providers, trust is required.

Shivan Sahib: we were forced to ship client intents. We don't want to be forced again

Scott Hendrickson: We intentionally do not address the problem of trust in this draft. Most proxies do not allow to change location today. We should not address geo hopping here.

Mark: Interest in the room discussing this further. Further discussion in the future. No decision yet.
