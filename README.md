# 115年度連江縣體育季桌球錦標賽 ｜ 3D 星際太空展館 (3D Cosmic Arena)

> **WebGL / Three.js 創意前端工程師 3D 沉浸式互動展館**  
> 融合 **米蘭奢華時尚（Celestial Haute Couture）** 與 **極限流體物理光影**，呈現連江縣體育季年度桌壇榮耀盛事。

---

## 🌌 專案特色 (Key Highlights)

- **🪐 2048px 超高清晰時尚球體（Procedural Celestial Textures）**：
  - **🔥 SECTOR 01: 烈焰黑曜熔金星（Vulcan Obsidian Gold）** ｜ 公開單打擂台星
  - **⚡ SECTOR 02: 蒂芙尼冰晶紫曜星（Tiffany Cyan & Amethyst）** ｜ 公開雙打雙生星
  - **🛡️ SECTOR 03: 勞力士星艦金盾星（Rolex Royal Gold & Titanium）** ｜ 賽事籌備與大會星
- **🏆 奧林匹克級前三名頒獎台（Podium Showcase Cards）**：
  - 每個星球點擊平滑推進特寫，展開 **第一名（金牌）**、**第二名（銀牌）**、**第三名（銅牌）** 專屬卡片。
  - 包含獲獎選手全名、專屬頒獎照片、榮譽徽章與戰績講評，並支援 4K Lightbox 全螢幕放大檢視。
- **🏓 星際量子桌球弧圈對拉（Quantum Ping-Pong Rally Simulation）**：
  - 白熾光子球沿三維引力拋物線高速對拉，實時計算下旋與弧圈軌跡，觸台觸發能量漣漪衝擊波。
- **🔊 純 Web Audio API 物理聲學引擎**：
  - 免外部音訊檔案依賴，純即時合成桌球板木質衝擊音、球桌彈跳落點回響、極速殺球破空音與 45Hz 宇宙低頻脈衝。
- **📱 跨裝置極致響應式支援（Mobile / Tablet / Desktop）**：
  - 桌機支援滑鼠 360° 軌道漫遊、滾輪縮放、`1`/`2`/`3` 數字鍵視角切換、`Space` 擊球、`ESC` 關閉。
  - 手機／平板支援觸控旋轉手勢、雙指捏合縮放、全螢幕（Fullscreen）沉浸式體驗。

---

## 🏆 賽事實體戰果名單 (Official Tournament Results)

### 🔥 公開組個人單打賽 (Singles Sector)
- 🥇 **第一名（冠軍）**：**張正輝 先生**（馬祖桌壇傳奇名將，凌厲發球搶攻，單打所向披靡）
- 🥈 **第二名（亞軍）**：**陳孚謙 先生**（正手弧圈球均衡沉穩，多局拉鋸防守反擊）
- 🥉 **第三名（季軍）**：**林樹清 先生 ／ 陳志國 先生**（並列雙季軍，近台快攻與削球戰術大師）
- 📸 **合照**：全體公開單打獲獎選手大合照。

### ⚡ 公開組個人雙打賽 (Doubles Sector)
- 🥇 **第一名（冠軍）**：**曹常容 先生 ／ 張正輝 先生**（冠軍金牌，雙雄默契無間戰術封鎖）
- 🥈 **第二名（亞軍）**：**邱德財 先生 ／ 邱祖珩 先生**（亞軍銀牌，父子同心俐落攻守位移）
- 🥉 **第三名（季軍）**：**劉玟槿 同學 ／ 陳潤青 同學** 與 **陳志國 先生 ／ 楊清宇 先生**（新星崛起青春風暴 vs 老練鐵壁防守，雙季軍雙照片並列展示）
- 📸 **合照**：全體公開雙打獲獎選手大合照。

### 🛡️ 賽事籌備與大會之星 (Prep & Logistics Sector)
- 🥇 **特優籌備第一名**：**大會賽務裁決與籌備裁判團**（連江縣體育會桌球委員會高規格公正執法）
- 🥈 **傑出後勤第二名**：**場地器材維護與戰略整備組**（專業球檯與40+三星比賽級球具整備）
- 🥉 **榮譽推廣第三名**：**全民健康推展與青年傳承隊**（熱血運動無齡界、老中青三代傳承培訓）
- 📸 **花絮**：大會精選實況與選手熱身花絮畫廊。

---

## 🚀 部署至 GitHub Pages 指南 (Deploy to GitHub Pages)

本專案為自包含靜態專案（Self-contained HTML5 / WebGL），零相依設定，直接支援 GitHub Pages 一鍵上架：

### 步驟 1：建立 GitHub 遠端倉庫並推送
```bash
cd E:\2026GEM-SKILL\table-tennis-cosmic-arena
git init
git add .
git commit -m "feat: initial release of 115 Lianchiang table tennis 3D cosmic arena"
# 建立遠端 repo 並推送到 GitHub（已登入 GitHub CLI）
gh repo create table-tennis-cosmic-arena --public --source=. --remote=origin --push
```

### 步驟 2：開啟 GitHub Pages
1. 前往您剛剛建立的 GitHub Repository 頁面：`https://github.com/pwb6331-hub/table-tennis-cosmic-arena`
2. 點選 **Settings** -> **Pages**。
3. 在 **Build and deployment** > **Branch** 下拉選單選擇 `main`，資料夾選擇 `/ (root)`，點選 **Save**。
4. 約 1 分鐘後即可透過 GitHub Pages 專屬網址全球線上連線瀏覽：
   `https://pwb6331-hub.github.io/table-tennis-cosmic-arena/`

---

## 🛠️ 技術棧 (Technology Stack)

- **3D 引擎**：Three.js (r128) + OrbitControls
- **動畫系統**：GSAP (GreenSock 3.12.5) Smooth Cubic Easing
- **音效架構**：Web Audio API (雙耳節拍、帶通濾波、木質共振聲學物理合成)
- **視覺字型**：Google Fonts Noto Sans TC (思源黑體) + Orbitron + Rajdhani
- **版面技術**：CSS3 Glassmorphism、Flexbox / CSS Grid 雙模響應式排版

---

## 📄 授權條款 (License)

本專案基於 [MIT License](LICENSE) 條款開源發布。
