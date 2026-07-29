# Suggestion button — floating "Share a suggestion"

A small rose button pinned to the bottom-right of every page. Tapping it opens a
short, NGM-styled form; the idea is written to a **Google Form** (which feeds a
**Google Sheet**), and that Sheet is embedded on a members' **Suggestion Board**
page so everyone can see what's been suggested next to the committee's reply.

This is the "light" alternative to a blog or forum: about an hour to set up, free,
and no delay to launch. If it gets real use, that's a good case for building
something bigger later.

## Files

| File | What it is |
| --- | --- |
| `01-top.html` | **The gadget.** Self-contained (own scoped CSS + JS). Paste into a site-wide Custom HTML gadget. |
| `mockups/preview.html` | **Standalone visual** — the gadget on a sample members' page, for showing the board. Not for pasting into WA (it embeds fonts and drops the members-only guard). |
| `mockups/preview.png` | Screenshot, form open. |
| `mockups/preview-button.png` | Screenshot, button at rest. |

This is a **self-contained layout gadget**, like `layout/header/` and
`layout/footer/` — it carries its own CSS/JS because it's HTML+JS, not just
styling, so it is a documented exception to the "styling lives in global.css"
rule (see the root `CLAUDE.md`). Fonts (Cormorant Garamond + DM Sans) are the
ones already loaded in WA's page head, same as the footer.

## Where it goes

Paste the entire contents of `01-top.html` into a **Custom HTML gadget at the
bottom of the Wild Apricot page template** (site-wide), right next to the footer
gadget. Because the button is `position:fixed`, it floats over every page no
matter where in the template the gadget sits.

## Before it works — three placeholders

The form posts to a Google Form. Create the form once, then fill in three
placeholders in `01-top.html`:

1. **Make the Google Form** (Google Drive → New → Google Form). Two questions:
   - `Your suggestion` — Paragraph, **Required**
   - `Your name` — Short answer, **not** required
   Under the form's **Responses** tab, click the Sheets icon to create the
   linked results spreadsheet.

2. **Get the field entry IDs.** Open the live form, right-click → *View page
   source*, and search for `entry.` — each question has an `entry.1234567890`
   id. (Or use the form's pre-fill link: *⋮ menu → Get pre-filled link*, fill
   dummy answers, *Get link*, and read the `entry.…` values out of the URL.)

3. **Fill in the placeholders:**
   | Placeholder | Replace with |
   | --- | --- |
   | `__FORM_ACTION__` | The form URL with `/viewform` changed to **`/formResponse`** |
   | `__ENTRY_IDEA__` | The `entry.…` id for the *suggestion* question |
   | `__ENTRY_NAME__` | The `entry.…` id for the *name* question |

   Also set the thank-you link (`href="/suggestions"`) to the real Suggestion
   Board page URL.

The form submits into a hidden iframe, so the member stays on the site and sees
an on-page "Thank you" instead of Google's confirmation screen.

> **If Wild Apricot's Content Security Policy blocks the cross-origin post**
> (the thank-you never appears): the simplest fallback is to drop the native
> form and embed the Google Form's own iframe inside the panel instead
> (*Google Form → Send → `< >` embed*), or point the button straight at the
> form in a new tab. The native styled form here is the nicer default; the
> embed is the guaranteed-to-work fallback.

## The results page (Suggestion Board)

On a **members-only** WA page, add a Custom HTML gadget embedding the linked
Google Sheet (*File → Share → Publish to web → Embed*, or the Sheet's
`/pubhtml` link). Hide the raw timestamp column and add two committee-owned
columns to the sheet — **Committee reply** and **Status** — which the committee
fills in and members see update live. See the artifact mock-up for the intended
look of that page.

## Members-only vs site-wide

By default the button only shows to **logged-in members** (WA sets
`body.memberContentView`), matching the footer's login-state pattern. To show it
to **everyone**, remove both:

- the `MEMBERS-ONLY visibility` CSS block in `01-top.html`, and
- the `MEMBERS-ONLY guard` `if(...)` block in the `<script>`.

## Two calls for the board

- **Who keeps an eye on it?** One committee member should check the sheet (say,
  weekly) and type a short reply. That single habit is what keeps a suggestion
  box alive — a stale, unanswered list is worse than none.
- **Names, anonymous, or both?** The form ships with an optional name field and
  an *anonymous* toggle, so members choose per suggestion. Anonymous lowers the
  bar to speak up; a name lets the committee follow up. Recommended: keep both.

## Keeping the preview in sync

`mockups/preview.html` contains an **inline copy** of the gadget's markup, CSS,
and JS (with fonts embedded and the members-only guard removed, plus a faked
submit so the thank-you state can be demonstrated). If you change `01-top.html`,
mirror the change in the preview so the screenshots stay honest.
