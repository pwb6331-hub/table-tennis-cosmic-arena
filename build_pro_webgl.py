import json, os

data_path = r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\assets\github_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    full_data = json.load(f)

html_code = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>115年度連江縣體育季桌球錦標賽 ｜ 3D 星際太空展館 (Pro WebGL Edition)</title>
  <!-- Google Fonts: Noto Sans TC (思源黑體), Orbitron, Rajdhani -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
  <!-- Three.js r128 & OrbitControls -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <!-- GSAP 3.12.5 -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

  <style>
    :root {
      --primary: #00f0ff;
      --primary-glow: rgba(0, 240, 255, 0.45);
      --amber-gold: #ffaa00;
      --amber-glow: rgba(255, 170, 0, 0.45);
      --amethyst: #b800ff;
      --gold-pure: #ffd700;
      --silver-pure: #e2e8f0;
      --bronze-pure: #e67e22;
      --bg-dark: #02040a;
      --hud-bg: rgba(6, 11, 24, 0.84);
      --hud-border: rgba(0, 240, 255, 0.25);
      --card-bg: rgba(10, 16, 32, 0.95);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --font-tc: 'Noto Sans TC', "Source Han Sans TC", "Source Han Sans", -apple-system, BlinkMacSystemFont, sans-serif;
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
      text-rendering: optimizeLegibility;
    }

    body, html {
      width: 100%;
      height: 100%;
      height: 100dvh;
      overflow: hidden;
      background-color: var(--bg-dark);
      font-family: var(--font-tc);
      color: var(--text-main);
      touch-action: none;
    }

    /* QR Code Share Modal for Mobile/Tablet/Desktop Connection */
    .qr-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 220;
      background: rgba(2, 4, 10, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .qr-modal.active {
      display: flex;
    }
    .qr-card {
      background: rgba(10, 18, 36, 0.98);
      border: 1px solid var(--primary);
      border-radius: 18px;
      padding: 26px 28px;
      max-width: 420px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      box-shadow: 0 0 50px rgba(0, 240, 255, 0.3);
      text-align: center;
    }
    .qr-card h3 {
      font-size: 19px;
      font-weight: 900;
      color: #fff;
      letter-spacing: 1px;
    }
    .qr-card p {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }
    .qr-box {
      background: #ffffff;
      padding: 14px;
      border-radius: 14px;
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .qr-box img {
      width: 200px;
      height: 200px;
      display: block;
    }
    .qr-url-box {
      width: 100%;
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-radius: 8px;
      padding: 10px 12px;
      font-family: var(--font-tech);
      font-size: 12px;
      color: var(--primary);
      word-break: break-all;
      user-select: all;
      -webkit-user-select: all;
    }
    .qr-actions {
      display: flex;
      gap: 10px;
      width: 100%;
    }
    .qr-actions button {
      flex: 1;
      justify-content: center;
      padding: 10px 14px;
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

    /* 3D Spatial Floating Anchors Layer */
    #spatial-anchors {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 5;
      pointer-events: none;
      overflow: hidden;
    }

    .spatial-label {
      position: absolute;
      top: 0;
      left: 0;
      pointer-events: auto;
      cursor: pointer;
      will-change: transform, opacity;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: filter 0.25s ease;
    }

    .spatial-label:hover {
      filter: brightness(1.25) drop-shadow(0 0 14px var(--primary));
      z-index: 8;
    }

    .spatial-pill {
      background: rgba(5, 10, 22, 0.86);
      border: 1px solid rgba(255, 255, 255, 0.22);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      padding: 6px 14px;
      border-radius: 30px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.65);
      white-space: nowrap;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .spatial-label.hit-pulse .spatial-pill {
      transform: scale(1.14);
      border-color: #ffffff !important;
      box-shadow: 0 0 28px rgba(255, 255, 255, 0.85) !important;
    }

    .spatial-label[data-key="singles"] .spatial-pill {
      border-color: rgba(255, 170, 0, 0.65);
      box-shadow: 0 0 18px rgba(255, 170, 0, 0.25);
    }
    .spatial-label[data-key="doubles"] .spatial-pill {
      border-color: rgba(0, 240, 255, 0.65);
      box-shadow: 0 0 18px rgba(0, 240, 255, 0.25);
    }
    .spatial-label[data-key="prep"] .spatial-pill {
      border-color: rgba(255, 215, 0, 0.65);
      box-shadow: 0 0 18px rgba(255, 215, 0, 0.25);
    }

    .spatial-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }

    .spatial-title {
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.6px;
      color: #fff;
    }

    .spatial-champ {
      font-size: 11px;
      font-weight: 500;
      color: var(--text-muted);
      padding-left: 6px;
      border-left: 1px solid rgba(255, 255, 255, 0.18);
    }

    .spatial-stem {
      width: 1.5px;
      height: 22px;
      background: linear-gradient(180deg, rgba(255,255,255,0.6) 0%, transparent 100%);
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
      padding: 15px 26px;
      background: linear-gradient(180deg, rgba(2, 4, 10, 0.95) 0%, rgba(2, 4, 10, 0.55) 80%, transparent 100%);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(0, 240, 255, 0.16);
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .badge-year {
      background: linear-gradient(135deg, #ff0055, #ff7700);
      color: #fff;
      font-family: var(--font-tech);
      font-size: 13px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 1px;
      box-shadow: 0 0 16px rgba(255, 0, 85, 0.5);
    }

    .title-box h1 {
      font-size: 20px;
      font-weight: 900;
      letter-spacing: 1.5px;
      background: linear-gradient(90deg, #ffffff 0%, #00f0ff 55%, #ffd700 100%);
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
      font-family: var(--font-tc);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(4px);
    }

    .btn-icon:hover, .btn-icon.active {
      background: rgba(0, 240, 255, 0.24);
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
      padding: 5px 10px;
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

    .sound-bars.active .sound-bar:nth-child(1) { animation: bounce 0.35s infinite alternate ease-in-out; }
    .sound-bars.active .sound-bar:nth-child(2) { animation: bounce 0.5s infinite alternate ease-in-out 0.12s; }
    .sound-bars.active .sound-bar:nth-child(3) { animation: bounce 0.42s infinite alternate ease-in-out 0.24s; }

    @keyframes bounce {
      0% { height: 4px; }
      100% { height: 14px; }
    }

    /* Telemetry & Rally Stats HUD */
    .telemetry-hud {
      position: absolute;
      top: 84px;
      left: 26px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      pointer-events: auto;
    }

    .rally-hud {
      background: var(--hud-bg);
      border: 1px solid var(--hud-border);
      padding: 10px 16px;
      border-radius: 10px;
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
      display: flex;
      justify-content: space-between;
      gap: 12px;
    }

    .fps-badge {
      color: #10b981;
      font-weight: 800;
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

    .rally-route-badge {
      font-size: 11px;
      font-weight: 700;
      color: #ffd700;
      letter-spacing: 0.5px;
      margin-top: 2px;
    }

    /* ========================================================================
       BOTTOM-RIGHT OFFICIAL SIGNATURE SEAL (連江縣桌球委員會 落款字樣)
       ======================================================================== */
    .map-signature-seal {
      position: absolute;
      bottom: 22px;
      right: 26px;
      z-index: 25;
      pointer-events: auto;
      display: flex;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, rgba(10, 18, 36, 0.92) 0%, rgba(5, 10, 22, 0.96) 100%);
      border: 1px solid rgba(255, 215, 0, 0.48);
      border-left: 3px solid #ffd700;
      padding: 8px 16px;
      border-radius: 10px;
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.65), 0 0 18px rgba(255, 215, 0, 0.15);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }

    .seal-emblem {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255, 215, 0, 0.22) 0%, rgba(255, 170, 0, 0.05) 100%);
      border: 1px solid rgba(255, 215, 0, 0.55);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      flex-shrink: 0;
    }

    .seal-text-group {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }

    .seal-main {
      font-size: 15px;
      font-weight: 900;
      letter-spacing: 2px;
      background: linear-gradient(90deg, #ffffff 0%, #ffe680 55%, #ffd700 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      white-space: nowrap;
    }

    .seal-sub {
      font-family: var(--font-tech);
      font-size: 9px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.8px;
      white-space: nowrap;
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
      max-width: 880px;
      width: 100%;
    }

    .orb-tab {
      flex: 1;
      min-width: 190px;
      max-width: 270px;
      background: var(--hud-bg);
      border: 1px solid var(--hud-border);
      border-radius: 12px;
      padding: 12px 16px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 14px;
      transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
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
      opacity: 0.45;
      transition: opacity 0.3s ease;
    }

    .orb-tab.tab-singles::before { background: var(--amber-gold); }
    .orb-tab.tab-doubles::before { background: var(--primary); }
    .orb-tab.tab-prep::before { background: var(--gold-pure); }

    .orb-tab:hover, .orb-tab.active {
      transform: translateY(-4px);
      background: rgba(12, 22, 44, 0.96);
      border-color: rgba(0, 240, 255, 0.75);
      box-shadow: 0 8px 26px rgba(0, 240, 255, 0.25);
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
       FASHION-TECH HOLOGRAM MODAL - UNCROPPED FULL PHOTO PODIUM SHOWCASE
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
      transition: opacity 0.32s ease;
    }

    .hologram-modal.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-card {
      width: 100%;
      max-width: 1220px;
      max-height: 92vh;
      background: rgba(8, 14, 28, 0.97);
      border: 1px solid var(--hud-border);
      border-radius: 18px;
      box-shadow: 0 0 60px rgba(0, 240, 255, 0.22), inset 0 0 25px rgba(0, 240, 255, 0.06);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.94) translateY(16px);
      transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hologram-modal.open .modal-card {
      transform: scale(1) translateY(0);
    }

    .modal-header {
      padding: 16px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(0, 0, 0, 0.45);
      flex-shrink: 0;
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
      font-size: 21px;
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
      background: rgba(255, 0, 85, 0.75);
      border-color: #ff0055;
      transform: rotate(90deg);
    }

    .modal-body {
      padding: 22px 28px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    .modal-lead-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.65;
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
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    }

    .podium-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.65);
    }

    /* Gold Card (1st) */
    .podium-card.rank-1-card {
      border-color: rgba(255, 215, 0, 0.65);
      box-shadow: 0 0 30px rgba(255, 215, 0, 0.15);
      background: linear-gradient(180deg, rgba(35, 28, 12, 0.96) 0%, rgba(12, 18, 36, 0.98) 100%);
    }
    .podium-card.rank-1-card:hover {
      border-color: #ffd700;
      box-shadow: 0 0 45px rgba(255, 215, 0, 0.35);
    }

    /* Silver Card (2nd) */
    .podium-card.rank-2-card {
      border-color: rgba(226, 232, 240, 0.5);
      box-shadow: 0 0 25px rgba(226, 232, 240, 0.12);
      background: linear-gradient(180deg, rgba(22, 28, 38, 0.96) 0%, rgba(12, 18, 36, 0.98) 100%);
    }
    .podium-card.rank-2-card:hover {
      border-color: #ffffff;
      box-shadow: 0 0 38px rgba(226, 232, 240, 0.3);
    }

    /* Bronze Card (3rd) */
    .podium-card.rank-3-card {
      border-color: rgba(230, 126, 34, 0.5);
      box-shadow: 0 0 25px rgba(230, 126, 34, 0.12);
      background: linear-gradient(180deg, rgba(34, 20, 14, 0.96) 0%, rgba(12, 18, 36, 0.98) 100%);
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
      background: rgba(0, 0, 0, 0.35);
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

    /* 100% UNCROPPED FULL PHOTO BOX (object-fit: contain) */
    .card-photo-box {
      width: 100%;
      height: 350px;
      position: relative;
      overflow: hidden;
      background: radial-gradient(circle at center, #0e1a32 0%, #040710 100%);
      cursor: zoom-in;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .card-photo-box img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 6px;
      transition: transform 0.35s ease;
    }

    .card-photo-box:hover img {
      transform: scale(1.03);
    }

    .card-photo-overlay {
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.72);
      border: 1px solid rgba(255, 255, 255, 0.24);
      border-radius: 20px;
      padding: 4px 10px;
      font-size: 11px;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 4px;
      backdrop-filter: blur(4px);
    }

    /* 100% UNCROPPED DUAL PHOTO BOX FOR JOINT 3RD PLACE */
    .dual-photo-box {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      height: 350px;
      padding: 8px;
      background: radial-gradient(circle at center, #0e1a32 0%, #040710 100%);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .dual-photo-box .mini-photo-item {
      position: relative;
      overflow: hidden;
      cursor: zoom-in;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 4px;
    }

    .dual-photo-box .mini-photo-item img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 4px;
      transition: transform 0.3s ease;
    }

    .dual-photo-box .mini-photo-item:hover img {
      transform: scale(1.04);
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

    /* Group Photos & Extra Carousel - Uncropped Full Display */
    .group-photo-section {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
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
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: zoom-in;
      background: radial-gradient(circle at center, #0c162c 0%, #040710 100%);
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
    }

    .group-photo-container img {
      width: 100%;
      height: auto;
      max-height: 540px;
      object-fit: contain;
      display: block;
      border-radius: 6px;
      transition: transform 0.3s ease;
    }

    .group-photo-container:hover img {
      transform: scale(1.015);
    }

    .group-caption {
      width: 100%;
      text-align: center;
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid rgba(0, 240, 255, 0.2);
      border-radius: 6px;
      padding: 7px 14px;
      font-size: 13px;
      font-weight: 600;
      color: #f0f6fc;
    }

    /* Uncropped Prep Gallery Grid */
    .prep-gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
      gap: 14px;
    }

    .prep-thumb-item {
      height: 220px;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      cursor: zoom-in;
      position: relative;
      background: radial-gradient(circle at center, #0e1a32 0%, #040710 100%);
      padding: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.25s ease;
    }

    .prep-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 6px;
      transition: transform 0.3s ease;
    }

    .prep-thumb-item:hover {
      border-color: var(--primary);
      box-shadow: 0 0 16px var(--primary-glow);
    }

    .prep-thumb-item:hover img {
      transform: scale(1.04);
    }

    /* Modal Footer Signature */
    .modal-footer-signature {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      padding-top: 8px;
      border-top: 1px dashed rgba(255, 255, 255, 0.12);
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #ffd700;
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
      max-width: 94vw;
      max-height: 90vh;
      object-fit: contain;
      border-radius: 12px;
      box-shadow: 0 0 40px rgba(0, 240, 255, 0.4);
      border: 1px solid rgba(0, 240, 255, 0.5);
    }

    /* Responsive Mobile / Tablet */
    @media (max-width: 900px) {
      .podium-grid {
        grid-template-columns: 1fr;
      }
      .card-photo-box, .dual-photo-box {
        height: 310px;
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
      .telemetry-hud {
        top: 66px;
        left: 16px;
      }
      .spatial-champ {
        display: none;
      }
      .controls-hint {
        display: none;
      }
      .map-signature-seal {
        bottom: 92px;
        right: 14px;
        padding: 6px 12px;
      }
      .seal-main {
        font-size: 13px;
      }
      .seal-sub {
        display: none;
      }
      .nav-orbs {
        gap: 8px;
      }
      .orb-tab {
        min-width: 120px;
        padding: 8px 10px;
      }
      .orb-tab-icon {
        width: 30px;
        height: 30px;
        font-size: 15px;
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

  <!-- 3D Projected Spatial Labels -->
  <div id="spatial-anchors">
    <div class="spatial-label" id="anchor-singles" data-key="singles">
      <div class="spatial-pill">
        <span class="spatial-dot" style="background:#ffaa00;box-shadow:0 0 8px #ffaa00;"></span>
        <span class="spatial-title">公開單打擂台星</span>
        <span class="spatial-champ">🥇 張正輝</span>
      </div>
      <div class="spatial-stem"></div>
    </div>

    <div class="spatial-label" id="anchor-doubles" data-key="doubles">
      <div class="spatial-pill">
        <span class="spatial-dot" style="background:#00f0ff;box-shadow:0 0 8px #00f0ff;"></span>
        <span class="spatial-title">公開雙打雙生星</span>
        <span class="spatial-champ">🥇 曹常容／張正輝</span>
      </div>
      <div class="spatial-stem"></div>
    </div>

    <div class="spatial-label" id="anchor-prep" data-key="prep">
      <div class="spatial-pill">
        <span class="spatial-dot" style="background:#ffd700;box-shadow:0 0 8px #ffd700;"></span>
        <span class="spatial-title">賽事籌備與大會星</span>
        <span class="spatial-champ">🛡️ 南竿體育館</span>
      </div>
      <div class="spatial-stem"></div>
    </div>
  </div>

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
          <button class="btn-icon active" id="btn-sound" title="切換立體聲音效">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
            <span id="sound-text">桌球音效: 開</span>
          </button>
        </div>

        <button class="btn-icon" id="btn-theme" title="變換星際背景與星雲主題 (Key B)">
          <span>🌌 星雲變換: 極光深空</span>
        </button>

        <button class="btn-icon" id="btn-hit" title="擊球加速模擬 (Space)">
          <span>🏓 擊球模擬</span>
        </button>

        <button class="btn-icon" id="btn-reset" title="重置為全景視角">
          <span>🪐 全景星圖</span>
        </button>

        <button class="btn-icon" id="btn-qr" title="手機/平板/桌機 GitHub 連線網址與 QR Code">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M3 11h8V3H3v8zm2-6h4v4H5V5zM3 21h8v-8H3v8zm2-6h4v4H5v-4zM13 3v8h8V3h-8zm6 6h-4V5h4v4zM13 13h2v2h-2zM15 15h2v2h-2zM13 17h2v2h-2zM17 17h2v2h-2zM19 19h2v2h-2zM15 19h2v2h-2zM17 13h2v2h-2zM19 15h2v2h-2z"/></svg>
          <span>📱 跨裝置連線</span>
        </button>

        <button class="btn-icon" id="btn-fullscreen" title="全螢幕切換">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
        </button>
      </div>
    </header>

    <!-- Telemetry & Rally Stats Tracker -->
    <div class="telemetry-hud">
      <div class="rally-hud">
        <div class="rally-title">
          <span>TRI-PLANET RALLY</span>
          <span class="fps-badge" id="fps-counter">60 FPS</span>
        </div>
        <div class="rally-counter"><span id="rally-count">56</span> <span class="rally-unit">HITS</span></div>
        <div class="rally-route-badge" id="rally-route">🏓 單打星 ➔ 雙打星</div>
      </div>
    </div>

    <!-- Bottom-Right Official Signature Seal (地圖右下角「連江縣桌球委員會」落款字樣) -->
    <div class="map-signature-seal" title="承辦單位：連江縣桌球委員會">
      <div class="seal-emblem">🏓</div>
      <div class="seal-text-group">
        <div class="seal-main">連江縣桌球委員會</div>
        <div class="seal-sub">LIENCHIANG TABLE TENNIS COMMITTEE</div>
      </div>
    </div>

    <!-- Bottom Navigation & Planet Selector -->
    <footer class="hud-footer">
      <div class="nav-orbs">
        <div class="orb-tab tab-singles" data-target="singles">
          <div class="orb-tab-icon" style="color: #ffaa00; border-color: rgba(255,170,0,0.4);">🔥</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 01 [KEY 1]</div>
            <div class="tab-title">公開單打擂台星</div>
          </div>
        </div>

        <div class="orb-tab tab-doubles" data-target="doubles">
          <div class="orb-tab-icon" style="color: #00f0ff; border-color: rgba(0,240,255,0.4);">⚡</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 02 [KEY 2]</div>
            <div class="tab-title">公開雙打雙生星</div>
          </div>
        </div>

        <div class="orb-tab tab-prep" data-target="prep">
          <div class="orb-tab-icon" style="color: #ffd700; border-color: rgba(255,215,0,0.4);">🛡️</div>
          <div class="orb-tab-info">
            <div class="tab-sub">SECTOR 03 [KEY 3]</div>
            <div class="tab-title">賽事籌備與大會星</div>
          </div>
        </div>
      </div>

      <div class="controls-hint">
        <div class="hint-item"><span class="hint-key">拖曳</span> 360° 旋轉視角</div>
        <div class="hint-item"><span class="hint-key">滾輪/雙指</span> 縮放星系</div>
        <div class="hint-item"><span class="hint-key">點擊星球/標籤</span> 檢視前三名頒獎台</div>
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
        <button class="btn-close" id="btn-close-modal" title="關閉 (ESC)">✕</button>
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

  <!-- Cross-Device GitHub Pages QR Modal -->
  <div class="qr-modal" id="qr-modal">
    <div class="qr-card">
      <h3>📱 手機／平板／桌機 GitHub 連線</h3>
      <p>使用手機或平板相機掃描下方 QR Code，或直接點擊複製網址，即可跨裝置開啟 3D 星際太空展館：</p>
      <div class="qr-box">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=https://pwb6331-hub.github.io/table-tennis-cosmic-arena/" alt="GitHub Pages QR Code">
      </div>
      <div class="qr-url-box" id="github-url-text">https://pwb6331-hub.github.io/table-tennis-cosmic-arena/</div>
      <div class="qr-actions">
        <button class="btn-icon active" id="btn-copy-url">📋 複製 GitHub 網址</button>
        <button class="btn-icon" id="btn-close-qr">關閉</button>
      </div>
    </div>
  </div>

  <script>
    /* ========================================================================
       1. DATA REPOSITORY (2048px Planet Textures, 4K Space BG, Uncropped Photos)
       ======================================================================== */
    const TOURNAMENT_DATA = ''' + json.dumps(full_data, ensure_ascii=False) + ''';

    /* ========================================================================
       2. CUSTOM GLSL SHADER LIBRARY (True Fresnel Rim + Dynamic Aurora Nebula)
       ======================================================================== */
    const ShaderLibrary = {
      fresnelAtmosphere: {
        vertexShader: `
          varying vec3 vNormal;
          varying vec3 vPositionNormal;
          void main() {
            vNormal = normalize(normalMatrix * normal);
            vPositionNormal = normalize((modelViewMatrix * vec4(position, 1.0)).xyz);
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
          }
        `,
        fragmentShader: `
          uniform vec3 glowColor;
          uniform float intensity;
          uniform float power;
          varying vec3 vNormal;
          varying vec3 vPositionNormal;
          void main() {
            float fresnel = pow(1.0 - abs(dot(vNormal, vPositionNormal)), power);
            gl_FragColor = vec4(glowColor, fresnel * intensity);
          }
        `
      },
      dynamicNebulaDome: {
        vertexShader: `
          varying vec3 vWorldPos;
          varying vec2 vUv;
          void main() {
            vUv = uv;
            vec4 worldPosition = modelMatrix * vec4(position, 1.0);
            vWorldPos = normalize(worldPosition.xyz);
            gl_Position = projectionMatrix * viewMatrix * worldPosition;
          }
        `,
        fragmentShader: `
          uniform float uTime;
          uniform vec3 uColorA;
          uniform vec3 uColorB;
          uniform vec3 uColorC;
          varying vec3 vWorldPos;
          varying vec2 vUv;

          // Fast 3D trigonometric wave interference for silky cosmic aurora
          float cosmicWave(vec3 p, float t) {
            float w1 = sin(p.x * 3.2 + t * 0.45) * cos(p.y * 2.8 - t * 0.35);
            float w2 = sin(p.z * 4.1 - t * 0.5) * cos(p.x * 2.2 + t * 0.28);
            float w3 = cos((p.x + p.y + p.z) * 2.6 + t * 0.6);
            return (w1 + w2 + w3) * 0.333;
          }

          void main() {
            float n1 = cosmicWave(vWorldPos * 1.4, uTime);
            float n2 = cosmicWave(vWorldPos * 2.8 + vec3(n1), uTime * 1.3);
            float auroraBand = smoothstep(-0.3, 0.75, n1 + n2 * 0.6);
            float equatorGlow = pow(1.0 - abs(vWorldPos.y), 2.2);

            vec3 col = mix(uColorA, uColorB, auroraBand);
            col = mix(col, uColorC, smoothstep(0.2, 0.9, n2) * equatorGlow);
            float alpha = (auroraBand * 0.35 + equatorGlow * 0.22);
            gl_FragColor = vec4(col, alpha);
          }
        `
      }
    };

    /* ========================================================================
       3. SPATIAL WEB AUDIO SYNTHESIZER (Physical Table Tennis Acoustics + Pan)
       ======================================================================== */
    class SpatialAudioEngine {
      constructor() {
        this.ctx = null;
        this.enabled = true;
        this.masterGain = null;
        this.noiseBuffer = null;
      }

      init() {
        if (this.ctx) return;
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.ctx = new AudioContext();

        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.setValueAtTime(0.75, this.ctx.currentTime);
        this.masterGain.connect(this.ctx.destination);

        const bufferSize = this.ctx.sampleRate * 0.05;
        this.noiseBuffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = this.noiseBuffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
          data[i] = Math.random() * 2 - 1;
        }

        this.startCosmicDrone();
      }

      startCosmicDrone() {
        if (!this.ctx) return;
        try {
          const osc1 = this.ctx.createOscillator();
          const osc2 = this.ctx.createOscillator();
          const filter = this.ctx.createBiquadFilter();
          const droneGain = this.ctx.createGain();

          osc1.type = 'sine';
          osc1.frequency.setValueAtTime(44, this.ctx.currentTime);
          osc2.type = 'triangle';
          osc2.frequency.setValueAtTime(46.5, this.ctx.currentTime);

          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(105, this.ctx.currentTime);
          droneGain.gain.setValueAtTime(0.07, this.ctx.currentTime);

          osc1.connect(filter);
          osc2.connect(filter);
          filter.connect(droneGain);
          droneGain.connect(this.masterGain);

          osc1.start();
          osc2.start();
        } catch (e) {
          console.warn("Drone init skipped:", e);
        }
      }

      playPing(frequency = 960, decay = 0.075, isSmash = false, panValue = 0) {
        if (!this.enabled) return;
        this.init();
        if (this.ctx.state === 'suspended') this.ctx.resume();

        const now = this.ctx.currentTime;
        const panner = this.ctx.createStereoPanner ? this.ctx.createStereoPanner() : null;
        const targetNode = panner || this.masterGain;
        if (panner) {
          panner.pan.setValueAtTime(Math.max(-1, Math.min(1, panValue)), now);
          panner.connect(this.masterGain);
        }

        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const filter = this.ctx.createBiquadFilter();

        osc.type = isSmash ? 'sawtooth' : 'sine';
        osc.frequency.setValueAtTime(frequency, now);
        osc.frequency.exponentialRampToValueAtTime(330, now + decay);

        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(isSmash ? 1450 : 1020, now);
        filter.Q.setValueAtTime(4.0, now);

        gain.gain.setValueAtTime(isSmash ? 0.55 : 0.38, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + decay);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(targetNode);

        osc.start(now);
        osc.stop(now + decay);

        const popOsc = this.ctx.createOscillator();
        const popGain = this.ctx.createGain();
        popOsc.frequency.setValueAtTime(440, now);
        popOsc.frequency.exponentialRampToValueAtTime(150, now + 0.038);
        popGain.gain.setValueAtTime(0.24, now);
        popGain.gain.exponentialRampToValueAtTime(0.001, now + 0.038);
        popOsc.connect(popGain);
        popGain.connect(targetNode);
        popOsc.start(now);
        popOsc.stop(now + 0.038);

        if (this.noiseBuffer) {
          const noise = this.ctx.createBufferSource();
          noise.buffer = this.noiseBuffer;
          const nFilter = this.ctx.createBiquadFilter();
          nFilter.type = 'highpass';
          nFilter.frequency.setValueAtTime(2400, now);
          const nGain = this.ctx.createGain();
          nGain.gain.setValueAtTime(isSmash ? 0.22 : 0.1, now);
          nGain.gain.exponentialRampToValueAtTime(0.001, now + 0.025);
          noise.connect(nFilter);
          nFilter.connect(nGain);
          nGain.connect(targetNode);
          noise.start(now);
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

    const soundSystem = new SpatialAudioEngine();

    /* ========================================================================
       4. PRO WEBGL 3D ENGINE (Dynamic Skybox + 3-Planet Table Tennis Rally)
       ======================================================================== */
    const container = document.getElementById('webgl-canvas');
    let scene, camera, renderer, controls;
    let planets = {};
    let planetMeshes = [];
    let raycaster, mouse;
    let bgSphereMesh, nebulaDomeMesh, starfield, starfieldOuter;
    let cyanRimLight, goldRimLight;
    let rallyBall, rallyHalo, trailLine, trailPositions, impactRing, sparkParticles;
    let rallyProgress = 0;
    let currentLegIndex = 0;
    let rallyRounds = 56;
    let isModalOpen = false;
    let isPageHidden = false;
    let hoveredPlanetKey = null;

    // 4 Switchable & Continuously Animated Cosmic Themes
    const COSMIC_THEMES = [
      {
        name: "極光深空",
        fogColor: 0x02040a,
        colorA: new THREE.Color(0x03091e),
        colorB: new THREE.Color(0x00d8ff),
        colorC: new THREE.Color(0x9d00ff),
        light1: 0x00f0ff,
        light2: 0xffaa00
      },
      {
        name: "烈焰超新星",
        fogColor: 0x0c0306,
        colorA: new THREE.Color(0x1f040a),
        colorB: new THREE.Color(0xff3300),
        colorC: new THREE.Color(0xffcc00),
        light1: 0xff4400,
        light2: 0xffd700
      },
      {
        name: "翡翠量子星河",
        fogColor: 0x020b09,
        colorA: new THREE.Color(0x021b16),
        colorB: new THREE.Color(0x00ffaa),
        colorC: new THREE.Color(0x0088ff),
        light1: 0x00ffaa,
        light2: 0x00aaff
      },
      {
        name: "紫曜星際風暴",
        fogColor: 0x070210,
        colorA: new THREE.Color(0x140428),
        colorB: new THREE.Color(0xff00aa),
        colorC: new THREE.Color(0x5500ff),
        light1: 0xff00aa,
        light2: 0x00f0ff
      }
    ];
    let currentThemeIndex = 0;

    // 3-Planet Rally Sequence: Singles (0) -> Doubles (1) -> Prep (2) -> Singles (0)
    const RALLY_ORDER = ['singles', 'doubles', 'prep'];
    const RALLY_LABELS = {
      'singles': '公開單打星',
      'doubles': '公開雙打星',
      'prep': '賽事大會星'
    };

    // Pre-allocated Scratch Vectors for Zero-GC Render Loop
    const _projVec = new THREE.Vector3();
    const _pStart = new THREE.Vector3();
    const _pEnd = new THREE.Vector3();
    const _pMid = new THREE.Vector3();
    const _pointerDownPos = { x: 0, y: 0, time: 0 };
    const TRAIL_LENGTH = 36;
    const SPARK_COUNT = 28;
    let sparkVelocities = [];

    // FPS Telemetry state
    let frameCount = 0;
    let lastFpsTime = performance.now();
    const fpsEl = document.getElementById('fps-counter');
    const routeEl = document.getElementById('rally-route');

    function initWebGL() {
      scene = new THREE.Scene();
      scene.fog = new THREE.FogExp2(0x02040a, 0.0035);

      camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1200);
      camera.position.set(0, 15, 48);

      renderer = new THREE.WebGLRenderer({
        antialias: true,
        alpha: false,
        powerPreference: "high-performance",
        stencil: false
      });
      renderer.setClearColor(0x02040a, 1);
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.32;
      container.appendChild(renderer.domElement);

      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.maxDistance = 135;
      controls.minDistance = 6;
      controls.maxPolarAngle = Math.PI / 2 + 0.15;

      raycaster = new THREE.Raycaster();
      mouse = new THREE.Vector2();

      // Studio-grade 3-Point Celestial Lighting
      const ambientLight = new THREE.AmbientLight(0x283855, 1.45);
      scene.add(ambientLight);

      const sunLight = new THREE.DirectionalLight(0xffffff, 2.5);
      sunLight.position.set(35, 45, 25);
      scene.add(sunLight);

      cyanRimLight = new THREE.PointLight(0x00f0ff, 3.4, 130);
      cyanRimLight.position.set(-25, 12, -20);
      scene.add(cyanRimLight);

      goldRimLight = new THREE.PointLight(0xffaa00, 3.0, 130);
      goldRimLight.position.set(28, -12, -15);
      scene.add(goldRimLight);

      buildDynamicSpaceBackground();
      buildStarfields();
      buildCelestialPlanets();
      buildTriPlanetRallySystem();

      window.addEventListener('resize', onWindowResize, { passive: true });
      renderer.domElement.addEventListener('pointerdown', onPointerDown, { passive: true });
      renderer.domElement.addEventListener('pointerup', onPointerUp, { passive: true });
      renderer.domElement.addEventListener('pointermove', onPointerMove, { passive: true });

      document.addEventListener('visibilitychange', () => {
        isPageHidden = document.hidden;
        if (!isPageHidden) clock.getDelta();
      });

      animate();
    }

    /* 1. Dynamic Rotating Skybox + Real-time GLSL Flowing Aurora Nebula Dome */
    function buildDynamicSpaceBackground() {
      if (TOURNAMENT_DATA.space_bg) {
        const textureLoader = new THREE.TextureLoader();
        textureLoader.load(TOURNAMENT_DATA.space_bg, (tex) => {
          tex.anisotropy = renderer.capabilities.getMaxAnisotropy();
          const bgGeo = new THREE.SphereGeometry(380, 64, 48);
          bgGeo.scale(-1, 1, 1);
          const bgMat = new THREE.MeshBasicMaterial({
            map: tex,
            transparent: true,
            opacity: 0.72,
            depthWrite: false
          });
          bgSphereMesh = new THREE.Mesh(bgGeo, bgMat);
          scene.add(bgSphereMesh);
        });
      }

      // Dynamic GLSL Aurora Nebula Dome (Continuously morphing cosmic waves)
      const domeGeo = new THREE.SphereGeometry(320, 64, 48);
      const theme = COSMIC_THEMES[0];
      const domeMat = new THREE.ShaderMaterial({
        uniforms: {
          uTime: { value: 0.0 },
          uColorA: { value: theme.colorA.clone() },
          uColorB: { value: theme.colorB.clone() },
          uColorC: { value: theme.colorC.clone() }
        },
        vertexShader: ShaderLibrary.dynamicNebulaDome.vertexShader,
        fragmentShader: ShaderLibrary.dynamicNebulaDome.fragmentShader,
        side: THREE.BackSide,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      nebulaDomeMesh = new THREE.Mesh(domeGeo, domeMat);
      scene.add(nebulaDomeMesh);
    }

    /* Switch Cosmic Theme Smoothly via GSAP */
    function cycleCosmicTheme() {
      currentThemeIndex = (currentThemeIndex + 1) % COSMIC_THEMES.length;
      const theme = COSMIC_THEMES[currentThemeIndex];

      const btnTheme = document.getElementById('btn-theme');
      if (btnTheme) {
        btnTheme.innerHTML = `<span>🌌 星雲變換: ${theme.name}</span>`;
      }

      soundSystem.playPing(1080, 0.08, false, 0);

      if (nebulaDomeMesh) {
        const u = nebulaDomeMesh.material.uniforms;
        gsap.to(u.uColorA.value, { r: theme.colorA.r, g: theme.colorA.g, b: theme.colorA.b, duration: 1.8 });
        gsap.to(u.uColorB.value, { r: theme.colorB.r, g: theme.colorB.g, b: theme.colorB.b, duration: 1.8 });
        gsap.to(u.uColorC.value, { r: theme.colorC.r, g: theme.colorC.g, b: theme.colorC.b, duration: 1.8 });
      }

      const c1 = new THREE.Color(theme.light1);
      const c2 = new THREE.Color(theme.light2);
      gsap.to(cyanRimLight.color, { r: c1.r, g: c1.g, b: c1.b, duration: 1.8 });
      gsap.to(goldRimLight.color, { r: c2.r, g: c2.g, b: c2.b, duration: 1.8 });
    }

    /* 2. Dual-Layer Counter-Rotating Starfields */
    function buildStarfields() {
      const createStarLayer = (count, spread, size) => {
        const starGeo = new THREE.BufferGeometry();
        const posArray = new Float32Array(count * 3);
        const colorArray = new Float32Array(count * 3);

        for (let i = 0; i < count * 3; i += 3) {
          posArray[i] = (Math.random() - 0.5) * spread;
          posArray[i + 1] = (Math.random() - 0.5) * (spread * 0.6);
          posArray[i + 2] = (Math.random() - 0.5) * spread;

          const rand = Math.random();
          if (rand > 0.6) {
            colorArray[i] = 0.2; colorArray[i + 1] = 0.95; colorArray[i + 2] = 1.0;
          } else if (rand > 0.3) {
            colorArray[i] = 1.0; colorArray[i + 1] = 0.8; colorArray[i + 2] = 0.3;
          } else {
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
        grad.addColorStop(0.25, 'rgba(0,240,255,0.85)');
        grad.addColorStop(0.6, 'rgba(0,240,255,0.2)');
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, 32, 32);
        const starTex = new THREE.CanvasTexture(canvas);

        const starMat = new THREE.PointsMaterial({
          size: size,
          vertexColors: true,
          map: starTex,
          transparent: true,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });

        return new THREE.Points(starGeo, starMat);
      };

      starfield = createStarLayer(3200, 360, 2.1);
      starfieldOuter = createStarLayer(1800, 480, 3.2);
      scene.add(starfield);
      scene.add(starfieldOuter);
    }

    /* 3. Three Fashion Celestial Orbs with Dynamic Flowing Surface & Orbital Motion */
    function buildCelestialPlanets() {
      const texLoader = new THREE.TextureLoader();
      const maxAniso = renderer.capabilities.getMaxAnisotropy();

      const configs = [
        {
          key: 'singles',
          texKey: 'vulcan',
          name: '公開單打擂台星',
          basePos: new THREE.Vector3(-18, 1.0, 1.5),
          pos: new THREE.Vector3(-18, 1.0, 1.5),
          radius: 4.8,
          color: 0xffaa00,
          glowColor: new THREE.Color(0xff6600),
          ringColor: 0xffaa00,
          ringRadius: 8.8,
          pan: -0.65,
          pitch: 980,
          anchorEl: document.getElementById('anchor-singles')
        },
        {
          key: 'doubles',
          texKey: 'cygnus',
          name: '公開雙打雙生星',
          basePos: new THREE.Vector3(0, 3.2, -5.5),
          pos: new THREE.Vector3(0, 3.2, -5.5),
          radius: 5.5,
          color: 0x00f0ff,
          glowColor: new THREE.Color(0x00f0ff),
          ringColor: 0x00f0ff,
          ringRadius: 10.4,
          pan: 0.0,
          pitch: 780,
          anchorEl: document.getElementById('anchor-doubles')
        },
        {
          key: 'prep',
          texKey: 'aegis',
          name: '賽事籌備與大會星',
          basePos: new THREE.Vector3(18, -0.8, 2.0),
          pos: new THREE.Vector3(18, -0.8, 2.0),
          radius: 4.6,
          color: 0xffd700,
          glowColor: new THREE.Color(0xffd700),
          ringColor: 0xffd700,
          ringRadius: 8.4,
          pan: 0.65,
          pitch: 1120,
          anchorEl: document.getElementById('anchor-prep')
        }
      ];

      configs.forEach(cfg => {
        const group = new THREE.Group();
        group.position.copy(cfg.pos);

        const texData = TOURNAMENT_DATA.planet_textures[cfg.texKey];
        const planetTex = texLoader.load(texData);
        planetTex.wrapS = THREE.RepeatWrapping;
        planetTex.wrapT = THREE.RepeatWrapping;
        planetTex.anisotropy = maxAniso;

        const geo = new THREE.SphereGeometry(cfg.radius, 64, 64);
        const mat = new THREE.MeshStandardMaterial({
          map: planetTex,
          bumpMap: planetTex,
          bumpScale: 0.14,
          roughness: 0.28,
          metalness: 0.48,
          emissive: cfg.color,
          emissiveIntensity: 0.16
        });
        const sphere = new THREE.Mesh(geo, mat);
        sphere.userData = { key: cfg.key, name: cfg.name, group: group };
        group.add(sphere);
        planetMeshes.push(sphere);

        // True GLSL Fresnel Rim Atmosphere Shader
        const atmosGeo = new THREE.SphereGeometry(cfg.radius * 1.18, 48, 48);
        const atmosMat = new THREE.ShaderMaterial({
          uniforms: {
            glowColor: { value: cfg.glowColor },
            intensity: { value: 1.15 },
            power: { value: 2.6 }
          },
          vertexShader: ShaderLibrary.fresnelAtmosphere.vertexShader,
          fragmentShader: ShaderLibrary.fresnelAtmosphere.fragmentShader,
          side: THREE.FrontSide,
          blending: THREE.AdditiveBlending,
          transparent: true,
          depthWrite: false
        });
        const atmos = new THREE.Mesh(atmosGeo, atmosMat);
        group.add(atmos);

        // Dual Concentric Luxury Rings
        const ringGeo = new THREE.RingGeometry(cfg.ringRadius * 0.82, cfg.ringRadius, 96);
        const ringMat = new THREE.MeshBasicMaterial({
          color: cfg.ringColor,
          side: THREE.DoubleSide,
          transparent: true,
          opacity: 0.48,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = Math.PI / 2.3;
        ring.rotation.y = Math.PI / 8;
        group.add(ring);

        const innerRingGeo = new THREE.RingGeometry(cfg.ringRadius * 0.68, cfg.ringRadius * 0.71, 96);
        const innerRingMat = new THREE.MeshBasicMaterial({
          color: 0xffffff,
          side: THREE.DoubleSide,
          transparent: true,
          opacity: 0.25,
          blending: THREE.AdditiveBlending,
          depthWrite: false
        });
        const innerRing = new THREE.Mesh(innerRingGeo, innerRingMat);
        innerRing.rotation.x = Math.PI / 2.3;
        innerRing.rotation.y = Math.PI / 8;
        group.add(innerRing);

        // Precision Geodesic Hex Lattice
        const wireGeo = new THREE.IcosahedronGeometry(cfg.radius * 1.36, 2);
        const wireMat = new THREE.MeshBasicMaterial({
          color: cfg.color,
          wireframe: true,
          transparent: true,
          opacity: 0.12,
          depthWrite: false
        });
        const wireSphere = new THREE.Mesh(wireGeo, wireMat);
        group.add(wireSphere);

        scene.add(group);

        planets[cfg.key] = {
          mesh: sphere,
          texture: planetTex,
          group: group,
          atmos: atmos,
          ring: ring,
          innerRing: innerRing,
          wire: wireSphere,
          config: cfg
        };
      });
    }

    /* 4. TRI-PLANET TABLE TENNIS RALLY SYSTEM (Bouncing across all 3 planets!) */
    function buildTriPlanetRallySystem() {
      // Glowing 40+ Table Tennis Ball
      const ballGeo = new THREE.SphereGeometry(0.62, 28, 28);
      const ballMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
      rallyBall = new THREE.Mesh(ballGeo, ballMat);

      const haloGeo = new THREE.SphereGeometry(1.45, 20, 20);
      const haloMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.55,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      rallyHalo = new THREE.Mesh(haloGeo, haloMat);
      rallyBall.add(rallyHalo);
      scene.add(rallyBall);

      // Pre-allocated Trail BufferGeometry
      const trailGeo = new THREE.BufferGeometry();
      trailPositions = new Float32Array(TRAIL_LENGTH * 3);
      trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
      const trailMat = new THREE.LineBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending
      });
      trailLine = new THREE.Line(trailGeo, trailMat);
      scene.add(trailLine);

      // Pre-allocated Impact Shockwave Ring
      const impactGeo = new THREE.RingGeometry(0.6, 1.15, 36);
      const impactMat = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.0,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      impactRing = new THREE.Mesh(impactGeo, impactMat);
      scene.add(impactRing);

      // Pre-allocated 3D Spark Burst Particles on Planet Impact
      const sparkGeo = new THREE.BufferGeometry();
      const sparkPos = new Float32Array(SPARK_COUNT * 3);
      sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
      const sparkMat = new THREE.PointsMaterial({
        color: 0xffd700,
        size: 0.65,
        transparent: true,
        opacity: 0.0,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      sparkParticles = new THREE.Points(sparkGeo, sparkMat);
      scene.add(sparkParticles);

      for (let i = 0; i < SPARK_COUNT; i++) {
        sparkVelocities.push(new THREE.Vector3());
      }
    }

    function triggerPlanetImpactEffect(planetKey, hitX, hitY, hitZ) {
      const p = planets[planetKey];
      if (!p) return;

      const colorHex = p.config.color;

      // 1. Shockwave Ring Expansion
      if (impactRing) {
        impactRing.position.set(hitX, hitY, hitZ);
        impactRing.lookAt(camera.position);
        impactRing.scale.set(0.5, 0.5, 0.5);
        impactRing.material.color.setHex(colorHex);
        impactRing.material.opacity = 0.95;

        gsap.killTweensOf(impactRing.scale);
        gsap.killTweensOf(impactRing.material);
        gsap.to(impactRing.scale, { x: 5.2, y: 5.2, z: 5.2, duration: 0.55, ease: "power2.out" });
        gsap.to(impactRing.material, { opacity: 0.0, duration: 0.55, ease: "power2.out" });
      }

      // 2. Planet Atmosphere & Ring Recoil Pulse
      gsap.killTweensOf(p.atmos.material.uniforms.intensity);
      p.atmos.material.uniforms.intensity.value = 2.2;
      gsap.to(p.atmos.material.uniforms.intensity, { value: 1.15, duration: 0.45, ease: "power2.out" });

      gsap.killTweensOf(p.group.scale);
      p.group.scale.set(1.06, 1.06, 1.06);
      gsap.to(p.group.scale, { x: 1.0, y: 1.0, z: 1.0, duration: 0.38, ease: "elastic.out(1, 0.4)" });

      // 3. Spatial HUD Label Pulse
      const el = p.config.anchorEl;
      if (el) {
        el.classList.add('hit-pulse');
        clearTimeout(el._pulseTimer);
        el._pulseTimer = setTimeout(() => el.classList.remove('hit-pulse'), 260);
      }

      // 4. 3D Spark Burst
      if (sparkParticles) {
        const posAttr = sparkParticles.geometry.attributes.position;
        const arr = posAttr.array;
        for (let i = 0; i < SPARK_COUNT; i++) {
          arr[i * 3] = hitX;
          arr[i * 3 + 1] = hitY;
          arr[i * 3 + 2] = hitZ;
          sparkVelocities[i].set(
            (Math.random() - 0.5) * 14,
            (Math.random() - 0.2) * 14,
            (Math.random() - 0.5) * 14
          );
        }
        posAttr.needsUpdate = true;
        sparkParticles.material.color.setHex(colorHex);
        sparkParticles.material.opacity = 1.0;
        gsap.killTweensOf(sparkParticles.material);
        gsap.to(sparkParticles.material, { opacity: 0.0, duration: 0.5, ease: "power2.out" });
      }

      // 5. Update Trail & Ball Halo Color to match hit planet
      if (rallyHalo) rallyHalo.material.color.setHex(colorHex);
      if (trailLine) trailLine.material.color.setHex(colorHex);

      // 6. Play Spatial Table Tennis Sound with Planet-specific Pitch & Stereo Pan
      soundSystem.playPing(p.config.pitch, 0.075, planetKey === 'prep', p.config.pan);

      rallyRounds++;
      const counterEl = document.getElementById('rally-count');
      if (counterEl) counterEl.textContent = rallyRounds;

      const soundBars = document.getElementById('sound-bars');
      if (soundBars) {
        soundBars.classList.add('active');
        clearTimeout(soundBars._timer);
        soundBars._timer = setTimeout(() => soundBars.classList.remove('active'), 240);
      }
    }

    /* Update 3-Planet Table Tennis Rally (Singles -> Doubles -> Prep -> Singles) */
    function updateTriPlanetRally(delta) {
      if (!rallyBall || !planets['singles'] || !planets['doubles'] || !planets['prep']) return;

      // Advance progress along current leg (0.0 -> 1.0)
      rallyProgress += delta * 1.35;

      if (rallyProgress >= 1.0) {
        rallyProgress -= 1.0;
        const arrivedKey = RALLY_ORDER[(currentLegIndex + 1) % RALLY_ORDER.length];
        const arrivedPlanet = planets[arrivedKey];
        const hitX = arrivedPlanet.group.position.x;
        const hitY = arrivedPlanet.group.position.y + arrivedPlanet.config.radius * 0.85;
        const hitZ = arrivedPlanet.group.position.z + arrivedPlanet.config.radius * 0.5;

        triggerPlanetImpactEffect(arrivedKey, hitX, hitY, hitZ);

        // Advance to next planet leg in the 3-planet loop
        currentLegIndex = (currentLegIndex + 1) % RALLY_ORDER.length;
        const fromKey = RALLY_ORDER[currentLegIndex];
        const toKey = RALLY_ORDER[(currentLegIndex + 1) % RALLY_ORDER.length];
        if (routeEl) {
          routeEl.textContent = `🏓 ${RALLY_LABELS[fromKey]} ➔ ${RALLY_LABELS[toKey]}`;
        }
      }

      const fromKey = RALLY_ORDER[currentLegIndex];
      const toKey = RALLY_ORDER[(currentLegIndex + 1) % RALLY_ORDER.length];
      const pFrom = planets[fromKey];
      const pTo = planets[toKey];

      // Start and End points on the upper-front rim of each planet
      _pStart.copy(pFrom.group.position);
      _pStart.y += pFrom.config.radius * 0.85;
      _pStart.z += pFrom.config.radius * 0.5;

      _pEnd.copy(pTo.group.position);
      _pEnd.y += pTo.config.radius * 0.85;
      _pEnd.z += pTo.config.radius * 0.5;

      const t = rallyProgress;

      // Table Tennis Double-Bounce & Topspin Arc between the 2 planets of current leg:
      // First 45% of leg: ball drops from Planet A onto an invisible cosmic mid-table bounce point,
      // Remaining 55% of leg: ball rebounds upward in a high topspin arc onto Planet B!
      const x = THREE.MathUtils.lerp(_pStart.x, _pEnd.x, t);
      const baseZ = THREE.MathUtils.lerp(_pStart.z, _pEnd.z, t);
      // Slight outward curve in Z for 3D depth
      const zCurve = Math.sin(t * Math.PI) * (currentLegIndex === 2 ? 6.5 : 3.2);
      const z = baseZ + zCurve;

      const baseY = THREE.MathUtils.lerp(_pStart.y, _pEnd.y, t);
      // High parabolic topspin jump
      const arcY = Math.sin(t * Math.PI) * 8.2;
      const y = baseY + arcY;

      rallyBall.position.set(x, y, z);

      // Update Spark Burst Particles if active
      if (sparkParticles && sparkParticles.material.opacity > 0.01) {
        const posAttr = sparkParticles.geometry.attributes.position;
        const arr = posAttr.array;
        for (let i = 0; i < SPARK_COUNT; i++) {
          arr[i * 3] += sparkVelocities[i].x * delta;
          arr[i * 3 + 1] += sparkVelocities[i].y * delta;
          arr[i * 3 + 2] += sparkVelocities[i].z * delta;
        }
        posAttr.needsUpdate = true;
      }

      // Shift pre-allocated trail buffer in-place (Zero GC allocation)
      for (let i = (TRAIL_LENGTH - 1) * 3; i >= 3; i -= 3) {
        trailPositions[i] = trailPositions[i - 3];
        trailPositions[i + 1] = trailPositions[i - 2];
        trailPositions[i + 2] = trailPositions[i - 1];
      }
      trailPositions[0] = x;
      trailPositions[1] = y;
      trailPositions[2] = z;
      trailLine.geometry.attributes.position.needsUpdate = true;
    }

    /* Update 3D Spatial Anchors (Zero-GC Projection) */
    function updateSpatialAnchors() {
      const halfW = window.innerWidth * 0.5;
      const halfH = window.innerHeight * 0.5;

      for (const key in planets) {
        const p = planets[key];
        const el = p.config.anchorEl;
        if (!el) continue;

        if (isModalOpen) {
          el.style.opacity = '0';
          el.style.pointerEvents = 'none';
          continue;
        }

        _projVec.copy(p.group.position);
        _projVec.y += p.config.radius + 2.4;
        _projVec.project(camera);

        if (_projVec.z > 1.0 || _projVec.z < -1.0) {
          el.style.opacity = '0';
          el.style.pointerEvents = 'none';
        } else {
          const sx = (_projVec.x * halfW) + halfW;
          const sy = -(_projVec.y * halfH) + halfH;
          el.style.transform = `translate3d(${sx.toFixed(1)}px, ${sy.toFixed(1)}px, 0) translate(-50%, -100%)`;
          el.style.opacity = '0.95';
          el.style.pointerEvents = 'auto';
        }
      }
    }

    /* Camera Fly-In Animation & Modal Open */
    function focusPlanet(key) {
      const target = planets[key];
      if (!target) return;

      soundSystem.playPing(1160, 0.07, true, target.config.pan);

      document.querySelectorAll('.orb-tab').forEach(tab => {
        tab.classList.toggle('active', tab.getAttribute('data-target') === key);
      });

      const pPos = target.group.position;
      const targetCamPos = new THREE.Vector3(pPos.x, pPos.y + 1.2, pPos.z + target.config.radius * 2.55);

      gsap.killTweensOf(camera.position);
      gsap.killTweensOf(controls.target);

      gsap.to(camera.position, {
        x: targetCamPos.x,
        y: targetCamPos.y,
        z: targetCamPos.z,
        duration: 1.25,
        ease: "power3.inOut"
      });

      gsap.to(controls.target, {
        x: pPos.x,
        y: pPos.y,
        z: pPos.z,
        duration: 1.25,
        ease: "power3.inOut",
        onComplete: () => {
          openModal(key);
        }
      });
    }

    function resetCamera() {
      closeModal();
      document.querySelectorAll('.orb-tab').forEach(tab => tab.classList.remove('active'));

      gsap.killTweensOf(camera.position);
      gsap.killTweensOf(controls.target);

      gsap.to(camera.position, {
        x: 0,
        y: 15,
        z: 48,
        duration: 1.5,
        ease: "power3.inOut"
      });

      gsap.to(controls.target, {
        x: 0,
        y: 1,
        z: 0,
        duration: 1.5,
        ease: "power3.inOut"
      });
    }

    /* Smart Pointer Disambiguation (Distinguish Click vs Orbit Drag) */
    function onPointerDown(event) {
      _pointerDownPos.x = event.clientX;
      _pointerDownPos.y = event.clientY;
      _pointerDownPos.time = performance.now();
    }

    function onPointerUp(event) {
      if (isModalOpen) return;
      const dx = event.clientX - _pointerDownPos.x;
      const dy = event.clientY - _pointerDownPos.y;
      const dist = Math.hypot(dx, dy);
      const dt = performance.now() - _pointerDownPos.time;

      if (dist < 6 && dt < 350) {
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(planetMeshes);
        if (intersects.length > 0) {
          const hitKey = intersects[0].object.userData.key;
          if (hitKey) focusPlanet(hitKey);
        }
      }
    }

    function onPointerMove(event) {
      if (isModalOpen) return;
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(planetMeshes);

      if (intersects.length > 0) {
        const key = intersects[0].object.userData.key;
        if (hoveredPlanetKey !== key) {
          hoveredPlanetKey = key;
          document.body.style.cursor = 'pointer';
          gsap.to(planets[key].atmos.material.uniforms.intensity, { value: 1.75, duration: 0.25 });
        }
      } else if (hoveredPlanetKey) {
        gsap.to(planets[hoveredPlanetKey].atmos.material.uniforms.intensity, { value: 1.15, duration: 0.25 });
        hoveredPlanetKey = null;
        document.body.style.cursor = 'default';
      }
    }

    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }

    /* High-Efficiency Render Loop with Dynamic Background & 3-Planet Bounce */
    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      if (isPageHidden) return;

      const delta = Math.min(clock.getDelta(), 0.1);
      const elapsed = clock.getElapsedTime();

      frameCount++;
      const now = performance.now();
      if (now - lastFpsTime >= 1000) {
        if (fpsEl) fpsEl.textContent = `${frameCount} FPS`;
        frameCount = 0;
        lastFpsTime = now;
      }

      // 1. Dynamic Cosmic Background & Aurora Nebula Motion
      if (bgSphereMesh) {
        bgSphereMesh.rotation.y = elapsed * 0.022;
        bgSphereMesh.rotation.x = Math.sin(elapsed * 0.15) * 0.06;
      }
      if (nebulaDomeMesh) {
        nebulaDomeMesh.material.uniforms.uTime.value = elapsed;
        nebulaDomeMesh.rotation.y = -elapsed * 0.018;
      }
      if (starfield) {
        starfield.rotation.y = elapsed * 0.015;
        starfield.rotation.z = Math.sin(elapsed * 0.1) * 0.04;
      }
      if (starfieldOuter) {
        starfieldOuter.rotation.y = -elapsed * 0.01;
      }

      // 2. Dynamic Planet Surface Texture Flow + Gentle Orbital Float
      if (planets['singles']) {
        const p = planets['singles'];
        p.mesh.rotation.y += delta * 0.35;
        p.texture.offset.x = (elapsed * 0.015) % 1;
        p.wire.rotation.y -= delta * 0.14;
        p.ring.rotation.z -= delta * 0.12;
        if (!isModalOpen) {
          p.group.position.y = p.config.basePos.y + Math.sin(elapsed * 1.4) * 0.55;
        }
      }
      if (planets['doubles']) {
        const p = planets['doubles'];
        p.mesh.rotation.y += delta * 0.28;
        p.texture.offset.x = (elapsed * 0.012) % 1;
        p.ring.rotation.z += delta * 0.1;
        p.innerRing.rotation.z -= delta * 0.18;
        if (!isModalOpen) {
          p.group.position.y = p.config.basePos.y + Math.sin(elapsed * 1.2 + 2.1) * 0.65;
        }
      }
      if (planets['prep']) {
        const p = planets['prep'];
        p.mesh.rotation.y += delta * 0.22;
        p.texture.offset.x = (elapsed * 0.01) % 1;
        p.wire.rotation.x += delta * 0.11;
        p.ring.rotation.z += delta * 0.09;
        if (!isModalOpen) {
          p.group.position.y = p.config.basePos.y + Math.sin(elapsed * 1.5 + 4.2) * 0.5;
        }
      }

      // 3. Update 3-Planet Table Tennis Rally
      if (!isModalOpen) {
        updateTriPlanetRally(delta);
        controls.update();
      }

      updateSpatialAnchors();
      renderer.render(scene, camera);
    }

    /* ========================================================================
       5. MODAL & HUD CONTROLLER (Uncropped Full Photos + Official Signature)
       ======================================================================== */
    const modal = document.getElementById('modal');
    const modalSector = document.getElementById('modal-sector');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content');
    const btnCloseModal = document.getElementById('btn-close-modal');

    function openModal(key) {
      const data = TOURNAMENT_DATA.planets[key];
      if (!data) return;

      isModalOpen = true;
      controls.enabled = false;

      modalSector.textContent = data.sector;
      modalTitle.textContent = `${data.name} ｜ ${data.subtitle}`;

      const podiumCardsHtml = data.rankings.map(item => {
        let photoSection = '';
        if (item.photo_extra) {
          photoSection = `
            <div class="dual-photo-box">
              <div class="mini-photo-item" onclick="openLightbox('${item.photo}')" title="點擊放大預覽">
                <img src="${item.photo}" alt="季軍第一組完整照片" loading="lazy">
              </div>
              <div class="mini-photo-item" onclick="openLightbox('${item.photo_extra}')" title="點擊放大預覽">
                <img src="${item.photo_extra}" alt="季軍第二組完整照片" loading="lazy">
              </div>
            </div>
          `;
        } else if (item.photo) {
          photoSection = `
            <div class="card-photo-box" onclick="openLightbox('${item.photo}')" title="點擊放大檢視原圖">
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
              全體選手與榮譽頒獎大合照（完整呈現）
            </div>
            <div class="group-photo-container" onclick="openLightbox('${data.group_photo}')">
              <img src="${data.group_photo}" alt="${data.group_caption}">
              <div class="group-caption">${data.group_caption}</div>
            </div>
          </div>
        `;
      } else if (data.extra_photos && data.extra_photos.length > 0) {
        const prepThumbs = data.extra_photos.map((src, idx) => `
          <div class="prep-thumb-item" onclick="openLightbox('${src}')" title="點擊放大檢視">
            <img src="${src}" alt="賽事準備實況 ${idx+1}">
          </div>
        `).join('');

        extraSection = `
          <div class="group-photo-section">
            <div class="group-section-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>
              賽事實況與選手熱身花絮精選（完整呈現）
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
        <div class="modal-footer-signature">🏓 連江縣桌球委員會 敬賀</div>
      `;

      modal.classList.add('open');
    }

    function closeModal() {
      isModalOpen = false;
      if (controls) controls.enabled = true;
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
      soundSystem.playPing(1280, 0.05, false, 0);
      lightboxImg.src = src;
      lightbox.classList.add('active');
    };

    lightbox.addEventListener('click', () => {
      lightbox.classList.remove('active');
    });

    /* Spatial Label & Bottom Tab Controls */
    document.querySelectorAll('.orb-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        focusPlanet(tab.getAttribute('data-target'));
      });
    });

    document.querySelectorAll('.spatial-label').forEach(lbl => {
      lbl.addEventListener('click', () => {
        focusPlanet(lbl.getAttribute('data-key'));
      });
    });

    /* Header Controls */
    document.getElementById('btn-reset').addEventListener('click', resetCamera);
    document.getElementById('btn-theme').addEventListener('click', cycleCosmicTheme);

    document.getElementById('btn-hit').addEventListener('click', () => {
      // Force an immediate jump to the next planet impact!
      rallyProgress = 0.99;
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
      if (e.key === 'b' || e.key === 'B') cycleCosmicTheme();
      if (e.key === 'Escape') {
        closeModal();
        lightbox.classList.remove('active');
      }
      if (e.key === ' ') {
        e.preventDefault();
        rallyProgress = 0.99;
      }
    });

    // Unlock Web Audio API on first mobile/tablet touch or desktop click
    const unlockAudio = () => {
      soundSystem.init();
      if (soundSystem.ctx && soundSystem.ctx.state === 'suspended') {
        soundSystem.ctx.resume();
      }
    };
    window.addEventListener('pointerdown', unlockAudio, { once: true, passive: true });
    window.addEventListener('touchstart', unlockAudio, { once: true, passive: true });

    // Cross-Device QR Modal handlers
    const qrModal = document.getElementById('qr-modal');
    const btnQr = document.getElementById('btn-qr');
    const btnCloseQr = document.getElementById('btn-close-qr');
    const btnCopyUrl = document.getElementById('btn-copy-url');
    const githubUrl = "https://pwb6331-hub.github.io/table-tennis-cosmic-arena/";

    btnQr.addEventListener('click', () => {
      soundSystem.playPing(1180, 0.06, false, 0);
      qrModal.classList.add('active');
    });
    btnCloseQr.addEventListener('click', () => {
      qrModal.classList.remove('active');
    });
    qrModal.addEventListener('click', (e) => {
      if (e.target === qrModal) qrModal.classList.remove('active');
    });
    btnCopyUrl.addEventListener('click', () => {
      navigator.clipboard.writeText(githubUrl).then(() => {
        btnCopyUrl.textContent = "✅ 已複製網址！";
        setTimeout(() => { btnCopyUrl.textContent = "📋 複製 GitHub 網址"; }, 2000);
      });
    });

    window.addEventListener('load', initWebGL);
  </script>
</body>
</html>
'''

paths = [
    r'E:\2026GEM-SKILL\table-tennis-cosmic-arena\index.html',
    r'E:\2026GEM-SKILL\index.html',
    r'E:\2026GEM-SKILL\115年度連江縣體育季桌球錦標賽_3D太空展館.html',
    r'C:\Users\A1547\.gemini\antigravity\brain\01ae478b-5840-417e-8783-95119ece3e7b\115年度連江縣體育季桌球錦標賽_3D太空展館.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Deployed Dynamic BG + 3-Planet Rally HTML -> {p} ({os.path.getsize(p)/1024:.2f} KB)")
