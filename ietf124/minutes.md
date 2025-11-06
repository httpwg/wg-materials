# HTTP Working Group Agenda - IETF 124

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [connect-tcp](#connect-tcp)
- [Resumable Uploads for HTTP](#resumable-uploads-for-http)
  - [3270 - retrieving lost responses after completed upload](#3270---retrieving-lost-responses-after-completed-upload)
  - [3214 - GET requests to upload resource](#3214---get-requests-to-upload-resource)
  - [3317 - Forward offset jumps](#3317---forward-offset-jumps)
  - [3193 - Request size granularity](#3193---request-size-granularity)
- [HTTP Unencoded Digest](#http-unencoded-digest)
- [Secondary Certificate Authentication of HTTP Servers](#secondary-certificate-authentication-of-http-servers)
  - [2841  - Support sending Exported Authenticators in multiple frames over HTTP/2](#2841----support-sending-exported-authenticators-in-multiple-frames-over-http2)
- [Cookies: HTTP State Management Mechanism](#cookies-http-state-management-mechanism)
- [Detecting Outdated Proxy Configuration - Yaroslav Rosomakho](#detecting-outdated-proxy-configuration---yaroslav-rosomakho)
- [Unbound DATA Frames in HTTP/3 - Yaroslav Rosomakho](#unbound-data-frames-in-http3---yaroslav-rosomakho)
- [HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding - Erik Nygren](#http11-request-smuggling-defense-using-cryptographic-message-binding---erik-nygren)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



## connect-tcp

Slides: To be provided!

BenS:
* This is the last open PR: https://github.com/httpwg/http-extensions/pull/3141
* It's been batted around for a while! There are some marked approvals. There are some additional concerns raised too.

TommyP: Anybody else with input?

AlanF: Are there a lot of protocols that people are running over tcp-connect that are relying on half-close? How critical is it to get perfect.

BenS: It's not and that's why it's a SHOULD. But, it's valuable to define how to do it right.

AlanF: At least the TLS stack I have worked with have limited support.

BenS: In /2 & /3, it's not controversial. It's also not always implementable.

TommyP (individual): In the /2 & /3, you're following what connect does. Can we just lean on what is or not say for /1? Does it need to be any better?

Bens: Gateways often end up doing version translation. So ... we need it to make sure the /2 and /3 translations work.

TommyP: You might already have this problem now.

BenS: My understanding is that http connect is defined in http semantics and in the /2 and /3 RFCs. There is no specification in /1.1 for shutdown and half-close.

TommyP (Chair): More eyes needed. Who is willing Kazuho, Alan, and one more.

## Resumable Uploads for HTTP

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-resumable-uploads-00)

Issues follow:

### 3270 - retrieving lost responses after completed upload

AlanF: I'm curious when the server that has a lot of secondary servers needs to cache.
Marius: Will be routed to which ever server has the upload info. Make it as small as possible.

Alessandro Ghedinhi: Cache maybe is not the right word. Maybe just say the server should resend the final response if the client asks for it - instead of talking about caching.

Marius: App can cache or regenerate

Austin: Every would like to solve this problem, but it's the same class of problems as a POST for a flight. Could just do POSTS requests.

BenS: Some funny about doing this with a zero length hash.  It's like unix touch command. If the upload is considered complete arguable any PATCH should fail - what does a zero length hash do to the metadata. I wouldn't want to jump to the first solution.

Marius: Zero length hash - response mirrors request.

BenS: Doesn't sound like PATCH anymore.

Kazuho: No strong feeling. If we need a generic solution, we decided not to make a generic upload scheme ..

MikeB (individual): For the question of a generic solution for POST. Isn't this a generic solution for POST? Server could just send you and interim response that says "you can come back later" (and creates the resource). This could just say I know the upload is small, but the processing is going to take 3m.

Marius: Need to brainstorm some more.

### 3214 - GET requests to upload resource

Crickets: ...

Marius: We will just continue.

### 3317 - Forward offset jumps

MikeB (individual): I would reframe this where the case is sending a hash and then it gets filled in because it also has access. The client already uploaded those bytes so we think of them as out of band or distributed client then this becomes simple. I don't think we should forbid this but how you do a distributed client out of scope for this draft.

LucasP: There's talk in the chat about concurrent uploads. But, we need to accept reality is that weird stuff is going to happen - clients have to deal with something. We can make the right wording with re-evaluating our choice of keeping this simple.

### 3193 - Request size granularity

LucasP: To be clear this is effectively a new feature request! Still working through issues of the starting point of the design. This is interesting but we could punt if we needed to.  My feeling is we could wait on this.

Austin: ? Maybe could support punting?

## HTTP Unencoded Digest

LucasP: No slides, no open issues. He's ready!

Chairs: Show of hands - nobody read it yet.  Who will read it shortly - many more hands.

## Secondary Certificate Authentication of HTTP Servers

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-secondary-certificate-authentication-of-http-servers-00)

### 2841  - Support sending Exported Authenticators in multiple frames over HTTP/2

EricG: Can we just close this?

Alessandro Ghedinhi: Just close it!

CoryB (/2 apologist): Just close it!

Chairs: Close out issue, do editorial pass, new version, and then start WGLC.

## Cookies: HTTP State Management Mechanism

MikeB (AD): Approved by IESG 6 months ago, but neededa couple of updates before it could go to RFC editor. Updates are in progress and it should go to RFC editor in another week or so. RFC before end of year / new year.

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-origin-bound-cookies-00)

DavidB: This is great we should do this! This fixes one of the original sins of the cookies header. We could use this for HSTS.

ChrisL: I share the enthusiasm. I really wish had of done it this way the first time!


## Detecting Outdated Proxy Configuration - Yaroslav Rosomakho

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-detecting-outdated-proxy-configuration-00)

MarkN (individual): My initial reaction is that Proxy-Status is about any kind of proxy. Should be intermediary status. What you're talking about the state of the client - might not be right place to put it. Maybe do your own header.

TommyP (individual): There are lots of Proxy-Status uses ... and it could fit in there so it depends potentially on how the parameter is phrased.  If it's saying you're stale then it seems like a new header. Worthwhile problem to solve.

BenS: The interesting question to me is are there open deployments that need this? Do we need a standard? We are talking aobut some pretty specific control plane stuff that's not normally done in the protocol.

YaroslavR: There is a need for multi-vendor.

JimT: Definitely need this! We got lots of use cases. Client fetch PAC files too often.

MarkN: This feels like the Link header discussions we had. If it's distinct protocol then use a new header. Shouldn't be scared of new headers now that we have structured fields.

MarkN: This is a little bit niche, but they are still part of the architecture. Willing to do an adoption call (chairs will talk).

## Unbound DATA Frames in HTTP/3 - Yaroslav Rosomakho

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-unbound-data-frames-in-http3-00)

CoryB: I'm sympathetic to this use case. It does feel like another step for HTTP becoming a general purpose transport. Not sure I am entirely convinced about this, but am willing to be.

BenS: Fun problem to think about. If we can come up with a solution great, but I'm not sure I like this solution. You need to future out if you need trailers early and most don't know. This proposal would only be used for this particular use case. Trailers for GPRC streaming applications so it couldn't use it.  If you really need this - use web-transport because it's there! See my alternative proposal on the list.

Alessandro Ghedinhi: Not against it and I get where you're coming from. But, it looks like more complexity to me.

AlanF: I think this is fine.

Kazuho: Not sure if we have enough information. This seems like a PUSH mechanism. One of the reason we need to have this is that the draft is a generic extension to HTTP. Maybe it should be reframes to be about dealign with settings - becomes specific to connect.

CoryB: Can't work in /2. Liked the idea of linking it to connect.

## HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding - Erik Nygren

[Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-http-request-smuggling-defenses-00)

CoryB: This is probably worth picking up.  Need to consider some datacenter centric problems.

ErikN: For service meshes we should try to solve.

Kazuho: I don't need an exporter we only need a hash chain. This is only hop-by-hop. We should try to do the right thing.

ErikN: 1st part: Can't just be hash, you need key and we get that from the exporter. 2nd part: we are stuck so :shrug:.

Alessandro Ghedinhi: This is a problem worth thinking about.

BenS: Not sure this approach is going to be fruitful. Would be in favor of stronger guidance to stop smuggling.

AlanF: This is a problem and it's real. I would like to see this go forward.

MarkN: Let's keep the discussion going because there does seem to be interest.

BenS: On the backend use case specifically, there one (missed it) that are suprt niche.

ErikN: Might be worth splitting it up in to two parts ...

AlanF: What I like about the idea is that there is /2 and /1 and /1 with no connection pooling.



MarkN (no hat): we sometimes hold a side event called the "http workshop" - one is scheduled for before Vienna. httpworkshop.org