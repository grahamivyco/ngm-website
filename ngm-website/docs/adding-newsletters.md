# Adding a newsletter issue

For whoever posts the newsletter. No code, and nothing to install.
Everything happens inside the Wild Apricot admin site.

**You'll need:** admin access to the website, and the issue saved as a PDF.

---

## How the page is put together

The page is a stack of **boxes, one per year**. Each shows up as a card
titled with the year and a count like *4 issues*.

Inside a box there are only two things: a **heading** (the year) and a
**list of issues**. That's the whole format.

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

Find the box for the right year. Click at the start of the first bullet,
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

**One box per year.** When January comes round, 2027 gets a box of its own.
Don't add it inside an existing box.

Where you put the box doesn't matter. The page orders the years newest
first by itself.

1. **Website → Site pages → Newsletter Archive**, then **Edit**.
2. Add a **Content** gadget. That's the one with the normal editing
   toolbar, not Custom HTML.
3. Type the year on its own line: `2027`. Just the year.
4. Press **Enter**, click the **bulleted list** button, and add the issue.
5. **Set the CSS class.** Select the gadget, open its settings, and put
   this in the **CSS class** field:

   ```
   ngm-wa-docs
   ```

6. Save.

**Step 5 is the one people forget.** Without it the box gets no styling:
plain bullets and blue underlined links. If a box ever looks like that,
that field is what to check.

## Please don't

- **Don't put anything else in a box.** The year and a list of issues
  only. No intro text or notes.
- **Don't use two columns.** One list going down the page. Two columns
  break on a phone.
- **Don't leave an issue unlinked.** A bullet with no link shows as a
  greyed-out row with a "Not posted" label.
- **Don't retype an entry to move it.** Retyping loses its link. Cut the
  line and paste it where you want it.
- **Don't leave an emptied box on the page.** Delete it.

## Something looks wrong?

**A box shows plain bullets and blue underlined links.** Its **CSS class**
has been cleared. Select the box, open its settings, and check the field
says `ngm-wa-docs`.

Anything else, email the website team at admin@needleworkguildmn.org
rather than trying to fix the layout by hand.
