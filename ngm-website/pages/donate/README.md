# Donate

**WA page:** Donate  ·  **URL:** `/donate`

Sandwich, one layout column:
1. `01-top.html` — Custom HTML: hero (eyebrow "Donate" + short copy that folds
   in why-give, where gifts go, and the 501(c)(3) / tax-deductible line, beside
   a photo — no CTA buttons) then the "Give online" heading (`#ngm-give`). Tags
   `<body class="ngm-donate-page">` so `global.css` can skin the form, and
   relabels the submit button to "Donate securely".
2. Native WA **"Donation form"** gadget — placed RIGHT HERE, in the same
   layout column, so the form shows inline on the page (no extra step). No CSS
   class needed; it's skinned by `global.css` (see `02-form-gadget.txt`). The
   skin paints the form's layout cell linen (`#F0EAE0`, same band as "Give
   online") with normal section spacing above and below.
3. `03-bottom.html` — Custom HTML: **Alternatives** (eyebrow) — three bordered
   cards (`.ngm-feat3` — By mail / Give monthly / In honor or memory) with a
   BARE icon (no sage chip behind it); they stay side by side until they wrap
   near mobile. The "Get in touch" contact link is folded into the intro copy
   above them;
   then the **Join** section (identical to the About page's "Find your people…"
   block). This section is linen so it stands apart from the white form section.
   There is no FAQ: its answers live in the hero copy (tax-deductible, where
   gifts go) and the tiles (monthly, in honor).

## Backgrounds
Hero = cream; the **"Give" heading band and the form = white**; **Alternatives
= linen** (so the form doesn't blend into it); Join = its own band. The form's
white field is painted on the gadget's own content box — see the "DONATION
FORM" block in `global.css`.

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

### Field layout
On desktop the fields flow in a 6-column grid where **every field is full width
by default**; only two groups pair up — **First + Last name** side by side, and
**City / State / Zip** three across. On **tablet** (641–900px) City/State/Zip
drop to their own lines; the rest is unchanged. It **stacks** to one column at
≤640px. `min-width:0` on each cell keeps long helper text (the "Donor
directions" hint) wrapping inside the form so nothing overflows into horizontal
scroll. Dropdowns use a custom chevron inset from the right. Spans map to WA
field **ids** in the "DONATION FORM" block of `global.css` (e.g.
`#idContainer12024897`/`…898` = First/Last, `…931/932/933` = City/State/Zip);
added fields fall back to full width and removed fields' rules go inert.

### Hero photo
Hidden on tablet & mobile (≤900px) so the copy leads straight to the form.

After the master `global.css` is live, use the `.html` versions.
