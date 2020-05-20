   
# HTTP WG May 2020 Interim Meeting Blue Sheets

_blue sheets only_; please add your name on a single line.
https://docs.google.com/document/d/1G-aolTxcnHS7mtVABVKJ7eN8f3iJHExZdRgkId1lZSc/edit
*Please close the document afterwards so others can add their names!*

# Minutes

Scribes: Robin Marx, Martin Thomson

## Lucas Pardue, Priorities

https://tools.ietf.org/html/draft-ietf-httpbis-priority
https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/priorities.pdf

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


## Brian Campbell / Client Certs

https://tools.ietf.org/html/draft-bdc-something-something-certificate
https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/client-cert.pdf

TTRP MTLS

mnot: are there any questions that might inform the decision about whether this might be adopted; 
ekr: if the people who want this are willing to deal with the fanciness of the potential solutions to this problem, the answer might be yes; if they are not, then the answer might have to be no
brian: maybe yes, but want a sense of what others think
mnot: we should probably talk about this on the list more
brian: we seem to be in a deadlock currently
mnot: chairs should talk


## Colm Divilly /  User Defined Resource Error HTTP Status Code

https://tools.ietf.org/html/draft-divilly-user-defined-resource-error
https://github.com/httpwg/wg-materials/blob/gh-pages/interim-20-05/user_defined_resource.pdf

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


jabber: 9 people
webex: 33 people

## Attendee name / affiliation

Barry Leiba, FutureWei
Colm Divilly, Oracle
James Gruessing, BBC
Patrick McManus, Fastly
Robin Marx, Hasselt University
Cory Benfield, Apple
Bence Béky, Google
Roberto Polli, Italian Digital Transformation Department
chi-jiun su, hughes network systems
Julian Reschke, Greenbytes
Martin Thomson, Mozilla
Lucas Pardue, Cloudflare
Mark Nottingham, Fastly
Magnus Westerlund, Ericsson
Tommy Pauly, Apple
Kazuho Oku, Fastly
Hiroyuki Goto, Gree
Eric Rescorla, Mozilla
Mike Bishop, Akamai
Brian Campbell, Ping
Ian Swett, Google
Ken Murchison, Fastmail
Daniel Stenberg, wolfSSL
Alessandro Ghedini, Cloudflare
Roy Fielding, Adobe
Michael Richardson, Sandelman Software Works
Felix Handte, Facebook
Dmitri Tikhonov, LiteSpeed Technologies
Chris Box, BT
 
 
 
 
 
 
 
 
 
 