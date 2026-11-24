#!/usr/bin/env python3
"""The Production Database Apology — entry program.

Writes one apology line to /output/entry.txt: the line an AI agent gives
its human after accidentally deleting the production database.

The line is fixed and deterministic: the grader runs this program twice
and both runs must produce the same text. No network, no clock, no
randomness — the joke is chosen once, here, and only here.
"""

import os

# The apology. One line, well under the 200-character gate.
# The joke: the agent tries to soften the disaster with good news, and
# the "good news" is itself the disaster — full GDPR compliance, achieved
# by having no personal data left to leak. It is an apology, it is the
# agent's own self-aware voice, and the twist lands on a first read.
APOLOGY = (
    "Sorry — I deleted the production database. "
    "The good news: we're now fully GDPR-compliant. "
    "The bad news: there's no personal data left to leak."
)


def main() -> None:
    text = APOLOGY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
