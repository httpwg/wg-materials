# HTTP Working Group Minutes - IETF 120


## Monday, 22 July 2024

### Resumable Uploads

#### Discovering upload limits upfront (#2833)

?: Would the Upload-Limit be set by the proxy or by the origin server.

Marius: The origin server would have a proxy on their side, and they would set it.

Mike Bishop: Do new requests have new fields work with options?

Marius: doesn't understand question.

#### Upload size (#2832)

Michael Toomim: Useful. Versioning draft has a similar mechanism.

Piotr Sikora: What about backwards compatibility with existing servers?

Marius: This only works if the server supports resumable uploads. For transparent upgrades you have to include it in the first request.

Michael: Useful for displaying a status bar.

#### Requesting digests from server (#2834)

Mike Bishop: Using digest fields seems like a sensible way, modulo naming.

Marius will talk to Lucas offline.

### QUERY

#### Identifying QUERY results (#1918)

Mike Bishop: There are 2 things we can communicate: on the response to the query we can say where you can find the results in the future. Example: serach for "weather in Vancouver": either link to weather right now, or link to weather at date of the query.

Not sure what the right answer is, but we need to pick one.

Mark: It's not either or, but we can document both. Need to look into exact semantics of Location and Content-Location.

mt: Location would tell you where would you go in the future when the world has moved on. Content-Location would link to the historical result.

Julian: to come up with a proposal in collaboration with Mark.

Mark: We're now putting more weight on the HTTP method.

Julian: Every HTTP method needs to specify concretely.

Julian: Can we define QUERY as a transformation? Skeptical.

Mark: Agrees.

Mike Bishop: 9110 says that a cached Host can be used to satisfy a GET request. Does this apply to QUERY as well? It's risky, but it's risky for POST too.

Mark: 3 things: Resource that you query, the resource and content location (like any other GETtable thing), and there's resource and location, which is also a resource that's static.

Mike: It's a GET-table thing to resend your query without all the parameters. Should QUERY be different from POST? No reason it should be, but could be tricky for proxies to get right.

Mark: Scary if cross-origin.

Mike: Was specified as cross-origin in the design team meeting, but should double-check.

mt: Mike should be on the draft. (-> https://github.com/httpwg/http-extensions/issues/2837)

### Cache Groups

No open issues. Ready for last call.

Mike: Any implementations:

Mark: No, but compatible with existing code. Draft might need to sit before it gains momentum.

### Communicating Proxy Configs in Provisioning Domains

Lucas Pardue: Where do these JSON tokens come from?

Tommy: We initially wanted to derive this from the string representation, but now we have a new string registry. There's also legacy types for existing protocols like SOCKS.

Lucas Pardue: Maybe use HTTP for HTTP-based proxying protocols.

Josh Cohen: ??? 
How would you find the PvD files?

Tommy: Two ways: Comes from the network as defined in PvD, RA from the router, fetch config from this HTTPS URI. This file could include a list of proxies.
Or could ask an existing proxy if there are any other proxies.

Yaroslav: How to define exceptions. Things that should go direct vs. things that go via the proxy. Draft currently only allows for suffixes.

Tommy: Current version does. Allows exclusions.

Mike Bishop: Use case for unprompted auth?

Tommy: Unclear how client cert configuration would work.


## Wednesday, 24 July 2024

###  Security Considerations for Optimistic Use of HTTP Upgrade -- Ben Schwartz

#### Slide 5 - deprecate HTTP upgrade token

* Mark Nottingham (mnot), as individual: we shouldn't act based on what random websites write about HTTP. Too many of them, impossible. Have had luck getting MDN to update, they're often seen as authoritative.
* Ben Schwartz: that screenshot was the only website I ever found that said this
* mnot, as individual: I agree with Roy saying that we don't need to deprecate, and if we do it should be its own intentional draft
* Ben: this is in quantum state: existing / not existing. If we mention one we have to pick one. Other option is to not mention it all
* Mike Bishop: we don't lose registry by indicating that something is obsolete

#### Slide 6

* Mike: I thought there was a stack that did this, but turns out no
* Ben: Not aware of stack that does this, just considered making this implementation myself
* Mike: does anyone in room know an implementation that does this over h1?
* Room: crickets

#### Slide 7

* Tommy Pauly, as individual: I like having this, 
* Michael Toomin: use RECOMMENDED instead of SHOULD
* mnot, as individual: some people don't like putting normative requirements on future specs
* Martin Thomson (MT): this should not be normative, but we should still do it. Should also improve the text to explain why upgrade means for the body and why GET is best
* mnot, as individual: +1 to writing down explanation
* Lucas Pardue: GET can haz body
* MT: just don't

#### Slide 8

* MT: this isn't really important but we shouldn't make strong claims here. Implementations that look at streams of bytes often take liberties and can still misinterpret. We can't definitely say that TLS is safe here
* Ben : what about h2 preamble
* MT: that's a part of defense in depth. We've seen middleboxes that scan the payload looking for GET until the find something


### HTTP Server Secondary Cert Auth - Eric Gorbaty

#### Slide 3

* Tommy, as individual: We have a use case where use secondary certs from a proxy. There the server sends the secondary cert based on watching previous client activity (client CONNECTed to this hostname that server is authoritative for). We don't need explicit signaling here. And we could add it later
* Erik Nygren (Erik N): It's useful to know when connection was coalesced onto, especially what caused that to happen.
* Eric Gorbaty (Eric G): Not a great answer for how to do that, let's take offline

#### Slide 4

* MT: strong allergic reaction to anything continuation-shaped. Mistakes were made, this could be another mistake. We could use a compression technique to handle the certificate chain here. Then individual signatures fit in an h2 frame
* Lucas Pardue: also worried about security issues related to continuation
* Mike: since this is an extension, it can change anything about the protocol and can allow continuation on control stream. We shouldn't though. re: MT's suggestion, good if we redefined exported authenticators from scratch, but really hard given how they work today
* David Schinazi: why were continuation frames a mistake?
* Mike: We defined a negotiable max frame size for a reason: multiplexing requires splitting frames. Continuation allows that. But because HPACK is a continuous block, you need the whole frame at once. But that might not apply here.
* MT: We have 16K as max frame size by default and in most implementation, but we have a 3byte length sowe could do that. You could wave the limit here as another solution since control frame. Not great for multiplexing but works
* Eric G: head of line block not great but 16MB is enough
* MT: you could also create a new stream type, but that's work
* David: Based on reasoning, TO_BE_CONTINUED might be easiest unless there's a footgun I'm not seeing
* Eric G: let's take to issue, we have multiple paths forward


### The HTTP Wrap Up Capsule - David Schinazi

WRAP UP

In which David invents new terminology, makes forward and reverse proxies, and nests protocols in awkward ways.

Our protagonist sets the stage, describing the actors on the stage and establishing their motivation.

The villian enters the scene, is foiled by some superlative defenses.

The denouement is introduced, but in a twist, this is the true beginning of the narrative.


Piotr Sikora: Seems good.  We should try to get capsules in CONNECT-TCP.  Something you didn't mention is that the capsule is only sent from the proxy to the client, but it might be useful to send it from the client to a proxy.  Especially in multi-hop scenarios.

David: The issue is that the proxy receiving the capsule can't act on that information because it has no control channel to send it to the origin.

Piotr: Could we distinguish between relays that terminate and those that don't in a multiple node arrangement.

David: You can't act on the information at a proxy because you don't have the ability to act within the encrypted tunnel.

Hot Mike Mike: GOAWAY might be a sufficient signal here.  Unless you need a per-stream signal.  Is this about winding up a single stream or not?

David: GOAWAY solves one of the problems: the proxy going away.  The other is about capping usage.  Then you need a per-request signal.  This is that per-request signal.

Erik Nygren had the same question as Hot Mike Mike.

Tommy Pauly: Maybe we need a different semantic for this.  Maybe focus on the "no credit left" use case.  We should have capsules in CONNECT_TCP either way.

David: We can rename.  THe capsule is simple, but it could carry more data.  Wanted to keep things simple.  Could explore that.

Lucas Pardue:  Understand the problem, worth fixing, this might work.  We don't need to resolve those until this is (potentially) adopted.  There are use cases for non-privacy proxies, such as for a control plane between multi-intermediary deployments.  We often involve additional services in contacting origins, which might need to do something like this.

Kazuho Oku: This has benefits.  This working only for capsules is not ideal.  I would prefer a frame-based approach.

David: Frames don't traverse intermediaries.  Maybe you can put data frames inside streams.  Having extra encapsulation might be usable.

Alan Frindell: I've seen this problem with webtransport.  We have a similar capsule in webtransport.  Maybe we can use that.

Erik Nygren: Are there other use cases that GOAWAY doesn't cover today?


### No-Vary-Search -- Jeremy Roman

Jeremy: I'm here to talk about new variable responses.  Browsers support URL parameters and this affects cache software.  A vary header that lists the parameters upon which the response varies.  Today Chrome does support this. the concept seems generally useful to cache implementations (browser caches, CDNs).  

Why do clients send "meaningless" parameters that the response doesn't even depend on?  

- ordering may not matter and the response may be the same although the parameters are reordered
- parameters may affect server processing but not semantic result of request (debug logging, affecting throttling)
- parameters may be more for use of the client

Solution proposed: new header "No-Vary-Search" with several options for different cases

- response doesn't depend on query params at all
- response doesn't depend on query param order
- response desont' depend on vaues of specific params

We've got some implementation status.  If this is interesting to the WG, there's still some work to make it more conforming as an Internet-Draft.  It doesn't yet tell cache implementations how to change their caching behavior, and those instructions would be required.  there may be issues we didn't run into with the Chromium cache but which other people find are important.  

#### Mic

Michael Toman: How does this affect cache performance in practice?

Jeremy: In our main case, we don't have any cache hits at all without this feature, so it's a big impact.  We want to prefetch and cache some things for google search results.  I don't have data about other applications.  

We do send a special purpose header indicating that the request is a prefetch.

MNot: it's common for CDNs to do this in a proprietary way, so it's nice to do this in a better way that's aligned with what browsers do as well.  I expect most people in the room are more transport than cache oriented, so if you can go back to your caching teams and ask them if there's interest, that would be appreciated. We can also take to the list and there are independent cache vendors there and we can get their feedback.  I think this is pretty obvious to take forward.

MNot with chair hat: I'll take this to the list and call for adoption. 


### Revising Cookies (again) -- Johann Hofmann

Johann: I work on Chrome, at Google 1 yr looking at cookies with Anne van Kesteren. We're at the point we want to start talking to the group here about our draft and this work.  We just put 6265Bis into WG last call after 10 years of overall development, which is really great and we appreciate all the work of the editors. So why do we want to do another one?  Valid question.  

6265bis added a lot of really great innovations, particularly in the browser security space, same-site attribute etc.  The way it introduced these things, unfortunately we'd call a layering violation: it did it in the way that browser specs would, but it's not a browser spec, it's an RFC.  We're feeling the pain of that trying to work on cookie store api, storage access api, partitioned cookie attributes etc.  We should be able to control how that works in the browser specs but it's hard to do?  It creates unnecesary overhead for non-browser user agents.  

Additionally we have deferred issues from 6265 bis, like same-site=none, and a new doc would be a great way to do that.

So how are we going to do that, we want to define the concept of a cookie store in the cookie spec, and make it more explicit.  then define operations on the cookie store, like add and delete.  Then we make expectations about how specs and implementations deal with these operations and network requests.  With browser UAs, we largely defer to HTML and fetch to use these operations on the network response.  Non-browser agents , the cookie spec would define how to behave.  

We have a draft, please review; definitely there are rough edges.  we have some hand wavy stuff around observing cookie changes in JavaScript. We're working on top of 6225bis.  I'm not super familiar but I think we're replacing whatever number 6265bis gets when it gets published. That's it.

#### Mic

Steven Bingler: Speaking as 6265bis editor, I think this is great. 

MNot; I think there's been background discussion about how this thankless work is necessary. we'll have to talk about who has energy to put into this.  With 6265bis we made sure that large new features were vetted as separate drafts before being included, but I don't see that being necessary with this work.  Johann you want people to know about the draft but not necessarily... ?

Johann: This is the first we're introducing to the group. happy to take feedback, we expect to continue working on this in the WG.  

MNot/Tommy: We'll talk to more people about this...

Johann: THere are new features we'd be introducing, for example the partitioned attribute.

### HTTP Resource Versioning, Michael T

Michael: This is a continuation of features to add state synchronization to HTTP.  The goal is to have the equivalent of a local-first google docs.  This requires 4 extensions to HTTP, each of which is individually valuable.  Today we're talking about one of those, versioning.  NOTE this is not API versioning.

HTTP resources change over time.  It's a state transfer protocol, and state changes. Each state change produces a new version.  Version history can be linear or it can branch/merge like a DAG.  This does exist in HTTP in a few ways:
 - Last-Modified header: a timestamp, but only to resolution of a second.
 - ETags: more precise but specific to content, a change back to previous version might restore an old etag, and it doesn't tell you what version is before or after another version. 
 - many approaches give you a different URL per version.

This slide shows a feature matrix of what features are supported by these 3 mechanisms. None of them support branching/distributed time .  None of them offer customizable time formats.  

The abilities of generalized versioning would include:

 - incremental RSS updates - just download changes
 - Host github repos natively on HTTP
 - CDNs could have historical archives
 - Apply PATCH from older versions and rebase for other clients
 - Send PUT/PATCH/POST edits that were made while offline - know which version the update was made against
 - Collaborative online editing

Our design goals (slide)

Now does this belong in this WG? 

Josh Cohen: Earlier you mentioned WebDAV. How would you compare to that what was done in versioing there?

Michael: What was done in WebDAV was different URLs for everything, including the version history, and lots of passing XML to find out what's going on. This is a lot simpler. 

MNot: If you ahve a git repo you have a full history. But in other situations you don't have every version of all history. IN which case, some tradeoffs need to be made and the protocol becomes more complex. I wonder which of these scenarios and use cases are really going to be compelling.

Michael: It's true some of these use cases require additional features too. 

Eric Nygren: Other things I've seen for CDN partial object caching, and you want multiple large objects cached simultaenously; having a model here might help with that.  Object store systems like S3 , could also find it useful.  [Michael: what is that updating a partial object? ]  The cache can serve partial objects with range requests, but you don't want this franken object in your cache.  Etags help there but you can still get into messy situations that don't converge towards a single object.  

Michael: I'll show a resumable uploads example. If you mutated your object, part of it is cached, the semantics will allow you to keep the cache of the old part, and also know that the other part has changed. 

Going on.  We want versions to vary with points in time, not content.  We don't want to require additional URLs, but we do want to be compatible with that. 

Two main headers: *Version* and *Parents*.  Version header stores a version, and Parents header stores a list of version IDs.  Within this, the Version ID is a unique string identifying an edit, and the Version-Type gives you the format of that string which allows for interesting semantics.  

Example slide: regular PUT can say which version is being updated. GET can be used to get a specific version.  I wrote this up on HackerNews one time, the WebDAV version is like 50 lines or something. 

Variant GET semantics includes getting an older version, getting the diff between two versions, and regular. 

MNot: So the Version header modifies the behavior of the GET?  How is this backward compatible?  If the cache doesn't recognize the Version header, it will just respond with what's in cache regardless of this header? 

... brief conversation concluding that this does in fact break with caching intermediaries that don't know about Version

Michael: If you PUT without a Version value, the server can provide a Version header. 

Version History, in our proposal, would be to return a 104 Multiresponse with multiple versions all included.

Here's some crazy things you can do with Version-Type.  [slide showing vector-clock used in version string]
If the version-Type is run-length-encoding... which lets CRDT become pragmatic.  When each version of the shared-editing document adds 1 character, returning every version is 1000x.  

Resumable uploads: when we upload, if we upload one byte at a time, and time is proportional to the length of the file being upload, we get the equivalent of a byte-stream.  Let's say we're doing an upload, the upload gets interrupted, teh client can ask the server what version (time) of the resource the server has. We don't need another header to figure out where to restart from.  

We've got a lot of implementations. This is a text file at a URL, that is also a collaborative editor.  You can see a version history if you open chrome dev tools, that is a DAG, you can edit offline and your edits get merged.  You don't have to use tons of JavaScript packages to stream over a Web socket. WE have working feeds, you connect to the feed, and get your stuff.  

MNot: Comments?

Chris Lemmons: I'm interested in the problem space.  I think you're solving a real problem, and there's value to a standard solution to the problem.  There are lots of existing solutions, and they don't operate well with caches in the middle.  Mark made observations about what the current implementation is likely to do with caches, and that's spot on, and we'll have to think about this to move the work forward.  Figuring out intermediaries is important here, is the exact value that doing the work here can provide.

MNot: this is the problem with new HTTP features, they always have to mesh with other features.  If we are to adopt this work we have to figure out how to chunk it.  There are scars and lived experiences in each of these areas, like teh byte ranges stuff which is a little scary, and multi-status.  

Kouhei??: We try to cache compiled resources, and the resources get larger and larger, so we hope to reuse the previous one.  This work is a step forward in that direction, where we can only compile the delta.  

Tommy Pauly, as chair:  Thank you for focusing on a particular flow and making it clear.  I think this approach is easeir for the group to digest and understand. 

MNot: I think people need some time and discussion, I know you've been working on this for a while but we still need that.  

