from app import *

@rt('/components')
def get():
    h2s = 'Why', 'How', 'The future'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(2, "Python components", *secs)

s1 = """"""

s2 = """"""

s3 = """"""
