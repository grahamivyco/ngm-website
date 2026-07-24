# NGM Design System — session primer

Paste this at the top of a new AI session before working on the NGM site. It is
the synthesized record of how this site is designed, coded, written, and shipped
— derived from the repo's own history so a fresh agent inherits the house style.

---

## 1. Visual language

The look is **warm, editorial, calm** — a needlework guild, not a SaaS app.
Think linen, sage, and terracotta; generous serif display type; nothing loud.

**Palette** (all exposed as `--ngm-` tokens; never hard-code hex in page markup):

| Role | Token | Hex |
| --- | --- | --- |
| Sage (primary) | `--ngm-sage` | `#5C7A52` |
| Sage dark (text/buttons) | `--ngm-sage-dk` | `#3E5538` |
| Sage light (tint fills) | `--ngm-sage-lt` | `#EEF3EC` |
| Terracotta rose (accent) | `--ngm-rose` | `#B87260` |
| Rose light / dark | `--ngm-rose-lt` / `--ngm-rose-dk` | `#F5EBE7` / `#9A5C4A` |
| Cream (page bg) | `--ngm-cream` | `#FAF7F2` |
| Linen (section bg) | `--ngm-linen` | `#F0EAE0` |
| Charcoal (body text) | `--ngm-charcoal` | `#242424` |
| Gray / gray-lt | `--ngm-gray` / `--ngm-gray-lt` | `#656565` / `#9A9A9A` |
| Border | `--ngm-border` | `#DDD5C8` |

Rose is an **accent only** — use it sparingly (italic word in a heading, one CTA,
a small chip). Sage carries the brand; cream/linen/white alternate as section
backgrounds (`.ngm-sec-cream`, `.ngm-sec-linen`, `.ngm-sec-white`).

**Type:** Cormorant Garamond (serif, display — `--ngm-serif`) + DM Sans (sans,
body/UI — `--ngm-sans`). Headings are serif, weight 400, `text-transform: none`,
sized with `clamp()` for fluid scaling. Body is DM Sans with generous
`line-height` (~1.8 on lead paragraphs).

**Signature move — the italic `em` accent in headings:** one word is wrapped in
`<em>` so it renders in *italic rose*, same size/weight/line-height as the rest of
the heading, differing only by color + italic. e.g.
`<h1 class="ngm-h1">A place for people who love to <em>stitch</em></h1>`.
This is the single most recognizable NGM flourish — reach for it on hero and
section headings.

**Shape & depth:** soft rounded corners (`--ngm-radius` 14px, `--ngm-radius-lg`
20px), pill buttons (`border-radius: 100px`), and layered soft shadows
(`--ngm-sh` / `--ngm-shm` / `--ngm-shx`) rather than hard borders. Hovers are
gentle: a 1px lift (`translateY(-1px)`) and a soft shadow, transitions ~.18–.2s.

## 2. Component & layout vocabulary

Recurring building blocks — reuse these names and patterns rather than inventing
new ones:

- **Eyebrow** (`.ngm-eyebrow`) — small uppercase letter-spaced sage kicker above a
  heading. Nearly every section opens with one.
- **Tiles** — the dominant content unit. Meeting-group tiles, member-perk tiles,
  event tiles, a Zoom "Join the meeting" tile. Compact, rounded, tinted.
- **CTAs** — pill buttons (`.ngm-btn` + `-green`/`-rose`/`-outline`/`-white`) and
  **arrow links** (`.ngm-arrow-link`, a text link with a nudging arrow).
- **Hero** — two-column copy + photo, with a **brand-mark loader** placeholder
  (the MN-outline-and-needle mark, borderless, pulsing) shown until the photo
  loads.
- **Stats marquee** — the scrolling "200+ members · 50+ years" bar, with a
  visually-hidden static copy for screen readers.
- **Bento gallery** (`.ngm-bento`) — responsive masonry photo grid (reflows
  4→3→2 cols) with `-big`/`-wide`/`-tall`/plain size modifiers.
- **Sections** (`.ngm-sec`, `.ngm-con`) — padded band + centered ≤1080px
  container.

## 3. CSS conventions

- **One stylesheet, one source of truth:** `global-css/global.css`, served live
  via jsDelivr. All styling lives here. Structure: shared design system
  (tokens → reset → type → layout → buttons → badges, sections 1–20) first, then
  per-page skins, then native WA gadget skins.
- **Namespacing:** every class is `.ngm-…`, every custom property is `--ngm-…`,
  and page styles are scoped under a `.ngm` wrapper so they never leak into
  Wild Apricot's own chrome.
- **Comment the *why*, ornately.** The CSS uses boxed section banners
  (`══════`) and numbered headers, and — crucially — long comments that explain
  the *reason* a rule exists, especially WA-fighting hacks. When you add a
  workaround, document what broke and why the fix works (see the button
  font-specificity note and the "KILL WA WRAPPER GAPS" sections for the tone).
- **Beating Wild Apricot's specificity** is a running theme: WA's theme targets
  anchors with high-specificity `body a:not(...)` rules, so NGM mirrors that
  specificity (`body a.ngm-btn { … !important }`) rather than escalating blindly.
  Match the platform's specificity; reserve `!important` for exactly the
  properties WA is overriding.
- **Tokens over literals:** reference `var(--ngm-…)`; don't paste raw hex into
  new rules.

## 4. Markup conventions

- **Markup-only page files.** Each page is one (or a `01-top` + `03-bottom`)
  `.html` file of pure markup — **no embedded `<style>` block**, no
  self-contained duplicate. Styling comes from `global.css`. (See CLAUDE.md.)
- **Semantic, accessible HTML.** Real `<section>`/`<h1>`/`<h2>`, `aria-hidden`
  on decorative elements, `role`/`aria-label` on inline SVGs, visually-hidden
  text mirroring animated/scrolling content, and a `prefers-reduced-motion`
  block that stills every animation. Accessibility is not an afterthought here.
- **Resilient images.** Photos are referenced by full WA file-manager URL, with
  `loading` hints, an `onload="this.classList.add('is-loaded')"` reveal, and an
  `onerror` fallback to a known-good gallery photo. New photo slots use
  `REPLACE_WITH_…` placeholders that already fall back gracefully.
- Alt text is descriptive and human ("Guild members stitching together at a
  monthly meeting"), not keyword filler.

## 5. Editorial / content instincts

The clearest through-line in the history is **restraint**: the site is
continuously *tightened*. Commits repeatedly "trim," "compact," "de-dup,"
"shorten copy," "drop the FAQ/Reach-out section," "less whitespace," "one
roster." When in doubt, **cut and consolidate** rather than add. Prefer one
well-made module over two overlapping ones.

Copy voice is **warm and welcoming, plain-spoken, community-first** ("a warm,
welcoming community of stitchers who learn from and look out for each other").
Short sentences, an em-dash aside, no marketing bluster.

Design decisions **propagate site-wide**: a pattern proven on the homepage
(eyebrows, CTAs, mobile alignment, tile styling) is then rolled out to every
page for consistency ("Propagate homepage mobile alignment site-wide"). Pages
borrow from each other on purpose — Events adopts home/about styling, Meetings
adopts home/about patterns.

## 6. Working rhythm

- **Iterate in explicit rounds.** Work ships as versioned passes — "Calendar
  round 2 / round 3," "Homepage v8/v9" — each a focused polish pass, not a
  rewrite. Small, reversible, well-labeled steps.
- **Commit messages: terse, scoped, specific.** Format is `Area: what changed
  (+ why if not obvious)`, e.g. `Calendar: simplify horizontal week-line rule
  (robust selector), drop doubled header border`. Lead with the page/area,
  list the concrete changes, keep it one line. PR numbers trail in `(#nn)`.
- **Document alongside the code.** Each page has a `README.md` noting its WA
  page name, gadget structure, section list, quirks, and an "Open TODO." Voice
  is bold inline labels + `·` / `—` separators. Keep these current when markup
  changes.
- **Respect the platform.** This site lives inside Wild Apricot; solutions work
  *with* WA's constraints (Custom-HTML gadgets, jsDelivr-served CSS, native
  gadget skins) rather than fighting the platform wholesale.

## 7. The short version

Warm editorial sage/cream/rose palette · Cormorant + DM Sans · italic-rose `em`
accent in headings · soft rounded pills and shadows · everything `.ngm-`
namespaced and tokenized · one `global.css`, markup-only pages · accessible and
reduced-motion-aware by default · copy and layout kept lean and continually
tightened · patterns proven once then propagated · ship in small labeled rounds
with terse scoped commits and a living README per page.
