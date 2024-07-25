from app import *

@rt('/foundation')
def get():
    h2s = 'ASGI & HTMX', 'HTTP', 'HTML, CSS, & JS'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(2, 'The foundations of FastHTML', *secs)

s1 = """FastHTML brings together and builds on top of two well-established, astonishingly flexible, performant technology frameworks: ASGI (implemented in Uvicorn and Starlette), and HTMX.

#### The ASGI, Uvicorn, and Starlette trio

ASGI is a small but incredibly clever approach to simplifying how HTTP, the foundation of web communication, works. It converts all the different parts of an HTTP transaction into a basic, well-defined Python API: a single function, which takes three parameters, which provides access to the full HTTP specification. Uvicorn is the ASGI server used by FastHTML – that is, it is responsible for listening for HTTP messages, and converting them into the Python ASGI API. This happens so automatically and reliably you’ll hardly even notice it’s there! Then Starlette is responsible for taking this powerful single-function ASGI foundation and making it more convenient for programmers, but adding a small number of functions and classes that remove the boilerplate you would otherwise need to support ASGI. As a FastHTML you very rarely need to know anything about the ASGI/Uvicorn/Starlette trio, other than that it’s there in the background doing a lot of work for you!

#### HTMX

HTML on its own provides only the most basic interaction mechanisms: you can click on a link to “get” an HTML page, or you can click a button on a form to “post” form data. In either case, the HTML result from the server replaces the current page (known as a “full page refresh”). These limitations have been there since the earlier days of the web. HTMX removes them, by removing four key constraints: 1) not only links and forms can call the server, but now any element on a page can; 2) not only clicks can call the server, but now any event can (e.g. mouseover, key-down, or scroll); 3) not only “get” and “post” HTTP methods are available to call on the server, but any method can be used; 4) not only can the server response be used to replace the whole page, but instead it can modify the existing page in any way, deleting elements, adding elements, or changing elements."""

s2 = """"""


s3 = """"""
