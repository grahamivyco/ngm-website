# Authorization required

**WA system page:** Authorization required

Shown when the visitor is **signed out** and the page requires a login.
Its sibling `access-denied` (403) covers the other case — signed IN but
without rights — so keep this page's message purely about signing in.

- `01-top.html` &mdash; markup only; styling comes from the Global CSS (must be live in WA).
- `01-top.html` &mdash; relies on the `.ngm-sys` skin in `global-css/global.css`; paste this at cutover.

The `.ngm-sys` intro-band skin lives in the master `global.css` (SYSTEM-PAGE INTRO BANDS section).
