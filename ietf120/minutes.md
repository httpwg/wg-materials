# Monday

## Resumable Uploads

### Discovering upload limits upfront (#2833)

?: Would the Upload-Limit be set by the proxy or by the origin server.

Marius: The origin server would have a proxy on their side, and they would set it.

Mike Bishop: Do new requests have new fields work with options?

Marius: doesn't understand question.

### Upload size (#2832)

Michael Toomim: Useful. Versioning draft has a similar mechanism.

Piotr Sikora: What about backwards compatibility with existing servers?

Marius: This only works if the server supports resumable uploads. For transparent upgrades you have to include it in the first request.

Michael: Useful for displaying a status bar.

### Requesting digests from server (#2834)

Mike Bishop: Using digest fields seems like a sensible way, modulo naming.

Marius will talk to Lucas offline.

## QUERY

### Identifying QUERY results (#1918)

Mike Bishop: There are 2 things we can communicate: on the response to the query we can say where you can find the results in the future. Example: serach for "weather in Vancouver": either link to weather right now, or link to weather at date of the query.

Not sure what the right answer is, but we need to pick one.

Mark: It's not either or, but we can document both. Need to look into exact semantics of Location and Content-Location.

mt: Location would tell you where would you go in the future when the world has moved on. Content-Location would link to the historical result.

Julian: to come up with a proposal in collaboration with Mark.

Mark: We're now putting more weight on the HTTP method.

Julian: Every HTTP method needs to specify concretely.

Julian: Can we define QUERY as a transformation? Skeptical.

Mark: Agrees.

Mike Bishop: 9110 says that a cached Host can be used to satisfy a GET request. Does this apply to QUERY as well? It's risky, but it's risky for POST too.

Mark: 3 things: Resource that you query, the resource and content location (like any other GETtable thing), and there's resource and location, which is also a resource that's static.

Mike: It's a GET-table thing to resend your query without all the parameters. Should QUERY be different from POST? No reason it should be, but could be tricky for proxies to get right.

Mark: Scary if cross-origin.

Mike: Was specified as cross-origin in the design team meeting, but should double-check.

mt: Mike should be on the draft. (-> https://github.com/httpwg/http-extensions/issues/2837)

## Cache Groups

No open issues. Ready for last call.

Mike: Any implementations:

Mark: No, but compatible with existing code. Draft might need to sit before it gains momentum.

## Communicating Proxy Configs in Provisioning Domains

Lucas Pardue: Where do these JSON tokens come from?

Tommy: We initially wanted to derive this from the string representation, but now we have a new string registry. There's also legacy types for existing protocols like SOCKS.

Lucas Pardue: Maybe use HTTP for HTTP-based proxying protocols.

Josh Cohen: ??? 
How would you find the PvD files?

Tommy: Two ways: Comes from the network as defined in PvD, RA from the router, fetch config from this HTTPS URI. This file could include a list of proxies.
Or could ask an existing proxy if there are any other proxies.

Yaroslav: How to define exceptions. Things that should go direct vs. things that go via the proxy. Draft currently only allows for suffixes.

Tommy: Current version does. Allows exclusions.

Mike Bishop: Use case for unprompted auth?

Tommy: Unclear how client cert configuration would work.