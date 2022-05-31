# Minutes: HTTP WG / May 2022


Meeting is about the active drafts; we'll get to proposals and new stuff in Philly.

## Signatures

Justin: New draft available.  New more generic design for signing the request (or parts thereof) that elicited a response.  New IANA registry for parameters.

Martin: Why not drop "target" from the IANA table?

Justin: Was trying to retain the requirement for the targeting of the parameter to be specified when it is registered.  Seemed like a way to ensure that specifications covered it, but maybe we can just make that a requirement for new registrations.

Justin: Editorial updates, followed style guide.

Roberto: Multiple way to pass the target URI. Should we pick only one?
Justin: Application-specific what form makes sense.

Lucas: Questions about algorithms; taken offline.

Justin: Produced Java and Python implementations.  Some other implementations exist.

Justin: Please look at issue 2133.

Mark: Is it stable?
Justin: Core stuff is stable for a year or so.  Not including the request flag ("req"), but that is optional/additional.  People are building to the spec.

Martin: Issue 1864 is not addressed.  Assert that some conclusion to this issue is necessary because it changes the way that the signature input (not Signature-Input) is constructed.

Justin: Disagreement about mechanism, but not clear that we need the feature.  Proposed to drop it and rely on extensibility.

Roberto: As Yaron says, there are other issues, absence of a field and absence of a parameter is another aspect of this that needs work.

Mark: Does this apply only to new fields?

Justin: no, applications could have tighter requirements than HTTP definitions

Mark: when I define a field, if there is a distinction between present and absent that is relevant, maybe I can just encode that difference explicitly instead.

## Cookies

Reviewed issues, a few left.  No editors.

## Alternative Services

Mike: not a lot moving.  Lucas and Martin (Duke) wrote a draft about a QUIC version parameter.  Allows for broadening scope of Alt-Svc advertisements.  Not a lot of discussion.

Lucas: There was an announcement of the draft.  We were asked to defer discussion of this to Philly.  Waiting for that opportunity.

Mark: Definitely need to chat about this later.  Need to take a step back and look at the broader picture of how we version things, how we identify things.  Not that we have opposing sides, more that we don't have energy.  But it is confusing.

Mike: We messed up by using ALPN in Alt-Svc and now we're trying to work out how to live with that.

Mark: Maybe a side meeting.

Martin: SVCB grew up from Alt-Svc and transcended its origins.  Maybe we need to look at how that worked out and learn from it, define a new thing that isn't Alt-Svc, but fills the same niche.

Mike: Coalescing and transport use and versioning all tie together.  Not sure what we want.  Is the certificate enough?  What about the ORIGIN frame?  (Might have been nice to have ORIGIN: `*`)

Mark: ORIGIN: \* might be a footgun in some cases.

Mike: ORIGIN itself can be a footgun with changing configurations.

Mike: CORE puts authority on the cert and puts the DNS part as optional.  That suggests one answer that we don't say.

Martin: would be good to get clarity about coalescing

Erik N: THere are some that do some coalescing, but don't do ORIGIN, so you can't tell them to stop.  Not having all the features creates some issues.

Mark: Not a lot of MUSTs around the implementation of these things; they're extensions.

Mark: Looks like a side meeting is needed.

Mike: Also want to highlight multi-CDN.  Tension between having a long lifetime for QUIC support and a short lifetime to avoid having stickiness to a CDN.  Awkward.

Lucas: This isn't hypothetical.  Lots of failed QUIC connections coming to us sometimes when we have multi-CDN and QUIC isn't enabled for that endpoint.  Probably not something Alt-Svc can fix.  Let's look at this holistically.

Mark: Probably not going to end up being called Alt-Svc.

Tommy: We also need to integrate with SVCB.

Mike: What does that mean for Alt-Svc-bis?

???

Finit


## Client Cert Header Field

Brian HAS SLIDES!

Draft: -02 talks about retention on resumption (some implementations don't retain this state) and post-handshake authentication

Issue 1935: No mechanism for error signaling from origin to gateway as it relates to generating TLS errors.

Brian: Out of scope for this work.  Signaling happens at the application.  Though TLS alerts can be problematic, we don't need a solution for this.  Overengineering.  Inclined to close this out.

Mike: Inclined to close also.  This can happen even on single connections.  The server can get a valid certificate, but it might not be authorized.  You get a 403 in that case, not a TLS alert.  Close the issue.

Brian: This draft makes this problem more obvious.

Tommy: I agree with what has been said.  Might be worth some guidance text or notes.

Brian: A little weird.

Tommy: You mentioned this was Informational.  Isn't this Standards Track?

Brian: ekr had some concerns about injection attacks in case proxy doesn't sanitize properly.  Informational was a way to run that blockade.

Mark: Need to check call for adoption.

Mike: We seem to be landing somewhere in between.  CDNs do this.  Need to align behaviour, but maybe we don't want to recommend this as a "best" practice.  But it is not already what is happening, just what is necessary.  Experimental? (no)

Francesca (in chat): Sounds like informational.

Martin: address 1935 with text; would be happy with PS rather than informational if we properly make the security implications clear.

Brian: Happy to suggest text.

### Issue 1927: certificate ordering.

Brian: Originally OK, but had reservations after looking at the text.  Is the information a) what was presented by the client, or b) what was assembled into a chain.  Currently a little ambiguous in the text and that might be OK, not sure what implementations do with this.  Don't fully understand why you would include the chain anyway.  No way for the server(proxy) to convey a list of anchors that it accepts, because that creates new signaling.  Not even sure how that might work.

Martin: Two different possibilities here. Either the origin trusts the CDN to do all the validation (and just needs to know which cert for authorization) or the origin is doing all the chain validation, and the CDN is only checking the signature. Hopefully everything needed for authorization is in the EE. Don't preclude either -- just describe how info is conveyed.

Brian: Some disagreement about deployment models.

Martin: Suggest order from TLS or suggest order from constructed chain.  Don't be overly prescriptive.

Chairs will follow up on status.


## QUERY Method

Julian (not present) suggests a design team meeting

Will setup a design team.

## Retrofit Structured Fields

One open issue.  Cookies!

How do we signal cookie value type.

Would SF-Cookie omit the type parameter?

First inclination is to omit it, but that creates redundant information, which might end up wrong.

## Next

Asked for two sessions at the next IETF.

