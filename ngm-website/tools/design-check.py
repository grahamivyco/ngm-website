#!/usr/bin/env python3
"""NGM design-system conformance check.

Run from anywhere:  python3 ngm-website/tools/design-check.py
Exit code 0 = conformant, 1 = findings to fix.

Checks (the rules live in design-system/NGM-design-system-prompt.md and
the repo-root CLAUDE.md):
  1. Every ngm-* class used in pages/ and system-pages/ markup has at
     least one rule in global-css/global.css (no unstyled classes).
  2. No embedded <style> blocks in page files (styling belongs in
     global.css; the self-contained exceptions all live in layout/).
  3. No inline style="…font-size…" overrides in page markup.
  4. Every font-size in global.css uses a type-role token; rem literals
     are allowed only for the display one-offs in SIZE_ALLOWLIST.
  5. No hardcoded font-family stacks in global.css outside the :root
     token definitions (use var(--ngm-sans) / var(--ngm-serif)).
  6. No per-instance WA id selectors (#id_XXXX…) — they change per
     render; use stable classes (see docs/wa-notes.md).
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent  # ngm-website/
CSS = ROOT / "global-css" / "global.css"

# Bare <form> wrapper inside the styled .ngm-cform card — never needs rules.
CLASS_EXCEPTIONS = {"ngm-cform-form"}

# Display one-offs that are deliberately not tokens (stat numbers, the $30
# price figure, hero numerals, the calendar micro-chip). Everything else
# must be a var(--ngm-*) token.
SIZE_ALLOWLIST = {"5rem", "2rem"}  # ONLY the $30 price lockup (figure + $-sign sup)

findings = []

css = CSS.read_text()
styled = set(re.findall(r"\.([a-zA-Z][\w-]*)", css))

pages = [f for d in ("pages", "system-pages")
         for f in sorted((ROOT / d).rglob("*.html"))
         if "mockups" not in f.parts]

for f in pages:
    html = f.read_text()
    rel = f.relative_to(ROOT)
    if "<style" in html:
        findings.append(f"{rel}: embedded <style> block — move the rules into global.css")
    stripped = re.sub(r"<style.*?</style>", "", html, flags=re.S)
    for m in re.finditer(r'style="([^"]*)"', stripped):
        if "font-size" in m.group(1):
            findings.append(f"{rel}: inline font-size override — use a type token in global.css")
    for m in re.finditer(r'class="([^"]+)"', stripped):
        for cls in m.group(1).split():
            if cls.startswith("ngm-") and cls not in styled and cls not in CLASS_EXCEPTIONS:
                findings.append(f"{rel}: class .{cls} has no rule in global.css")

# Blank out /* … */ comments (newlines kept, so line numbers stay true) —
# comments may cite live per-instance ids as documentation.
css_code = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), css, flags=re.S)

for i, line in enumerate(css_code.splitlines(), 1):
    for m in re.finditer(r"font-size:\s*([0-9.]+rem)", line):
        if m.group(1) not in SIZE_ALLOWLIST:
            findings.append(f"global.css:{i}: font-size {m.group(1)} — use a type-role token (var(--ngm-…))")
    if re.search(r"font-family:\s*['\"]", line) and "--ngm-" not in line:
        findings.append(f"global.css:{i}: hardcoded font-family — use var(--ngm-sans)/var(--ngm-serif)")
    if re.search(r"#id_[A-Za-z0-9]", line):
        findings.append(f"global.css:{i}: per-instance WA id selector — use stable classes")

if findings:
    print(f"DESIGN CHECK: {len(findings)} finding(s)\n")
    for f in sorted(set(findings)):
        print("  •", f)
    sys.exit(1)
print("DESIGN CHECK: clean — pages and global.css conform to the design system")
