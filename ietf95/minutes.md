<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Minutes from HTTPBIS Session 1, IETF 95](#minutes-from-httpbis-session-1-ietf-95)
  - [Agenda Summary and Administrivia (chair)](#agenda-summary-and-administrivia-chair)
    - [Thanks to Barry for his service as AD](#thanks-to-barry-for-his-service-as-ad)
    - [Welcome to Alexey as new AD](#welcome-to-alexey-as-new-ad)
  - [Specification Status (chair)](#specification-status-chair)
  - [Active Drafts](#active-drafts)
    - [Opportunistic Security (chair)](#opportunistic-security-chair)
      - [Separate Lifetime from Commitment](#separate-lifetime-from-commitment)
      - [Requirement to Filter Alt-Svc Header Needs To Be Explicit Normative Text](#requirement-to-filter-alt-svc-header-needs-to-be-explicit-normative-text)
      - [Commit without Same Host Opt In](#commit-without-same-host-opt-in)
      - [Other Issues](#other-issues)
    - [Character Encoding and Language for Parameters (chair)](#character-encoding-and-language-for-parameters-chair)
      - [Client Hints (chair)](#client-hints-chair)
      - [Define More Precisely Which CH Headers are Sent by Default](#define-more-precisely-which-ch-headers-are-sent-by-default)
      - [Define "Accept-CH" More Precisely](#define-accept-ch-more-precisely)
      - [Should CH Headers be Treated as Simple Headers?](#should-ch-headers-be-treated-as-simple-headers)
    - [HTTP Encryption Content Encoding](#http-encryption-content-encoding)
      - [Key Spec](#key-spec)
    - [Potential Work](#potential-work)
      - [Thoughts on HTTP Header Field Parsing](#thoughts-on-http-header-field-parsing)
    - [Origin Frame](#origin-frame)
  - [Adjournment](#adjournment)
- [Minutes from Session 2, IETF 95](#minutes-from-session-2-ietf-95)
  - [Administrivia (chair)](#administrivia-chair)
  - [RFC6265bis](#rfc6265bis)
  - [Potential Work II](#potential-work-ii)
    - [TCP Tuning for HTTP](#tcp-tuning-for-http)
    - [Client Certificates](#client-certificates)
    - [Secondary Server Certificates (Mike Bishop)](#secondary-server-certificates-mike-bishop)
    - [Cache Digests](#cache-digests)
    - [Decomposing/Disentangling HTTP](#decomposingdisentangling-http)
    - [Merkle Integrity Content Encoding](#merkle-integrity-content-encoding)
    - [Secure Content Delegation using HTTP](#secure-content-delegation-using-http)
  - [Adjornment](#adjornment)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# Minutes from HTTPBIS Session 1, IETF 95

## Agenda Summary and Administrivia (chair)
### Thanks to Barry for his service as AD
### Welcome to Alexey as new AD

## Specification Status (chair)

## Active Drafts

### Opportunistic Security (chair)
(in WGLC)

#### Separate Lifetime from Commitment

Martin: I have trouble wrapping my head around this one.  We should just do this, though with slightly restructured JSON, something along the lines of what Kari suggested.

Mark: Caching gets a little interesting here too.  You effectively need a lifetime for the alternative service without having server authentication.

Martin: Mike's suggestion was to say "The following alternatives have the following lifetime, which require/don't require security".

Mark: Let's take this offline.  It sounds like this is not adding too much complexity.  I'm sensitive to that because we only have one implementer, so we want to keep complexity down.

#### Requirement to Filter Alt-Svc Header Needs To Be Explicit Normative Text

Mark: Seems to be uncontroversial

#### Commit without Same Host Opt In

Basically the same resolution as the first issue.  I think we can then take this to Last Call.

#### Other Issues

Julian: There is one open question that's not in the github tracker, which is the restriction that the opportunistic rquest needs to be over HTTP2, as discussed on the list.  The spec better explains what the problem is than it did before, but it's still confusing to read.
(description of the problem)

Mark: What would you like to see?

Julian: The server should reject opportunistic requests in the case where it's not clear that the code making decisions on the content has the correct information.

Martin: The MUST requirement is of no use to us.  I think with Julian's hand-waving, we're going too far.  I think it's clear where the danger lies.  I think if we can do that, we've achieved our goal here; then being proscriptive about what clients and servers must do here doesn't add any value.  We should articulate the problem and leave it at that.

Julien: The problem is that for the server code it's untestable whether the application running inside the server is broken, so it has to be a conscious decision by the server operator enabling or disabling this behavior.

Michael Bishop: This is a problem for servers.  We know this exists.  If a request comes in, we look at the arriving port and what hosts/resources are configured for that.  It may not be a solvable problem in the protocol spec; if we want to do anything in the document, we need to say the client must use a request form that includes the scheme.  I don't know how many client libraries expose the option to do this, however.

Eric: On the client side, I agree with Michael.  On the server side, the option might remove the need for the MUST.  Most of the server implementations appear to do the wrong thing, so it's not clear how HTTP2 is any better here.

Mark: It sounds like we have emerging consensus.  It strikes me that putting the scheme information in a pseud-header field in HTTP2, hiding it from HTTP, maybe wasn't serving our audience very well; it requires them still to figure out the scheme in a non-standard way.

### Character Encoding and Language for Parameters (chair)

Mark: No open issues.

Julien: I haven't done anything with this since it became a WG item except testing the I-D submission system with some non-ASCII in it.  It still needs some work; I'll get to it maybe next month.

Mark: It's mostly editorial work.  We can come back to the WG when there are specific questions.  Hopefully it'll just go along quietly in the background.  Do you think we could WGLC during Berlin?

Julien: Before.

#### Client Hints (chair)

Mark reviewed the issues list from the tracker.

Ted: Could "Save Data" be split off into a separate header field?  (a new issue)   The willingness to do this particular thing is not limited to particular methods of delivering that savings.  There are a couple listed, and some might be significantly different from others.

Ted will raise this as an issue in the tracker and on the list for discussion.

#### Define More Precisely Which CH Headers are Sent by Default

Mark: Pretty straightforward.

#### Define "Accept-CH" More Precisely

Mark: Need to explain more clearly the scope of this option.  Ilya says this can be resolved by plumbing in the HTML and FETCH specifications.  We shouldn't have to think about this much more.  I know it seems weird to have some of this in one spec and some in another but it seems to be how these things are going.

#### Should CH Headers be Treated as Simple Headers?

Julien sent a pull request.  Ilya will reiew the proposed changes.

### HTTP Encryption Content Encoding

Mark: We need advice from CFRG about the crypto choices made in this document.  Martin, please get other helpful reviewers to take a look at this aspect of it.

Martin: That's the only issue as far as I know.

Everyone was looking at Alexey.

Mark: We were also talking about doing signatures; should we hold this up for that?

Martin: They're orthogonal, so no.

EKR: Imposing encryption and signature is not a straightforward proposition.  Which composition do you envision for these?

Mark: These are building block specs, so...

EKR: I don't think you can advance those independently.  You can do them together, or drop one of them.

Mark: What impact would this have over in WEBPUSH?

Martin: It would be the long pole holding us up.

Mark: How long, estimate?

Martin: Let's talk about it offline.

Mark: We have serious concerns with this spec, and that's as far as we can go at the moment.

#### Key Spec

Mark: We've been working on this for a while, and the remaining issues are relatively minor.  We've done a lot of work to make this easy for an intermediary to implement, but we don't have news that there are implementations.   We should make sure we're on the right path before advancing.  Right now you have to do a double lookup.  The preliminary feedback from implementers is that they would love not to have to do that.  Are there any implementers in the room with feedback?  Without that feedback we have to sit on this spec.

Julien: What's the issue exactly?

Mark: Most intermediaries cheat and don't implement the whole current spec because of the horrible performance impact.  As a result of the choices we've made here, we have to embody the performance optimizations they've made.

Julien: So Key will be too complex?

Mark: Complex is okay; doing lots of syscalls or unbounded computation is not.

Julien: I'm trying to understand why you'd do more work besides parsing for Key.

Mark: A proper implentation of the existing spec would not have a problem, but I don't think there are any.

Mark: Let's take the discussion offline.

### Potential Work

#### Thoughts on HTTP Header Field Parsing

Julien: "Again?"

(slides, mostly the same as what was presented in Quebec City and Toronto)

Mark: I think there's pretty broad agreement that there's a problem needing to be solved, which is that Julien is a single point of failure in terms of HTTP header review.  I also hear people uncomfortable with JSON, but I think we should start with it just to get something done.  JSON pointer might be a problem for performance reasons.

Erik: In the HTTP2 context, you'd have a direct mapping from JSON to CBOR.

Mark: That's what we were referring to before; it's a big long term win.

Jeroen: If you have an engine that wants to make decisions based on headers, you'd have to look at data types of certain values.  "Date" is really annoying.  Having a way to do binary comparisons is great.  Not all implementations use JSON.

Mark: We have to pick something.  Or make something, which is scarier.

Mark: Call for Adoption of this is basically done.  If people have further thoughts, please make them on the list or talk to me.  Julien is available to edit.

### Origin Frame

Mark: Call for Adotion is open.

(slides)

Patrick: I'm in favor of expansion of this document in general, and we certainly should adopt it.

Nick: I think this is an interesting thing we should advance.  We should do <something> separate from the Origin Frame work, however.

## Adjournment

Please review the Part 2 schedule and drafts before the second half of the meeting later in the week.




# Minutes from Session 2, IETF 95

## Administrivia (chair)

## RFC6265bis

Martin: What proof to you have that you'll bust everyone else like at Google?

Mike West: Blizzard looked like the next most vulnerable, but they were willing to change behavior.  We need to tread carefully, but I think something can be done here.

Richard: The leave-cookies-alone I'm in favor of.

Mark: Talked to a few people about cookie prefixes, and the only one that has done anything used a lot of __*.

Mark: Richard and Mark are ok with same-site cookies,

Richard: The default in CORS is closed (same-origin), and we do something safer -- you have to opt-in.

Mike West:  It is radical, but we can discuss it.

Martin: Changing the lifetime on cookies without the secure flag could cause severe breakage.  If we treat cookies over insecure connections as ephemeral, we might not break much and still cleanup cookies.

Richard: It can be worked around by setting it on HTTPS and reading it over HTTP.

Mark:  I've heard of this approach in a number of contexts.

Martin: In this safe environment, a MiTM might still have a difficult time.

Mike West: It is interesting, but I'm concerned about the approach because how 'session' is defined is fluid.  A hybrid approach might be workable.  Another might be to use a form of combined cookie.

Mark: Convincing everyone to change how they use cookies to get what we want to combat pervasive monitoring is probably too high a bar.

Eric: One thing that sites have used to prevent tracking is to store a persistent cookie.

Martin: There are events the browser can detect to try and use to address this problem.

Eric:  I wonder if the CSP cookie scope is worth tracking in relation to this cookie lifetime work.

Mike West: People are supportive of the draft, but I'm not sure if many have thought about implementing it.

The working group is not objecting to its ability to make progress on solving the cookie issues.  There will be calls for adoption of cookie prefixes and same-site cookies, and look forward to drafts on cookie lifetimes.

## Potential Work II

### TCP Tuning for HTTP

Aaron Falk: Send a note to TCM and Transport about this work.  Getting more cross-area review would really benefit this work.  I would be happy to help review it if adopted here.

Patrick: I'm in favor of this work, but it needs to talk more about the impacts of various network pieces more than how to configure your servers.

Spencer Dawkins:  A lot of the related documents are Experimental, and it would be great if they can advance.  We've done cross-area sharing before with success.

Barry:  There's some discussion happening if this work belongs here or in Transport.  Wherever it is done needs significant help from the other area.

Bryan:  I'm in favor of this work, and have a related document I can share.

Barry: Don't worry about the category of other documents.  The AD can deal with that.

Chair will discuss with Transport area people to find the right way to get TCP Tuning done.

### Client Certificates

Mike Bishop:  We shipped something proprietary to meet needs, but would be really happy to change to a standard.

Kazuho:  This is the simplest way to solve the problem, and we should do it.

Mark: We could adopt, knowing it won't get feedback in a long time.

Mike Bishop: I think it's worth adopting to help drive development.

Martin: I also think it's worth adopting even if it's abandoned later.

There are no objections to a call for adoption on client certificates.

### Secondary Server Certificates (Mike Bishop)

Martin:  Another advantage is that the alternative is a cert with lots of SANs which are much much bigger; being able to server a smaller cert makes things faster.

Patrick: Are these deltas to the client cert extension or its own thing?

Mike Bishop:  This was originally written as an extension to the client certs draft, but we can move things around so it stands alone.  Also, this and client-cert could be the same draft.

Patrick:  I think it's worth doing both.

Nick: I strongly support.

Martin: the only problem is the potential to capture, but it's a small worry.

Mike: The current requirement involves matching on DNS, and this removes that.  We could still rely on DNSSEC, or push down a proof.

Richard: How do I figure out how to send the cert request for a new connection?

Mark:  This was talked about on Monday.

Richard:  I think the negotiation conerns need more discussion.

Mike: The draft does not currently talk about session resumption but you probably could do it without pushing the certs again.

Mark: At the time, the thinking was SPDY was enough and more complexity was not needed, but that might be different now.

Eric: Another idea is to have a separate record in DNS to look up for validation against.

Mike: The server can opt-out using a server frame.

Martin:  We should all for adoption to adopt both client- and secondary-server after Mike and I merge the documents.

Mark: The proposed work is a combination of the two with advice from the Security area.

The working group supports a call for adoption of the client- and secondary-server certs documents.

### Cache Digests

Martin:  I believe browsers already flush caches when you flush a site.

Martin: We need more discussion as a frame, since there might be collisions with multiple caches.  You are assuming there is only one cache, and that's not likely the case (think intermediaries).

Mark: The cache is hop-by-hop.

Bryan: I like it as a frame, and allow the server to request it to get a sense of what the client has cached.

Mark: It can help if you need to drop 

Martin:  I'm happier with these answers, but a note should be added that it could be done with a header to expidite experiementation.

Mark: It's moving 

Leif: What if the server doesn't do push?

Mark: There would be an indicator.

Martin:  We have afix in TLS 1.3 that allows the server to speak first.  Firefox would then see about sending the cache digest only if we have a reliable indication that the server supports it.

Eric: What about the server being able to indicate its limits?

Martin: There is benefit for a client to be able to ask, such as false positivies being 1/6 then maybe I can take the hit for a larger table to get false positives 1/1000.

Mark:  A balance would need to be struck.

A short call for adoption will be issued, with a third party to help judge consensus.

### Decomposing/Disentangling HTTP

Tim: Work happening in DNSOP for running DNS over HTTP (over TCP or UDP).

Mark: A lot of different working groups use HTTP as a transport.

Eric: This is very interesting work we should continue to provide better semantics.  The DNS work is really DNS over the HTTP framing to get the same transport semantics in HTTP.

Ian Swett: There is certainly an effort to clean QUIC up before standardizing.

Martin: We need to think very carefully how we use HTTP.  We should continue the conversation, but I don't think we need another RFC for this.

Mark: I think we should let it sit around and think more on it.

### Merkle Integrity Content Encoding

Richard: Has there been any implementation or experiementation?

Martin:  We needed a better solution to the current SRI, and I have a prototype.

Richard:  Firefox is interested in this work, mostly internal now but some with wider scope.

Eric: I like it and have lots of use cases for it.

Natasha: I think this is interesting from a W3C perspective.

Mark:  Please look at the draft -- there's been lots of interest over years.

### Secure Content Delegation using HTTP

Ian: There is a prototype -- would it move into the browser?

Martin: Using ServiceWorkers for this interferes with other uses of ServiceWorkers, so we would look at moving into the browser eventually.

Ian: The implication is that the integrity is maintained with the delegation.

Nick: Does this work if it's not TLS the whole way?

Martin:  The primary request is end-to-end, but the secondary don't need to be.

Eric: This could help with HTTPS adoption for large CDN usecases.

Martin: This might be a better solution to LURK.

Thomas: This can be resource intensive for the CDN.

Martin:  You're operating as a proxy, so you've signed up for that.  The client could just talk directly to the origin.

Martin: The client discovers this delegation through MAGIC!

Mike Bishop: I have seen a lot of interest for this in SMBs more so than the browsers.

Martin: I'll need to talk to higher ups about sharing the implementation.

## Adjornment

---

* [Content Security Policy: Cookie Controls](https://w3c.github.io/webappsec-csp/cookies/)
