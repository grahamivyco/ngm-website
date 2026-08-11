# NGM Design System — canonical reference

The operative design system lives in **`global-css/global.css`** (its `:root`
tokens and existing component idioms). This file is the human/AI-readable
summary. When they disagree, global.css wins — update this file to match.

**Conformance is machine-checked:** run `python3 ngm-website/tools/design-check.py`
after any page or CSS change. It must exit clean.

## Tokens (defined once in `:root` of global.css)

**Colors** — always via tokens, never raw hex in new rules:
`--ngm-sage #5C7A52` · `--ngm-sage-dk #3E5538` · `--ngm-sage-lt #EEF3EC` ·
`--ngm-rose #B87260` · `--ngm-rose-dk #9A5C4A` · `--ngm-rose-lt #F5EBE7` ·
`--ngm-cream #FAF7F2` · `--ngm-linen #F0EAE0` · `--ngm-linen-dk #E5DDD0` ·
`--ngm-charcoal #242424` · `--ngm-gray #656565` · `--ngm-gray-lt #9A9A9A` ·
`--ngm-border #DDD5C8`

**Fonts** — exactly two families, always via tokens:
`--ngm-serif` (Cormorant Garamond — display/titles, weight 400) and
`--ngm-sans` (DM Sans — everything else).

**Type roles** — every `font-size` resolves to ONE of these tokens
(plus the `--ngm-h1`/`--ngm-h1-sub`/`--ngm-h2` clamps and a short
the $30 price-figure lockup, the only remaining literal):

| Token | Size | Role |
|---|---|---|
| `--ngm-title-card` | 1.5rem | large card/serif titles |
| `--ngm-title-md` | 1.3rem | medium card & system titles |
| `--ngm-title-lg` | 1.7rem | extra-large serif titles, stat numerals |
| `--ngm-text-base` | 1rem | base-size UI text |
| `--ngm-h1-mobile` / `--ngm-h2-mobile` | 2.75 / 2.2rem | heading sizes at mobile widths |
| `--ngm-title-tile` | 1.22rem | small tile titles, person names |
| `--ngm-text-lead` | 1.0625rem | section leads, intros, Visit & CTA copy — equals body: ONE copy size |
| `--ngm-text-body` | 1.0625rem | standard body copy, notes |
| `--ngm-text-md` | .95rem | secondary copy, form text |
| `--ngm-copy` | .95rem | card/tile descriptions — ONE size, one step below body copy |
| `--ngm-btn-size` | .9rem | buttons, pills, controls |
| `--ngm-text-ui` | .85rem | small UI text, quiet links |
| `--ngm-text-meta` | .82rem | meta lines, dates, hints |
| `--ngm-eyebrow-size` | .78rem | eyebrows, mini-labels |
| `--ngm-tag-size` | .65rem | tags, badges, chips |

**Layout/shape** — `--ngm-radius 14px`, `--ngm-radius-lg 20px`, shadows
`--ngm-sh/-shm/-shx`, section padding `--ngm-pad-x*`, grid gap `--ngm-gap`,
tile/card padding `--ngm-tile-pad`/`--ngm-card-pad`, icon squares
`--ngm-icon-box`/`--ngm-icon-box-sm`.

## Component idioms — reuse, don't reinvent

- **Headings:** serif, weight 400, sentence case, with an italic `<em>`
  accent (same size/weight, differs only by italic + color).
- **Eyebrows:** `.ngm-eyebrow` — sans, uppercase, `--ngm-eyebrow-size`,
  letter-spaced, sage-dk.
- **Buttons:** `.ngm-btn` + variant (`-green`, `-outline`, `-rose`,
  `-outline-rose`, `-white`, `-fit`, `-sm`) — pill radius 100px,
  `--ngm-btn-size`, weight 500.
- **Inline text links:** `.ngm-inline-link` idiom — sage-dk, weight 500,
  `font-size: inherit`, border-bottom underline `rgba(62,85,56,.35)`
  darkening on hover. Never `text-decoration: underline` for new links.
  A catch-all (`body .ngm p/li a:not([class])`) applies the same idiom to
  any classless link in branded copy — but still add the class explicitly.
- **Checks:** the About-page mask check (`.ngm-feat li::before` idiom) —
  bare 15px sage check, no circle/box.
- **Tiles/cards:** cream tile on white bands, white tile on cream/linen
  bands; 1px `--ngm-border`, `--ngm-radius`, icon in a `--ngm-sage-lt`
  rounded square, serif `--ngm-title-tile` title, `--ngm-copy` description.
  (See `.ngm-hub-rtile`, `.ngm-vol-card`, `.ngm-lib-term`.)
- **Tile pairs (primary/secondary):** when two action tiles sit together
  (Member Hub + Request the Link), the primary keeps the filled light-sage
  `.ngm-hub-zoom-module` card and the secondary adds
  `.ngm-hub-zoom-module-alt` — white card, `--ngm-border`, `--ngm-sage-lt`
  icon chip. The tile version of filled vs outline buttons.
- **Hero bands:** cream, centred, 72/48/56 padding, border-bottom
  (`.ngm-cal-hero`, `.ngm-vol-hero`).
- **Closing CTA bands:** rose-lt, centred, `--ngm-text-lead` copy, pill
  buttons (`.ngm-si-cta`, `.ngm-about-cta`, `.ngm-vol-cta`).
- **Breakpoints:** 980 (nav/hamburger), 900 (grids collapse — layout
  only, still left-aligned), 640 (phone centring of copy/tiles/CTAs),
  560 (phone sizing).

## Hard rules (checked by tools/design-check.py)

1. Markup in `pages/**` / `system-pages/**` `.html`; ALL styling in
   `global-css/global.css`. No embedded `<style>`, no inline `font-size`.
2. Every `ngm-*` class used in markup must have rules in global.css —
   never invent a class and leave it unstyled.
3. `font-size` only via type-role tokens; `font-family` only via
   `--ngm-sans`/`--ngm-serif`.
4. Rules targeting native WA gadgets/anchors need `body`-prefixed
   selectors with `!important` on font properties (WA's theme bolds and
   re-fonts anchors otherwise), verified against the live DOM via the
   browser console — stable classes only, never per-instance `id_*` ids
   (see `docs/wa-notes.md` and the repo-root CLAUDE.md).
