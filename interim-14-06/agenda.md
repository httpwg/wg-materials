# HTTPbis Interim Meeting Agenda (DRAFT)

## New York, New York US 5-6 June 2014

([Meeting Arrangements](https://github.com/http2/wg_materials/blob/master/interim-14-06/arrangements.md))


## Related Documents

* [Hypertext Transfer Protocol version 2](http://tools.ietf.org/html/draft-ietf-httpbis-http2)
* [HPACK - Header Compression for HTTP/2](http://tools.ietf.org/html/draft-ietf-httpbis-header-compression)

We'll be taking minutes on [Etherpad](http://etherpad.tools.ietf.org:9000/p/notes-14-06-interim-httpbis)


## Schedule

### THURSDAY 5 June 2014

	0830-0900 Reception
    0900-0915 Introduction
    0900-1200 Morning Working Session
    1200-1300 Lunch
    1300-1700 Afternoon Interop Session
    

### FRIDAY 6 June 2014

	0830-0900 Reception
	0900-1200 Morning Working Session
	1200-1300 Lunch
	1300-1500 Afternoon Working Session I
	1500-1530 Break
	1530-1700 Afternoon Working Session II


## Agenda

### Administrivia

* Blue sheets
* Introductions
* Agenda Bashing
* Scribe selection
* NOTE WELL

### HTTP/2 Draft Review

Martin Thomson will preset a review of the [current
draft](http://tools.ietf.org/html/draft-ietf-httpbis-http2) and seek guidance
on any outstanding editors' questions.

### HTTP/2 Issues

See the [Issues List](https://github.com/http2/http2-spec/issues?milestone=&page=1&state=open).

#### Extensibility

* [Frame Type Extensibility](https://github.com/http2/http2-spec/issues/95)
* [Websockets](https://github.com/http2/http2-spec/issues/386)

#### Content Compression and Encoding
* [Requiring clients to support content-codings](https://github.com/http2/http2-spec/issues/460)
  - proposal: [472](https://github.com/http2/http2-spec/issues/472)
* [Support for GZIP at the server](https://github.com/http2/http2-spec/issues/424)
* [Security Implications of GZIP](https://github.com/http2/http2-spec/issues/423)
* [Compress segments rather than frames](https://github.com/http2/http2-spec/issues/466)

#### Header Compression
* [Headers and Flow Control](https://github.com/http2/http2-spec/issues/480)
  - see also: [482](https://github.com/http2/http2-spec/issues/482)
  - see also: [456](https://github.com/http2/http2-spec/issues/456)
* [Negotiate "no huffman"](https://github.com/http2/http2-spec/issues/485)
* [Allow intervening DATA frames](https://github.com/http2/http2-spec/issues/481)

#### Negotiation / Upgrade
* [Indicating Chosen Service](https://github.com/http2/http2-spec/issues/443)
  - proposal: [474](https://github.com/http2/http2-spec/issues/474)
* [Flusing Alternative Service Cache](https://github.com/http2/http2-spec/issues/444)
* [Alt-Svc header host restriction](https://github.com/http2/http2-spec/issues/492)
* [Intermediaries and Alt-Svc](https://github.com/http2/http2-spec/issues/462)
* [Refining Prior Knowledge](https://github.com/http2/http2-spec/issues/418)
  - proposal: [420](https://github.com/http2/http2-spec/issues/420)

#### Stream Handling
* [Race Condition in Shutdown when proxying](https://github.com/http2/http2-spec/issues/458)
  - proposal: [475](https://github.com/http2/http2-spec/issues/475)
* [Sending Priority for closed streams](https://github.com/http2/http2-spec/issues/468)
  - proposal: [489](https://github.com/http2/http2-spec/issues/489)
* [Enable weight of 0](https://github.com/http2/http2-spec/issues/436)

#### Editorial(-ish)
* [Account for Proxies](https://github.com/http2/http2-spec/issues/413)
* [State Diagram](https://github.com/http2/http2-spec/issues/484)

#### Security
* [Forbid coalescing](https://github.com/http2/http2-spec/issues/490)
* [HTTP:// URLs over TLS](https://github.com/http2/http2-spec/issues/315)
* [TLS Renegotiation](https://github.com/http2/http2-spec/issues/363)
* [Restrict cipher suite selection](https://github.com/http2/http2-spec/issues/491)



### Other Issues and Deliverables

Discussion of other potential issues (editorial or design), additional
deliverables, etc.

## Wrap-up

We'll review action items and plan next steps, including future meetings:

* [Toronto IETF](http://www.ietf.org/meeting/upcoming.html)
* Future Interim meetings
