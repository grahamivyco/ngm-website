# Board Minutes

Replaces the existing WA page **"Meeting Minutes"** (`pageId 18146`), which
lists 2025 and 2024 as two plain bulleted columns of links.

**Update that page — don't make a new one.** It already exists and already
holds the list; a second minutes page means two things to keep current.

## Structure: sandwich

```
01-top.html       Custom HTML — hero (with the way back) + intro line
                  + the accordion script
02-wa-gadget.txt  native WA CONTENT gadget(s) — one per block
```

**There is no `03-bottom`.** Nothing sits under the cards; the Back to
the Member Hub button is in the hero.

**Live slug: `/meeting-minutes`** (not `/board-minutes` — the Member Hub
tile points there).

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
5. Nothing goes below the cards — delete any old bottom gadget.
6. All gadgets go in the **same layout row**, row background
   transparent so the linen band runs continuously.
7. The live slug is **`/meeting-minutes`** and the Member Hub tile now
   points there.

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

1. **Hero** (`01-top`) — cream band, "Meeting minutes" eyebrow, the
   title, one line of copy, and the Back to the Member Hub button.
2. **Intro line** (`01-top`) — linen band, opens the list.
3. **The cards** — one white accordion card per content gadget, on linen.

### Two sections were removed (Sep 2026)

- **"About these minutes"** — four tiles covering draft status, older
  minutes being in the library cabinets, how corrections are handled,
  and not forwarding the files. **None of it was sourced.** It was
  written from a guess at how the Guild works; the old page carried no
  such claims. If any of it is true it can come back, once confirmed.
- **"Ask the board"** — a rose CTA band pointing at the secretary.

## The section title is BUILT, not styled

This bit matters. Two earlier attempts styled the editor's own heading
in CSS and both lost — the live page kept rendering it bold sans:

- the old content carries inline font markup (`<font face="Arial">`,
  `<span style="font-family:…">`) that outranks a rule aimed at the
  heading element, and
- on some blocks the heading sits in a **gadget of its own**, where a
  rule scoped to `.ngm-wa-minutes` never reaches it at all.

So the script in `01-top.html` reads the heading's **text**, hides the
original (`.ngm-min-src`), and builds its own `.ngm-min-title` button.
Everything downstream styles classes we control. **Don't go back to
styling the editor's heading.**

When the heading was its own gadget, that gadget is left empty and would
show as a white strip across the linen band, so the script collapses it
too (`.ngm-wa-minutes-src-empty`).

Verified by rendering all three shapes: a real `<h2>`, a
`<p><strong><span style="font-family:Arial">`, and a heading in a
separate gadget. All three come out Cormorant.

## Rows

Mirrors the events gadget, with two changes the maintainer asked for:

- **The hairlines stay straight.** The row carries the line and *no*
  radius; the rounded hover fill is a separate layer underneath
  (`li:has(a)::before`). A radius on the row itself bows the line up at
  both ends, which is what the events gadget does.
- **Hovering a row hides the lines above and below it**
  (`li:hover` and `li:has(+ li:hover)` drop their border colour), so the
  rounded fill sits clean with nothing touching it.

Serif date, charcoal → sage on hover, one line per meeting. Unlinked
bullets are caught with `li:not(:has(a))` and get the muted treatment
plus the "Not posted" chip.

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

## Two bugs found on the live page (Sep 2026)

### Titles reading "Board Meeting Minutes 20250 meetings"

WA renders a content gadget before its rows exist. The script built the
card anyway, so it produced a title button reading "Board Meeting Minutes
2025" + "0 meetings" — and marked the gadget finished, so it never filled
in. Then the *next* gadget's title search walked backwards looking for a
heading, landed on that card, and took its **button text**: title and
count run together.

Two guards:

- `ours()` — the title search never reads from anything this script built
  (`.ngm-min-sec`, `.ngm-min-title`, `.ngm-min-src`).
- Done-ness is tracked **per list, not per gadget**, and a list with no
  rows is skipped entirely so the MutationObserver retries once WA fills
  it.

Both reproduced against the pre-fix script and confirmed fixed, using a
gadget whose list is populated 250ms late — the pre-fix run returns
`"Board Meeting Minutes 2025Board Meeting Minutes 20250 meetings"`.

### The band stopped short of the footer

On a tall viewport with few cards the page ran out and the theme's own
background showed below the linen. The script now flags
`body.ngm-min-page` and the CSS paints WA's content wrappers linen —
the same approach the member directory uses for its cream page
(`body.ngm-dir-page`). The hero's cream band still paints over the top.

⚠ That rule names WA's wrappers (`.mLayout`, `#idPageShadingContainer`,
`.zonePlace.zoneContent`, `.WaPlaceHolderContent`), copied from the
directory page. If a gap remains on the live page, one of those is
wrong for this template — inspect and add the real one.

## No accordion (Sep 2026)

Sections were briefly collapsible. That put an extra click between a
member and the thing they came for, and the lists are short, so the
collapsing is gone entirely — no button, no chevron, no toggle. The
title is a plain `<h2>` the script builds; every list is always visible.

The document icon came off the title at the same time. The rows each
carry one, where it does real work marking a PDF link; two of them read
as clutter. Flipping that round — icon on the title, bare dates in the
rows — is a small change if it ever reads better that way.

## The generated classes need the gadget treatment too

The script injects its heading INSIDE a native WA gadget, so WA's theme
rules for headings apply to it. A plain `.ngm-min-title` (0,1,0) lost to
them and the year came through in the theme's own bold sans — "sometimes",
because it depends which theme rules match.

`.ngm-min-title`, `-txt`, `-count`, `-none` and `-kind` are therefore
`body`-prefixed with `!important` on every font property, exactly as the
repo-root `CLAUDE.md` requires for anything targeting a native gadget. It
was missed because the ELEMENT is ours even though the gadget around it
is not — worth remembering for anything else this script builds.

Verified against a simulated theme that sets Arial/Verdana, weight 700 and
uppercase on gadget headings and spans. Pre-fix it rendered
`Verdana 20px w700 uppercase`; now `Cormorant Garamond 24px w400 none`.
