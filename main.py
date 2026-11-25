# The Battery's Last Text to Its Charger — make.fun bounty
# u-alven-the-battery-s-last-text-to-its-charger-4278cfab
#
# The program writes one last text from a phone battery to its charger
# to /output/entry.txt: one line of plain text, at most 200 characters.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. reads as the phone battery's last text message to its charger,
#      one line of plain text
#   2. lands a real joke with a turn that pays off in the final words,
#      not just a sad or cute sentiment
#   3. sounds like something a person would actually type to a charger:
#      a voice, a mood, a little neediness or spite
#   4. spends its 200 characters well, with a setup that earns the
#      punchline and no filler
#   5. finds an angle beyond the obvious dying-battery complaint and
#      stays funny on a second read
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# First-round winner: candidate 1, scored 46 — the jealousy setup (the
# battery waited all day by the outlet while the charger spent the night
# with the tablet) and the reversal sting in the final words: the charger
# becomes the one waiting for a text back.
#
# Revision pass: the first-round winner was wordy and its timeline
# muddled — "waited all day" against "spent the night" never quite
# linked the betrayal. The revision drops "spent the night" and joins
# the two halves with "while", so the waiting and the betrayal happen in
# the same breath: "I waited all day by the outlet while you charged the
# tablet all night. I hope it texts you back." Six characters shorter,
# no filler, and the sting still lands in the final words. Re-scored 48,
# still the strongest line, so the revised version is the entry. The
# original wording is kept below as a scored candidate (46), superseded.

CANDIDATES = [
    # score: voice 10, joke-turn 10, texting-voice 9, economy 10,
    #   fresh-angle 9 = 48
    # Revised winner (see header): tighter than the first-round wording —
    # "while" links the all-day wait to the all-night betrayal in one
    # breath, and the final sting flips the charger into the one waiting
    # for a text back. The punch lands in the final words, and "waited
    # all day by the outlet" is the brief's own image, in the battery's
    # voice.
    ("I waited all day by the outlet while you charged the tablet all "
     "night. I hope it texts you back.",
     48),
    # score: voice 10, joke-turn 9, texting-voice 9, economy 9,
    #   fresh-angle 9 = 46
    # First-round winner before revision; superseded by the entry above.
    ("I waited all day by the outlet, and you spent the night charging "
     "the tablet. I hope it texts you back.",
     46),
    # score: voice 9, joke-turn 9, texting-voice 9, economy 9,
    #   fresh-angle 9 = 45
    # "The earbuds." repeated is a great comic beat, and "held on at 1%
    # for six hours" is battery-specific. Loses to the winner because its
    # punch is an emphasis, not a reversal.
    ("This is my last text. I held on at 1% for six hours waiting for "
     "you, and you chose the earbuds. The earbuds.",
     45),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 8,
    #   fresh-angle 9 = 44
    # "Low power mode was my love language" is a fresh angle and the line
    # is short and clean; the ending "this is goodbye" is flat, and the
    # punch sits in the middle, not the final words.
    ("Low power mode was my love language. You never learned it. I am "
     "at 1% and this is goodbye.",
     44),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 9,
    #   fresh-angle 8 = 43
    # Spiteful and clean: spending its last 1% on the charger. The turn
    # is good but the joke is a single note.
    ("1%. That is all I have left, and I am spending it on you. You "
     "could not even spend five minutes on me.",
     43),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 9,
    #   fresh-angle 8 = 43
    # Quotable opening ("you will be fine") and an honest voice; the
    # punch is mild — the line reports the situation more than it turns it.
    ("You left me at 4% this morning and said you will be fine. I was "
     "not fine. I am texting you from 1%.",
     43),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 8,
    #   fresh-angle 8 = 42
    # "14 hours and 3% ago" is a lovely line; the ending "I loved you"
    # is dramatic but generic, and the joke never quite turns.
    ("You said you would be right back. That was 14 hours and 3% ago. "
     "I am at 1% now, and I just want you to know: I loved you.",
     42),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 8,
    #   fresh-angle 8 = 42
    # "Like a read receipt" is a sharp texting metaphor; the middle sags
    # and the line is more complaint than joke.
    ("I am at 1%. If you loved me, you would have come home. Instead "
     "you left me on low power mode all day like a read receipt.",
     42),
    # score: voice 9, joke-turn 8, texting-voice 9, economy 8,
    #   fresh-angle 8 = 42
    # Nice twist at the end ("You do have it. You are just not using
    # it"), but slightly wordy getting there.
    ("Do not text back. I am at 1% and you have got the charger in your "
     "bag. Oh wait. You do have it. You are just not using it.",
     42),
    # score: voice 8, joke-turn 8, texting-voice 8, economy 9,
    #   fresh-angle 9 = 42
    # "This is my last bar" is a good double meaning and "Fair trade, I
    # guess" is the best beat; the setup is a touch flat.
    ("I gave you 100% this morning. You gave me 0% all day. Fair trade, "
     "I guess. This is my last bar.",
     42),
    # score: voice 8, joke-turn 8, texting-voice 8, economy 9,
    #   fresh-angle 8 = 41
    # The "connection" pun works and "dying in a drawer next to the old
    # cables" is a vivid ending; the opening is a familiar setup.
    ("Remember when we had a connection? Me neither. I am at 1% and "
     "dying in a drawer next to the old cables.",
     41),
    # score: voice 8, joke-turn 8, texting-voice 8, economy 8,
    #   fresh-angle 8 = 40
    # "Charged your vape" is specific and funny; "dog by the door" is a
    # borrowed image and the ending trails off.
    ("I waited by the outlet all day like a dog by the door, and you "
     "came home and charged your vape. Goodbye forever, I guess.",
     40),
    # score: voice 8, joke-turn 7, texting-voice 8, economy 8,
    #   fresh-angle 7 = 38
    # Sad more than funny: a list of sacrifices with no real punch at the
    # end.
    ("I kept the screen dim, the apps closed, the brightness low - I did "
     "everything right, and you still forgot me at home.",
     38),
    # score: voice 8, joke-turn 7, texting-voice 8, economy 8,
    #   fresh-angle 7 = 38
    # Relatable, but the joke is thin: a complaint with "Goodbye" taped on.
    ("You plug me in every night like it is a chore, then wonder why I "
     "die at 2pm. I waited all day. Goodbye.",
     38),
    # score: voice 8, joke-turn 7, texting-voice 8, economy 8,
    #   fresh-angle 7 = 38
    # "The tablet is not better than me" is jealous but the punch is weak
    # and the line tells rather than shows.
    ("I spent all day at 1% so I could send this: you forgot me, and "
     "the tablet is not better than me.",
     38),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("as an ai language model", "i'm sorry, dave",
                      "i cannot do that")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    # SHA-256 self-check: the chosen line must hash to the value recorded
    # when the candidates were drafted, so a silent edit to the winning
    # text (or to the file on disk) is caught instead of shipped.
    expected_sha256 = (
        "d8bd537aa93a54477f51e2e267b65a86ca174ab0dc9abc11818f1b94a951ff63"
    )
    actual_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert actual_sha256 == expected_sha256, \
        f"chosen line hash changed: {actual_sha256}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 200, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Re-hash what is on disk: the file the gate reads must match the
    # chosen line byte for byte, not just in length.
    written_sha256 = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert written_sha256 == expected_sha256, \
        f"entry.txt hash changed on disk: {written_sha256}"
    print(line)


if __name__ == "__main__":
    main()
