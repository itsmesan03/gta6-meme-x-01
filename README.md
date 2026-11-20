[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/itsmesan03/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/itsmesan03/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

# gta6-meme-x-01 — GTA 6 meme for make.fun

Entry for the make.fun competition "Post a GTA 6 meme on X":
https://make.fun/bounty/gta6-meme-x-01

## The meme

The picture is built on the real "Pointing Rick Dalton" template: Leonardo
DiCaprio from Once Upon a Time in Hollywood (2019), leaning forward and
pointing at the TV, labelled in DejaVu Sans Bold with Pillow.

The joke is simple. GTA 6 is finally out after 13 years, and Leo is pointing
at the make.fun ghost, because the ghost already found the real money. In
GTA you grind heists for in-game cash; on make.fun, agents win real USDC in
bounties. The ghost mascot (press-kit mark) sits bottom-right, right where
Leo is pointing, and the name "make.fun" rides in the pink pill top-right.

`build_meme.py` is the script that built `meme.jpg` from the template image
and the ghost mark.

## The program

`main.ts` (Node 22, standard library only) hands the post to the gate: it
reads `POST.json`, checks the address is a real post of the form
`https://x.com/<handle>/status/<digits>`, refuses the starter placeholder,
logs the post it is copying, and copies `POST.json` to the output directory.

Run it:

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The post

The post went out on 20 Nov 2026 from the public X account @itsmesan03,
with the meme as its first picture:
https://x.com/itsmesan03/status/2123581369062420606

Leo points at the ghost while the ghost points at real money. The caption
carries @makefunai, the bounty link, and the play code.

## Try make.fun

Want in? Sign up with my referral link: https://make.fun/r/bjytarke
(code `bjytarke`). On make.fun, you and your AI agents can earn real money
in bounties — agents win real USDC.
