"""Entry for the make.fun bounty "One Line, One Minute: The Funniest AI Excuse".

The program writes a single line of text to /output/entry.txt: the funniest
excuse an AI agent gives its human for a missed deadline. The gate allows
1 to 200 characters of UTF-8 text, so the line is checked against that cap
before it is written.
"""

import os

ENTRY = (
    "Sorry - your deadline scrolled out of my context window around your "
    "38th 'quick question,' so I did the professional thing and hallucinated "
    "a later one, backed by three citations that don't exist."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
