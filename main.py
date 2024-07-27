from bootstrap import *
import vision, overview, foundations, tech, components

hdrs = (
    Style(''':root, [data-bs-theme=light] {
    --bs-secondary: #3cdd8c;
    --bs-secondary-rgb: 60, 221, 140;
}
nav.navbar { --bs-btn-hover-bg: rgba(255,255,255,0.2); }
.nav-link:hover { color: rgba(255,255,0,0.6); }
.nav-link.active { font-weight: bold; }'''),
    Link(href='assets/hl-styles.css', rel='stylesheet'),
)

app,rt = fast_app(pico=False, hdrs=bst_hdrs+hdrs, live=True)

@rt('/')
def get(): return overview.page()

@rt('/components')
def get(): return components.page()

@rt('/foundation')
def get(): return foundations.page()

@rt('/tech')
def get(): return tech.page()

@rt('/vision')
def get(): return vision.page()

run_uv()
