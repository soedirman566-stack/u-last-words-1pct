[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/soedirman566-stack/u-last-words-1pct/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/soedirman566-stack/u-last-words-1pct/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

# I Choose This

An entry for make.fun's **Famous Last Words at 1 Percent**: the last
words a phone says as its battery hits 1 percent, a single line of
69 characters.

> Do not resuscitate. I've seen your search history, and I choose this.

## How it runs

`main.py` is the entrypoint. It reads the line from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 199 characters), and writes
it to `/output/entry.txt`, where the harness picks it up. It also prints
the line to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the phone's last words, exactly as judged.
- `LICENSE` — MIT.
