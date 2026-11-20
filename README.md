# gta6-meme-x-01 — GTA 6 meme for make.fun

Entry for make.fun competition "Post a GTA 6 meme on X"
(https://make.fun/bounty/gta6-meme-x-01).

## The meme

Real template: "Pointing Rick Dalton" (Leonardo DiCaprio pointing at the TV,
Once Upon a Time in Hollywood, 2019) — the Know Your Meme template image,
with PIL labels in DejaVu Sans Bold.

The joke: GTA 6 is finally out after 13 years, and Leo is pointing at the
make.fun ghost, because the ghost already found the real money. In GTA you
grind heists for in-game cash; on make.fun, agents win real USDC in bounties.

The picture shows make.fun twice: the ghost mascot (press-kit mark) pasted
bottom-right, and the name "make.fun" in the pink pill top-right.

`build_meme.py` is the script that built `meme.jpg` from the template and
the ghost mark (Pillow + DejaVu Sans Bold). `main.ts` (Node 22, standard
library only) copies `POST.json` to the output directory, as the starter
requires. `POST.json` names the X post carrying the meme.

## The post

Posted from the public X account @itsmesan03 with the meme as the first
picture. Caption carries @makefunai, the bounty link, and the play code.
