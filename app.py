from fasthtml.common import *
from bootstrap import *
from itertools import chain

ghurl = 'https://github.com/AnswerDotAI/fasthtml'
fhurl = 'https://fastht.ml'

hdrs = (Style(''':root, [data-bs-theme=light] {
  --bs-secondary: #3cdd8c;
  --bs-secondary-rgb: 60, 221, 140;
}
nav.navbar { --bs-btn-hover-bg: rgba(255,255,255,0.05); }
.nav-link:hover { color: rgba(255,255,0,0.6); }
.nav-link.active { font-weight: bold; }'''),)

app,rt = fast_app(pico=False, hdrs=bst_hdrs+hdrs, live=True)

def BstPage(selidx, title, *c):
    navitems = [('Overview', '/'), ('Vision', '/vision'), ('Foundations', '/foundation'),
                ('Components', '/components'), ('Technology', '/tech'), ('Limitations', '#', {'disabled':True})]
    ghico = Icon('fab fa-github', dark=False, sz='lg', href=ghurl)
    nb = Navbar('nav', selidx, items=navitems, ra_items=ghico, cls='navbar-light bg-secondary rounded-lg',
                image='logo.svg', hdr_href=fhurl, placement=PlacementT.Default)
    return (
        Title(title),
        Script('initTOC()'),
        Container(nb,
            Toc(Container(H1(title, cls='pb-3'), *c, mt=3)),
        typ=ContainerT.Xl, mt=3, data_bs_spy='scroll', data_bs_target='#toc')
    )

def Sections(h2s, texts):
    colors = 'yellow', 'pink', 'teal', 'blue'
    div_cls = 'py-2 px-3 mt-4 bg-light-{} rounded-tl-lg'
    return chain([Div(H2(h2, id=f'sec{i+1}', cls=div_cls.format(colors[i%4])), txt)
                  for i,(h2,txt) in enumerate(zip(h2s, texts))])
