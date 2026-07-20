# Member Profile — mockups

Two designs for `/Sys/Profile`. **They are not equivalent — read which is which
before showing either to anyone.**

## `profile-buildable.*` — the real target
Wild Apricot's own page: same structure, same fields, same order as the live site
(matched against a screenshot of the real page). Everything restyled here is
**CSS only**, so this is what the Global CSS should aim to produce.

What the CSS does: Cormorant heading + DM Sans body · purple page title → charcoal
serif · light-blue subheaders → sage eyebrows · pink links → sage · light-blue
buttons → sage pills · field rows with sage-dark labels and hairline dividers ·
sage underline on the active tab.

Two changes that are **not** CSS:
- The live page title reads "CONTACT PROFILE" — that's the WA page name, renameable
  in page settings.
- The red arrow graphic ("Click EDIT PROFILE to Make Changes") is content added to
  the page; delete it once the button reads as a button.

Also possible: hiding fields members don't need (e.g. **User ID**) with
`display:none` — hidden, not removed; the data still exists.

## `profile-concept.*` — aspirational, NOT buildable
A fully NGM-designed profile: membership hero band with Renew, five account cards
with at-a-glance summaries, two-column contact/email layout. **WA does not allow
custom HTML on `/Sys/Profile`**, so the structure here cannot be built. Useful for
showing intent; misleading if presented as a plan.

## Before the CSS can actually be written
These match WA's *structure* but not its *class names*. Writing selectors that
land needs one Inspect snippet of the live profile area (right-click the
"Membership details" heading → Inspect → Copy → Copy outer HTML). Until then the
skin in `global.css` is provisional — see the parent README.
