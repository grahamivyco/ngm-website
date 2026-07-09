# Global CSS

The full contents of the WA **Global CSS** tab go in `global.css`.

This is where site-wide overrides live (the `body`-prefixed, high-specificity
selectors that beat the `casefile_guardian` theme) plus the CSS-only skins for
system pages, each scoped to its WA gadget class (e.g.
`body .WaGadgetMembershipApplication`) to prevent selector leakage.

Paste the entire tab into `global.css`. When you update it, replace the whole file
so history shows a clean diff.
