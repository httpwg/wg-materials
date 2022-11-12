# HTTP Working Group Minutes - IETF 115

## Monday, 7 November 2022

### [Signatures](https://datatracker.ietf.org/doc/draft-ietf-httpbis-message-signatures) - [slides](signatures.pdf)

Justin Richer (JR): feedback received after WGLC

Lucas Pardue (LP) to provide feedback on digest.

JR: how to treat trailer fields

Mark Nottingham (mnot): In HTTP Semantics (RFC 9110) we recognize that header and trailer fields have different semantics, so we separate them into two namespaces. 

JR: propose "tr" flag

Martin Thomson (MT): You can add tr and req to a field name to identify that it's both a trailer and a request

JR: Are trailers even real?

MT: They are real, but they're not a great thing to be signing

JR: I can't find a good reason to disallow it, so I'd rather define how to do it.

MT: This is the way to break stuff, but that is sometimes what people want.

mnot: The people who like trailers _really_ like trailers.

JR: Collecting implementations, see my presentation to SAAG.

mnot: Is there an appropriate level of review for really critical stuff like this.

(Julian Reschke in chat: there are open issues related to percent-decoding and combined field value generation that still need to be discussed)

### [Alternative Services](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc7838bis) - [slides](alt-svc.pdf)

Mike Bishop (MB) presenting 

Julian Reschke (JRe): Zulip is down

MB: Alt-Svc and HTTPS records don't always align.

Replace Alt-Svc with Alt-SvcB

Benjamin Schwartz (BS): I'm for the SvcB change, what's the issue with stickiness?

MB: "How does the client verify that the cached data is still valid? We want stickiness for endpoints, but not for load-balancing. How do we balance that?"

BS: Reasonable to say AltSvcB is a sticky operator. 

MB: Draft has a flag that says "never use this endpoint unless explicitly told to"

MT: The propsal from the design team is effectively to take this / AltSvcB as the complete replacement for AltSvc, i.e. that we obsolete 7838, we want to say AltSvc is no longer useful.

There are some unreloved issues

HTTPS Records have priority order, which gives you control as to where users end up, but mayb that's not sufficient. So each record has a flag that says "only use this if you were told to"

Interesting suggestion from GH, whcih we will bring to the list.

We want feedback on "AltSvcB solves my usecase" vs "We want AltSvc"

Eric Kinnear (EK): This is useful for us. We strongly prefer getting this infromation from DNS, and we know it before we actually build the connection, which makes a signification and measurable difference in the amount of H3 that we use.

We want both signals

We can consider killing AltSvc separately, but we'd like this.
MB: At 114 we did have some people say they need AltSvc to redirect to H3
David Schinazi (DS): In some platforms we can't get HTTPS / AltSvcB records, so I'd be sad if that went away.

Tommy Pauly (TP): Question for DS: When are we going to update POSIX and `getaddrinfo`? Would it be sufficient on any platform to have a bespoke API for these things.

DS: It's a matter of time, the energy is going on the DNS resolver that ships with Chrome, and the fallback to `getaddrinfo ` is unlikely to get any love. It'll take us a while to get support on all platforms.

LP: As someone responsible for getting to H3 to work, I approve of teh shape of this solution, the GH suggestion is interesting. I don't feel strongly about getting rid of the AltSvc header quickly, adding AltSvcB solves our pain currently.

MT: There is an issue with teh avavilibilyt of HTTPS records, and we get on the order of 2% errors for A / AAAA, but 5% for HTTPS records, and 45% for DNSSEC. This really hinges on how much H3 are you willing to sacrifice on the altar of making progress. Eventually the 2-3% of networks who don't pass on HTTPS records might be small enough that it's acceptable (to kill AltSvc).

### [ORIGIN H3](https://datatracker.ietf.org/doc/draft-ietf-httpbis-origin-h3) - [slides](origin.pdf)
MB presenting

MT: We have mandatory flags, mandatory flags are just called frame types. If you want a mandatory flag define a new frame type. These are problems best solved by future us.

DS: +1 MT. Option 4. Kick the can down the road.

LP: Don't like any of the options. Don't even want to deprecate flags in H2 ORIGIN, if you want 4 frame types, fine. 

MB: Should we do that now or in future.

LP: Without a concrete use case let's punt.

mnot: The outcome is punt the problem.

MB: Reserving extra frame types is slightly worse than sticking in an extra byte.

mnot: Does anyone care about this?

No-one cares

MB: WGLC?

### [Cookies](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis) - [slides](cookies.pdf)

Steven Bingler (SB) presenting

mnot: Do you want to close those three issues, go to WGLC, get this done, and them immediately begin a new revision fixing these 3 issues and the 18 deferred ones?

SB: Yes

DS: The allows a different character encoding for setting cookies vs sending them, is that an issue?

SB: This is an issue because nowadays servers are no longer one entity, and one part may set and another part might not be able to understand them.
We're thinking about how to do expanded character set cookies.

DS: Maybe add a footgun warning in the spec. 

### [Partitioned Cookies](https://datatracker.ietf.org/doc/draft-cutler-httpbis-partitioned-cookies/) - [slides](partitioned-cookies.pdf) _Dylan Cutler_

Dylan Cutler (DC) presenting

mnot: When we talked about getting major changes to 6265bis we had strong concensus requirements. Probably too late for 6265bis, but maybe the next one

MT: Mozilla and the W3C are very keen on this work. We're willing to be guided on timeline by the group. Would advocate for some sort of signal that the IETF process is working on this, but maybe park it so we don't need to block on that work.

mnot: Sounds reasonable. Should we do this at Yokohama or before.

Brian Campbell (BC): What's the rational for providing this at all, vs. letting the browser make its own decisions for partitioning?

DC: Chromes philosophy is to have this be an opt-in behaviour between now and when we turn 3rd party cookies off gives developers an option to migrate to a partitioned cookies world before we just turn everything off.

BC: Is this not a breaking change itself

DC: There is going to be a breaking change in future. This lets servers control their migration timeline.

mnot: There is an explainer, right?

DC: Let's discuss this offline.

MT: This has been debated at length in other forums. The concensus view was that blocking 3rd party cookies in this scenario was the best, but that was not unanimous. Our experience with partitioning is that it almost completely works, so we could do without this, but we were a minority voice. This is the compromise.

mnot: We haven't adopted anything yet, so we can continue discussion.

### [Client Certs](https://datatracker.ietf.org/doc/draft-ietf-httpbis-client-cert-field) - [slides](client-cert.pdf)

Brian Campbell presenting

LP: Most of the issues are really low key. Some editorial.

JGH: How does the Origin check that the terminator has actually seen the client cert.

BC: It doesn't. That's why this is informational. It describes existing practice.

### MASQUE update - [slides](masque.pdf) _David Schinazi_

David Schinazi presenting.

No questions.

### [Unprompted Auth](https://datatracker.ietf.org/doc/draft-schinazi-httpbis-unprompted-auth/)  - [slides](unprompted-auth.pdf) _David Schinazi_

David Schinazi presenting.

MT: It's possible that in certain contexts e.g. web browsers an adversary may be in a position to make requests. This only provents the authenticator from being used on another connection, not prevent reusing the connection.

DS: The attack model there is that the attacker is already inside the browser, which we consider that it's out of scope.

MT: You could bind it to something inside the request e.g. URL.

DS: We can, it's a performance / security trade off.

Alex Chernyakhovsky: This is a connection oriented export, which does weird things to streams, it'd be nice to bind it to the URL.

DS: We can iterate on this.

MB: I do think it's useful. Similar to Exported Authenticators.

DS: Server has to request the client auth.

MB: There are already servers that refuse to admit a resource exists unless you 

BS: I def. want this. I have been involved with a use case that tries to achieve this property. If we assume that there is no indication that a server supports this, which means that it must be configured OOB. Any mechanism could also just have provisioned a symmetric secret. 

DS: This is the general q about symmetric vs asymmetric, but you have to tie the list of origins with the set of keys, which gives you a scaling issue.

BS: I'm not convinced it provides that efficiency. You have to provide the client with O(n) information (i.e. the list of supported hosts).

DS: Depends on the usecase. 

BS: I am telling you, _you_ don't need this. This can be done with bridge authentication. There's a more flexible less complicated use case.

We should solve this.

Kyle Nekritz: What is being done here that couldn't be done with token binding.

DS: More complex machinary, and I don't think it has the property that a client speaks first.

KN: Usually yes, but I think you can omit that. 

DS: From memory, this was complicated in token binding.

mnot: Is there interest in solving this use case

Smattering of hands in the room, several +1s in the chat.

Continue discussion on list.

Meeting closes.

## Friday, 11 November 11 2022

Notetaker: Jonathan Flat

### [Resumable Uploads](https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload) - [slides](resumable-upload.pdf)

Marius Kleidl (MK): Before major issues, talk about example implementation (in chat). Overall, download resumption is standardized, uploads should be resumable, too. There's a few procedures, upload creation, offset retrieving, upload appending and upload deletion. For more info, see the current draft. We're looking for feedback on these major issues.

- Server-generated URL vs client-generated token: (how do we identify the upload?)

Current draft uses the Upload-Token header for client, but we propose using server-generated URLs with 1xx responses (also in 2xx response).

Kazuho Oku (KO): First a question, server-generated URL or token?

MK: Server generated URL would contain some kind of token.

KO: Prefer server-generated token. Should be discussion on how to embed the token, RESTful URL vs in request header field. Not strong opinion

Jonathan Flat (JF): Originally supported client generated token - can send all data on 1st req, fall back if server doesn't support it. Great benefit in still using server-generated urls as long as we have 1xx responses to convey support - definitely support server. Like using Location as provided by server. 

Ted Hardie (TH): A little confused on how this would interact with ETags. If you create with URLs, you interact with ETags.

MK: We haven't considered ETags that much.

TH: New ETag space with each generated URL.

MK: Only one server-generated URL per session.

TH: One server-generated URL is simple, but lose some power of this approach.

Martin Thomson (MT): In response to Ted's question, I lean towards URL, it's generally how we identify things in HTTP. Explains an example. The URL is more of a reference to a transaction in this case. POST is different, you POST to a resource to create another resource. That (transaction) resource has an impact on ETags.

TH: How does this interact with resources where one person POSTs and then many others have access to this resource? 

MT: Don't think question is fundamentally different from scenario where resource is changing. 

JF: Potential for intermittent 1xx responses, progress indicator. Demarcate resources as they're being uploaded. 

Mark Nottingham (MN): Should accomodate lots of different use cases. 

Hans-Jörg Happel (HH): Gut feeling is for server-generated URLs. Parallel uploads could be a use for client-generated tokens.

MK: Something to be considered.

MT: Parallel uploads is orthogonal. Status check gets complicated.

MN: Sounds like general support for server-generated.

MK: Idempotency key issue. Problem is if the client doesn't receive the (1xx) response for the upload creation procedure. Adding idempotency key can mitigate this.

MT: Always a risk when you take a dependency on something. Difficult for a server to guarantee that they respect them. Don't need to solve everything in space of uploads with this draft. 

JF: Idempotency key not necessarily needed. Need to know server supports it anyways. Might be better to standardize if you know a server does support it, take extra round trip. Could be an add on but not necesssarily integral part of protocol. 

KO: Regarding previous issue, people prefer server-generated URLs. Is this very similar to client-generated token? Idempotency keys can collide. 

MN: Agrees - but not too worried about dependency because hopefully Idempotency key spec is finished before this. HTTP extensions like this should be more general, combine extensions in different ways.

MK: Use of prefer header issue. How do we identify that the client is interested in resumable uploads? We potentially suggest using `Prefer: resumable-upload`.

HH: When should this kick in?

MK: Desire to make resumable uploads work for all file sizes. Prefer header - if client indicates file size, server can decide if it's worth creating resumable upload resource - ie file too small. 

JF: Interesting point about overhead of server deciding to support it. Might slow down adoption if server is rejecting requests when client does support it. 

MN: Prefer is loosely specified, not clear what it's for. Tends to be used for things configured by user. Defining protocol extension, giving it its own header might be cleaner. 

Bron Gondwana (BG): Large-file enthusiast. IMAP Literal + or -. This allows the server to give permission to upload based on the size of the object.

JF: Having boundary between large and small sizes can be difficult because of connection speed. 

HH: What's maximum file size that server will accept? No current standard on this.

MK: Expect header.

MN: Expect: 100-continue is still used (unfortunately). I think it's fine, but it will be interesting to see how that interops.

MK: No concerns regarding this.

MK: Open issues. 

HH: Hashes may be handy.

MK: We've considered that out of scope of the draft, but have looked into it at Transloadit.

HH: Could be really helpful.

### [Retrofit Structured Fields](https://datatracker.ietf.org/doc/draft-ietf-httpbis-retrofit)

MN: 4 open issues. -01 takes date type out of retrofit draft.
- algorithm for retrofit parsing

Julian Reschke (JR): I think that the current text has some issues around the parsing algorithm.

MN: We can "monkey patch" it, or actually change the parsing algorithm in structured-fields bis.

JR: Should be in structured fields spec. Want implentations to be consistent. 

MT: Can you talk a little bit more about the rationale?

MN: Mitigate interop issues by having a "compatible mode" flag for structured field parsing.

MT: Probably preferable. Don't see it as two separate algorithms (what you're doing by putting it in retrofit document). This is sort of an editorial choice.

MN: In a way, yeah.

MT: Don't want to complicate it for implementors doing the retrofit, or for first time implementors doing the whole thing.

MN: Algorithm is already pretty complicated. Concerned that might have to duplicate some of algorithms, or add statements like goto step 3 - really ugly.

MT: Leaning towards JR's choice, do it in the spec, with a flag.

Mike Bishop (MB): If a user is parsing using a structured-field library, and the library doesn't support it, bad issues. Spec should require implementations to support the flag.

MN: MB is agreeing. 
- differences in error handling between HTTP and structure field parsing
- add SF-based authorization and WWW-Authenticate headers

MN: Any other feedback?

MN: None, ok.

### [QUERY](https://datatracker.ietf.org/doc/draft-ietf-httpbis-safe-method-w-body)

JR: Open tickets to improve documentation. Discussion about translating query payload to QUERY. A few issues that could be resolved by saying "no we don't do that," or we could take some time to work through them, depends on our energy. The work remaining really varies, I'd like to see people volunteering.

MN: Feedback on this spec? Matter of finding right time where people have bandwidth to work on this.

JR: Need to get digest specs out, resumable uploads. Then we'll have more bandwidth.

Benjamin Schwartz (BS): Why is idempotency key not sufficient? If we have POST with idempotency-key, do we need QUERY?

MN: BS is asking about query method.

JR: Agree there is some overlap here, but not only about making things idempotent - also making things safe. 

BS: Example where that would matter to a party that's not part of a conversation?

JR: Would have to think about that.

MN: Moving on.

### Other Topics

### ORIGIN deployment - [slides](origin-coalescing.pdf) _Sudheesh Singanamalla_

(see slides)

Sudheesh Singanamalla (SS): This work is based on experiences deploying origin frames.

- Walk-through of connection coalescing.
- But what happens for subresources?
- Chrome's Approach: IP addresses for different hostnames must match
- Firefox's Approach: Transitivity between sets of IPs
- Where are the subresources located?
    - 14% of web pages have a dependency on resources from one other AS (autonomous system)
    - More than 50% need no more than 6 AS
- Where are the most coalescable sub-resources?
    - The top 10 ASes handle more than 60% of all web requests for subresources
    - Connection re-use potential can be approximated to number of ASes used
- Challenges with ORIGIN Frames
    - Default ORIGIN Frame allows arbitrary host name from server (no authority)
- Authoritative ORIGIN Frames could preclude DNS
- Modelling: >60% improvement (reduction in median) in number of DNS and TLS connections
- IP coalescing ties services, hard to correlate in real world

MT: Does modelling involve congestion control?

SS: No it is more naive.

- Use of ORIGIN frames makes coalescing practical.
- Takeaway 1: Connection coalescing works in practice!
    - ~50% reduction in number of new connections to the cdnjs hostname we attempted coalescing to
    - Reduced number of connections means more possible clients
- Takeaway 2: ORIGIN frames hav no-worse performance, almost immeasurable improvement
    - Performance cannot be assumed to improve, and should be avoided as primary motivation
- Cloudflare contributes the first public server-side implementation to aid adoption
- Needs careful deployment since non-RFC compliant network stacks exist
- Key motivator are actually privacy improvements
- Other motivator is resource scheduling opportunities at the endpoints

MN: Presentation is relevant to past and current work. 

Bryan Call (BC): On simulated traffic, did you do browser caching?

SS: All measurements were done with no caching, wanted to observe behavior on the network itself. If there's caching, there's no need for coalescing.

BC: Was wondering if you were thinking about page-reloads, cold-cache vs. warm cache.

SS: No, but that's an interesting point.

Piers O'Hanlon (PO): Wondering what breakdown was in terms of protocols used (H2/H3) - can really affect performance. 

SS: Focused only on H2. 

PO: Performance stuff may come not from HOL blocking then, ok.


### ["Modern" HTTP Proxies](https://datatracker.ietf.org/doc/draft-schwartz-modern-http-proxies/) - [slides](modernizing-http-forward-proxies.pdf) _Ben Schwartz_

BS: There's a lot of old ways/methods to proxy over HTTP, but this has some unfortunate properties. You can only have one proxy per origin. To make it worse, virtual hosting of these things are impossible. Starting in H2, there's no equivalent of absolute URI form. Proxy has to know what the actual authority is. CONNECT-* dodged these problems by identifying proxy services by URI templates. We should take that strategy to create a modern version to setup these HTTP proxies - for HTTP request and CONNECT-TCP.

BS: Lots of technical tidbits (see slides). Most important thing is, if you were designing HTTP proxying for HTTP today, how would you do it?

BS: Would like to see this draft adopted. Some question if this could fit in the MASQUE recharter.

MT: I think that a lot of people have varying comfort. TCP CONNECT has interest. Asking a resource for a access point to proxy is interesting. Should probably split HTTP Request Proxy off.

BS: Where should we do it?

MT: Rule out HTTPAPI working group, I think this group could do it, MASQUE could also maybe take it on but decision starts here.

MB: +1 to MT. Like the reworking of CONNECT for TCP, not sold on request proxying. MASQUE sound like they won't put it in scope. I'd like to see the TCP CONNECT work here. Maybe not HTTP request proxy, could use OHAI for that.

BS: Want to come up with a standard for HTTP request proxy.

Eric Orth (EO): Good idea, right working group for it, MASQUE is not. This is a general proxy. MASQUE should avoid being general proxy wg. I don't know if this is enough of a good idea for all the legacy proxies to implement it. I'd like to see more discussion of the use cases. (Beyond "hey everyone write your own stuff").

David Schinazi (DS): +1 to what's said before. Building proxies from scratch at Google. CONNECT TCP sounds interesting, don't have use case for request proxy - and some dangers there, so unbundle. Goal of the new charter at MASQUE is not to become the proxy group. HTTPBIS sounds preferable.

MN: This is probably fine, probably need discussion of the position. Highly doubt legacy will want to switch over. More of alternative for other use cases, so maybe don't call it "Modern HTTP Proxies".

Tommy Pauly: I think we should take it to the list. More clear support for TCP side of things, which I personally agree with. Good to provide a renamed, smaller scope document that we'll take to the list.

BS: Ok will do!

### [HTTP Authentication with SASL](https://datatracker.ietf.org/doc/draft-vanrein-httpauth-sasl/) - [slides](httpauth-sasl.pdf) _Rick van Rein_

(see slides)

Rick van Rein (RR): Would be nice to have stronger and more flexible authentication for RESTful APIs. Many protocols adopt SASL for this flexibility. HTTP authentication used to be an island defining it's own mechanism. Can use Kerberos or OPAQUE in SASL implementation. Want to add an HTTP `User: ` header, akin to `Host: `. `User:` is a further refinement. HTTP-SASL adds cryptographic agility, which is useful for quantum relief, etc. HTTP-SASL built for Apache, Nginx, Firefox. Would like this group to adopt this SASL proposal. Questions?

MN: Thoughts about doing this in HTTPBIS, implementation interest?

JH: Isn't SASL a security thing, and HTTP is a general area?

MN: Answer has varied in the past. 

RR: Send here by dispatch group.

MT: Probably the right place to talk about this. Integration into HTTP probably the most interesting part. Can't answer implementor interest. Can broswer APIs do this in user-space instead of webpage?

RR: We do that in the extension.

MT: Does that require priveleged access to contents of requests/responses? Or can you just use the fetch API? Is it possible to build right in the webpage?

RR: Would not work for automation/RESTful APIs.

MT: If it's possible to drive in self-service fashion, you can demonstrate utility. Implementing this is browser is a challenge since you need to do work here, in the browsers, in fetch. If you can do that on top, it's better to show implementor interest and utility.

RR: We can do that.

Alexey Melnikov (AM): Is access to WWW-Authenticate a priveleged access?

MN: I believe so.

MT: Not certain, I think there's priv info that browswers will put in certain contexts. I'm not certain if js can set the values if you know them. Generally you do a request to the browser to access it's store of the credentials. This puts a contraint on the fetch API. It may be possible to set the values explicitly, but don't quote me on that.

MN: Browsers are one interesting party, another are libraries like curl. I think this is a continuing discussion. Tommy and I will chat, we'll continue the discussion on list. We'll figure out next steps, and if we want to write a draft.

TP: I agree with your summary.

