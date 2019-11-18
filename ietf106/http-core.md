# http-core status for [Singapore IETF 106](https://datatracker.ietf.org/meeting/106/agenda#2019-11-18-080000)

Editors:
  - Roy T. Fielding
  - Mark Nottingham
  - Julian F. Reschke
  
The -06 drafts for http-core were published last week:

  - [draft-ietf-httpbis-semantics-06](https://tools.ietf.org/html/draft-ietf-httpbis-semantics-06)
  - [draft-ietf-httpbis-messaging-06](https://tools.ietf.org/html/draft-ietf-httpbis-messaging-06)
  - [draft-ietf-httpbis-cache-06](https://tools.ietf.org/html/draft-ietf-httpbis-cache-06)

Diffs since 05 can be seen at

  - https://httpwg.org/http-core/diffs/diff_semantics_05_to_06.html
  - https://httpwg.org/http-core/diffs/diff_messaging_05_to_06.html
  - https://httpwg.org/http-core/diffs/diff_cache_05_to_06.html

and a frankenRFC diff of all changes since the last consensus RFCs, rearranged
according to the current draft structure to show just the word changes:

  - https://httpwg.org/http-core/diffs/diff_semantics_frfc_to_06.html
  - https://httpwg.org/http-core/diffs/diff_messaging_frfc_to_06.html
  - https://httpwg.org/http-core/diffs/diff_cache_frfc_to_06.html

As always, the best way to track our work is on github at

  - https://github.com/httpwg/http-core

and especially the list of commits and open issues:

  - https://github.com/httpwg/http-core/commits/master
  - https://github.com/httpwg/http-core/issues

For this meeting, we will probably focus on the issues marked with the label "discuss"

  - https://github.com/httpwg/http-core/labels/discuss

(which are still being added to, so speak up if you want to discuss something).

The following 29 issues have been closed since the last meeting in Montreal:

  - https://github.com/httpwg/http-core/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed+closed%3A%3E2019-07-19+sort%3Acreated-asc

with the bulk of text changes being about

 - refactoring the byte ranges grammar to be extensible: [196](https://github.com/httpwg/http-core/issues/196), [212](https://github.com/httpwg/http-core/issues/212)
 - moving trailer fields to Semantics: [16](https://github.com/httpwg/http-core/issues/16), [117](https://github.com/httpwg/http-core/issues/117)
 - moving payload body requirements to Semantics: [159](https://github.com/httpwg/http-core/issues/159), [202](https://github.com/httpwg/http-core/issues/202)
 - moving retries to idempotent methods: [27](https://github.com/httpwg/http-core/issues/27)
 - adding a port registration: [36](https://github.com/httpwg/http-core/issues/36)
 - adding a min supported URI length: [169](https://github.com/httpwg/http-core/issues/169)
 - incorporating the remaining RFC2818 (HTTP over TLS) text: [236](https://github.com/httpwg/http-core/issues/236)
 - replacing "cacheable by default" with heuristically cacheable: [54](https://github.com/httpwg/http-core/issues/54), [242](https://github.com/httpwg/http-core/issues/242)
 - defining requirements on caching incomplete responses: [25](https://github.com/httpwg/http-core/issues/25), [221](https://github.com/httpwg/http-core/issues/221)

See the "Changes since ..." sections at the end of each draft for a brief
summary of what has been changed.

We currently have roughly 60 open issues remaining on the list, though 15 are
editorial and many others have only small bits left to do before closing.

We are also monitoring RC 723* errata:

  - https://httpwg.org/http-core/httpbis-errata-status.html

Right now, we have only two reports that haven't been dealt with:

 - https://github.com/httpwg/http-core/issues/163
 - https://github.com/httpwg/http-core/issues/53
