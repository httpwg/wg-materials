# HTTP Working Group Minutes - IETF 122

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [18 March 2025](#18-march-2025)
  - [QUERY method](#query-method)
  - [CONNECT-TCP](#connect-tcp)
  - [Security Considerations for Optimistic Protocol Transitions in HTTP/1.1](#security-considerations-for-optimistic-protocol-transitions-in-http11)
  - [Resumable Uploads](#resumable-uploads)
  - [Secondary Certificate Authentication](#secondary-certificate-authentication)
- [21 March 2025](#21-march-2025)
  - [No-Vary-Search](#no-vary-search)
  - [Incremental HTTP Messages](#incremental-http-messages)
    - [#3007, Definition of Incremental Delivery](#3007-definition-of-incremental-delivery)
  - [HTTP Unencoded Digest](#http-unencoded-digest)
  - [Delete-Cookie and _HttpOnly Prefix](#delete-cookie-and-_httponly-prefix)
  - [Cookies: HTTP State Management Mechanism](#cookies-http-state-management-mechanism)
  - [Critical CH and Accept-CH Frame](#critical-ch-and-accept-ch-frame)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 18 March 2025

* Chair present: Tommy Pauly
* Notetaker: Yaroslav Rosomakho

Query method, CONNECT-TCP, optimistic HTTP upgrades, resumable uploads and secondary certificate authentication on the agenda today.

Francesca: Agenda bashing: proposal to discuss cookies draft. Currently stuck in IESG evaluation with a really easy-to-fix DISCUSS. What is the status? It would be great to get an update before Wednesday.

Steven promised to make an update asap.

Mike Bishop is welcomed as a new AD

### QUERY method

Mike Bishop is presenting in person, Julian Reschke remote

Document is considered to be done. Few editorial and minor updates. All non-editorial stuff is resolved. Heading for WGLC soon.

Mike presents open issue #3004: should GET parameters be used for a stored query? Proposal is to spell in the draft not to do that.

Martin Thomson suggests that this is not something that requires special handling. Suggests that query variables in GET request do not really matter for HTTP and whole URL should be considered as an identity of the resource.

Ben Schwartz: Asks if response code should be 200 or 300. Mike confirmed that the 200 is intentional code. Ben asks for consistency of Location header across 200 and 300 response codes. Ben provides an example that redirects do not really work with DoH. He agrees with Martin's interpretation.

Julian Reschke questions interpretation of Location header by the client. Mike's interpretation of Martin's comment is that Location represents a new URI that should be treated as a different resource. Julian agrees, but asks if draft should have some text about it and proposes to think more about this issue. He proposes to clarify query parameters and body in the draft text.

Mike suggests to issue WGLC once this issue is resolved.

Rahul Gupta: has a concerns with limitations of the query format. Mike explains that QUERY follows the same contract as POST method - contents of QUERY (or POST) is not defined by HTTP but is handled by higher level application logic. So one might need to define a media type to signal something more structured.

### CONNECT-TCP

Ben Schwartz is presenting remotely

Ben explains what is CONNECT-TCP (CONNECT method with URI template similar to CONNECT-UDP). Now it is even more similar to CONNECT-UDP as it now requires Capsule protocol very similarly to CONNECT-UDP. That's the only change in the latest draft revision.

Open question (issue #3000) about signaling FIN vs RST. Ben explains the difference between FIN and RST. In HTTP/1.1 FIN vs RST is not specified, but in HTTP/2 this is signaled through Stream closure error. Ben discusses proposals to encode this in CONNECT-TCP. One option is a new Capsule type for graceful closure.

Kazuho Oku: does not think we need a final capsule. The only use case he thinks this is needed if there is some data after the FIN. And he suggests to keep status quo.

Mike Bishop: Supports status quo for H2 and H3. He likes the idea to have an option to transmit data after connection was closed/interrupted. 

Ben asks if this is related to HTTP/3 reliable reset. Mike says that HTTP/3 reliable reset is "stream is aborted but there is still data to be delivered".

David Schinazi: Supports Mike - Capsules are future-proof. There could be use cases to send additional data after the TCP connection is complete - for example a report about quality of the connection. He does not support TCP Flags capsule.

Tommy Pauly: believes that the pattern of data after connection is closed makes sense and was seen in other technologies. But he questions what it means for this draft and if it can be effectively used for those who does not use it yet.

Kazuho Oku: Receiver of final data cannot hold the stream forever. He questions if this creates an attack vector. He thinks we should define details of how and when stream should be closed.

Yaroslav Rosomakho: Supports for closure capsules with auxiliary information and ability to send post-connection metadata after connection was closed.

David Schinazi: does not see security or reliability issue associated with stream lifetime extension.

Mike Bishop, Ben Schwartz and Mike Bishop discuss relationships between reliable reset and final data capsule. Defining this now removes dependency on reliable reset and makes implementations simpler.

Piotr Sikora: current version of the draft suggests to use incomplete capsules to signal reset.
Kazuho Oku: the problem is that when you reset you don't know metadata that you may want to send after reset.

Lucas Pardue has a preference to avoid this for now to avoid additional extension negotiation.

Tommy Pauly asks Ben's opinion on this problem.

Ben thinks that we should set a deadline for the decision and make a consensus call. Tommy highlights that there were no strong opinions on this topic and proposes for Ben to make a decision to crystallize the consensus.

Ben explains that this is not implementable in standard Go as there is no way to signal and propagate a TLS alert. Capsules would potentially solve this.

David Schinazi agrees that sending a broken Capsule to reset stream is not a great option. David believes that we need implementations and get to decisions based on outcomes of implementation efforts.

Tommy confirms that the plan is to discuss this issue for few more weeks and see if we can converge better.

David Schinazi proposes to take discussion to the PR 2939.

### Security Considerations for Optimistic Protocol Transitions in HTTP/1.1

Ben Schwartz is presenting remotely

Previously was limited to Upgrades.

Ben performed a search on Github for ```CONNECT.*HTTP\/1.1``` in Python code and found a bunch of affected clients. First 50 results included 4 clients that assumed success without checking the status code - so this is a real problem.

-07 draft highlights that client must wait for 2xx response before forwarding any TCP payload data. Server ```MAY``` close the connection when rejecting connection attempt to deal with clients not processing response codes.

Ben asks if we should change MAY to MUST or SHOULD. According to Martin MAY is not strong enough language.

Ben proposes a MUST or a SHOULD with additional conditions.

Tommy Jensen: SHOULD is fine. He is also proposing to carve out extension for 407. According to Ben closing connection for 407 is acceptable - client would need to come back with authentication on a new connection.

Martin Thomson: cost could be significant for people who open lots of connection. On another hand a single 407 could help as proxy would learn about required authentication for the whole connection pool.

David Schinazi does not believe that performance considerations are not important for HTTP/1 as people should move to HTTP/2 or HTTP/3 for better performance.

Yaroslav Rosomakho brings up compatibility with broken clients as an argument for SHOULD.
David Schinazi proposes to go with MUST as controlled environments would violate this anyway and we can avoid defining conditions for SHOULD.

David Schinazi and Tommy bring up IESG guidance for SHOULD vs MUST. Tommy proposes to go with MUST.
Ben proposes to launch WGLC soon.

### Resumable Uploads

Marius Kleidl presents remotely

New revision -06 is a major restructured editorial overhaul. Few normative changes: "expires" is now "max-age" to better align with other HTTP work. PATCH responses no longer include Upload-Offset and Upload-Limit but include Upload-Complete.  Added problem type for inconsistent length values. There is minor revision -07 with reference updates and nothing substancial.

There is only one editorial issue open #2962. As there are no comments on mailing list WGLC might be considered soon.

Issue #2964: "Method for appending representation data". Current draft uses PATCH method with "application/partial-upload" media type. Some suggest that POST or PUT would be better methods. Or perhaps a PATCH with different media-type such as "application/append-data" that could be potentially used for other protocols.

Mike Bishop: PUT implies that resource is replaced so it is not a good fit. POST could work. PATCH modifies existing resource so it also fits. He does not care about media type, but believes that second media type is more accurate.

Lucas Pardue: does not believe that there is a good reason to change current approach. He suggests closing this and moving on.

Marius is happy to leave it as is and move on.

Marius presents a table showing how proxies forward 103 or 104 responses from origins. Traffic Server does not forward 103 and breaks 104 response. Caddy does not forward 103/104. Varnish responds with 503 for both 103 and 104.

Martin Thomson highlights that fetch API recognises 103 but not 104. 103 is the only status code in 1xx that can be forwarded.

Marius raised an issue for Fetch but so far no interested implementers.

There are running implementations showing interoperability and suggests moving forward with WGLC.
Tommy suggests to close last remaining issue and move ahead.

Lucas Pardue: this is a mainstream solution that does not break HTTP semantics and suggests to keep going with this proposal.

### Secondary Certificate Authentication

Eric Gorbaty presents in person

There is one non-editorial issue: #2841 support sending exported authenticators in multiple frames over HTTP/2 - if it cannot fit into a single frame.

Maximum frame size might not be enough for a certain large exported authenticators. A number of possible solutions discussed:

o A new stream type
o CONTINUATION
o Specify total size up front
o Possible cert compression

Current proposal is to allow violation of frame size for certificate frames.

Martin Thomson: could we use stream for this?

Eric: this would require a separate certificate stream.

Martin Thomson: we could use a push.

Eric: We could investigate more if its worth adding more complexity.

Martin: key challenge would be to work out stream lifecycle. But streams has all the right properties for it.

Mike Bishop considers what to do in HTTP/3. Violating frame size is not a good option but is unlikely to break library boundaries. This is extension that is negotiated in advance and we could define a specific stream to carry certificates in both HTTP/2 and HTTP/3. He likes the idea of not being protocol specific.

Kazuho Oku: What is expected size of this frame?

Eric: I don't know what the upper bound would be. It worth assuming that it could be large enough in the future so it would be good to have a future-proof solution.

Mike Bishop: ServerHello would be a good benchmark for size.

Lucas Pardue: /breaking up line, could not understand

Eric: will investigate new stream solution before jumping into decision conclusion.

Asking for implementation interest and interop testing.

Tommy asks the room for implementation volunteers. No responses in the room.

Authors would like input from WG on issue #2841. Will take it to the list.


## 21 March 2025

* Chair present: Tommy Pauly
* Notetaker: Nidhi Jaju and Eric Kinnear

### [No-Vary-Search](https://datatracker.ietf.org/doc/draft-ietf-httpbis-no-vary-search/)

Domenic Denicola, presenting remotely

Since last meeting:
- Added an introduction
- New section (Section 7) on how to patch the HTTP caching specification for this feature

No other open issues. 

Implementations so far:
- Prefetch cache in Chrome
- HTTP cache in Chrome
- Google Search server
- Multiple other sites (can look at [chromestatus.com](https://chromestatus.com/metrics/feature/timeline/popularity/4425))

Lucas: Sounds like most of the implementations are from Google?

Domenic: There are two different places in the client where we implement this

Tommy: Which were the non-Google ones? I thought I heard multiple clients, but there aren't multiple browser clients.

Domenic: There are multiple websites, including non-Google ones, sending the header.


Tommy: Anyone who is looking at doing implementation?

Martin Thomson: We are looking at an implementation, would have to go look at where the status is. Generally positive on the idea that this is something that would make caching performance better. The feedback that Domenic was talking about came from us.

Tommy: Is that coming relatively soon? Should we wait until that comes?

MT: I think, no. Because there are not two client cache implementations, they do tend to show a whole bunch of different performance and compatibility constraints. While we've found one issue with the algorithm, I wouldn't be confident until we get further along. We could WGLC this and then park it. The chances of a breaking change seem pretty minimal.

Tommy: As you were mentioning some of the new changes + RFC9111, should we mark this as officially updating that RFC?

Domenic: I don't have strong opinions, so happy to take your guidance.

Tommy: I can file an issue for that and we can discuss on GitHub.

### [Incremental HTTP Messages](https://datatracker.ietf.org/doc/draft-kazuho-httpbis-incremental-http/)

Kazuho Oku, presenting in-person

MT: I share Kazuho's preference here. If request has incremental, intermediary should flip its default if its default is to buffer.

Kazuho: Do you have preferences regarding signalling mechanisms?

MT: No other signalling preferences.

Piotr Sikora: I think there are enough edge cases that we should focus on the initial case, which is a hard-requirement. The preferences I would probably remove from the spec because clients are then micro-managing the buffering behavior of intermedaries. Either they have hard requirement and need it or they shouldn't care.

Tommy Pauly (as individual and co-author): Agree that keeping it simple is good. I think that some fo these complex syntax variants and tri-states are adding complexity that we might not need. Question of framing of hard failing and not is, so 
Also, to Piotr's point, seems fine to define the zero boolean preference.

Kazuho: For hard fail, it's important for certain applications. It's true you might not know who the intermediary is, and in that case we can require. There might be some value in requiring specific behavior for services that actually implement this.

Tommy: That makes sense. I think specifying that a intermediary may reject a request on the basis that it says this wont be incremental

Kazuho: I'm not sure if the people asking for buffer mode actually wants that ahrd fail mode or just the preference.

Tommy: We could say that marking it as zero is the same as not putting in anything at all, but we may s well not.

MT: I think you reached the same conclusion that I have. All of these signalling mechanisms can be added later if we find out that we need them. Re: Oblivious relays, the relay knows that it's a relay and can do the right thing for each case. Kazuho's point that if you understand the application that is traversing the intermediary, you can have a stronger requirement. Otherwise, what we have seems to work for most of those cases.

Piotr: Just to clarify, when we mean 0, incremental should be forbidden not preferred. The point of bringing incremental here was to have it be a generic solution for other use cases as well.

#### [#3007](https://github.com/httpwg/http-extensions/pull/3007), Definition of Incremental Delivery

MT: Another way of thinking of this, these are a minimum, not a maximum. You don't buffer to a given time and given byte limit. If either limit is reached, then you move on. Even a single byte.

Kazuho: Problem with that is Nagle's algorithm, but yes. 

### [HTTP Unencoded Digest](https://datatracker.ietf.org/doc/draft-pardue-httpbis-identity-digest/)

Lucas Pardue, presenting remotely

Lisa Dusseault: Are you going to change the title, if you don't like the name of it?

Lucas: I'm open to suggestions.

Lisa: It's easy to change the draft name.

Lucas: The reason we've change it from an encode from what was unencoded because people are building implementations right now. 

Justin Richer: I just barely understand the difference between Content-Digest and Wrapper-Digest. I'm worried that a third digest header could add more confusion. If the use case is there, then I think it makes sense to do it.
In the picture on the slide, am I the hannibal in this? I'm not sure. 

Lucas: This is only part of the team.

Tommy: Discuss this more on the list.

### [Delete-Cookie](https://datatracker.ietf.org/doc/draft-deletecookie-weiss-http/) and [_HttpOnly Prefix](https://datatracker.ietf.org/doc/draft-httponlyprefix-weiss-http/)

Yoav Weiss, presenting remotely

Tommy: Regarding process stuff, we are not going to update RFC6265bis, unless there's extremely strong indications.
There's another effort to revise that yet again. We haven't done any adoption calls on that, I would advice if the authors and group participants could collectively think those should get folded together, that could essentially be part of one adoption effort.

Johann Hofmann: I can see both proposals being in the new cookies draft. It's important for partitioning cookies, 3P cookie blocking.

MT: This is good work. It would be good to delete the header field, not just individual cookies. I know you don't work for Google anymore, maybe Johann can do that for us and remove cookies from that browser and we'll do the same on our end.

Johann: Yeah that's the next one after that.


### [Cookies: HTTP State Management Mechanism](https://datatracker.ietf.org/doc/draft-annevk-johannhof-httpbis-cookies/)

Johann Hofmann, presenting remotely

Yoav Weiss: Agree that this looks like the right place for my proposals. How do you see that happening? Should I just file PRs against this draft?

Johann: You can probably do that. It's not adopted yet oddicially, so I'm not sure. You need a few bits about properly specifying the bit about partitioning cookie access and then get merged.

Yoav: Makes sense, thanks.

MT: I'm not the chairs, what we've done in the past for cookies since we have to be a bit more careful, run an adoption call for the draft, be happy with it. Once it's adopted, then let that draft die and merge all the contents into the cookie spec. That seems like a good plan here, I'd advocate for the chairs doing that relatively soon.

Tommy: That makes sense, I'll chat with Mark when we'll be able to chat.

Johann: Probably good idea to wait, Yoav. Probably just going to be some number of week or months.

Tommy: Would be good to have PRs ready to go though so people can talk and think about them. It's easy to just push buttons to merge later.

I think the action item is for Mark and I as chairs to go kick things off.

### [Critical CH](https://datatracker.ietf.org/doc/draft-victortan-httpbis-chr-critical-ch/) and [Accept-CH Frame](https://datatracker.ietf.org/doc/draft-victortan-httpbis-chr-accept-ch-frame/)

Victor Tan

Tommy Jensen: I think these are interesting. Far more interesting with the TLS draft in place. My interest is having the correct CH when the clients willing to send them on the very first request. I think having the critical makes sense, and it's a good way to differentiate what is nice to have vs. have to have. But I would really want to see the TLS draft adopted.

MT: There's a high-level question here that has never really been answered in this group. It may not be one that the HTTP WG needs to be answering, but it does need to be answered somewhere. That's the nature of adaptive content and who is responsible for making sure that adaptive content is made available and what the tradeoffs are. CH assumes that the server is responsible for adapting that very first content to something to do with the client, in particular privacy-sensitive aspects of the client. I don't accept that premise. Most of the use cases here boil down to delivering ads more quickly. Most of the Web starts with a request for a webpage, that content is often not adapted based on the client, the content itself has everything you need to change for when there's different browser support, etc. Counter-example, a large image where the device screen size could help, but that's what the picture element does. And the nice thing there is that you can still request something else if you prefer. The privacy properties are much nicer, since you don't have to give the server your pixel ratio. Poor privacy example because the server can kind of figure this out. Do we even think that client hints are a good idea? Some people have accepted that fact, but I haven't yet.

Lucas Pardue: At a high level, I don't know if I have an opinion on client hints. But living in a world where is does already exist, and some people are doing this stuff, I can believe the use case where on the very first visit ever to a website there is an area that people do care about performance of serving the right content in the fastest amount of time. It seems pretty racy and annoying to get right. I don't think it makes sense to do on its own without the TLS stuff. We've discussed this before with H2 server settings and other things too. 

Ted Hardie: I've been talking offline about the geo-IP requirements, but one of the mechanisms for that is using client hints. It's very clear that the use of Geo-IP in many of these cases isn't really aligned with something the client needs, it's aligned with something the server wants. That makes me believe that the point at which you send a client-hint is actually an architectural question about the relationship between the client and the server that is a good bit broader than just how fast can this go? What is the client going to know about what it will get for this private information? Especially for Geo-IP, it is very private information. Moving it earlier, especially into the TLS part of the conversation, is quite worrying, because it is quite identifying and we don't necessarily want to move it into a different layer of the exchange. We want it to be part of the context of the web rather than the security context. Needs a good bit of thought, perhaps reach out to the TAG or other folks who are considering the architecture of the web and have a broader conversation.

Yoav Weiss: I'm somewhat biased here, as I was involved with client hints and the picture element in the past. To respond to MT, I don't think it's either or. Some servers need to do server-side adaptation, while others can use the picture element and that is fine. Similarly, HTML content, some servers choose to adapt their content in order to get that initial HTML as soon as possible and as much of it as possible to the client and there are legit deployment reasons for it. One such reason that is no longer valid, import maps have been fixed, but you have a single shot at getting the right import map to the client, was a blocking asset and you wanted it to be as small as possible and as adapted to the client as possible. No longer relevant since that's been fixed, but there are other reasons you want similar things. I can see that kind of mechanism used for language negotiations, which are currently pretty bad and could be improved. There are real life resons why you would want to adapt your HTML.

Tommy Pauly: I got in the queue as an individual to say I think a lot of the questions Martin was bringing up are interesting and good to address. I think it would help to be very concrete in the use case that we're trying to unlock here and the particular client hints that we're talking about and how that will benefit the user and the client. Framing it like that will help us better understand what are the tradeoffs for privacy and performance, etc. When it's fully in the abstract, we can project different use cases and it's quite broad. That's been the case with client hints from the beginning to a degree. Being able to have that conversation would be really good. Concreteness about the use cases would help motivate group engagement with the discussion.

Will Earp: I have a number of issues with this. There's more data that the browser has to send, which makes the initial payload bigger. The server can just request more data, it can just send an Accept-CH header and request more data back. It doesn't really increase privacy, it reduces it. You have to make an additional request for the critical CH header, so that hurts performance. The idea that we should send specific data that is easier to parse to the server so it can send different content, it shouldn't be doing that anyway. I don't understand why you've frozen the OS version in the UA header because the user-agnet header will still be useful for robots and things like that. A specification for how it should be structured. Parsing is hard because people don't specify it in a format that is unified.

Victor: Currently we don't have any limitation that we can't request the order, so it's still under development. We just need to better control the kind of information that will be provided in the user agent itself.

Will: I agree with the UA freezing part, like you don't need to know the version of the minor version, but major version stays.

Victor: For the major version, we have said that's entropy. Version can be used to identify when you combine it with all the other information. I think we have an explainer for that.

Tommy: Continue discussion on the list, would be great to have further updates on the use cases that we can share with the group.
