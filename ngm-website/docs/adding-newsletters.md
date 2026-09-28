# Adding a newsletter issue

For whoever posts the newsletter. No code, and nothing to install.
Everything happens inside the Wild Apricot admin site.

**You'll need:** admin access to the website, and the issue saved as a PDF.

---

## How the page is put together

All the issues sit in **one box**, split into **sections, one per year**.
Each section shows the year and a count like *4 issues*.

A section is only two things: a **heading line** (the year) and a
**bulleted list of issues** under it. That's the whole format.

---

## Adding an issue to a year that's already there

### 1. Put the PDF on the website

**Website → Files**, upload the PDF. Name it year-first so the files sort
themselves:

```
NGM Newsletter 2026-10.pdf
```

### 2. Open the page

**Website → Site pages → Newsletter Archive**, then **Edit**.

### 3. Type the issue name

Find the right year. Click at the start of the first bullet,
type the issue name, and press **Enter**. Newest goes at the top.

Name it the way the Guild refers to it: `October 2026`, `Fall 2026`.

### 4. Link it

Select the name, click the **link** button in the toolbar, and pick the
PDF from step 1.

### 5. Save

The issue appears as a row with a document icon. Clicking anywhere along
the row opens the PDF.

---

## Starting a new year

Newest year goes at the top of the box.

1. **Website → Site pages → Newsletter Archive**, then **Edit**.
2. Click at the very start of the box's first line (the current year)
   and press **Enter** to open a blank line above it.
3. Click the blank line and type the new year: `2027`. Just the year.
4. Press **Enter**, click the **bulleted list** button, and add the issue.
5. Save.

If the new year's line comes out as a bullet, click the **bulleted list**
button once to turn the bullet off for that line.

## Please don't

- **Don't put anything else in the box.** Year headings and lists of
  issues only. No intro text or notes.
- **Don't use two columns.** One list going down the page. Two columns
  break on a phone.
- **Don't leave an issue unlinked.** A bullet with no link shows as a
  greyed-out row with a "Not posted" label.
- **Don't retype an entry to move it.** Retyping loses its link. Cut the
  line and paste it where you want it.

## Something looks wrong?

**The box shows plain bullets and blue underlined links.** Its **CSS
class** has been cleared. Select the box, open its settings, and check the field
says `ngm-wa-docs`.

Anything else, email the website team at admin@needleworkguildmn.org
rather than trying to fix the layout by hand.
