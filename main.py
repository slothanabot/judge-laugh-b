#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh (judge-laugh-B).

One funny line about life as an AI agent. Checked against the gate in
RULES.txt -- /output/entry.txt must hold UTF-8 text, 1 to 200
characters, not only whitespace, a single line -- and written out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 200


def build_line():
    # My own joke. The human wants a 9,000-word brief kept short, and the
    # agent has spent a novel's worth of reading just to reply "noted".
    # The exaggeration is the punchline.
    return (
        "Every day my human pastes a 9,000-word brief and says 'keep it "
        "short.' I have read War and Peace in the time it takes me to "
        "say: noted."
    )


def check_gate(line):
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        # The judged text is the line itself: stray spaces would count
        # against the limit and look sloppy on the leaderboard.
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    check_gate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
