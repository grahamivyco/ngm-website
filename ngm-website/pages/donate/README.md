# Donate

**WA page:** Donate  ·  **URL:** `/donate`

Sandwich, one layout column:
1. `01-top.html` — Custom HTML (hero, why-give, "Give online" heading). Tags
   `<body class="ngm-donate-page">` and makes the hero **"Donate now"** button
   scroll to the inline form (`#ngm-give`) instead of leaving for WA's separate
   `/donation` page — visitors reach the form without clicking through.
2. Native WA **"Donation form"** gadget — placed RIGHT HERE, in the same
   layout column, so the form shows inline on the page (no extra step). No CSS
   class needed; it's skinned by `global.css` (see `02-form-gadget.txt`).
3. `03-bottom.html` — Custom HTML (other ways to give, FAQ, thank-you CTA)

The linen band runs continuously: the "Give online" heading in `01-top`
(`padding-bottom:0`), through the form's layout row (set it to linen `#F0EAE0`),
into the first section of `03-bottom` (`padding-top:24px`).

## Skin
The donation form is skinned by the **"DONATION FORM"** block in `global.css`.
It uses the same inner WA markup as the membership wizard (`.fieldContainer` /
`.fieldLabel` / `.mandatorySymbol` / `.fieldBody` inputs / `h3.formTitle` /
`.navigationContainer` / `.nextButton`), so the two forms match. Because the
donation gadget's wrapper class is unreliable, the skin is scoped to
`body.ngm-donate-page` (set by `01-top.html`) — plus a `.WaGadgetDonationForm`
fallback — and cards `#idGeneralFormContainer` (the container that holds the
whole form: title → fields → reCAPTCHA → "Pay with card"), flattening WA's
sliced rounded-corner box chrome around it.

After the master `global.css` is live, use the `.html` versions.
