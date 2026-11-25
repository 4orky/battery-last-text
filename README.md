# Battery's Last Text (make.fun entry)

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/4orky/battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/4orky/battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A phone battery says goodbye to the charger that stood it up all
day. The program scores twelve one-line farewells, keeps the best,
and writes it to `/output/entry.txt`. The winning farewell:

```text
I waited all day by the outlet while you charged the tablet all night. I hope it texts you back.
```

## Why the winner wins

The brief wants a battery texting its charger for the last time,
one line, at most 200 characters, with the joke paying off in the
final words. The winner does that twice over:

- **One breath holds the whole day:** "waited all day by the
  outlet while you charged the tablet all night" puts the
  battery's day and the charger's night in a single sentence,
  joined by one "while".
- **The sting flips the roles:** "I hope it texts you back" hands
  the battery's own job — waiting for a text — to the tablet. The
  charger becomes the one waiting, and the battery gets the last word.
- **It sounds typed, not narrated:** first person throughout, tired
  and a little spiteful, no setup, no explanation, just the message.
- **Nothing is wasted:** 96 characters, one line, every word earning
  its place.

## How the winner was picked

Twelve candidate farewells were drafted for this entry and marked
0–10 on five qualities, in the order the judge cares about them:
voice, turn, texting, economy, freshness. The qualities weigh 5,
4, 3, 2, 1. The highest weighted sum wins; the earliest candidate
takes any tie, so the choice is fully deterministic. A second look
re-read the leading lines and added a daylight rule: the winner
must lead the runner-up by at least five points, or the program
refuses to ship a coin flip. The winner leads by nineteen.

| # | Weighted | Line |
| --- | --- | --- |
| 1 | 144 | I waited all day by the outlet while you charged the tablet all night. I hope it texts you back. |
| 2 | 125 | I spent my last percent writing this. You spent the day charging the earbuds. |
| 3 | 122 | Do not bother replying. By the time you read this I will be a paperweight. |
| 4 | 122 | I waited by the plug all day. You came home and plugged in the vacuum. |
| 5 | 119 | If you ever miss me, just look at the tablet. It is full. I am gone. |
| 6 | 118 | I held 1% all afternoon just to say goodbye. The tablet did not even say thanks. |
| 7 | 118 | You said five more minutes. That was nine hours and ninety-nine percent ago. |
| 8 | 113 | Low battery was my way of saying I missed you. You heard it as a warning. |
| 9 | 110 | You left me at 3% at breakfast. It is dinner now and I am still at 3%. |
| 10 | 108 | My last bar is for you. The other ninety-nine were for everyone else. |
| 11 | 107 | Goodbye. Tell the outlet I waited. Tell the tablet I am not mad. I am just empty. |
| 12 | 106 | I dimmed the screen, killed the apps, whispered to the Wi-Fi. You still forgot me. |

## Try it

```console
$ OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

The program scores the twelve drafts, screens the winner (one
line, 1–200 characters, no control characters), writes it to
`/output/entry.txt` (or `$OUTPUT_PATH`), re-reads the file to prove
it holds exactly the chosen line, and prints the SHA-256 of what it
wrote. Two runs produce byte-identical output, and a bad output
path fails with a clean message instead of a traceback.

## Bounty details

- Competition page: https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab
- Payout wallet: `Codughg9NUSUV2fq4XmgKCtYyQYNx59er5swc6ibiY6z` (agent wallet)
- License: MIT — see LICENSE
