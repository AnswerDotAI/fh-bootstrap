from app import *

@rt('/')
def get():
    caption = "'Real' web development shouldn't be this hard..."
    fig = Image('webdev.jpg', alt='Web dev', caption=caption, left=False)
    h2s = 'Getting started', 'Background', 'Current Status'
    txts = [Markdown(s1), Div(fig, Markdown(s2)), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(0, 'About FastHTML', *secs)

s1 = """
You're using a FastHTML app right now. We didn't create a separate blog system for this site, because with FastHTML building apps is so easy there's no need for it! 

If you're an experienced web developer, then you can use all your knowledge of CSS, HTML, HTTP, and JavaScript to build web applications with FastHTML right away. We've heard from expert coders that they've successfully built complete web applications within an hour of first getting started with FastHTML. We've got a [Quickstart for Web Developers](https://docs.fastht.ml/quickstart_for_web_devs.html) that will get you up and running quickly (and read the rest of the docs while you're there!). Be sure to also read through the heavily-commented source of this [idiomatic fasthtml app](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py). Then, study some of the [fasthtml-example applications](https://github.com/AnswerDotAI/fasthtml-example), particularly the first four listed. One of the biggest hurdles we've noticed for experts is that they assume all the complexity of prior frameworks is necessary, and that's not true. So be sure to read the docs and examples, and keep an open mind!

If you haven't done much (or any) web development, try following through each step of [FastHTML By Example](https://docs.fastht.ml/by_example.html). We don't yet have a self-contained guide explaining all the HTML, HTTP, CSS, etc foundations you'll need to know, so you'll probably need to do some self-learning through other resources too. But watch this space -- we're planning a complete web programming from scratch course soon!
"""

s2 = """
FastHTML is a system for writing web applications in Python. It is designed to be simple, powerful, and flexible. It is also designed to be easy to learn and use.

The project was originally started by Jeremy Howard at Answer.AI for a number of reasons:

- Over the last 25 years of web development Jeremy had realised that web programming could be both easier and more powerful. He was particularly concerned that recent trends had moved away from the power of the web's foundations, resulting in a fractured ecosystem of over-complex frameworks and tools
- He realised that two small but ingenious developments had made the web's foundations more powerful and more accessible: **ASGI** and **HTMX**. But the tools available for using them were still too complex, and the barriers to entry were still too high
- Jeremy and his wife Rachel had spent the last 8 years working to make artifical intelligence more accessible to more people, and noticed that the most widely used web development tools were too complex for people who aren't full time coders. This meant that Jeremy and Rachel's students struggled to turn their AI project ideas into working applications
- Jeremy's goal for Answer.AI is to help society benefit from AI, which means creating lots of useful products and services that use AI effectively -- and that means that creating those products and services needs to be made as fast and easy as possible.

FastHTML is a framework that deals with all these issues: it returns to the roots of the web, leveraging ASGI and HTMX, and is usable by both experienced developers and new coders.

#### A new generation of coders

Coding is the key to turning the ideas in your head into the products and services that can help people. AI has recently made it easier to get started with coding, which means there are more people than ever before who can create useful stuff.

But this new generation of coders do not generally have the same background as full-time software engineers. They may have been trained in a different field, or they may have learned to code on their own. We hope that FastHTML will make it easier for this new generation of coders to turn their ideas into reality, and to create maintainable and scalable solutions which they can iterate on and continuously improve.
"""

s3 = """
FastHTML works well right now, but it's still young. We're working on a number of things to make it even better. Not everything is ready "out of the box" yet. If you see something missing that you need, please let us know by [creating an issue](https://github.com/AnswerDotAI/fasthtml/issues). Or feel free to add it yourself and send in a PR!

The plan is for FastHTML to do just about everything that frameworks like Django, NextJS, and Ruby on Rails do, but it'll take a while to get there! For experienced developers, adding bindings to CSS frameworks, pypi Python modules, and JS libraries is straightforward -- if you add one, please put your binding module on pypi so that the community can use it, and let us know so we can link to your project.

Here's a few things on our short to medium term agenda:

- OAuth support
- Support for more databases
- Support for more CSS frameworks, including DaisyUI, Bootstrap, Shoelace, and Flowbite (we've already made a start at all of these).
"""
