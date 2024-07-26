from fasthtml.common import *
from enum import Enum
from markdown import markdown

def Markdown(s, **kw): return Div(NotStr(markdown(s, extensions=['smarty', 'extra', 'sane_lists'])), **kw)

bst_sz_d = {'576':'sm', '768':'md', '992':'lg', '1200':'xl', '1400':'xxl'}
jsdurl = 'https://cdn.jsdelivr.net/npm'
bst_styleurl = f'{jsdurl}/bootstrap@5.3.3/dist'
bst_jsurl = f'{jsdurl}/bootstrap@5.3.3/dist/js'
fa_cfurl = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1'
tocurl = 'https://cdn.rawgit.com/afeld/bootstrap-toc/v1.0.1/dist'
capsels = 'figure.d-table figcaption, ' + ', '.join(f'figure.d-{k}-table figcaption'
                                                    for k in bst_sz_d.values())
bst_hdrs = (
    Link(href=f"{bst_styleurl}/css/bootstrap.min.css", rel="stylesheet"),
    Link(href=f"{fa_cfurl}/css/all.min.css", rel="stylesheet"),
    Style(capsels + '''{
        caption-side: bottom;
        font-style: italic; font-size: 85%;
        color: color-mix(in srgb, currentColor 75%, transparent);
    }'''),
    Style('\n'.join(
        f'@media (min-width: {k}px) {{ figure.d-{v}-table figcaption {{ display: table-caption; }} }}'
        for k,v in bst_sz_d.items())),
    StyleX('assets/fh-bootstrap.css'),
    Script(src="https://cdn.jsdelivr.net/gh/AnswerDotAI/fasthtml-js@main/fasthtml.js"),
    Script(src=f"{bst_styleurl}/js/bootstrap.bundle.min.js"),
    Script(src=f"assets/bs-toc.js"),
    Link(href=f"{tocurl}/bootstrap-toc.min.css", rel="stylesheet")
)

def placehold(x,y): return f'https://placehold.co/{x}x{y}'

class VEnum(Enum):
    def __str__(self): return self.value

class BSEnum(Enum):
    def __str__(self):
        r = self.value
        nm = self.__class__.__name__.rstrip('T').lower()
        if not r: return nm
        return f'{nm}-{r}'

class ContainerT(BSEnum):
    Basic = ''
    Fluid = 'fluid'
    Sm = 'sm'
    Md = 'md'
    Lg = 'lg'
    Xl = 'xl'
    Xxl = 'xxl'

class SizeT(VEnum):
    Default = ''
    Sm = 'sm'
    Md = 'md'
    Lg = 'lg'
    Xl = 'xl'
    Xxl = 'xxl'

def Container(*c, typ:ContainerT|str=ContainerT.Basic, cls='', **kw):
    return Div(*c, cls=f'{typ} {cls}', **kw)

class PlacementT(VEnum):
    Default = ''
    FixedTop = 'fixed-top'
    FixedBottom = 'fixed-bottom'
    StickyTop = 'sticky-top'
    StickyBottom = 'sticky-bottom'

class PositionT(BSEnum):
    Static = 'static'
    Relative = 'relative'
    Absolute = 'absolute'
    Fixed = 'fixed'
    Sticky = 'sticky'

def NavbarItem(text, href='#', current=False, disabled=False, cls='', **kw):
    acls = 'nav-link'
    if current:
        kw['aria_current'] = 'page'
        cls += ' active'
        acls += ' active'
    if disabled:
        kw['aria_disabled'] = 'true'
        acls += ' disabled'
    return Li(A(text, href=href, cls=acls, **kw), cls='nav-item '+cls)

def Navbar(id, selidx, items, ra_items=None, image=None, text=None, hdr_href='#', dark=False,
           cls='', itemcls='', expand='lg',
           container=ContainerT.Fluid, placement=PlacementT.Default, **kw):
    image = Img(src=image, cls='d-inline-block align-text-bottom') if image else None
    if dark:
        kw['data-bs-theme'] = 'dark'
        cls += ' bg-dark'
    def mk_navitem(i, o):
        if isinstance(o, XT): return o
        text, href, *kw = o
        kw = kw[0] if kw else {}
        return NavbarItem(text, href, i==selidx, cls=itemcls, **kw)
    items = [mk_navitem(i, o) for i,o in enumerate(items)]
    if not ra_items: ra_items = []
    if isinstance(ra_items, XT): ra_items = [ra_items]
    return Nav(
        Div(
            A(image, text, href=hdr_href, cls='navbar-brand'),
            Button(
                Span(cls='navbar-toggler-icon'), type='button',
                data_bs_toggle='collapse', data_bs_target=f'#{id}',
                aria_controls=id, aria_expanded='false', aria_label='Toggle navigation',
                cls='navbar-toggler'),
            Div(
                Ul(*items, cls='navbar-nav me-auto mb-2 mb-lg-0'), *ra_items,
                id=id, cls='collapse navbar-collapse'),
            cls=container),
        cls=f'navbar navbar-expand-{expand} {placement} {cls}', **kw)

def NavText(text): return Span(text, cls='navbar-text')

def Image(src, alt=None, sz:SizeT=SizeT.Sm, caption=None, capcls='', pad=2, left=True, cls='', retina=True, **kw):
    place = 'start' if left else 'end'
    if retina: kw['srcset'] = f'{src} 2x'
    return Figure(
        Img(src=src, alt=alt, 
            cls=f'figure-img img-fluid {cls}', **kw),
        Figcaption(caption, cls=f'caption-{sz} {capcls} text-center'),
        cls=f'd-sm-table float-{sz}-{place} mx-{sz}-{pad+1} my-{sz}-{pad}')

def Icon(ico, dark=False, sz='', cls='', button=True, **kw):
    cls += f' {ico}'
    if dark: cls += ' btn-dark'
    if sz: cls += f' btn-{sz}'
    if button:
        kw['role'] = 'button'
        cls += ' btn'
    return I(cls=cls, **kw)

def Toc(*c, width=2):
    return Div(
        Div(
            Nav(id='toc', data_toggle='toc', cls='sticky-top'),
            cls=f'col-sm-{width}'),
        Div(*c, cls=f'col-sm-{12-width}'),
        cls='row')

def BstFooter(copy, img, img_href, cs, cls='', **kw):
    # From the bootstrap examples footers page
    return Container(
        Footer(
            P(copy, cls='col-md-4 mb-0 text-muted'),
            A(img, href=img_href,
                cls='col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none'),
            Ul(*[Li(o, cls='nav-item') for o in cs], 
                cls='nav col-md-4 justify-content-end'),
            cls=f'{cls} d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top', **kw))
