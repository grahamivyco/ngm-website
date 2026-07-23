# Membership Application

**WA page:** `/application` (WA system/join form)

The form is skinned site-wide by `global-css/global.css` (the WA SYSTEM-PAGE FORMS
section, plus the MEMBERSHIP APPLICATION / JOIN WIZARD block). `01-top.html` is an
optional branded heading to place above the form if the page allows a Custom HTML
gadget. **Verify the form skin against the live page** — WA's form markup is deeply
nested and the skin is provisional.

The heading copy now matches the Join page: the membership year runs **June 1 through
May 31**. The CSS skin was verified against the **live `/application` identify-step
markup** (theme `casefile_guardian`) and corrected to WA's real classes — `.validationError`
for inline errors, `.levelLabel` for the selected level, `.fieldContainer`/`.fieldLabel`
for field rows — plus the pay / prev / cancel buttons via WA's stable control-id suffixes
(`…_payOnline`, `…_payWithBankAccount`, `…_prev`, `…_cancel`). The later **profile and
payment steps** reuse these same classes but should still be eyeballed on the live flow.

---

## The new-member flow (how the pieces connect)

Entry points (header **Join**, the login-page footer link, page CTAs) →
**`/join`** marketing page →
**`/application`** (this native WA form + optional branded heading) →
WA-native **$30 payment** + confirmation + account creation →
**`/sys/login`** → **Member Hub**.

Repo pieces: `pages/join/` (marketing), this folder (`/application`),
`system-pages/login/` (which links back to Join for non-members).

**Payment-button wording:** `button-rename.html` is a small inline `<script>`
(paste into a Custom HTML gadget on `/application`) that renames the review-step
buttons "Pay with credit or debit card" → "Pay Online" and "Invoice me" →
"Pay by check (invoice me)". Button labels are WA input values, so this can't be
done in CSS. It matches on exact label text, so it never touches the earlier
steps' "Next" button.

## Live-verification & WA-settings checklist

Things that can only be done on the live Wild Apricot site — run these before launch:

1. **Confirm real slugs:** `/join`, `/application`, `/sys/login`. If any differ, update
   the login footer link (`system-pages/login/03-bottom.html` + its `.slim`, currently a
   `/join` placeholder marked `SET URL`) and the three Join CTAs
   (`pages/join/01-top.html`).
2. **Branded heading:** on `/application`, check whether WA allows a Custom HTML gadget
   **above** the form. If yes, paste `01-top.html`; if not, skip — the form is still
   skinned. (See `02-wa-gadget.txt`.)
3. **Walk the live form** with the redesign CSS active and spot-check: fonts, field
   borders + focus ring, level pricing, mandatory asterisks, Next / Submit / Cancel pill
   buttons, and validation / error messages. Adjust any selector that didn't catch the
   live markup.
4. **WA admin config (outside this repo):** membership level = **$30/yr**, term
   **June 1 – May 31**, online payment enabled, application-approval workflow set,
   confirmation email content reviewed.
5. **End-to-end test** with a throwaway email: submit application → pay $30 → receive
   confirmation → the new account logs in → lands on **Member Hub**. Then refund/delete
   the test record.
6. **Header state:** logged-out vs logged-in header swaps correctly after joining.
