# HTTP WG Minutes: October 2022

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Resumable Uploads](#resumable-uploads)
  - [Issue 2239 - server-generated token/URI or client token](#issue-2239---server-generated-tokenuri-or-client-token)
  - [Issue 2240 and Issue 2243 - feature detection and transparent upgrade to resumable](#issue-2240-and-issue-2243---feature-detection-and-transparent-upgrade-to-resumable)
  - [Issue 2247 - Browser compatibility](#issue-2247---browser-compatibility)
- [Signatures](#signatures)
- [Cookies](#cookies)
- [QUERY Method](#query-method)
- [Client Cert Header Field](#client-cert-header-field)
- [Alternative Services](#alternative-services)
- [ORIGIN in HTTP/3](#origin-in-http3)
- [AOB](#aob)
  - [Retrofit](#retrofit)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Resumable Uploads

Marius discusses the status of the draft.

### [Issue 2239](https://github.com/httpwg/http-extensions/issues/2239) - server-generated token/URI or client token

Martin: (in chat) 1xx means server-generated token is delivered in parallel

Mnot: if we have multiple uses for different styles, can we do both?

Marius: yes, maybe

Martin: doing both is a failure outcome - when we fail to consider all of the use cases. a lot of the reason for doing client-generated tokens seem to depend on everything completing in one round trip, but that is at odds with the goals of resumable uploads, which take longer

Marius: there are cases where things take less time, such as lots of small resources

### [Issue 2240](https://github.com/httpwg/http-extensions/issues/2240) and [Issue 2243](https://github.com/httpwg/http-extensions/issues/2243) - feature detection and transparent upgrade to resumable

There is interest in integrating this feature into HTTP stacks on platforms (like browsers and servers), make it available via upgrade; is there enough interest to do this?

Guoye (chat): some interest in integrating this in the client library so that its use is transparent to applications

### [Issue 2247](https://github.com/httpwg/http-extensions/issues/2247) - Browser compatibility

Can we make these work in such a way that they're compatible with existing browsers?

Martin: Lots of work to get this to work with Fetch, either teaching fetch about 1xx generically or to teach it about *this* new 1xx so that uploads are good.

Lucas: there is a difference between exposing the machinery so that JS apps can fill in the gaps and doing this inside fetch.  the latter might be easier; 100-continue is handled today magically, so that people don't need to deal with it.  I don't really appreciate the complexities.

Mnot: agree with Lucas. it is possible to oversell how hard it is, but generally the hardest part is getting browsers to commit to it; I would shy away from designing a generic 1XX API, which might be hard (think security/privacy implications).

Guoye: we have two use cases - browser/generic client where we want most uploads upgraded; the other is where people want to do the work for itself. we should make feature detection optional; for the browser, we depend on the new 1xx, others can use this themselves, possibly without the 1xx (just by understanding that the resource supports resumption).  If we switch to a server-generated token, we need to consider both cases.

Austin: in chat raises a point about Idempotency-Key (HTTP API WG proposal)

Mnot: sense is that these are adjacent, but not overlapping

Julian: in chat asks about 103 status in implementations

Mnot: yep, still working through that


## Signatures

Justin: it's perfect, clearly; time to go to WGLC

Mnot: need to think about what we need to do to get the appropriate level of review

Justin: SECDIR?

Mnot: we already got one, we might ask for another

Justin: might be a good idea to get another ahead of IESG review

Justin: don't think that this needs the same level of analysis as TLS 1.3

Mnot: we need clarity about the right level of review

Chris Wood: I was surprised to see this in WGLC without some security analysis, particularly considering the complexity of the spec; I don't think that being at this layer absolves it of responsibility for getting analysis; perhaps SECDIR or some security folks need to work out what the right bar is; I'm sure we will be able to find someone to do the analysis, but without that analysis I'm concerned

Justin: might need to get ADs in the room

Lucas in chat: maybe SECDir can advise on the level of analysis that is appropriate

Mnot: ?

Lucas: question about digest examples in the draft; happy to help

Justin: discussion about covering message content, using digest, with a non-normative example of that


## Cookies

Quick status update

dveditz: was the redirect problem in all cases or just for same-site lax by default cases?
steven: Chrome applies a POST exception; so we have a two-minute window in which we (Chrome?) let cookies through; the result of some experiments was that we need more information; will take a number of months to work this out

dveditz: mozilla is considering not implementing samesite lax by default due to being able to rely on partitioning


## QUERY Method

Some remaining open issues (6).  Julian is looking for help with these.

## Client Cert Header Field

A few small things to do before completion.  9110 terminology changes needed; easy. how to signal if a cert isn't acceptable

mnot: generally agree that the proxy is responsible for managing signaling the error (?)
martin: the problem is that the proxy can't synthesize TLS-layer errors from HTTP-layer signals, at least not generically; made a suggestion on the PR

problem with cert-chain description; need to allow for either copying from TLS or constructing a certification path on its own

mnot: this is an informational spec

(longer discussion about how to construct text for this problem; suggestions in GitHub; seem to be settling on something like https://github.com/httpwg/http-extensions/pull/2258#discussion_r988399239)

Lucas: cloudflare does have a header that we give to people for client certificate validation; a spec would improve some of that

## Alternative Services

Mike: not a lot of movement because we're spinning up a design team to talk about what the successor draft looks like; some of these will be addressed or put out of scope

Meeting soon

## ORIGIN in HTTP/3

One open editorial issue in -01.  WGLC?

Lucas: there is a danger of face-planting here, if ORIGIN and all the stuff that comes with it work, then fine; but there are lots of other stuff around this that could take a big redesign

Mike: I have some changes I'd like to make, but that would break compatibility

## AOB

### Retrofit

Adding the Date type - in this draft, standalone, or a revision of SF?

Martin: revise SF

Mnot: doesn't like being the guinea pig
Justin: likes the ABNF from a implementation perspective; the paint is barely dry on 8941, but apart from that strange feeling, I don't see a reason not to; we'd eventually do a bis to collect the additions

Mnot: probably go with a SF revision; need to keep scope in check