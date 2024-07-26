from app import *

def page():
    secs = Sections(('ASGI & HTMX', 'HTTP', 'HTML, CSS, & JS'),
                    map(Markdown, [s1, s2, s3]))
    return BstPage(2, 'The foundations of FastHTML', *secs)

s1 = """FastHTML brings together and builds on top of two well-established, astonishingly flexible, performant technology frameworks: *ASGI* (implemented in Uvicorn and Starlette), and *HTMX*.

#### ASGI

ASGI is a small but incredibly clever approach to simplifying how HTTP, the foundation of web communication, works. It converts all the different parts of an HTTP transaction into a basic, well-defined Python API: a single function, which takes three parameters, which provides access to the full HTTP specification. Uvicorn is the ASGI server used by FastHTML-–-that is, it is responsible for listening for HTTP messages, and converting them into the Python ASGI API. This happens so automatically and reliably you’ll hardly even notice it’s there! Then Starlette is responsible for taking this powerful single-function ASGI foundation and making it more convenient for programmers, but adding a small number of functions and classes that remove the boilerplate you would otherwise need to support ASGI. As a FastHTML you very rarely need to know anything about the ASGI/Uvicorn/Starlette trio, other than that it’s there in the background doing a lot of work for you!

To learn more about how Uvicorn and Starlette work in FastHTML, see the relevant [technology section](/tech#sec3).

#### HTMX

HTML on its own provides only the most basic interaction mechanisms: you can click on a link to “get” an HTML page, or you can click a button on a form to “post” form data. In either case, the HTML result from the server replaces the current page (known as a “full page refresh”). These limitations have been there since the earlier days of the web. HTMX removes them, by removing four key constraints:

1. Not only links and forms can call the server, but now any element on a page can
2. Not only clicks can call the server, but now any event can (e.g. mouseover, key-down, or scroll)
3. Not only “get” and “post” HTTP methods are available to call on the server, but any method can be used
4. Not only can the server response be used to replace the whole page, but instead it can modify the existing page in any way, deleting elements, adding elements, or changing elements.

<img src="assets/htmx-meme.png" alt="HTMX meme" class="img-fluid mx-auto d-block">

HTMX is famous for its [memes](https://v1.htmx.org/essays/#memes), including the image above. It is the successor of [intercooler.js](https://intercoolerjs.org/), which is now over 10 years old---so it's a mature technology. HTMX/Intercooler is responsible for the idea that we can build on top of the fundamentals of the web, without sacrificing the ability to create modern, interactive web applications. Without it, FastHTML would not exist (although perhaps now we should update that meme to FastHTML 2024, where we would have just 3 parts: browser, DOM, and a python file!) To learn more about how HTMX works and how to use it, see the [HTMX technology section](/tech#sec2). 
"""

s2 = """"""


s3 = """"""
