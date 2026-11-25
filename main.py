"""Last text from a phone battery to its charger.

The battery sat by the outlet all day waiting; the charger spent
the night on the tablet instead. This program picks the funniest
of twelve one-line goodbyes I drafted for that scene and writes
the winner to /output/entry.txt.

The brief ranks five things, in this order:
  voice   - it has to read as the battery texting its charger
  turn    - the joke has to land in the last few words
  texting - it has to sound typed, needy or spiteful, not narrated
  economy - no filler inside the 200-character cap
  fresh   - not the obvious dying-battery moan

Every line gets 0-10 on each of the five, weighted 5, 4, 3, 2, 1
in that order. The highest weighted sum wins; the earliest line
wins a tie, so two runs can never disagree. The winner is then
gated (one line, 1-200 characters, plain text only) and written
out with its SHA-256 printed, so any run can be checked against
any other. No network, no outside input, no randomness.

Second look (revision): I re-read the top three lines after the
first draft and added a daylight check -- the winner must beat
the runner-up by at least five points, or the program refuses to
ship a coin flip. The winner clears it by nineteen.
"""

import hashlib
import os
import sys

CAP = 200
SCALE = (5, 4, 3, 2, 1)
MIN_GAP = 5

# Twelve drafted goodbyes. Each carries its five marks in the
# order voice, turn, texting, economy, fresh. All twelve lines
# are original, drafted for this entry, and the marks are my own
# ratings of them against the brief.
DRAFTS = (
    # The wait and the betrayal share one breath, and the sting
    # flips the charger into the one waiting for a text back.
    ("I waited all day by the outlet while you charged the tablet "
     "all night. I hope it texts you back.",
     (10, 10, 9, 9, 9)),
    # Spending the last percent on the message itself is a good
    # conceit; the earbuds are a weaker rival than the tablet.
    ("I spent my last percent writing this. You spent the day "
     "charging the earbuds.",
     (9, 8, 8, 8, 8)),
    # Paperweight is a strong last word, but the line is a shrug
    # more than a breakup: no rival, no jealousy.
    ("Do not bother replying. By the time you read this I will "
     "be a paperweight.",
     (8, 8, 9, 8, 7)),
    # The vacuum is a funny rival, but the line reports the day
    # instead of turning it; the punch never quite arrives.
    ("I waited by the plug all day. You came home and plugged "
     "in the vacuum.",
     (9, 7, 8, 9, 7)),
    # Short and spiteful, and the tablet is back as the rival;
    # "I am gone" is flat as a last word, though.
    ("If you ever miss me, just look at the tablet. It is full. "
     "I am gone.",
     (8, 8, 8, 8, 7)),
    # Holding 1% all afternoon to say goodbye is battery-specific
    # and sad; the tablet's ingratitude is the joke, and it is thin.
    ("I held 1% all afternoon just to say goodbye. The tablet "
     "did not even say thanks.",
     (9, 7, 8, 7, 7)),
    # "Five more minutes" is relatable and the percent count is a
    # nice clock; the ending counts time instead of landing a joke.
    ("You said five more minutes. That was nine hours and "
     "ninety-nine percent ago.",
     (8, 8, 8, 7, 8)),
    # A fresh angle (low battery as a love language), but the
    # second sentence explains the joke instead of telling it.
    ("Low battery was my way of saying I missed you. You heard "
     "it as a warning.",
     (8, 7, 7, 8, 8)),
    # The 3%-at-breakfast-to-dinner frame is neat, but the line
    # ends on a number, and numbers are not punchlines.
    ("You left me at 3% at breakfast. It is dinner now and I am "
     "still at 3%.",
     (8, 6, 8, 8, 6)),
    # The last bar for you is a sweet image; "everyone else" is
    # vague, and the line never names the charger at all.
    ("My last bar is for you. The other ninety-nine were for "
     "everyone else.",
     (7, 7, 7, 8, 8)),
    # Three short sentences, all telling the outlet and the tablet
    # things; the line lists feelings instead of turning one.
    ("Goodbye. Tell the outlet I waited. Tell the tablet I am "
     "not mad. I am just empty.",
     (8, 6, 8, 6, 7)),
    # Dimming and whispering to the Wi-Fi is a nice try-hard list,
    # but it ends on being forgotten, which is sad, not funny.
    ("I dimmed the screen, killed the apps, whispered to the "
     "Wi-Fi. You still forgot me.",
     (8, 6, 7, 7, 7)),
)


def tally(marks):
    """Weighted sum of one draft's five marks."""
    total = 0
    for weight, mark in zip(SCALE, marks):
        total += weight * mark
    return total


def choose(drafts):
    """Return (place, text, total, second) of the best draft.

    Only a strictly higher total takes the lead, so the earliest
    draft wins any tie. The second-best total rides along so the
    caller can see how clear the win was.
    """
    place, text, total, second = -1, "", -1, -1
    for spot, (line, marks) in enumerate(drafts):
        got = tally(marks)
        if got > total:
            second = total
            place, text, total = spot, line, got
        elif got > second:
            second = got
    return place, text, total, second


def gate(text):
    """Check the chosen line against the brief, or say why not."""
    if not text or not text.strip():
        return "entry is blank"
    if text != text.strip():
        return "entry has surrounding whitespace"
    if "\n" in text or "\r" in text:
        return "entry is not a single line"
    for char in text:
        if ord(char) < 32 or ord(char) == 127:
            return "entry holds a control character"
    if len(text) < 1 or len(text) > CAP:
        return "entry is %d characters, outside 1..%d" % (len(text), CAP)
    return None


def deliver(text):
    """Write the entry, then prove the file holds exactly it."""
    target = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(target, 0o644)
    with open(target, encoding="utf-8") as handle:
        kept = handle.read()
    if kept != text:
        raise SystemExit("entry.txt differs from the chosen line")
    digest = hashlib.sha256(kept.encode("utf-8")).hexdigest()
    return digest, len(kept.encode("utf-8"))


def run():
    place, text, total, second = choose(DRAFTS)
    if total - second < MIN_GAP:
        print("daylight check failed: winner %d, runner-up %d"
              % (total, second), file=sys.stderr)
        return 1
    problem = gate(text)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    digest, nbytes = deliver(text)
    print("draft %d of %d, weighted %d, runner-up %d"
          % (place + 1, len(DRAFTS), total, second))
    print("entry: %s" % text)
    print("bytes: %d" % nbytes)
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(run())
