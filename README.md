# Lockout

A daily Wordle-style game for the Super Cyber Friday (SCF) live chat. Players crack a 5-letter cybersecurity "password" in 6 attempts before the account locks, then paste a spoiler-free score into the chat.

Live version: https://claude.ai/artifact/5cQK1fATHvjf3rgDP8G1Yi

## How it works

- **One file.** Everything is in `index.html`: the game, the answer list and the spell-check dictionary. No build step or server; open it in a browser.
- **Daily puzzle.** Puzzle #1 was 2026-11-16 (`START` in the script). Each day takes the next word from `ANSWERS`, then the list loops (120 words, about four months).
- **Spell check.** Guesses must be in `DICT`, about 14,200 five-letter words. Every answer is also always accepted.
- **Custom puzzles.** "Set password" builds a link like `…#p-<hex>` that opens a puzzle with your own word and an optional hint. The word is hex-encoded, not secret.
- **Sharing.** "Copy result for chat" copies the score in one of three styles (Lock & key, the default; Terminal; Classic), with an optional solve time. It never includes the answer.
- **Saved locally.** Progress and preferences live in the player's browser (`localStorage`). Nothing is sent anywhere.

## Common edits

| To change | Edit in `index.html` |
|---|---|
| Daily answers or their order | `ANSWERS` (5 uppercase letters each) |
| Start date / puzzle numbering | `START` |
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
