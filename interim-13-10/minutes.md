# HTTPbis Working Group Interim Meeting Minutes

9-11 October 2013 - Seattle, WA USA


## WEDNESDAY 9 October 2013

* Blue sheets
* Introductions
* Agenda Bashing
* NOTE WELL
* HTTP/2.0 Protocol Test draft

Michelle Lai presented her draft on HTTP/2.0 Protocol Test Principles. We then
gathered implementation experience regarding draft-06; generally, feedback was
good, although most problems were seen about header compression.

We then broke into informal groups, centred around protocol testing (Michelle
Lai), header compression testing (Herve Ruellan) and general interop work
between implementations.



## THURSDAY 10 October 2013

* Blue sheets
* Introductions
* Scribe selection
* Agenda bashing
* NOTE WELL

### Issue 1

Upgrade issue: Move the Upgrade mechanism from the 2.0 draft to a different
spec until it will be fully tested ? Upgrade is a complicated mechanism to
setup a plain text 2.0 connection.

Lots of discussion about Alternate-Protocol and the potential for that to
replace the use of Upgrade.

There will be a separate draft describing the Alternate mechanism and it will be referenced in the next implementation draft version as experimental.

### Issue 250

Header compression: discussion about removing "substitution operation" from the
spec as it is quite complex to implement and brings little benefits. No clients
at moment support it (is it true?)

Consensus to drop it for the time being and to evaluate it again in the future

### Issue 233

Move the new header addition to the top (index 0) 

### Issue 258

The initial header table is currently mutable. Consensus to make the initial
header table completely immutable and always present.

### Issue 259

Discussion on having separate tables for client and server at all, or simply
having a single table containing common header names for both. Consensus on one
Big Table.

### Issue 242

We're not going to define what header field values are or aren't. We're going
to say that the compressor carries octet sequences and avoid the issue entirely.

### Issue 120

Roberto described the use of this for doing things like reclaiming header
compression table for long-lived connections.

This is one particular solution to the problem posed by wanting to change the
size of the header compression table.

Proposal from Mike Bishop:
https://github.com/MikeBishop/http2-spec/commit/fb59b5517105867f8fa681aecf6868da
9bc2a6e3

There is consensus on work on it. Discussion if include the mechanism for it in
the next implementation spec or keep it in a separate spec. The proposal will
be discussed in the list.

### Issue 216

discussion on other possible reference sets to be used. Work on a draft
proposal to be discussed in Vancouver.


### Issue 228

Consensus on proposal #2. Remove the END_STREAM flag from CONTINUATION and
determine whether a stream is ended based on the initial HEADERS frame flags.

### Issue 246

FRAME_SIZE_ERROR

### Issue 95

lets discuss it in Vancouver

### Issue 221

Discussion on :host and host, potential chance to rename :host to :authority.
Proposal to apply the "do not set and MUST ignore" rule for colon headers.


### Issue 257

omit colon-prefixed headers to be treated as a malformed HTTP message.
Intermediares should not act on interpret them just forwarding them.

I think some discussions occurred after issue 257

### Issue 18

Some discussion about non-final status codes: issue raised #264 and assigned to
mnot

### Issue 260

Jeff Pinner wants to make the 2^14 limit apply only to DATA frames.

James Snell wants to make the 2^14 limit apply only to all except 
HEADERS/PUSH_PROMISE/CONTINUATION frames.

Roberto recognizes the layering violation, and would address it by making 2^14
the limit at the framing layer.

Patrick isn't concerned with the layering violation, but sees the possibility
for avoiding CONTINUATIONS frames on large headers to be nice.

The coin toss in Seattle decided that it would be a fixed 2^14-1 limit for ALL
frames, regardless of layer.

### Issue 223

People like explicit disable PUSH_PROMISE as a binary on/off 

### Issue 193

clarify in the draft, push is allowed only for safe cachable methods + no
request body.


### Issue 184

it has been discussed the possibilty to use SETTINGS ACK + reset streams to
limit server resource usage, instead of using profiles as proposed in the issue.

put the issue on hold until we get more implementation/interop experience. 


### Issue 23

closed

### Issue 112

We talked about heuristics for avoiding DoS.  Not a lot of enthusiasm.
We've talked about PING and empty, acknowledged SETTINGS.
We've talked about a new explicit GOAWAY code for "enhance your calm".

### Issue 150

closed

### Issue 171

closed

### Issue 187

closed

### Issue 202

closed. no interest in carrying the reason phrase.

### Issue 215

discussion summarized in the issue

### Issue 219

closed

### Issue 240

closed.

### Issue 261

closed.

### Discussion on Priority

How a proxy maps priorities from different connections/browser within a single
connection towards the Origin Server. People agree that this is something worth
to work on.

Priority dependencies, i.e. grouping, tree, list etc.

a new Issue #270 has been create to track the discussion.



## FRIDAY 11 October 2013

* Blue sheets
* Introductions
* Scribe selection
* Agenda bashing
* NOTE WELL


### Issue 269

We need to retain :authority and host as separate, because there are 1.1 cases that break without both.  OAuth in particular.


### Issue 95

lots of discussion on frame types

lots of discussion on alpn strings

some snoozing by the notetaker

### ALPN

Mark wants to collect input

Will is concerned about how many bytes this can use, as is Patrick

Jeff wants to use NPN


