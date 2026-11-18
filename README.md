# Lockout

A weekly Wordle-style game for the Super Cyber Friday (SCF) live chat. Players crack a 5-letter cybersecurity "password" in 6 attempts before the account locks, then paste a spoiler-free score into the chat.

Live version: https://claude.ai/artifact/5cQK1fATHvjf3rgDP8G1Yi

## How it works

- **One file.** Everything is in `index.html`: the game, the answer list and the spell-check dictionary. No build step or server; open it in a browser.
- **Weekly puzzle.** The password rotates automatically at **12:00 AM Pacific every Friday**, the same moment for every player wherever they are. Puzzle #1 is Friday 2026-11-20 (`FIRST_WEEK`). Each week takes the next word from `ANSWERS`, then the list loops (120 words, a bit over two years). Before #1 the page serves a practice round. A page left open across the rotation switches itself to the new password within a minute.
- **Spell check.** Guesses must be in `DICT`, about 14,200 five-letter words. Every answer is also always accepted.
- **Custom puzzles.** "Set password" builds a link like `…#p-<hex>` that opens a puzzle with your own word and an optional hint. The word is hex-encoded, not secret.
- **Sharing.** "Copy result for chat" copies the score in one of three styles (Lock & key, the default; Terminal; Classic), with an optional solve time. It never includes the answer.
- **Saved locally.** Progress and preferences live in the player's browser (`localStorage`). Nothing is sent anywhere.

## Common edits

| To change | Edit in `index.html` |
|---|---|
| Weekly answers or their order | `ANSWERS` (5 uppercase letters each, one per week) |
| Date of puzzle #1 | `FIRST_WEEK` |
| Rotation day or time zone | `ROTATE_DAY` (0=Sun … 5=Fri), `ROTATE_TZ` and `ROTATE_TZ_LABEL` |
| Rank titles | `RANKS` (index 0 = solved in 1 guess) |
| Share emoji styles | `STYLES` |
| Link included in the share | `BASE` |

If players report a real word being rejected, add it to `MODERN` in `tools/build_dict.py` and run:

```bash
python3 tools/build_dict.py
```

That rewrites the `DICT` line in `index.html` from the macOS dictionary (`/usr/share/dict/web2`).

## Publishing

The live link is a Claude artifact. The artifact copy is `index.html` with the `<!doctype>`, `<html>`, `<head>`/`<body>` wrapper and the charset/viewport tags removed, because the artifact host adds its own. Update the artifact by republishing to the same URL so the share link stays the same.

## Next-event promo

When a game ends, the page promotes the next Super Cyber Friday with a link to its Crowdcast page. The event is stored in the `scf-event` block of `index.html`; update it with `python3 tools/set_event.py --name "Hacking ..." --url https://www.crowdcast.io/c/... --date YYYY-MM-DD` (or `--clear`). A local Claude scheduled task (`scf-games-event-promo`) does this every Friday at 3 PM ET from ClickUp, then republishes the artifact and pushes. The promo hides itself after 3 PM ET on the show day.
