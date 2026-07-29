# Request the Zoom Link — setup

A branded NGM form that auto-emails the Zoom link. Visitors only ever see our
form; a hidden Google Form + a short Apps Script do the sending. The link lives
in the script, not on the page, so it stays off public view.

## Files (paste each into its own Custom HTML gadget, top to bottom)

1. `01-top.html` — hero / intro
2. `02-form.html` — the branded form (has 4 placeholders to fill, below)
3. `03-bottom.html` — the "what happens next" note

Styling is in `global-css/global.css` (`.ngm-rl-*`).

## One-time setup

### 1. Make the hidden Google Form
Google Form with four questions, in this order:
- **Name** — Short answer
- **Email** — Short answer, **Required**
- **Which meeting?** — Short answer (or Dropdown)
- **Message** — Paragraph (holds the prefilled "I'm not a member…" note; the
  visitor can edit it before sending)

It's never shown to anyone, so don't bother styling it.

### 2. Get the form's action URL + entry ids
- Open the live form → right-click → **View page source** → search `entry.` —
  each question has an `entry.1234567890` id. Note which is which.
- The action URL is the form's link with `/viewform` changed to
  **`/formResponse`**.

### 3. Fill the 4 placeholders in `02-form.html`
| Placeholder | Replace with |
| --- | --- |
| `__FORM_ACTION__` | the `/formResponse` URL |
| `__ENTRY_NAME__` | Name question's `entry.…` id |
| `__ENTRY_EMAIL__` | Email question's `entry.…` id |
| `__ENTRY_MEETING__` | "Which meeting?" question's `entry.…` id |
| `__ENTRY_MESSAGE__` | "Message" question's `entry.…` id |

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
