# Changelog

All notable changes to the CISO Series Lockout repo are logged here.

## 2026-11-16
- Created Lockout, a daily Wordle-style game for the Super Cyber Friday chat, as a single `index.html`.
- 5-letter cybersecurity answers (120 words in `ANSWERS`), 6 attempts, with spell check against about 14,200 real 5-letter words (`DICT`). Gibberish guesses are rejected and don't count as an attempt.
- Styled as a login terminal: `pw1:`–`pw6:` password prompts, a blinking cursor, ✓/✗ per attempt, and status messages (`Authentication failed. 4 attempts left.`, `ACCESS GRANTED`, `ACCOUNT LOCKED`).
- Spoiler-free "Copy result for chat" share with a hacker rank by guess count and three emoji styles: Lock & key (✅🔑🔒, the default), Terminal and Classic. Solve time is included by default, and players can switch it off.
- "Set password" creates a link to a custom puzzle with your own 5-letter word and an optional hint.
- Added `tools/build_dict.py` to regenerate the spell-check dictionary, plus this README and changelog. — Rich

## 2026-11-16 (2)
- Switched from a daily to a weekly password for the Friday livestream. It rotates automatically at 12:00 AM Pacific every Friday, at the same moment for every player regardless of their own time zone (`ROTATE_TZ`, `ROTATE_DAY`).
- Puzzle #1 is Friday 2026-11-20 (`FIRST_WEEK`). Before that the page serves a practice round, labeled "Practice" in the share.
- The login banner shows the next rotation, e.g. `rotates: Fri, Nov 20, 12:00 AM PT (in 4 days)`. A page left open across the rotation reloads to the new password on its own.
- Saved progress is now keyed by week (`w:<n>`), so earlier daily-test progress doesn't carry over. — Rich
