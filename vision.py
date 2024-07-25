from app import *

@rt('/vision')
def get():
    caption = "'Real' web development shouldn't be this hard..."
    fig = Image('webdev.png', alt='Web dev', caption=caption, left=False)
    caption = "A minimal FastHTML app really is minimal."
    fig = Image('hello.png', alt='Web dev', caption=caption, left=False, retina=True)
    h2s = 'No compromise', 'Scaling down', 'Scaling up'
    txts = [Markdown(s1), Div(fig, Markdown(s2)), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(1, 'The FastHTML Vision', *secs)

s1 = """FastHTML is a general-purpose full-stack web programming system, in the same vein as Django, NextJS, and Ruby on Rails. The vision is to make it the easiest way to create quick prototypes, and **also** the easiest way to create scalable, powerful, rich applications.

It’s important we have a system that can scale down, as well as up. That’s because the best way to create a big complex application is to first create a small simple application, and then add to it in small steps. If we don’t make it easy to create small simple applications, then fewer people get started, and fewer ideas get tried.

#### Two types of tools

Most software development platforms that make it easy to get started, make it hard to scale in size and complexity. As a result, the development landscape gets segmented into “domain expert tools” like Streamlit, Gradio, and Wordpress, vs “serious programmer tools” like React and Django.

This means that picking one of those domain expert tools is a compromise: if what you’re building is really successful, then at some point you’ll have to throw it away and start again – possibly in a whole different programming language. Furthermore, the domain expert tools generally use very high-level abstractions specific to a single tool, which means learning a new set of foundations too."""

s2 = """FastHTML scales down by picking the most widely used language for “getting stuff done” – particularly by folks who aren’t full-time programmers: Python. And then it throws away everything that makes Python web programming complicated. No templates with quirky template languages. No multi-folder multi-file project skeletons. No complex type systems. No separate JavaScript frontend. No single-framework reactive abstractions. No build step. No tree shaking.

A FastHTML application can start as a single Python file. In fact, it can stay as a single Python file! You only need to break things into multiple files if _you_ decide that will help you build or maintain your software.

FastHTML applications don’t require learning about and installing separate CSS and JavaScript frameworks. You can pip install a complete style library, such as a UI toolkit or template, and use it entirely from Python. We’re building FastHTML libraries for DaisyUI, Bootstrap, Shoelace, Flowbite, and more. You can use these, or create your own, and customise them all with Python. You can pip install additional functionality provided by JavaScript and Python libraries, both controllable entirely from Python."""


s3 = """FastHTML scales up by taking advantage of the foundations of the web. Because a FastHTML application directly uses HTTP, HTML, JavaScript, and CSS, there’s nothing standing between your application and power of the web. FastHTML comes with powerful yet simple tools for function-level and handler-level caching, async, threading, HTML partials, and so forth.

The most important thing is that the fundamentals you started out with when you scaled down, are identical to those you’ll use when you scale up! Same language, same libraries, same abstractions. As you continue on your web programming journey, as you learn more and more, all your new skills become more and more powerful!

#### The foundations

FastHTML brings together and builds on top of two well-established, astonishingly flexible, performant technology frameworks:

  * **The ASGI, Uvicorn, and Starlette trio** : ASGI is a small but incredibly clever approach to simplifying how HTTP, the foundation of web communication, works. It converts all the different parts of an HTTP transaction into a basic, well-defined Python API: a single function, which takes three parameters, which provides access to the full HTTP specification. Uvicorn is the ASGI server used by FastHTML – that is, it is responsible for listening for HTTP messages, and converting them into the Python ASGI API. This happens so automatically and reliably you’ll hardly even notice it’s there! Then Starlette is responsible for taking this powerful single-function ASGI foundation and making it more convenient for programmers, but adding a small number of functions and classes that remove the boilerplate you would otherwise need to support ASGI. As a FastHTML you very rarely need to know anything about the ASGI/Uvicorn/Starlette trio, other than that it’s there in the background doing a lot of work for you!
  * **HTMX** : HTML on its own provides only the most basic interaction mechanisms: you can click on a link to “get” an HTML page, or you can click a button on a form to “post” form data. In either case, the HTML result from the server replaces the current page (known as a “full page refresh”). These limitations have been there since the earlier days of the web. HTMX removes them, by removing four key constraints: 1) not only links and forms can call the server, but now any element on a page can; 2) not only clicks can call the server, but now any event can (e.g. mouseover, key-down, or scroll); 3) not only “get” and “post” HTTP methods are available to call on the server, but any method can be used; 4) not only can the server response be used to replace the whole page, but instead it can modify the existing page in any way, deleting elements, adding elements, or changing elements."""
