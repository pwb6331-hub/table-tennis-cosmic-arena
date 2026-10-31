import json, os

data_path = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets\github_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    full_data = json.load(f)

html_code = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>115年度連江縣體育季桌球錦標賽 ｜ 3D 星際太空展館</title>
  <!-- Google Fonts: Noto Sans TC, Orbitron, Rajdhani -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&family=Orbitron:wght@500;700;800;900&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
  <!-- Three.js & Controls via Cloudflare CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <!-- GSAP Animation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

  <style>
    :root {
      --primary: #00f0ff;
      --primary-glow: rgba(0, 240, 255, 0.45);
      --amber-gold: #ffaa00;
      --amber-glow: rgba(255, 170, 0, 0.45);
      --amethyst: #b800ff;
      --amethyst-glow: rgba(184, 0, 255, 0.4);
      --gold-pure: #ffd700;
      --silver-pure: #e2e8f0;
      --bronze-pure: #e67e22;
      --bg-dark: #02040a;
      --hud-bg: rgba(6, 11, 24, 0.86);
      --hud-border: rgba(0, 240, 255, 0.22);
      --card-bg: rgba(10, 16, 32, 0.94);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-tc: 'Noto Sans TC', "Source Han Sans", -apple-system, BlinkMacSystemFont, sans-serif;
      --font-tech: 'Orbitron', 'Rajdhani', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body, html {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: var(--bg-dark);
      font-family: var(--font-tc);
      color: var(--text-main);
    }

    #webgl-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
      outline: none;
    }

    /* UI Overlay Layer */
    .ui-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* Top HUD Header */
    .hud-header {
      pointer-events: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 26px;
      background: linear-gradient(180deg, rgba(2, 4, 10, 0.95) 0%, rgba(2, 4, 10, 0.5) 80%, transparent 100%);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(0, 240, 255, 0.15);
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .badge-year {
      background: linear-gradient(135deg, #ff0055, #ff5500);
      color: #fff;
      font-family: var(--font-tech);
      font-size: 13px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 1px;
      box-shadow: 0 0 16px rgba(255, 0, 85, 0.5);
      text-transform: uppercase;
    }

    .title-box h1 {
      font-size: 20px;
      font-weight: 900;
      letter-spacing: 1.5px;
      background: linear-gradient(90deg, #ffffff 0%, #00f0ff 60%, #ffd700 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 2px;
    }

    .title-box p {
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 1px;
      font-family: var(--font-tech);
    }

    .hud-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-icon {
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid rgba(0, 240, 255, 0.28);
      color: var(--primary);
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-family: var(--font-tech);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(4px);
    }

    .btn-icon:hover, .btn-icon.active {
      background: rgba(0, 240, 255, 0.25);
      border-color: var(--primary);
      box-shadow: 0 0 16px var(--primary-glow);
      transform: translateY(-1px);
      color: #fff;
    }

    .btn-icon:active {
      transform: translateY(1px);
    }

    /* Sound Visualizer & Wave */
    .sound-status {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 0, 0, 0.55);
      padding: 6px 12px;
      border-radius: 20px;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .sound-bars {
      display: flex;
      align-items: flex-end;
      gap: 3px;
      height: 14px;
    }

    .sound-bar {
      width: 3px;
      height: 4px;
      background: var(--primary);
      border-radius: 2px;
      transition: height 0.1s ease;
    }

    .sound-bars.active .sound-bar:nth-child(1) { animation: bounce 0.4s infinite alternate ease-in-out; }
    .sound-bars.active .sound-bar:nth-child(2) { animation: bounce 0.6s infinite alternate ease-in-out 0.15s; }
    .sound-bars.active .sound-bar:nth-child(3) { animation: bounce 0.5s infinite alternate ease-in-out 0.3s; }

    @keyframes bounce {
      0% { height: 4px; }
      100% { height: 14px; }
    }

    /* Quantum Rally Stats Tracker */
    .rally-hud {
      position: absolute;
      top: 86px;
      left: 26px;
      background: var(--hud-bg);
      border: 1px solid var(--hud-border);
      padding: 10px 16px;
      border-radius: 8px;
      pointer-events: auto;
      display: flex;
      flex-direction: column;
      gap: 4px;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }

    .rally-title {
      font-family: var(--font-tech);
      font-size: 10px;
      color: var(--text-muted);
      letter-spacing: 1.2px;
    }

    .rally-counter {
      font-family: var(--font-tech);
      font-size: 22px;
      font-weight: 900;
      color: #fff;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }

    .rally-unit {
      font-size: 11px;
      color: var(--primary);
    }

    /* Bottom Sector Selector Navigation */
    .hud-footer {
      pointer-events: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 18px 20px;
      gap: 10px;
      background: linear-gradient(0deg, rgba(2, 4, 10, 0.98) 0%, rgba(2, 4, 10, 0.6) 70%, transparent 100%);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }

    .nav-orbs {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 14px;
      max-width: 980px;
      width: 100%;
    }

    .orb-tab {
      flex: 1;
      min-width: 200px;
      max-width: 280px;
      background: var(--hud-bg);
      border: 1px solid var(--hud-border);
      border-radius: 12px;
      padding: 12px 16px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 14px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }

    .orb-tab::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--primary);
      opacity: 0.4;
      transition: opacity 0.3s ease;
    }

    .orb-tab.tab-singles::before { background: var(--amber-gold); }
    .orb-tab.tab-doubles::before { background: var(--primary); }
    .orb-tab.tab-prep::before { background: var(--gold-pure); }

    .orb-tab:hover, .orb-tab.active {
      transform: translateY(-4px);
      background: rgba(10, 18, 38, 0.96);
      border-color: rgba(0, 240, 255, 0.7);
      box-shadow: 0 6px 24px rgba(0, 240, 255, 0.25);
    }

    .orb-tab.active::before {
      opacity: 1;
      box-shadow: 0 0 12px var(--primary);
    }

    .orb-tab-icon {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      flex-shrink: 0;
    }

    .orb-tab-info {
      text-align: left;
      overflow: hidden;
    }

    .orb-tab-info .tab-sub {
      font-size: 10px;
      color: var(--text-muted);
      letter-spacing: 0.8px;
      font-family: var(--font-tech);
    }

    .orb-tab-info .tab-title {
      font-size: 14px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .controls-hint {
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .hint-item {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .hint-key {
      background: rgba(255, 255, 255, 0.12);
      padding: 2px 7px;
      border-radius: 4px;
      font-family: var(--font-tech);
      font-size: 11px;
      color: #fff;
    }

    /* ========================================================================
       FASHION-TECH HOLOGRAM MODAL - PODIUM SHOWCASE
       ======================================================================== */
    .hologram-modal {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 100;
      background: rgba(2, 4, 10, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease;
    }

    .hologram-modal.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-card {
      width: 100%;
      max-width: 1180px;
      max-height: 92vh;
      background: rgba(8, 14, 28, 0.96);
      border: 1px solid var(--hud-border);
      border-radius: 18px;
      box-shadow: 0 0 60px rgba(0, 240, 255, 0.22), inset 0 0 25px rgba(0, 240, 255, 0.06);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.92) translateY(20px);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hologram-modal.open .modal-card {
      transform: scale(1) translateY(0);
    }

    .modal-header {
      padding: 18px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(0, 0, 0, 0.4);
    }

    .modal-header-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .sector-tag {
      font-family: var(--font-tech);
      font-size: 12px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      background: rgba(0, 240, 255, 0.15);
      border: 1px solid var(--primary);
      color: var(--primary);
    }

    .modal-header h2 {
      font-size: 22px;
      font-weight: 900;
      letter-spacing: 1px;
    }

    .btn-close {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      font-size: 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .btn-close:hover {
      background: rgba(255, 0, 85, 0.7);
      border-color: #ff0055;
      transform: rotate(90deg);
    }

    .modal-body {
      padding: 24px 28px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .modal-lead-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
      border-left: 3px solid var(--primary);
      padding-left: 12px;
    }

    /* Podium Grid: 1st, 2nd, 3rd Cards */
    .podium-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      align-items: stretch;
    }

    .podium-card {
      background: var(--card-bg);
      border-radius: 14px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    .podium-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.6);
    }

    /* Gold Card (1st) */
    .podium-card.rank-1-card {
      border-color: rgba(255, 215, 0, 0.6);
      box-shadow: 0 0 30px rgba(255, 215, 0, 0.15);
      background: linear-gradient(180deg, rgba(35, 28, 12, 0.95) 0%, rgba(12, 18, 36, 0.98) 100%);
    }
    .podium-card.rank-1-card:hover {
      border-color: #ffd700;
      box-shadow: 0 0 45px rgba(255, 215, 0, 0.35);
    }

    /* Silver Card (2nd) */
    .podium-card.rank-2-card {
      border-color: rgba(226, 232, 240, 0.5);
      box-shadow: 0 0 25px rgba(226, 232, 240, 0.12);
      background: linear-gradient(180deg, rgba(22, 28, 38, 0.95) 0%, rgba(12, 18, 36, 0.98) 100%);
    }
    .podium-card.rank-2-card:hover {
      border-color: #ffffff;
      box-shadow: 0 0 38px rgba(226, 232, 240, 0.3);
    }

    /* Bronze Card (3rd) */
    .podium-card.rank-3-card {
      border-color: rgba(230, 126, 34, 0.5);
      box-shadow: 0 0 25px rgba(230, 126, 34, 0.12);
      background: linear-gradient(180deg, rgba(34, 20, 14, 0.95) 0%, rgba(12, 18, 36, 0.98) 100%);
    }
    .podium-card.rank-3-card:hover {
      border-color: #e67e22;
      box-shadow: 0 0 38px rgba(230, 126, 34, 0.3);
    }

    .card-top-badge {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(0, 0, 0, 0.3);
    }

    .badge-rank-title {
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .rank-1-card .badge-rank-title { color: #ffd700; }
    .rank-2-card .badge-rank-title { color: #e2e8f0; }
    .rank-3-card .badge-rank-title { color: #f39c12; }

    .badge-label {
      font-family: var(--font-tech);
      font-size: 10px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
      letter-spacing: 0.5px;
    }

    .card-photo-box {
      width: 100%;
      aspect-ratio: 4 / 3;
      position: relative;
      overflow: hidden;
      background: #000;
      cursor: zoom-in;
    }

    .card-photo-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .card-photo-box:hover img {
      transform: scale(1.06);
    }

    .card-photo-overlay {
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(0, 0, 0, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 20px;
      padding: 4px 10px;
      font-size: 11px;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(4px);
    }

    .dual-photo-box {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3px;
      aspect-ratio: 8 / 3;
      background: #000;
    }

    .dual-photo-box .mini-photo-item {
      position: relative;
      overflow: hidden;
      cursor: zoom-in;
      height: 100%;
    }

    .dual-photo-box .mini-photo-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }

    .dual-photo-box .mini-photo-item:hover img {
      transform: scale(1.08);
    }

    .card-info {
      padding: 16px 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }

    .winner-name-text {
      font-size: 18px;
      font-weight: 900;
      letter-spacing: 0.5px;
      color: #fff;
      white-space: pre-line;
      line-height: 1.4;
    }

    .rank-1-card .winner-name-text {
      background: linear-gradient(90deg, #fff7cc, #ffd700);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .winner-desc-text {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    /* Group Photos & Extra Carousel */
    .group-photo-section {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .group-section-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .group-photo-container {
      width: 100%;
      max-height: 380px;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      position: relative;
      cursor: zoom-in;
      background: #000;
    }

    .group-photo-container img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      transition: transform 0.3s ease;
    }

    .group-photo-container:hover img {
      transform: scale(1.02);
    }

    .group-caption {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      background: linear-gradient(0deg, rgba(0, 0, 0, 0.85) 0%, transparent 100%);
      padding: 8px 14px;
      font-size: 12px;
      color: #fff;
    }

    .prep-gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 12px;
    }

    .prep-thumb-item {
      aspect-ratio: 4 / 3;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: zoom-in;
      position: relative;
      background: #000;
    }

    .prep-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }

    .prep-thumb-item:hover {
      border-color: var(--primary);
      box-shadow: 0 0 14px var(--primary-glow);
    }

    .prep-thumb-item:hover img {
      transform: scale(1.08);
    }

    /* Lightbox Fullscreen Preview */
    .lightbox-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 200;
      background: rgba(2, 4, 10, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
      cursor: zoom-out;
    }

    .lightbox-overlay.active {
      display: flex;
    }

    .lightbox-img {
      max-width: 92vw;
      max-height: 88vh;
      border-radius: 12px;
      box-shadow: 0 0 40px rgba(0, 240, 255, 0.4);
      border: 1px solid rgba(0, 240, 255, 0.5);
    }

    /* Responsive Mobile / Tablet */
    @media (max-width: 900px) {
      .podium-grid {
        grid-template-columns: 1fr;
      }
      .modal-card {
        max-height: 94vh;
      }
      .hud-header {
        padding: 12px 16px;
      }
      .title-box h1 {
        font-size: 16px;
      }
      .title-box p {
        display: none;
      }
      .btn-icon span {
        display: none;
      }
      .rally-hud {
        top: 68px;
        left: 16px;
      }
      .controls-hint {
        display: none;
      }
      .nav-orbs {
        gap: 8px;
      }
      .orb-tab {
        min-width: 130px;
        padding: 8px 10px;
      }
      .orb-tab-icon {
        width: 32px;
        height: 32px;
        font-size: 16px;
      }
      .orb-tab-info .tab-title {
        font-size: 12px;
      }
    }
  </style>
</head>
<body>

  <!-- WebGL Three.js Container -->
  <div id="webgl-canvas"></div>

  <!-- UI HUD Layer -->
  <div class="ui-layer">
    <!-- Top Header -->
    <header class="hud-header">
      <div class="brand-group">
        <div class="badge-year">115年度</div>
        <div class="title-box">
          <h1>連江縣體育季桌球錦標賽</h1>
          <p>3D COSMIC ARENA ｜ 馬祖南竿體育館 榮耀星際殿堂</p>
        </div>
      </div>

      <div class="hud-controls">
        <div class="sound-status">
          <div class="sound-bars" id="sound-bars">
            <div class="sound-bar"></div>
            <div class="sound-bar"></div>
            <div class="sound-bar"></div>
          </div>
          <button class="btn-icon" id="btn-sound" title="切換立體聲音效">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
            <span id="sound-text">桌球音效: 開</span>
          </button>
        </div>

        <button class="btn-icon" id="btn-hit" title="擊球模擬音效">
          <span>🏓 擊球模擬</span>
        </button>

        <button class="btn-icon" id="btn-reset" title="重置為全景視角">
          <span>🌌 全景星圖</span>
        </button>

        <button class="btn-icon" id="btn-fullscreen" title="全螢幕切換">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
        </button>
      </div>
    </header>

    <!-- Rally Stats Tracker -->
    <div class="rally-hud">
      <div class="rally-title">QUANTUM RALLY SPEED</div>
      <div class="rally-counter"><span id="rally-count">0</span> <span class="rally-unit">PONG / MIN</span></div>
    </div>

    <!-- Bottom Navigation & Planet Selector -->
    <footer class="hud-footer">
      <div class="nav-orbs">
        <div class="orb-tab tab-singles" data-target="singles">
          <div class="orb-tab-icon" style="color: #ffaa00; border-color: rgba(255,170,0,0.4);">🔥</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 01</div>
            <div class="tab-title">公開單打擂台星</div>
          </div>
        </div>

        <div class="orb-tab tab-doubles" data-target="doubles">
          <div class="orb-tab-icon" style="color: #00f0ff; border-color: rgba(0,240,255,0.4);">⚡</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 02</div>
            <div class="tab-title">公開雙打雙生星</div>
          </div>
        </div>

        <div class="orb-tab tab-prep" data-target="prep">
          <div class="orb-tab-icon" style="color: #ffd700; border-color: rgba(255,215,0,0.4);">🛡️</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 03</div>
            <div class="tab-title">賽事籌備與大會星</div>
          </div>
        </div>
      </div>

      <div class="controls-hint">
        <div class="hint-item"><span class="hint-key">拖曳</span> 360° 旋轉視角</div>
        <div class="hint-item"><span class="hint-key">滾輪/捏合</span> 縮放星系</div>
        <div class="hint-item"><span class="hint-key">點選星球</span> 進入前三名戰報</div>
      </div>
    </footer>
  </div>

  <!-- Hologram Modal -->
  <div class="hologram-modal" id="modal">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-header-left">
          <span class="sector-tag" id="modal-sector">SECTOR 01</span>
          <h2 id="modal-title">賽事榮耀榜</h2>
        </div>
        <button class="btn-close" id="btn-close-modal">✕</button>
      </div>
      <div class="modal-body" id="modal-content">
        <!-- Dynamically populated -->
      </div>
    </div>
  </div>

  <!-- Lightbox -->
  <div class="lightbox-overlay" id="lightbox">
    <img class="lightbox-img" id="lightbox-img" src="" alt="高解析照片預覽">
  </div>

  <script>
    /* ========================================================================
       DATA REPOSITORY WITH ULTRA-RES TEXTURES & PODIUM DETAILS
       ======================================================================== */
    const TOURNAMENT_DATA = ''' + json.dumps(full_data, ensure_ascii=False) + ''';

    /* ========================================================================
       WEB AUDIO API - PING-PONG SOUND ENGINE & AMBIENT SCI-FI DRONE
       ======================================================================== */
    class AudioEngine {
      constructor() {
        this.ctx = null;
        this.enabled = true;
        this.droneGain = null;
        this.masterGain = null;
      }

      init() {
        if (this.ctx) return;
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.ctx = new AudioContext();

        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.setValueAtTime(0.75, this.ctx.currentTime);
        this.masterGain.connect(this.ctx.destination);

        this.startCosmicDrone();
      }

      startCosmicDrone() {
        if (!this.ctx) return;
        try {
          const osc1 = this.ctx.createOscillator();
          const osc2 = this.ctx.createOscillator();
          const filter = this.ctx.createBiquadFilter();

          osc1.type = 'sine';
          osc1.frequency.setValueAtTime(45, this.ctx.currentTime);

          osc2.type = 'triangle';
          osc2.frequency.setValueAtTime(47.5, this.ctx.currentTime);

          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(110, this.ctx.currentTime);

          this.droneGain = this.ctx.createGain();
          this.droneGain.gain.setValueAtTime(0.08, this.ctx.currentTime);

          osc1.connect(filter);
          osc2.connect(filter);
          filter.connect(this.droneGain);
          this.droneGain.connect(this.masterGain);

          osc1.start();
          osc2.start();
        } catch(e) {
          console.warn("Drone audio error:", e);
        }
      }

      playPing(frequency = 940, decay = 0.08, isSmash = false) {
        if (!this.enabled) return;
        this.init();
        if (this.ctx.state === 'suspended') this.ctx.resume();

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const filter = this.ctx.createBiquadFilter();

        osc.type = isSmash ? 'sawtooth' : 'sine';
        osc.frequency.setValueAtTime(frequency, now);
        osc.frequency.exponentialRampToValueAtTime(340, now + decay);

        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(isSmash ? 1500 : 980, now);
        filter.Q.setValueAtTime(3.8, now);

        gain.gain.setValueAtTime(isSmash ? 0.65 : 0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + decay);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        osc.start(now);
        osc.stop(now + decay);

        // Ping wood hit resonant pop
        if (!isSmash) {
          const popOsc = this.ctx.createOscillator();
          const popGain = this.ctx.createGain();
          popOsc.frequency.setValueAtTime(420, now);
          popOsc.frequency.exponentialRampToValueAtTime(160, now + 0.04);
          popGain.gain.setValueAtTime(0.22, now);
          popGain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
          popOsc.connect(popGain);
          popGain.connect(this.masterGain);
          popOsc.start(now);
          popOsc.stop(now + 0.04);
        }
      }

      toggle() {
        this.enabled = !this.enabled;
        if (this.masterGain && this.ctx) {
          this.masterGain.gain.setValueAtTime(this.enabled ? 0.75 : 0, this.ctx.currentTime);
        }
        return this.enabled;
      }
    }

    const soundSystem = new AudioEngine();

    /* ========================================================================
       THREE.JS WEBGL 3D COSMIC ENGINE
       ======================================================================== */
    const container = document.getElementById('webgl-canvas');
    let scene, camera, renderer, controls;
    let planets = {};
    let raycaster, mouse;
    let starfield, brightStars;
    let rallyBall;
    let rallyProgress = 0;
    let rallyRounds = 56;

    function initWebGL() {
      // Scene
      scene = new THREE.Scene();
      scene.fog = new THREE.FogExp2(0x02040a, 0.004);

      // Camera
      camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1200);
      camera.position.set(0, 14, 46);

      // Renderer
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.3;
      container.appendChild(renderer.domElement);

      // Controls
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.maxDistance = 140;
      controls.minDistance = 6;
      controls.maxPolarAngle = Math.PI / 2 + 0.1;

      // Raycasting
      raycaster = new THREE.Raycaster();
      mouse = new THREE.Vector2();

      // Lights
      const ambientLight = new THREE.AmbientLight(0x283855, 1.4);
      scene.add(ambientLight);

      const mainLight = new THREE.DirectionalLight(0xffffff, 2.4);
      mainLight.position.set(35, 45, 25);
      scene.add(mainLight);

      const rimLight = new THREE.PointLight(0x00f0ff, 3.2, 120);
      rimLight.position.set(-25, 12, -20);
      scene.add(rimLight);

      const goldRim = new THREE.PointLight(0xffaa00, 2.8, 120);
      goldRim.position.set(28, -12, -15);
      scene.add(goldRim);

      // Build Environments
      buildSpaceBackground();
      buildStarfields();
      buildCelestialPlanets();
      buildPingPongRallySystem();

      // Events
      window.addEventListener('resize', onWindowResize, false);
      window.addEventListener('pointerdown', onPointerDown, false);

      animate();
    }

    /* 1. Deep Space Ultra-Res Panorama */
    function buildSpaceBackground() {
      if (TOURNAMENT_DATA.space_bg) {
        const textureLoader = new THREE.TextureLoader();
        textureLoader.load(TOURNAMENT_DATA.space_bg, (tex) => {
          tex.mapping = THREE.EquirectangularReflectionMapping;
          const bgGeo = new THREE.SphereGeometry(350, 64, 48);
          bgGeo.scale(-1, 1, 1);
          const bgMat = new THREE.MeshBasicMaterial({ map: tex, transparent: true, opacity: 0.75 });
          const bgMesh = new THREE.Mesh(bgGeo, bgMat);
          scene.add(bgMesh);
        });
      }
    }

    /* 2. Haute Couture Multi-tier Starfield */
    function buildStarfields() {
      // Tier 1: Micro dust stars
      const starGeo = new THREE.BufferGeometry();
      const starCount = 4200;
      const posArray = new Float32Array(starCount * 3);
      const colorArray = new Float32Array(starCount * 3);

      for (let i = 0; i < starCount * 3; i += 3) {
        posArray[i] = (Math.random() - 0.5) * 400;
        posArray[i + 1] = (Math.random() - 0.5) * 220;
        posArray[i + 2] = (Math.random() - 0.5) * 400;

        const rand = Math.random();
        if (rand > 0.6) {
          // Tiffany Cyan
          colorArray[i] = 0.2; colorArray[i + 1] = 0.95; colorArray[i + 2] = 1.0;
        } else if (rand > 0.3) {
          // Amber Gold
          colorArray[i] = 1.0; colorArray[i + 1] = 0.8; colorArray[i + 2] = 0.3;
        } else {
          // Pure White
          colorArray[i] = 0.95; colorArray[i + 1] = 0.98; colorArray[i + 2] = 1.0;
        }
      }

      starGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
      starGeo.setAttribute('color', new THREE.BufferAttribute(colorArray, 3));

      const canvas = document.createElement('canvas');
      canvas.width = 32;
      canvas.height = 32;
      const ctx = canvas.getContext('2d');
      const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
      grad.addColorStop(0, 'rgba(255,255,255,1)');
      grad.addColorStop(0.25, 'rgba(0,240,255,0.8)');
      grad.addColorStop(0.6, 'rgba(0,240,255,0.2)');
      grad.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 32, 32);
      const starTex = new THREE.CanvasTexture(canvas);

      const starMat = new THREE.PointsMaterial({
        size: 2.2,
        vertexColors: true,
        map: starTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      starfield = new THREE.Points(starGeo, starMat);
      scene.add(starfield);
    }

    /* 3. Three Fashion Celestial Orbs */
    function buildCelestialPlanets() {
      const texLoader = new THREE.TextureLoader();

      const configs = [
        {
          key: 'singles',
          texKey: 'vulcan',
          name: '公開單打擂台星',
          pos: new THREE.Vector3(-18, 1, 0),
          radius: 4.8,
          color: 0xffaa00,
          glowColor: 0xff7700,
          ringColor: 0xffaa00,
          ringRadius: 8.8
        },
        {
          key: 'doubles',
          texKey: 'cygnus',
          name: '公開雙打雙生星',
          pos: new THREE.Vector3(0, 2.5, -4),
          radius: 5.6,
          color: 0x00f0ff,
          glowColor: 0xb800ff,
          ringColor: 0x00f0ff,
          ringRadius: 10.5
        },
        {
          key: 'prep',
          texKey: 'aegis',
          name: '賽事籌備與大會星',
          pos: new THREE.Vector3(18, -1, 1),
          radius: 4.5,
          color: 0xffd700,
          glowColor: 0xffea00,
          ringColor: 0xffd700,
          ringRadius: 8.2
        }
      ];

      configs.forEach(cfg => {
        const group = new THREE.Group();
        group.position.copy(cfg.pos);

        // Load 2048px Ultra-Res Texture
        const texData = TOURNAMENT_DATA.planet_textures[cfg.texKey];
        const planetTex = texLoader.load(texData);
        planetTex.wrapS = THREE.RepeatWrapping;
        planetTex.wrapT = THREE.ClampToEdgeWrapping;

        const geo = new THREE.SphereGeometry(cfg.radius, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: planetTex,
          roughness: 0.32,
          metalness: 0.45,
          emissive: cfg.color,
          emissiveIntensity: 0.15
        });
        const sphere = new THREE.Mesh(geo, mat);
        sphere.userData = { key: cfg.key, name: cfg.name, group: group };
        group.add(sphere);

        // Atmosphere Fresnel Glow
        const atmosGeo = new THREE.SphereGeometry(cfg.radius * 1.16, 48, 48);
        const atmosMat = new THREE.MeshBasicMaterial({
          color: cfg.glowColor,
          transparent: true,
          opacity: 0.22,
          side: THREE.BackSide,
          blending: THREE.AdditiveBlending
        });
        const atmos = new THREE.Mesh(atmosGeo, atmosMat);
        group.add(atmos);

        // Precision Concentric Rings
        const ringGeo = new THREE.RingGeometry(cfg.ringRadius * 0.84, cfg.ringRadius, 80);
        const ringMat = new THREE.MeshBasicMaterial({
          color: cfg.ringColor,
          side: THREE.DoubleSide,
          transparent: true,
          opacity: 0.5,
          blending: THREE.AdditiveBlending
        });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = Math.PI / 2.3;
        ring.rotation.y = Math.PI / 8;
        group.add(ring);

        // Wireframe Hex Precision Outer Shell
        const wireGeo = new THREE.IcosahedronGeometry(cfg.radius * 1.38, 2);
        const wireMat = new THREE.MeshBasicMaterial({
          color: cfg.color,
          wireframe: true,
          transparent: true,
          opacity: 0.14
        });
        const wireSphere = new THREE.Mesh(wireGeo, wireMat);
        group.add(wireSphere);

        scene.add(group);

        planets[cfg.key] = {
          mesh: sphere,
          group: group,
          atmos: atmos,
          ring: ring,
          wire: wireSphere,
          config: cfg
        };
      });
    }

    /* 4. Quantum Table Tennis Laser Rally */
    function buildPingPongRallySystem() {
      const ballGeo = new THREE.SphereGeometry(0.55, 24, 24);
      const ballMat = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        blending: THREE.AdditiveBlending
      });
      rallyBall = new THREE.Mesh(ballGeo, ballMat);

      const haloGeo = new THREE.SphereGeometry(1.25, 20, 20);
      const haloMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.45,
        blending: THREE.AdditiveBlending
      });
      rallyBall.add(new THREE.Mesh(haloGeo, haloMat));

      scene.add(rallyBall);
    }

    function updateRally(delta) {
      if (!rallyBall || !planets['singles'] || !planets['doubles']) return;

      const p1 = planets['singles'].config.pos;
      const p2 = planets['doubles'].config.pos;

      rallyProgress += delta * 1.6;
      if (rallyProgress > Math.PI * 2) {
        rallyProgress = 0;
      }

      const t = (Math.sin(rallyProgress) + 1) / 2;
      const x = THREE.MathUtils.lerp(p1.x + 5, p2.x - 5, t);
      const z = THREE.MathUtils.lerp(p1.z, p2.z, t);
      const arcHeight = Math.sin(t * Math.PI) * 7.5;
      const y = THREE.MathUtils.lerp(p1.y, p2.y, t) + arcHeight + 3.5;

      rallyBall.position.set(x, y, z);

      if (Math.abs(t - 0.01) < 0.03) {
        if (!rallyBall.userData.hitLeft) {
          rallyBall.userData.hitLeft = true;
          rallyBall.userData.hitRight = false;
          triggerTableTennisHit('pong');
        }
      } else if (Math.abs(t - 0.99) < 0.03) {
        if (!rallyBall.userData.hitRight) {
          rallyBall.userData.hitRight = true;
          rallyBall.userData.hitLeft = false;
          triggerTableTennisHit('ping');
        }
      }
    }

    function triggerTableTennisHit(type) {
      if (type === 'ping') {
        soundSystem.playPing(980, 0.07, false);
      } else {
        soundSystem.playPing(560, 0.09, false);
      }

      rallyRounds++;
      const counterEl = document.getElementById('rally-count');
      if (counterEl) counterEl.textContent = rallyRounds;

      const soundBars = document.getElementById('sound-bars');
      if (soundBars) {
        soundBars.classList.add('active');
        setTimeout(() => soundBars.classList.remove('active'), 250);
      }
    }

    /* Camera Fly-In Animation & Modal Open */
    function focusPlanet(key) {
      const target = planets[key];
      if (!target) return;

      soundSystem.playPing(1150, 0.07, true);

      document.querySelectorAll('.orb-tab').forEach(tab => {
        tab.classList.toggle('active', tab.getAttribute('data-target') === key);
      });

      const pPos = target.config.pos;
      const targetCamPos = new THREE.Vector3(pPos.x, pPos.y + 1.2, pPos.z + target.config.radius * 2.6);

      gsap.to(camera.position, {
        x: targetCamPos.x,
        y: targetCamPos.y,
        z: targetCamPos.z,
        duration: 1.4,
        ease: "power3.inOut"
      });

      gsap.to(controls.target, {
        x: pPos.x,
        y: pPos.y,
        z: pPos.z,
        duration: 1.4,
        ease: "power3.inOut",
        onComplete: () => {
          openModal(key);
        }
      });
    }

    function resetCamera() {
      document.querySelectorAll('.orb-tab').forEach(tab => tab.classList.remove('active'));

      gsap.to(camera.position, {
        x: 0,
        y: 14,
        z: 46,
        duration: 1.6,
        ease: "power3.inOut"
      });

      gsap.to(controls.target, {
        x: 0,
        y: 1,
        z: 0,
        duration: 1.6,
        ease: "power3.inOut"
      });
    }

    /* Click Raycasting on 3D Objects */
    function onPointerDown(event) {
      if (event.target.closest('.ui-layer') || event.target.closest('.hologram-modal') || event.target.closest('.lightbox-overlay')) {
        return;
      }

      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const meshes = Object.values(planets).map(p => p.mesh);
      const intersects = raycaster.intersectObjects(meshes);

      if (intersects.length > 0) {
        const hitKey = intersects[0].object.userData.key;
        if (hitKey) {
          focusPlanet(hitKey);
        }
      }
    }

    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }

    /* Render Loop */
    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      const elapsed = clock.getElapsedTime();

      if (planets['singles']) {
        planets['singles'].mesh.rotation.y += delta * 0.32;
        planets['singles'].wire.rotation.y -= delta * 0.14;
      }
      if (planets['doubles']) {
        planets['doubles'].mesh.rotation.y += delta * 0.26;
        planets['doubles'].ring.rotation.z += delta * 0.08;
      }
      if (planets['prep']) {
        planets['prep'].mesh.rotation.y += delta * 0.2;
        planets['prep'].wire.rotation.x += delta * 0.1;
      }

      if (starfield) {
        starfield.rotation.y = elapsed * 0.012;
      }

      updateRally(delta);

      controls.update();
      renderer.render(scene, camera);
    }

    /* ========================================================================
       MODAL: 1ST / 2ND / 3RD PODIUM INJECTION
       ======================================================================== */
    const modal = document.getElementById('modal');
    const modalSector = document.getElementById('modal-sector');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    const btnCloseModal = document.getElementById('btn-close-modal');

    function openModal(key) {
      const data = TOURNAMENT_DATA.planets[key];
      if (!data) return;

      modalSector.textContent = data.sector;
      modalTitle.textContent = `${data.name} ｜ ${data.subtitle}`;

      const podiumCardsHtml = data.rankings.map(item => {
        let photoSection = '';
        if (item.photo_extra) {
          photoSection = `
            <div class="dual-photo-box">
              <div class="mini-photo-item" onclick="openLightbox('${item.photo}')">
                <img src="${item.photo}" alt="季軍第一組" loading="lazy">
              </div>
              <div class="mini-photo-item" onclick="openLightbox('${item.photo_extra}')">
                <img src="${item.photo_extra}" alt="季軍第二組" loading="lazy">
              </div>
            </div>
          `;
        } else if (item.photo) {
          photoSection = `
            <div class="card-photo-box" onclick="openLightbox('${item.photo}')">
              <img src="${item.photo}" alt="${item.name}" loading="lazy">
              <div class="card-photo-overlay">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
                放大預覽
              </div>
            </div>
          `;
        }

        return `
          <div class="podium-card rank-${item.rank}-card">
            <div class="card-top-badge">
              <div class="badge-rank-title">
                ${item.rank === 1 ? '🥇' : item.rank === 2 ? '🥈' : '🥉'} ${item.rank_title}
              </div>
              <span class="badge-label">${item.badge}</span>
            </div>
            ${photoSection}
            <div class="card-info">
              <div class="winner-name-text">${item.name}</div>
              <div class="winner-desc-text">${item.desc}</div>
            </div>
          </div>
        `;
      }).join('');

      let extraSection = '';
      if (data.group_photo) {
        extraSection = `
          <div class="group-photo-section">
            <div class="group-section-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
              全體選手與榮譽頒獎大合照
            </div>
            <div class="group-photo-container" onclick="openLightbox('${data.group_photo}')">
              <img src="${data.group_photo}" alt="${data.group_caption}">
              <div class="group-caption">${data.group_caption}</div>
            </div>
          </div>
        `;
      } else if (data.extra_photos && data.extra_photos.length > 0) {
        const prepThumbs = data.extra_photos.map((src, idx) => `
          <div class="prep-thumb-item" onclick="openLightbox('${src}')">
            <img src="${src}" alt="賽事準備實況 ${idx+1}">
          </div>
        `).join('');

        extraSection = `
          <div class="group-photo-section">
            <div class="group-section-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>
              賽事實況與選手熱身花絮精選
            </div>
            <div class="prep-gallery-grid">
              ${prepThumbs}
            </div>
          </div>
        `;
      }

      modalContent.innerHTML = `
        <div class="modal-lead-desc">${data.desc}</div>
        <div class="podium-grid">
          ${podiumCardsHtml}
        </div>
        ${extraSection}
      `;

      modal.classList.add('open');
    }

    function closeModal() {
      modal.classList.remove('open');
    }

    btnCloseModal.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    /* Lightbox */
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    window.openLightbox = function(src) {
      if (!src) return;
      lightboxImg.src = src;
      lightbox.classList.add('active');
    };

    lightbox.addEventListener('click', () => {
      lightbox.classList.remove('active');
    });

    /* Tab Controls */
    document.querySelectorAll('.orb-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const key = tab.getAttribute('data-target');
        focusPlanet(key);
      });
    });

    /* Header Controls */
    document.getElementById('btn-reset').addEventListener('click', resetCamera);

    document.getElementById('btn-hit').addEventListener('click', () => {
      triggerTableTennisHit(Math.random() > 0.5 ? 'ping' : 'pong');
    });

    const btnSound = document.getElementById('btn-sound');
    const soundText = document.getElementById('sound-text');
    btnSound.addEventListener('click', () => {
      const isOn = soundSystem.toggle();
      soundText.textContent = `桌球音效: ${isOn ? '開' : '關'}`;
      btnSound.classList.toggle('active', isOn);
    });

    const btnFullscreen = document.getElementById('btn-fullscreen');
    btnFullscreen.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === '1') focusPlanet('singles');
      if (e.key === '2') focusPlanet('doubles');
      if (e.key === '3') focusPlanet('prep');
      if (e.key === 'Escape') {
        closeModal();
        lightbox.classList.remove('active');
      }
      if (e.key === ' ') {
        triggerTableTennisHit('smash');
      }
    });

    window.addEventListener('load', () => {
      initWebGL();
    });
  </script>
</body>
</html>
'''

# 1. 寫入到 GitHub 專案資料夾 index.html
gh_index_path = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\index.html'
with open(gh_index_path, 'w', encoding='utf-8') as f:
    f.write(html_code)
print(f"Generated GitHub index.html: {gh_index_path}, Size: {os.path.getsize(gh_index_path)/1024:.2f} KB")

# 2. 寫入到工作區根目錄 index.html
ws_index_path = r'E:\2026GEM-SKILL\index.html'
with open(ws_index_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

# 3. 更新工作區 115年度連江縣體育季桌球錦標賽_3D太空展館.html
ws_demo_path = r'E:\2026GEM-SKILL\115年度連江縣體育季桌球錦標賽_3D太空展館.html'
with open(ws_demo_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

# 4. 同步至 Artifact 目錄
artifact_path = r'C:\Users\A1547\.gemini\antigravity\brain\01ae478b-5840-417e-8783-95119ece3e7b\115年度連江縣體育季桌球錦標賽_3D太空展館.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html_code)
print("All index.html files deployed successfully!")
