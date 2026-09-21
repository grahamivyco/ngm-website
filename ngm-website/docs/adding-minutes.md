# Adding a set of board minutes

For whoever posts the minutes. You don't need to know any code, and you
don't need this repository. Everything happens inside the Wild Apricot
admin site.

**You'll need:** admin access to the website, and the minutes saved as a PDF.

---

## 1. Put the PDF on the website

Go to **Website → Files** and upload the PDF.

Name it so the files sort themselves, year first:

```
NGM Board Minutes 2026-09-14.pdf
```

Keep using the same pattern every month. It means the newest file is always
at the bottom of the list, and you can find any meeting by eye.

## 2. Open the minutes page

**Website → Site pages → Meeting Minutes**, then **Edit**.

## 3. Add the date

Find the list of dates for the right year.

Click at the start of the newest date in that list, press **Enter** to make
a new bullet above it, and type the date.

**Newest goes on top.** The list runs down the page from most recent to
oldest.

## 4. Link the date to the PDF

Select the date you just typed, click the **link** button in the toolbar,
and choose the PDF you uploaded in step 1.

## 5. Save

That's it. The date will show up as a row with a document icon, and clicking
anywhere on the row opens the PDF.

---

## If the board met but the minutes aren't written up yet

Type the date and **don't link it**. Leave it as plain text.

It'll show as a greyed-out row with a small **Not posted** label, so members
can see the meeting happened and the minutes are coming.

When the minutes are ready, come back, select the date, and add the link as
in step 4. The "Not posted" label disappears on its own.

## The first meeting of a new year

Each year has its own block, and often its own box on the page. Add a
**heading** above the newest list naming what it is:

```
Board Meeting Minutes 2027
```

Then a bulleted list under it, and add the date as usual.

Keep the wording consistent with the blocks already there. The page carries
more than one kind of minutes — board, executive board, annual meeting — so
the heading has to say which. The line underneath it is added automatically.

If you add a **new box** rather than typing into an existing one, it needs
the CSS class set. See "Something looks wrong?" below for where that field
is; the value is `ngm-wa-minutes`.

## Please don't

- **Don't put anything else in that box.** A heading and a list of dates,
  nothing more. No intro text and no notes — the wording above and below
  the list lives elsewhere on the page and is already handled.
- **Don't use two columns.** One list going down the page. Two columns look
  fine on a laptop and break on a phone.
- **Don't retype the older entries.** They're fine as they are.

## Something looks wrong?

If the list suddenly loses its formatting (plain bullets, blue underlined
links, no icons), the gadget's **CSS class** has probably been cleared.
Select the box holding the list, open its settings, and check the CSS class
field says:

```
ngm-wa-minutes
```

If anything else looks off, email the website team at
admin@needleworkguildmn.org rather than trying to fix the layout by hand.
