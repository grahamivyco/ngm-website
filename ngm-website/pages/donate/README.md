# Donate

**WA page:** Donate  ·  **URL:** `/donate`

Sandwich, one layout column:
1. `01-top.slim.html` — Custom HTML (hero, why-give, "Give online" heading)
2. Native WA "Donation form" gadget — no CSS class needed; skinned by `global.css` (see `02-form-gadget.txt`)
3. `03-bottom.slim.html` — Custom HTML (other ways to give, FAQ, thank-you CTA)

The linen band runs continuously: the "Give online" heading in `01-top`
(`padding-bottom:0`), through the form's layout row (set it to linen `#F0EAE0`),
into the first section of `03-bottom` (`padding-top:24px`).

After the master `global.css` is live, use the `.slim.html` versions.
