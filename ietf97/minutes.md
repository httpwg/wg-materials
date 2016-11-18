# IETF97 HTTP WG Minutes

## Session I

*Minute taker: Pete Resnick*

### Start of Meeting

Welcome Patrick as new co-chair

Agenda Bash

Today is about already adopted docs

Mike Bishop: Move draft-bishop-httpbis-http2-additional-certs, which depends on TLS, to Thursday - OK

Announcement of "Bar" BOF on DNS-Over-HTTP this evening

Mention of QUIC - please participate, will be coordination with HTTPBIS

###  draft-ietf-httpbis-cache-digest

Recent discussion - editors suggest target should be Experimental; implementer community is not focused on this now.

Would need to add an appendix re: working with ServiceWorker

Open issues list review

Martin Thomson: Doing this as a setting is not a good idea. Concerned that the experiment will not learn anything.

Mike Bishop: PUSH is not very viable without this; frankly I don't have time to invest in an implementation.  Experimental not a bad idea.

Mark Nottingham (from floor): Agree that push needs to be worked on, but would really like to see this.

### draft-ietf-httpbis-client-hints

Ready for Last Call

Martin Thomson: Reminder that this is Experimental, lower bar

### draft-ietf-httpbis-encryption-encoding

Martin Thomson: Would like some review in this group re: out of band content encoding

Julian Reschke: Minor concern that there are other specs that want to build on this. They'll all have to come up with ways to martial the key; is that good? Spec currently talks about key ids. Needs some more discussion about how they are to be used.

Martin will work on that prose - Hoping for quick WGLC. The WebPush folks are OK with changes in here.

Patrick: Is there a larger discussion to happen regarding self-describing?

Martin: Push discussion to Thursday. Do we need a document on this?

Julian Reschke: Next revision of ??? should have some discussion

Mike Bishop: Offered to work on this

### draft-ietf-httpbis-http2-encryption

Martin: One concern was whether this should be done for 1.1

Erik Nygren had a concern about whether origin framing would be sufficient for this

Mike Bishop: Is the concern about the server getting confused, or that they're both in the same crypto context. Not aware of a real security threat.

Erik: It really depends on what the default in.  (ie, allowing the origin to opt-in to mixed resource with origin frame is fine.) security is the concern

Martin: The issue is whether you can combine context from secure and non-secure origins

Erik: I only see the ORIGIN frame being a good option to address the security concerns before the client tries to mix.  Otherwise it is opening up a risk/exposure until the server says "ok to mix".

Martin: The mixing is the question. (Patrick paraphrases: When is an opt-in not an opt-in.) This is getting very complex without real benefit.

Erik: I think ORIGIN frame, .wk, and a SETTING are all fine ways to allow servers to indicate that it is OK to mix schemes.

Erik Nygren: any of those are sufficient as long as it is opt-in from the server.

### draft-ietf-httpbis-rfc5987bis

Presentation: https://www.ietf.org/proceedings/97/slides/slides-97-httpbis-sessa-julian-5987bis-00.pdf

Ready for LC writeup.

### draft-ietf-httpbis-jfv and draft-kamp-httpbis-structure

Presentation: https://www.ietf.org/proceedings/97/slides/slides-97-httpbis-sessa-julian-5987bis-00.pdf

Mark Nottingham (from floor): Don't think the ??? problem is solved. Don't know that this needs to be published in WG; maybe ISE. Having more than one document published by the WG is not good.

Patrick: We should publish what's good, not publish for the sake of publishing

Martin: Not worth publishing jfv

Poul-Henning Kamp: my draft is an exploration of existing rfc723x headers, to see if a they have a common structure we can use going forward.  It can be made general and replace JSON, but main benefit probably to prevent parser proliferation going forward.

Julian: The WG has encouraged the reuse of existing ABNF (e.g. Prefer header). We should also answer the question of whether we want these sorts of header fields. Also, we could solve by simply deciding that non-ASCII in headers is OK. Answering these questions might address the issue.

Poul-Henning: Don't think we should have non-ASCII headers. If my proposal works, fine, if not fine.

Chairs: Sounds like we're considering adoption; could do so for purposes of discussion, even if we don't go forward with these solutions.

Martin: If this is simply a matter of unifying the header field format, great. But people seem to be looking for something else as well (e.g., more byte-efficient format, more efficiently-processed format), but that's not we're addressing now. More investigation needed.

Mike Bishop: A common structure will lead to these addressing these other desires.

Poul-Henning: The recursion stuff is severable. For private headers, you could indicate "common structure" in the brackets. Also optional. Agree with Mike's point about needed a structure to get compression et. al.

Mark (from floor): Continuing down the path should be interesting. Need investigation and discussion. A big part of this is dealing with error handling.

More comments from Julian and Poul-Henning. Chairs conclude there is interest in the room on the topic. Question to the room:

*Who thinks that a common header policy is a reasonable path to go down? A stronger hum for it is reasonable to go down, a weak hum for objection or don't have enough info.

Ted Hardie: I was in the "need more info" group. No great objection, but probably best to leave this individual until the investigation of "point bits is complete.

Julian: We need to define scope. Data types might not be ready to go yet.

???: I have difficulty with abstract and unproven syntax being used as a future protocol guideline. But I see no reason not to explore various alternatives as experimental work.

Joe Hildebrand: Is this far enough along to focus discussion?

Mark (from floor): Yes, JFV focused investigation, we should drop that and move to the next bit to focus.

Joe: Reducing number of parsers in future is a good thing.  Doing this great in H2 and just OK in HTTP/1.1 would also provide another reason to switch to H2.

### draft-ietf-httpbis-origin-frame

Mark gives short introduction to motivation

Current thinking: Abandon the origin draft and come up with something simpler like "Only use this connection for what was used in the SNI."

Mike Bishop: It was cheaper to just implement coalescing.

Patrik (from the floor): Still believe in the full vision, but there is a pain point. This setting is a good way to address that.

Erik: given the oppsec discussion, we might need separate settings for each of  "allow_mixed_scheme" and "do_not_allow_mixed_origins" (since they have different details).  Still on the fence SETTINGS vs the more complex ORIGIN frame.

Martin: Not enough info to make a decision today.

Eric Rescorla: We could do something simpler now, and then build more complex later.

Mark: Not all clients will support now, but easy enough to do with a 1-bit setting.

Martin: 421 is a sufficient backstop

Mark: Suggest park this document for now, and then add to opsec document if need the 1-bit.

Erik agrees.

### draft-ietf-httpbis-rfc6265bis

Plan is to incorporate the drafts that have been accepted and bring to WG

No other comments

### Updates on calls for adoption

####   draft-stenberg-httpbis-tcp

Heard that people were interested in the topic, but sounded too much like a configuration guide

Tim W. is going to take up a revision to the document

#### Opportunistic Security

Presentation: https://www.ietf.org/proceedings/97/slides/slides-97-httpbis-sessa-oe-nick-sullivan-00.pdf

### Potential new work: Early Hints

Presentation: https://www.ietf.org/proceedings/97/slides/slides-97-httpbis-sessb-early-hints-00.pdf

Mark (from floor): We've had this problem over the years. This is an nice elegant trade-off. The majority use case is HTTPS, so interop worries re: intermediaries shouldn't come up. The target is the browsers, and this could be useful.

(Some thumbs up from the room to Mark's comments)

Mike Bishop: Our stack handles this, but our dev tools don't.

Patrick: Other implementations have been fixed, just because of the discussion on this list.

Julian: ???

* Sense of the room: Who is interested in implementing this? 5 or 6 hands.

Chairs' discussion: What's the appropriate level of work for the group?

Julian Reschke: Mapping HTTP to QUIC, where is that work taking place? Going to effect people in this WG, where ever it happens.

Mark: Could give feedback to QUIC about its architecture

Ted Hardie: Does work on DNS in HTTP, if the BOF goes well, come in here

Mark: Historically we don't bring in "X over HTTP"