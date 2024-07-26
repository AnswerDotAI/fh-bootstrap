from app import *

def page():
    h2s = 'Python', 'HTMX', 'Uvicorn', 'Starlette', 'SQLite'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3), Markdown(s4), Markdown(s5)]
    secs = Sections(h2s, txts)
    return BstPage(3, "FastHTML's tech stack", *secs)

s1 = """
"""

s2 = """
https://www.youtube.com/watch?v=3GObi93tjZI
Nowadays most web applications are built using backend systems that return a combination of JSON and HTML data over HTTP. Javascript, normally using frameworks such as React, Angular, or Vue, is used to combine the JSON and HTML together for display in the browser. This is an *"API based"* approach to web development.

An alternative "hypermedia-based" approach, used by systems such as HTMX, simplifies things greatly by just returning HTML. FastHTML is designed to create hypermedia applications. Nearly all of the complexity of client-server programming vanishes when using this approach. When going to a page directly, the server will respond with a standard HTML web page:

```
<html>
  <head><title>Example</title></head>
  <body>
    <p id="greet" hx-get="/change">Hello World!</p>
  </body>
</html>
```

But when clicking on this link, 
```
<p id="greet" hx-get="/change">Nice to be here!</p>
```
"""

s3 = """"""

s4 = """"""

s5 = """"""

