# Global CSS

This folder holds the site-wide CSS for the WA **CSS** tab.

## The files

### `global.css` — the redesign stylesheet (paste this into Wild Apricot)
The consolidated sage/cream NGM redesign, in one commented file: design tokens,
reset, typography, layout, buttons, badges once at the top, then each page's styles
and the native WA gadget skins (login/account, calendar, member profile + tabs).

To publish: open it on GitHub → **Copy raw file** → paste into WA's CSS tab → Save.
It's the human-readable master too, so make CSS edits here directly.

> **Paste the whole file.** When updating the live CSS, replace the **entire**
> contents of the WA CSS box (select all → delete → paste → Save). A partial paste
> leaves the older styles that were below the cut still active and looks half-applied.

### `current-live-backup.css` — the RESTORE file
A snapshot of the old CSS that was live before the redesign. **Use it to revert:** if a
paste goes wrong, replace the WA CSS tab with this file and save to get back to a known
state.
