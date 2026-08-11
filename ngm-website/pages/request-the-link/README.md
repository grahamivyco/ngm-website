# Request the Zoom Link — setup

A branded NGM form that auto-emails the Zoom link. Visitors only ever see our
form; a hidden Google Form + a short Apps Script do the sending. The link lives
in the script, not on the page, so it stays off public view.

## File (paste into ONE Custom HTML gadget)

- `01-top.html` — the **whole page** in a single gadget: two-column hero + form
  (copy left, contact-style outlined form card right), then Visit (come in
  person), an "Already a member?" full-width Member Hub tile, and the Join CTA.
  On submit the form swaps to a "Check your inbox" success tile.

The Google Form action URL and entry ids are already wired into `01-top.html`
(form id `1FAIpQLSdHUEpdX3DAQzMKyAnL6cCdAB5SRBMBeLgCbpwrXQAH3ZFr5A`).
Styling is in `global-css/global.css` (`.ngm-rl-*`, plus the shared `.ngm-cform`
/ `.ngm-field` contact-form styles and `.ngm-mt-hero-grid`).

## One-time setup

### 1. Make the hidden Google Form
Google Form with four questions, in this order:
- **Name** — Short answer
- **Email** — Short answer, **Required**
- **Which meeting?** — **Short answer** (recommended — see warning)
- **Message** — Paragraph (holds the prefilled "I'm not a member…" note; the
  visitor can edit it before sending)

It's never shown to anyone, so don't bother styling it.

> **⚠️ Make "Which meeting?" a Short answer, not a Dropdown/Multiple choice.**
> Google validates choice questions against their option list: any value it
> doesn't recognise is rejected. Because our page posts through a hidden iframe
> and never reads Google's response, a rejected submission is *silent* — the
> visitor still sees "Check your inbox", but nothing is recorded and the
> Apps Script auto-reply never runs, so **no link email is sent.** A Short
> answer accepts whatever the branded dropdown sends, so the on-site
> `<select>` options can say anything. (If you insist on a dropdown, its
> options must match the `<option>`s in the form in `01-top.html`
> **character for character.**)

### 2. Get the form's action URL + entry ids
- Open the live form → right-click → **View page source** → search `entry.` —
  each question has an `entry.1234567890` id. Note which is which.
- The action URL is the form's link with `/viewform` changed to
  **`/formResponse`**.

### 3. Form wiring — ✅ DONE (values live in `01-top.html`)
The placeholders described above are already filled in the form inside
`01-top.html` (the old separate `02-form.html` was folded into it):
`action` → the live `/formResponse` URL · Name `entry.1887642062` ·
Email `entry.1387094665` · Which meeting? `entry.692599503` ·
Message `entry.2137921043`. Only redo this if the Google Form's
questions change (each edit can mint new entry ids).

### 4. Add the auto-reply (Apps Script)
In the Google Form: **⋮ menu → Script editor** (or Extensions → Apps Script),
paste this, and set your real link + passcode:

```javascript
function onFormSubmit(e) {
  var items = e.response.getItemResponses(), email = '', name = '';
  for (var i = 0; i < items.length; i++) {
    var t = items[i].getItem().getTitle().toLowerCase();
    if (t.indexOf('email') > -1) email = items[i].getResponse();
    if (t.indexOf('name')  > -1) name  = items[i].getResponse();
  }
  if (!email) return; // email required, but guard anyway
  MailApp.sendEmail({
    to: email,
    replyTo: 'inquiry@needleworkguildmn.org', // replies go to the guild, not the account running the script
    name: 'Needlework Guild of Minnesota',    // display name in the recipient's inbox
    subject: 'Your Zoom link — Needlework Guild of Minnesota',
    htmlBody: 'Hi ' + (name || 'there') + ',<br><br>'
            + 'Welcome! Here is the Zoom link for Guild meetings:<br><br>'
            + '<b>Link:</b> PASTE_ZOOM_LINK<br>'
            + '<b>Passcode:</b> PASTE_PASSCODE<br><br>'
            + 'It works for every meeting, and your first visit is free. '
            + 'The host opens the room five minutes early.<br><br>'
            + '— Needlework Guild of Minnesota'
  });
}
```

Then wire the trigger: **clock icon (Triggers) → Add Trigger →** function
`onFormSubmit`, event source **From form**, type **On form submit** → save and
authorize.

### 5. Test
Submit the form on the page. The branded "Check your inbox" message should show,
and the link email should arrive within a minute.

## Notes
- **Keeps the link private:** it's only in the Apps Script, never in the page
  HTML, and only ever emailed to the address entered.
- **Wild Apricot CSP:** if the cross-origin post is ever blocked (the thank-you
  never appears), the fallback is to point the form's `action` at the Google
  Form directly, or embed the Google Form iframe. The Apps Script auto-reply
  works either way.
