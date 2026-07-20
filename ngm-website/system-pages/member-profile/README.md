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

⚠️ **Provisional:** the skin targets WA's shared form classes but was not verified
against this specific live page (it requires login). After the Global CSS is live,
open `/Sys/Profile`, check it, and if a field or button looks off, capture the element's
class and the skin can be tuned — same process used for the login page.
