# HTTP Working Group Minutes - IETF 94

## Monday, 2 November 2015 13:00-15:00

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [agenda bashing](#agenda-bashing)
- [Specification Status](#specification-status)
- [Active Drafts](#active-drafts)
  - [[Alternative Services](https://tools.ietf.org/html/draft-ietf-httpbis-alt-svc)](#alternative-serviceshttpstoolsietforghtmldraft-ietf-httpbis-alt-svc)
  - [[Opportunistic Security](https://tools.ietf.org/html/draft-ietf-httpbis-http2-encryption)](#opportunistic-securityhttpstoolsietforghtmldraft-ietf-httpbis-http2-encryption)
  - [[Key](https://tools.ietf.org/html/draft-ietf-httpbis-key)](#keyhttpstoolsietforghtmldraft-ietf-httpbis-key)
- [Client Certificates and HTTP/2](#client-certificates-and-http2)
- [Potential Work](#potential-work)
  - [COOKIES](#cookies)
- [AOB](#aob)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


### Agenda Bashing

No comments


### Specification Status

- [The ALPN Header Field](http://datatracker.ietf.org/doc/rfc7639/) *RFC Published*
- [Client Initiated Content Encoding](https://datatracker.ietf.org/doc/draft-ietf-httpbis-cice/) *In RFC Editor Queue*
- [An HTTP Status Code to Report Legal Obstacles](https://datatracker.ietf.org/doc/draft-ietf-httpbis-legally-restricted-status/) *Exiting WGLC*

mnot: doesn't think we'll need much in way of mods based on review, will kick off with IESG in near term
   

### Active Drafts


#### [Alternative Services](https://tools.ietf.org/html/draft-ietf-httpbis-alt-svc)

Discuss the [issues list](https://github.com/httpwg/http-extensions/issues?q=is%3Aopen+is%3Aissue+label%3Aalt-svc) and draft status.

mike bishop:  see comments in the issue #76 & PR #98

martin T,: spec typical cert checks for normal case, and if the alt svc has addtn'l reqs, need to spec them also. dont think we have real issues with alt svcs, but we have a soft fail, which ends up just degrading the ecosystem.  need to get the addtnl checks on certs right -- what is in spec now is too vague

mikeb: when we tried to be more specific at last ietf mtg, folks didnt' like the specifics <chuckle>
  
mnot: eg have the typical defaults, spec addtnl stuff in context of the alt svc spec

ekr:  <missed>
  
mike b: tried to say "impls have their own reqs anyway" 

mnot: perhaps say "other" rather than "impl specific"

martin t: essence that we reserve right to impose further restrictions is fine

[issue #89](https://github.com/httpwg/http-extensions/issues/89) - using alt svc on local host

mnot: patrick have anything to add?  had difficulty to generate the text, if there's no issue we can close it, if not we need addnl txt

martin t: thinks Patrick's last comment is fine,

mnot: closed 

[issue #92](https://github.com/httpwg/http-extensions/issues/92) alt-svc vs the ability to convey the scheme inside the protocol 

martin t: the point is to avoid app being confused, eg by looking at the "stack" and if see TLS underneath, they often assume https.  need app containers to shield the app from seeing that there's TLS there when doing opp security and the connection isn't authn'd -- having text along those lines a good thing -- highlight things one needs to look for.  eg in sec considerations

patrick m: this is similar to virt hosting environments, emphasize that origin is not changing.  

julian via jabber: right now we have a MUST NOT  in the sec cons. do we agree on changing this to advisory prose?

in Sec 9.5

martin & julian disagreeing on what change can be made to S 9.5 -- has to doing with diffs between HTTP 1.1 vs 2

mnot: ok, take it to the list then

[issue #96](https://github.com/httpwg/http-extensions/issues/96) IANA procedure for alt-svc parameters

mnot: what review level is needed for this?  "ietf review", "spec req'd", "expert review" ?

yoav n:  thinks expert review is approp.

mnot: finding expert can be painful

martin t: spec req'd involves expert

barryL: appoint someone who participates in WG and have them query WG wrt answer, thus is sort of a shepherded WG review

yoav: anoint Julian as expert :)

mnot: thinks can get this to WGLC in a few weeks -- lets get discussions happening on list. There are impls of this, is there any discussions of test suites?

pr #101: 

mike b: diss levels of  normative text in diff places, tried to rectify that, eg changing 'can' to 'SHOULD'

mnot: 1st is a normative change...

mike:  so that one was a MAY and elsewhere a SHOULD

martint: this one is ok -- should encourage clients to use this so SHOULD is approp

pr #98 was discussed way up above

[ patrick m has their own test suite -- but no one else speaks up ]






#### [Opportunistic Security](https://tools.ietf.org/html/draft-ietf-httpbis-http2-encryption)

mnot: waiting for alt-svc to be done -- so in holding pattern -- hasnt been chance to deploy this on server side until recently.

martin: there was disc on this during TPAC last week, there's been work on it since then, in a few weeks may see email about how this works. 

mnot: can see this going in any direction:  publish as-is, don't pub, modify it
martin: yes



#### [Key](https://tools.ietf.org/html/draft-ietf-httpbis-key)

mnot: way to calculate a cached key -- VARY header is tough to use
 martin will be shepherd on spec, mnot is co-author
 had a decent amount of implr interest from "cache" folk
 have a fair # of issues- some minor, some speculative

issue #?

igrigorik submitted

martin: rather than the proposed syntax perhaps we can simplify it in some manner, eg have mult matching rules mean 'OR' -- currently ordering and precedence is likely an issue.  

mnot: take to list

issue #?  case insensitve matches

mnot: summarizing: we'll interate on this draft one or two times and then we'll have something ready for experimentation -- really want impl experience before shipping it

[ leif intending to impl ]



### Client Certificates and HTTP/2

Presentation: [client authentication](https://docs.google.com/presentation/d/1-2bBYDvWqrTM-RUz2bKzkTFyIO4kJzMT6jRhFcuiR84/edit#slide=id.p) - Martin Thomson

mnot: we disallowed client certs in http/2 because we disallowed reneg -- this is a proposal that meshes with discussion in TLS WG

slide: history

mic yoav: does this really matter?  one can do <foo>
  
martin: trying to avoid situations where that is possible -- can lock the entire browser due to concurrency issuse (eg firefox) -- u receive req for cert, whch client to I ask to provide the cert?

slide: ignoring prob doesn't make it go away

?: did you ask TLS wg to fix this?

martin: yes, and will explain what we're doing

yoav: there will be disc about this in TLS session

ekr: TLS 1.3 will support a diff sec mech, in gen it is hard to reason about semantics of reneg, thus decisions taken in TLS WG

slide: soln overview

there is a WAITING_FOR_AUTH frame added to h2, and an identifier that maps this to the TLS context

yoav: <some detail wrt correlation>
  
martin: this ident makes it more clear what the binding is between the layers and sidesteps concurrency blockage 

slide: part 1.1: WAITING_FOR_AUTH frame

slide: part 1.2:   TLS 1.2 magic

 ident is sent in ClientHello extension by client
 server can then decide which of the outstanding authz's it wishes to take on
 
slide: part 1.3: TLS 1.3 magic

 not entirely decided here how it works
 
slide: part 2 - setting reneg

martin: my opinion: don't use this feature
   this can cause some surprises in your stacks, ie practical concerns wrt state of a session
   
mnot: don't use "now" or "ever" ??

martin: you use this for bkwds compat, but this is not the future

mike b: why dont we just define a ALPN (?) for this (for the futuure) and this prop is just back compat

martin: agree

yoav: am not sure why this is more deployable than other way

martin: this doesnt touch the app at all -- in the other approach, the server needs to send a 401, and that's a change to the app api yhou're presenting

yoav: disagree

martin: the 401 goes to client, and then ought to send an alert at tls layer but can't in tls1.3. the point of this is to fix bkwd compat req w/o changing apps

yoav: this still looks to me the same api 

ekr: this is a much easier drop-in than the alternatives

?: observes that not having this solved is slowing h2 deployemnt -- but saying dont use this isn't helpful -- is there a doc we want to write that says "please use this but it is dangerous"

martin: we do have a handle on the sorts of probs this might cause, so we will quantify thos probs and leave it as that

mke b: we're crossing layers, so understand why it makes folks nervous, as to why we don't have an api using 401 is that we're killing the old stream, that reqs client stack to do things that aren't easy or presently supported, and also the svr has to think it is on same xaction when it isn't, so this draft is easier to do

martin: the disc on list seemed to arrive at that

slide: adopt me

martin: do we want to work on this prob?  there is a draft, sub'd just before the deadline -- mike & I. as mike said, this'd be easier to adopt
  
mike b: had earlier draft, didn't adopt it, msft pub'd as proprietary, made TLS folk sad, this draft is an improvement, so am fine with deprecating the prior approach

martin: goog may take diff view on this, 

mikeb: they removed reneg while app data is flowing -- ... -- do still have open question on tls implr's 

martin: we may need to tweak the tls v1.2 aspect of this from this

mnot: need more disc on tls 1.2 & 1.3 particulars to ensure we  going in right direction

ekr: at TLS interim, we decided to adopt changes that support this -- what is not done is a tech proposal for the crypto that makes this work -- but there is consensus on the semantics

martin: the 1.2 question has to do with reneg handling in 1.2 stacks

mnot: that makes me relatively comfortable wrt making call for adopt in next week or two



### Potential Work

* [A JSON Encoding for HTTP Header Field Values](http://tools.ietf.org/html/draft-reschke-http-jfv)

mnot: this is for NEW HEADERS. If your data is interms of JS objects, can map to this since uses json. In h2 had disc wrt header-aware compression - thus some interest in this. Every time some one comes up with new http header field Julian needs to review, and he is thus the bottleneck. Would much reather have documentation and techniques for this such that less review is needed
thus this spec -- an attempt to do that. The audience for this is other spec writers. Feedback is that looks interesting but isn't a std -- chick & egg prob
maybe we httpbis should adopt and make some progress.

julian: there is connection to the key spec.
  there is one field that relies on <foo> -- if can fix that in the key spec, then http-jfv might be able to be used.
  maybe that would make it popular for other header fields?
  
mnot: agree - - inclined to issue call for adopt -- want to talk with folk in webappsec to see if this is palatable & useful -- comments?

jeffH: seems reasonable

julian: yep


* [Encrypted Content Encoding for HTTP](http://tools.ietf.org/html/draft-thomson-http-encryption)

mnot: this is martin's spec -- web push depends on this?

martin: yes, this is basis of msg encryp in webpush. need to work out where this lives
  
mnot: were waiting for usecases & implrs to emerge -- has occured -- so issue call for adopt -- is sec-oriented, want to be careful



* [ORIGIN Frame](https://tools.ietf.org/html/draft-nottingham-httpbis-origin-frame)

mnot: h2 allows you to coalesce origins on a given connection -- of interest to CDNs -- clients interested & willing to impl?

patrickm: yes, we are interested in this

martin: the std way we decide something can be coalesced, we get same ip addr & port, this introduces potential for one to learn what other names are available on an origin w/o going thru dns disco -- is that the intent?

mnot: in h2, both dns and the cert have to match, we're not changing that, there are cases where both dns and cert match and it is a mistake -- a ques is whether we want to add semantics to this 

mikeb: if a client wanted to do the opt, can query the dns, to a certain extent the client decides that and it doesn't need to be spec'd

martin: we ahve to 'consider it' in any case -- don't think this is a bad idea
patrickm: let's adopt

ekr: what about the privacy issue?   it provides a more agressive way to exfiltrate what extensions are suppoted -- hmmm... concerned about DNS naming -- ie dns name blocking -- 

mnot: in proposed spec, origin sends frame to client -- these are origins I am willing to serve -- can be a long list

ekr: ultimately thinks it's fine

mnot: may send call for adoption on this, will see if Erik N is willing to edit

ekr: is this a doc that doesn't req https?  it wud be attracitve to go to goog and they send you frame with all this info -- is fine over https -- but if plain http isn't ok

mnot: intent is to not do over http

#### COOKIES

martin: preso on this:  

* [Cookies!](https://docs.google.com/presentation/d/1fw97QlPENqAB1bMUySIIm4dBbnno75tHVpbs302txPM/edit?ts=5636b0a6#slide=id.gd1d4c5107_0_70)

slide 2: cookies are stale.
  enumerate probs with cookies
  
slide 3: lets get fresh.
 [ summarizes the four draft-west-* IDs -- three of which are listed below]
   
slide 4: the choice is yours.
  do we do a subset of thsse four IDs or all of 'em ?
  

mnot: prob a bad idea is to make blanket statement "we going to improve cookies"  given history

proposing: hve initial phase of gtting some impl experience with these proposals, and only open up cookie spec and apply the ones that we've decided that "works" 
  
martin: do want to impl some of thise on short timescale -- eg cookie slinging is of concern now as opposed to origin cookie which is a "nice to have"

mnot: we have text already, maybe also regard cookie spec as a carefully managed "living standard" that gets constantly updated

ekr: nice to disting btwn "nice to haves" and "necessary" ones.
 eg secure cookies thing is being impl'd -- fait accompli ?
  others prob need some coordination -- what is the relnship of them to exisitng mechs.
  eg first party only is jiust a declaration, and then how does that relate to origin cookie.
    thus need to have client and svr work together to get value out of them, and if there impl diffs btwn clients and svrs then may not get value.
    
mnot: thinks mike finds origin cookie as 'defense in depth' that svr can't depend upon.
  jiust wanted to kick off discussion.
  need to discuss approach steps too
  


* [First-Party Cookies](http://tools.ietf.org/html/draft-west-first-party-cookies)

addresses CSRF



* [Cookie Prefixes](http://tools.ietf.org/html/draft-west-cookie-prefixes)

addresses cookie leakage



* [Leave Secure Cookies Alone](https://tools.ietf.org/html/draft-west-leave-secure-cookies-alone)

addresses cookie slinging attacks


origin-cookie -- https://github.com/mikewest/internetdrafts/blob/master/origin-cookies/draft-west-origin-cookies-01.txt 


* [Accept Push Policy](https://tools.ietf.org/html/draft-ruellan-http-accept-push-policy-00)
? from Canon presenting -- <link to slides???>

slide 4: load balancer

slide 5: fast first display

slide 7: push policy - defines server behavior regarding push -- can be negotiated

slide 9: possible policies

mnot: this is from DASH as primary use-case, for common web use case wonders if it will be useful whether servers will use it -- if just for dash, then it can have such headers in its specs

?: want to at least have feedback from this community
  and maybe go a bit further than dash needs, generalizing and doing IETF
  
martin: this is similar to signaling about the client cache -- could be useful -- wonders whether we see clients actually implementing policies around this and what sorts of policies

mnot: tend to agree, if we have mech for svr to learn client state it is interesting, but if we stdz something, need to do it right, and not be vague

martin: the other preso from this last weekend was good -- can experiment with cookies and svc workers -- this is interesting, can experiment with this using those techniques, eg is a simple system of tags sufficient or something more complex necessary for desired use cases?


### AOB

mikeb: wrt  PR #101 on alt-sve -- julian commented on it just now

mnot: answering julian: thinks we can resolve this in the issue

