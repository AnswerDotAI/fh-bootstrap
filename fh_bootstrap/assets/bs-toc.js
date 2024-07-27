// This is a rewrite of https://afeld.github.io/bootstrap-toc/

const find = sel => any(sel).filter(e => !e.attribute('data-toc-skip'));
const childNav = p => p.appendChild($E('ul', {cls:'nav navbar-nav'}));

const initTOC = (tocId='toc') => {
  document.addEventListener('DOMContentLoaded', () => {
    const top = [1,2,3,4,5,6].find(i => find("h"+i).length > 1) || 1;
    any(`nav[data-toggle="${tocId}"]`).forEach(nav => {
      const topctx = childNav(nav);
      let ctx = topctx, prevNav;
      find(`h${top},h${top+1}`).forEach(el => {
        const text = el.dataset.tocText || el.textContent;
        if (!el.id) el.id = 'id-' + crypto.randomUUID().slice(-12);
        const newNav = $H`<li><a class="nav-link" href="#${el.id}">${text}</a></li>`;
        ctx = (+el.tagName[1]) === top ? topctx :
          prevNav && ctx === topctx ? childNav(prevNav) : ctx;
        ctx.appendChild(newNav);
        prevNav = newNav;
      });
    });
  });
};
