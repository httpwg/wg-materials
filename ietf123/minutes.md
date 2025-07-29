# Wednesday, 23 July 2025

Note takers: Eric Rosenberg

## Rechartering

No objections. Will continue discussion with AD to take further steps.

## Cookies - Anne van Kesteren

Brief recap. Soliciting suggestions. No questions or comments.

## QUERY - Julian Reschke

- Define what the selected representation is for QUERY

    - Mike Bishop: also a question about what a conditional request means for QUERY. With GET, you retrieve object and then apply the conditions. With POST, you apply the conditions before you do the operations at all. Real question is: which of those modes do we expect?
    - Julian R: I think the concept of identify the URL of a resource where you can just continue the query with GEt, if that happens and we should encourage that all these open issues go away. That means conditionals, frame requests...
    - Martin Thomson: The model is GET, not POST. If you model payload of query as giving your path to a specific URL that you don't know yet, and you're GETing with a URL you don't know about because you have this huge query, then that sort of lays you very naturally to the conclusion that this is just GET...
    - Mike B: 9110 specializes GET in a number of cases. Saying this has the same behavior as GET, requires updating 9110. Updating is undesirable.
    - Julian R: ...., don't want to update the base spec either
    - Mark N: current definition of selected representation accommodates this. ...
    - Martin T: If there are cases in 9110 that need to be updated, we shouldn't shy away from that
    - Mark N: 9110 was written in a way that there would only ever be a single GET-like method which we are now violating.
    - Julian R: like suggestion from Martin that this is modeled closer to GET... Treat selected representation as GET with a body. Would this help with caching question?
    - Mark N: my recollection of discussion with Roy is that he backed away from his position a little bit. Cites Roy's GH comment on "QUERY: HTTPDIR/RF review - Caching".
    - Mike B: if you need to cache it, transform it into a GETable URL and cache that.
    - Mark N: I believe we can make progress here, just need the right text.
    - Mike B: clarification about HTTP directorate review, AD role, etc.
    - Julian R: May need 2nd WGLC after changes of this scope.
    - Tommy Pauly: let's cut a new revision with these updates. Consider WGLC/last call once that's complete.

## Resumable Uploads - Marius Kleidl

- No open issues
- Multiple implementations. Interop performed at IETF 121 in Dublin
- Draft is ready, WGLC?
- How many people have read the draft? 10-15 hands
- Chairs: will start last call

## Incremental HTTP Messages - Kazuho Oku

- WGLC?
- How many people have read? 15-20 hands
- Tommy Pauly: are we aware of people using this yet?
- Kazuho: Personally not
- Tommy P: would be good to do in parallel
- Ben Shwartz: draft talks about intermediaries, but this would be very helpful to implement in client networking stacks. If you are a maintainer of an HTTP client implementation, consider implementing.
- Martin Thomson: not aware of many client APIs that don't have this capability.
- Mark N: may make WGLC longer here because touches intermediaries which can be a little slow.

## Detecting Outdated Proxy Configuration - Yaroslav Rosomakho

- Mark N: Proposal is to piggyback ....
- Julian R: 
- Mark N: should proxy forward or strip header?
- Yaroslav: ...
- Travis Langston: see use in this. Have two minute inactivity timer that gets bumped up. End result is it's still fairly frequent. I could see us using something like this.
- Alessandrdo Ghedini: Does stale mean the client might fetch configuration later or that it's required to continue?
- Yaroslav: It's a hint only.
- Alessandrdo G: what about case where proxy wants client to fetch configuration because there's a vulnerability in old configuration. Could the proxy return an error status code to tell the client to fetch the new configuration and then come back? Using existing status code.
- Yaroslav: worth exploring. Proxy is not signaling to client a new configuration URL
- Alessandro: using timestamp.. would it make sense to use a configuration ID instead?
- Yaroslav: could add this, but there is no configuration ID in PAC files. Closest thing is etag
- Ben Schwartz: Have related draft with overlap. This draft, does support a redirect capability. Biggest question to me: do you need the ability to signal stale on successful responses. 
- Yaroslav: experience says yes. We don't want client to fail in order to signal configuration is outdated. Another common situation is when I want to gracefully shutdown the proxy - stopping client from using that. 
- Tommy Pauly: as individual, good discussion. Useful, real problem, agree that this is something that we should be able to signal on success too. Draining case as well as "something changed, there may be more to the configuration". Need to work out details of spelling. Big diversity of configurations and configuration sources. Some are mentioned, but there are even more. There may not be a single version, we have cases where the type of client you are influences what config you get, but a single proxy serves multiple types of clients. 
- Yaroslav: I think current proposal addresses this. 
- Tommy P: Beyond PvD and PAC, there are more propriety configs which have the same problems. There are cases where proxies are configured through MDM profiles. Going the direction of etag complicates this because of diversity of sources
- Mike Bishop: as individual, really are two cases: config is fine and out of date and config is bad and you need to refresh. What about status code 421? do we need to say that if you get a 421 that you need to refresh your configuration
- Mark N: how do you know it's from a proxy?
- Mike B: this is a response on the outer request not on the inner request. Don't think we need a distinct status code. When you're going over TLS and you have an outer and inner request, you can easily distinguish. If you're doing plaintext, then you see things combined and can't trust. OTOH, if you get a 421 on the proxy request, maybe you should refresh anyway.
- Mark N: Re: 421, this has nothing to do with the connection. Details we can discuss later. Does the use case allow restricting to just CONNECT? Looking at problem space, may want to look at more generic problem of cache invalidation. 
- Mark N: looks like there's interest in this, let's keep the discussion going.


# Friday, 25 July 2025
14:30 - 16:30 Friday Session III - Tapices

Note Taker: Andrew McGregor

## 15 min - No-Vary-Search

- Presentation skipped

## 15 min - HTTP Unencoded Digest - Lucas Pardue

- Mark N: The intent with structured fields is that unrecognised fields are ignored. A reasonable implementer would default to ignoring extra fields. Updating documents seems excessive.
- Lucas: Should we take out the new text?
- Mark: No
- Marius Kleidl: Would like to support updating 9530 about this point. HTTP API working group has a document about these digests, so it would clear things up for that document.
- Lucas: We could make the integrity digest part of that formal term
- Martin: 6919 doesn't specify the discouraged form, which is what 9530 uses, but would like to see an Erratum filed on this.

## 15 min - Secondary Certificate Authentication of HTTP Servers

- Allesandro Ghedini: It seems like we could be a problem we fix when we actually have the problem
- Mike Bishop: The promise has a nice property that if you don't care you ignore the frame. Reserve a frame type and people can try the experiment
- Yaroslav: Feels like there are many use cases, so it might be best to keep this work concise
- Lucas: I don't want multiple frames in H2, simple solution is just to use H3, so I'd advocate just closing the issue with no action

- Alternate solution H3 over QMux
- Martin T: I don't think this is the answer. You can increase the size of frames in H2, but at least until we have post-quantum certs we'll probably be OK. I looked again at the state machine for streams, and you'd have to have something like a push promise in order to make a stream without messing up with the state machine.
- Tommy Pauly: There's going to be other discussion around post-quantum. The chairs got a request for looking at other secondary certs, and there's interest in looking at this area. So we can do the simple thing, ship it, and come back to the area. Looking at the open issues, we have two cases of things we could do but may not want to, nobody seems to be shouting about that.
- Mark N: I agree, with that said it's food for thought about the evolution of QMux. We need to think about how we use the community resource.

## 15 min - Template-Driven CONNECT for TCP (slides)

- Yaroslav: Right now there are different paths for how you generate RST, which seems like an implementation nightmare, so any particular reason we don't do a capsule for RST, that seems a more universal solution.
- Benjamin: The spec says that you must close the stream abruptly. If the send stream is closed without sending FINAL_DATA, you will emit an RST. The state machine is transparent to RST without version specificity. But the abrupt close is version specific.
- Y: If you don't send a FINAL_DATA, otherwise you're supposed to send an RST, which is more about what happens when something unexpected happens.
- B: Servers can send an RST to indicate data was rejected even after an initial success.
- Kazuho: Don't know if we need to say something specific about TLS alerts on H1.1.
- B: Maybe we should say we should close the stream with close notify rather than an alert
- David: The FINAL_DATA capsule is what makes it work, so if you don't send that it indicates that you had an unclean shutdown, and maybe we can specify the mechanisms as examples of what to do when that happens.
- B: Currently the text is more prescriptive than that.
- D: I'm saying maybe it's *too* prescriptive, and we could perhaps relax that.
- Tommy: with regards to RST, when you have the proxy connection close abruptly, you have to do something, and that should be a RST. Therefore, a separate RST capsule is redundant, because you have two ways to do the same thing.
- Martin: Few TLS sstacks give you access to either close_notify or alerts, and propagating RSTs will do the job
- B: It says that for insecure mode, but for secure we're intending to carry it in a secure manner.
- Martin: TLS close-notify is almost never used
- David: I hope we can get some implementation before we send it to the IESG
- Tommy: Would you be able to arrange some interop tests?

## 10 min - HTTP Version Translation of the Capsule Protocol (slides)

- Mike Bishop: WT discussed whether they wanted to define WT over H1, not much interest, so that doesn't exist. so that doesn't exist.
- some discussion missed
-  Mark N: Positively flagging convertible in the header seems more sound
-  Yaroslav: Datagram capsules and H3 datagram conversion interconversion... there are some sharp edges there, e.g. MTU and loss tolerance
-  David S: Similar to MASQUE datagram discussions, was convinced the datagram header should be mandatory, ekr was convinced it should be optional. Ekr was right. Conceptually nice idea, but in practice it is way less simple than you would expect. I think it can be done, the question becomes what's the point. If we think there's going to be a lot of ALPNs that have this, then it makes sense to make translating middleboxes, I don't see that happening. I would like to wait for evidence there's a problem that actually needs solving.
-  Kazuho: For every new upgrade token, I have to modify code, it's a pain, would be nice if there were a way of indicating that I can pass through without having to modify code.
-  Eric Kinnear: I had similar thoughts, but I don't love the spellings. Would be nice to have a standard set of building blocks that we can use to build WT over H3, for example. But I'd be interested in solving this kind of problem.
-  Lucas: I don't know what to do here, I don't have this problem quite yet. There's a problem down the line with extended connect.
-  Tommy: To what degree do we feel the pain here?
-  Erik Nygren: I think it's worth solving this, in the CDN world we definitely have this kind of problem. Would be better not to have to just pass the byte stream and hope.
-  Eric Kinnear: The other thing that becomes an issue here is the presence or absence of settings in H1
-  Kazuho: When proxies were designed in H1.1 era, there was no thought to whether upgrade token was version specific, and I thnk we have to resolve the ambiguity.
-  David: Lucas and I have been discussing revising capsule protocol, as there are some bugs. We're looking at if we can join forces to do capsule protocol v2 to solve a lot of these issues.

Should we consider work in this area? Yes: 15, No Opinion: 17, No: 0


## 10 min - Template-Driven HTTP Request Proxying - Ben Schwartz (remote)

- Yaroslav: HTTPS is supposed to be CONNECT rather than an absolute URI request.
- B: Yes, this does not solve the meta-communication with the proxy problem.
- Mark N: I notice you're introducing a new term "request proxy", which we should take care about. Second, there are different styles of forward proxy implementers, some are very performance sensitive, parsing out an encoded URL from a request is likely to cause some of them issues.
- Lucas: If I'm to do this, I'd like to specify what version of HTTP to use for the request
- B: URIs are supposed to be version independent...
- Lucas: I'm not sure it's necessary to do this
- Jonathan: This proxy is a full man in the middle, correct?
- B: Yes
- David S: I understand that there are people whose security model is "whoops". This is a thing of the past, because now we use CONNECT even for plain http.
- Steve Hill: These days a large fraction of traffic has to be picked up via transparent proxying. Given that we've largely stopped using proxy config, what hope do we have that it will be picked up?
- B: I don't think this is necessarily for general clients
- Marius: I recently ran into a situation where we had to use multiple forward proxies, which is a bit cumbersome, so we'd like to see a better solution.
- Mike Bishop: I don't really want to encourage this, but I understand it has some use cases. I think if you want to do this in a modern way, you do OHTTP without encrypting the payload. That gives you a clear boundary between proxy and origin. Not opposed to doing this work, but I don't think this is the right method.
- Tommy: OHTP relays aren't prevented from using templates.
- Mike: The minimum thing would be that you agree on the template format.
- Kazuho: The use cases should be constrained to a particular organisation, and I'm concerned about the security aspects also, so maybe we don't need to do it.
- Mark N: We'd need to have a use case discussion and perhaps some misuse case discussion, wondering if it's worth it.
