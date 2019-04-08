
# HTTP Working Group Minutes - IETF104 Prague

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Monday - HTTP Core](#monday---http-core)
  - [Issue #203: Expect should be a list header](#issue-203-expect-should-be-a-list-header)
  - [Issue #202: Tighten language around GET and DELETE request bodies](#issue-202-tighten-language-around-get-and-delete-request-bodies)
  - [Issue #165: Updating stored headers](#issue-165-updating-stored-headers)
  - [Issue #137: Serializing a header line](#issue-137-serializing-a-header-line)
  - [Issue #128: Quoted cache-control directives](#issue-128-quoted-cache-control-directives)
  - [Issue #120: Status codes and caching:](#issue-120-status-codes-and-caching)
  - [Issue #111: Header terminology](#issue-111-header-terminology)
  - [Issue #54: Method registry should include cacheability](#issue-54-method-registry-should-include-cacheability)
  - [Issue #51: MIME sniffing](#issue-51-mime-sniffing)
  - [Issue #30: Field-name syntax](#issue-30-field-name-syntax)
  - [Issue #22: Clarify rules around half-closed TCP connections](#issue-22-clarify-rules-around-half-closed-tcp-connections)
  - [Issue #7: New header field considerations: list vs keyword](#issue-7-new-header-field-considerations-list-vs-keyword)
- [Thursday - Extensions and Proposals](#thursday---extensions-and-proposals)
  - [Variants](#variants)
  - [BCP56bis](#bcp56bis)
  - [Cache](#cache)
  - [Client Hints](#client-hints)
  - [Structured Headers](#structured-headers)
  - [Secondary Certificates](#secondary-certificates)
  - [HTTP/3 & QUIC](#http3--quic)
  - [Proxy Status](#proxy-status)
  - [HTTP/2 as a Transport](#http2-as-a-transport)
  - [Stateful Compression](#stateful-compression)
  - [Protocol to origin](#protocol-to-origin)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Monday - HTTP Core

### Issue #203: Expect should be a list header
Decision: proceed

### Issue #202: Tighten language around GET and DELETE request bodies
Clarity is desired, but doesn't necessarily exist at present

Is DELETE like GET or OPTIONS in this regard?

Decision: strengthen GET language, open separate issue to discuss DELETE

### Issue #165: Updating stored headers

Mike Bishop: if the body hasn't changed, the interpretation shouldn't change. Use that as guide for building list of headers to exclude.

Alternative to defining special treatment for these headers (beyond the connection-oriented headers): recommend responses that include them also be marked uncacheable.

Decision: categorize these headers into buckets with different solutions (pursue browser/client/caches behavior reconciliation)

### Issue #137: Serializing a header line

Decision: close with no action

### Issue #128: Quoted cache-control directives

Decision: more testing

### Issue #120: Status codes and caching:

Decision: continue discussing

### Issue #111: Header terminology

Proposal exists on issue

Add definitions for existing colloquial terms

Add examples

Decision: continue discussing

### Issue #54: Method registry should include cacheability

Decision: ???

### Issue #51: MIME sniffing

Decision: merge proposed language into spec

### Issue #30: Field-name syntax

Decision: gather telemetry (from browsers, servers, and HTTP archive)

### Issue #22: Clarify rules around half-closed TCP connections

Consensus exists to clarify

Proposal: clients SHOULD NOT early-FIN, servers are discouraged from aborting on client FIN

Mild consensus exists to accept proposal

Decision: discuss reservations on PR

### Issue #7: New header field considerations: list vs keyword

Decision: write recommendation for new headers


## Thursday - Extensions and Proposals

### Variants

Roy: Why Variant-Key exists instead of reading the header fields in the representation?

Mark: Because the key can diverge from the contents of the header fields.

### BCP56bis

Ted Hardie: Using application-specific media type in Content-Type to indicate it's not a browser might be used for fingerprinting applications by proxies.

Mark: Is a reverse proxy acting on behalf of the origin still part of your treat model?

Ted: For the Privacy section, what I'm suggesting is to add text saying that anything on the path, whether it's proxy acting on behalf of the end-user or the origin, will know which of those applications is using HTTP substrate.

Mark: I'm going to push back, because I think what you're really saying is that if you don't encrypt the data, then anything on the path can see that data, and that's true for the URI, that's true for the headers, body. MIME sniffing is well documented and widely implemented, and even if you use a generic media type, then proxies will still understand what application you're using.
 
### Cache

(issue #777 - header name)

Alessandro: Using Cache doesn't seem consistent with other existing headers, like Cache-Control.

MT: This is bikeshedding, pick something and deploy. Renaming header (if needed) is easy.

### Client Hints

MT: We have some reservations about use of the Feature Policy, generally, and there are aspects of it which are not very mature, and some which we don't necessarily agree with.

Yoav: I know that there are some concerns about inheritability of Feature Policies in nested contents, but Client Hints should work fine with or without inheritability.

MT: It might be easier to move forward with this without using Feature Policy.

Tommy: We're interested in being able to mark Save-Data, but not other hints, we have some reservations. Could you clarify what your plan would be for a separate Save-Data?

Yoav: Save-Data would be split into an independent draft, separate from the current network info, so that people can implement it without other network-related hints.

Tommy: Editorial. It might be good to add note about what makes sense to be used as hints.

Mark: Fastly's optimizer team likes the granularity of data to automatically optimize images.

Mark: This is a good framework for a new content negotiation mechanism. This is a good pattern, and let's use it in the future.

EKR: I disagree that this reduces the fingerprinting surface, it removes some things, but it also adds things that were previously unaccessible to the server, like memory.

Yoav: Each of those hints is already available using the JavaScript API, so websites can already retrieve that information one way or the other. This is the same as the already existing active fingerprinting that browsers can  track, block and protect against. But it doesn't add any passive vectors.

EKR: That's not true. It changes active vectors into passive vectors. If something was previously only accessible using JavsScript API, and now it's always sent by the client, then it's now a passive vector.

Yoav: It's not sent all the time, it's only sent on the server opt-in.

EKR: Yes, but it's sent on every request once the server has requested it.

Yoav: Yes, but the servers can do the same with Cookies, query parameters, etc.

EKR: That's using state storage, and browsers are specifically taking action to restrict the state storage, so that's not a good argument.

Yoav: I don't think this adds any new vectors.

EKR: It takes active vectors and turns them into passive vectors.

Yoav: It's not passive vectors, because it requires a server opt-in.

EKR: Once again, there is a difference between what the server does explicitly do vs what is sent on every request. One of the things that we look at, in order to determine whether or not websites are fingerprinting, is to determine whether they are making requests for data that they have no legitimate use for on the client-side, like WebRTC. With this, they can request an array of hints that are then sent to the server and we don't have a way to know how it processes this data, which has a different set of properties than the JavaScript APIs.

Yoav: How is that different from site reading that data and sending it using Cookies?

EKR: As I said, browsers are taking action to restrict the use of state storage.

Yoav: Browsers can take similar actions against usage of the Client Hints for websites that collect many bits of information. Tracking Client Hints won't be more complex than tracking the equivalent JavaScript APIs.

EKR: I don't think that's accurate, because we can tell when the website is making use of the data vs sending it back for storage, but when the website asks for Client Hints and it's sending it back to itself, we have no way of knowing how the data is being used. That's a different situation.

Yoav: How is that different from sending viewpoint with ... to the server?

EKR: If it's doing that regularly, and not making any use of of it, that is something that we would like to look at.

Yoav: ...

Mark: It seems like we're going in circles, and this is coming up fairly often, and some people disagree, so we need to open an issue and find a resolution for it.

EKR: I guess my question would be, has any other web engine indicated that they're going to implement this feature?

Yoav: Not at the moment.

Mark: To be clear, that's not necessarily a bar for us for not publishing it.

EKR: ...
Mark: Yes, but there is the history in this working group of still doing that.

Robin Marx: I just wanted to say that the idea of splitting Save-Data into a separate spec seems really good to me. I see a future when we have more specific user preferences, not just generic Save-Data, but actually users say "I want this type of content" or "I don't want this type of content", so that would make that easier in the future. Please do that.

Alan: Clarification question, will this be sent in all responses from the server or once per origin?

Yoav: Only for responses from the top-level navigation response, so if the server is not sending Accept-CH-Lifetime and it's only interested in hints on subresources then it needs to send them on each navigation response, but if server is interested in having those hints being applicable to future navigation requests, then it needs to add a Accept-CH-Lifetime, and for that lifetime it doesn't need to send them again.

Alan: Should we add those headers to QPACK?

### Structured Headers

(issue #782 - uri reference syntax)

Roy: While I agree that interoperability is a concern, it's a concern regardless of whether we use angle brackets or double quotes. But I don't think you've addressed that kind of concern anywhere else in the spec.

Mark: There is a fairly strong practice of using "sloppy URLs" elsewhere.

Roy: It would be fine if we had a "sloppy reference" instead of a URI reference.

Mark: (jokingly) I'm really hoping this term is going to stick now.

(issue #781 - empty lists and empty fields)

Roy: I don't believe that we need structured headers specification, but if we do, then we shouldn't reduce existing syntax. The Accept header, for example, has a meaning when it's sent with empty value, so having a standard that cannot represent common HTTP headers doesn't make any sense to me.

Mark: The goal of this is to be somehow compatible with common HTTP headers, but more to have a crisp data model for new headers. As for the empty list, you characterize it as a theoretical concern, but it's a practical one, since it won't work on the wire in some circumstances.

(Kazuho and Julien agree to relax this and allow empty values.)

(issue #765 - parameters as a set; ordered vs unordered)

Roy: Variant-Key is using an ordered set.

Mark: It's ordered dictionary, not parameters. So dictionaries are ordered, but parameters are not. What I think we want to do here is make parameters ordered as well.

Jeffrey: A spec that wants to treat all orders as equivalent, it could just say that in the spec, instead of relying on Structured Headers definition.

Watson: You want this to be a list with no repetitions allowed?

Mark: No, it would be an ordered dictionary, which is a popular data structure.

Watson: So that's a list with keys and values and you can't repeat the keys twice.

Mark: That would be one representation of it, yes.

MT: Is it true that you cannot repeat the key?

Mark: That, I think, would be the trade-off, that you cannot have the repeated key.

MT: Is that true for the dictionaries as well?

Mark: For dictionaries it is true, yes.

MT: As long as those two are consistent, go ahead.

(issue #737 - integer limits)

Kazuho: My understanding of PHK's proposal was that he argued for a minimum guaranteed range of 15 digits (instead of 52 bits), not the maximum.

Mark: I didn't get that at all from the conversation. My understanding was that he wants to clamp the number of digits and generate an error if you exceed it, as a way to make sure that whatever you feed the parser is what we think it is. If you don't clamp it to 15 digits then you don't get that property.

Kazuho: Allowing implementations to first check the number of digits reduces the chance of having vulnerabilities, thereby making the minimum guaranteed range the 15 characters makes sense, even if you allow implementations to exceed that range if they know how to handle that.

Mark: Will there be the maximum?

Kazuho: No.

MT: The reason we put numbers in header fields is usually to count things. 15 digits is a lot of things, and we do have limits in other protocols that are in that general size category. It's in theory possible to exceed this number, but you get a pretty long way with 15 digits, and I'm perfectly comfortable with following PHK's suggestion here. Anything more can be worked-around with string-hack or different-type-hack. I don't mind Kazuho suggestion, but then when you think about it, byte ranges that reach this large... Good luck.

Mark: My reaction to Kazuho's proposal is that interoperability might suffer, in places that matter. As a concrete example, if you're running over QUIC, and you want to represent a steam identifier, then you cannot do that with an integer here, but I think I'm OK with it too. Like I said, you can add BIGINT later on.

Brian: My concern is that if the limit is there, then people will implement it lazily and just parse whatever JavaScript natively represents, and there will be some values that are represented as integers (when it fits the limit), and some that are represented as strings (when it doesn't fit the limit), so this is going to get complicated and eventually exciting.

Mark: Did you read the Structured Headers spec? The wonderful thing we're trying to do is that we really, really, really mean it that you must be strict with parsing. We have parsing algorithms and test suites to prove that people are following those algorithms.

Brian: ASN1 has test suites and parsing algorithms.

Mark: Thanks for that nightmare.

Roy: The idea, as I understood it originally, was to simplify the processing of HTTP message handlers by giving them more regular grammar. I do not, under any circumstances, understand why would you need this kind of data in a header field. I can understand having large numbers, having binary values, UTF-8, but very large strings of digits doesn't make any sense to me.

MT: If you happen to have 2^61 QUIC streams and you want to identify them, then you won't be able to... oh well. But when you think about what it takes to get to 2^61 streams in a QUIC connection, then you'll realize that you will run out of packet numbers. It's kind of academic.

Mark: Well, but if I define a header field that's supposed to represent a QUIC stream identifier, then it would be weird not to allow it to represent the entire range.

### Secondary Certificates

Watson: I don't think I understand the issue with misissued certificates.

Mike: The issue here is that without Secondary Certificates, if someone issued a certificate that jointly covered victim.com and attacker.com, then victim.com owner could monitor CT logs for misissuance, find that certificate and get it revoked. The difficulty with Secondary Certificates is that you no longer have to put attacker.com in the misissued victom.com certificate.

EKR: I'm just trying to think through the first defense that you're proposing. So the way I understand this works is, in a trivial version, it would have a list of approved domains, to protect against stolen certificate, but then you'd need to go to the DNS for the primary?

Mike: ??? yes

Nick: does requires=* bypass ability to track stolen certificate?

MT: it does.

Nick: disallowing requires=* (requiring domain), would also protect against stolen certificate.

Nick: for some types of certificates (signed exchanges) there are more requirements that make it harder for misissue,

MT: I like the CAA, the simplification is to remove requires=*, not sure what it's providing?

Mike: it helps with the customers to bring their own certs. Without it, CDN would need to issue separate certificate for each customer.

MT: CAA record can include the CDN in it, so it can issue certificates for that CDN.

Mike: ???

Watson: confused why misissuance is a problem of servers and not of CAs. They should be already be protecting against them. Worry about mississuance, but there are bigger issues.

MT: yes, people can hijack BGP, etc. There are lots of records that are produced and auditing might be hard without all the context. One of the principles driving this is that if I'm the owner then I can audit and monitor this. Defense in depth.

EKR: confused about why requires=* if we need the 

Nick: the situation is that there are multiple primary sites, each of them can thousands secondary sites. 

EKR: what I'm suggesting is that you need to 

MT: you might arrive one of 1000s certificates, in order to client to add CDN.com to list of certificates it's good for, then it needs 

EKR: ??? just treat the proof that you have the ???

### HTTP/3 & QUIC

(re URI scheme)

MT: it turns out that H3 always inspred to always ... The question is whether it's the domain we should be sending this request to? With domain fronting, it's possible to send any SNI to ???  Host header field can be used to handle the request. The certificate is good for all the TCP ports (and UDP ports), so the question is whether we want to allow this? Coauthorative is the only answer.

EKR:  Couple observations. (1) Various URI options, any one of those is not backward-compatibile is non-starter. No-one is going to support httpq://, is it reasonable to just try QUIC without any extra indication? Connection coalescing means that we give up on the idea than anything else than TLS certificate matters. Just use https:// for QUIC? 

Ted Hardie: tried httpq:// for other protocols, it was a complete disaster. Don't do that. We might do Alt-Svc in the other direction for dual-stack.

Mark: Go back to RFC7230, the word "potential" is very important. It doesn't mean that we can't do the happy eyeballs (dual-stack). We may add another DNS record?

Ian: option 2 is undeployable. Would be interested in other DNS / Link other attributes. Don't mess with the URI.

Igor: don't break the internet. QUIC is very young, so there might be problems. Let's not do happy eyeballs.

Erik: for QUIC-only clients maybe it's worth looking how to indicatie QUIC connection, for the web case, then DNS scenario might be worth looking at. DNS people suggest SRV record?

Lucas: the Alt-Srv option could be used to load-balance and redirect traffic to different QUIC endpoints. re DNS there no fallback?

Roy: dual-stack seems to be allowed by RFC????. Is the result compatibile with social requirements (authoritative and encrypted), then relying on the certificate is fine, and then server needs to have control over both TCP and UDP.

Eric: ??? agrees with EKR

Toma: UDP connections to 443 are signal of DDoS, and it might result in false positives.

### Proxy Status

Alessandro: We have some uses for this, interested in working on this and adopting.

Roy: rename Cache to Cache-Status.

### HTTP/2 as a Transport

No questions.

### Stateful Compression

No questions.

### Protocol to origin

No questions.

