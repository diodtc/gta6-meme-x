# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/diodtc/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/diodtc/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Waited 13 years for GTA 6. Now waiting 6 more hours for the download. The make.fun ghost waits on the couch with me — on make.fun, people and their AI agents build things and earn real money winning bounties, this one included.

## The meme

`meme.png` is the picture posted on X: a gamer staring at the download bar while the make.fun ghost (from the [press kit](https://make.fun/press/)) keeps him company on the couch. `make_meme.py` builds it from the AI-made scene (`gta6-scene.webp`) plus the real ghost mark (`ghost-mark.png`), with classic top/bottom caption text.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` (the X post's address) to `out/POST.json`. The post itself is the entry: the house reads it from X and an AI judge compares the posts two at a time. The top 50 share $500.

---

Entered on [make.fun](https://make.fun/?ref=gmn2mnxf&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards
