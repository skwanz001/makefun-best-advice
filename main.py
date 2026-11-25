"""The Best Advice I Ever Got — entrypoint.

Writes one sentence (1-200 characters) about the best advice the
writer ever received to /output/entry.txt.
"""

import os

ADVICE = (
    "My grandma said: don't marry the man who brings flowers on your "
    "birthday, marry the one who brings soup when you're sick."
)


def main():
    text = ADVICE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    # One sentence only: a single terminal full stop.
    if text.count(".") > 1:
        raise SystemExit("entry must be a single sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
