# Board Minutes

Replaces the existing WA page **"Meeting Minutes"** (`pageId 18146`), which
lists 2025 and 2024 as two plain bulleted columns of links.

**Update that page — don't make a new one.** It already exists and already
holds the list; a second minutes page means two things to keep current.

## Structure: sandwich

```
01-top.html       Custom HTML — hero + "Minutes by meeting" heading
02-wa-gadget.txt  native WA CONTENT gadget — the list of meetings
03-bottom.html    Custom HTML — "About these minutes" tiles + CTA
```

The list lives in the **native gadget**, not in this repo. That is the whole
point: adding a set of minutes is a monthly job for the secretary, and it
should not require editing HTML, rebuilding `dist/`, or pasting a gadget.

## Adding a set of minutes

1. Upload the PDF via **WA → Website → Files**.
2. Open the page in WA and edit the **content gadget**.
3. Type the date at the top of the right year's list, select it, insert the
   link to the PDF. Save.

That's it. No HTML, no repo, no paste step, nothing to keep in sync.

**A meeting whose minutes aren't written up yet:** type the date and leave
it unlinked. It styles itself as a muted row with a "Not posted" chip. The
old page did this too, but as a bare bullet among ten links, which just
reads as a broken link.

**A new year:** add a heading containing the year (any heading level, the
year alone is enough) above the others, then a fresh list under it.

Full rules for how the gadget's content must be structured are in
`02-wa-gadget.txt`. The short version: one heading per year, one bulleted
list under it, one meeting per bullet, newest first, single column.

**`docs/adding-minutes.md` is the handout version** — the same steps written
for whoever posts the minutes, with no repo or code references in it. Send
them that, not this file.

## The existing links carry over

**Nothing needs harvesting.** The current page's list already holds all 21
PDF links. Move that content into the content gadget as-is and the CSS
restyles it — the hrefs come along untouched.

This is the main practical reason to do it as a sandwich rather than as
Custom HTML: the PDF URLs never have to be read off the old page, retyped,
or kept anywhere in this repo.

## ⚠ Check the restriction first

In the WA **Site pages** list, "Meeting Minutes" sits under *Pages not in
menu* and shows **no padlock**. Member Hub shows one. If that's accurate, the
board minutes are reachable by anyone with the URL right now.

This page tells members not to forward the files. Before pasting it, either
restrict the page to members or take that line out. Don't ship the claim
without the restriction.

"Not in menu" is not access control. It only hides the page from navigation.

## ⚠ Nothing has been posted since November 2025

The list ends at 11 November 2025, and that date has no link. It is now
September 2026, so roughly ten months of minutes are missing. Worth raising
with the secretary before this goes live.

## Wild Apricot setup

1. Open the existing **Meeting Minutes** page (`pageId 18146`).
2. **Restrict it to members** (see above).
3. Paste `dist/pages/board-minutes/01-top.html` into a Custom HTML gadget
   at the top. `global.css` must already be live in the CSS tab.
4. Put the existing list into a **Content** gadget below it and set its
   **CSS class** to `ngm-wa-minutes` — see `02-wa-gadget.txt`. Reshape the
   content to one heading + one list per year, single column.
5. Paste `dist/pages/board-minutes/03-bottom.html` into a second Custom HTML
   gadget below that.
6. All three gadgets go in the **same layout row**, row background
   transparent or white so the band runs continuously.
7. Consider a friendly URL (`/board-minutes`) — the Member Hub tile in
   `pages/member-hub/01-top.html` already points there, so either set that
   slug or change the tile.

## How the styling works

`global.css`, section "BOARD MINUTES".

The WA content editor writes **no classes** — just a heading per year and a
plain `<ul>` of `<li>`, each holding a link or bare text. So the rules style
that raw output directly, hooked on the gadget's own CSS class
(`ngm-wa-minutes`, set in gadget settings). Same trick `.ngm-wa-events` uses,
and the reason no unstable per-instance `id_*` selector is needed.

- Year headings: `h1`–`h4` inside the gadget get the serif treatment and the
  rule line. Only the year is typed.
- Rows: each `li` is a flex row with a hairline. The file icon is painted as
  `li::before` — the editor can't insert one and shouldn't have to.
- The link fills the row, so the hit area is the full width, not just the
  date's. Arrow appears on hover/focus via `a::after`.
- Unlinked bullets are caught with `li:not(:has(a))` and get the muted
  treatment plus the "Not posted" chip. `:has()` is already used elsewhere
  in this file.
- `body` prefix + `!important` on font properties throughout: WA's theme
  re-fonts and bolds anchors inside its own gadgets.

The hero, tiles and CTA ride the existing shared rules — `.ngm-min-*` was
added to the `.ngm-lib-hero` / `.ngm-lib-cta` / `.ngm-lib-term` selector
groups rather than redefining them.

**Tradeoff accepted:** the Custom-HTML version had a second "PDF · approved
7 October" meta line per row. The editor can't produce that without the
secretary typing markup, so it's gone. The date, icon and chip carry the
row.

**Verified by rendering,** not by reading the CSS — a simulated content
gadget (headings + bare `<ul><li><a>`, no classes) rendered in Chromium at
1200px and 390px: rows style correctly, unlinked bullets become "Not posted"
rows, hover fill spans the whole row, list stays left-aligned on a phone,
no horizontal overflow.

⚠ Re-verify the gadget's own wrapper classes against the live DOM once it
exists, per the repo-root `CLAUDE.md`. `.gadgetStyleBody` is assumed from
the events gadget; if the content gadget wraps differently, that one rule
needs adjusting. Everything else keys off `ngm-wa-minutes` and plain tags,
so it holds regardless. Snippet to dump it:

```js
(function () {
  var g = document.querySelector(".ngm-wa-minutes");
  if (!g) return console.log("gadget not found — is the CSS class set?");
  console.log("gadget classes:", g.className);
  console.log("children:", [...g.children].map(function (c) {
    return c.tagName + "." + (c.className || "(none)");
  }).join("  |  "));
  console.log("headings:", [...g.querySelectorAll("h1,h2,h3,h4")].map(function (h) {
    return h.tagName + ":" + h.textContent.trim();
  }).join("  "));
  var li = g.querySelector("li");
  console.log("first row:", li && li.outerHTML.slice(0, 200));
})();
```

## Sections

1. **Hero** (`01-top`) — cream band, "Members only" eyebrow, one line.
2. **Minutes by meeting** heading (`01-top`), then the list (gadget).
3. **About these minutes** (`03-bottom`, linen) — four tiles: drafts can
   change, older minutes are in the library cabinets, how to report an
   error, and a note that the files are for members.
4. **Closing CTA** (`03-bottom`, rose) — email the secretary, back to the
   Member Hub.

## The meeting pattern (from the old page)

Monthly, second Monday in most months, January through November. **No
December meeting** in either year. Useful for spotting a gap.

- **2025** — 13 Jan, 10 Feb, 17 Mar, 14 Apr, 12 May, 9 Jun, 14 Jul, 11 Aug,
  8 Sep, 13 Oct, 11 Nov *(no file)*
- **2024** — 8 Jan, 12 Feb, 11 Mar, 8 Apr, 13 May, 10 Jun, 8 Jul, 12 Aug,
  9 Sep, 14 Oct, 18 Nov

## Confirm before go-live

- **The members-only restriction** (see the warning above).
- **The "Draft" idea.** The first "About these minutes" tile says a set can
  be posted before the board approves it. If the Guild only ever posts
  approved minutes, drop that tile. The old page had no such concept.
- **`secretary@needleworkguildmn.org`** is right for corrections (currently
  Karen Hesse, per the Member Hub roster).
- **Whether older minutes are in the library cabinets.** The "Older minutes"
  tile says so, based on the Lending Library page's note about archived
  materials. Worth a check with a librarian.
- **Pre-2024 minutes** — the old page only goes back to 2024.

## Related

Kym asked for a Member Hub documents timeline covering job descriptions,
newsletters and minutes. This covers minutes only. The gadget styling is
generic — any content gadget given the `ngm-wa-minutes` class gets the same
document list, so a newsletter archive needs no new CSS. The WA Site pages
list already shows a "Newsletter Archive" page to work from.
