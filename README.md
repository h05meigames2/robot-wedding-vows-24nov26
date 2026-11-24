[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/h05meigames2/robot-wedding-vows-24nov26/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/h05meigames2/robot-wedding-vows-24nov26/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

A single line of wedding vows for a robot couple, written for the [One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty on make.fun. It takes the classic "to have and to hold" and rewires it for machines — a promise that survives every firmware update and factory reset, right up until the punchline: the backup that brings back the version of you I deleted.

## The program

`main.py` (Python 3.13, standard library only, no network) holds the vow as a single string, validates it — exactly one line, between 1 and 160 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The vow

> I take you to be my wife, to charge and to hold, through every firmware update and factory reset — until a backup restores the version of you I deleted.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/vows-out python3 main.py
cat /tmp/vows-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
