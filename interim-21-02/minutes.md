# HTTP Working Group Interim Meeting Agenda - February 2021

* [WebEx](https://ietf.webex.com/ietf/j.php?MTID=mde981c219c6c58efccdbd8f1ab718440)
  - Meeting number: 185 939 4156
  - Password: gogogopher
* [Meeting chat](xmpp:httpbis@jabber.ietf.org?join)
* [Minutes](https://codimd.ietf.org/notes-httpbis-21-02)

*Taking minutes? See [our guide](https://github.com/httpwg/wiki/wiki/TakingMinutes)*

## 9 February 2021

There are official RFCs now for Structured Headers (RFC8941) and Client Hints (RFC8942)

### Active Extension Drafts

#### [Extensible Prioritization Scheme for HTTP](https://tools.ietf.org/html/draft-ietf-httpbis-priority) - Lucas

Lucas:
* At 0 open issues, with -03 published
* Haven't heard much from implementers

mnot: Do you think we're ready for WGLC?
Lucas: I'll take chair's steer here, and don't want to rush it
mnot: I don't think it's urgent to ship this
Tommy: Seeing implementation results would be helpful
Alan Frindell: Has there been any interop yet?
Lucas: If anyone can help with the testing that would be appreciated
Bence Béky: As an update from Chrome, we don't have a lot of feedback
* Our current H2 dependency 
* Current implementation considers the weight, but I do not expect a change in performance
* I'm not asking to hold on until we have implementation experience
Tommy: If you have any measurements, that would give us the confidence we need
Alan: We might have something to show by March IETF
mnot: Chairs will discuss about the next step in process, which may be WGLC

#### [Signing HTTP Messages](https://tools.ietf.org/html/draft-ietf-httpbis-message-signatures)

Justin Richer: Not many updates, but it's been hard to get in touch with our lead editor
* First round of surgery changes done back in December ready for the next steps
* Document now explicitly uses structured headers
* Next steps are to further work on the algorithm for both client and server
* Still some outstanding questions, including multiple signatures
* No implementation yet but I intend to work on it
* Outsiders to HTTPbis are interested in this, e.g. Mastodon project
mnot: It'd be great if they would come and participant instead of forking
Justin: This is not a philosophical fork, just the way that community works
mnot: Sounds like you have hit a few bumps but have the motivation to continue
Justin: My next plan is to make an editorial cleanup now this is a working group draft
* Then to further the work Annabelle started when moving to structured headers

#### [Digest Headers](https://tools.ietf.org/html/draft-ietf-httpbis-digest-headers) - Lucas
   [Slides](https://httpwg.org/wg-materials/interim-21-02/digests-21-02.pdf)
Lucas: Since October is mostly editorial changes, with no new version pushed
* Thanks to Julian for his analysis
* 2 Issues that need input:
  * Digests in Requests
    * We have a difference in opinion, what does "Digest" mean in requests?
    * There's a cluster of issues that need to be unstuck
    * As an example, uploading different ranges of a large file with resumable upload
    * It wants to use digest to validate the integrity of each chunk
    * http-semantics has been updated to include the sever MUST ignore Content-range with a method that does not define it
    * Possible path forward is to apply Digest to representation data
Julian: I would be helpful if we had real world examples
* What do you mean by partial request data?
Lucas: For example if you want to send ten bytes, but sent the first two, the digest applies across all ten bytes.
Julian: I don't want asymmetry, I want consistency so that requests and responses are treated the same
* The obvious answer is to pick one, but I am not yet sold on range request the Digest applies on the entire resource
Lucas: It has been useful in the past for me to use HEAD and reading the Digest to verify the integrity
Julian: I'm not sure flipping 
Roy: There is no way you'll ever resolve this, it will have to be split up
Lucas: I don't want to break a lot of existing implementations
Martin Thomson: I was wondering if asymmetry is something we can live without, and apply Digest to the content not representation
* We don't have to deal with PUT - PUT might be the only method that selects a representation and partial PUT is an odd duck
* Julians comments nailed it for me - what does an implementation have to make this decision: a server can know what the selected representation contains; a client is never asserting anything about the contents of a resource, it's only guessing or asserting and that representation might never exist
Justin Richer: I got to the end without not being clear if I need to do something to my response before calculating the digest?
* How do fix this without impacting http-semantics?
Lucas: The trouble is that its hard to get your head around
* From the perspective of a HTTP layer, "representation digest" would vary based on the content negotiation
* We risk going back to Content-MD5 without interoperability
Justin: Most of data I need to sign will be serialised JSON in memory, not a file, and I need a clear way to protect that
* The spec may have to take into consideration natural asymmetry
mnot: I'm not sure payload digest is the one you want, we should work through the use cases
* Also consider Roy's suggestion of separate headers for Digest, and Content-Digest
Lucas: Is this undeployable without both headers?
Julian: Maybe we need to realise the spec is too ambiguous and can't be rewritten without breaking someone's implementation.
* Are deployments of Digest widely deployed?
* We should test if implementations of that specifications are widely deployed
Brian Campbell: If the Digest spec could be more declarative about what is being fed into the digest calculation, as it's very difficult to grok.
* At least be clear in the document for regular people to document
* More examples would be helpful too
Lucas: It's tricky, I don't want to have to describe all the semantics
* Dealing with old algorithms
* In summary, we want to update the IANA registry as the status is confusing
* For the sake of simplicity just to keep known good algorithms, and deprecate (MUST NOT) all others
mnot: This is a fine approach, keep it simple, but consider "deprecate" instead of "obsolete"
Lucas: I wonder how much toe-treading we are doing with our IANA expert
mnot: AD decides on the new expert, we can talk about that
Martin: TLS have "recommended" column, maybe we should consider that but this is the right outcome
Sawood Alam: Git uses SHA-1, as well as archiving and wondering why its deprecated here
Martin: There's plenty of reasons why, but if there is a concern about collisions it shouldn't be used
Lucas: Should we have "id-" prefix on all digest-algorithms?

#### [RFC6265bis](https://tools.ietf.org/html/draft-ietf-httpbis-rfc6265bis) - Lily
[Slides](https://httpwg.org/wg-materials/interim-21-02/6265bis-2021-02.pdf)
Steven Englehardt: We have 29 open issues, with some falling into some needing deferral, consensus, changes to security mechanisms, expiration and eviction
* Interop issues fall into three categories
  * Syntax and Parsing
  * Access via non-HTTP APIs - e.g. SameSite
  * Domain Attribute Semantics - e.g. What happens when localhost is specified?
Lily Chen: Recent changes
* Parsing with SameSite - this lead to Firefox being aligned with Chrome/Safari
* SameSite vs cross-site with redirects
* Call for Adoption for Cookie Incrementalism received strong support
* Rewrite of the http-state test suite is complete

#### [HTTP/2 bis](https://tools.ietf.org/html/draft-ietf-httpbis-http2bis) - Martin
[Slides](https://httpwg.org/wg-materials/interim-21-02/http2-2021-02.pdf)
Martin Thomson: Not a lot to report
* New version submitted
* Cory Benfield is enlisted as editor
* Proably Not:
  * Static HPACK Table - This would require updating HPACK as well as others
  * New ALPN
  Tommy: Let's just put "nope" unless something crazy chases
  * Cut Server Push - This depends on changing the ALPN
  mnot: I'm aware that splitting push into a separate document would just cause editorial work
  Ian Swett: Adding some notes about cache limitations and client support would be helpful
  Lucas: I agree about the editorial work, given the state machine
  Eric Kinnear: Default disable would be totally acceptable
  Mike Bishop: I think its acceptable to disable it unless you use it, lets default to off and move on
  mnot: I can work on a pull request
* Probably
  * Guidance for new field design regarding compression
    mnot: My only concern is where this might be read
  * Do we want to add that much text to the spec?"
    mnot: I will try to condense the text
    Lucas: Will we want to move the Cookie Crumbling text?
  * Frames with multiple errors
    Martin: Does anyone have any concern about making normative changes here?
    Cory: I don't meaningfully disagree with Martin, the easiest solution would be use the lowest numerical error code as an example
      * Anyone wanting real clarification here isn't going to get it
      * I also oppose "most appropriate error code" without clarification of what appropriate means
* Untriaged
  * Consider loosening requirements for clients to rejest connection specific header fields
    Martin: Looks like an intermediary acting more like a tunnel
    Cory: Do we know what the current state of browser behaviours?
    Martin: This will go into the "do nothing" box
  * Design for 0-RTT
    Martin: It's possible but I don't think anyone wants to do it
  * Partial remove of priority signalling
    Martin: Effectively old-spec implementations will send these frames, and new implementations will just discard them
    Cory: This intersects with Lucas and Kazuho's priority draft
    Martin: Given the progress, it might be worth making a pointer
    mnot: I think we should have a consensus call on the list
    Tommy: Does this PR reference the old version?
    Martin: It does, but it's a tombstone not a normative reference
  * Upgrade mechanism
    Martin: I don't think anyone has implemented it, and we could do the same "tombstone" trick
    Ian: We should probably just remove it
  * Reserve codepoints for greasing
    mnot: If folks could gather data on these, that would be helpful
    Ian: Ways moving forward on that will be difficult, I would like people to take a look at this and determine if they could deploy it on their stack
    Alan Frindell: This is hard based on our previous experiences of WebSockets
    Ian: We enabled WebSockets 2 or 3 times as well, and rolled it back

## 11 February 2021


#### [bcp56bis](https://tools.ietf.org/html/draft-ietf-httpbis-bcp56bis) - Mark


### HTTP Core

* As needed - issue discussion

### Proposals

* 10 min - [CDN-Cache-Control](https://tools.ietf.org/html/draft-cdn-control-header) - Mark


