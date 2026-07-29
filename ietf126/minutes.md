# IETF126 HTTP Working Group Minutes


## Resumable Uploads for HTTP - update

Marius Kleidl: there have been many small changes since last WG last call.  Consult the draft for list of changes. 

Marius: We had to remove the section about integrity digest; it felt more like a theoretical exercise than a practical feature. Lucas posted about this on the list. 

Tommy: Given the changes so far, has anything that would affect interop been reflected in folks' implementations? or do we want some time for implementations to update?

Marius: Apple's stack has been caught up, I have to update mine a bit but the changes have not affected interop and need not delay the processing of the draft. 

## Cookies: HTTP State Management Mechanism

Mark: RFC 6265 revision - that is in the final review phase (recently AUTH48, name changed).  Refactoring the cookie spec, more reasonably talks about what goes on the wire. 

## The Preliminary Request Denied HTTP Status Code

*Mark Nottingham*

Mark: My spec, I'm virtually on the floor. Not a lot of discussion. Core text is stable. We DO need to choose a status code for it!  In the 4xx block, we talked about 419.  We found one squatter, talking to them hasn't concluded.  Do folks think we should use 419 or try to find another.  Do I hear a bid for 419? Great, we'll send a message on the list to see if we get any objections, but we have support in the room for 419. 

## Secondary Certificate Authentication of HTTP Servers

Mark: We're going to kick off a WG last call for this on the list, with vague support from the room.

Mike: We have been working on this for a while. Please send to WG last call (speaking as author).  I'll read it myself as it has been a while since I've read this version.

## Template-Driven HTTP CONNECT Proxying for TCP

*Ben Schwartz*

[See slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-connect-tcp-00)

* issues listed as closed per slides
* One still in discussion on FINAL_DATA #3422

Benjamin: Asking chairs if this is the revised I-D that was needed, or if we need to redo WG last call.

Mark: We'll do a notification to the list but not a full redo of last call.  We can do our chairs review, IETF last call, and IESG, which gives opportunity if somebody's issue was missed.

Benjamin: The open issue is about shutdown of connection in an unclean way, and some consequences of that. There are interesting implications related to resource utilisation.  The TCP state machine can end up in a state where one side or the other is holding onto resources open for several minutes. 

David Schinazi: it's fine to me.

Tommy: I'll work on shepherd write-up.

David: IANA is expert review, so anybody in the planet can request provisional, and it becomes permanent if approved.

## HTTP Signature-Key Header

*Dick Hardt*

[See slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http-signature-keys-00)

Dick: [gave presentation]

Mark: I don't think we want to go to deeply into identity in this group, but this still might be a suitable home for this group. 

Dennis Jackson: If this group takes it on it will need to be done carefully, with attention to security properties. But it looks really useful. 

Mark: From a .well-known URI perspective, I want to make sure that the reference isn't a foot-gun.

Dick: The different parties have their own .well-known, the code verifying the signature doesn't necessarily need this.

Ted: I read the spec and section 4.6 may need a little extra explanation of, if you understand both, how you resolve that.  

Mark: We're not doing a call for adoption right now, just vague interest  

Poll: 16 vaguely interested in adopting, 20 no opinion. 


## Using QUIC Stream Resets with Partial Delivery in HTTP/3

*Marten Seemann*

[See slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-reset-stream-at-in-http3-00)

Mike: It could be your HTTP stack that generates status code. So if you're getting an application layer response, then you send a close, because that is your complete response. If you don't generate a response and did not process the request, you reset with H3 connect.

Benjamin: If we are using TCP, the H3 Connect error will be converted into a TCP reset. It has the same semantics as classic quick reset.  The result is the data you're trying to protect will be dropped anyway.  I think this is valid.  you're welcome to do this. 

Martin: You're saying it doesn't work in the client to proxy direction, right?

Benjamin: It's symmetrical. Clients are just typically more likely to have the application consuming TCP plug directly into the HTTP stack. But that's not a requirement.  Anyway I wanted to confirm there's no proposed change to the Connect TCP draft here.

David S: I was just checking RFC9293 and it says that if you get a reset, any socket call must fail.  We're cutting out use cases that don't quite work.  So, taking a quick step back, we happen to put stream metadata that's is critical to connection state in the stream data, because we didn't have a way to tack on. If QUIC had been built differently, we wouldn't need this.  The ones I find compelling, are sending header frames and make sure that gets across and nuke the rest.  I don't think this quite matches HTTP semantics.

Tommy: I think I agree with what I heard so far.  If we are talking about CONNECT we should talk about extended CONNECT and variants thereof.  This might be useful for the doc, and later we can discuss what stays in and what stays out, but give some guidance to clients how they make use of this. Is it for error logging/reporting, or is there some action?  That would help us evaluate which cases make sense, not just because you *can* do it but because we *want* to do it.

Mike: with h3 editor hat on: Everybody's favourite feature is HTTP PUSH< which I know all of you have fully implemented. [laughter].  So the server sends a push promise, with the push ID and header. But if that unidirectional stream gets reset, then the client will SEE that push promise has never been fulfilled. If this were available in QUIC we would have used it.

Martin: Do you want me to add that to the draft?

Mike: Please.

Mark: [as me, not chair] I've always been uncomfortable about connection layer errors rather than HTTP semantic errors.  We need to be super clean considering what belongs at what layer.  The semantic errors do survive end-to-end, the connection stuff tends not to.

Mark [as chair]: It seems like there's interest, Martin is willing to work on the draft, let's continue discussion on list. 


## HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding

*Erik Nygren*

[See slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http11-request-smuggling-defense-using-cryptographic-message-binding-01-version-of-draft-00)

Erik presented slides

Chairs: Any interest?

Ben S: I'll repeat something I said on the mailing list: do we think this is something that can be implemented on top of an unmodified HTTP1.1 implementation? If the underlying implementation can be modified, then presumably one could just use HTTP2. 

Erik: I intend to try and see how much code change is required to implement.  There's a big shift between HTTP1.1 and HTTP2... some implementations do that as a translation layer anyway, which is a source of some of these problems.  Before going too far with this, and possibly before WG adoption, I do think it would be worthwhile testing if this can be a small enough implementation change.

Ben: I do think it *can* be implemented on top of a HTTP1.1 stack. It can't defend against modification, because it doesn't know the message or message length. There may be other cryptography we could use here, like a non-hash cryptographic MAC or stream cipher to indicate what counter this is. 

Mark [speaking as myself]: The problem here is widely acknowledged and serious. From a deployment standpoint, beyond the concerns Ben had, it seems it adds overhead, risk (if youg et things wrong it breaks hard). What do you see the deployment scenarios as?  How does it add value to folks? does it get built into Apache? deployed behind CDNs/

Erik: I see the big use case between a CDN and a customer.  Getting implementations into apache, nginx is where the big value would be. Modern deployments today with front layer proxy, like haproxy or nginx, in front of some HTTP1.1 API service, sometimes implemented in python or javascript library... could defend stuff built on that path.  The big risk is many of those patterns do have a HTTP1.1 hop in them, and have legit clients and malicious clients on the same downstream connection.  Saying "don't use PCONN" might not be realistic for them to deploy. It's not worth doing unless there's a critical mass of implementors interested, and that depends on low complexity.

Dennis: Your draft references HTTP-synch an academic paper, but you stripped it down to be more deployable?  
Erik: They were convergent evolution. The author works at the same company i do. 

Dennis: It looks like the attacks these defend against are distinct.  The paper says what things are fixed and not fixed. The same would be good for this draft. 

Erik: Agreed, it's not worth it unless enough CVs are addressed.

David "Shoving weird crypto into http" enthusiast: With my other hat on I sometimes work on OS, smuggling is a sizeable number of the attacks we're seeing. I support work in this area. TLS exported authenticators make peoples' heads hurt.  So I do support this work, and I recommend having a response to the first message in your init message. It will help you then.

Erik: we do need indication ahead of INIT that you do support this, otherwise there's a risk an attacker can send the INIT directly, smuggle it through in a way that causes problems.

Chris Lemmon: I want this to exist, and I want it to HAVE BEEN deployed. I think the story you're telling around making this simple to add to libraries, so as a security professional I can say, "Just patch your nginx" or "just patch your go library" and "don't turn off the flag that says enable this".  Then we can build an ecosystem that winds up in a more secure place as people deploy this. I'm seeing a massive amount of bundling attacks. 

Yutaka Oiwa: I've been working on smuggling attacks since 20 years ago, and had a solution 20 years ago. But so many implementors are just using libraries.  Maybe this time, moving to HTTP 2 definitively secure, is a more reliable solution.

Mark: It sounds like there's strong interest and also concerns about whether we can be successful. Erik please continue working on this and bring back to us, I can see a call for adoption in the future. 

Tommy: I agree, we have energy here.  I'm curious to hear if anyone in the room today would like to see certain properties addressed before you'd be in favour of adoption? 

Erik: if implementors are interested in being co-authors, I'd be very interested in that. 


##  A Perfect Forward Secure Extension to Oblivious HTTP

*David Schinazi*

[See slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-ohttp-pfs-key-config-00)

Dennis: Nothing changes about the first request, right? Isn't that the request I really care about?

David: It depends. The first request and response often set up the channel and what you want to talk about.

Dennis: But also authentication material and other fun things.

David: Because it's not just a single gateway, the client might hit a different region, those keys have much more opportunity to leak. I think there's a measurable security increase. 

Dennis: I think there's an awkward mismatch in demanding both 0RTT and PFS.

David: Yes. I mentioned this. "If you're doing bidirectional, just use TLS".  I got the answer "We absolutely need 0RTT".  It seems to be what people using OHTTP really want because if they didn't they would just be using TLS over CONNECT. 

Dennis: This would need careful review.

David: Agree. I want to pick your brain about doing this in TLS. I highly doubt th t's easy.

Kazuho Oku: working at a company that already supplies chunked gateways, it's hard to explain this to customers. I hope PFS will be applied.  It's an application choice.

Martin Thomson: I find cognitive dissonance .  Applications can decide the right things about RTT but not the right things about other subjects? I'm interested in exploring the idea Dennis raised.  I'd like to uplevel and say, what are the use cases for this?  Chunked -> bidirectional was an unfortunate consequence.  If people are starting to use this and don't want to use TLS, I think I might prefer to fix TLS than take this path.  If we can educate users about the non-PFS-first-flight, perhaps we can educate them about "Hey, there's CONNECT"

David: HTTP gateways may be easier to deploy than CONNECT.  I don't know if that's true for chunked.  The people doing CONNECT are in one part of the company, and doing chunked in another.  Google quick crypto had non-linkable 0RTT.  But you needed a way to actually bind your HPKE key.  I'm happy to chat about that. If that's easy, then I agree, but I just can't see it.

Jonathan Hoyland: If you're doing interactive chunked messages, then aren't you already in quite a bad place security wise? You lose quite a lot of the oblivious guarantees? 

David: I think the only thing you're leaking is the latency between client and server, and that's nowhere near as bad as leaking the client IP address.

Jonathan: I was looking at the chunked HTTP security considerations, and the attack is somebody who can see both sides of the connection can identify which packets are related to which customers.  

david: Take Google safe browsing; we want to offer this to customers with a guarantee that we have no access to the IP address. We're not trying to defend against state actors with access to both sides.

Ben: I'm skeptical for the reasons Dennis said.  Offering partial-forward-secret-partially... 

David: This is the same primitive as with TLS1.3 and 0RTT.

Ben: I'm not sure they're directly comparable. Every user is possibly doing 0RTT under a different key in TLS1.3.

David: That's true, but if we have unlinkable 0RTT, we're going to have that as well.

Ben: My employer has a clear and high-priority use case that almost matches what you have hear.  Whatsapp private processing, we've published a paper on this.  Private Compute enclave, to try to get the privacy property you're trying to get here. We've done this in production at some cost, there's got to be a better way. There's a recurring problem here across several companies. 

David: Please put a link to that white paper in the chat.

Chris Wood: THanks for writing this up, I think it's useful.  Doing this in HTTP or TLS, I think this is a trivial enhancement to what chunked provides. I think we have the expertise.  It's much simpler than shipping OHTTP in production. Frankly doing new things in TLS these days is hard for other reasons. I'd like to explore this route.  

Mike Bishop [as AD]: We maybe closed OHAI prematurely, though I don't think we knew this at that time.  I understand the time it takes to take stuff to TLS.  At the same time, there's a reason OHAI was in the security area. I'd want very thorough review from the security directorate, and more thorough proofs than we usually do.  

Dennis: For the TLS 0RTT thing, I think there would be wider use cases for browsers. It would be nice to have one transport that did both things.  I don't think it's great that we reimplement TLS at another layer, one feature at a time.  

David: I have shipped chunked HTTP, and I won't shift those people to TLS.  let's chat more. 

Tommy [wearing no hats]: Overall we have uses cases that we really want to be 0RTT and fully unlinkable. We should understand more, for the bidirectional active stream, how much do they really really need the 0RTT beginning? I understand CONNECT is trickier because of CDN setups, but what are the actual technical problems? 

David: Note this works just as well for regular HTTP without the chunked. I think there's cases where that matters, like requests with an OAuth token that is scoped in time.  If the key in the request leaks a day later, that's less sensitive than the response with sensitive data actually is.

Mark: I'm hearing a level of interest in this, also concerns around use cases.  Discussion needs to continue. No doubt we'll have you back here again.  


## An Extensible Key Configuration Format for Oblivious HTTP 

[See same slides as above, David presented]

Mike: we should justify the content-type change based on work we want to do, not for client bug.

David: No, its that as long as we're updating clients, there's a feature we could add.





