# Authorization required

**WA system page:** Authorization required

Shown when a page needs the visitor to authenticate first.

- `01-top.html` &mdash; self-contained (own fonts + CSS); works even before the new Global CSS is live.
- `01-top.slim.html` &mdash; relies on the `.ngm-sys` skin in `global-css/global.css`; paste this at cutover.

The `.ngm-sys` intro-band skin lives in the master `global.css` (SYSTEM-PAGE INTRO BANDS section).
