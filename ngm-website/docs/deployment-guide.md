# NGM Redesign — Deployment / Cutover Guide

Everything you need to take the redesign from this repo onto the live Wild Apricot
site. **Nothing here is on the live site yet** — this is the plan for cutover day.

> **Safety net:** before you change the live Global CSS, you already have
> `global-css/current-live-backup.css` — an exact copy of what's live now. If anything
> looks wrong mid-cutover, paste that back into the WA **CSS** tab to revert instantly.

---

## The cutover order (do it in this sequence)

Doing it in this order means the site is never half-styled:

1. **Paste the master Global CSS.** WA admin → **CSS** tab → replace its contents with
   `global-css/global.css` → Save. (This is the whole redesign's styling.)
2. **Update the site template** with the new header and footer:
   - Header: `layout/header/01-top.html` → the site-wide Custom HTML gadget in the template.
   - Footer: `layout/footer/01-top.html` → the footer gadget.
3. **Do each page** (below). For each: open the WA page, paste the block(s) in order,
   add any native gadget between them, Save.
4. **Swap pages to their slim version.** Once the Global CSS is live, each page gadget's
   own `<style>` is redundant — replace each `01-top.html` with `01-top.slim.html`
   (and `03-bottom.html` with `03-bottom.slim.html`). Optional but keeps things clean.
5. **Spot-check** each live page (logged out and logged in).

---

## Pages

**Single** = one Custom HTML gadget (`01-top.html`).
**Sandwich** = `01-top.html` → native WA gadget (see the page's `02-wa-gadget.txt`) → `03-bottom.html`.

| Page | Live URL | Type | Middle gadget |
|------|----------|------|---------------|
| Homepage | `/` | Sandwich | Upcoming events (`ngm-wa-events`) |
| About | `/about-us` | Single | — |
| Calendar | `/calendar` | Sandwich | WA **Calendar** gadget (`ngm-cal`) |
| Events (landing) | `/events` | Sandwich | Upcoming events |
| Workshops | `/workshops` | Sandwich | Upcoming events → filter to workshops |
| Join | `/join` | Single | — |
| Meetings | `/monthly-meetings` | Sandwich | Upcoming events |
| Stitch-Ins | `/daytime-stitch-in` (+ `/evening-stitch-in`) | Sandwich | Upcoming events |
| Daytime Counted Thread | `/daytime-counted-thread` | Sandwich | Upcoming events → filter to this group |
| Evening Needlepointers | `/evening-needlepointers` | Sandwich | " |
| Potpourri Stitchers | `/potpourri-stitchers` | Sandwich | " |
| Beading | `/beading` | Sandwich | " |
| Retreat | `/retreat` | Single | — |
| Japanese Embroidery | `/japanese-embroidery` | Sandwich | Upcoming events → filter |
| 5th Tuesday | `/fifth-tuesday` | Sandwich | Upcoming events → filter |
| Member Hub | `/members` | Sandwich | Upcoming events |
| Donate | `/donate` | Single | — |
| Contact | `/contact-us` | Single | — |

For every sandwich page, set the native gadget's **CSS class** and filter per its
`02-wa-gadget.txt`, and set the gadget's layout **row background to linen (#F0EAE0)**.

## System pages (WA built-ins)

| Page | Live URL | Status |
|------|----------|--------|
| Login | `/Sys/Login` | ✅ Built — branded heading (`system-pages/login/`) + form skin in Global CSS |
| Membership application | `/application` | Skin in Global CSS + optional branded heading (`system-pages/membership-application/`) |
| Member profile | `/Sys/Profile` | CSS-only skin in Global CSS (verify against the live page) |
| Renewal | `/Sys/Profile` renewal flow | CSS-only skin in Global CSS (verify) |
| Contact profile | contact profile screen | CSS-only skin in Global CSS (verify) |

The account/login **button** (name → View profile / Change password / Log out) is skinned
site-wide in Global CSS (`WaGadgetLoginForm`).

---

## ⚠️ Set these real URLs before (or during) cutover

The redesign uses placeholders where only you know the real WA page:

| Where | Placeholder | Point it at |
|-------|-------------|-------------|
| Member Hub cards (`member-hub/03-bottom.html`) | `/directory` | your WA member directory page |
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
- The full self-contained page versions stay in the repo as backups even after you swap
  to slim; both always render correctly.
