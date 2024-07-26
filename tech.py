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
"""

s3 = """"""

s4 = """"""

s5 = """"""

