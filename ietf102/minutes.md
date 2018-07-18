HTTPbis WG
Tuesday, 17 July 2018 1550
Chairs: Patrick McManus and Mark Nottinham
Minutes: Paul Hoffman
	Words from the slides not duplicated here

Active Extension Drafts

HTTP Representation Variants - Mark Nottingham
	https://datatracker.ietf.org/doc/draft-ietf-httpbis-variants/
	One person indicated that they might implement
	One cache has implented, another has intent to implement
	Patrick: Park this doc for an indeterminate period time

BCP56bis - Mark Nottingham
	https://datatracker.ietf.org/doc/draft-ietf-httpbis-bcp56bis/
	{{ No slides }}
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

Secondary Certificates - Mike Bishop
	https://datatracker.ietf.org/doc/draft-ietf-httpbis-http2-secondary-certs/
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

Structured Headers - Mark Nottingham
	https://datatracker.ietf.org/doc/draft-ietf-httpbis-header-structure/
	Martin: These things go on the wire ordered anyway
		But processors don't need to follow the order
	Julian: What characters are allowed in identifiers?
	Would like to ship by IETF 103
	Commitments to review: about four
		
Cache Digests for HTTP/2 - Kazuho Oku
	https://datatracker.ietf.org/doc/draft-ietf-httpbis-cache-digest/
	Intend to keep this open

Client Hints - Mark Nottingham
	https://tools.ietf.org/html/draft-ietf-httpbis-client-hints
	Just started WG Last Call for three weeks
	Experimental because only one browser 

RFC6265bis: Cookies - Mike West
	https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis
	Not much document progress since last meeting
	Implementation progress

Proposed Work

The "SNI" Alt-Svc Parameter / HTTP Alternative Services via DNS - Mike Bishop, Ben Schwartz
	https://datatracker.ietf.org/doc/draft-bishop-httpbis-sni-altsvc/
	https://datatracker.ietf.org/doc/draft-schwartz-httpbis-dns-alt-svc/
	Ekr: Why would an alternative server send me a new SNI
	Mark: Doesn't require the alternate to be named in the cert?
		Mike: Adds a "concieled option"
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
	Mark: Who is interested in continuing discussion DNS ALTSVC
			Reasonable
		Who is interested in continuing discussion of Alt-Svc SNI
			Slightly less

CDN Loop Prevention - Nick Sullivan
	https://www.ietf.org/id/draft-cdn-loop-prevention
	Martin: Concerned about privacy, but the alternatives are worse
		Use opaque identifier
	?: Likes the Forwarded header is better with "by" field.
	Leif ?: Would like spec to be useful for cross-CDN and intra-CDN
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

HTTP-initiated Network Tunnelling / HELIUM - Lucas Pardue (remote), Ben Schwartz (slides)
	https://datatracker.ietf.org/doc/draft-pardue-httpbis-http-network-tunnelling/
	http://tools.ietf.org/html/draft-schwartz-httpbis-helium
	Ben: HELIUM was covered in DISPATCH
	Mike: Likes the architecture and problem statement
		Maybe don't want the transport part here
		Maybe form a new WG for the combined set
	Erik: There is a lot of transport stuff here
		IPsec over UDP covers a lot of the use cases
	Jana Iyengar: Google already has such a use case
		Useful
	Ben: DISPATCH chairs want it in DISPATCH

Related

H2 Server Push Data - Aman Nanner
More H2 Server Push Data - Brad Lassey
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