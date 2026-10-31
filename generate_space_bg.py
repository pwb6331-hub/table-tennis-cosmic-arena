import math, random, os
from PIL import Image, ImageDraw, ImageFilter

bg_path = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets\space_hd_bg.jpg'
w, h = 2560, 1440
im = Image.new('RGB', (w, h), (2, 4, 10))
draw = ImageDraw.Draw(im)

# 1. 宇宙深空放射狀星雲漸層
for y in range(h):
    ny = y / h
    r = int(2 + 10 * math.sin(ny * math.pi))
    g = int(4 + 16 * math.sin(ny * math.pi * 0.8))
    b = int(10 + 26 * math.sin(ny * math.pi * 0.6))
    draw.line([(0, y), (w, y)], fill=(r, g, b))

nebula = Image.new('RGBA', (w, h), (0, 0, 0, 0))
neb_draw = ImageDraw.Draw(nebula)
random.seed(2026)

# 星雲雲團
colors = [
    (0, 160, 255, 30), # 科技天青
    (140, 20, 200, 22), # 皇家奢華紫
    (255, 80, 0, 16),   # 琥珀星光
    (0, 240, 220, 25)   # 冰藍輝光
]

for _ in range(35):
    cx = random.uniform(0, w)
    cy = random.uniform(0, h)
    rx = random.uniform(250, 700)
    ry = random.uniform(120, 450)
    col = random.choice(colors)
    neb_draw.ellipse([(cx - rx, cy - ry), (cx + rx, cy + ry)], fill=col)

nebula = nebula.filter(ImageFilter.GaussianBlur(80))
im.paste(nebula, (0, 0), nebula)

# 2. 銳利星塵（三層不同半徑與亮度）
stars = Image.new('RGBA', (w, h), (0, 0, 0, 0))
st_draw = ImageDraw.Draw(stars)

# 微星 (Micro stars)
for _ in range(1200):
    x = random.uniform(0, w)
    y = random.uniform(0, h)
    brightness = random.randint(120, 255)
    st_draw.point((x, y), fill=(brightness, brightness, 255, random.randint(140, 240)))

# 亮星 (Bright stars)
for _ in range(180):
    x = random.uniform(0, w)
    y = random.uniform(0, h)
    rad = random.uniform(1.2, 2.5)
    col = (255, 255, 255, 230) if random.random() > 0.3 else (0, 240, 255, 220)
    st_draw.ellipse([(x - rad, y - rad), (x + rad, y + rad)], fill=col)

# 巨星十字星芒 (Sparkle cross stars)
for _ in range(25):
    x = random.uniform(0, w)
    y = random.uniform(0, h)
    st_draw.line([(x - 8, y), (x + 8, y)], fill=(255, 255, 255, 180), width=1)
    st_draw.line([(x, y - 8), (x, y + 8)], fill=(255, 255, 255, 180), width=1)
    st_draw.ellipse([(x - 2, y - 2), (x + 2, y + 2)], fill=(255, 255, 255, 255))

im.paste(stars, (0, 0), stars)
im.save(bg_path, quality=90)
print("Saved high-res space background:", bg_path, "Size:", os.path.getsize(bg_path) / 1024, "KB")
