# Access denied (403)

**WA system page:** Access denied (403)

Shown when someone tries to open a members-only page without access.

- `01-top.html` &mdash; self-contained (own fonts + CSS); works even before the new Global CSS is live.
- `01-top.slim.html` &mdash; relies on the `.ngm-sys` skin in `global-css/global.css`; paste this at cutover.

The `.ngm-sys` intro-band skin lives in the master `global.css` (SYSTEM-PAGE INTRO BANDS section).
