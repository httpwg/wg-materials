# HTTP Working Group Minutes - IETF103 Bangkok

## Wildcard addition
3 min - HTTP record - Ray Bellis
 - Mike Bishop: We already have alt-service. We have a draft for putting that in DNS.
 - Ray Bellis: I see this as being the primary service for HTTP. This is simpler to deploy.
   I'm looking for feedback from implementors.

## HTTP Core


### [Github Issue 138](https://github.com/httpwg/http-core/issues/138)

Roy Fielding: I'd prefer not to change this.

Action: Close this

### [Github Issue 129](https://github.com/httpwg/http-core/issues/129)

No meaningful discussion, silent agreement.

### [Github Issue 128](https://github.com/httpwg/http-core/issues/128)

Roy Fielding: If we say MUST NOT, we're creating a new error condition.

Chairs: Are we aware of any implementation that generates these quoted forms?

Action: Gather some data. If there's no conclusive data, we can close with no action.

### Github Issue 120

Roy: What are we trying to fix:

Mark: Make it easier to make new status codes.

Roy: The issue is when we introduce status codes like 206. Status codes aren't frequently updated and you don't usually want to cache them when they are introduced.

Mark: Well, 206 wasn't a thrilling success

Mike Bishop: I think I'm convinced that things should be cacheable if there's a Cache-Control header. And if we want a new status code to not store, we can make the server send no-store with the new code.

Mark: Server doesn't need to do anything to make it not cacheable; omitting Cache-Control is sufficient.

Roy: You could define a new parameter that says "Cache like 200", so if it contained that, it would cache like the other code. I'm not sure I like it.

Mark: But how long do you have to keep that for.

Action: Simmer for a bit longer.

### GitHub Issue 111

Alexey: In email space, the latest docs say we don't yse "header", we use "header field", "header block" and other things. I think it might be better to invent new terms.

Pete Resnick (?): The reason for that is because there was a time where "header" referred to the "block" instead of the line.

Patrick: We have "headers" which contain a plurality of "header". I think it's consistant with our naming, but doens't improve readability:

Mike Bishop: "Header block" is the output of the compression process. The exact meanings aren't obvious from reading the docs.

Mark: There aren't that many people minting new email header fields.

Alexey: I don' think that's true.

Mark: In the HTTP community, the most common terminology is "Header" and reaching that community means using those terms. Does anyone disagree?

Martin Thompson: We have a lot of docs that already call them header feield.s People call them headers and it's just annoying typing "field".

Mike: The easiest thing is consistency. We can note that we colloquially call them headers.

Patrick: Core is a restatement, so we can use Header Field in Core, but allow "Header" in other documents.

Alexey: I think it's interesting to settle on one terminology.

Piotr Sikora: One argument for using specific terminology is that it's ambiguous whether "Header" applies to both Key and Value or just Value.

Action: Continue discussion in the issue on GitHub.

### GitHub Issue 48

No discussion

### Github Issue 45

Martin Thompson: I think Julian answered the questoin well enough. IU don't think the document answers it well enough, but as long a sthere's just one answer.

Action: As in the issue, create a separate section discussing normalization rules.

### Github Issue 42

Pete Resnick: I talked to Michelle and she asked about it. That developed into: Separate out how we want to work it on this end and let the backend take care of their side.

Alexey: Michelle will investigate what is easiest for them.

Mark: We don't need to overspecify how its presented.

Roy: +1, should we talk about reorganizing IANA registries in general. Each registry has a different style of title and organization. It would be nice if we had one HTTP section in IANA.

Alexey: Typically docs don't tell IANA how to structure it. You can usually just talk to IANA.

Mark: But we want to put URLs in our documents.

Alexey: I don't know if they are happy to have URLs in drafts.

Mark: In principle, I think that if we can harmonize the registries, it would be better. We need redirects as well. I think we can even rename them. I'll talk to Michelle.

Action: Open an issue about registrations.

### Issue 39

Julian Reschke: I don't disagree. But I don't think it helps with the confusion.

Mark: We may need more conversation.

Ori Finkleman: This issue comes up in streaming video clients. Many clients don't properly resolve relative references after redirects. Talking to CDNs that use HTTP redirect, they have issues with many clients. Clients think thye are following the RFC. We need to know what the correct way to resolve these references is. If we can get consensus on a single interpretation, we can work with clients to fix it.

Roy Fielding: We don't define the behaviour in the HTTP RFC, it's defined in other RFCs.

Patrick: It took a long time to figure out what RFC to cite, so some helpful information in core may produce more consistant implementations.

?: The confsion is about what is the base URI for a manifest referenced from HTML. The issue is about whether something referenced from an embedded reference gets which URI.

Action: ?

### Issue 34

Roy: There's no way we will replace this with URL Specs. It's neither suitable for the IETF nor is it correct. We can still learn from it, though. This issue came from a bug reported to Mozilla about double-hash signs are being removed from identifiers.

Mark: I will attempt to channel Ana: I think the reasoning is that because locaiton headers are arguiably under control of more authors, you need better defined error handling. URL handls that. It's not my argument, though. Does anyone have warm thoughs about this?

We could reference the URL standard informatively, but that would be strange.

Patrick: That would indeed be strange.

Roy: We could describe how to handle "invalid" messages that go outside the defined grammar.

Mike: The bigges issue is using percent-encoding thigns that aren't allowed? We could maybe improve the text about that.

Action: Consider addding some informative text about error handling.

### Issue 30

Martin: I don't think we need to rely on the fact that some implementations allow more to make the decision.

Piotr: Nginx does not allow underscore.

Mark: I put in underscore, but maybe we should disallow it.

Martin: I suspec anyone usign CGI Environment variable will reqrite dash.

Mark: Period and plus seem useful.

Martin: With two non-digit, non-alpha, you can base64.

Mark: Dash, period, digit, and alpha? Should we require things to start with digit or aplha.

Martin: That seems a good idea. But there are a number of languages that this gets mapped to that suggest that we should start and end with alpha and digit.

Roy: Are we changing the normative requirements here?

Mark: No, just the registry. We can change the registry rules and allow implementations to decide for themselves what they accept.

Martin: The concern is that if folks reject whole messages because of "broken" headers, we'll cause interoperability concerns.

Mark: But we're not prohibiting these headers.

Martin: We need clarity around the expected behaviour.

Patrick: The registry should reflect best practices.

Mark: We can define the "safe" area and if people go out of it, there is error handling.

Roy: We can split the spec into obsolete and recommended, but changing the ABNF is a big change.

Patrick: This might cause collateral damage in compliant implementations.

Roy: We could write the rules so they only limit the registry.

Roy: We could split received and sent ABNF that are different. But that's not great. Implementations already have to accept what they get and do error handling from there.

Martin: Can we get some information to help make the decision? What do implementations actially do on chars outside the norm? What chars are used in practice? Some folsk can actually measure these things.

Mark: We would get information all over the map, I think. Also public traffic is very different than private traffic happening behind firewalls.

Piotr: Nginx rejects the entire request with bad headers.

Patrick: Filter on respinses?

Piotr: No idea.

Patrick: I'm worried about "SHOULD NOT generate" will cause second order effects. I would like Core to clarify and increase interoperability. I worry that this would only produce the former.

Mark: I'm concerned that we can wind up with a scneario where we have headers that are in use cannot be registered.

Mark: Data wouldhelp. What is the set of things that cause interop issues?

Jonathan Lenox: Registry is expert review. Maybe experts can discourage strange chars unless they are particularly useful.

Mark: But it would be good if we had more than a registry issue.

Action: No consensus.

### Issue 22


Roy: The issue with clarifying it for TCP is that HTTP can run across lots of things, so it's difficult to describe it in a sensical and accurate way for HTTP over just TCP.

Martin: We recently recornized the same thing about TLS. It used to be the case that we didn't recognize half-closed, but we've corrected that.

Roy: That's a great improvement. If we have text that makes sense, I'm not opposed to putting it into the spec.

Patrick: This is a real operational issue. Most of the time, the client is actually gone, and we wind up waiting a really long time for a client that doesn't want data.

Mike: I've encountered this before. I think "half-closed means nothing" is the right answer.

Ted Hardie: It sounds like the issue is exacerbated by NAT and should have a v4 v6 distinction.

?: I'm not sure what the use case for this is. Couldn't we use Connection: close. Why would half-closed be useful?

David S: I don't think there are apps that do this for operational reasons. Still... I think it makse sense to have guidance. You can save resources with this. If you know new requests aren't coming in, you can save resources.

Eric Kinnear: This make ssense for HTTP1. But in the H2 world, we have different expectations. "half-closed means nothing" may be the safer answer.

Mike Bishop: I think it's harmful to clients that half-close to not send them the data.

Patrick: But... which clients? I think in practice, half-closed almost always means the client has gone away. I'd like to have information about specific clients.

Mike: In H2, it discusses half-close, but recommends against it. I'll go collect information about which clients do this.

Action: Collect information about client behaviour.

### Issue 16

Action: Improve wording.

### Issue 10

Roy: I push back on changes because I want to reduce the number of changes and ensure they are all important.

Pete: Do we make special dealing with other magical special names like localhost?

Patrick: No.

Pete: Then why this one?

Patrick But that's a good idea.

Pete: Just .onion doesn't seem a good choice.

David Schinazi: These reseved names belong in DNS. Maybe we can make comments to point at the Special Use Name registry.

Ted Dardie: People are encouraged to put these special use names under .arpa. This seems like a reasonable sweet spot.

Mark: Would a reference to 6761 work?

Ted: DNS doesn't love the current framing, so it would be better not to reference 6761.

David: I'm going to contradict mtself. HTTP isn't a DNS client. If your HTTP engine makes a query for .onion, the DNS resolver is what needs to know.

Mark: But 6761 answers this.

David: My bad.

Pattrick: We can poit to some requirements on HTTP in the DNS lookups.

Action: Mark wil work on some text.

### Issue 132

Roy: I think HTTPD uses a second resolution timestamp for a weak etag and upgrades to a strong tag when the second elapses.

Bron Gonwana: We have an implementation that needed to provide a weak etag that then upgraded to a strong etag when we were cetain the data wouldn't change. The etag we use is a SHA-1 of the content.

Roy: Folks mostly ignore this and take the chance that we have a bad answer.

Action: Look into this.

### 304 Cache Updates

Mark: Looking into how 304 updates cached headers. There are major variations in how these are handled. In broswers, they update cached resposnse with new headers, but they exempt some headers, including those that include Content-, which includes Content-Security-Policy. I'd love a chat with browser vendors. I've got bugs open with browsers and they are all looking at each other's implementations. Proxies don't like updating headers on disk for performance reasons. Maybe we should recommend against 304s? Please talk to me about it.
Patrick: Is there an issue open?
Mark: Nope. We do need to figure out which headers should be exempted. And if proxies won't update headers... are we stuck?

### Security Implications of Shared Compression

Murry Kucherawy: I'm working with Facebook and elsewhere that have to do with compression dictionaries. I want to collect all the information about compression dictionary security concerns into a single document that can serve as a checklist for future authors. If you have information for this doc, please let me know.

## Administrivia

(applause for Tommy)

## Active Extension Drafts

### CDN Loop Prevention

MT: deployment experience with CDN loop prevention?

Mark: Fastly has implemented and deployed the extension.

Chris Lemons: Has interest in deploying the extension.

Nick: Cloudflare has plans to implement very soon.

### Variants

Chris: Registry with extra data is better than more registries.

MT: What's the argument for doing this at all rather than relying on definisions of header fields?

Mark: Registry collects the knowledge in one place. Could we create extra column in header registry?

MT: Same concern. Existing registry or not, it's still overhead.
Put this in a wiki in GitHub as a non-normative reference?

Ted: Unclear on level of granularity. Is the point here to give folks an opportunity to disclose cookie semantics, or something else?

Mark: If we can describe a set of functions that are useful, then folks can use it, otherwise folks can fall back to a variant.

Ted: Who would update their tooling based on this cookie change?

Mark: Discussions with web developers shows interest.

Thomas: Will issue #549 address scenarios where applicataions cookies override user preferences of accept language?

### BCP56bis

MT: 7230 is fine, and want it to move on. No significant benefit in having it reference core items.

Mark: Core is an entry point into HTTP newcomers.

McManus: 7230 is sufficient for now.

Mike: Finish document off with reference to core.

Chris: Having to between right and fast, would prefer right.

Alexey: Both sides seem valid. Depends on how quickly we want this document published. We can put references to existing documents and leave note to editors.

MT: Pretending that either document will stay the same is a joke. Let's not worry about this.

### Secondary Certificates

Ekr: Want to host Mozilla and Fastly on Cloudflare CDN. Those have no relationship with each other, but use the same connection. In order for this to happen, another certificate extension is needed that says they're hosted on a particular CDN. This is another trust mechanism we've never had before.

Mike: This is what you need for secondary certificates.

RLB: We're changing the way certificates are used, so this requires a decoration of the intended context in which the certificate will be used.

Ekr: Tamarin or it didn't happen. Having trouble reasoning about this.

Mike: Nick has algorithm for tracking which server is valid: build up set of candidate certs based on SAN, subject, and affiliation tags.

DKG: Building up set of names based on SAN lists, and cert has some requires. (?)

EKR: What attack is this intended to stop?

Mike: Attack is where attacker acquires private key to legitimate certificate. Not detectable by CT. This forces you to put a requires reference in a CT-logged cert.

EKR: DNS hijacking is the threat.

Mike: Missisued certificates would cover both domains and coalescing would cover it up.

EKR: This was Sleevi's objection to removing the DNS check from coalescing.

Mike: DNS check is independent of secondary certificates. Don't want to make the situation worse. (?)

EKR: CDN compromise is easiest way to compromise private key -- is there another way to do that?

Mike: Not quite.

Nick: Prevents attacker that compromised a certificate without the CDN name (?). In order to use a secondary cert, it has to have the name of something in the primary cert. Any secondary cert has to have a require that includes a SAN that's on the original connection. Independent site certs without requires cannot be used for coalescing.

EKR: (missed)

DKG: Defense this offers is that these certificates leave in CT log is name of CDN, where attack took place?

Mike: No. Two attacks, one depends on CT log. First case is where attacker requests cert that has no obvious link to them from the CA. This forces reference to site under control.

DKG: Not reference to site under control, but reference to CDN. Breadcrumb is one layer of indirection. Breadcrumbs reduce search space by number of possible CDNs.

Mike: Considering case where compromised cert goes to CDN and uploads under it under their account? CDN would prevent that.

Subodh: Change in security model is that this reduces DNS compromise to the compromise of primary domain. Must compromise DNS in primary domain to attack this proposal.

Mike: If primary domain is comrpomisable then you're no different than in normal TLS.

MT: Do we need somethign simpler? Maybe a flag that says the cert is OK being a secondary. requires:* is this flag, but this goes much further.

Mike: No difference between flag in certs and not doing anything which draft currently says.

DKG: In misissuance attack, the only breadcrumb that this leaves is that the cert was deployed on some CDN.

Mike: Yes, believe so.

DKG: Why don't you need a secondary cert? Can't point DNS at CDN?

### Structured Headers

MT: (#702) perhaps create a different grammar?

Mark: Current spec uses identifier. We could change this.

MT: Don't know if we've managed to maintain lexical distinguishable on the wire.

Mark: Can identify lexographically at the top level.

MT: If we're there then this is probably workable.

MT: In cases where a new header field contains a date needs a number and defines it as a number, and we just live with it for existing headers with dates. First instance that uses the date should be carefully looked at to determine if it's an integer or float so we can use the same type going forward.

Mark: Will probably start working on a draft for this soon.

Piotr: If we want to use numbers, why use ASCII instead of binary?

Mark: Want to create an alternate encoding that can map to HTTP/1.1 but also map to more efficient encodings as needed.

Alexey: Do we need timezones?

Mark: Locked to UTC (?)

MT: (#684) This is an awkward one.

Mark: Might just provide general advice.

Chris: There's no hope for people who mangle headers.

MT: No concrete action needed. Just provide a red flag for people.

Mark: Distributed tracing work is looking at structured headers.

Piotr: (missed)

Mark: Introduce new requirement to HTTP that intermediaries don't concatenate headers?

Piotr: Yes.

Felix H: What percentage of headers are amenable to porting to structured headers?

Mark: A lot.

### Cache Digests for HTTP/2

Kazuho: Assumed browsers would implement before WGLC?

(missed)

### Client Hints

MT: No plans to implement. Lots of things to implement regarding privacy and others. Surprised since I thought this was done.

Eric: Good and interesting ideas, would like to see move forward.

David: Can you send (foo?) to the list?

McManus: Yes.

### RFC6265bis: Cookies

(nothing)

## QUIC and HTTP

Kazhuo: HTTPbis will sign off on QPACK too?

Mike: Yes, I think that makes sense.

Mark: QUICWG deferred naming of deliverable to this WG.

McManus: Two aspects: (1) name, and (2) future maintenance belongs in this group.

MT: Take QPACK along since this group owns httpbis.

Bret: Be wary of market perception, HTTP/3 might cause confusion.

EKR: HTTP/3 does not carry the fact that it's over QUIC, and it implies that we're tired of HTTP/2.

Jana: Signaling is important. This does create a very clear fork.

Eric: HTTP/3 is fine. Long-term, HTTP/2 is explicitly over TCP. HTTP/3 is over QUIC and could be over TCP. Doesn't mean HTTP/2 is not good and not a viable fallback path.

MT: Recognition that we're forking the protocol at every major release.

Mark: When we have a new wire mapping, we have a new version identifier.

Mike: Fork is the fact that we don't obselete the previous version.

Mark: Can't tell people to stop using HTTP/1.1.

MT: (missed)

Ted: WG should think about how transport changes affect semantics changes to http. We've not yet had this discussion.

Mike: Only requirement is that TLS 1.3 or greater must be used as handshake. Might want to be more explicit about versions support things can be used for whatever (?).

Chris: Effectively a marketing decision. Will recommend HTTP/N+1 over HTTP/N if possible to support it.

**Hum: in favor of httpbis owning documents.**

**Hum: in favor of HTTP/3.**

## Proposed / Related Work

###HTTP/2 as Transport - Eric Kinnear

Piotr: Competing proposal to discuss later.

Tommy: Empty headers are not generally compatible.

Mike: Intent for framing layer was that it is separable, and this works.

Subodh: Headers frame might be desirable for proxies to help routing.

Piotr: Need headers for proxy case, which brings us to 8441. Might end up with two solutions.

Eric: Intent is for either endpoint to open up the bytestream.

David: Allows fallback from things over QUIC transport to H2. Setings are in http not QUIC transport. Might need some work.

Woo: Have you considered cases where middleboxes need to shut down the bytestream gracefully? We have GOAWAY now. There is no way for other side to signal to stop using the stream.

Eric: Get into this case if you have a hanging GET.

Jana: (jokingly) should call it HTTP/2++

### Cache Header - Mark Nottingham

Roy Fielding: CDN would be a more specific name than cache as this is not applicable to all caches.

Chris: Very fun to debug things that go across multiple caches simultaneously. Light years ahead of experience. Would be great to be able to stack these. Not just CDNs.

Thomas: Trying to work on this.
