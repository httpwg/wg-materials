# HTTP Working Group Minutes- IETF 98

## Friday, 31 March 2017

### Status

* draft-ietf-httpbis-rfc5987bis-05 in RFC Editor queue
* draft-ietf-httpbis-http2-encryption-11 also in RFC Editor queue

### Active Drafts (12 minutes each)

#### [RFC6265bis: Cookies](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis)

Mike West: 3 drafts adopted.

Drafts are tested in implementations:
    

    * [Cookie Prefixes](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-prefixes):

    * Shipped in Chrome 51 (May, 2016) and Firefox 50 (November, 2016)
    * Google see some usage of these new cookies
        * 0.004% of `Set-Cookie` headers Chrome sees are using `__Host-` (seen by 1.08% of users)
        * 0.00001% using `__Secure-` (0.03% of users)

* [Strict `secure`](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-alone): Ramped up to 100% in Chrome 56 (January), Firefox 52 (March)
Impact to developers low enough compared to benefits. Not too many bugs reports.
The web-view developers are however also noting this change, they have more expectations on stability. 

#### [Same-site cookies](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site): Chrome 51. 0.01% of usage.

Expect to update the RFC in April.

Issue list not huge. Issues seen in Chrome seem pretty straightforward.

Jim Roskind: stats in number of users. Number given regarding 'set-cookies'. Could get numbers on users, but not easy.

#### [Early Hints](https://tools.ietf.org/html/draft-ietf-httpbis-early-hints)

Kazuho

Mechanism for the server to notify to client what headers are expected to look like in the final response.

Two changes.
    
Security considerations about cross-origin information leak. If client doesn't recognize 1xx response and connects through a forward proxy. Non-issue for HTTPS and for HTTP/2.

Mike Bishop: would apply to client doing pipelining?
K: would affect both.
Mike Bishop: would apply for pipelining without a forward proxy
Roy Fielding: Already a concern as 1xx codes can be extended by anyone. Thus this could happen in other cases also. 

When to apply 103 headers. Part of the informational response itself, as well as (speculative) part of final response. RFC 7231: MAY ignore unexpected 1xx responses.
Two options:
    - Leave it a MAY or be explicit
Current solution: be explicit to have a well-defined behaviour.

Roy Fielding: Some problem with wording, as it can be interpreted as one do not parse the headers. Will send to mail list.. 

Patrick: good idea to be explicit.

Patrick: no open issue in github.

Kahuzo: once 'when to apply' issue is solve, could move to LC.

Roy: could move to LC anyway.

Martin: tweak this, and ship the draft.


#### [Expect-CT](https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct) ([presentation](https://docs.google.com/presentation/d/1JXtSTPbb_ydyVeBnoD2xVooJzAiKGURzInCxqhKZXAY/edit#slide=id.p))

Emily Stark

Expect-CT: response header to allow sites to opt in to Certificate Transparency enforcement and/or reporting

Implementation underway in Chrome.

Blockers from TRANS WG

- Need to settle architecture questions for CT
- Plan for distributing log metadata, for server to know when to update regarding CTs.

Richard Barnes: Expectation out of TRANS may be to big. Unlikely to result in an consistent policy. 

Emily: Don't have such strong expectation. Want to have something for shipping in Chrome.
    
Patrick: issues?

Emily: mostly editorial issues.

Set content-type header when sending reports.

Patrick: how do you see next steps?

Emily: maybe TRANS will settle in the next few weeks. Possibly go to LC in Prague

Martin: don't put expectation in work of TRANS. Once TRANS done, Emily should tell WG and see how it works.

Emily: implementation for LC?

Patrick: has Julian done a review?

Emily: Commented on an issue.

Roy: uses Cookie syntax, which is bad. Copy any other headers. Will file issue.

Roy: still don't understand why it is not an option on certificates.

Emily: this is not something to keep forever. Hope to remove this header in a few years, when browser have a direct support for CT.

Roy: don't think it is a good idea to deploy header fields for a limited time.

Martin: regarding syntax should use header structure draft.

Suboh Iyengar: Maybe adding a header from clients to inform server that they are enforcing  CT ?, Will file issue 
    
Julian Reschke: I don't think expect-ct actually uses cookie syntax

#### [Header Common Structure](https://tools.ietf.org/html/draft-ietf-httpbis-header-structure)

Patrick: in fairly early stage. Poul is editing it but has limited time to do it.

Patrick: should discuss about it. Whether this work is valuable?

Martin: raised an issue: what's the posture regarding repeated parameter names. Issue was closed without discussion.

Mnot: intend to make pull requests on this spec.

Patrick: recuring problem. Show of hands for having read draft: 6 people.

#### [Immutable Responses](https://tools.ietf.org/html/draft-ietf-httpbis-immutable) ([presentation](immutable.pdf))

Patrick: need document to update list of cache-control values. But this document is pretty straightforward.

Proposal: LC ready.

Number of thumb-ups.

#### [Cache Digests for HTTP/2](https://tools.ietf.org/html/draft-ietf-httpbis-cache-digest)

Kazuho:
    
Two new issues.

##### Issue #264 Overhead in cache digest algorithm:
    
- Dedupe URLs before hashing
- Change from SHA256(url) to SHA256(path). Path is shorter. But caches cannot reusue SHA256(url) they might already use.

Mike Bishop: don't know what our key are.

##### Issue #268 Enabling O(1) removal from digest

- Reduce cost of building/maintaining Cache Digests
- Using Cuckoo filters in place of Golomb-coded sets
- Exact encoding or implementation is not available yet.

Stefan Eissing: are browser interested in this?

Patrick: Good to get feedback on implementation status and who. 

Kazuho: server-side in Node.js, client-side service-worker.
Should have an apendix on how cache-digest should be encoded as HTTP header.

Patrick: what kind of interest got on this work.

Kazuho: browser vendors wondering on whether doing this. Server vendors seem to be more interested.

Stefan: httpd has support, but has not seen any client.

Mike Bishop: interested in it, but don't have time to implement this. Blind push can be a waste of bandwidth.

Patrick: seems #268 will be hard to resolve without running code.

mnot: I’ve had a discussion with one browser engineer who says they might be trying to implement in the (somewhat) near future; that’s not a commitment, however. I think the question is whether we wait for a browser implementation, or ship it as experimental and see.

Martin: how much to expect to learn from 1 person implementing this. #268 could be resolve on paper. Two paths: park it, or publish it as an experimental draft.

EKR: agree. Either park it or decided on one algorithm to run an experiment with. 

#### [The ORIGIN HTTP/2 Frame](https://tools.ietf.org/html/draft-ietf-httpbis-origin-frame)

Erik Nygren: changes since last version.

- Origin frame: incremental.
- Relaxing requirement for HTTPS: can ignore the DNS.
- Security considerations
- Introducing wildcards without following the DNS may be dangerous.

Mnot: parked it. Thing it is ready to unpark.

Mike Bishop: relaxing the DNS portion. HTTP/2 says do check the DNS. Do you intended to update RFC 7540?

EKR: two reasons to check the DNS. Want to know where you're going. For security reasons.

Erik: security aspect and operational aspect. Not following DNS would change many things.

?: Whole point seems to be coasleasing connections.

Patrick: Looked at implementing it and found another experiment on the code point chosen. Issue with reusing? 

Martin: We have holes in the registry, but no problem to pick the next value. 

Mike: about checking the DNS. If multiple host names, multiple IPs that don't overlap. Any of these IPs same server, but different certs. Therefore when using origin, these IPs don't match.

Patrick: privacy aspect on allowing host to replace the DNS.
Origin is not block by secondary certs, but the two go well together.

Nick Sullivan: summarize 3 main benefits
- Use the same connections for servers on same machine SNI or not.
- 
- Not doing the DNS lookup could also provide a performance benefit.

Mike: TLS WG: hum showing interest in ???

Patrick: from implementation side Firefox very interested. At least 4 large servers very interested.

Mike: Additional cert draft requires to check the DNS. If compromised Cert need to convince you to connect on any domain.

Nick Sullivan: secondary certs should also skip DNS.

Kile Nekritz: 
    
Erik: right now, DNS as second factor (maybe weak). If compromised cert, need also to compromise DNS for an effective attack.

EKR: 1st attack factor: compromise CA, can do whatever I want.

Erik: still not convinced that origin frame is safe by itself.

Piotr Sikora: origin could allow to hijack all the trafic.

Mike: If connected to server authoritative for several host names, could use it even if DNS tells otherwise.

Suboh: did the original intent changed?

Patrick: original intent was more complex.

Erik: does seem to have been a change in scope. Probably need a broader security analysis on how coalescing works?

Martin: notion of constraining space and expanding it could be made separate. Concerned by middleboxes on the path that want to use these things. Have full control on where packets end. None options relying on DNS help in these scenarios. Only certs work.

Patrick: never fully worked on security properties of routing.

Nick: secondary certs expand domains, origin frame restricts.

Mike: have ability to connect to a proxy: delegates DNS resolving to the proxy.

Patrick: list discussion for consensus on DNS issue. Will ask document authors to bring those issues on the list.

#### [Random Access and Live Content](https://tools.ietf.org/html/draft-ietf-httpbis-rand-access-live)

Darshak Thakore

Range has limitations. Proposal is sort of a hack, but best one could came to.

Martin: advise not to pick too large numbers. Concerned about overflow while server is parsing.

Patrick: no issues. Need more information from WG?

Darshak: feedback from WG would be good. Will update a few things.

Martin: open issues for those things. Once resolved, ask for LC.

Patrick: reviews: Martin, Hanes?, Mark.

Darshak: marked as experimental. Link from 7233?

Martin: would be more confortable once has been tested on the web. Hit some reseanable number of sites to check on server support. Check that results are not really bad, in which case Proposed Standard would be fine. Otherwise can only publish an experimental doc.

### QUIC Working Group Collaboration

#### 25 min - Mike Bishop -- [Update on the mapping of HTTP/2 and QUIC]
(https://www.ietf.org/proceedings/98/slides/slides-98-httpbis-quic-00.pdf)

Mike Bishop presenting slides from QUIC WG + QUIC Tutorial.

Settings are unchangeable during the connection

EKR: for changing settings, server need to be able to kill the connection while asking the client to restart.

Mike: harder for the server. Would use GOAWAY in HTTP/2.

EKR: difficult to differentiate close and don't reconnect vs. close and reconnect.

Martin: Proposal was for a flag, I am done and go away

Mike: Aware of one case where settings are used midstream. However, that need will disapear with ?

Martin: do have AltSvc to push someone somewhere else.

HPack replacements

Krasic's proposal: Add some additional to HPACK: can reference things in same packets or known as received. More complicated, but enables code-reuse

Mike Bishop proposal (presentation from QUIC WG [QPACK](https://www.ietf.org/proceedings/98/slides/slides-98-quic-qpack-00.PDF)).

Design issue: how the selected solution for HPACK in QUIC will impact connections?

Need to decide if frame and SETTINGS registries are common between HTTP/2 and QUIC or not.

Mnot: I think that the overlap is at the HTTP semantic layer; frame types, error codes are below that, and using the same registry is going to cause confusion.

Roy: if there are fields values valid in H2 but not QUIC, then have different registries.

Martin: semantic very similar, but with subtle differences.

Mike: HTTP over QUIC, big section on difference of H2 frames in QUIC.

Ben Kadak: If you are going to have the situation that you have similar things but they are subtle different. Then using differnet code point avoids missinterpretation of those subtle differences.

Stefan Eissing: mic: it's usedul to have extensions for one or the other without taking care of both all the time

Martin: agree with that.

Julian Reschke: question reminds me of the common field registry for email and http

EKR: don't want someone defining something for H2 and not being ported to QUIC.

Erik: 2 different WG. New feature would need 2 drafts? Or a single draft would be sufficient?

Gabriel Montenegro: Referencing work around link layers. We had a mental model applied to different use cases. We tried to use the same code point when applicable, but in some cases there where was a requirement to use different code points. 

Jim Roskind: question of re-ordering. Reordering very infrequent thing. Chrome: can show how much reordering occurs to you. It is really something that happens. Some routers are multithreaded.

### Feedback

#### 10 min - Feng Qian -- [Cross Layer Interaction of H2 Connection Management](https://www.ietf.org/proceedings/98/slides/slides-98-httpbis-eng-qian-cross-layer-interaction-of-h2-connection-management-01.pdf)

Feng Qian

Presentation of results from research work.

Problem: a large transfer fills the TCP buffer and blocks a smaller file when using HTTP/2.

Proposal: new frame for migrating a response to a new connection. Includes provisions for ensuring correct ordering of response-bytes sent across the different connections.

Roy: how does the server knows that two connections belong to the same client?

Feng: need some identifier for the client, that is added to the protocol.

Jim Roskind: how do you cause the second connection to arrive at the same machine? Problem is with load balancing. In addition common that second connection has other egress port and will be directed to different machine.

Feng: haven't really considered this.

Piotr Sikora: solution: lowering the TCP buffer, so that the frame can stay in the HTTP server.

Feng: if too small, performance can be affected. Difficult to come with the optimal value for the TCP buffer.

Kazuho: setting TCP buffer to exact size of RTT. 

Feng: difficult to predict the network condition changes to set the right value.

Patrick: this is a hard problem, but not impossible. Survey to find what people are doing in the real?

Feng: want to do some measurements on how servers are behaving. Most important thing is the behaviour of the user.

Mike: both Linux and Windows expose info on how much data is needed by TCP to maintain the link saturated. Would be interested to find what sites take advantage of that.

Feng: did some experimentations and found all servers have this problem to different degrees.

Jim Roskind: this is bufferbloat in the server. Should be addressed at the server level, not at the HTTP level.

Benjamin Schwartz: TCP_NOT_SEND_LO_WHAT? option in TCP. It's recommended in some documentation for implementating HTTP servers.

Piotr Sikora: ???

Kazuho: connection migration has benefits: could migrate one request to a cache.


