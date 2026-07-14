# Contact Us

**WA page:** Contact Us  ·  **URL:** `/contact-us`

Sandwich, one layout column:
1. `01-top.html` — Custom HTML (hero + "Send us a message" heading band)
2. Native WA contact / web form gadget — no CSS class needed (skinned by `global.css`); see `02-form-gadget.txt`
3. `03-bottom.html` — Custom HTML (Reach us contact boxes, Find us map, Volunteer board roles + emails, Come-see-us CTA)

The heading band that ends `01-top` uses `padding-bottom:0` and the opening band of
`03-bottom` uses `padding-top:24px`, so the native form nests snugly in the middle.

After the master `global.css` is live, use the `.slim.html` versions.
