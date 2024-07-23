from fasthtml.common import *
from bootstrap import *
from itertools import chain

app,rt = fast_app(pico=False, hdrs=bst_hdrs)
ghurl = 'https://github.com/AnswerDotAI/fasthtml'
fhurl = 'https://fastht.ml'

@rt('/')
def get():
    navitems = [('Overview', '#'), ('Foundations', '#'), ('Components', '#'),
                ('Limitations', '#', {'disabled':True})]
    ghico = Icon('fab fa-github', dark=True, sz='lg', href=ghurl)
    caption='This is a caption for the image. It wraps properly when the figure is floating.'
    fig = Image(src=placehold(250,250), alt='Placeholder', caption=caption, pad=3, left=False)
    para = P('This paragraph of text should wrap around the figure on small screens and above. '*4)
    secs = tuple(chain(*[(H2(f'Section {i}', id=f'sec{i}'), fig, tuple([para]*4)) for i in range(1,4)]))
    nb = Navbar('nav', 0, items=navitems, ra_items=ghico, dark=True, image='logo.svg', hdr_href=fhurl, placement=PlacementT.Default)
    return (
        Title('Bootstrap FastHTML demo'),
        Script('onloadTOC()'),
        Container(
            nb,
            Toc(Container(
                H1('This is a heading', cls='mb-4'), *secs,
                mt=3)),
        typ=ContainerT.Xl, mt=3, data_bs_spy='scroll', data_bs_target='#toc')
    )

run_uv()
