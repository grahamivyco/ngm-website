# Join

**WA page:** Join (slug `/join`)
**Structure:** ONE Custom-HTML gadget holding the whole page —
`01-page.html`. The membership form is NOT embedded here; it lives on its
own page, `/Application-Duplicate/` (see `system-pages/membership-application/`).

`01-page.html`, top to bottom:

1. **Hero** (cream) — eyebrow **Join**, "Become a member", membership facts
   folded into the copy ($30/year, welcoming since 1972), photo alongside,
   and one CTA button — "Start the membership application" — linking to
   `/Application-Duplicate/`.
2. **Pricing** (linen) — big lone $30 with the per-month/June–May details
   folded into the lead copy.
3. **Visit** (cream) — the homepage "Come stitch with us" section with the
   MVUUF address/photo and the Zoom tiles band.
4. **Contact CTA** (rose band) — "Questions? / We'd love to help" linking
   to /contact.
5. Ends with the Member-Hub-tile login-redirect script.

## WA editor setup

The Join page should contain exactly one Custom-HTML gadget, holding
`01-page.html`. Earlier versions used two Custom-HTML gadgets (01-top /
03-bottom) with the native WA "Membership application" gadget between
them — WA rendered the form's later steps (payment, confirmation) in-page
surrounded by the marketing sections, so the form moved to the dedicated
`/Application-Duplicate/` page. If the old gadgets/rows are still present: delete the
Membership-application gadget and the second Custom-HTML gadget, and paste
`01-page.html` into the remaining one.

Styling: global.css. The JOIN PAGE embed block scoped to
`body.ngm-join-page` is now inert (this page no longer adds that body
class) and is kept only as a parked reference.

## Open TODO
- Replace hero photo if desired (currently a real /resources URL).
