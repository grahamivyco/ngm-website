# Join

**WA page:** Join (slug `/Join-Duplicate`)
**Structure:** TWO Custom-HTML gadgets stacked in one column — the
membership form is NOT embedded here; it lives on its own page,
`/application` (see `system-pages/membership-application/`).

1. `01-top.html` — hero: eyebrow **Join**, "Become a member", membership
   facts folded into the copy ($30/year, welcoming since 1972), photo
   alongside, and one CTA button — "Start the membership application" —
   linking to `/application`.
2. `03-bottom.html` — pricing as plain copy (linen; big lone $30 with the
   per-month/June–May details folded into the lead), the homepage
   "Visit / Come stitch with us" section (cream, with the Zoom tiles band),
   and a "Questions? / We'd love to help" rose CTA band linking to
   /contact-us. Ends with the Member-Hub-tile login-redirect script.

`02-form-gadget.txt` records that the native WA "Membership application"
gadget was REMOVED from this page and how to delete it in the WA editor.
Earlier iterations embedded the form between the two gadgets, but WA
renders the form's later steps (payment, confirmation) in-page surrounded
by the marketing sections — so the form moved to the dedicated
`/application` page instead.

Styling: global.css. The JOIN PAGE embed block scoped to
`body.ngm-join-page` is now inert (01-top no longer adds that body class)
and is kept only as a parked reference.

## Open TODO
- Replace hero photo if desired (currently a real /resources URL).
