# Join

**WA page:** Join (slug `/Join-Duplicate`)
**Structure:** donate-style — THREE pieces stacked in one column:

1. `01-top.html` — Custom HTML gadget: hero (eyebrow **Join**, "Become a
   member", membership facts folded into the copy, social buttons, photo —
   no CTAs) + the white "Start here / Begin your membership" heading band.
   Its script adds `body.ngm-join-page`.
2. **Native WA "Membership application" gadget** — placed directly below
   01-top so the form's email step starts right on this page (see
   `02-form-gadget.txt`). Set the row background to white.
3. `03-bottom.html` — Custom HTML gadget: pricing as plain copy (linen; the
   old price card's badges/tags/checklist were dropped), "What you get"
   checklist grid (white), the homepage "Visit / Where we meet" section
   (cream), and a "Questions? Contact us" rose CTA band.

Removed from the old page: hero CTAs, the big price card, the "Why join /
More than a membership" pillars, and the "Ready to stitch / Become a member
today" closing CTA (the form at the top *is* the join CTA now).

Styling: global.css — the site-wide MEMBERSHIP APPLICATION skin cards the
form; the small JOIN PAGE block (scoped to `body.ngm-join-page`) paints the
form band white and tucks the card under the heading.

## Open TODO
- Replace hero photo if desired (currently a real /resources URL).
- Verify the embedded application gadget's email step live; later steps
  (payment/confirmation) may continue through WA's native flow — expected.
