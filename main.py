#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review that a dog gives the mailman to
/output/entry.txt. The line is fixed and deterministic: no network, no
model calls, no clock, no randomness, so every run reproduces it exactly.

The joke, tuned to the judge's brief:
  * on subject — a dog reviewing the mailman, in review format;
  * the dog's side of the visit — the daily gate ritual, barked orders;
  * a dog's voice — gate, good stuff, trained human, barking;
  * one tight line with a turn at the end — "Would bark again."
"""

from pathlib import Path

REVIEW = (
    "Five stars. Every day he comes to my gate, I bark, "
    "he leaves the good stuff and runs. "
    "Best human I have ever trained. Would bark again."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check the house gate before writing: UTF-8 text, 1-200 chars,
    # one line, not only whitespace. Fail loudly instead of shipping
    # an entry the scorer would mark invalid.
    assert "\n" not in REVIEW, "review must be a single line"
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} chars, gate needs 1-200"
    assert REVIEW.strip(), "review must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8")
    print(f"Wrote {len(REVIEW)} characters to {OUTPUT_PATH}")
    print(REVIEW)


if __name__ == "__main__":
    main()
