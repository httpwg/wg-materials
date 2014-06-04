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

* 95: Frame Type Extensibility

* 413: Account for Proxies

* 460: Requiring clients to support content-codings
  - proposal: 472
* 424: Support for GZIP at the server
* 423: Security Implications of GZIP
* 466: Compress segments rather than frames

* 443: Indicating Chosen Service
  - proposal: 474
* 444: Flusing Alternative Service Cache
* 462: Intermediaries and Alt-Svc

* 458: Race Condition in Shutdown when proxying
  - proposal: 475
* 468: Sending Priority for closed streams
  - proposal: 489
* 436: Enable weight of 0

* 480: Headers and Flow Control
  - see also: 482
  - see also: 456
* 485: Negotiate "no huffman"
* 481: Allow intervening DATA frames

* 484: State Diagram

* 490: Forbid coalescing
* 315: HTTP:// URLs over TLS
* 363: TLS Renegotiation
* 491: Restrict cipher suite selection

* 418: Refining Prior Knowledge
  - proposal: 420

* 386: Websockets


### Other Issues and Deliverables

Discussion of other potential issues (editorial or design), additional
deliverables, etc.

## Wrap-up

We'll review action items and plan next steps, including future meetings:

* [Toronto IETF](http://www.ietf.org/meeting/upcoming.html)
* Future Interim meetings
