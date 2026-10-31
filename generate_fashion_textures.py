import math, random, os, io, base64
from PIL import Image, ImageDraw, ImageFilter

output_dir = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets'
os.makedirs(output_dir, exist_ok=True)

def generate_vulcan_texture(w=2048, h=1024):
    """
    Hermès Flame Obsidian & Amber Gold
    奢華黑曜石熔金、極細大理石流體紋路
    """
    im = Image.new('RGB', (w, h), (10, 4, 2))
    draw = ImageDraw.Draw(im)
    
    # 基礎奢華金黑流體帶
    for y in range(h):
        ny = y / h
        # 多重正弦波調制
        wave1 = math.sin(ny * math.pi * 6 + 1.2) * 0.4
        wave2 = math.cos(ny * math.pi * 14) * 0.2
        mix = max(0.0, min(1.0, ny + wave1 + wave2))
        
        # 琥珀金到烈焰橙與黑曜岩
        r = int(255 * (0.15 + 0.85 * mix))
        g = int(140 * (0.05 + 0.95 * (mix ** 1.8)))
        b = int(20 * (0.02 + 0.98 * (mix ** 3.0)))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # 加入細緻熔金絲綢裂紋
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    random.seed(11501)
    
    for _ in range(80):
        start_x = random.uniform(0, w)
        start_y = random.uniform(0, h)
        cur_x, cur_y = start_x, start_y
        steps = random.randint(40, 120)
        width = random.uniform(2, 6)
        gold_color = (255, random.randint(180, 240), random.randint(60, 120), random.randint(90, 210))
        
        for _ in range(steps):
            next_x = (cur_x + random.uniform(5, 25)) % w
            next_y = cur_y + random.uniform(-4, 4)
            if next_y < 0: next_y = 0
            if next_y >= h: next_y = h - 1
            ov_draw.line([(cur_x, cur_y), (next_x, next_y)], fill=gold_color, width=int(width))
            cur_x, cur_y = next_x, next_y
            
    overlay = overlay.filter(ImageFilter.GaussianBlur(2))
    im.paste(overlay, (0, 0), overlay)
    
    path = os.path.join(output_dir, 'planet_vulcan.jpg')
    im.save(path, quality=92)
    print("Saved Vulcan Texture:", path)
    return path

def generate_cygnus_texture(w=2048, h=1024):
    """
    Tiffany Ice Cyan & Royal Amethyst
    蒂芙尼綠、冰川電光藍與皇家紫晶雙流體
    """
    im = Image.new('RGB', (w, h), (3, 8, 20))
    draw = ImageDraw.Draw(im)
    
    for y in range(h):
        ny = y / h
        # 雙流體旋轉干涉波
        wave = math.sin(ny * math.pi * 8) * 0.35 + math.sin(ny * math.pi * 16) * 0.15
        val = max(0.0, min(1.0, ny + wave))
        
        # 蒂芙尼冰綠 (0, 240, 255) 到 皇家紫羅蘭 (120, 0, 220)
        r = int(10 + 130 * math.sin(val * math.pi))
        g = int(30 + 200 * (1.0 - val))
        b = int(70 + 185 * math.cos(val * math.pi * 0.5))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    random.seed(11502)
    
    for _ in range(70):
        cx = random.uniform(0, w)
        cy = random.uniform(0, h)
        rad_x = random.uniform(80, 260)
        rad_y = random.uniform(15, 60)
        color = (0, 240, 255, random.randint(40, 120)) if random.random() > 0.4 else (200, 50, 255, random.randint(30, 90))
        ov_draw.ellipse([(cx - rad_x, cy - rad_y), (cx + rad_x, cy + rad_y)], fill=color)
        
    overlay = overlay.filter(ImageFilter.GaussianBlur(12))
    im.paste(overlay, (0, 0), overlay)
    
    path = os.path.join(output_dir, 'planet_cygnus.jpg')
    im.save(path, quality=92)
    print("Saved Cygnus Texture:", path)
    return path

def generate_aegis_texture(w=2048, h=1024):
    """
    Rolex Royal Gold & Brushed Titanium
    勞力士皇家金、鈦銀精密幾何經緯刻度
    """
    im = Image.new('RGB', (w, h), (14, 18, 25))
    draw = ImageDraw.Draw(im)
    
    for y in range(h):
        ny = y / h
        wave = math.cos(ny * math.pi * 10) * 0.2
        val = max(0.0, min(1.0, ny + wave))
        r = int(30 + 190 * (val ** 1.5))
        g = int(35 + 160 * (val ** 1.6))
        b = int(45 + 90 * (val ** 2.0))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    # 繪製高精密經緯與蜂巢幾何刻度線
    step_x = w // 32
    step_y = h // 16
    for x in range(0, w, step_x):
        ov_draw.line([(x, 0), (x, h)], fill=(255, 215, 0, 55), width=2)
    for y in range(0, h, step_y):
        ov_draw.line([(0, y), (w, y)], fill=(255, 255, 255, 45), width=1)
        
    im.paste(overlay, (0, 0), overlay)
    path = os.path.join(output_dir, 'planet_aegis.jpg')
    im.save(path, quality=92)
    print("Saved Aegis Texture:", path)
    return path

vulcan_path = generate_vulcan_texture()
cygnus_path = generate_cygnus_texture()
aegis_path = generate_aegis_texture()
print("All planet textures generated.")
