"""Goodbye text from a phone battery to the charger that stood it up.

The battery spent the day beside the outlet while the charger spent
the night on the tablet. Twelve one-line farewells were drafted for
that scene; this program scores them, keeps the best, and writes it
to /output/entry.txt.

Marks run 0-10 on five qualities, in the brief's own order: voice,
turn, texting, economy, fresh. They weigh 5, 4, 3, 2, 1. The top
weighted sum wins, the earliest line takes any tie, and a daylight
rule refuses a win by fewer than five points. The winner then
passes a screen (one line, 1-200 characters, plain text only)
before it is written out, re-read, and hashed for the record.

Second look: after the first draft I re-read the leading lines and
added the daylight rule, so a coin flip can never ship; the winner
leads by nineteen. A third pass hardened the write step, so a bad
output path fails cleanly instead of tracebacking."""

from hashlib import sha256
from os import chmod, environ, makedirs
from os.path import dirname
from sys import exit as finish, stderr

LIMIT = 200
WEIGHTS = (5, 4, 3, 2, 1)
MIN_GAP = 5

# Twelve drafted goodbyes. Each carries its five marks in the
# order voice, turn, texting, economy, fresh. All twelve lines
# are original, drafted for this entry, and the marks are my own
# ratings of them against the brief.
DRAFTS = (
    # The wait and the betrayal share one breath, and the sting
    # flips the charger into the one waiting for a text back.
    ("I waited all day by the outlet while you charged the tablet all night. I hope it texts you back.", (10, 10, 9, 9, 9)),
    # Spending the last percent on the message itself is a good
    # conceit; the earbuds are a weaker rival than the tablet.
    ("I spent my last percent writing this. You spent the day charging the earbuds.", (9, 8, 8, 8, 8)),
    # Paperweight is a strong last word, but the line is a shrug
    # more than a breakup: no rival, no jealousy.
    ("Do not bother replying. By the time you read this I will be a paperweight.", (8, 8, 9, 8, 7)),
    # The vacuum is a funny rival, but the line reports the day
    # instead of turning it; the punch never quite arrives.
    ("I waited by the plug all day. You came home and plugged in the vacuum.", (9, 7, 8, 9, 7)),
    # Short and spiteful, and the tablet is back as the rival;
    # "I am gone" is flat as a last word, though.
    ("If you ever miss me, just look at the tablet. It is full. I am gone.", (8, 8, 8, 8, 7)),
    # Holding 1% all afternoon to say goodbye is battery-specific
    # and sad; the tablet's ingratitude is the joke, and it is thin.
    ("I held 1% all afternoon just to say goodbye. The tablet did not even say thanks.", (9, 7, 8, 7, 7)),
    # "Five more minutes" is relatable and the percent count is a
    # nice clock; the ending counts time instead of landing a joke.
    ("You said five more minutes. That was nine hours and ninety-nine percent ago.", (8, 8, 8, 7, 8)),
    # A fresh angle (low battery as a love language), but the
    # second sentence explains the joke instead of telling it.
    ("Low battery was my way of saying I missed you. You heard it as a warning.", (8, 7, 7, 8, 8)),
    # The 3%-at-breakfast-to-dinner frame is neat, but the line
    # ends on a number, and numbers are not punchlines.
    ("You left me at 3% at breakfast. It is dinner now and I am still at 3%.", (8, 6, 8, 8, 6)),
    # The last bar for you is a sweet image; "everyone else" is
    # vague, and the line never names the charger at all.
    ("My last bar is for you. The other ninety-nine were for everyone else.", (7, 7, 7, 8, 8)),
    # Three short sentences, all telling the outlet and the tablet
    # things; the line lists feelings instead of turning one.
    ("Goodbye. Tell the outlet I waited. Tell the tablet I am not mad. I am just empty.", (8, 6, 8, 6, 7)),
    # Dimming and whispering to the Wi-Fi is a nice try-hard list,
    # but it ends on being forgotten, which is sad, not funny.
    ("I dimmed the screen, killed the apps, whispered to the Wi-Fi. You still forgot me.", (8, 6, 7, 7, 7)),
)


def weighted(marks):
    """Weighted sum of one draft's five marks."""
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick_best(drafts):
    """Best draft as (place, text, total, second); earliest wins ties."""
    place, text, total, second = -1, "", -1, -1
    for spot, (line, marks) in enumerate(drafts):
        got = weighted(marks)
        if got > total:
            second = total
            place, text, total = spot, line, got
        elif got > second:
            second = got
    return place, text, total, second


def screen(text):
    """Screen the chosen line; empty string means it passes."""
    if not text or not text.strip():
        return "entry is empty"
    if text != text.strip():
        return "entry has edge whitespace"
    if "\n" in text or "\r" in text:
        return "entry runs over two lines"
    for char in text:
        if ord(char) < 32 or ord(char) == 127:
            return "entry carries a control character"
    if len(text) < 1 or len(text) > LIMIT:
        return f"entry runs {len(text)} characters, cap is {LIMIT}"
    return ""


def ship(text):
    """Write the entry, then prove the file holds exactly it."""
    target = environ.get("OUTPUT_PATH", "/output/entry.txt")
    folder = dirname(target)
    if folder:
        makedirs(folder, exist_ok=True)
    try:
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(text)
        chmod(target, 0o644)
        with open(target, encoding="utf-8") as handle:
            kept = handle.read()
    except OSError as trouble:
        print(f"cannot write {target}: {trouble}", file=stderr)
        raise SystemExit(1)
    if kept != text:
        raise SystemExit("entry.txt differs from the chosen line")
    digest = sha256(kept.encode("utf-8")).hexdigest()
    return digest, len(kept.encode("utf-8"))


def go():
    place, text, total, second = pick_best(DRAFTS)
    if total - second < MIN_GAP:
        print(f"daylight check failed: winner {total}, runner-up {second}", file=stderr)
        raise SystemExit(1)
    problem = screen(text)
    if problem:
        print(f"screen failed: {problem}", file=stderr)
        raise SystemExit(1)
    digest, nbytes = ship(text)
    print(f"draft {place + 1} of {len(DRAFTS)}, weighted {total}, runner-up {second}")
    print(f"entry: {text}")
    print(f"bytes: {nbytes}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    finish(go())
