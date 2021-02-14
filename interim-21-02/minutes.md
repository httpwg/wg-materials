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


### [bcp56bis](https://tools.ietf.org/html/draft-ietf-httpbis-bcp56bis) - Mark

Mark: Went to last call a long time ago, parked it. There's been substantial rewrites since then. Mark made recent changes to refer to core. Wise to do another WGLC since it has changed. Call for WG participants to file issues against it. Wants to WGLC in a few weeks.

Mark: Cache status ready for WGLC.

Mark: Proxy status ready for WGLC.

### HTTP Core

* As needed - issue discussion

Mark: 26 issues open. Editors believed 9 issues are worth discussing, but floor is open for other issue discussion.

#### Mark: Issue 751
* Mark: Wants Roy's comment here.
* Roy: The main reason this is a MUST is to encourage people to send the version they actually support. Worry that clients will send a "safe" version first and let a server indicate a higher version, and servers may do the same. Applies to intermediaries and origin servers. This worked, took only a small amount of time to go from 1.0 to 1.1. Could change that MUST to a SHOULD or make the change Willy requests but we need to recognise that the version of the protocol has this additional purpose.
* Mike Bishop: Thinks this requirement is fine for clients and servers. For intermediaries, they may not want to invoke everything that e.g. 1.1 supports if the client doesn't support 1.0 and so it can't stream it through. Makes sense to have a different requirement on intermediaries.
* Martin: Might disagree with Mike here given Roy's context. Endpoints that generate messages must understand the message they generate. Roy's point is very good in the 1.1 era, maybe less good in 2/3 era. But good in 1.1: pick the best version you have to make a request. Saying both things may be valuable here.
* Mark: Assumes this only applies to minor versioning in H1 because this is in H1 messaging. Maybe worth having intermediary-specific wording about requests when there are buffering considerations. Maybe we should just say the intermediary should add Via?
* Roy: Certainly that's what the design was.
* Mark: Intermediary is in control of its own destiny here.
* Mike: Proxys gonna do what proxys gonna do.
* Alan: Are we mostly concerned here about chunked and default connection keepalive, or is there some other feature it can't do? Upstream half of an intermediary sending a message that's 1.1 even if a client is 1.0, I'm agreeing to downgrade it myself, or I shouldn't send 1.1.
* Mark: Original design would append a Via header to communicate that the peer is 1.0 so the server knows.
* Alan: Is that a requirement? Are servers supposed to do that?
* Mark: No.
* Cory: Is anyone aware of any server that does this?
* Roy: Apache doesn't as we were trying to force that evolution. It does change its version back to 1.0 when it knows the client is not compliant.
* Cory: Maybe we should call this out more clearly then.
* Roy: Worth revisiting.
* Tommy: Martin in chat notes that we could keep the text and add SHOULD, then note why you may not. Seems like a nice way out.

### Issue 740, mid stream trailers
* Mark: Should mid-stream trailers be accommodated in the spec? Discussion started in the QUIC WG, added things into the core spec to allow this, no current version of HTTP has the capability to do this. This effectively changes the signature of what HTTP is: is that appropriate to do?
* Martin: Document very clearly described a protocol that was deployed except for this bit. This was a very jarring point in the document. Could be done as an extension: adopt an item in the WG that defined these semantics and defined extensions to the various protocols to realise this. Seems like a better approach. Sympathises with the annoyance about not being able to do this.
* Cory: Agrees with Martin, happy to see the WG adopt an extension.
* Roy: Agrees with Martin in every respect except for the desire to get it done. Wants the WG's opinion on this.
* Julian: It's a surprise that we put this into the core spec as in the QUIC HTTP work it was decided not to put this in H3 because core didn't define it. We defined it, but we were too late. Roy has pointed out that there is an H2 extension that does this. As it's been in there for serveral revisions, is concerned about dropping it as we're finishing work.
* Mike: Comes down to us not having a concrete extension point to do this for semantics. There are easy extension points for H2 and H3 if the semantics support it. Not a big fan, but if there are people who want it then having it in the semantics spec to say there may be a way to define this is not too far out of left field.
* Mark: Personal 2cents. H3 did not defer from doing this because it wasn't in core, didn't do it because there wasn't implementer interest. It was brought up, people said "that's a cool idea maybe we should do it someday" and interest was lost. There's already uncertainty about how trailers work, they're borderline unusable, don't want to add more fuzziness in the spec. We need interop in the spec. Preference would be at most to put a note in the spec that a future extension might do this, or if it must stay confine it to a note. Make it clear it isn't interoperable.
* Tommy: If we have an extension and someone wants to do it, nothing stops them even without semantics saying it. Would you have a strong objection to having it be pulled? Would that cause a problem for extensibility in the future?
* Roy: Extension would have to be independent of the existing stuff we have now. Not too bad, gives you more freedom. But we'd have to close down headers and trailers as they are today and revisit the text to do it.
* Mike: Not saying "we should keep this text", saying if the WG wants to pursue this then having semantics call out there may be multiple instances of field sections here is ok. If semantics says "there are exactly or up to 2" field sections period, and then we introduce a way to carry 3+, then not every client will be able to interpret that. In the semantic layer if we say "there are n field sections, though 1 is the most common" then we have sent a signal.
* Tommy: If 2 is hard enough, given so many people assume 1, is defining n encouraging good implementations?
* Sawood: What versions is this proposal for?
* Roy: We're talking specifically about the semantics document. To be clear, this is "how do you interpret it if you receive", but you also need a mechanism to send. HAven't defined it.
* Sawood: In 1.1 there is an opportunity for extra metadata, but for buffered responses there is no obvious way to manage this.
* Cory: No-one would add API surface for this.
* Roy: The goal would be to have one way to interpret this.
* Mark: This seems like hope-based standardisation, are we gonna do it right?
* Roy: Would you prefer misery-based?
* Tommy: Sense is majority suspect it's not practical.
* Roy: Can take an action item to propose striking it.

Roy to produce a proposal for striking the section.

#### Issue 733: Arbitrary limitation on authentication parameters
* Mark: Semantics requires credentials to be either `token68` or `auth-param`. Very limited set of characters. Can we open up that character set?
* Roy: We've had this requirement for 10 years now, what do we break by changing it?
* Mark: Hard to imagine that any software is checking that an unknown auth scheme conforms to `token68`.
* Julian: Goal in original spec was intended to be compatible with Basic but to discourage use, as any new scheme would be non-extensible. `token68` vs `auth-param` is either-or. Goal was (and should be) to have everything use `auth-params`. The point of this design was to discourage the use of that syntax.
* Mark: I want to use a URI in a bearer token as we published the bearer token URI scheme. Can't do this due to the limitation on `token68`. People are gonna want to send URIs as bearer tokens despite contraventions in the spec.
* Julian: Bearer spec says so too. Why aren't they defining bearer2?
* Mark: Is the right solution to fork bearer auth schemes or adjust them to admit that it's an artifical constraint? Or have implementation diverge from specification?
* Martin: Julian's argument was interesting. There is a path to including a URI: all it requires is some quoting. This doesn't work with Bearer, but does anyone have such a firm attachment to the word "Bearer"?
* Mark: Is forking it worth the hassle?
* Martin: I don't think people care about bearer per-se.
* Mark: Significant amount of deployed software and practice around it. Instinct is it's easier for us to change the spec than the multitude of folks using Bearer to adjust their practice.
* Justin: Wouldn't having a more open definition in semantics allow Bearer to constrain the text for its own space? Isn't this asking to remove the restriction? Bearer could specify a subset.
* Mark: We may need an update to the bearer spec.
* Justin: I don't think there was a lot of debate about the character set when we specced Bearer. Doesn't think implementations will notice. Keeping the core semantics spec to avoid limiting to arbitrary decisions made by OAuth is a good thing to do. Also we are speccing OAuth 2.1 (not quite a bis document), but we may be able to functionally redefine what goes in Bearer as part of OAuth WG. How do we liaise this between the groups?
* Mark: Hesitant to start the liason as it will add a significant delay to publishing these documents. Justin can carry the message if we decide to change.
* Cory: It may surprise many users of the Bearer scheme to learn that there is a spec at all: the ship may have sailed already.
* Julian: Mark wants to align the spec with what Mark anticipates will happen in reality. If the intent is to use a non base-64 URI, this breaks the definition in HTTP and Bearer. The way to fix this is to change Bearer to allow auth params instead of token68. Does not require a change to HTTP, does require a change to Bearer.
* Roy: The core spec contains this definition to help parse the field unambiguously. May not be as simple as changing the spec. Do not see a need for the change.
* Mark: Responding to Julian, we could update Bearer, but posits that no implementation will pay attention. Bearer is widely deployed, users believe it's an unstructured string, whatever we deploy will be ignored. Would prefer to see the specs reflect reality. Mark doesn't want to allow anything in the spec that would make parsing ambiguous, though he notes it'll be ignored.
* Martin: Why not base64 your URI?
* Mark: The point is to avoid leaking secrets, if you b64 encode them you can't recognise them.
* Justin: The restriction in 6750 is because OAuth tokens were designed to be passed also as form and query parameters. Token should be URL-safe without any additional encoding. Would be nice to have OAuth 2.1 token construction aligned with this reality.
* Mark: If we can't change the spec that's fine, thought it was worth discussing.
* Tommy: Intertia is to keep token68 as-is.

WG took the action to keep the definition as-is.

#### Issue 729: Proxy in the cache key

* Mark: This assumes the cache is co-located with the client, not the proxy.
* Martin: That this was a client-side cache was not obvious to me from context.

WG will take this as editorial and clarify.

#### Issue 715: Unknown preconditions aren't safe

* Mark: How do we add preconditions to the protocol in a way that can be relied upon by the client?
* Martin: Having tried to define a precondition there wasn't a lot of support for anything. There was a clear algorithm to follow but it didn't contemplate the possibility there were other preconditions.
* Julian: Tricky thing in WebDAV is to know if the server understands the header fields. Negotiated via OPTIONS. Tricky to define interactions if you have multiple conditional header fields. For WebDAV this hasn't been a problem due to assumptions of Etags being present.
* Roy: Generally speaking when people introduce these features they make sure they work.

Roy to write a new proposal to clarify.

#### Issue 697: Whitespace is not removed from field values in H2 or H3

* Martin: This is really editorial. Text should just say that things might be removed. Or is there a strict requirement here, should this be MUST?
* Roy: This is supposed to say the field content _excludes_ the whitespace, not so much that it's literally dropped as bytes.
* Julian: RFC 7540 appears to forbid this with a MUST in Security Considerations. Is this implemented?
* Martin: Probably not enforced in H2.

The WG agreed that the editors are to clarify this text, which should be a requirement. Also taking an item to clarify the text in H2.

#### Issue 687: MUST NOT lie

* Martin: This is just weird, especially with normative language attached.
* Mike: Great aspirational statement, not a protocol requirement.
* Roy: We've been enforcing it for 25 years.
* Tommy: Have we?
* Roy: Yes.
* Mark: Is this a requirement on the implementation or the deployment?
* Roy: It's a requirement on the interpretation. Recipients can interpret things they know to be a lie as though they are not standard, and are not bound to conform to the standard.
* Mike: This seems to apply at the individual protocol element level, not at the HTTP semantics level.
* Roy: This allows HTTP spec to override decisions about violating other specifications.
* Mark: P3P and DNT are great specs to use as examples. When these specifications were violated, no-one looked to the HTTP spec (or indeed P3P or DNT) about whether they were lying. They looked to the specs for semantics and then fell back to a legal analysis. This requirement is a no-op becuase this isn't the domain of protocols, it's the domain of a social/political discussion.
* Roy: This is semantics.
* Mark: I agree. Our authority stops at defining the semantics, not the meta-requirement to use them properly.
* Roy: Still don't care.
* Roy: Protocols are examined by governments, not just technical folks.
* Mark: Did this specific text help with governments and legal analysts?
* Roy: Yes, this text was added to resolve specific disputes.
* Mark: Do you have pointers to minutes?
* Roy: They're in the W3C somewhere, maybe DNT discussions.
* Tommy: The WG seems not to be supportive of the text as-is. Is a compromise available here? Perhaps an explicit grant of right to the recipient?
* Roy: Yes, though it doesn't target the responsible party. It's helpful to have an explicit requirement that you can point to say that someone is violating the specification.
* Tommy: Could we get a PR that removes this requirement but puts something non-normative?
* Mark: The argument that the spec allows them to say whatever they want is an argument that is sometimes made, but it's not clear that would be legally relevant. The downside of leaving this in the spec is only that it violates protocol designer sensibilities.
* Martin: We use normative language to achieve interoperability, but this does not appear to be justify a normative requirement. In favour of having text to this effect, but it's not clear that normative language is relevant.
* James: Notes https://github.com/privacycg/proposals/issues/10#issuecomment-777710469 and https://github.com/bslassey/privacy-budget as examples that this problem is real. Not sure if this is the best place to address it.
* Roy: Would like specific proposals for what the change is.
* Tommy: Could you accept the language being non-normative?
* Roy: I don't see any specific reason to remove the requirement and have no desire to. It would be a horrifyingly bad decision to remove this language.
* Julian: Confusion around this sentence is caused by not understanding why this is there. Perhaps we should explain why this is there. Not something Roy added in the most recent revision!
* Cory: This text will need to be carefully managed to avoid undermining the intent.

Roy to propose improvements and rephrasing the text.

#### Issue 683: Control characters

* Mark: We've always been quite open about what field values can contain, but we have restricted it here.
* Roy: Traditionally we've allowed whatever was capable of being robustly handled, though for interop reasons we required a constrained character set.
* Martin: Someone should go back in time and remove the robustness principle. Roy is right though, once you've made the decision to accept the junk we should accept it forever.
* Mark: Should we talk about the impact of CR?
* Roy: We require CR to be replaced with SP.
* Julian: Current text requires rejecting control characters or replacing them with whitespace. Allowing CR to be treated as CR is probably asking for trouble.
* Roy: People are filing vulnerability statements against servers for not removing bare CR. For some reason, clients have decided to tolerate it.

WG agrees to align with fetch for hard refusal of characters and strongly caution against the use of control characters for senders and field definitions. CR and NULL to be replaced by space or rejected.

#### Issue 681: Should -messaging obsolete RFC 1945?

* Mark: Do we move it to obsolete or historic? If obsolete, this document obsoletes it.
* Tommy: Seems more like historic than obsolete.

Working group agrees close with no action.

#### Issue 743: Where does upgrade go?

* Mark: Currently there is an awkward split for upgrade and transfer codings between messaging and semantics.
* Roy: If it's in -messaging it needs to point to lots of things in -semantics, if it's in -semantics it's awkward because it's 1.1-only. Proposal is to put it in -semantics and say explicitly it's 1.1-only.
* Mark: We wanted to have as few headers that were version-specific as possible.
* Martin: The ones that we do have are very awkward. Unfortunately so is Upgrade.

WG to leave this in semantics.

#### Issue 690: Is -messaging part of the core spec?

* Julian: TRACE is the biggest wrinkle here.
* Roy: What should a H2 server do if it receives a TRACE over H2?
* Martin: We could say that it produces a response that matches the request it received, and then apply an informative reference to suggest a HTTP/1.1-format response.

Martin to open a ticket for his proposal.

### CDN Cache Control

[CDN-Cache-Control](https://tools.ietf.org/html/draft-cdn-control-header)

* Mark: Put this spec together for a new field that has the same syntax and semantics, but targetted at CDNs. This is because CDNs already do this now, but in different and incompatible ways. Common to want to cache different in CDNs than other caches, due to the relationship with the CDN. Common questions have been: What about other non-CDN caches that may want to be specifically addressed? What about multi-CDN? There is an appendix that provides recommendations for creating other fields that target the specific cache. What we really need here is a generic, targettable cache-control header. Proposal is that if the WG adopts this specification we turn it into that kind of framework. Other ideas include having one mega cache-control header to do this: this is much more complex and much less human friendly, even though Structured Headers allows this to work. Much simpler to just do this at the field level.
* James: Would multi-CDN not be worth adding as part of the value?
* Mark: The idea is that the main header applies to all CDNs.
* Lucas: Have any CDNs other than author's orgs expressed interest?
* Mark: Yes, backchannel.

WG to call for adoption.






