HTTP WG IETF 93 Meeting Minutes

[ wseltzer is your etherpad scribe. please help correct! ]

mnot: Agenda bashing: https://tools.ietf.org/wg/httpbis/agenda?item=agenda-93-httpbis.html

### Specification Status

mnot: Tunnel-protocol in RFC editor queue.
client-initiated content encoding submitted to IESG

Julian Reschke: Authentication-info header field. Obsoletes RFC 2617 in combination with BAsic and Digest specs; depends on PRECIS framework, 

mnot: What do we need to do to obsolete 2617?

Barry: It's already taken care of. The documents flag it, when they're published. Looking at 2 HTTPAUTH WG docs (Basic and Digest)...
[scrolling through document headers]
they say Obsoletes: 2617 (if approved)

### [Alternative Services](https://tools.ietf.org/html/draft-ietf-httpbis-alt-svc)
          Discuss the [issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Aalt-svc) and draft status.
          
mnot: Julian and I worked through issues list yesterday. Work from the bottom up.

## [Alt-Svc alternative cache invalidation #16] (https://github.com/httpwg/http-extensions/issues/16)

Julian: while the use case you mentioned would be handled, not convinced all would be. If we need to group alt-svc so they can be independently refreshed, we might need to think of labels

mnot: e.g. explicit label field in the header for a group. But complex to implement in clients.

Martin Thomson: Rather than identifying the mechanism, identify the source. 

Mike Bishop: That doesn't entirely make sense to me. Any alt-svc can handle itself. Where it came from is the origin or someone authorized to speak for the origin. Need to think more about what we shoudl do for validation. 

mnot: We know we need something, not sure what its shape should be. In the past, we've tended to overdesign. Keep it simple. 

Patrick McManus: Operationally, seems a bit confusing to have two elements from the same origin, different sources

Martin: Propose a single global scope for a given origin. Whatever you learn next replaces what you have. Keeps things simple, but means you might not get the pinning with respect to H2. You can maintain with a bit more care. 

mnot: if want to use alt-svc for oppsec, then switch to load-balancing... 

Martin: that's why we have @@

Erik Nygren: If you had one global setting, and priorities, then set high priority for oppsec, lower priority, short-lived for load-balancing. Push a whole set. 

Mike: max-age currently applies to the entire entry. If it applied per parameter, 

Bence Beky: might be a need to send a header or frame to clear alt-svcs. While implementing hacks proposed on ML, I found them more complicated 

Julian: According to ABNF, max-age is specific to parameters. 

mnot: seems simplest to have one global scope. An empty frame resets. 

Julian: Need to change the syntax to allow an empty alt-svc header. currently does not. 

mnot: Does anyone who thinks we need more capable labeling system want to talk about use cases? Does anyone object to simple global scope? 

[no objections]

Patrick: Not clear that oppsec needs an alternative. 

Erik: Need clear guidance on what ordering to use (priority, shortest lifetime?) 

mnot: when we've discussed in past, inclination to leave it to the client. 

Erik: here, we probably want to make explicit

Martin: if no other preference, lexical ordering

## ALPN identifiers in Alt-Svc #43

mnot: marked as editor-ready. Do we need to discuss? 

## need to define extensibility for alt-svc parameters #69 https://github.com/httpwg/http-extensions/issues/69

mnot: conventional would be to make must-ignore

Julian: still need to define how to add new ones

Erik: define the granularity of what to ignore. 

mnot: proposal to make extensibility work at the attribute level. How do we do mandatory? we don't. 
Do we need an IANA registry for such extensions? One direction could be to establish directory on first need for it. 

Barry: if you think there are likely to be extensions, go ahead and create it now. If not likely, then defer. 

Julian: put it in now. 

Mike: Issue 71, one proposal was to kick that out to extension, so we'd need a registry then. 

mnot: ok, establish registry

## 71. Persistence of alternates across network changes alt-svc design

mnot: it would be nice to have an option to say whether alt-svc should be flushed. Do we need to define that extension now, or defer? 

Erik: worthwhile to put it in from the beginning. 

mnot: any objections?

[no objections]

mnot: add a parameter to do this now. 

## 73 Alt-Svc: Elevation of privilege alt-svc design

mnot: we currently allow someone to advertise alternative on same origin without strongly authenticating. Designed for oppsec so you don't need a valid cert. Is this reasonable? 
one suggestion, disallow advertising port higher than privileged ports if origin is on privileged port; 

Martin: Another potential attack if you have untrusted actor on your host. if you have cluster, id one node on the cluster, someone can target all the traffic to one node as DDOS
I don't like the segregation on 1024, but might be ok
alternative, if you see alt-svc frame, you might ignore header, on the ground that server is capbable of sending frame. header less trusted.

mnot: should we treat localhost specially? ongoing discussion in webappsec about mixed content in local host. 

Martin: I might open that issue. 

Patrick: I don't have a lot of faith in the 1024, but don't storngly object. 
Another issue I've heard, when changing hosts, verifying certs, right mechanism is CORS, and this violates CORS. 

mnot: I'd like to hear more, because that's a very differnt layer

Patrick: DNS rebinding attacks can do the same.

mnot: not CORS, but something the server can do to indicate it's used as alternative 

Mike: see oppsec discussion

mnot: we're really just talking about http urls. 

Mike: for http, I really don't want to let you move me to a different port without HTTPS, but might be ok

mnot: you can alwasy ignore the advertisement

Martin: What level of advice do we think is appropriate? Do we outline the potential use? 

Erik: What about being fairly vague in alt-svc, more specific in oppsec?

mnot: still put info about privileged ports here?

Erik: certainly in oppsec.

Martin: We might describe the risks. 

mnot: describe the risks and recommend a privilege barrier

## 74 Alt-Svc: Alternates of alternates

mnot: is everyone comfortable with what's in the issue as "second reading"?  Yes.

## 75 Alt-Svc header with 421 status alt-svc design

Mike: asking you to reverse the text in 421

Patrick: it should be flipped to must not

mnot: must be ignored. 
An alt-svc header in a 421 must be ignored. 

## Alt-Svc and Cert Pinning #76

mnot [reads]
spec currently reads must be valid, but not necessarily identical credentials. 

Mike: starting from HTTP means there are attacks that will work against you. 

mnot: oppsec is not proof against active attackers in any way. if we start trying to plug holes, we'll never stop. 

Mike: but here, you're making the attack worse, because you could redirect wth host, have a long-lived alt-svc

Martin: we also have guidance about clearing state between networks, particularly for unsecured origins. If you're mitmd once due to cert compromise, high chance in the browser that that can be persisted already. 
if you can get something in browser cache, storage, service workers...

mnot: oppsec provides no secuirty indicators to user. 

Martin: we can talk about concerns, don't need to change the design

Mike: can live with it

Erik: oppsec can't send to a different hostname

mnot: so even for https origin, we're rooting our trust in the certificate. a bad cert could persist. 
Need to add security considerations and possible mitigations. 

## 83 Alt-Svc Header - hop by hop

mnot: any proxy in the way is going to strip it. 

Martin: Thumbs down. Patrick: nod. 

Martin: I like that you can push this all the way through a proxy. Not consistency for consistency's sake. 

mnot: close with no action. 

## 87 alt-svc response header field in HTTP/2 frame 

Martin: only reason to treat differently if ability to write to header field is less privileged than ability to write to frame. 

mnot: there may be circumstances where it's intreesting to put it into header. 

mnot: no special handling

## 89 Using alt-svc on localhost

mnot: do we know enough now?

Martin: treat public address-space -> private or into localhost as privilege escalation. Recommend ignoring the alternative that appears

mnot: rough-in some text, discuss with browser security folks. 

mnot: through with alt-svc issues. lots of work for the editors 

### [Opportunistic Security](https://tools.ietf.org/html/draft-ietf-httpbis-http2-encryption)

mnot: checkpoint. We've only had one browser implementation. TAG F2F and WebAppSec discussions of things that look like oppsec. Have another good look once alt-svc settles down. 
not inclined to publish right away. 

Martin: some uncertainty in community what the right strategy is here. Upgrade Insecure from WebAppSec, akin to HSTS. 
original vision for oppsec was to try to move cleartext http closer to https
other changes could let us avoid that. Doesn't address the landing page issue, where you start from HTTP

mnot: other issues, hard to get certs for some people; hard to transition from http to https on some websites. W3C efforts to make that easier

Erik: IPv4 space issues and SNI. We're not yet at the SNI adoption point where everyone can use v4 HTTPS without IP address. 
tradeoff 

Patrick: lots of parallel paths. I think we all want to wind up at full HTTPS. 
other issues: 3d party content; hosting providers' models; corp behind the firewall. 
I believe there's medium-term value here. Don't want to put oppsec on back burner forever. 

### [451](https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status)
          Discuss the [issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3A451) and draft status.
          
## 80 distinguishing intermediaries from origins. 

mnot: some people have said that's interesting. poll on mailing list said yes, it's useful to make machine-readable. If we're going to differentiate, how? 
header? status code? 

mnot: my inclination would be to use a different status code. not a lot of feedback about whether it's done right. Headers, more likely to make errors. 
lots easier to change one digit in-flight in a status code than to change a header. 

Martin: it won't be anywhere near as cool

mnot: if the web is going to HTTPS, then one would think intermediaries have less opportunity to add legal restriction codes

Wendy Seltzer: As a researcher, I think it will be interesting to get differentiated information; don't have a strong feeling which mode. 

mnot: ok, taking back to list. 

### Potential Work
## Search method

Julian: common webdev question: why can't I use a payload with GET? 
[reading slides] (https://httpwg.github.io/wg-materials/ietf93/ietf-93-httpbis-search.pdf)

Phil Hunt. I was one of those trying to use GET. I had a draft that was uglier than necessary because it couldn't use SEARCH, dealing with stored results. 
https://tools.ietf.org/html/draft-hunt-scim-search-00

mnot: safe POST, or use to store search? 

Phil: POST to store the search query, SEARCH to execute. Query itself becomes a restful object. 
stateful results are useful. 

Martin: Stored queries. I'm not worried about that. We frequently log GET requests and do all sorts of "non safe" things on the server. Channeling Roy, the client is not responsible for its side effects on the server. 

mnot: why not just use POST? 

Julian: leave the stored query stuff out of the spec. SEARCH is GET with a body [meme alert]

mnot: think I'm ok with that.

Phil: if you look at SCIM, @@

PUT v SEARCH?

mnot: I'd be concerned that if this gets implemented in browser, we lose a lot of cache efficiency on the web. 

Julian: if we do this, explain why it's almost always better to use GET
SEARCH RFC is experimental, I'm the author, so we should be able to relax payload to make it more generic. 

mnot: my inclination is to call for adoption. any more discussion? 
Call for adoption on the list. 

## New content-codings. 
New content-codings - [Presentation](https://docs.google.com/presentation/d/1rncpm-SRSzVv86lHQipGHi0TXwjoDycXkLGhkwUwB4c/edit#slide=id.p)

Martin: give people a sense how all these things fit together. 
[reviewing slides]

### Remaining items on the [watchlist](https://github.com/httpwg/wiki/wiki/WatchList)
mnot: Julian wants to wait for new RFC format for non-ascii for @@
Encrypted content encoding, client hints
inclined to call for adoption on client hints.

Martin: some extensive security review, getting it into WG would help on feedback. 

mnot: I'd explicitly reach out to Security Area. 
weak interest in Patch status 
there's a repo with an issues list for HTTP/1.1
Strong feelings on any of these docs? 

[cookies!]









