# HTTP Working Group Minutes - IETF 117

## Wednesday, 26 July 2023


### Chair Slides & Agenda Bashing

Chairs - Mark Nottingham (mnot) and Tommy Pauly (TP)

Notetaker - Jonathan Hoyland (JGH)


### Resumable Uploads - Jonathan Flat (JF) (on behalf of Guoye)

#### Upload Complete

- some thumbs up.

#### Header versioning

Kazuho Oku (KO) - If this is an issue I prefer having a suffix like `Upload Complete-v3`

Martin Thomson - I wouldn't worry about this at all. We changed stuff on previous slides, but that was a complete header change. We could spend a ton of time engineering this, and I don't think it's worth the effort. 

#### Byte Range Patch 

Watson Ladd (WL) - That's a different case. This is a single file, and the server only wants to see it when it's done. We shouldn't rely on this change in semantics.

JF - We only want to support it in pending.

Julian Reschke (JR) in chat: PATCH needs a media type irregardless of byte-range

Austin Wright (AW) - Other WG should be able to pass byte range patch pretty quickly. This allows for the server to receive packets out of order, and fix corrupted messages. 
We could say "we are sending 500 bytes" and the server would know it's done when it's received them. One of the bases of byte range patch was to support this.

JF - Yeah ...

Guoye Zhang - We changing the syntax of the content range header. If we drop it the current replacement storage is not

Tommy Jensen (TJ) - If we're still supporting `Upload-Complete` for header discoverey now there are two ways to express where we're uploading to, and I don't like ambiguity.

Erik Nygren - Lots of implementation ambiguity and bug potential. Think about how this interacts with intermediaries 

Marius Kleidl (MK) - We can just take the parts of content range that we want.

JR - The semantics of HTTP PATCH require us to have a media type, even if it's as simple as application/append, we will still need to define that type.

#### Upload Progress

TJ - Active disinterest given the expericeces with incompatibility with 100 responses

Hans Jorg Happel - I would generally be in favour of something like that. 

KO - In general servers can send any 100 at any time, so prohibiting this seems awkward

MK - We can reuse 104 or pick a new 100 response code.

JF - How much should be included in the draft? 

Take it to the list

#### Fetch API proposal from WHATWG

No queue

#### Other Open Issues

No queue

### Templated Connect-TCP - Ben Schwartz (BS)

MT - We're not talking TCP Fast Open 

BS - That's orthoganal

MT - False Start is a bad term pick a new one

DS - TLS also has False Start

Mike Bishop (MB) - The H/3 spec had to have additional language around Connect saying it's weird and you have to process the headers and then process the body after the tunnel connects

KO - What about connection recovery in H/1.1?

BS - Next slide

TP - IN Connct UDP Masque stuff it's talking about the client sending it optimistically, so you can talk about optimistically sending the body data.

BS - I'll update the i-d to match the MASQUE terminology.

MT - This is really bad (false start vs connection recovery) the server doesn't know if the server is waiting or not. When we're talking H/1.1 so the client sends the request to the the server and the server reqects it, but the clietn got positive affirmation before it was rejected.
Not good to just [not do this] because then you don't get to do the optimistic sending.
If this is the way people expect H11 to work then 9298 hos a bug. Probably shoudl'n thave allowed optimistic sending.

BS: If you look at the H22 folw here then there is no connect requests and wit han upgrate token that's uncerocgnised then the server is in H11 land whenre it's supposedly allowed to reject the upgrade and keep the socket open.
We need to be aware of rejest smuggling.

MT: We need to update some RFCs because they contradict each other in awys that cause security problems.

David Schinazi (DS): Editor of the documemnt. Possible to support datagram capsules. Not aware of anywane using connec UP over H/1 or planning for that, so does this atack matter? This attack where you have capsules that spell HTTP things, clever , but assumes evil clietn. 

BS: Presumes you have an evil traffic source beding your client.

BS: Capule type 20559 were common then this creates a security issue.

BS : Prevent capsule type with confusable meanings should be unregisterable. 

DS: Too farfetched for us to worry about. 

Lucas Pardue: Job security enthusiast. You haven't caused the problem but you've pulled the covers off something gross, and that's a shame but we need to fix this stuff especially the 1.1. It won't happen but it can.

WL: We had a similar issue with NPT where existed uses squatting over a whole bunch of fielsd that were suppost te dbe gree. It was bad. 

KO: I'd prefer just banning this behavour [...]

Alex Chernyakhovsky (AC) - I think we are crossing the threshould were contiuning to invest in new performance features like this in H1 is a waste of time. Just say H2+ only

BS: Not an optimisation, just correctness. We need to cater to proxies that speak H/1 on the backend.


### Unprompted Authentication - David Schinazi

TP - Authour of PrivacyPass auth scheme - would like to see alignment. We did bas64 in quotes. That's what it had to be because it could start with a number.

DS - Can the token start with a number

mnot - Yes, HTTP token

TP - You have to allow the equal to be there. 

mnot - Not proposal one

MT - I don't want to talk about it. You fix it. I want to talk about the previous thing. [cryto stuff] This is parallel invention of an existing feature in TLS. This is EAs all over again, but not as well. Let's use them instead.

DS - Those had a layer of complexity that's more than this.

MB - +1 MT. Modulo question of TLS stack support for this. The complexity comes from the certificate request context, which doesn't exist here. The other thing is it has toe represtable as something in TLS.

NS - Ditto. Is EA. Defineable context isn't necessary. Including the stuff in the exporter makes it implicit. Generally speaking this is effectively the same. 

JGH - ...

KN - If EAs are too complex we can do token binding instead. We can change it from negotiated.

TP - I'll have to reread the EA stuff. We might just need to reopen that. Certificate Frame stuff is coming back up on thursday. Reconsider in the case of 

CW: We implemented this, unless you can get HTTP access to the TLS layer it's really hard. Do we need to bind to the TLS layer.

DS: Freshness

JGH: Yes, for security. 

--
CW: Document assumptions about registration. Happy with whatever.

MT: Important that client and server agree on the public key being used. Fix it in the protocols.

DJ: With EAs you get this for free

JGH: Not free you have to send it explicitly.

DJ: "free"

### Structured Field Values Bis - Mark Nottingham

MT: The deault is pick up a library to do something that's 2 lines of code. I don't want a dependency on the 3986 spec. Just pick uupercase or loweraces. Just go with it that way. 

mnot: Did I hear you volunteer to revise the ROI spec in the middle of that?

Chris Lemmons (CL): People are gonna use existing libraries. Asking for an extra call to Lcase or Ucase at the end. ???

KO: This isn't a critical concern. 

MT: There are perf implications for having to process both upper and normal case. All field names are lowercase now. 

TP - Cost is equivalent to fix in parsing.

MT: I suggested language - cite RFC 4648 and in there it's upper case. Someone else flipped a coin previously, no sense reflipping it. 

JR - I still don't get why we have a problem with Authentictaion. The only thing we can say that will always work is this is a string. There's no extension point there. It's fixed.

mnot: I know you believe that tokens are strings are interchangeable in HTTP. I'm not convicende that people and use paramaters understand that. 
Some of the lock in and say this has to be one or the other.

TP - We had this issue in PrivacyPass, and we had to go through all implementations and check they supported both.

MT: JR is saying that the mapping is necessarily complete.  No extension to Authz  ... we'll be sure that it cannot fit within the mapping that exsts. Do we expect to have an espcaep valve whereby you have the non-map version. Availbale in a certain conetit. 

mnot: The fpilosapy is that yeah, if you use this spec you have to be able to fall back for at thealst the compabible fields.

MT: If fallbacks exist then we don't have a requirement to curtail. Otheriwse it's a bit weird to define a strafromation but then go and apply contraints that the transform is possible. I'd rather avoid. 

mnot: So we don't need a hard requirement.

mnot: We have folks stuffing binary stuff in there so ...

MT: I don't know how someone presented with a string can decide if it's bytes or strings.

mnot: To make this work you need a pair of new fields. 

MT: To make it interoperable yeah. 

###  QUERY Method

JR: no progress, but likely progress before IETF 118.


## Other Topics
---

### Alt-Svc update - Mike Bishop

MB: We would like to see implementation and trying out of what we've written so far. 

### WebSockets Design Team Report - Lucas Pardue

KO: In priority 1 do you mean that there is already an existing HTTP connection, or strating from nothing?

LP: A bit of both. Depending on what the client might already have open.

MT: In other contexts we've reached the conclusion that DNS is good at hints, but not establishing context.

LP: Yeah, this is all about hinting. The ultimate response is the response code you get back.

AC: I don't think DNS is the right way to do this. What about adding another field to the TLS handshake where we declare all the features that apply at once. Similar to ALPN.

BS: I think the right solution is an RFC that says HTTP is version independent because the idea that you have certain services that only exist in certain HTTP versions. If you're not in that state it's a transient failure which we can tolerate, but the correct solution is to get out that state.

DB: +1 BS. ALPN is the only thing that will solve H/1 / H/2 thing. We don't want DNS to be able to downgrade HTTP version. Proposed solution is going to add not remove problems.

WL: This is the same as trying to advertise H3 or H2

Eric Kinnear: By the time your selecting H2 or H3 it's already a bit late. People are getting this wrong today. We should look at data about how often we get this wrong. 

LP: For me point 2 is answered. A second design team wouldn't be able to do better. For point 1 I think that's a clear no. 



## Thursday, 27 July 2023
---

### Chair Slides & Agenda Bashing

Chairs - Mark Nottingham (mnot) and Tommy Pauly (TP)

Notetakers - Ankshit Jain, Travis Langston

Possibly bash in talk from last time that wasn't reached.

### Secondary Certificate Authentication of HTTP Servers - Eric Gorbaty

Eric Gorbaty (EG) (Presenter) 

Jonathan Hoyland (JH): Asks if server also needs to send an origin frame.

EG: Server expects the Origin frame. Will be included. 

JH: Either include origin frame or IP/DNS check

Mike Bishop (MB): Technically maybe not. Probably want something to get around DNS check. Updated drafts of HTTP says authority is established by the certificate,  browser's choice to decide how to trust.

MN: Reminder time constrained, talking about adoption here so don't go too deep into details. 

JH: Wants to get this working for clients, so there's interest in client and server stuff. Agrees about keeping scope simple. Wants to adopt this, but only if we can do client side as well. 

Alessandro Ghedini (AG): Interested last time. Cloudflare implemented, no one used it, still interested and have new masque use case now. 

MB: Adopted secondary certs, do we need to adopt it again?

MN: Want to see significant interest from the group before trying again.

Watson Ladd (WL): Good idea, let's move it forward. 

Lucas Pardue (LP): Supports it.

MN: There was this level of interest before, but if failed, didn't get implementation, especially from clients.

JH: Previous draft had interest from server side, need interest from browser side. 

Chairs: Show of hands - 20 in favor, 4 not in favor. Asking for feedback from people not in support of adoption. 

Martin Thomson (MT): Didn't go either way. Want to spend more time clarifying what the use cases are, more discussion of that - current discussion was more in details. 

### Compression Dictionary Transport - Patrick Meenan

Patrick Meenan (PM) (Presenter), asking for adoption

MN: Discussed before, there were reservations before, asking for feedback from the group.

MT: Looks like good work. Supportive of finding out how well it works with developers, delta thing seems easy to integrate into various workflows. Doesn't really want pattern matching in the stack, but can talk about that in terms of details once we get into discussions in the working group. No objection to moving this in here. 

PM: Doing trial is so we can shut it down, get rid of anything that existed in case it didn't work.

Alan Frindell (AF): Colleague Felix supports it. 

AG: Also interested in adopting, have done some work in the past in this general area, but like MT said, need to figure out some, but probably a good place to start.

LP: Following the work before, separation of what to include in the group and what not to include is good. Some thorny edge cases to consider, reservations about spec. 

PM: Few items are browser specific, didn't feel appropriate to include in here.

MN: Seems like found a way to unblock concerns. 

PM: Privacy and security reviews haven't crapped on it yet, a first. Pattern matching - have seen cases where version of resources are in middle of path, main dots at end, so needed at least a wildcard in the middle.

Chairs: Show of hands - 27 in favor, none not in favor. Take it to list, call for adoption.

### HTTP Availability Hints - Mark Nottingham

MN: Presenting. Had on agenda last time, ran out of time. Looking for adoption. Fairly important problem to solve, Vary is awful, but is this an interesting approach?

AG: Problem exists, and should be solved, question is how. Doesn't know if this is right solution, can try, see what happens. 

Chris Lemmons (CL): Important and good to solve. Solutions seems marginally better than previous iterations. Probably technically possible to implement, a good thing. Interested in seeing where this goes.

Mike Bishop (MB): Same opinion as CL. 

MN: Feeling isn't different from those expressed. Wants to try, not confident it'll turn out great.

Chairs: Take it to list. Show of hands - 20 in favor, 1 not in favor

MT: Not very happy with idea that we keep swinging and missing on this one. Would like to see more evidence that this one is going to work. Pretty lukewarm response here. 

MN: Agrees that response was lukewarm, but momentum can help gather evidence, adoption is one way to do that. 

MT: Clear signal from browser or client of some sort.

MN: Cache, not a client. 

MT: Lot of caches here, didn't hear much from them, or from client side caching. 

MN: Not 2 swings and misses, more like took 2 swings and learned. 

MT: Want more enthusiasm, that's all.

TP: Asking for implementation support, anyone interested in experimenting. 3 people in the group are interested.

MN: Cloudflare cache team is interested in the implementation. Most optimistic thing is this is in same state that early hints was in when Kazuho first talked about it. 

### HTTP Cache Groups / An HTTP Cache Invalidation API - Mark Nottingham

MN: Presenting. Looking for adoption. Have talked to number of CDN teams, they are interested. CMS are very interested, but not sure if CDN will support. 

LP: Clarify the proposals. Is this not 2 different things?

MN: This is 3 different things.

LP: Too many things going on, has opinions on all of them, not sure what's being asked.

MN: Idea of CDN and reverse proxy interested. 

LP: Last thing is good and separable from other stuff. 

CL: Number 2 - very interested, but not entirely clear where that API is supposed to be, is there expectation that it's supposed to be on every cache, centralized system for collection of intermediaries? 3 - also interesting, not sure but looks very similar to work coming out of CDNI working group. Goals may be sufficiently distinct. 

Rich Salz (RS): Interesting. 2 - is most interesting (invalidation API), can adapt in front of existing APIs. Others are fine as well.

MB: Echo it sounds interesting, will probably need customers to ask for this before implementation happens. Sees last one as config file telling you where to find common elements you expect from each CDN, the more common CDN things that have already been defined, the more valuable it is. 

MN: Agrees, other purpose of config file is that they can differ across CDNs. Asking for Fastly folks for feedback. 

Piotr Sikora (PS): Cache tax thing is fine, interesting, should be adopted. Second and third is almost like out of bound API, not sure if should be in HTTP WG. 

Erik Nygren (EN): Intriguing. Need customer demand. Mapping concepts on multiple large systems, similar on surface level but details will be very different fundamentally. Complexity will be passed to the edge, could become lot harder than it seems. 

MN: Agrees it could become harder, but need to try. 

Marco Munizaga (MM): As an individual and user of CDNs, thinks it seems great.

### Request-OTR Header - Shivan Sahib

Shivan Sahib (SS) Presenting, asking if interest from WG, and if this is right place for this. 

Dennis Jackson (DJ): Interesting. Concern is that it is not as effective as Private Browsing, and users could think this is actually secure, while local history could save it. Any way to avoid telling user about this, avoid confusion? Otherwise have complicated user education issue. Concerned that this is pitched as privacy measure, that's not effective and might be actively harmful.

Ryan Globus (RG): Great idea, additional tool to private browsing. Could be helpful for other apps (like email) going to browser. Excited about it

Watson Ladd: Why does it need to be a HTTP header vs meta tag?

SS: Could do both. 

MN: Interesting idea, issues are around privacy and browser integration. Header is something that anyone can create so it's important for the group. WebAppSec seems like you'll have more people in room who have spent more time thinking about this.  

MT: Privacy CG chair at W3C - can probably take this.




