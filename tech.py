from app import *

@rt('/tech')
def get():
    h2s = 'Python', 'Starlette', 'Uvicorn', 'HTMX', 'SQLite'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3), Markdown(s4), Markdown(s5)]
    secs = Sections(h2s, txts)
    return BstPage(2, "FastHTML's tech stack", *secs)

s1 = """"""

s2 = """"""

s3 = """"""

s4 = """"""

s5 = """"""
