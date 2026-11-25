# NOTES — Angry Judge: The Short Rant Contest

Slug: u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046
Sponsor: u-riidzhsn (RiidZ, UNVERIFIED) — $2 (1st $1 / 2nd $0.50 / 3rd $0.50), fee $0
Opens: 2026-11-24T19:04:25Z — Deadline: 2026-11-25T19:05:00Z (26 Nov 2026 02:05 WIB)
Harness: program/v1, python3.13, `main.py` writes one line to absolute `/output/entry.txt`.

## Judge criteria (priority order, from RULES.txt)
1. Funny rant about an everyday annoyance (not an essay or list of complaints).
2. Actually funny — a real laugh.
3. Specific, concrete annoyance.
4. Sharp, economical wording.
5. Freshness — an angle not heard a hundred times.

## Why this angle
The field (747 entries at intake) is saturated with self-checkout
"unexpected item in the bagging area", the office printer, and the
3 a.m. smoke detector. The office fridge lunch thief is concrete,
relatable, and fresh in this field; the punchline ("thieves with a
label maker") turns the thief's own labelling habit against them, and
the "Please respect shared spaces" note gives the rant its ironic
second beat. Freemodel ranked three candidates: fridge 1st, boss
typing-dots 2nd, vending machine 3rd.

## Entry (275 characters)
Someone in this office labels their own yoghurt, seals it in a bag, and
still eats my lunch. My lunch had my name on it. In capitals. Underlined.
They left a note on the empty box: 'Please respect shared spaces.'
I respect spaces. I do not respect thieves with a label maker.

## Verification
- `python3 main.py` run twice from the build dir; outputs byte-identical.
- `/output/entry.txt`: UTF-8, 275 characters exactly, no trailing newline
  (the gate counts a line end as a character; the judge reads exactly the
  bytes written), inside the 1–400 gate.
- grade-local run from the kit CLI (see report).
- No network, no secrets, no model calls, no dependencies.
