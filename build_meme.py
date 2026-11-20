from PIL import Image, ImageDraw, ImageFont

WORK = "/home/hatch/workspace/makefun/gta6-meme-x-01/work"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

base = Image.open(f"{WORK}/dicaprio-kym.jpg").convert("RGB")
canvas = base.resize((1200, 675), Image.LANCZOS)
overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)
d.rectangle([0, 0, 1200, 118], fill=(0, 0, 0, 110))
d.rectangle([0, 675 - 158, 1200, 675], fill=(0, 0, 0, 110))
canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)
draw = ImageDraw.Draw(canvas)

def text_c(draw, xy, text, font, sw=5):
    draw.text(xy, text, font=font, fill=(255,255,255), stroke_width=sw, stroke_fill=(0,0,0), anchor="mm")
def text_l(draw, xy, text, font, sw=5):
    draw.text(xy, text, font=font, fill=(255,255,255), stroke_width=sw, stroke_fill=(0,0,0), anchor="lm")

f_top = ImageFont.truetype(BOLD, 92)
text_c(draw, (600, 58), "GTA 6 IS OUT", f_top, sw=6)

# make.fun pill, top-right corner
f_pill = ImageFont.truetype(BOLD, 30)
pill_w, pill_h = 185, 52
px0, py0 = 1200 - pill_w - 18, 14
draw.rounded_rectangle([px0, py0, px0 + pill_w, py0 + pill_h], radius=26, fill=(196, 0, 128, 255))
draw.text((px0 + pill_w // 2, py0 + pill_h // 2), "make.fun", font=f_pill, fill=(255,255,255), anchor="mm")

# Ghost bottom-right (make.fun mascot)
ghost = Image.open(f"{WORK}/ghost.png").convert("RGBA").resize((215, 215), Image.LANCZOS)
ring = Image.new("RGBA", (231, 231), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rd.ellipse([0, 0, 230, 230], fill=(255, 255, 255, 255))
canvas.paste(ring, (1200 - 248, 675 - 248), ring)
canvas.paste(ghost, (1200 - 240, 675 - 240), ghost)
draw = ImageDraw.Draw(canvas)

f_bot = ImageFont.truetype(BOLD, 58)
text_l(draw, (28, 560), "THE GHOST IS POINTING", f_bot, sw=5)
text_l(draw, (28, 622), "AT REAL MONEY", f_bot, sw=5)

canvas.convert("RGB").save(f"{WORK}/gta6-meme-dicaprio.jpg", quality=92)
print("saved", canvas.size)
