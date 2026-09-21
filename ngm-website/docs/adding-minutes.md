# Adding a set of minutes

For whoever posts the minutes. No code, and nothing to install. Everything
happens inside the Wild Apricot admin site.

**You'll need:** admin access to the website, and the minutes saved as a PDF.

---

## How the page is put together

The page is a stack of **boxes**. Each box is one set of minutes — "Board
Meeting Minutes 2025", "Annual Meeting Minutes", and so on — and shows up as
a card with a title, a document icon, and a count like *11 meetings*.

Visitors click a title to fold the list open. That happens on its own; there
is nothing for you to switch on.

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

### 4. Link it

Select the date you just typed, click the **link** button in the toolbar,
and pick the PDF from step 1.

### 5. Save

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
2. Type the heading, then the list of dates under it.
3. Open the gadget's settings and put this in the **CSS class** field:

   ```
   ngm-wa-minutes
   ```

   Without it the box won't be styled and won't fold out.

You can also just type a second heading and list inside an existing box.
That works, and you get two fold-out sections in the one card. A box per
year is tidier.

**Name the heading properly.** It becomes the card's title, and the page
carries more than one kind of minutes, so it has to say which:

```
Board Meeting Minutes 2027
```

Not just "2027".

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
