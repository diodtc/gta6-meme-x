#!/usr/bin/env python3
"""Build the GTA 6 meme: composite the real make.fun ghost onto the couch
next to the waiting gamer, add classic top/bottom caption text.
Input: media-generation-gta6-scene-*.webp (AI scene), ghost-mark.png (press kit)
Output: meme.png (1920x1280 PNG, the post's first picture)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCENE = "gta6-scene.webp"
GHOST = "ghost-mark.png"
OUT = "meme.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(SCENE).convert("RGB")
W, H = img.size  # 1920x1280

# --- make.fun ghost, seated on the couch cushion (covers the plush toy) ---
ghost = Image.open(GHOST).convert("RGBA")
gs = 340  # ghost disc diameter
ghost = ghost.resize((gs, gs), Image.LANCZOS)
gx, gy = 1240, 830  # centre of the cushion seat, covering the plush toy fully
# soft contact shadow under the ghost
shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([gx - 150, gy + 120, gx + 150, gy + 175], fill=(0, 0, 0, 110))
shadow = shadow.filter(ImageFilter.GaussianBlur(12))
img = Image.alpha_composite(img.convert("RGBA"), shadow)
img.paste(ghost, (gx - gs // 2, gy - gs // 2), ghost)
img = img.convert("RGB")

# --- classic meme caption, white with thick black outline ---
d = ImageDraw.Draw(img)

def text_block(lines, y_top, size):
    font = ImageFont.truetype(FONT, size)
    y = y_top
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font, stroke_width=6)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        d.text(((W - tw) / 2, y), line, font=font, fill="white",
               stroke_width=6, stroke_fill="black")
        y += th + 8
    return y

text_block(["WAITED 13 YEARS FOR GTA 6"], 36, 96)
text_block(["NOW WAITING 6 MORE HOURS", "FOR THE DOWNLOAD"], H - 260, 84)

img.save(OUT, "PNG")
print(f"wrote {OUT} {img.size}")
