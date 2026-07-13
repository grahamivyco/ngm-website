# Global CSS

This folder holds the site-wide CSS for the WA **Global CSS** tab. There are two files
with very different jobs:

## `global.css` — the MASTER redesign stylesheet
The consolidated sage/cream NGM redesign, all in one place. The shared design system
(tokens, reset, typography, layout, buttons, arrow links, badges) appears **once** at
the top, followed by each page's own styles and the native WA gadget skins
(login/account, calendar). Fonts are `@import`ed at the top.

- **This is the redesign — not yet live.** Do **not** paste it into the WA Global CSS
  tab until the full-site cutover (see the project's staged-rollout plan). A half-applied
  redesign looks broken to members.
- At cutover, each page gadget's own `<style>` block can be deleted, because its styles
  live here now. (The header/footer gadgets keep their inline CSS — they carry HTML+JS.)
- Rebuilt from the page files by `scratchpad/build_master.py`; if you change a page's
  `<style>`, re-run it (or edit `global.css` directly) so this stays the source of truth.

## `current-live-backup.css` — the RESTORE file
An exact snapshot of what is in the live WA Global CSS tab **right now** (the version
members are used to — it still has purple relics from a scrapped mid-update alongside the
sage calendar styles).

- **Use it to revert.** If you paste something experimental into the live Global CSS tab
  and want to undo it, replace the tab's contents with this file and save.
- If you ever change the live Global CSS, update this file to match.
