
# httpbis WG minutes IETF-92 Dallas  -- Tue afternoon 1300h

## post-wg specs
  no discussion
  

## issues list discussions

### alternative svcs

https://github.com/httpwg/http-extensions/labels/alt-svc

two issues still open - discussing on list

#44 - think we have agreement on it
 pat mcmanus(pm) is fine with it
 
#43 ALPN Identifiers ...
 martin thomson (mt) explains the detailed context
   ought to document the more broad connotations in the spec/doc
   
 mnot we should clarify that http/1.1 means HTTP/1.1 over TLS

mnot: we do have several issues open that aren't controversial -- need editors to update draft(s) and close out the issues

pm ff37 impls this stuff, in beta, so folks can try that



### http opportunistic sec

#33 is open and needs to be incorp'd, then goto WGLC with this for 2 wks

mnot: moz impl'g, akamai on server side, other bwsrs?

 desires to advance this in compnay of alternative svcs
 
### tunnel protocol for CONNECT
 
  has been discusssion, but no open issues, can goto WGLC
  
 martin thompson(mt) there is not as much context in the into matterial so see the open pull request 
 
  had priv feedback that they were unhappy with this
  but webrtc apps will have this header field forced on them
  
 mnot: yes, in general can't make new header fields mandatory in http'
  but apps such as webrtc can do so, thus making that explict is nice/useful
  Go ahead and put the text in, will issue WGLC
  
  ekr: might need some wordsmithing that some traffice analysis of this stuff is possible -- will suggest text
  
  
## Potential Work

 mnot: only want to keep WG open if there's useful work to do
 
 [see http wiki page "WatchList"
 
  might be some of these the WG may want to digve into...
  
  ### http signature
    draft-cavege-http-signatures-04
    
   tad early to adopt this?
   
  ###  HTTP client hints

    have heard browser folk express interest in this
    -grigorik-http-client-hints-02
    please review this
    
    larry masinter(lm): there was work in this area 10 yrs ago -- already extant RFCs that cover much of this territory
    
    mnot: agree that the above should be eval'd in that light
    
    ekr: relates to client fingerprinting -- we ought to minimize passive fp surface and not worry so much about active so this draft may surface that struggle
    
    interest in spec?  some yes...
    
    pm: not evry client is a bwsr -- its not like u req a ietf wg to mint a header -- could experiment actively with it not just hack spec
    
    chris bentzel goog -- innarested in this
      if u have tcp proxy this might be useful
      
    peter ? FB -- innarested in this too
     eg for mobile website
     
    ? -- might be useful for DASH
    
    mnot: am concerned about priv concerns tho
    
    
### key http response header field
 roy & mnot
 is a way to estab a 2ndy cache key that VARY selects
  vary is coarse, in usual case it is difficult to use to estab a 2ndy cache key
  this spec is wway to derive a more fine-grained 2ndary cache key
  
  might be either do this spec or kill 2ndry cache keys altogether
  illya ? likes this
  
  if we adoped client hints -- we'd need dthis
  
  stuart cheshire (sc) -- I-Tunes team would like this
  
  mt: concern w/this is the complexity -- trim it and leave open door for enhancing in future
  
  sc: will ask them for specific needs
  
  mnot: right not is kitchen sink-y  (...describes...)
  
  part of issues with this is header syntax
  
### json encoding the http header fields -- julian reschke (jr)
 idea here is use json to describe header field, then serialize into header field value, could be a win
 
 jr: it also makes internat aka i18n easier
 
 phb: in long term we'll move to using json for everything
  presently have class of headers for routing etc and a class for content -- would want to teases appart
  
 eliot: how does jr view the transition to this working?
 
 mnot: if i define a new header, then use this going forward
 
 roy fielding: this is not an opportunity to define http/3
 jr: trying to address defining new http headerfields easier
 
 phb: need a headerfield schema...
 mnot: <pushes back>
 
 
 
### www-authenticate I-D that uses the JSON HF definition technique

mt: would need something more concrete than "just use json"
  suggests like two practices for how to use
  
  peter ? FB: having such doc would be helpful
  
  mnot: putting aside the specific proposal -- have a HUM on a doc defining a convention for defining header definition conventions
  
  decent hum on interest
  almost none on harmful
  a little on don't know
  
  
mike bishop via jabber: this could encourage data smuggling via headers
 
 oiwa: :  < something about the www-authn example> 
 mnot: agree that was/is confusing
 
 
 
 ## Tim Bray draft 451  status code to repoort legal obstacles
 
 mnot: discussion on list
  fair # folks think the semantics not well enough sorted out
  wouls like to discuss now
  
 barry leiba (bl) participant: is ok with what the WG thinks (formerly opposed)
  what were the args wrt insufficient semantics ?  think they are pretty clear
  
 paul hoffman (ph): tim puts up examples of folks using this
  so it can be used
  it has shown to be sorta useful, but maybe not super useful
  
 mnot: some folks said just use 403 with a response body
 ph but that wud change semantics of 403

 lm:i pushed back on this purpose seems to be political theatre why not be informational?
 
 mnot: a use case is if u want to crawl web and get indications of censorship
 
 phb: this status code is supplying addttnl info
  it isn't law here is the issue itself, but in brings the law into the picture....
  
 jon peterson(jp)
  could imagine getting a diff page with a 406
  
 wendy seltzer-- chilling effects project
  thinksthis useful potentially
  
 mnot: we'd define header fields that'd be used in conj w/this statsu code
 
 ?: something about could indicate the proxy or orgin blocking access to this content
 
  mnot: two status codes perhaps
  
 bl: anybody say "no"?
 
 <nope>
 
## indicating char encoding and lang for http header field parameters
 this'd be just adoping and finishing this
 should be close to done
 it was a wg spec jr sez -- but recants -- mnot celebrates
 
 
## client init'd content encoding
 another jr spec
 allows client to use content-encoding on requests
 server can use accept-encoding in responses
 
 client impls -- wud u use this?
 
 jr: has addressed the issues form last mtg
 
 mnot: is an incremental optional addtn to http, some folks coiuld use it, makes sense to adopt
 
 lm: how's the interact with http header scoping?
 mnot: have to treat as a hint
 
 <no objections otherwise>
 
## 2NN Patch Status Code
 mnot: esoteric use case 
 mt <makes face>
 mt: i could see how it'd be use fule in narrow cases
  could annoy api creators
  
 roy: sez Yuk
 ?: we currently do this when runing commercial proxy
 roy: effecively make all requets VARY
 
 lm: don't have to tie to dtag ?
 mnot: yes, stong etag
 
 tim bray?: w/intermediates, will be like 206
 
 
## origin cookies and 1st party cookies
 seems a # folks innarested but they are limited given how deployment will happen
 cudn't rely on them being there and so limited utility?
 
 mt: <...various gnarlyness wrt cookies...>
 
 ?: discussing with someone and intend to continue to work on this draft (which one?)
 
 mt: in terms of csp, complant UAs gain a bit of resistane to stuff like CSRF
 
 mnot: need to have chat with Mike West and webappsec folk
 
 mnot: some interest but need more discussion
 
## encrypted content-encoding for http
 mnot: working on this w/MT
 
 mt: coupl use cases: webpush
  need to putsh stuff thru intermediary
  
  encrypt doc on server
  
  crazy caching stuff
  
  this is just a simple cut down version of tls record layer and some key mgmt
  
  there's some impls -- pretty interested in getting this going
  
  using jose didn't work in http semantics
    eg a msg being processed continuously rather than a single blob
    
  no optionality in the format -- simple
  
  will engage w/sec folk
  
 lm: there's desire afoot to secure http headers and otionally body and so ....
 
 ph: why wont CMS w/smime eg smiime 3 not work?
 pls engage smime list
 
 mnot: so this spec is an fyi at this point
 
 
## issues against the httpbis doc
 mnot: eventually take it to full std
  once http/2 is done, align with http2, then try full std
  now http2 is done, so mebbe think about this

 can't see us starting this now, but mebbe later this year?
 jr: no further thoughts
 
 
# H2 (aka HTTP2)  deployment advice
 have a faq on wiki, but info is thin
 there is perf increase but to really get in full need to tweak lots of deployment configs
 would be helpful to write down
 
 lm: have chatted w/folks this week
  2 aspects:
      1) what does it mean to benchmark http on the real internet?  how do you measure whether one deployment is better or worse?
      
      2. and then deployment advice for how to attain improvements
      
 mnot: w3c webperf wg -- could engage with thtem on this?
 lm: lotsa folk at ietf who know internet perf too -- will the lower layer folks interface wiht the webperf wg ?
 
 mnot: rum is interesting because it measures end user perf perspective -- in real world settings -- thus we really ought to engage with them
 
 ph: we have benchmarking wg -- wuud not have this go there -- long time leades
  thinks webperf & rum is beter route
  
 Dan Druta: goal-based: what do u want to improve? latency? load? etc
 stakeholderbased: eg for web dvlprs, for web masters, for svc provider, etc...
 
 both dimensions do both
 
 mnot: suggests starting wuch effort on the wiki -- need folks to be willing to do work
  thinks webperf folks will eventually address it, but wud be ince if folks here would kick it off
  

# other uses of http2

## mpeg dash
 video streaming over http -- innaresting stuff on http2
 
herve ruellan (hr):  DASH and HTTP/2
 <see preso in meeting materials>
 
 FDH -- flull duplex over http
 
 Dan Druta: <detailed issues wrt pushing msgs to the server>
  dunno if that was considered, but need to 
  "how quickly can u adapt?"
  
 hr: yes can adapt but quickly is always difficult
 
 ? <detailed ques wrt push msg characteristics>
  sees benebit as ?
  seems lots of complexity w/o lots value
  didn't understand range option at all
  
 jr & roy:  request push sounds like GET, how is it diff than pipelined GET ?
 
 hr: <explains>
 
 mnot: http2 designed such that can interleave lots of reqs together
  here client can hint the server about something the client knows
  
 
 craig tayler(ct): concerned how server push will affect the ? semantics
  might be issue
  
 hr: yes, there issue here, an intent to have the server respond w/header to client
  then clinet knows to feeeze the signal ?
  
 mt: if u know what u need just ask for it
  thinks dash advantage is when svr knows more about pacing of segments
  eg if server sends next segment w/o client asking for it there's advantages
  also client can notice about net issues and ask for lower quality....
  hmmm mebbe this looks like multi-get which we didn't do....
  
 ?: involved in dash
  yes there's a manifest file, server can update the manifest
  not clear whether h2 stack offers ?
  ?
  stacks have looked at don't offer this stuff as yet
  that's something we need to address
  need a soln for this
  
  other think is whether push strategies is gooing to be defined somewhere
  questions about flow control
  
  mnot: http2 doesn't strictly define how svr push works, def'd as cache update, not notification to the webapp client
   wonder if we need to notify a listner about cache updates
   
 pm: how can u prioritize things -- we did some of that w/GETs in http2 -- could use that?
  <smthg about pushing addtnl metadata to the client> 
  could be useful
  
 lm: implicit context is using mpeg-dash for realtime
  if u have a series of pipelined GETs  u'll get em all
  timing is implicit
  if u want to generalize this u might make the timing explicit
  
 ?: not sure dash is useful for RT, but maybe progressive dwnload?
  ?
  
 mt: <cmthg abotu canceling an outstanding req>
 there's some useful cases for this
 avoid an XHR ?
 
 mnot: dont hear interest in making this a generic extension yet
  
  dash folks have use case to send to client that they have partial segment to send
  want to send it so client can do what they want
  
  steerred themfrom patial content
  use a diff media type to label it
  is a side discussion
  
  will discuss approp items with BL
  
  
