# Needlework Guild of Minnesota — Website Source

Canonical source of truth for the custom frontend layered on the NGM Wild Apricot (WA) site.

> **Important:** Wild Apricot does **not** deploy from GitHub. This repo is the master
> copy, backup, and change history for the code. To publish a change you still paste
> the code into the matching WA gadget or CSS tab. This repo is where the *correct*
> version always lives.
>
> **Live-loading (optional):** the site-wide **CSS, header, and footer** can be wired to
> load straight from this repo via a CDN, so editing them here updates the live site with
> no re-pasting. One-time WA setup + details in [`deploy/`](deploy/README.md).

## How this repo is organized

```
ngm-website/
├── design-system/       Reference: colors, type, CSS conventions (paste at top of new AI sessions)
├── global-css/          Content of the WA "Global CSS" tab (site-wide overrides + system-page skins)
├── layout/
│   ├── header/          Nav header gadget
│   ├── footer/          Footer gadget
│   └── wrapper-reset/   WA Wrapper Reset gadget
├── pages/               One folder per public page (each = the Custom HTML gadget code)
│   ├── homepage/
│   ├── about/
│   ├── events-home/
│   ├── meetings/
│   ├── calendar/
│   ├── join/
│   ├── stitch-in/
│   └── member-hub/
├── system-pages/        WA system pages (CSS-only or Theme-Override skins)
│   ├── login/
│   ├── membership-application/
│   ├── renewal/
│   ├── member-profile/
│   └── contact-profile/
└── docs/                WA-specific notes, gotchas, and conventions
```

## What goes in each page folder

Each page is often assembled from **multiple gadgets in a specific paste order**
(Custom HTML -> native WA gadget -> Custom HTML — the "sandwich" pattern). So each
folder holds the gadget files in order plus a short `README.md` recording:

- The WA **page ID** / URL
- The **paste order** of gadgets
- Any native WA gadget IDs the code depends on

File-naming convention inside a page folder:

```
01-top.html          first Custom HTML block
02-wa-gadget.txt     note describing the native WA gadget that sits between
03-bottom.html       second Custom HTML block
styles.css           page-specific CSS (if any lives outside Global CSS)
README.md            paste order, page ID, notes
```

## Publishing workflow (repo -> live site)

1. Edit the file(s) here and commit (so history is preserved).
2. Open the matching page/gadget in WA admin.
3. Paste the updated block(s) in the documented order.
4. Publish in WA and spot-check the live page.

## Editing on GitHub without git

Non-technical volunteers can edit any file directly in the browser: open the file
on github.com, click the pencil, make the change, and "Commit changes." No command
line needed.
