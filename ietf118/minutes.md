# HTTP Working Group Agenda - IETF 118

## Thursday, 9 November 2023

Notetakers: Jonathan Flat and Marius Kleidl

### Compression Dictionary Transport - Patrick Meenan (remote)

Summary of draft (request/response headers - see slides for additional info)

Changes since IETF 117 (PRs open, not yet in draft):
- request matching changed to use WHATWG URLPattern
- must include a path to match
- `match` is now split into `match-path`, `match-search`, `math-dest`
- optionally include a search (query) to match
- optionally include a fetch destination (Sec-Dest-Match field value)
    - e.g. site-wide dictionary for `document` destination
- default TTL is now 7 days
- non-dictionary compression is required
- client MUST sort A-E to reduce Vary variation

Discussion:

Mike Bishop: understands sorting of Accept-Encoding, but why is this done in this draft?

Patrick Meenan: this draft includes two new encodings, so we update the rules to require sort. but it can also be removed

MB: Seems beyond the scope of the draft, but it could be a good recommendation.

Timothy Terriberry: [not able to unmute]

Mark Nottingham: regarding sorting: concerned because of caches, caches should normalize A-E so that this isn't needed, we see that's not the case, but we shouldn't make clients do it if it's already broken

MN: don't understand zstd-d requirement

MB: if you support zstd-d, you must also support zstd, open issue of cache lifetime, an appropriately implemented HTTP cache should handle its space constraints, shouldn't need to reduce TTL to try to help caches

MN: reducing TTL is preemtive solution

PM: server can choose one value for TTL through headers, 7 days was trying to encourage frequent users more than free users


MN: how can all URLs be expressed in the match-* patterns?

PM: regular expressions are not supported, but wildcards are allowed

Vlad Krasnov: can we have an option to get the URL of the dictionary not only the hash?
we already have mechanisms to fetch dict based on URL and etag, finding dict based on hash is extra work, possibly a big change

PM: Trying to think of how we could do that since URLs don't map 1-1 to dictionary. You could maybe add to the request to the URL, but you still need to verify that

Mark: Vlad is concerned having a second index they have to lookup since every byte counts at scale.

PM: would adding a dictionary source url to http request help?

Vlad: Best if we could use an ETag instead of a hash.

PM: I think we'll always need to have the SHA in there.

VK: yes, but etag in addition would be good

PM: dictionary-source and dictionary-etag?

David Schinazi: from Timethy in chat: I don't see a lot of details in the draft about how the dictionary is used by the different algorithms. Maybe this is "obvious" but it might be helpful to at least have reference(s).

PM: I could probably link to at least the shared zstd and brotli APIs. Don't want to get into the exact details.

DS: from Timothy: The motivation for that question is that one of the things I found very helpful for SDP compression with gzip (for WebRTC) was to truncate the original message at some cutoff shorter than the maximum window size. Making sure the start of the document is inside the window helps avoid re-sending some headers that only appear once, and leaving a little bit of extra room makes sending the same SDP with only minor changes work much better. Have you considered being able to specify a limit on the amount of the document used for the dictionary?

PM: When you set a dict the entire response is used as a dict. For html, there are largely going to be external dictionarys that are custom built. There are things like WASM or CSS where you're versioning and can use the existing resource as a dict. As far as size goes, Chrome allows up to 100MB, but what you choose is up to you.

MB: Commenting on SHA vs path/ETag. One of the benefits of SHA is you don't know you don't know what it is, protects user's browser history.

PM: DOn't think it exposes any more than SHA, we've already assumed the SHA could be used as a tracking token. Already treated cleanup as if it was user-trackable.

Austin Wright: did you consider URI template? I experimented with it and it works in constant time

PM: We haven't, I'll take a look. Strong pressure from W3C side for URL pattern

MN: Pressure from the W3C or WHATWG?

PM: From both sides.

### Cookies - Steven Bingler (remote)

Quick status update
Changes in -12 draft: just advise the reader which section to implement
Slide of open-issues, stayed fairly constant.

(#2104) Same-Site cookies and redirects is only real blocker
- Caused breakage when Chrome/Firefox turned it on before
- If we don't solve this now, I'm going to remove it from the spec so we can continue work.

Work after RFC6265bis (e.g. CHIPS)

No questions from audience

### Unprompted Authentication - David Schinazi

Unprompted Auth --> The Signature HTTP Auth Scheme
Quick summary of draft (see slides)

Exported Authenticators (#2604)
- Should we just use it? From a crypto perspective, it was possible, but it would require tweaks to the spec in the TLS wg and would be harder to implement. We also have folks wanting to implement it above TLS. We did not switch to Exported Authenticators.

Put everything in the TLS Exporter Context

We've also put the key in the Authentication Parameters.

Jonathan Hoyland built a Tamarin Model which found some of these issues.

Jonthan Hoyland: There's another paper on how you can extend a security model even more. It could find even more attacks!

DS: Can the security people stop doing that?! (jk) We always welcome more security people to do their work.

Full implementation and looking to interop more.

We want to complete one implementation before WGLC, maybe WGLC before Brisbane?

Alessandro Ghedini: Clarification about EA, how is that more difficult than doing TLS Exporters?

DS: Main reason is that you also need to extract from TLS library which hash algo was used inside HKDF inside TLS. Not all TLS libraries give an easy way to do that. Not everything uses SHA-256 all the time.

AG: If the spec is not useful for somoe use case, maybe it's worth doing the work to modify it?

JH: Another issue with EA is that the client cannot send an EA it has to be requested by the server.

DS: Yeah more complicated in terms of spec and implmenetation work, but possible

Tommy Pauly: (EA implementer) personally I think the decision sounds fine. If someone did fix the EA issues, is there a way to start using that?

DS: In terms of extensibility, this scheme has a construction and we can built a different one, don't add another layer.

TP: glad about implementation experience. Was this just a test or a proper deployment/experiment?

DS: More of a basic interop. Part fo wider plan to do other things. It's not going to be deployed on its own

MB: Wanted to respond to TP on EA. If you think about it, if someone were to write a draft on how to stick an EA into a scheme (he might do this soon). Because of the problems we know, David is explaning how to use EA in the cases they don't work. We can write a draft on how to handle EA auth for the things it can do.

MN: Let's discuss the name soon.

DS: Ok

### QUERY Method

Julian has not had time to work on it but will soon. Only a few issues left.

MB: (From Julian in chat): I have no news about QUERY right now, but I did review the open issues, and I still think that a focused design team telco could speed things up.

MN: I am willing to participate in design team. Mike Bishop also interested in participating in design team. If anyone else is, please reach out.

### Retrofit Structured Fields - Mark Nottingham

MN: Nearly done, soon last call (again)

TP: issues from last call have been sorted out. soon we will do another last call for one week

Julian Reschke: you currently have a dependency on the draft-bray-unichars I-D. I'm not sure how that will be progress. (NOTE: this is sfbis, not retrofit)

MN: I think its an info reference though, if its going downhill we could just take it out in editing. Regarding retrofit, its relatively stable, we wanted to take a pause and think about it because its an abstract draft. Think about how it could be used in different cases. We will talk about this at IETF 119

No questions on SFBis or retrofit

### Cache Groups - Mark Nottingham

Because we have so much time, moving Cache Groups to this time. This is a new cache control mechanism to group valid responses, e.g. for invalidation. CDNs already do this , but we want to do it in a way that is truly interoperable.

No comments from audience.

### The qpack_static_table_version TLS extension - Rory Hewitt (remote)

*Not intending to diss the inventors of QPACK*

Context/overview of draft (see slides)
- QPACK is already 5 years old, there are a bunch of new headers that aren't part of the pre-defined static table, must be strings in dynamic table.
- Various limitation of the original QPACK static table.

Proposal is to add QPACK static table registry to IANA, use TLS extension to negotiate entries in the static table.
Spec is focused on future proofing.

Should it be a TLS extension? Boundary crossing since its an HTTP draft? Maybe use ALPS/ALPN, but those aren't used much?

DS: How much will this help? Do you have data?

Rory Hewitt: Quick answer is idk, doing testing now. Purely looking at HTTP webarchive, there are a lot of headers now (9 or 10) which are significantly more frequently found in the wild than the least frequently found static QPACK headers.

DS: As someone who used to work on browsers, I would want to see some of those numbers. My personal take is ALPS is designed for things exactly like this. MT is too busy with nom-com, maybe we could ship ALPS today!

RH: I would love to use ALPS. Victor Vasilie said there was some implmenetation, but the draft has died? The individual draft doesn't have any standing, but I think this would be a great use case to revive the draft

Alan Frindell: I have some data from inside our datacenter and CDN (internal traffic, not general traffic)! Have recent experience and will go back and look at it. We experimented with a different HTTP client stack (Instagram) that had different compression strategies and that had significant regressions.

AF: Issues in the static table should be fixed by dynamic table, if correctly implemented. We should automate table updates.

MB: Interest in this, open issue is H3 to adjust static table in use, punted it to an extension, now here's our extension. Hesistant on tagging things on the end of the static table. The ability to choose a different table is probably more appealing. There were concerns around IOT with H2 H3 that could now say, "I don't support a static table" or "I only support the first N entries".

RH: Everybody could specify their own static table for their specific usage. Could just be 20 headers that they use.

MB: Specific details here. Reviving ALPS is more palatable vs TLS extension, there's a lot of wiggle room. But I support updates to the static table.

AG: I also agree this is useful work. It seemed a bit weird we would define a single static table once. There's a lot that needs to be figured out, I don't understand the negotiation process in the draft, the way I would think of it would be someone defines a table in a new draft, that table goes in a registry, etc. You would just use that specific table. Do you know of any specific use case the length in the TLS extension would be required?

RH: the use for specifying table lenth is: client might support less entries in the table than the server, for example to save space.

AG: Right, but would the lenght of the static table be part of the version?

RH: We could come up with the concept of version, which is a reordered copy.

AG: Ah so if you define a version of a static table, you would define the table in its entirety.

RH: Yes, version for table and length for number of entries.

Lucas Pardue: In Multicast HTTP, one of the difficulties with dynamic QPACK stuff was that you wouldn't be able to join a session since you didn't have the table history. I like the idea we could define domain specific tables like this since it could support these use cases. Pluggable static tables could enable a lot of interesting things--better than just having an append operation. In the latter case, the process of updating the table would become political, who updates the table right away, etc. 

Kazuho Oku: Echo Mike and Lucas, very good start. I'm not sure about TLS ext vs ALPS. We could just use the SETTIGNS frame with 0.5-RTT? Like QUIC, we could remember the previous session.

Dragana D: I would like to see perf data before doing anything. I would like to avoid TLS ext. Kazuho said what I wanted to say.

Michael To: Echo Lucas, if we're at the point where the static table has multiple versions, that's a dynamic table. Maybe we rethink the model, maybe we have an initial table?

VK: First, good idea if compression is better. The lowest table version is picked between server and client. Ok for the server, but requires a lot of data on the client. Maybe a list is better?

RH: If it were a TLS ext or ALPS, ideally you want client to send through "these are the ones I support", and server negotiates, they at least need to support the minimum version. You're right, we can't have a client with 50 versions of the table.

David Benjamin: On 0.5-RTT data, considered that for ALPS. I wrote a draft comparing ALPS and 0.5-RTT data. It doesn't work when strong ordering between client request and server info. SETTINGS frame might not be sent in 0.5-RTT.

Yaroslav R: Good point about domain specific header sets, e.g. IOT devices. Maybe instead of numeric version, maybe support alphanumeric version strings where people can define their own versions.

MN: Table is a bike-shedding process. What is the goverance on selecting this table? What is the duration for updating the table?
Maybe a new ALPN token and that's okay? If you do need ALPS that's another issue, since it hasn't had enough support. How much gain do we get from this? Static table was really just to get through the first few flight, then we're in the dynamic table. More than anything we need data.

AG: Comment on Static vs dynamic: lot of complexity for dynamic table. It is a common option to not implement dynamic table. If we can prove there is benefits, it's good work.

LP: Reminded me on how good it would be to do that in JS libraries in browsers, I'll post a link in the chat. Behaviors we might not want. https://infrequently.org/2022/03/cache-and-prizes/

AF: Not implementing dynamic table since its complicated. If you want to have 3 headers in the static table, you can implement you own dynamic table method easily.

MN: My concern too--how complicated is this gonna get?

MN (Chair): But there's a lot of interest.

TP (Chair): Lots of discussion on collecting data, that should be the thing to move us forward.

MN (Chair): Also, one server-side data is interesting, but if we could bring client and server data to be more holistic that would be great.

AF: Call on list? HTTP workshop or interim? 

MN (Chair): Workshop would be a nice place to talk about this.

MB: If we want to do this through ALPS, does this go through ALPS formally.

MN: We're concerns about ALPS in terms of feasiblility and ecosystem impact, we couldn't assume anything. We need to know what properties we need for the negotiation system.

TP: We have enough overlap between TLS and HTTP we can figure out the properties we need in the solution. We have a collaborative approach across these WG (HTTP and TLS).

## Friday, 10 November 2023

Note Takers: Eric Rosenberg

### Resumable Uploads - Marius Kleidl

Jonathan Flat: byterange patch adds unneeded complexity. In favor of option 1 or 3. Optional 3 could be partial PUT with same content type?

Austin Wright: Previously suggested partial PUT may be suitable here. Byterange patch suggested for cases where you don't know if server supports partial PUT. 

Marius: May be other patch formats in the future

Mark Nottingham: Probably do need special media type for certain cases. "+" has a meaning - might not use what's in slides.

Kazuho Oku: We are not trying to create a long running transaction protocol. We don't need to do more than what HTTP does today.

Mark Nottingham: Decision to be made as to whether we try to model this as a resource state or try to provide fidelity down to the message level. IF we're trying to provided fidelity down to the message level - that's very difficult.

Jonathan Flat: Client should decide what it wants to do in response to 500. Perhaps retry.. but probably doesn't need to be specified. Instead of sending empty PATH request, client should send request again for offset.

Austin Wright: For client missing response case, ... 

Jonathan Lennox: Questions seem largely relevant to hackathon project where proxy transparently handles a lot of this. Not sure how viable this is. Probably need more coordination with the application server.

Kazuho Oku: Sending offset is fine. Not sure clients can rely on it to release memory. Proxies are required to forward information responses - this should be safe.

Lucas Pardue: ..

Jonathan Flat: If one gets dropped, you can still figure out where to resume. We should require all location header field values are the same.

Lucas Pardue: you're either going to get all or none of the information responses. Dealing with getting some but not all is less interesting.

Lucas Pardue: We should mention integrity can help, but is not needed. Doesn't need to be specified in this draft. Do nothing more than mention the possibility of doing this (HTTP digests) - but even that is probably not needed.

Mark Nottingham: Philosophy is to describe the components and how to use them - not type relationships


### Templated Connect-TCP - Ben Schwartz

David Schinazi: Filed issue - would it make sense to have a default template similar to CONNECT-UDP and CONNECT-IP?

Ben Schwartz: I didn't do that because if you don't have a tempalte, we already have a default way to do TCP proxying - using standrd HTTP CONNECT. If you only have a hostname or authority to go on, you're already good to go.

DS: In a world where we're building "new" proxies, it would be nice to have all proxying types together so that we can completely get rid of legacy CONNECT.

BS: I don't object to default template. Those "new" proxies should just be configured with a URI template.

Tommy Pauly: While I agree Ben.. for future things we could do here (e.g. connect-udp listen), I'd be interested in seeing a tcp listen proxy. Would work well within the ecosystem of connect-tcp. In that case, the "old" way ...

Tommy Pauly (Chair): Relationship with optimistic upgrade... is there are a particular relationship between this and that? Do we want to adopt that other work before going to last call

Ben Schwartz: No relationship between the documents. Comfortable moving independently.

Mike Bishop: One of the reasons we want this is because legacy CONNECt, doesn't let you specify the hostname of the proxy as part of the request. Legacy CONNECT isn't a sufficient fallback for those who need that hostname. 

BS: That seems like a strong agument

Erik Nygren: +1 for default template so we can get rid of legacy 

David Schinazi: Second open issue about origin. Ties into this conversation.. Original HTTP spec is not clear about what the origin is when you're talking to a proxy, in particular because there's no scheme. You get into weird situations getting alt-svc on a CONNECT response. Would be unfair to fix all that here, but might be useful to have that discussion. Perhaps this document should clearly spell out what the origin is here.

BS: We could add this as further motivation at top of document.

Yaroslav Rosomakho: In traditional CONNECT, there is a way to specify proxy origin. Proxy hostname can be derived from SNI. Perhaps this could be mentioned for implementors that want a fallback mechanism

BS: Inclined to avoid talking about SNI. This lives entirely within HTTP. 

MN: We're not updating 9110, correct?

BS: Correct

MN: Draft talks about the semantics of CONNECT - this isn't needed.

### Security Considerations for Optimistic Use of HTTP Upgrade - Ben Schwartz (remote)

Lucas Pardue: Good work, thanks Ben. We should adopt.

Mike Bishop: Definitely support adoption. I will point out that pointing to the example of h2c upgrade - that is now deprecated behavior. Maybe we can point to it as a good design pattern that is used, but is no longer in use.

Kazuho Oku: This has to be adopted to fix CONNECT-UDP. We can say just don't do this in HTTP/1.1

David Schinazni: Please adopt

Jonathan Lennox: Mentioned in order to do this you need to use certain capsule types - worth putting in registry to make this not possible.

BS: Draft says don't optimistically send when doing HTTP/1.1

David Schinazi: Strongly agree with Ben - I would be strongly against reserving capsules

Poll for adoption support. 35 yes, 1 no, 32 no opinion. Will do formal call on the list.

### Reverse HTTP Transport - Ben Schwartz (remote)

Ted Hardie: You have somehow avoided to talk with firewall folks if this is your view of what firewalls are capable of. Firewalls do much more complicated things than what you're describing. You should make your agument for this completely disjoint of what other services do.

BS: Noted

Lucas Pardue: Lots of people doing this type of thing. Creating a standard for something many people are doing seems sensible. The point about proxies and DDoS didn't totally make sense to me. Not sure if ready for adoption - another draft revision or two would help.

David Schinazi: Christian H had the idea of a "hidden server". This is implementable with MASQUE. Important property is you do funky things at the proxy and leave end-to-end alone. This draft does the opposite. This may not be impossible, but this seems very challenging to get right. We should solve at proxying layer.

BS: A lot of the solutions that take that form end up with double encryption. 

Kazuho Oku: Agree with what Lucas said. There are real use cases - I would be happy to see this adopted. There are limits to this design if you consider large scale deployments. That is, the endpoint is being defined by the fqdn and authentication is being tied to certificates. Could we use an extended CONNECT method to create this? Would be able to use URI and any scheme.

BS: Right now this is bound to client certificate authentication - sounds like you're suggesting considering other ways to authenticate the origin.

KO: ....

BS: Need to think about how you convince the intermediary you are the origin

Ted Hardie: In chat there's a pointer to a system from 2000 that does something very similar. There are a bunuch of different variations that have been designed along the way. The hardest thing you'll have to do here is write down exactly what is in scope and out of scope when you reverse the roles of HTTP. You could say this is just for proxies talking to origins. This needs a BoF. The scope of work you're taking on is either extremely large or narrow depending on what the charter says. You're going to have to do the work to figure out what the appetite of the community is to do this work.

Alex C: Interested in theory, but worried about role reversal and the effect that it has. I've seen this particular use case desired and people asking how to accomplish similar things without touching firewall. Appliances are typically HTTP/1.1 only, but this draft is h2 and newer. Why not just use MASQUE? Nervous about scope - let's find a way to bridge technology gap with a less invasive solution.

Austin Wright: Have done research in HTTP over mesh networks. Not sure there needs to be any specification or ALPN identifier. What happens if things are congested, when does origin open more connections? Also with h2, some implementations always assume odd numbers are always requests. 

Michael Toomim: Find this exciting. Connected to group - distributed web hobbyists/hackers. Would be interested in this for serving a website from your phone. This connects with what I'm presenting on state synchronization in a more p2p web.

Tommy Pauly: Like the direction Kazuho was going with this. In the next talk, we're discussing secondary certs. We're only discussing server use cases there, but there may be client use cases too.

### Secondary Certificate Authentication of HTTP Servers - Eric Gorbaty

MN: We have done work in this area before. Stopped due to concerns about complexity and implementor interest.

Lucas Pardue: Support adoption of this with its current limited scope. For the hybrid proxy use case, you'd going to end up with long lived tunnels. Should think further about using these things together. Agree on punting on client certs.

Alessandro Ghedini: I was in favor of previous draft. Even with the reduced scope, this is useful and opens the door to further work in the future. Part of the reason the original draft fizzled out was that there wasn't much interest in implementors, particularly client side implementors. Would be good to heart from clients (e.g. browsers) that want to implement.

Eric Gorbaty: ...

David Schinazi: Regarding implementation, someone from Apple is bringing this work to the group, it wouldn't be surprising to see this in Safari.

Mike Bishop: I will note the original draft was two separate drafts, but the group asked to group them. I support adoption

Jonathan Hoyland: I am a proponent of the "not scoped down" version of this because I want the client side stuff. We previously discussed unpromted auth and exported authenticators. Seems like we're locking ourselves out. Leave out the section that we don't support clients.

EG: I would say there are a number of mechanisms to support the client side support of this to do it well and safely. Those were where a lot of the complexity in the old draft came from.

Jonathan Hoyland: Punting on the complexity is fine if the working group is OK with the work happening twice.

Erik Nygren: I was also more interested in the client side of this. I'm worried if we do the server side of this without a DNS check, we open ourselves up to risk.

EG: Current draft does recommend DNS check as well as origin. Are you suggesting that it should be mandatory?

Erik Nygren: DNS check as mandatory or for general case would make sense. Presentation previously at maprg showed ...

Tommy Pauly (no chair hat): To respond to Jonathan - given the discussion we had for unprompted auth, we may want some tweaks at the TLS level definition here. We've done a good job of pushing through smaller documents without too much overhead. I don't think this imperils the efforts at the client-side. If anything this allows us to learn more from implementation experience.

Show of hands for adoption support: 24 YES, 3 NO, 43 No Opinion 

### Per-Resource Events Protocol - Rahul Gupta

Austin Wright: Use partial content

Alex C: Why HTTP? Curious what client and server is used. Why not some other protocol?

Rahul G: It's easier to use HTTP for clients. ...

MN: Be clear about where HTTP is adding value (e.g. intermediation, ...)

Austin Wright: Sparse resources where ...

### Braid - Michael Toomim

David Schinazi: Changing the goal of HTTP is daunting. I understand when you say HTTP was desired for a different era, but we've also evolved it since. It's working quite well. From my experience, big paradigm shifts rarely happen incrementally. I don't see a big paradigm shift in the cards. I like how you say we're almost there. Focus there - highlights the gaps and push there.

Michael T: By "goal", let's work on those items.

David S: I recommend you bring here all the bits in HTTP and have the tying together somewhere else (e.g. W3C)

Kévin Dunglas: I'm author of similar protocol. Already proposed to IETF a while ago. Main difference is ... There is a strong need for standardization. 

Mike B: From IETF perspective, closest parallel is MASQUE. Not necessarily a vision of new work, but rather composition of many pieces already happening. Find the pieces that are missing, bring them to the appropriate working groups, and drive it.

MN: Individual components need to stand on their own. The draft as-is is top down.



