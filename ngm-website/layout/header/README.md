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

## Menu contents (Sep 2026)

Both the desktop dropdowns and the mobile submenus hold the same entries —
**change them in pairs**, or the phone menu silently drifts from the desktop
one.

**Meetings:** Daytime Counted Thread & Needlepoint · Potpourri Stitchers ·
Daytime Stitch-In · Evening Stitch-In · Sunday Tea & Stitch · Come & Stitch ·
Zoom and Stitch · 5th Tuesday Open Stitching

**Events:** Annual Retreat 2027 · Annual Meeting 2027 · March to the Finish ·
A Fall Finish · Traditional Japanese Embroidery · Workshops

Recent moves: 5th Tuesday Open Stitching went from Events to Meetings (Kym
Aug 24, Jody Sep 10); Retreat 2026 was swapped for Retreat 2027 and Annual
Meeting 2027 added (Vivien, Sep 19); Zoom and Stitch and Retreat 2027 were
added (Jody, Sep 15).

⚠ **Three of those hrefs are guesses** — `/zoom-and-stitch`,
`/annual-meeting-2027` and `/annual-retreat-2027`. The pages are being
written by Jody and Vivien and this session had no way to reach the live
site to read the real slugs. Check each in WA (Website → Site pages) and
correct the href before pasting. `docs/backlog-status.md` tracks this.

## This is not the WA menu

This gadget **is** the site's visible navigation; WA's own navigation menu is
hidden by `global.css` (`.navigation-menu`, `.menu-navigation`, … →
`display:none`). So editing WA's menu in the admin UI changes nothing a
visitor sees, and a stale `?pageId=…` entry in it produces a link nobody can
click. Anything menu-shaped is edited **here** and pasted into the site-wide
template. Worth knowing before showing anyone "how to edit the top menu".
