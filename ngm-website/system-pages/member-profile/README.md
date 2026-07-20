# Member Profile

**WA page:** `/Sys/Profile` — CSS-only (Wild Apricot does not allow custom HTML here).

> **Mockups:** see [`mockups/`](mockups/) — `profile-buildable` is the CSS-only
> target this skin should produce; `profile-concept` is aspirational and **cannot**
> be built on a WA system page. Don't confuse the two when sharing.

This page is skinned entirely by `global-css/global.css` (the WA SYSTEM-PAGE FORMS +
WaGadgetLoginForm sections, plus the **MEMBER PROFILE + TABS** section): DM Sans /
Cormorant fonts, sage buttons, and NGM field styling. There are no gadgets to paste
for this page.

The **MEMBER PROFILE + TABS** block also skins the tabs the member-hub "Manage your
account" tiles link to — Event Registrations, Finances (Invoices & payments),
Donations, Privacy, Email preferences — since they're all views of this same
`/Sys/Profile` page. It styles the data tables (registrations/invoices/donations),
field rows, and tab bar on-brand.

✅ **Verified against the live DOM** (theme `casefile_guardian.v3.0`, July 2026). The
skin targets WA's real profile classes, confirmed from the logged-in page source:

| Element | Real WA class/selector |
|---------|------------------------|
| Profile gadget wrapper | `.WaGadgetContactProfile` |
| Page heading (separate gadget) | `.WaGadgetHeadline h1.header` |
| Tab bar / active tab | `ul.memberDetailsTabMenu` / `li.selected` |
| Section headers | `<h4>` inside `.captionContainer` |
| Field label / value | `.fieldLabel` / `.fieldBody` |
| Edit / Renew buttons | `input.typeButton` (Edit = `[id$="editButtonTop"]`, Renew = `[id$="RenewalButton"]`) |
| Privacy "Details to show" grid | `#memberFieldTable` |
| User ID row (hidden) | `#idContainer12024901` |

The earlier version targeted **guessed** classes (`.WaGadgetMemberProfile`, `.fieldName`,
`.tabItem`) that don't exist on the page, so it applied nothing — that's what a
plain-looking live profile means. If WA changes theme or field IDs, re-capture the page
source and re-map. Note the "Contact Profile" title and the red "Click EDIT PROFILE" arrow
are **content** (a Headline gadget), not CSS: the arrow is hidden by the skin, but rename
the page to "My profile" and delete the arrow image in WA to finish the look. Event
registrations / Invoices / Donations are separate `/Sys/Profile/*` pages — their table
skin is still generic and can be tuned the same way once captured live.
