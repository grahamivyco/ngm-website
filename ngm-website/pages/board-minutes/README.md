# Board Minutes

Replaces the existing WA page **"Meeting Minutes"** (`pageId 18146`), which
lists 2025 and 2024 as two plain bulleted columns of links.

**Update that page — don't make a new one.** It already exists, it's already
linked from wherever people reach it today, and a second minutes page means
two things to keep current.

## ⚠ Check the restriction first

In the WA **Site pages** list, "Meeting Minutes" sits under *Pages not in
menu* and shows **no padlock**. Member Hub shows one. If that's accurate, the
board minutes are reachable by anyone with the URL right now.

This page says the files are for current members. Before pasting it, either
restrict the page to members or take that line out. Don't ship the claim
without the restriction.

"Not in menu" is not access control. It only hides the page from navigation.

## ⚠ Nothing has been posted since November 2025

The list ends at 11 November 2025, and 11 November 2025 has no link. It is
now September 2026, so roughly ten months of minutes are missing — nine or
ten meetings, on the monthly pattern below. Worth raising with the secretary
before this goes live; the page will show a "Nothing posted for 2026 yet"
block until they arrive.

## Getting the real links

The dates are already in `01-top.html`. The **PDF URLs are not** — they exist
only as hrefs on the old page, and every row currently reads
`MINUTES_URL_NEEDED` (deliberately not a URL, so an early paste fails loudly
rather than looking fine and going nowhere).

Don't re-type 21 URLs. Open the old page, open the browser console
(F12 → Console), paste this, and copy what it prints:

```js
(function () {
  var out = [], year = "";
  var ICON = '<svg class="ngm-min-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6"/><path d="M9 17h4"/></svg>';
  var ARROW = '<svg class="ngm-min-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>';
  var MONTHS = "January February March April May June July August September October November December".split(" ");
  function parse(t) {                                   // -> {label, sort} or null
    var m = /([A-Z][a-z]+)\s+(\d{1,2}),?\s+(\d{4})/.exec(t);
    if (!m) return null;
    var mi = MONTHS.indexOf(m[1]);
    if (mi < 0) return null;
    return { label: (+m[2]) + " " + m[1] + " " + m[3],
             sort: +m[3] * 10000 + (mi + 1) * 100 + (+m[2]) };
  }
  document.querySelectorAll("h1,h2,h3,h4,li").forEach(function (el) {
    if (/^H[1-4]$/.test(el.tagName)) {
      var y = /(20\d\d)/.exec(el.textContent); if (y) year = y[1];
      return;
    }
    if (el.querySelector("li")) return;                 // skip nested wrappers
    var txt = el.textContent.replace(/\s+/g, " ").trim();
    if (!/(20\d\d)/.test(txt)) return;                  // not a dated row
    var d = parse(txt);
    if (!d) return;                                     // not a dated row
    var a = el.querySelector("a[href]");
    out.push({ year: year || String(txt.match(/(20\d\d)/)[1]),
               date: d.label, sort: d.sort, href: a ? a.href : null });
  });
  var years = {};
  out.forEach(function (r) { (years[r.year] = years[r.year] || []).push(r); });
  var html = Object.keys(years).sort().reverse().map(function (y) {
    // newest meeting first — the old page lists them oldest first
    years[y].sort(function (a, b) { return b.sort - a.sort; });
    var rows = years[y].map(function (r) {
      if (!r.href) return '      <li class="ngm-min-row">\n' +
        '        <span class="ngm-min-link ngm-min-link-none">\n          ' + ICON + '\n' +
        '          <span class="ngm-min-main">\n' +
        '            <span class="ngm-min-date">' + r.date + '<span class="ngm-min-tag">Not posted</span></span>\n' +
        '            <span class="ngm-min-meta">The board met. The minutes aren&rsquo;t up yet.</span>\n' +
        '          </span>\n        </span>\n      </li>';
      return '      <li class="ngm-min-row">\n' +
        '        <a class="ngm-min-link" href="' + r.href + '" target="_blank" rel="noopener">\n          ' + ICON + '\n' +
        '          <span class="ngm-min-main">\n' +
        '            <span class="ngm-min-date">' + r.date + '</span>\n' +
        '            <span class="ngm-min-meta">PDF</span>\n' +
        '          </span>\n          ' + ARROW + '\n        </a>\n      </li>';
    }).join("\n");
    return '    <h3 class="ngm-min-year">' + y + '</h3>\n    <ul class="ngm-min-list" role="list">\n' + rows + '\n    </ul>';
  }).join("\n\n");
  console.log(html);
  return html;
})();
```

It prints finished `<h3>` + `<ul>` blocks, hrefs and all. Paste them over the
placeholder blocks in `01-top.html`, rebuild `dist/`, and the page is done.

Sanity-check the output before trusting it: 22 rows, 21 of them links, and
11 November 2025 as the one "Not posted" row.

## How people add minutes from here

This matters more than it looks — it's a monthly job for the secretary, not
a developer task. Three routes, worst to best:

### 1. As built: edit the HTML (works now, heavy)

Edit `01-top.html` here, run `python3 ngm-website/tools/build-dist.py`, paste
`dist/pages/board-minutes/01-top.html` into the gadget. Duplicate the nearest
`<li class="ngm-min-row">`, move it to the top of its year, set the href, the
date and the meta line.

Fine for whoever maintains this repo. Too much to ask of a volunteer
secretary every month, and the likely outcome is route 2 by accident.

### 2. Edit the gadget directly in WA (what will actually happen)

Someone opens the Custom HTML gadget in WA and edits the markup there. It
works, and **the repo silently goes stale** — the next person to paste from
`dist/` wipes out every row added that way.

If this route gets used, mirror the change back into `01-top.html` the same
day. Treat a drifted gadget as a bug.

### 3. Sandwich it, so the list is a normal WA content gadget (recommended)

Split the page the way the rest of this repo already does
(`docs/wa-notes.md`, "Gadget architecture"):

```
01-top.html      Custom HTML — hero + "Minutes by meeting" heading
02-wa-gadget     native WA content gadget — JUST the list of dates + links
03-bottom.html   Custom HTML — "About these minutes" tiles + CTA
```

The secretary then adds a meeting the way they add anything else in WA:
open the editor, type the date, insert the link to the PDF. No HTML, no
repo, no paste step, nothing to keep in sync. The chrome stays here.

**What it needs first:** `global.css` rules that style the content gadget's
own `<ul>/<li>/<a>` output to match `.ngm-min-*`. Per the repo-root
`CLAUDE.md`, those selectors must be written against the **verified** DOM,
not guessed. Run this on the page once the gadget exists and paste the
output back:

```js
(function () {
  var g = document.querySelector('[class*="WaGadgetContent"], [class*="WaGadgetCustomHTML"]');
  var lists = document.querySelectorAll("ul, ol");
  console.log("gadget:", g && g.className);
  lists.forEach(function (ul, i) {
    console.log(i, ul.className || "(no class)", "| parent:", ul.parentElement.className,
                "| items:", ul.children.length, "| first:", ul.textContent.trim().slice(0, 40));
  });
})();
```

Route 3 is the one to aim for. Routes 1 and 2 both end with the repo and the
live page disagreeing.

## Wild Apricot setup

1. Open the existing **Meeting Minutes** page (`pageId 18146`).
2. **Restrict it to members** (see the warning above).
3. Paste `dist/pages/board-minutes/01-top.html` into a Custom HTML gadget,
   replacing the old bulleted-column content. `global.css` must already be
   live in the CSS tab.
4. Consider giving it a friendly URL (`/board-minutes`) and adding it to the
   Member Hub tile — the tile in `pages/member-hub/01-top.html` already
   points at `/board-minutes`, so either set that slug or change the tile.

## Sections

1. **Hero** — cream band, "Members only" eyebrow, one line of copy.
2. **Minutes by meeting** (white) — year headings and the document rows.
   Each row is one wide link: file icon, date (+ optional chip), a meta
   line, and an arrow that appears on hover/focus. A meeting with no file
   uses `.ngm-min-link-none` — a `<span>`, not an `<a>`, so there is
   nothing to click.
3. **About these minutes** (linen) — four tiles: drafts can change, older
   minutes are in the library cabinets, how to report an error, and a note
   that the files are for members.
4. **Closing CTA** (rose) — email the secretary, back to the Member Hub.

## The meeting pattern (from the old page)

Monthly, second Monday in most months, January through November. **No
December meeting** in either year. Useful for spotting a gap.

- **2025** — 13 Jan, 10 Feb, 17 Mar, 14 Apr, 12 May, 9 Jun, 14 Jul, 11 Aug,
  8 Sep, 13 Oct, 11 Nov *(no file)*
- **2024** — 8 Jan, 12 Feb, 11 Mar, 8 Apr, 13 May, 10 Jun, 8 Jul, 12 Aug,
  9 Sep, 14 Oct, 18 Nov

## Styling

`global.css`, section "BOARD MINUTES". The hero, CTA band and tiles ride the
existing shared rules (`.ngm-lib-hero` / `.ngm-lib-cta` / `.ngm-lib-term`
groups) rather than redefining them — `.ngm-min-*` was added to those
selector lists. The only new component is the document list
(`.ngm-min-year`, `.ngm-min-list`, `.ngm-min-link` and friends). The list is
exempted from the site-wide 640px phone-centring rule, because a centred
file list stops lining up row to row.

Rendered and checked locally at 1200px and 430px: no horizontal overflow,
77px row hit targets, hover fill and focus ring both working.

## Confirm before go-live

- **The members-only restriction** (see the warning at the top).
- **The "Draft" idea.** The page assumes minutes can be posted before the
  board approves them. If the Guild only ever posts approved minutes, drop
  the Draft chip from the docs and the first "About these minutes" tile.
  The old page had no such concept.
- **`secretary@needleworkguildmn.org`** is right for corrections (currently
  Karen Hesse, per the Member Hub roster).
- **Whether older minutes are in the library cabinets.** The "Older minutes"
  tile says so, based on the Lending Library page's note about archived
  materials. Worth a check with a librarian.
- **Pre-2024 minutes** — the old page only goes back to 2024. If earlier
  years exist somewhere, they can be added as more year blocks.

## Related

Kym asked for a Member Hub documents timeline covering job descriptions,
newsletters and minutes. This covers minutes only. The document list is
generic, so a newsletter archive can reuse `.ngm-min-*` as-is — and the WA
Site pages list already shows a "Newsletter Archive" page to work from.
