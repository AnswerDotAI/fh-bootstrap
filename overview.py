from app import *

def page():
    caption = "'Real' web development shouldn't be this hard..."
    fig = Image('assets/webdev.jpg', alt='Web dev', caption=caption, left=False)
    h2s = 'Getting started', 'Background', 'Current Status'
    txts = [Markdown(s1), Div(fig, Markdown(s2)), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(0, 'About FastHTML', *secs)

s1 = """
You're using a FastHTML app right now. We didn't create a separate blog system for this site, because building apps with FastHTML is so easy there's no need for it! Here is the [source code](https://github.com/AnswerDotAI/fh-bootstrap/blob/main/overview.py) for the page you're reading right now. You'll see that the source code is very simple, relying on Python components like `Markdown` to build the page. The components are simple Python functions---for instance, here is the [source code for `Markdown`](https://github.com/AnswerDotAI/fh-bootstrap/blob/main/bootstrap.py#L5-L6), taking just two lines of code!

If you're an experienced web dev, then you can use all your knowledge of CSS, HTML, JS, etc. to build web applications with FastHTML right away. We've heard from expert coders that they have successfully built complete web apps within an hour of getting started with FastHTML. We've got a [Quickstart for Web Developers](https://docs.fastht.ml/quickstart_for_web_devs.html) tutorial that will get you up and running quickly. (Read the rest of the docs while you're there!) Next, read through the heavily-commented source of this [idiomatic fasthtml app](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py). Then study some of the [fasthtml-example applications](https://github.com/AnswerDotAI/fasthtml-example), particularly the first four listed.

If you haven't done much (or any) web development, try following through each step of the [FastHTML By Example](https://docs.fastht.ml/by_example.html) tutorial. We don't yet have a self-contained guide explaining all the web foundations you'll need to know (HTML, HTTP, CSS, etc.), so you'll probably need to do some self-learning through other resources. But watch this space---we're planning a complete web programming from scratch course soon!
"""

s2 = """
FastHTML is a system for writing web applications in Python. It is designed to be simple, powerful, and flexible. It is also designed to be easy to learn and use. The project is inspired by technologies such as React JSX, Hotwire, Astro, FastAPI, and Phoenix LiveView.

FastHTML was originally started by Jeremy Howard at Answer.AI for a number of reasons:

- Over 25 years of web development, Jeremy realized that web programming could be easier and more powerful. He was particularly concerned that recent trends had moved away from the power of the web's foundations, resulting in a fractured ecosystem of over-complex frameworks and tools
- He saw that two small but ingenious developments had made the web's foundations more powerful and more accessible: **ASGI** and **HTMX**. But the tools available for using them were still too complex, and the barriers to entry were still too high
- Jeremy and his wife Rachel had spent the last 8 years working to make artifical intelligence accessible to more people. They saw that the most widely used web development tools were too complex for people who aren't full time coders. This meant that Jeremy and Rachel's students struggled to turn their AI project ideas into working applications.
- Jeremy's goal for Answer.AI is to help society benefit from AI, which means creating lots of useful products and services that use AI effectively---so creating those products and services needs to be made as fast and easy as possible.

FastHTML is a framework that deals with all these issues: it returns to the roots of the web, leveraging ASGI and HTMX, and is usable by both experienced developers and new coders. One of the biggest hurdles we've noticed for experts is that they assume all the complexity of prior frameworks is necessary, and that's not true. So be sure to read the docs and examples, and keep an open mind!

#### A new generation of coders

Coding is the key to turning the ideas in your head into products and services that can help people. AI has recently made it easier to get started with coding, which means there are more people than ever before who can create useful stuff.

But this new generation of coders do not generally have the same background as full-time software engineers. They may have been trained in a different field, or they may have learned to code on their own. We hope that FastHTML will make it easier for this new generation of coders to turn their ideas into reality. To create maintainable and scalable solutions.
"""

s3 = """
FastHTML works well right now, but it is still young. We are using it for nearly every part of the FastHTML project itself. For instance, we worked with a design team to create the [fastht.ml home page](https://www.fastht.ml/), which is implemented in FastHTML---here is the [home page source](https://github.com/AnswerDotAI/home-fasthtml/blob/main/main.py).

We're working on a number of things to make FastHTML even better. Not everything is ready "out of the box" yet. If you see something missing that you need, please let us know by [creating an issue](https://github.com/AnswerDotAI/fasthtml/issues). Or feel free to add it yourself and send in a pull request!

The plan is for FastHTML to do just about everything that frameworks like Django, NextJS, and Ruby on Rails do, but it'll take a while to get there! For experienced developers, adding bindings to CSS frameworks, pypi Python modules, and JS libraries is straightforward---if you add one, please put your binding module on pypi so that the community can use it, and let us know so we can link to your project. We invite you to use the "`fh-`" prefix on PyPI to make it easy to identify FastHTML packages there.

Here's a few of the things on our short to medium term agenda:

- OAuth support
- Support for more databases
- Support for more CSS frameworks, including DaisyUI, Bootstrap, Shoelace, and Flowbite (we've already made a start at all of these).
"""
