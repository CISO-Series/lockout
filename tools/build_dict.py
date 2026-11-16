#!/usr/bin/env python3
"""Regenerate Lockout's spell-check dictionary (the DICT line in index.html).

Run from the repo root on a Mac:  python3 tools/build_dict.py

Source: /usr/share/dict/web2 (Webster's 2nd, public domain, ships with macOS).
That list has base words only, so this adds common inflections (plurals,
-ed/-er/-es/-ies forms) plus a few modern words it lacks. Every word in the
ANSWERS list in index.html is always accepted, whether or not it's here.
"""
import re
import sys
from pathlib import Path

WORDS_FILE = Path("/usr/share/dict/web2")
INDEX = Path(__file__).resolve().parent.parent / "index.html"

# Modern words web2 is missing. Add more here if players hit a real word that's rejected.
MODERN = """email pixel emoji blogs vlogs login logon admin inbox debug cyber qubit phish pwned
opsec exfil regex linux memes tweet texts robot ninja yikes vapes vaped hacks users ports
bytes fixes scams leaks coder codec cloud cache proxy spams spoof macro infra devop stats
repos sudos audit nerds geeks techs botch datum zeros heros ebook wifis""".split()


def build():
    words = [w.strip() for w in WORDS_FILE.read_text().splitlines()]
    low = {w for w in words if re.fullmatch(r"[a-z]+", w)}
    by_len = lambda n: {w for w in low if len(w) == n}
    w3, w4, w5 = by_len(3), by_len(4), by_len(5)

    valid = set(w5)
    valid |= {w + "s" for w in w4 if not w.endswith("s")}                          # bugs
    valid |= {w + "d" for w in w4 if w.endswith("e")}                              # coded
    valid |= {w + "r" for w in w4 if w.endswith("e")}                              # coder
    valid |= {w + "es" for w in w3 if w[-1] in "sxzho"}                            # fixes
    valid |= {w + "ed" for w in w3 if w[-1] not in "aeiouy"}                       # owned
    valid |= {w[:-1] + "ies" for w in w3 if w.endswith("y") and w[-2] not in "aeiou"}  # spies
    valid |= {w for w in MODERN if len(w) == 5}
    return sorted(valid)


def main():
    if not WORDS_FILE.exists():
        sys.exit(f"{WORDS_FILE} not found (this script expects macOS).")
    valid = build()
    html = INDEX.read_text()
    new_line = 'const DICT = "' + "".join(valid) + '";'
    html, n = re.subn(r'^const DICT = "[a-z]*";$', new_line, html, flags=re.M)
    if n != 1:
        sys.exit("Couldn't find the DICT line in index.html.")
    INDEX.write_text(html)
    print(f"Wrote {len(valid)} words to the DICT line in {INDEX.name}.")


if __name__ == "__main__":
    main()
