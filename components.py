from app import *

def page():
    h2s = 'Why', 'How', 'The future'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3)]
    secs = Sections(h2s, txts)
    return BstPage(4, "Python components", *secs)

s1 = """"""

s2 = """"""

s3 = """"""
