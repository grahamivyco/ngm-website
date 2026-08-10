# Release plan — target Wednesday (Aug 12, 2026)

Everything merged through PR #198 is done; working tree is clean. What's left
falls into four buckets. Work the first two before the cutover; the cutover
itself is bucket 3.

---

## 1. System-page gaps (from the WA System-pages list)

The repo already covers: Access denied (403), Authorization required, Contact
profile (incl. Event registrations / Invoices / Donations tabs), Event details,
Membership renewal, Page not found (404), Terms of use, Unsubscribe — plus
Member public profile and Email member (styled in `global.css`), and the
non-system Login / Profile / Membership-application pages.

Still to style (all reachable from links the redesign ships):

- [x] **Change password** (`/Sys/Password/Change`) — CSS-only page, styled
      against the console-verified DOM (see
      `system-pages/change-password/README.md`). NB the custom header has
      no WA account dropdown, so the page's only entry points are the ones
      the redesign adds: the Member Hub My-profile card link and the
      /Sys/Profile banner button.
- [ ] **Reset password request** (`/Sys/ResetPasswordRequest`) — the
      "Forgot password" target on the login form and Authorization-required.
- [ ] **Reset password** — the page the emailed reset link lands on.
- [ ] **Event registration** — members register for Fall Finish / Retreat /
      workshops. Check first whether the existing `.WaGadgetPublicWizard`
      wizard styling already covers `.WaGadgetEventRegistration*`; extend if not.

Deliberately skipped (guild doesn't use them; nothing links there): Online
store cart/checkout/product, Blog post, Forum topic ("no forums"), Poll
details, Financial document, Add member to bundle, Anonymous payment profile,
Membership level change (single $30 level), Site search results. One quick
pass to confirm nothing in header/footer links to any of these is enough.

## 2. Content blanks — need real-world info (only the guild knows these)

- [ ] `pages/come-stitch/03-bottom.html` — in-person Come & Stitch venue
      (name + street address).
- [ ] `pages/sunday-tea-stitch/03-bottom.html` — host phone number for the
      "call to be let in" note.
- [ ] `pages/potpourri-stitchers/03-bottom.html` — confirm how attendees let
      the hostess know they're coming.
- [ ] Homepage — confirm Potpourri Stitchers day/time and Sunday Tea & Stitch
      frequency.
- [ ] Homepage + About — swap `REPLACE_WITH_..._GALLERY` photo placeholders
      for real `/resources/Pictures/...` URLs. (About tiles have `onerror`
      fallbacks, so this is non-blocking; homepage hero should be real.)
- [ ] `layout/suggestion-button/01-top.html` — fill the three Google-Form
      placeholders (`__ENTRY_IDEA__`, `__ENTRY_NAME__`, form action). If the
      form isn't ready, hold this gadget out of the release.
- [ ] `layout/wrapper-reset/01-top.html` — replace `REPLACE_HUB` with the
      real Member-Hub gadget ID.
- [ ] Contact-us — the branded inquiry form is a visual placeholder until the
      live form gadget is authorized; decide whether it ships as-is.

## 3. The cutover itself (manual pastes, per `docs/publishing-guide.md`)

- [ ] Paste `global-css/global.css` into WA → Website → CSS, Save.
      (`current-live-backup.css` is the instant revert if anything breaks.)
- [ ] Template: paste new header + footer gadgets.
- [ ] Each page in the guide's table, in order — Custom-HTML paste(s) plus
      native middle gadget where the page is a "sandwich".
- [ ] Join page: confirm it's ONE Custom-HTML gadget (delete the old
      membership-application gadget + second HTML gadget if still present).
- [ ] Favicon the native way: Settings → Site → Meta-tags → Raw Headers
      (`brand/favicon.ico` uploaded under Website → Files).

## 4. Post-cutover verification

- [ ] Spot-check every page logged OUT and logged IN (member view).
- [ ] Re-verify the `upcomingEventsStyle001` class on the homepage events
      gadget survives the theme cutover.
- [ ] Verify macro tokens render: `{Contact_First_Name}`,
      `{Membership_Level}`, `{Renewal_Date}`, `{Balance}`.
- [ ] Walk the auth loop end-to-end: log in, change password, log out,
      forgot-password email, reset, log back in.
- [ ] Register for a test event (event-registration styling check).
- [ ] Mobile pass on homepage, member hub, profile, one group page.
