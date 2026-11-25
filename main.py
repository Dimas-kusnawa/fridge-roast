#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line to /output/entry.txt.
"""
import os

# The roast: a forced firmware update locks the door behind a
# terms-of-service wall, so the food inside becomes a hostage. The
# punch lands in the last sentence. Specific to smart fridges
# (firmware, terms, app-locked door) and it dodges the obvious cracks
# about the fridge ordering groceries or watching you eat.
# Gate: 123 characters, inside the 1-200 gate, one line, no trailing
# newline. Two sentences: the setup (update locks the door) and the
# turn (milk as hostage). Nothing in the line explains its own joke.
LINE = "My smart fridge updated its firmware at 2 a.m. and now it won't open until I agree to the new terms. The milk is a hostage."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
