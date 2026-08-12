#!/usr/bin/env python3
"""Build ngm-website/dist — PRODUCTION-CLEAN copies of every paste file.

The canonical sources (pages/, system-pages/, layout/, global-css/) keep
their maintainer comments; this tool writes comment-stripped twins under
dist/ with the same relative paths. Paste INTO Wild Apricot from dist/;
edit only the sources, then re-run:

    python3 ngm-website/tools/build-dist.py

What gets stripped:
  - HTML comments (<!-- ... -->)
  - CSS comments (/* ... */) in <style> blocks and in global.css
  - JS block comments (/* ... */) and whole-line // comments in <script>
  - runs of blank lines collapse to one

Never hand-edit dist/ — it is overwritten on every run.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def strip_css(text: str) -> str:
    return re.sub(r"/\*[\s\S]*?\*/", "", text)


def strip_js(text: str) -> str:
    # Safe for this codebase: no JS string/regex literal contains "/*",
    # and no code line begins with "//" that isn't a comment.
    text = re.sub(r"/\*[\s\S]*?\*/", "", text)
    text = re.sub(r"(?m)^[ \t]*//.*$", "", text)
    return text


def tidy(text: str) -> str:
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.lstrip("\n")


def clean_html(text: str) -> str:
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    text = re.sub(
        r"(<style[^>]*>)([\s\S]*?)(</style>)",
        lambda m: m.group(1) + tidy(strip_css(m.group(2))) + m.group(3),
        text,
    )
    text = re.sub(
        r"(<script[^>]*>)([\s\S]*?)(</script>)",
        lambda m: m.group(1) + tidy(strip_js(m.group(2))) + m.group(3),
        text,
    )
    return tidy(text)


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)

    built = []
    for base in ("layout", "pages", "system-pages"):
        for src in sorted((ROOT / base).rglob("*.html")):
            if "mockups" in src.parts:
                continue
            out = DIST / src.relative_to(ROOT)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(clean_html(src.read_text(encoding="utf-8")), encoding="utf-8")
            built.append(out)

    css_src = ROOT / "global-css" / "global.css"
    css_out = DIST / "global-css" / "global.css"
    css_out.parent.mkdir(parents=True, exist_ok=True)
    cleaned = tidy(strip_css(css_src.read_text(encoding="utf-8")))
    css_out.write_text(cleaned, encoding="utf-8")
    built.append(css_out)

    # sanity: brace balance must survive the strip
    if cleaned.count("{") != cleaned.count("}"):
        print("ERROR: global.css brace count changed after stripping", file=sys.stderr)
        return 1

    # ONE-PASTE SITE CHROME — header + footer + feedback pill in a single
    # gadget. Paste it at the BOTTOM of the page template (the footer's
    # slot): the header lifts itself to <body> and is position:fixed, the
    # pill floats, and the footer renders right where the gadget sits.
    # Replaces the three separate template gadgets.
    chrome = "\n\n".join(
        (DIST / rel).read_text(encoding="utf-8").strip()
        for rel in (
            "layout/header/01-top.html",
            "layout/footer/01-top.html",
            "layout/feedback-button/01-top.html",
        )
    ) + "\n"
    chrome_out = DIST / "layout" / "site-chrome" / "01-top.html"
    chrome_out.parent.mkdir(parents=True, exist_ok=True)
    chrome_out.write_text(chrome, encoding="utf-8")
    built.append(chrome_out)

    (DIST / "README.md").write_text(
        "# dist — production paste copies (GENERATED)\n\n"
        "Comment-free twins of every paste file. Paste into Wild Apricot\n"
        "from HERE. Never edit these — edit the sources and re-run\n"
        "`python3 ngm-website/tools/build-dist.py`.\n",
        encoding="utf-8",
    )
    print(f"dist built: {len(built)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
