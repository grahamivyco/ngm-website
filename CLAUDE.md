# Working conventions for this repo

This repo holds the source for the Needlework Guild of Minnesota's Wild Apricot
(WA) website. Read this before editing.

## Single source of truth: page HTML + global.css

- **Styling lives in `ngm-website/global-css/global.css`.** The live site loads
  this one file (served via jsDelivr:
  `https://cdn.jsdelivr.net/gh/grahamivyco/ngm-website@main/ngm-website/global-css/global.css`).
  To change how anything looks, edit `global.css`.
- **Page markup lives in the `*.html` files** under `ngm-website/pages/<page>/`
  (and `ngm-website/system-pages/<page>/`) — e.g. `01-top.html`,
  `03-bottom.html`. These are the canonical page files: the ones to edit and to
  paste into the WA Custom-HTML gadgets. They carry **no embedded `<style>`
  block** — all styling comes from `global.css`.

## One copy only — no self-contained duplicates

There used to be two copies of every page (a self-contained `01-top.html` with
an embedded `<style>` block, plus a `01-top.slim.html` markup-only twin).
Keeping them in sync was error-prone, so the self-contained copies were removed
and the markup-only files were renamed to plain `01-top.html` / `03-bottom.html`.

- **Do not add an embedded `<style>` block to a page file**, and do not create a
  second "self-contained" copy of a page. One `.html` file per gadget, markup
  only.
- When a change needs new CSS, put it in `global-css/global.css`.

## Exceptions (leave as-is unless asked)

A few files are legitimately self-contained (their own CSS/fonts) because they
have no global-CSS equivalent — do not "slim" or delete them unless explicitly
asked:

- `ngm-website/layout/header/`, `layout/footer/`, `layout/wrapper-reset/`
- A handful of `system-pages/` (e.g. `contact-profile`, `member-profile`,
  `renewal`, and the `mockups/`).

## Images

Photos are hosted on the WA file manager and referenced by full URL, e.g.
`https://needleworkguildmn.org/resources/Pictures/Website%20Update%20Photos/<file>`.
Reference images by URL; don't commit large binaries to the repo.

## Design & style preferences (how to match the house style)

Full reference: `ngm-website/design-system/NGM-design-system-prompt.md`. The
short version of what the maintainer consistently wants:

- **Aesthetic:** warm and editorial — sage `--ngm-sage-dk`/cream/linen with
  terracotta `--ngm-rose` as a *sparing* accent. Cormorant Garamond (serif
  display) + DM Sans (body). Soft rounded corners, pill buttons, gentle layered
  shadows and small hover lifts — never loud or high-contrast.
- **Signature flourish:** italicize one word in a heading with `<em>` so it
  renders italic-rose (same size/weight) — e.g. `love to <em>stitch</em>`.
- **Tokens & namespacing:** every class is `.ngm-…`, every custom property is
  `--ngm-…`, page styles scoped under `.ngm`. Use `var(--ngm-…)` — don't
  hard-code hex in new rules.
- **Reuse the vocabulary:** eyebrows, tiles, pill CTAs + arrow links, hero with
  brand-mark loader, bento gallery, `.ngm-sec`/`.ngm-con`. Prove a pattern on
  one page, then propagate it site-wide rather than inventing per-page variants.
- **Accessibility by default:** semantic sections/headings, `aria-hidden` on
  decorative bits, visually-hidden copies of animated content, a
  `prefers-reduced-motion` block, and `onload`/`onerror` image fallbacks.
- **Editorial instinct is restraint:** tighten, trim, de-dup, consolidate. When
  unsure, cut rather than add. Copy is warm, plain-spoken, community-first.
- **Comment the *why*,** especially Wild-Apricot workarounds — mirror WA's
  specificity (`body a.ngm-btn { … !important }`) instead of escalating blindly.
- **Ship in small labeled rounds** with terse scoped commits
  (`Area: what changed (+ why)`), and keep each page's `README.md` current.

## Summary

Edit the page `*.html` files for markup and `global-css/global.css` for
styling. That's it — there is no second copy to keep in sync.
