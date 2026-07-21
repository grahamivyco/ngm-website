# Live-loading from GitHub → Wild Apricot

Wild Apricot has **no native GitHub deploy** and its REST API does **not** expose
page HTML or the CSS tab, so there is no true "git push → site updates" pipeline.
This folder sets up the closest practical thing: instead of pasting full code into
WA, you paste a **tiny loader once**, and it pulls the real code live from this repo
over the [jsDelivr](https://www.jsdelivr.com/) CDN. After that, a `git push` to
`main` updates the live site — no re-pasting.

This covers the three site-wide pieces: **Global CSS**, **header**, and **footer**.

> Requires the repo to be **public** (jsDelivr only serves public repos). This one is.

---

## One-time setup in Wild Apricot

You paste each snippet **once**. Everything in `wa-snippets/` is a copy-paste block.

You paste each of the three blocks **once**, into three places:

| Snippet | Paste into | Replaces |
|---------|-----------|----------|
| `wa-snippets/css-tab.css` | The WA **CSS** tab (this is its whole contents) | pasting `global.css` into the CSS tab |
| `wa-snippets/header-loader.html` | The **top** template Custom HTML gadget (where the header used to live) | the full pasted header |
| `wa-snippets/footer-loader.html` | The **bottom** template Custom HTML gadget (where the footer used to live) | the full pasted footer |

The CSS goes in the **CSS tab** (not a gadget) on purpose: that puts the stylesheet in
`<head>`, so there's no flash of unstyled content. If you ever can't edit the CSS tab,
the same jsDelivr URL also works as a `<link rel="stylesheet">` inside the top gadget.

After that, your day-to-day workflow is just: **edit the file in the repo → commit →
push to `main`.** The live site reflects it within ~1 minute.

---

## What updates automatically after setup

| Repo file | Live effect |
|-----------|-------------|
| `global-css/global.css` | Site-wide styling |
| `layout/header/01-top.html` | Header everywhere |
| `layout/footer/01-top.html` | Footer everywhere |

Individual **page bodies** (`pages/*/`) are **not** covered — those still get pasted
into their WA page gadgets, because many are "sandwiches" with a native WA gadget
(Upcoming Events, Calendar) in the middle that can't be externalized. The big,
most-edited pieces — CSS, header, footer — are the ones automated here.

---

## How freshness / caching works

jsDelivr caches `@main` URLs for up to ~12 hours. To avoid waiting, the GitHub Action
at `.github/workflows/purge-jsdelivr.yml` runs on every push that touches these three
files and calls `https://purge.jsdelivr.net/...` for each — dropping the cached copy so
the next page load fetches the new version. Typical time to live: **~1 minute.**

You can also purge manually by visiting the purge URL in a browser, e.g.:
`https://purge.jsdelivr.net/gh/grahamivyco/ngm-website@main/ngm-website/global-css/global.css`

Or run the workflow by hand from the repo's **Actions** tab ("Purge jsDelivr cache" →
Run workflow).

---

## Pinning / freezing a version

The snippets use `@main` = always the latest commit. To freeze the live site to a
known-good version, replace `@main` in the snippet URL with a git **tag** or **commit
SHA**, e.g. `@v1` or `@a1b2c3d`. Tagged/SHA URLs are cached long-term and never change,
so a bad commit can't reach the live site until you bump the pin.

---

## Rollback

- **Undo the whole approach:** put the full header/footer/CSS back into their WA gadgets
  / CSS tab (the full code always still lives in this repo) and delete the loader
  snippets. Nothing here is destructive or one-way.
- **CSS emergency:** the WA CSS tab still accepts `global-css/current-live-backup.css` —
  paste it back to instantly revert styling.

---

## Trade-offs to know

- **Header/footer load via JS**, so they appear a beat after the page and aren't in the
  initial HTML (minor for SEO on a header/footer; the CSS `<link>` has no such issue).
- **Depends on jsDelivr + a public repo.** If the repo ever goes private, switch to
  Cloudflare Pages or Netlify (both serve from private repos) and change the snippet URLs.
- If jsDelivr is ever unreachable, the loaders fail quietly (logged to console) and the
  page renders without the header/footer — so keep the full code in the repo as the
  fallback, which is exactly how it already is.
