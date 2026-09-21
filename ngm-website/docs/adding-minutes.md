# Adding a set of minutes

For whoever posts the minutes. No code, and nothing to install. Everything
happens inside the Wild Apricot admin site.

**You'll need:** admin access to the website, and the minutes saved as a PDF.

---

## How the page is put together

The page is a stack of **boxes, one per year**. Each shows up as a card
titled with the year and a count like *11 meetings*.

Board, executive board and annual meetings all go in the year they happened.
There is no separate box per kind of meeting.

All of it is visible — there is nothing to click open, and nothing for you
to switch on.

Inside a box there are only two things: a **heading** and a **list of
dates**. That's the whole format.

---

## Adding one meeting to a year that's already there

### 1. Put the PDF on the website

**Website → Files**, upload the PDF. Name it year-first so the files sort
themselves:

```
NGM Board Minutes 2026-09-14.pdf
```

Use the same pattern every time. The newest file then always sits at the
bottom of the list, and you can find any meeting by eye.

### 2. Open the page

**Website → Site pages → Meeting Minutes**, then **Edit**.

### 3. Type the date

Find the box for the right year. Click at the start of the newest date in
it, press **Enter** to make a new bullet above, and type the date.

**Newest goes on top.**

### 4. If it wasn't an ordinary board meeting, say so

Ordinary board meetings need nothing — they're most of the list.

For the others, type a dash and the kind on the same line:

```
7 April 2025 — Executive Board
5 April 2025 — Annual Meeting
```

Any dash works, and so does a middle dot. The wording after it is up to
you; keep it short. It turns into a small label beside the date.

### 5. Link it

Click the **link** button in the toolbar and pick the PDF from step 1.

**Select whatever's easiest** — just the date, or the whole line including
the label. Both come out the same. You don't have to be careful about it.

### 6. Save

The date appears as a row with a document icon. Clicking anywhere along the
row opens the PDF.

---

## The board met, but the minutes aren't written up yet

Type the date and **don't link it**. Leave it as plain text.

It shows as a greyed-out row with a small **Not posted** label, so members
can see the meeting happened and the minutes are coming.

When they're ready, come back, select the date and add the link. The label
disappears on its own.

## Starting a new year

Easiest way: **add a new box** above the others.

1. Add a **Content** gadget — the one with the normal editing toolbar, not
   Custom HTML.
2. Type the year as the heading, then the list of dates under it.
3. Open the gadget's settings and put this in the **CSS class** field:

   ```
   ngm-wa-minutes
   ```

   Without it the box won't be styled and won't fold out.

You can also just type a second heading and list inside an existing box.
That works, and you get two fold-out sections in the one card. A box per
year is tidier.

**The heading is just the year** — `2027`, nothing else. The kind of
meeting goes on the individual rows, as above.

A year where nothing has been posted yet is fine to put up: heading, empty
list. The card will say "Nothing posted for this year yet", which tells
members the year exists and the minutes are still coming.

## Please don't

- **Don't put anything else in a box.** Headings and lists of dates only.
  No intro text, no notes. The wording at the top of the page is already
  handled.
- **Don't use two columns.** One list going down the page. Two columns look
  fine on a laptop and break on a phone.
- **Don't retype the older entries.** They're fine as they are.

## Something looks wrong?

**A box shows plain bullets and blue underlined links, and won't fold open.**
Its **CSS class** has been cleared. Select the box, open its settings, and
check the field says `ngm-wa-minutes`.

**A title shows as plain bold text above a card.** Same cause — that box, or
the box its heading sits in, is missing the class.

Anything else, email the website team at admin@needleworkguildmn.org rather
than trying to fix the layout by hand.
