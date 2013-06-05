# HTTPbis Interim Meeting Agenda

## San Francisco, USA  13-14 June 2013

([Meeting Arrangements](https://github.com/http2/wg_materials/blob/master/interim-13-06/arrangements.md))


## Related Documents

* [Hypertext Transfer Protocol version 2.0](http://tools.ietf.org/html/draft-ietf-httpbis-http2)
* [Header Diff: A compact HTTP header representation for HTTP/2.0](http://tools.ietf.org/html/draft-ruellan-headerdiff)
* [Header Delta-Compression for HTTP/2.0](http://tools.ietf.org/id/draft-rpeon-httpbis-header-compression)
* [A DNS Resource Record for Service Descriptions](http://tools.ietf.org/html/draft-lear-httpbis-svcinfo-rr)


## Schedule

### THURSDAY 13 June 2013

    0830-0900 Reception
    0900-1200 Morning Session
    1200-1300 Lunch
    1300-1500 Afternoon Session I
    1500-1530 Break
    1530-1700 Afternoon Session II

### FRIDAY 14 June 2013

	0830-0900 Reception
	0900-1200 Morning Session
	1200-1300 Lunch
	1300-1500 Afternoon Session I
	1500-1530 Break
	1530-1700 Afternoon Session II


## Agenda

### Administrivia

* Blue sheets
* Introductions
* Scribe selection
* Agenda bashing
* NOTE WELL
* Ground rules for the meeting


### HTTP/2 Draft Review

Martin Thomson will preset a review of the [current
draft](http://tools.ietf.org/html/draft-ietf-httpbis-http2) and seek guidance
on any outstanding editors' questions.


### HTTP/2 Issues

The primary focus of the issues discussion is to converge on what we need to do
to publish a First Implementation Draft. As such, we can decide to skip any
issue that isn't relevant to that goal in this meeting.

See also the [Issues List](https://github.com/http2/http2-spec/issues?milestone=&page=1&state=open).

#### Upgrade

* [Upgrade Mechanism](https://github.com/http2/http2-spec/issues/1) - general review 
* [Advertising Settings During Negotiation](https://github.com/http2/http2-spec/issues/51)
* [Pre-Upgrade Requests](https://github.com/http2/http2-spec/issues/52)
* [Magic Syntax](https://github.com/http2/http2-spec/issues/101)
* [Registry of Opaque Strings](https://github.com/http2/http2-spec/issues/12)
* [Cross-Protocol Attacks](https://github.com/http2/http2-spec/issues/35)

#### Frame Layout

* [Reserved Bit](https://github.com/http2/http2-spec/issues/67)

#### Frame Semantics

* [Opaque Data in RST_STREAM and GOAWAY](https://github.com/http2/http2-spec/issues/17)
* [Stream ID in GOAWAY](https://github.com/http2/http2-spec/issues/63)
* [Ping Payload](https://github.com/http2/http2-spec/issues/68)
* [The FINAL Flag](https://github.com/http2/http2-spec/issues/103)
* [Frame Extensibility](https://github.com/http2/http2-spec/issues/95)
* [SETTINGS persistence](https://github.com/http2/http2-spec/issues/8)

#### Stream Life Cycle

* [Discovering Maximum Frame Size](https://github.com/http2/http2-spec/issues/28)
* [Unilateral Stream Creation](https://github.com/http2/http2-spec/issues/73)
* [Concurrent Streams Limits and Unidirectional Streams](https://github.com/http2/http2-spec/issues/78)
* [Separate HEADERS+PRIORITY](https://github.com/http2/http2-spec/issues/99)
* [Frame Size limits](https://github.com/http2/http2-spec/pull/92)
* [SETTINGS_MAX_CONCURRENT_STREAMS](https://github.com/http2/http2-spec/issues/38)

#### Header Compression

* [Header Compression](https://github.com/http2/http2-spec/issues/2) - selecting a candidate
* [Routing Data in Headers](https://github.com/http2/http2-spec/issues/23)
* [Header Block Field Name Length](https://github.com/http2/http2-spec/issues/41)

#### Server Push

* [Cacheability of Server Push](https://github.com/http2/http2-spec/issues/24)
* [no-push default](https://github.com/http2/http2-spec/issues/40)
* [PUSH_PROMISE stream priority](https://github.com/http2/http2-spec/issues/75)

#### Flow Control

* [Settings Flag for Disabling Flow Control](https://github.com/http2/http2-spec/issues/44)
* [FINAL and WINDOW_UPDATE](https://github.com/http2/http2-spec/issues/104)

#### Prioritization

* [Prioritisation](https://github.com/http2/http2-spec/issues/7) - general review
* [Priority](https://github.com/http2/http2-spec/pull/111)

#### HTTP Mapping

* [Trailers](https://github.com/http2/http2-spec/issues/47)
* [Negotiation of trailers](https://github.com/http2/http2-spec/issues/21)
* [Handling Expect/continue](https://github.com/http2/http2-spec/issues/18)
* [Indicating the end of a header block](https://github.com/http2/http2-spec/issues/22)
* [Rejecting non-idempotent requests](https://github.com/http2/http2-spec/issues/57)


#### Transport Mapping

* [SETTINGS_CURRENT_CWND](https://github.com/http2/http2-spec/issues/65)
* [SETTINGS_UPLOAD_BANDWIDTH](https://github.com/http2/http2-spec/issues/107)
* [SETTINGS_DOWNLOAD_BANDWIDTH](https://github.com/http2/http2-spec/issues/108)
* [SETTINGS_ROUND_TRIP_TIME](https://github.com/http2/http2-spec/issues/109)
* [SETTINGS_DOWNLOAD_RETRANS_RATE](https://github.com/http2/http2-spec/issues/110)
* [TCP Exclusivity](https://github.com/http2/http2-spec/issues/26)


### Other Issues and Deliverables

Discussion of other potential issues (editorial or design), additional
deliverables, etc.


## Implementation and Testing

We should have a first implementation draft shortly after the meeting, if all
goes well. As such, our next phase of work should be implementing and testing
the draft.

We'll discuss the schedule involved, in light of the upcoming Hamburg interim
meeting. In addition to implementation planning, we'll need to start
documenting how we'll perform testing.

In particular, we should discuss what aspects of the following will be tested
in the first instance:

* Upgrade mechanisms: APLN? Dedicated port? Upgrade?
* Flow control?
* Prioritization?
* Server push?

## Wrap-up

We'll review action items and plan next steps, including future meetings:

* [Berlin IETF](http://www.ietf.org/meeting/87/)
* [Hamburg Interim](https://github.com/http2/wg_materials/blob/master/interim-13-08/arrangements.md)
* 2013 Q4 Interim?
* [Vancouver IETF](http://www.ietf.org/meeting/upcoming.html)
* 2014 Q1 Interim?
