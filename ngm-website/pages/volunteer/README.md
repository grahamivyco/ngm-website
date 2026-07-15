# Volunteer

**WA page:** Volunteer opportunities  ·  **Structure:** SINGLE Custom HTML gadget — `01-top.html`.
Three sections: Hero, Roles &amp; positions (role-card grid), Ways to pitch in, and a closing "Interested in helping?" CTA. A members-facing page introducing the volunteer roles that keep the Guild running.

## Wild Apricot setup
- Create a page at `/volunteer` (restrict to members if desired).
- Paste `01-top.html` into a Custom HTML gadget — it is fully self-contained.
- Once the Global CSS (`global.css`) is live in WA, switch to `01-top.slim.html` instead (same markup, no inline `<head>`/`<style>`).

## Confirm before go-live
- **Role descriptions** — the 14 role cards are DRAFT copy (flagged in-page with an HTML comment). Confirm each description with the board.
- **Volunteer-coordinator email** — the CTA button currently links to `ngmprograms@needleworkguildmn.org` (flagged in-page with a `SET:` comment). Confirm the best address for volunteer inquiries.
