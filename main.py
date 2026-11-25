"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about a small everyday annoyance to
/output/entry.txt. The rant is fixed text: the program is deterministic,
makes no network calls, reads no files, and needs no secrets.

The rant (275 characters, inside the 1-400 gate):
an office fridge lunch thief who labels their own yoghurt, seals it in
a bag, and still eats the narrator's labelled lunch — then leaves a
passive-aggressive note about respecting shared spaces.
"""

import os

ENTRY = (
    "Someone in this office labels their own yoghurt, seals it in a bag, "
    "and still eats my lunch. My lunch had my name on it. In capitals. "
    "Underlined. They left a note on the empty box: 'Please respect shared "
    "spaces.' I respect spaces. I do not respect thieves with a label maker."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
