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

Find the box for the right year, add a bullet, and type the date.

**Put it wherever's convenient.** The page sorts each year's dates newest
first on its own, so a date typed in the wrong place still lands right.

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

**One box per year.** When January comes round, 2027 gets a box of its own
— don't add it inside an existing box.

Where you put the box doesn't matter. The page orders the years newest
first by itself.

1. **Website → Site pages → Meeting Minutes**, then **Edit**.
2. Add a **Content** gadget. That's the one with the normal editing
   toolbar — *not* Custom HTML.
3. Type the year on its own line: `2027`. Just the year, nothing else.
4. Under it, start a bulleted list and add the dates as usual.
5. **Set the CSS class.** Select the gadget, open its settings, and put
   this in the **CSS class** field:

   ```
   ngm-wa-minutes
   ```

6. Save.

**Step 5 is the one people forget.** Without it the box gets no styling at
all — plain bullets and blue underlined links, sitting apart from the rest
of the page. If a box ever looks like that, that field is what to check.

### Putting a year up before there's anything in it

Fine, and useful — it tells members the year exists and the minutes are
coming. Do the same as above, but stop after step 3: **just the year as the
heading, nothing under it.** The card will say "Nothing posted for this year
yet."

Add the dates to it as they arrive.

## Please don't

- **Don't put anything else in a box.** Headings and lists of dates only.
  No intro text, no notes. The wording at the top of the page is already
  handled.
- **Don't use two columns.** One list going down the page. Two columns look
  fine on a laptop and break on a phone.
- **Don't retype an entry to move it.** Retyping loses the link to its PDF.
  Cut the line and paste it where you want it — the link comes with it.
  (Usually you don't need to move anything: dates sort themselves.)
- **Don't leave an emptied box on the page.** If you move everything out of
  one, delete the box. An empty box with no heading shows up as a stray
  blank card.

## Something looks wrong?

**A box shows plain bullets and blue underlined links, and won't fold open.**
Its **CSS class** has been cleared. Select the box, open its settings, and
check the field says `ngm-wa-minutes`.

**A title shows as plain bold text above a card.** Same cause — that box, or
the box its heading sits in, is missing the class.

Anything else, email the website team at admin@needleworkguildmn.org rather
than trying to fix the layout by hand.
