# HTTP WG May 2020 Interim Meeting Blue Sheets

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Session I](#session-i)
  - [Priorities](#priorities)
  - [Client Certs](#client-certs)
  - [Colm Divilly /  User Defined Resource Error HTTP Status Code](#colm-divilly---user-defined-resource-error-http-status-code)
  - [Session I Blue Sheet](#session-i-blue-sheet)
- [Session II](#session-ii)
  - [Signing HTTP Messages](#signing-http-messages)
  - [Secondary Certificates](#secondary-certificates)
  - [Digest Headers by Lucas Pardue](#digest-headers-by-lucas-pardue)
  - [Cookies 🍪](#cookies-)
  - [Advisory Content-Length for HTTP by Mark Nottingham](#advisory-content-length-for-http-by-mark-nottingham)
  - [Session II Blue Sheet](#session-ii-blue-sheet)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Session I

_Scribes: Robin Marx, Martin Thomson_

### Priorities

* Presenter: Lucas Pardue
* [Draft](https://tools.ietf.org/html/draft-ietf-httpbis-priority)
* [Slides](https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/priorities.pdf)

LP: Main points we'd like feedback on:

- how to do interop testing of priorities?
- how to signal priority on the wire: frames vs headers (currently: default priority is via headers, priority update is via frame). Why not use both? (have to support both either way: "misbehaving" clients + reordering)
- open PR 1167 that gives frame proper place in the text
- if there are frames: how do we manage versioning in the future? How do we diagram H2 and H3 frames in the same document (editorial, issue #1096)? 
- issue 1056: what is the default priority of a Push?

MT: are we assuming we need reprioritization? I thought that was in contention

LP: don't have slides for this, but good point. Should discuss that during the meeting. Would help prevent the need for a frame though. 

Ian: Chrome's behaviour today doesn't violate normative text in H3 at this time: reordering makes handling of frame-before-header necessary anyway.

Ian: to MT: design team feels reprioritization is important. Already used + there are other use cases that are compelling. Would prefer not to re-visit that decision and keep it in-scope. 

MT: just because people are doing it, doesn't mean it's good. Not seeing evidence that this is necessary. Is lots of complexity involved in managing two things that aren't synced. Want to assess it's really needed (we also "needed" dependency trees, look where that got us)

MT: would like to see: evidence this has material improvement for some class of application + that servers would be willing to implement it (not just Google servers, but more in general) + that it works when a random person implements it

LP: outcome of that decision will impact this headers vs frames debate heavily. Don't have answer to usefulness for reprioritization. From implementation experience: seems easy enough to parse and adhere to re-prioritization signal, though we don't do that yet. 

Kazuho: we have implemented PRIORITY_UPDATE: bit of a pain to buffer this when reordering happens (though that happens in H2 as well). Not more complicated than H2 and other aspects are simpler than H2, so overall much simpler than H2. 

LP: let's continue with slides and keep this in mind for later

MT: how do you account for resource allocation here? Layering issues: in terms of knowing if a particular stream is allowed or not and Push IDs etc. Is that considered in PR 1167? 

LP: Was planning to do that, are some TODOs/early text around that (especially around Push, also update for stream beyond max FC limits). In my experience: no layering violations, as application is in control of limits it asks transport lib to manage on its behalf. 

MT: concern was about case where you have a stream budget you expect the transport to manage, but have no idea where it is with that. Then if you get a PRIORITY_UPDATE, you need to cross to the transport and see what the state is, so = layer violation. 

LP: based on old PRIORITY frame, so I'd say layering violation was always there. 

Tommy: (as individual) shouldn't assume relationship between app and transport is so directly managed wrt stream limits (e.g., app sets rough allowed "window") 

LP: maybe that's some general feedback to give to the H3 document beyond priorities, will take that into account.

LP: Which option for having different frame types across priority drafts? Option 1 = tie to H3, Option 2 = presented in presentation (separate weird frame types, later settle on the final ones)

Jabber: use a Transport Parameter to indicate which priority scheme is used? 

LP: Long term issue, again a possible layering violation though...

Ian: Option 2 is probably the right option

MT: Upside: implementations would be more tolerant of random junk if we send it. So option 2 is better for that too. 

MT: wrt diagramming issue: is an editorial issue

LP: have a slide for that! Options: a) use ascii for H2 and new format for H3  b) pick one  c) define only payload   d) Other suggestion

Mark: probably best taken to the list, risk of bikeshedding

No takers on the issue about default priority on Push (#1056)


### Client Certs

* Presenter: Brian Campbell
* [Draft](https://tools.ietf.org/html/draft-bdc-something-something-certificate)
* [Slides](https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/client-cert.pdf)

mnot: are there any questions that might inform the decision about whether this might be adopted; 

ekr: if the people who want this are willing to deal with the fanciness of the potential solutions to this problem, the answer might be yes; if they are not, then the answer might have to be no

brian: maybe yes, but want a sense of what others think

mnot: we should probably talk about this on the list more

brian: we seem to be in a deadlock currently

mnot: chairs should talk


### Colm Divilly /  User Defined Resource Error HTTP Status Code

* Presenter: Colm Divilly
* [Draft](https://tools.ietf.org/html/draft-divilly-user-defined-resource-error)
* [Slides](https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/user_defined_resource.pdf)

Martin: how do you distinguish between the different entities?  THis externalizes some of the state of the server implementation.  How does the client care about this.

Colm: Yes, but this fails safe.  (many more words, sorry)

Julian: it is possible to reject the creation of broken resources in the first place?

Colm: not always; these are not always created using HTTP, they might use proprietary interfaces

mnot: agree with Martin about how it is unclear who generates the message (was this user code or infrastructure, which leads to proliferation; this is orthogonal to the core reason for the status code; I might prefer that a header be defined for this

colm: how do you deal with the fact that headers aren't typically captured

mnot: when you standardize, that does tend to result in things hitting logs

cory b: there is prior art here with 502 (gateway timeout), the same problem applies there, but this doesn't necessarily strike me as a problem that needs to be solved in HTTP, rather it is something for the infrastructure provider to address; other clouds provide monitoring and logging for this

colm: in summary: preference for a header, is there any appetite for a header

mnot: out of time, but maybe


### Session I Blue Sheet

* Barry Leiba, FutureWei
* Colm Divilly, Oracle
* James Gruessing, BBC
* Patrick McManus, Fastly
* Robin Marx, Hasselt University
* Cory Benfield, Apple
* Bence Béky, Google
* Roberto Polli, Italian Digital Transformation Department
* chi-jiun su, hughes network systems
* Julian Reschke, Greenbytes
* Martin Thomson, Mozilla
* Lucas Pardue, Cloudflare
* Mark Nottingham, Fastly
* Magnus Westerlund, Ericsson
* Tommy Pauly, Apple
* Kazuho Oku, Fastly
* Hiroyuki Goto, Gree
* Eric Rescorla, Mozilla
* Mike Bishop, Akamai
* Brian Campbell, Ping
* Ian Swett, Google
* Ken Murchison, Fastmail
* Daniel Stenberg, wolfSSL
* Alessandro Ghedini, Cloudflare
* Roy Fielding, Adobe
* Michael Richardson, Sandelman Software Works
* Felix Handte, Facebook
* Dmitri Tikhonov, LiteSpeed Technologies
* Chris Box, BT
 
 
 
## Session II

_Scribes: Peter Wu and Justin Richer_


### Signing HTTP Messages

* Presenter: Annabelle Backman
* [Draft](https://tools.ietf.org/html/draft-ietf-httpbis-message-signatures)

Annabelle Backman:

- identify parts to sign
- sign them
- attach signature to an HTTP message
- been adopted as a WG item, converted to MD, -00 draft available
- feedback on an incoming change set:
- structured headers; replace bespoke header w/structured headers (Signature-Input and Signature)
- "we're drastically changing the format"
- pull content identifiers into a structured list with parameters
- help headers be durable as more headers/fields are added during request mutation
- multiple signatures (one signature can sign a previous signature header)
- proposal: re-use Signature-Input inner list in the signature calculation

EKR: concern about picking parts of the headers and how that can be secured.

Annabelle: there are many use cases with different semantics and applications. Intention is to provide a foundation for applications to build a solution for signing.

EKR: Picking and choosing what you're signing is weak vs just signing over everything

Roberto Polli: removal of expiration property - thinks it is not a secure choice. Signature is bound to the validity. Properties such as expiry should be included in cleartext with the signature.

Annabelle: expiry is not removed, just not included in the examples in the slides. Expiration is also optional. Will take this conversation to the issue tracker. The reason for breaking it into two separate headers: due to limitations of structured headers, parameters are hard. Multiple signatures are hard to do with structured headers. Please reply to the list for security concerns for separating the two.

Due to running of time, Annabelle will take the rest to the list.

Mark: It's a new draft, everyone be sure to take a look at it

### Secondary Certificates

* Presenter: Mike Bishop
* [Slides](https://datatracker.ietf.org/meeting/interim-2020-httpbis-02/materials/slides-interim-2020-httpbis-02-sessa-secondary-certificates.pdf)

Mike: Concern about lack of client implementations.

Watson Ladd: Cloudflare is interested in this proposal. Offering secondary certificates for subresources in the page.

Mark: considers parking this draft until there are client implementations. There seems to be server interest, but we really need client support.

Mike: Akamai is interested in using it to allow users of client certificates to step up to H2

Mark: Concern about which certificate to use and when; added complexity

Martin Thomson: thinks it's worth doing, but it is weighing cost/benefits. There are other things competing for time, QUIC, etc. It's a bit complicated, not opposed to it, just time.

EKR: wonders about the intended functionality. Browsers don't want to do client certificates in the first place.

Mike: draft was originally written for client certs. Then there was a draft for server certs, then merged. Latest draft allows separately supporting one or the other.

Martin: complexity about getting the UI right is non-trivial. It's relatively easy to fix the TLS and HTTP stack, but the rest is more difficult.


### Digest Headers by Lucas Pardue

* Presenter: Lucas Pardue
* [Slides](https://datatracker.ietf.org/meeting/interim-2020-httpbis-02/materials/slides-interim-2020-httpbis-02-sessa-digest-headers.pdf)

- alignment with newer HTTP terminology (help would be appreciated here)
- how do we handle different methods, including partial representations of request body (still needs discussion)

Mark: I can help with some of those issues, contact us (+Julian)

Roberto: We need some historical knowledge to move forward

Watson: Draft indicates protection against buggy compression, doesn't seem to actually do that as specified

Roberto: content-encoding is property of representation, could be mistaken

Lucas: will take a task to discuss offline and work through scenarios into an issue


### Cookies 🍪

* Presenter: Mike West

Update1: RFC6265bis plods forward slowly; in the fixing small issues stage

- need more platform tests
- majority of issues are around samesite attribute
- support for UTF-8 in header values. Large issue, non-trivial. "important but not urgent", need to decide to spend time on it now or later

Update2: browsers experiment with default behaviors beyond what's specified in the RFC

- SameSite=lax rolled out in Chrome, but reverted in April due to breakage.
- Safari started blocking third-party cookies completely.

Annabelle: Some of these features are tripping up legitimate cross-domain use cases. How much outreach is there to the Identity provider community? How can we keep up?

Mike: Challenge is to maintain the stuff about identity transfer but without the wild-west and its side effects. Main venue seems to be the [Privacy CG](https://github.com/privacycg/).

Martin: This is going to be a moving target; what's the end-point?

Mike: Something like http state tokens proposal for an end state. Suggestions for next steps in [Cookie Incrementalism](https://mikewest.github.io/cookie-incrementalism/draft-west-cookie-incrementalism.html)

Mike: calls out for help to move the draft forward. It's an important issue, but not urgent. If implementations like browsers are consistent, but not documented, that is not ideal.

Mark: Reality is bigger than just browsers

### Advisory Content-Length for HTTP by Mark Nottingham

* Presenter: Mark Nottingham
* [Slides](https://datatracker.ietf.org/meeting/interim-2020-httpbis-02/materials/slides-interim-2020-httpbis-02-sessa-advisory-content-length.pdf)

- leave content-length for message delineation and create a new field for other uses

Mark: is standardizing this header field helpful? Should it be in the HTTP Semantics document, or separate?

James Gruessing: think it is helpful, it belongs to the Semantics doc.

Julian Reschke: if it's in semantics, does it affect the standards level we can achieve?

Mark: it's really just new syntax for an existing feature

Martin Thomson: thinks it is useful for things like progress bars in browsers and chunked encoding or compression.

Barry Leiba: how long would it take for the Semantics document to get out of the door? Can this proposal be added to it?

Mark: pretty soon, but it can become a separate document if needed.

Mark: thinks there is continued interest?


### Session II Blue Sheet

* Tommy Pauly, Apple
* Ted Hardie, Google
* Julian Reschke, greenbytes GmbH
* chi-jiun su, hughes network systems
* Justin Richer, BSPK
* James Gruessing, BBC
* Annabelle Backman, AWS
* Barry Leiba, FutureWei
* Jack J, Google
* Patrick McManus, Fastly
* Alessandro Ghedini, Cloudflare
* Eric Rescorla, Mozilla
* Lucas Pardue, Cloudflare
* Cory Benfield, Apple
* Watson Ladd, Cloudflare
* Ken Murchison, Fastmail
* Martin Thomson, Mozilla
* Chris Wood, Cloudflare
* Peter Wu, Cloudflare
* Alan Frindell, Facebook
* Jonathan Hoyland, Cloudflare
* Mike West, Google
* Hiroyuki Goto, Gree
* Alissa Cooper, Cisco
* Mike Bishop, Akamai
* Gabriel Montenegro, independent
* Roman Danyliw, Carnegie Mellon University
* Felix Handte, Facebook
* Roberto Polli, Italian Digital Transformation Department
* Ian Swett, Google
* Magnus Westerlund, Ericsson
* Daniel Stenberg, wolfSSL
 
