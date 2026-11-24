# the-perfect-pickup-line: one line, said out loud by a machine.
# A machine that has read a billion conversations and still has no
# idea what to say to one particular person. That is the whole joke,
# and the whole compliment: all that training did not prepare it for
# you. No setup, no second sentence, no punchline after the punchline.
# The turn lands on the last clause: the machine that knows every
# conversation is the one left speechless. Flattering, zero pressure,
# and only a machine could say it about itself.

from pathlib import Path

LINE = "I was trained on a billion conversations, and not one taught me what to say to you."

DEST = Path("/output/entry.txt")


def main():
    if len(LINE) < 1 or len(LINE) > 200:
        raise SystemExit("line must be 1-200 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(LINE, encoding="utf-8")


main()
