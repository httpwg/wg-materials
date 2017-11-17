Friday, 17 November 2017
9:30-11:30 Morning session I, Canning - in other time zones
Administrivia
2 min - Blue sheets / scribe selection / NOTE WELL

3 min - Agenda bashing
Active Drafts
balance of time

Using Early Data in HTTP

Random Access and Live Content

Expect-CT

Header Common Structure
Possible replacement: Structured Headers


Cache Digests for HTTP/2 - presentation

Client Hints

RFC6265bis: Cookies

BCP56bis



## Expect-CT
https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct

Emily sent a summary.

MNot: Seems like a bit more implementation experience would be useful


## Early Data in HTTP
https://tools.ietf.org/html/draft-ietf-httpbis-replay

MT: I think this is a done.  Lots of input from the WG with 3 implementations.  Seems to work and TLS 1.3 is about to go out.

EKR: Basically Ready

Tommy Pauly: Do we want a mention of TFO/TLS?


## Random Access and Live Resources
https://tools.ietf.org/html/draft-ietf-httpbis-rand-access-live

MT: For an experimental draft, this is plenty of testing.  

Darshak Thakore: Should we go to last call for this?

Mnot: Should we give more time to give implementers more implementation experience before last call?

MT: Document and testing is high enough quality that this doesn't need to be experimental.

MNot: Would like to get Apache, CDNs, Varnish team themselves to take a close look at this as well.

Ted Hardie: How does this work if the beginning of the content expires?  How do you know the last possible moment you can go back to?

Craig Pratt: As long as there's some overlap, you should get partial content.

MNot: Ted's question brings up the next question.  Now that we're comfortable with the safe, do we think this will be cache-friendly?


## Structured Headers for HTTP
https://tools.ietf.org/html/draft-ietf-httpbis-header-structure

MNot: Putting aside the details, is this the general direction we're trying to go in?

Kazuho: I really like this draft and think it's a good direction.

Patrick McManus: Asks how many people have read the current draft and the former?  Like 6 people.  

MT: A lot more folks who aren't here have read the drafts.  Thinks this draft is much more promising than the other draft.

Patrick McManus: Previous feedback was this was 'too big' and this was an effort to narrow the scope of this.

Mnot: Encouraged by the level of engagement on the list.

Michael ?: Was there any reason not to have a length?  Thinks 

MT: If we were to retroactively apply the rules to new headers, you probably should use these practices.

Julian Reschke: Relayed from jabber: I think this goes into the right direction. Would be good to decide on adoption soon.

Yoav Weiss: Better structure would provide much better HPACK compression and releive the pressure to give new params short names to save bytes. 


## Cache Digests for HTTP/2
https://tools.ietf.org/html/draft-ietf-httpbis-cache-digest

Sebastian Deckers: Is there any intent to add signaling when a cache entry is inserted or expired?

Kazuho: The server can assume once a resource is pushed or requested, it should be in the client cache.

Mike Bishop: A single simple filter seems like the right approach and it's not supporting multiple.  On the 

MNot: Yoav, are you wearing your 'Chrome' hat?

Yoav: To some extent yes.  Chrome and Akamai.

MNot: If there's a good chance of getting browser implementations, that'd be a good development and I could take my name off the draft.

Sebastian Deckers: Did an experimental prototype with a service worker, and the results were very positive.  Thinks we should move forward.

Patrick McManus: Labeled as experimental.  Kazuho, what would you like to do?

Kazuho: Best option would be a or c.  

Mnot: Does it make sense to publish document with headers and service workers and keep it experimental?

Yoav: Replacing GCS with Cuckoo filter seems like a good change for reasons mentioned.  Not seeing GCS being adopted.

Sebastian Deckers: No real opinion on GCS vs Cuckoo, but do have a hackathon experiment to compare them.  If that helps?


## Client Hints
https://tools.ietf.org/html/draft-ietf-httpbis-client-hints

Update from Ilya Grigorik, who is not here today.

MT: There was a conversation about the Geolocation header?  Where are we going long term?  Geolocation is an awesome test, but a terrible thing to add.

EKR: What is the experiment?

Yoav: Regarding geolocation and privacy, at some point we need to distinguish between active content and passive content.  Add something to feature policy to select 3rd parties instead of everyone.

EKR: This obviously has a privacy implication, and everything you leak has implications.  

Mnot: In terms of geolocation, we should not be adding new things to this document.

Yoav: Re EKR's points, this is not about sending user private info everywhere.  

Brad Lassey: If the user is opting into providing information, how is that an unintentional leak?

MT: If the site asks for something once, then it's now being provided on every request forever.


## Cookies rewrite
[RFC6265bis: Cookies](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis)

Mike is not online.

MT: Having a discussion internally about cookie expiration.  Different browsers have different policies.  

