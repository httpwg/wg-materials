# HTTPbis Design Team Meeting - 8 Mar 2014

## 363 - Renegotiation / use cases (client certs)

ACTION: Martin and EKR to write a draft

## 362 - BLOCKED frame

ACTION: Roberto to take to the list

## 270 - Priority Levelling

Martin summarised what he intends to do to incorporate the proposal.

## Padding

Pinner: What do we say about it? How does padding interact with flow control? Padding as spec'd is a pain in the arse / ass to implement.

Current state of padding explained; no interest in changing it.

## HPACK 

Discussed getting rid of EOS, but most people don't care.

## SRV / DNS

Emile wants to be able to discover support for HTTP/2 without talking HTTP/1 first for HTTP:// URIs.

Roberto, Patrick want to lay groundwork for future adoption of DNS-based solutions, but feel that it's premature to specify. However, it should fit nicely into Alternate Services. Salvatore agrees, and suggests working on it in a separate document.

Emile points out that we don't say anything about domain name resolution in our
specification. Roberto points out that we need to say that prior knowledge /
out of band information is suspect, and may fail. That should future-proof
this for future negotiation mechanisms. Martin points out that that's already
there.

## Cluster #1

    alt-svc 
      349 - Load Asymmetry
      315 - HTTP:// over TLS
    421 - Mixed Schemes
    426 - "Unsupported Scheme" error code
    386 - WebSockets

Talked about Alt-Svc and mapped out how the spec will be done; Julian to edit.
    
Discussed whether it's interesting to do HTTP:// over TLS for HTTP/1.1; there
are security concerns, but they may be manageable. However, there is no current
interest in doing so (that may change).

Clarified how authenticated and non-authenticated HTTP:// over TLS can co-exist.

Talked about how mixed schemes + unsupported scheme could be used
to satisfy use cases like WebSockets.

Mixed schemes seems uncontroversial (and mostly editorial).

Unsupported scheme makes sense if we have alt-svc (which we do), but lively
debate on whether it should be a HTTP status code or error code. Room was
leaning towards status code (except Roberto).

Also discussed renaming error codes to something less confusing.


## Proxies

Wide-ranging discussion.

Subresource Integrity was discussed; strong server-side interest, but
apparently browser folks think it won't get used.

Video delivery is a special / hard problem, and isn't directly addressed by
subresource integrity (except with a merkel tree / hash list).

It is interesting to work on a proxy problem / use cases / scope document
(Informational). Input document(s) TBD. Target audience is WG members and new
participants. It should talk about negatives and positives, and perception.

Discovery is hard. We encourage interception proxies through inaction. Not much
interest in standardising WPAD (security concerns, deployment concerns), but
strong interest in proxy.pac from implementers, due to considerable pain. Would
be interested in clarifying the current format and normalising behaviour as
much as possible, and potentially in extending / replacing the format. E.g., IPv6, secure proxy.

Signatures in HTTP is HTTP, "Modern S-HTTP". Using current WebPKI.

We need more rich policy semantics; this is a research project, but one that the community should undertake. Many of the problems we see are because the protocols / UX do not offer the expressiveness to inform users and sites, or allow them to make informed choices. 

User Interface / User Experience is critical to all of this, but not for us to do. We need someone to do it, however, and it may block some of our work.









## Extensibility

---

Long-term Planning
