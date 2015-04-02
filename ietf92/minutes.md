# httpbis WG minutes IETF-92 Dallas  -- Tue afternoon 1300h


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [post-wg specs](#post-wg-specs)
- [Current extension spec issues](#current-extension-spec-issues)
  - [alt-svc issue 44 - think we have agreement on it](#alt-svc-issue-44---think-we-have-agreement-on-it)
  - [alt-svc issue 43 - ALPN Identifiers](#alt-svc-issue-43---alpn-identifiers)
  - [OppSec issue 33](#oppsec-issue-33)
  - [tunnel protocol for CONNECT](#tunnel-protocol-for-connect)
- [Potential Work](#potential-work)
  - [http signature](#http-signature)
  - [HTTP client hints](#http-client-hints)
  - [key http response header field](#key-http-response-header-field)
  - [json encoding the http header fields](#json-encoding-the-http-header-fields)
  - [www-authenticate I-D that uses the JSON HF definition technique](#www-authenticate-i-d-that-uses-the-json-hf-definition-technique)
  - [451 status code to report legal obstacles](#451-status-code-to-report-legal-obstacles)
  - [indicating char encoding and lang for http header field parameters](#indicating-char-encoding-and-lang-for-http-header-field-parameters)
  - [client init'd content encoding](#client-initd-content-encoding)
  - [2NN Patch Status Code](#2nn-patch-status-code)
  - [origin cookies and 1st party cookies](#origin-cookies-and-1st-party-cookies)
  - [encrypted content-encoding for http](#encrypted-content-encoding-for-http)
- [Issues against the httpbis docset](#issues-against-the-httpbis-docset)
- [H2 (aka HTTP2) deployment advice](#h2-aka-http2-deployment-advice)
- [mpeg dash](#mpeg-dash)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## post-wg specs

no discussion
  

## Current extension spec issues

### alt-svc issue 44 - think we have agreement on it

pat mcmanus(pm) is fine with it
 
 
### alt-svc issue 43 - ALPN Identifiers

martin thomson (mt) explains the detailed context ought to document the more broad connotations in the spec/doc
   
mnot: we should clarify that http/1.1 means HTTP/1.1 over TLS

mnot: we do have several issues open that aren't controversial -- need editors to update draft(s) and close out the issues

pm: ff37 impls this stuff, in beta, so folks can try that


### OppSec issue 33 

is open and needs to be incorp'd, then goto WGLC with this for 2 wks

mnot: moz impl'g, akamai on server side, other bwsrs?

 desires to advance this in compnay of alternative svcs
 
### tunnel protocol for CONNECT
 
has been discusssion, but no open issues, can goto WGLC
  
martin thompson(mt) there is not as much context in the into matterial so see the open pull request. Had priv feedback that they were unhappy with this but webrtc apps will have this header field forced on them
  
mnot: yes, in general can't make new header fields mandatory in http' but apps such as webrtc can do so, thus making that explict is nice/useful

Go ahead and put the text in, will issue WGLC
  
ekr: might need some wordsmithing that some traffice analysis of this stuff is possible -- will suggest text
  
  
## Potential Work

See http wiki page "WatchList"

mnot: only want to keep WG open if there's useful work to do. Might be some of these the WG may want to dive into...
  
### http signature

draft-cavege-http-signatures-04
    
tad early to adopt this?
   
###  HTTP client hints

have heard browser folk express interest in this

larry masinter(lm): there was work in this area 10 yrs ago -- already extant RFCs that cover much of this territory

mnot: agree that the above should be eval'd in that light

ekr: relates to client fingerprinting -- we ought to minimize passive fp surface and not worry so much about active so this draft may surface that struggle

interest in spec?  some yes...

pm: not every client is a browser; its not like you require a ietf wg to mint a header -- could experiment actively with it not just hack spec

chris bentzel goog: interested in this; if you have tcp proxy this might be useful
  
peter griess FB (pg): interested in this too, eg for mobile website
 
?: might be useful for DASH

mnot: am concerned about privacy concerns tho
    
    
### key http response header field

is a way to establish a secondary cache key that VARY selects. Vary is coarse, in usual case it is difficult to use to establish a secondary cache key. This spec is way to derive a more fine-grained secondary cache key.
  
might be either do this spec or kill 2ndry cache keys altogether

Ilya G likes this; if we adopted client hints -- we'd need this.
  
stuart cheshire (sc): iTunes team would like this
  
mt: concern w/this is the complexity -- trim it and leave open door for enhancing in future
  
sc: will ask them for specific needs
  
mnot: right not is kitchen sink-y  (...describes...)
  
part of issues with this is header syntax
  
### json encoding the http header fields

idea here is use json to describe header field, then serialize into header field value, could be a win
 
jr: it also makes internet aka i18n easier
 
phb: in long term we'll move to using json for everything. presently have class of headers for routing etc and a class for content -- would want to teases apart
  
eliot: how does jr view the transition to this working?
 
mnot: if i define a new header, then use this going forward
 
roy fielding: this is not an opportunity to define http/3

jr: trying to address defining new http header fields easier
 
phb: need a header field schema...

mnot: <pushes back>
 
 
### www-authenticate I-D that uses the JSON HF definition technique

mt: would need something more concrete than "just use json". Suggests like two practices for how to use
  
pg: having doc on header definition best practices would be helpful
  
mnot: putting aside the specific proposal -- have a HUM on a doc defining a convention for defining header definition conventions
  
decent hum on interest

almost none on harmful

a little on don't know  
  
mike bishop via jabber: this could encourage data smuggling via headers
 
oiwa: :  < something about the www-authn example> 

mnot: agree that was/is confusing
 
 
### 451 status code to report legal obstacles
 
mnot: discussion on list. A few folks think the semantics not well enough sorted out. Would like to discuss now.
  
barry leiba (bl) participant: is ok with what the WG thinks (formerly opposed). What were the args wrt insufficient semantics ?  think they are pretty clear
  
paul hoffman (ph): tim puts up examples of folks using this. So, it can be used. It has shown to be sorta useful, but maybe not super useful.
  
mnot: some folks said just use 403 with a response body

ph: but that would change semantics of 403

lm: I pushed back on this purpose seems to be political theatre why not be informational?
 
mnot: a use case is if you want to crawl web and get indications of censorship
 
phb: this status code is supplying addttnl info. It isn't law here is the issue itself, but in brings the law into the picture....
  
jon peterson(jp): could imagine getting a diff page with a 406
  
wendy seltzer: chilling effects project thinks this useful potentially
  
mnot: we could define header fields that'd be used in conjunction with this status code
 
?: something about could indicate the proxy or origin blocking access to this content
 
mnot: two status codes perhaps
  
bl: anybody say "no"?
 
(no objection)
 
### indicating char encoding and lang for http header field parameters

this'd be just adopting and finishing the spec.

should be close to done

"It was a WG spec" jr says -- but recants -- mnot celebrates
 
 
### client init'd content encoding

another jr spec

allows client to use content-encoding on requests

server can use accept-encoding in responses
 
mnot asks client implementations -- would u use this?
 
jr: has addressed the issues from last meeting
 
mnot: is an incremental optional addition to http, some folks could use it, makes sense to adopt
 
lm: how's the interact with http header scoping?

mnot: have to treat as a hint
 
<no objections otherwise>
 
 
### 2NN Patch Status Code

mnot: esoteric use case 

mt <makes face>

mt: I could see how it'd be useful in narrow cases. Could annoy api creators
  
roy: Yuk.

?: we currently do this when running commercial proxy

roy: effectively make all requests VARY
 
lm: don't you have to tie it to etag ?

mnot: yes, strong etag
 
?: w/intermediates, will be like 206

(roy later says it won't make all requests vary)
 
 
### origin cookies and 1st party cookies

mnot: Seems a number of folks are interested, but they are limited given how deployment will happen.
couldn't rely on them being there and so limited utility?
 
mt: <...various gnarlyness wrt cookies...>
 
?: discussing with someone and intend to continue to work on this draft (which one?)
 
mt: in terms of csp, compliant UAs gain a bit of resistance to stuff like CSRF
 
mnot: need to have chat with Mike West and webappsec folk
 
mnot: some interest but need more discussion
 
 
### encrypted content-encoding for http
 
mnot: working on this w/MT
 
mt: coupl use cases: webpush, need to push stuff thru intermediary, encrypt doc on server
  
mt: This is just a simple cut down version of tls record layer and some key mgmt
  
mt: there's some impls -- pretty interested in getting this going
  
mt: using jose didn't work in http semantics. eg a msg being processed continuously rather than a single blob
    
mt: no optionality in the format -- simple
  
mt: will engage w/sec folk
  
lm: there's desire afoot to secure http headers and optionally body and so ....
 
ph: why wont CMS w/smime eg smime 3 not work? pls engage smime list
 
mnot: so this spec is an fyi at this point
 
 
## Issues against the httpbis docset

mnot: eventually take it to full std. once http/2 is done, align with http2, then try full std. Can't see us starting this now, but maybe later this year?
 
jr: no further thoughts
 
 
## H2 (aka HTTP2) deployment advice

We have a faq on wiki, but info is thin.

There is perf increase but to really get in full need to tweak lots of deployment configs. Would be helpful to write down advice.
 
lm: have chatted w/folks this week. 2 aspects:

1. What does it mean to benchmark http on the real internet? How do you measure whether one deployment is better or worse?

2. and then deployment advice for how to attain improvements
      
mnot: w3c webperf wg -- could engage with them on this?

lm: lots of folks at IETF who know internet perf too -- will the lower layer folks interface with the webperf wg ?
 
mnot: RUM is interesting because it measures end user perf perspective -- in real world settings -- thus we really ought to engage with them
 
ph: we have benchmarking wg -- would not have this go there -- long time leads. Thinks webperf & rum is beter route
  
Dan Druta: goal-based: what do u want to improve? latency? load? etc. Stakeholder-based: e.g. for web developers, for web masters, for service providers, etc... both dimensions do both.
 
mnot: suggests starting effort on the wiki -- need folks to be willing to do work
  thinks webperf folks will eventually address it, but would be ncce if folks here would kick it off
  

## mpeg dash

 video streaming over http -- iteresting stuff on http2
 
herve ruellan (hr):  DASH and HTTP/2 (see preso in meeting materials)
 
FDH -- full duplex over http
 
Dan Druta: <detailed issues wrt pushing msgs to the server> dunno if that was considered, but need to.  "how quickly can u adapt?"
  
hr: yes can adapt but quickly is always difficult
 
? <detailed ques wrt push msg characteristics>
  sees benebit as ?
  seems lots of complexity w/o lots value
  didn't understand range option at all
  
jr & roy: request push sounds like GET, how is it diff than pipelined GET ?
 
hr: <explains>
 
mnot: http2 designed such that can interleave lots of reqs together. Here client can hint the server about something the client knows.
 
craig tayler(ct): concerned how server push will affect the ? semantics - might be issue
  
hr: yes, there issue here, an intent to have the server respond w/header to client. Then client knows to freeze the signal ?
  
mt: if u know what u need just ask for it. Thinks dash advantage is when server knows more about pacing of segments. E.g., if server sends next segment w/o client asking for it there's advantages. Also, client can notice about net issues and ask for lower quality.... hmmm maybe this looks like multi-get which we didn't do....
  
?: involved in dash. Yes there's a manifest file, server can update the manifest. Not clear whether h2 stack offers. Stacks have looked at don't offer this stuff as yet. That's something we need to address. We need a solution for this. Other think is whether push strategies is going to be defined somewhere. 
  
questions about flow control
  
mnot: http2 doesn't strictly define how server push works, defined as cache update, not notification to the webapp client. Wonder if we need to notify a listener about cache updates.
   
pm: how can you prioritize things -- we did some of that w/GETs in http2 -- could use that? <smthg about pushing addtnl metadata to the client> could be useful.
  
lm: implicit context is using mpeg-dash for realtime. If you have a series of pipelined GETs, you'll get em all. Timing is implicit. If you want to generalize this you might make the timing explicit.
  
?: not sure dash is useful for RT, but maybe progressive download?
  
mt: <somethingg about canceling an outstanding req> there's some useful cases for this. Avoid an XHR ?
 
mnot: don't hear interest in making this a generic extension yet. 

mnot: Dash folks also have use case to send to client that they have partial segment to send want to send it so client can do what they want
  
mnot: I steered them from partial content to use a different media type to label it.

mnot: I will discuss appropriate times for new items with BL
  
  
