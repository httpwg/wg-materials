# HTTPbis Working Group Agenda - IETF 87

 - Meeting chat: <xmpp:httpbis@jabber.ietf.org?join>
 - Minutes: <http://tools.ietf.org/wg/httpbis/minutes>

## WEDNESDAY 31 July 2013 - 1510-1720 Afternoon Session II/III

### Potsdam 2: HTTP/1 and HTTP/2

 *   1 min - Blue sheets / scribe selection 
 *   4 min - Agenda bashing
 *  30 min - HTTP/1.x
             - draft -23 changes [Julian Reschke]
             - WGLC summary / Issue discussion 
			   <http://trac.tools.ietf.org/wg/httpbis/trac/report/20>
 *  85 min - HTTP/2.x
             - San Francisco Interim meeting summary
             - Draft changes and open questions [Martin Thomson]
			 - Implementation Status summary
			 - Header Compression Benchmark [Christian Grothoff]
			 - Known State For the TLS Case [Gabriel Montenegro]
             - update from TLS WG [EKR]
			 - Issue discussion
			   <https://github.com/http2/http2-spec/issues?labels=design&milestone=&page=1&state=open>


## FRIDAY 2 August 2013 - 0900-1100 Morning Session I

### Bellevue: HTTP/2 and Transport Joint Meeting

*    1 min - Blue sheets / scribe selection 
*    4 min - Agenda bashing
*   15 min - HTTP and Encryption [Mark Nottingham]
*   20 min - HTTP/2 With A Transport Eye [Allison Mankin]
*   20 min - Flow Control
    HTTP2 does flow control on top of TCP; in particular, how does HTTP2
    mitigate pain from shrinking and sometimes zeroing the flow control windows?
    Also, which entities are advised to use and which to not use flow control?
*   20 min - Priorities
    What is the relationship between HTTP priorities and QoS (or lack thereof)?
*   20 min - Initial Congestion Window 
    Previous versions of HTTP/2 (and SPDY) experimented with storing the 
	congestion window size to reuse in future connections. This has been 
	recently removed, but discussion may still be helpful.
*   20 min - General Discussion / Other Issues
