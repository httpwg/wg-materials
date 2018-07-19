
# HTTP Working Group Minutes

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Tuesday, 17 July 2018](#tuesday-17-july-2018)
  - [Active Extension Drafts](#active-extension-drafts)
    - [HTTP Representation Variants - Mark Nottingham](#http-representation-variants---mark-nottingham)
    - [BCP56bis - Mark Nottingham](#bcp56bis---mark-nottingham)
    - [Secondary Certificates - Mike Bishop](#secondary-certificates---mike-bishop)
    - [Structured Headers - Mark Nottingham](#structured-headers---mark-nottingham)
    - [Cache Digests for HTTP/2 - Kazuho Oku](#cache-digests-for-http2---kazuho-oku)
    - [Client Hints - Mark Nottingham](#client-hints---mark-nottingham)
    - [RFC6265bis: Cookies - Mike West](#rfc6265bis-cookies---mike-west)
  - [Proposed Work](#proposed-work)
    - [The "SNI" Alt-Svc Parameter / HTTP Alternative Services via DNS - Mike Bishop, Ben Schwartz](#the-sni-alt-svc-parameter--http-alternative-services-via-dns---mike-bishop-ben-schwartz)
    - [CDN Loop Prevention - Nick Sullivan](#cdn-loop-prevention---nick-sullivan)
    - [HTTP-initiated Network Tunnelling / HELIUM - Lucas Pardue (remote), Ben Schwartz (slides)](#http-initiated-network-tunnelling--helium---lucas-pardue-remote-ben-schwartz-slides)
  - [Related](#related)
    - [H2 Server Push Data - Aman Nanner](#h2-server-push-data---aman-nanner)
    - [More H2 Server Push Data - Brad Lassey](#more-h2-server-push-data---brad-lassey)
- [Wednesday, 18 July 2018](#wednesday-18-july-2018)
  - [QUIC and HTTP](#quic-and-http)
    - [Priorities](#priorities)
    - [GREASE](#grease)
  - [HTTP Core](#http-core)
    - [Editors' update](#editors-update)
    - [Issue Discussion](#issue-discussion)
      - [Include Status Code 422 (123)](#include-status-code-422-123)
      - [Are headers always defined with ABNF? (74)](#are-headers-always-defined-with-abnf-74)
      - [Deprecate Accept-Charset (61)](#deprecate-accept-charset-61)
      - [Reuse of Responses (52)](#reuse-of-responses-52)
      - [415 and Accept (48)](#415-and-accept-48)
      - [* in Accept-* (46)](#-in-accept--46)
      - [Extension Capabilities (44)](#extension-capabilities-44)
      - [3xx redirects - request formation (38)](#3xx-redirects---request-formation-38)
      - [Header registry (42)](#header-registry-42)
      - [Field-name Syntax (30)](#field-name-syntax-30)
    - [Wrap Up](#wrap-up)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Tuesday, 17 July 2018

* Chairs: Patrick McManus and Mark Nottingham
* Minutes: Paul Hoffman

### Active Extension Drafts

#### HTTP Representation Variants - Mark Nottingham

One person indicated that they might implement

One cache has implemented, another has intent to implement

Patrick: Park this doc for an indeterminate period time

#### BCP56bis - Mark Nottingham

Has gotten fairly broad review inside and outside the WG

Rate of change is slowing down

Wants to wait for HTTP core documents

Willing to wait for this

Martin Thomson: Having it is more important that publishing it
	Would be good to ship with core documents, so hold until then

20ish people in the room has read it

Patrick: Lots of issues have been opened and dealt with
	Please read the privacy considerations section
	Someone from SAAG wanted a normative reference

Paul Hoffman: That person was saying why the weren't doing BCP56 correctly

Julian Reschke: Some things might move between this and the core doc

#### Secondary Certificates - Mike Bishop

Martin: Hesitant to go back to TLS often
	Likes the separation between the identifiers
	Concerned with the carriage of the blobs

Ben Schwartz: Is it possible to send a request that gets more than one?

Mike: You can find the request ID of the one that you sent

Ben: Could you have frames that have requests that get explicit answers?

Mike: Could add that

Kazuho Oku: I don't need the request ID.
	If we put the request ID in the request, it doesn't save us anything

Nick Sullivan: Saving the search

Martin: Is OK with either one

?: What is the context of the certificate authentication?
	Can this be applied to alt-svc?

Mike: Only for this connection

Nick: This is for reducing the scope with more complexity

Ben: Could you imagine a tag that creates a pool?

Richard Barnes: Tagging seems way more sensible for CDNs
	Hinging your security on adding that tag

?: Suggests a tighter restriction

Kyle ?: Could share with related certificates

Richard: Wants certs with domain names

More to do, lots of interest

#### Structured Headers - Mark Nottingham

Martin: These things go on the wire ordered anyway
		But processors don't need to follow the order

Julian: What characters are allowed in identifiers?

Would like to ship by IETF 103

Commitments to review: about four

#### Cache Digests for HTTP/2 - Kazuho Oku

Intend to keep this open

#### Client Hints - Mark Nottingham

Just started WG Last Call for three weeks

Experimental because only one browser

#### RFC6265bis: Cookies - Mike West

Not much document progress since last meeting

Implementation progress

### Proposed Work

#### The "SNI" Alt-Svc Parameter / HTTP Alternative Services via DNS - Mike Bishop, Ben Schwartz

Ekr: Why would an alternative server send me a new SNI

Mark: Doesn't require the alternate to be named in the cert?

Mike: Adds a "concealed option"

Ekr: It must validate for the real cert

Ben: Agrees with that analysis
		Introduces a variety of modes, some don't cover all attacks

?: Why are we mucking around with the SNI itself?
	Can we eliminate it altogether?

DKG: Allows an attacker to block

Erik Nygren: Is this in addition to or instead of?

Ekr: Makes the cover domain subject to blocking

DKG: ESNI permits client-facing server from the actual server

Mike: Alts do not

DKG: Lets middle server see clear text

Kazho: Why do you need a new DNS record type?

Ben: Allows load balance across multiple CDNs

Erik: Likes ALTSVC in DNS
	Problems with ESNI goes away

Patrick: Likes some parts of some of these

Lutz Jacob: Is interested in this for "trusted traffic"
	Origin can redirect traffic around
	Publishing the records might be a challenge for the

Ted: Doesn't think DNS human readability is important

Ben: Someone needs to configure this somewhere
		Likes ESNI, but it creates a operational integration point that has to be fully automated

Ekr: If you want PFS for ESNI, then you have to rotate the keys quickly
	Is everyone on the CDN going to use the alt svc to go to the one cover name
	So everyone in the world goes through an extra round trip

Mike: You can also use some other host name in the cert, and get ambiguity

Ekr: Huge information leak

Ben: Useful for if there is just one domain on an IP address

Mark: Who is interested in continuing discussion DNS ALTSVC?

*Reasonable*

Who is interested in continuing discussion of Alt-Svc SNI?

*Slightly less*

#### CDN Loop Prevention - Nick Sullivan

Martin: Concerned about privacy, but the alternatives are worse
		Use opaque identifier

?: Likes the Forwarded header is better with "by" field.

Leif: Would like spec to be useful for cross-CDN and intra-CDN

Nick: Thinks already has intra-CDN solution

Patrick: Would the resolution of scope be OK in the WG

Mark: Very specific problem
			Doesn't want it to be so general to not fix the inter-CDN problem

Kazuho: Likes the must-not-modify feature

Erik: Likes having a specific header

Mike: Novel and useful piece is a header that much not be removed

Chris ?: In favor of looking at this work

?: Helps work end-to-end

Mark: Reusing "Forwarded" makes people maybe want to remove it
		Wants it done in this WG instead of in a CDN-specific group

Hum: None opposed

#### HTTP-initiated Network Tunnelling / HELIUM - Lucas Pardue (remote), Ben Schwartz (slides)

Ben: HELIUM was covered in DISPATCH

Mike: Likes the architecture and problem statement
	Maybe don't want the transport part here
	Maybe form a new WG for the combined set

Erik: There is a lot of transport stuff here
	IPsec over UDP covers a lot of the use cases

Jana Iyengar: Google already has such a use case
	Useful

Ben: DISPATCH chairs want it in DISPATCH

### Related

#### H2 Server Push Data - Aman Nanner
#### More H2 Server Push Data - Brad Lassey

Kazuho: Push is useful if you have a long pipe

Aman: Push over QUIC could be interesting

William ?: .15% had push
	Three weeks ago it one third
	Question on how many pages got nuked

Alan ?: Browsers are different, so it is hard for big sites like Facebook

Erik: Can you filter by when the push happens

Mike: Both are collecting data off of Chrome, but you have diverging results
	First navigations are different than all navigations
	Maybe joint experiment from both sides


## Wednesday, 18 July 2018

### QUIC and HTTP

#### Priorities
Patrick: Leave it alone in h/2

Mike Bishop: Do you never expect another version of HTTP?

Patrick McManus: In my mind QUIC is h3

Mark Nottingham:  On the client side it's a clean slate, on the server side I expect them to complain.

Gabriel Montenegro: Do you think we can take advantage of this in h/2 without extra signalling?

Patrick McManus: I see it as a bunch of backporting from hQ to h/2

Jana: Agree with Patrick, leave it alone for now

??  (Apple): I would be content with leaving it alone.  With the future and things diverge, then the API layers should be in line.

Roy Fielding: The question is if someone willing to write a doc about h2 priorities, then we should accept it.

Lucas Purdue: How does this relate to priority work in WICG?

Mark Nottingham and Patrick McManus and Martin Thomson: The WICG is a playground, and has little weight on their process.

The working group consensus is to do nothing for now.

#### GREASE

Martin Thomson: We should do this to maintain similarity with QUIC, and it's hard.

Patrick McManus: Many things brought it to tls1.3 and QUIC.  My draft id connect tunnels for websockets was deployed.  He had settings deployed from server -> client, and a popular OS client promptly closed the connection.  If there are other willing to experiment, join me.

Mike Bishop: Since the issue was found on a client, then we need servers to deploy this experiment?

Mark Nottingham: anyone want to send GREASE values? (handful)

The working group will wait for experimentation reports on the list and decide how to incorporate into the documents.


### HTTP Core

#### Editors' update

mnot: Have an open issue to reference new documents.  We can go through the cookies doc, but not sure about QUIC.

mbishop: There text we want to reference in QUIC from the new RFCs.

mnot: I think we can get it done in time for QUIC to reference them.

Roy Fielding: The history of the drafts can be seen for the last 15 years in github.  There are a set of diffs of the changes to HTTP core.

mcmanus:  I appreciate all the work that went into this reorganization.

mnot: The overall structure is good, and can be tweaked as we go along.


#### Issue Discussion

##### Include Status Code 422 (123)

mnot: Good to add it; it's generic and should be in core.  Do we mark the that this document updates webdav?

Julian: Not necessarily, unless we change the definition.

mt: Include it, but don't worry about Updates WebDAV.


There is consensus to include it in HTTP core.


##### Are headers always defined with ABNF? (74)

Roy Fielding:  Maybe we change it to be the condition we do not want it to fail.

Mark Nottingham: What about what to do if there are multiple instances of the same field?

Roy Fielding: Define it in terms of what the field is when combined.

Martin Thomson: My experience is that things that coalesce do it blindly?



##### Deprecate Accept-Charset (61)

mnot: I recommend changing it to obsoleted.

mt: No one use this, and fine that if they do they get undesired results.

mcmanus: It's a good bar to set that if something is harmful.

mt: Abbreviate it for historical purposes and deprecate it.  We can't remove something unless it never existed.

rfielding: I agree we should have it in the spec, and why you shouldn't use it.

The working group consensus is to mark Accept-Charset as obsolete.

##### Reuse of Responses (52)

mt: Jeffery notes preload and prefetch also have this problem.

mcmanus: We could introduce the notion of single use response.

mnot: We have a section for caching and history lists.  I do like the idea of a single use response.

mt: We need to decide on which of these `no-store` is, and go from there.

mnot: I'm talking about whether no-store is opt-out from re-using it.

mt: If I've been waiting for a response and now I have to regenerate.

mcmanus: FF sometimes collapses and sometimes doesn't, so it is contextual.

Chris Lemmons: If we get the same requests very close, we collapse them, so clarity would be helpful.

The working group consensus is to clarify the definition of 'no-store'.

##### 415 and Accept (48)

Julian: Is this a request to extend RFC 7694?

mnot: Would we obsolete 7694 and incorporate into core?

mt: It makes sense to roll these into HTTP core and obsolete the former.

The working group consensus is to roll 7695 into core.

There is some support to incorporate Accept into the server-side; to confirm on the list.

##### * in Accept-* (46)

Julian: I seen people ask for "*/text" or "*/*+json".

mt: Glob it!

mnot: If I have 5 specific JSON-based media types, I'm not sure what the utility is.

Julian: If you have support for 5 types, then I can ask for the JSON variant of all the types you can produce.

mnot: I believe ti be an interesting use case for "give me any image type".

roy:  I would hesitate to make any changes here.

mcmanus:  If anyone has implementation experience can tell us about it.

roy: I don't have any good use cases for it.  We've kept this for historical reasons, and people have used it to select a particular version of a media type.

mnot: I suspect the most we can do is warn people about unintended consequences.

Julian: This might be for BCP 56bis.

The working group consensus is to add text to discourage or warn about it, but not deprecate it.

##### Extension Capabilities (44)

Mbishop: For connect specifically, it does feel a little weird.  I wonder if we can find appropriate wording about how connect converts to this other tunnel.

mnot: I think that's a separable issue, and revisit "CONNECT" as a generic method.  It probably shouldn't modify the semantics of GET.

mbishop: I wonder if an extension for a particular mapping can effect how a method is modified in that mapping.

mnot: How it gets expressed on the wire shouldn't affect that mapping.

mt: I'm not sure about CONNECT as an example, but consider it "special" instead.  This question is difficult because we are talking about the semantic model, and not talking about e.g., h/2 bits.

mnot: We have an open issue to put text around the semantic issues around h/2.  Then we can talk about h/2 extensions.

mcmanus: The way this is describe is in terms of h/2 model and not the generic core model.

mnot: We went to great effort to talk about extension points in -bis, but h/2 was coming.

Julian: In h/2 the extension can modify anything, and that causes confusion and conflict.  What Patrick did for CONNECT and websocket was ok but should not be looked at for more generic.

roy: Extending a name to have meaning where it didn't before is ok, but extending it to change its meaning should not be allowed anywhere in the IETF.

mt: We reserved CONNECT in the registry.

The working group consensus is to explore it but wait for h/2 text.

There is also consensus to revisit the definition of CONNECT.

##### 3xx redirects - request formation (38)

mt: I think this is largely orthogonal; we don't have to do it, but it's reasonable to do while the document is open.

mcmanus: Some of the implementation deviation is the lack of guidance.

mnot: I think fetch has done a lot of the hard work and we should reflect that here.

Working group consensus is to work on some text here.

#####  Header registry (42)

mt: I think this is largely orthogonal; we don't have to do it, but it's reasonable to do while the document is open.  I think this is useful if the registry rulesa re sufficiently different.  I'm a little in support, but procedures can drag on a bit.

Alexey: I would like you to take this issue to dispatch.  If you are suggesting to change the registration procedure it should be dispatched.

This issue requires more discussion on list and likely needs to be taken to DISPATCH.

##### Field-name Syntax (30)

mt: Sure (make it simpler).

mbishop: My inclination is that if you are updated then you might not be backward compatible.

roy: Would like the reduced syntax.

Julian: This can be done with new registration procedures (above).

#### Wrap Up

Chairs encourage everyone to engage in the issues on the list.
