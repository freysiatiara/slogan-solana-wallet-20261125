"""One-line slogan for a Solana wallet agent.

Writes the chosen slogan to /output/entry.txt.
Standard library only; no network access.
"""

import os

ENTRY = "Ask your wallet. It answers in Solana."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140
MAX_WORDS = 20


def _validate_entry(text):
    """Check the slogan meets the competition gate and judge limits."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-140 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text.split()) > MAX_WORDS:
        raise ValueError("entry must be at most 20 words")
    return text


def main():
    entry = _validate_entry(ENTRY)
    if "Solana" not in entry:
        raise ValueError("entry must name or clearly evoke Solana")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip guard: the file on disk must be byte-identical to the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise ValueError("written entry does not match the validated entry")


if __name__ == "__main__":
    main()
