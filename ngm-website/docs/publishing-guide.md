# NGM Redesign — Publishing / Cutover Guide

Everything you need to take the redesign from this repo onto the live Wild Apricot
site by pasting it in (WA has no GitHub publishing — every change is a manual paste
into a WA gadget or the CSS tab).

> **Safety net:** before you change the live Global CSS, you already have
> `global-css/current-live-backup.css` — an exact copy of what's live now. If anything
> looks wrong mid-cutover, paste that back into the WA **CSS** tab to revert instantly.

> **Paste from `dist/`.** Every paste file has a production-clean twin under
> `ngm-website/dist/` (same relative path, comments stripped — no maintainer
> notes go onto the live site). The commented originals stay the files you
> EDIT; after any edit, regenerate with
> `python3 ngm-website/tools/build-dist.py`. Never hand-edit `dist/`.

---

## The cutover order (do it in this sequence)

Doing it in this order means the site is never half-styled:

1. **Paste the master Global CSS.** WA admin → **CSS** tab → replace its contents with
   `global-css/global.css` → Save. (This is the whole redesign's styling.)
2. **Update the site template** with the new chrome — ONE gadget:
   - Paste `dist/layout/site-chrome/01-top.html` (header + footer +
     feedback pill combined) into a single Custom HTML gadget
     **anywhere** in the template, and delete the old separate
     header/footer/feedback gadgets. Every piece positions itself: the
     header fixes to the top, the footer lifts itself to the very
     bottom of the page, the pill floats bottom-right.
   - (The separate `dist/layout/header|footer|feedback-button` files
     still exist if you prefer three gadgets.)
   - **Every template, not just the main one.** The `/Sys/*` system pages
     (member public profile, Send-message, login, etc.) can use a
     DIFFERENT page template that still carries the old chrome (tapestry
     strip, maroon photo banner, purple nav). In WA admin → Website →
     **Page templates**, open each template in use and give it the same
     treatment: delete the old banner/nav gadgets, paste the new
     header + footer gadgets. (The new header's CSS also hides WA's
     native purple navigation menu.) Spot-check
     `/Sys/PublicProfile/...` and its Send-message page afterwards.
3. **Fonts in Raw Headers** (kills the font flash on every click). WA admin →
   **Settings → Site → Meta-tags → Raw Headers** — add:

   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap">
   ```

   Raw Headers reach every page on every template BEFORE first paint. The
   header gadget carries the same links as a fallback (the browser dedupes
   the duplicate request) — but body-gadget links load after first paint,
   which is what made pages visibly re-font on each navigation.
4. **Do each page** (below). For each: open the WA page, paste the block(s) in order,
   add any native gadget between them, Save.
5. **Global CSS must be live first.** The page `.html` files carry no `<style>` of
   their own — they rely entirely on the Global CSS for styling, so make sure the
   Global CSS tab holds the full `global.css` before/when you paste the page gadgets.
6. **Spot-check** each live page (logged out and logged in) — including the
   error pages: hit a made-up URL for the 404, and open a members-only page
   while logged out for the 403.

---

## Pages

**Single** = one Custom HTML gadget (`01-top.html`).
**Sandwich** = `01-top.html` → native WA gadget (see the page's `02-wa-gadget.txt`) → `03-bottom.html`.

> **Sandwich pages can be ONE gadget.** Every sandwich page also has
> `dist/<page>/one-gadget.html`: paste that single file into ONE Custom-HTML
> gadget placed **above** the native gadget, and skip the bottom gadget
> entirely. The top half renders in place; the bottom half is hidden until a
> script moves it directly **below** the native gadget, then reveals it (no
> flash). The separate `01-top.html` / `03-bottom.html` files remain if you
> prefer two gadgets.
>
> **Exception — the Login page stays TWO gadgets.** Its WA layout is a real
> two-column split (green hero cell | form cell), so a single gadget above
> the form cannot place the closing line inside the right cell. Paste
> `dist/system-pages/login/01-top.html` in the LEFT cell, the native login
> gadget in the right cell, and `03-bottom.html` under it in that same right
> cell. (No `one-gadget.html` is generated for it.)

| Page | Live URL | Type | Middle gadget |
|------|----------|------|---------------|
| Homepage | `/` | Sandwich | Upcoming events (`ngm-wa-events`) |
| About | `/about` | Single | — |
| Calendar | `/calendar` | Sandwich | WA **Calendar** gadget (`ngm-cal`) |
| Events (landing) | `/events` | Sandwich | Upcoming events |
| Workshops | `/workshops` | Sandwich | Upcoming events → filter to workshops |
| Join | `/join` | Single | — |
| March to the Finish | `/march-to-the-finish` | Single | — |
| A Fall Finish | `/a-fall-finish` | Single | — |
| Meetings | `/meetings` | Sandwich | Upcoming events |
| Stitch-Ins | `/daytime-stitch-in` (+ `/evening-stitch-in`) | Sandwich | Upcoming events |
| Daytime Counted Thread | `/daytime-counted-thread-&-needlepoint` | Sandwich | Upcoming events → filter to this group |
| Evening Needlepointers | `/evening-needlepointers` | Sandwich | " |
| Potpourri Stitchers | `/potpourri-stitchers` | Sandwich | " |
| Retreat | `/annual-retreat-2026` | Single | — |
| Japanese Embroidery | `/traditional-japanese-embroidery` | Sandwich | Upcoming events → filter |
| 5th Tuesday | `/5th-tuesday-open-stitching` | Sandwich | Upcoming events → filter |
| Member Hub | `/member-hub` | Single | — |
| Donate | `/donate` | Single | — |
| Contact | `/contact` | Single | — |

For every sandwich page, set the native gadget's **CSS class** and filter per its
`02-wa-gadget.txt`, and set the gadget's layout **row background to linen (#F0EAE0)**.

## System pages (WA built-ins)

Paste each from `dist/system-pages/<name>/`. Find them in WA admin →
**Website → System pages**, open the page, and paste into a Custom-HTML
gadget (some are heading-only banners that sit ABOVE the native content —
see each page's README).

| WA system page | Paste file | Notes |
|------|------|------|
| Page not found (404) | `page-not-found/01-top.html` | Full branded page |
| Access denied (403) | `access-denied/01-top.html` | Full branded page — members-only message |
| Authorization required | `authorization-required/01-top.html` | Banner above the native login form |
| Login | `login/01-top.html` + `03-bottom.html` | TWO gadgets, two-column layout: hero in the left cell; native form + `03-bottom.html` in the right cell |
| Change password | `change-password/01-top.html` | Banner above the native form |
| Event details | `event-details/01-top.html` + `03-bottom.html` | Or `one-gadget.html` (single gadget above the native gadget) |
| Event registration | — | BLOCKED: needs a live registration to dump (see its README) |
| Member profile | — | CSS-only skin in Global CSS |
| Contact profile | `contact-profile/01-top.html` | Banner + CSS skin |
| Renewal | `renewal/01-top.html` | Banner + CSS skin |
| Membership application | `membership-application/01-top.html` | Banner; form skinned in Global CSS |
| Terms of use | `terms-of-use/01-top.html` | Branded heading ABOVE the existing legal text |
| Unsubscribe | `unsubscribe/01-top.html` | Banner above the native controls |
| Member directory | `pages/member-directory/01-top.html` | A normal page, not a system page (`/member-directory`) |

The account/login **button** (name → View profile / Change password / Log out) is skinned
site-wide in Global CSS (`WaGadgetLoginForm`).

---

## ⚠️ Set these real URLs before (or during) cutover

The redesign uses placeholders where only you know the real WA page:

| Where | Placeholder | Point it at |
|-------|-------------|-------------|
| Member Hub cards (`member-hub/03-bottom.html`) | `/member-directory` | your WA member directory page |
| Member Hub cards | `/resources` | your member-only resources / documents page |
| Donate buttons (`donate/01-top.html`) | `/donation` | your WA donation form |

Search the repo for `SET URL` and `/donation` to find them all.

## Photos to add

Every page has photo placeholders (dashed sage boxes labelled with what fits). To add a
real photo, replace the placeholder `<div class="ngm-mt-photo">…</div>` with:
`<img src="…your image URL…" alt="…" style="width:100%;height:100%;object-fit:cover;border-radius:var(--ngm-radius-lg)">`
Guild images live at `needleworkguildmn.org/resources/Pictures/…`. The Retreat, Workshops,
Join, About, Meetings, Stitch-In, and Events pages already use real photo URLs as examples.

---

## After cutover
- Keep `current-live-backup.css` updated if you ever hand-edit the live Global CSS.
- Page markup lives in the `*.html` files (markup only); all styling is in the Global
  CSS. There is no separate self-contained copy to keep in sync.
