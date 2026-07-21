# Site Header / Nav (global)

**Structure:** SINGLE Custom HTML gadget — `01-top.html`. Login-state aware
via `body.memberContentView` / `body.publicContentView` (CSS + JS). Paste into
the site-wide page template so it appears on every page.

**Favicon:** set **natively in Wild Apricot**, not in this gadget. In WA admin:
**Settings → Site → Meta-tags → Raw Headers**, and add a `<link rel="icon">`
pointing at the uploaded icon. Upload `brand/favicon.ico` via **Website → Files**
(Pictures folder). Doing it here is the official way — it puts the icon in the
server-rendered `<head>`, so it shows in the browser tab/bookmarks with no flash.
(An earlier version injected the favicon from this gadget's JS; that loaded too
late — WA's default icon flashed first and it never reached the tab — so it was
removed.) See `brand/README` context and `docs/wa-notes.md`.
