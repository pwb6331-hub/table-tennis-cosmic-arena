import os, base64, io, json
from PIL import Image, ImageOps

target = r'E:\115\LIFE\3玟瑾7上\115年度連江縣體育季桌球錦標賽'
assets_dir = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets'

def img_to_b64(path, max_size=(1200, 1400), quality=82):
    try:
        im = Image.open(path)
        im = ImageOps.exif_transpose(im)
        im.thumbnail(max_size, Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format='JPEG', quality=quality)
        return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        print('Error:', path, e)
        return None

def file_to_b64(path, mime="image/jpeg"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')

# 1. 公開單打照片
singles_1st = img_to_b64(os.path.join(target, '公開單打', '第一名', '863103505_29009125485407406_5178213079965240879_n.jpg'), (900, 1200), 82)
singles_2nd = img_to_b64(os.path.join(target, '公開單打', '第二名', '869873722_29009127455407209_6948567798254274913_n.jpg'), (900, 1300), 82)
singles_3rd = img_to_b64(os.path.join(target, '公開單打', '第三名(陳)', '876794437_29009129622073659_4313618879974222479_n.jpg'), (900, 1200), 82)
singles_all = img_to_b64(os.path.join(target, '公開單打', '合照', '860852188_29009123565407598_3141386596420692141_n.jpg'), (1400, 900), 84)

# 2. 公開雙打照片
doubles_1st = img_to_b64(os.path.join(target, '公開雙打', '第一名', '877400567_29011482931838328_5098233391844630526_n.jpg'), (900, 1200), 82)
doubles_2nd = img_to_b64(os.path.join(target, '公開雙打', '第二名', '875876039_29011485098504778_2475974579901122108_n.jpg'), (900, 1200), 82)
doubles_3rd_liu = img_to_b64(os.path.join(target, '公開雙打', '第三名(劉)', '863408596_29011486521837969_2433342363621401614_n.jpg'), (900, 1200), 82)
doubles_3rd_chen = img_to_b64(os.path.join(target, '公開雙打', '第三名(陳)', '867105820_29011488405171114_8824357544143788463_n.jpg'), (900, 1200), 82)
doubles_all = img_to_b64(os.path.join(target, '公開雙打', '合照', '861977082_29011481058505182_2158522769064187726_n (1).jpg'), (1400, 900), 84)

# 3. 準備與實況照片
prep_dir = os.path.join(target, '準備')
prep_photos = []
if os.path.exists(prep_dir):
    for f in sorted(os.listdir(prep_dir)):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            p = os.path.join(prep_dir, f)
            b64 = img_to_b64(p, (1000, 1000), 78)
            if b64:
                prep_photos.append(b64)

vulcan_b64 = file_to_b64(os.path.join(assets_dir, 'planet_vulcan.jpg'))
cygnus_b64 = file_to_b64(os.path.join(assets_dir, 'planet_cygnus.jpg'))
aegis_b64 = file_to_b64(os.path.join(assets_dir, 'planet_aegis.jpg'))
space_b64 = file_to_b64(os.path.join(assets_dir, 'space_hd_bg.jpg'))

implementation_plan = {
    "title": "連江縣體育會115年「體育季」桌球錦標賽實施計劃",
    "organizer": "連江縣桌球委員會",
    "sections": [
        {
            "heading": "一、計畫依據",
            "content": ["連江縣體育會計畫辦理。"]
        },
        {
            "heading": "二、計畫目標",
            "content": [
                "推展全民運動，提倡運動風氣，提升地區動態休閒運動，厚植馬祖運動競爭力，藉由桌球運動強化健康體魄、改善社會運動風氣。鼓勵社區民眾積極參與，落實運動生活化，實質倍增運動人口。"
            ]
        },
        {
            "heading": "三、計畫推動組織及成員",
            "content": [
                "1、推動組織：連江縣政府教育處、連江縣體育會、連江縣桌球委員會。",
                "2、推動成員：連江縣政府教育處、連江縣體育會、連江縣桌球委員會、裁判組及競賽組。"
            ]
        },
        {
            "heading": "四、計畫內容",
            "content": [
                "（一）計畫期程：115年10月31日（08：30－18：30）",
                "（二）參與對象及方式：公開組 － 個人（單打／雙打）。",
                "（三）計畫執行方式：",
                "　1、教育與宣導：促進團隊精神，發展全民運動。",
                "　2、參賽人員：預計參賽人員（計100人，各組別50人）。",
                "　3、活動推展：連江縣南竿鄉復興牛角廟下方活動中心舉辦。",
                "　4、比賽方式：公開組 － 個人（單打／雙打）雙敗制。（初賽3戰2勝制／決賽5戰3勝制）",
                "　5、比賽規則：採2024年中華民國最新桌球協會最新桌球規則辦理。",
                "　6、比賽用球：採中華民國桌球協會指定用球。",
                "　7、報名日期：115年10月01日起至10月30日止。",
                "　8、報名單位：連江縣桌球委員會－總幹事陳君筑。電話：0928－016929。",
                "　9、獎勵辦法：個人獎：冠軍（獎牌＋獎品）、亞軍（獎牌＋獎品）、季軍（獎牌＋獎品）。"
            ]
        }
    ]
}

structured_data = {
    "space_bg": space_b64,
    "planet_textures": {
        "vulcan": vulcan_b64,
        "cygnus": cygnus_b64,
        "aegis": aegis_b64
    },
    "implementation_plan": implementation_plan,
    "planets": {
        "singles": {
            "key": "singles",
            "sector": "SECTOR 01 // VULCAN SINGLES",
            "name": "公開單打擂台星",
            "subtitle": "公開組個人單打賽（雙敗制：初賽3戰2勝／決賽5戰3勝）",
            "desc": "於連江縣南竿鄉復興牛角廟下方活動中心熱烈開打！經過雙敗制激烈淘汰與高張力攻防，恭喜所有獲獎名將（榮獲獎牌＋獎品）：",
            "rankings": [
                {
                    "rank": 1,
                    "rank_title": "第一名（冠軍）",
                    "name": "張正輝 先生",
                    "badge": "GOLD CHAMPION",
                    "desc": "馬祖桌壇傳奇名將，發球搶攻凌厲，連續強攻掌控全場節奏，榮登公開單打冠軍寶座！",
                    "photo": singles_1st,
                    "photo_caption": "公開單打 第一名頒獎：張正輝 先生"
                },
                {
                    "rank": 2,
                    "rank_title": "第二名（亞軍）",
                    "name": "陳孚謙 先生",
                    "badge": "SILVER RUNNER-UP",
                    "desc": "正手反手均衡發力，步法靈活敏捷，在多局拉鋸戰中沉穩應戰，奪得公開單打亞軍！",
                    "photo": singles_2nd,
                    "photo_caption": "公開單打 第二名頒獎：陳孚謙 先生"
                },
                {
                    "rank": 3,
                    "rank_title": "第三名（季軍）",
                    "name": "林樹清 先生 ／ 陳志國 先生",
                    "badge": "BRONZE PODIUM",
                    "desc": "林樹清近台快撕刁鑽多變，陳志國削中帶攻防守沉著，兩位桌壇常勝軍並列第三名季軍榮耀！",
                    "photo": singles_3rd,
                    "photo_caption": "公開單打 第三名頒獎：林樹清 先生、陳志國 先生"
                }
            ],
            "group_photo": singles_all,
            "group_caption": "115年度連江縣體育季桌球錦標賽・公開單打獲獎選手與頒獎貴賓全體大合照（南竿鄉復興牛角廟下方活動中心）"
        },
        "doubles": {
            "key": "doubles",
            "sector": "SECTOR 02 // CYGNUS DOUBLES",
            "name": "公開雙打雙生星",
            "subtitle": "公開組個人雙打賽（雙敗制：初賽3戰2勝／決賽5戰3勝）",
            "desc": "雙打講求絕對默契、極限補位與戰術壓制，於南竿鄉復興牛角廟下方活動中心締造場場精彩對攻高潮：",
            "rankings": [
                {
                    "rank": 1,
                    "rank_title": "第一名（冠軍）",
                    "name": "曹常容 先生 ／ 張正輝 先生",
                    "badge": "GOLD CHAMPION",
                    "desc": "雙雄合璧戰術無懈可擊！曹常容與張正輝攻防呼應，左右開弓展現頂級宰制力，榮獲公開雙打第一名冠軍！",
                    "photo": doubles_1st,
                    "photo_caption": "公開雙打 第一名頒獎：曹常容 先生、張正輝 先生"
                },
                {
                    "rank": 2,
                    "rank_title": "第二名（亞軍）",
                    "name": "邱德財 先生 ／ 邱祖珩 先生",
                    "badge": "SILVER RUNNER-UP",
                    "desc": "父子同心、絕佳默契走位！邱德財沉穩控球搭配邱祖珩強勁弧圈突擊，勇奪公開雙打第二名亞軍！",
                    "photo": doubles_2nd,
                    "photo_caption": "公開雙打 第二名頒獎：邱德財 先生、邱祖珩 先生"
                },
                {
                    "rank": 3,
                    "rank_title": "第三名（季軍）",
                    "name": "劉玟槿 同學 ／ 陳潤青 同學\n與 陳志國 先生 ／ 楊清宇 先生",
                    "badge": "BRONZE PODIUM",
                    "desc": "【雙季軍殊榮】新星崛起！劉玟槿同學與陳潤青同學展現超強拼勁勇奪季軍；陳志國與楊清宇老練配合鐵壁防守同登季軍！",
                    "photo": doubles_3rd_liu,
                    "photo_extra": doubles_3rd_chen,
                    "photo_caption": "公開雙打 第三名頒獎：劉玟槿同學、陳潤青同學 / 陳志國先生、楊清宇先生"
                }
            ],
            "group_photo": doubles_all,
            "group_caption": "115年度連江縣體育季桌球錦標賽・公開雙打獲獎選手與頒獎貴賓全體大合照（南竿鄉復興牛角廟下方活動中心）"
        },
        "prep": {
            "key": "prep",
            "sector": "SECTOR 03 // AEGIS PREP & PLAN",
            "name": "賽事籌備與大會星",
            "subtitle": "實施計劃、大會組織與南竿鄉復興牛角廟下方活動中心實況",
            "desc": "依據連江縣體育會計畫辦理，由連江縣政府教育處、連江縣體育會及連江縣桌球委員會（總幹事陳君筑、裁判組及競賽組）共同推動：",
            "rankings": [
                {
                    "rank": 1,
                    "rank_title": "第一名（特優籌備）",
                    "name": "連江縣桌球委員會 裁判組及競賽組",
                    "badge": "EXCELLENCE LEAD",
                    "desc": "總幹事陳君筑統籌規劃，裁判組及競賽組採2024年中華民國桌球協會最新規則公正執法，圓滿完成雙敗制賽事！",
                    "photo": prep_photos[0] if len(prep_photos) > 0 else None,
                    "photo_caption": "賽事準備現場 01：連江縣桌球委員會裁判組及競賽組"
                },
                {
                    "rank": 2,
                    "rank_title": "第二名（傑出場館與後勤）",
                    "name": "南竿鄉復興牛角廟下方活動中心 場地整備組",
                    "badge": "OUTSTANDING VENUE",
                    "desc": "於連江縣南竿鄉復興牛角廟下方活動中心專業佈置標準球檯、採中華民國桌球協會指定用球，提供100位參賽人員極致舞台！",
                    "photo": prep_photos[1] if len(prep_photos) > 1 else None,
                    "photo_caption": "賽事準備現場 02：南竿鄉復興牛角廟下方活動中心球檯與器材整備"
                },
                {
                    "rank": 3,
                    "rank_title": "第三名（榮譽推展）",
                    "name": "連江縣政府教育處 ／ 連江縣體育會 全民運動推展團",
                    "badge": "SPIRIT AWARD",
                    "desc": "推展全民運動、提倡運動風氣，鼓勵社區民眾積極參與，落實運動生活化，厚植馬祖運動競爭力！",
                    "photo": prep_photos[2] if len(prep_photos) > 2 else None,
                    "photo_caption": "賽事準備現場 03：參賽選手熱身交流與現場花絮"
                }
            ],
            "extra_photos": prep_photos[3:],
            "group_caption": "115年度連江縣體育季桌球錦標賽・南竿鄉復興牛角廟下方活動中心幕後準備與實況"
        }
    }
}

out_path = os.path.join(assets_dir, 'github_data.json')
with open(out_path, 'w', encoding='utf-8') as out:
    json.dump(structured_data, out, ensure_ascii=False)

print(f"Updated github_data.json with implementation plan & new venue! Size: {os.path.getsize(out_path)/1024:.2f} KB")
