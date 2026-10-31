import json, os, base64

assets_dir = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets'
struct_path = r'E:\2026GEM-SKILL\table_tennis_space\structured_data.json'

with open(struct_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def file_to_b64(path, mime="image/jpeg"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')

vulcan_b64 = file_to_b64(os.path.join(assets_dir, 'planet_vulcan.jpg'))
cygnus_b64 = file_to_b64(os.path.join(assets_dir, 'planet_cygnus.jpg'))
aegis_b64 = file_to_b64(os.path.join(assets_dir, 'planet_aegis.jpg'))
space_b64 = file_to_b64(os.path.join(assets_dir, 'space_hd_bg.jpg'))

data['space_bg'] = space_b64
data['planet_textures'] = {
    'vulcan': vulcan_b64,
    'cygnus': cygnus_b64,
    'aegis': aegis_b64
}

out_path = os.path.join(assets_dir, 'github_data.json')
with open(out_path, 'w', encoding='utf-8') as out:
    json.dump(data, out, ensure_ascii=False)

print(f"github_data.json ready! Size: {os.path.getsize(out_path) / 1024:.2f} KB")
