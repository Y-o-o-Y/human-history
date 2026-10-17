# -*- coding: utf-8 -*-
"""
Generate index2.html with an authoritative newspaper / editorial archive style:
- Clean white / newsprint background (#ffffff / #f8f9fa)
- Monotone text colors: strictly 3 colors max (#111827 Ink Black, #4b5563 Editorial Gray, #991b1b Deep Crimson)
- Classical editorial typography (Serif headlines like WSJ / NYT, clean sans-serif for UI)
- Dignified journalistic layout, eliminating the AI SaaS / neon cyberpunk dark dashboard feel
- Preserves all original copy, titles, data, and interactive features (Database, Bar Chart Race, GIS Map)
"""
import json
from geo_coords import coords

# Load events
with open('events_master.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

events_json = json.dumps(events, ensure_ascii=False)
coords_json = json.dumps(coords, ensure_ascii=False)
total_count = len(events)

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>人道事件編年史 (1800–2026) 全球定量歷史學綜合儀表板</title>
  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <!-- Google Fonts & 源泉圓體 (GenSenRounded) Webfont -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <!-- 源泉圓體 CDN Webfont -->
  <link rel="stylesheet" href="https://fontsapi.zeoseven.com/303/main/result.css">
  <!-- Leaflet CSS & JS for Interactive Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  <style>
    /* Strictly 3 text colors throughout the entire application:
       1. Primary: #111827 (Deep Ink Black)
       2. Secondary / Muted: #4b5563 (Editorial Slate Gray)
       3. Accent / Alert: #991b1b (Editorial Deep Crimson)
    */
    :root {{
      --font-rounded: "源泉圓體", "GenSenRounded2 TC", "GenSenRounded", "GenSenRounded TW", "GenSenRounded TC", "GenSenRounded2", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", "Microsoft JhengHei", sans-serif;
      --font-mono: "JetBrains Mono", "源泉圓體", "GenSenRounded2 TC", Consolas, Monaco, monospace;
      
      --c-black: #111827;
      --c-gray: #4b5563;
      --c-crimson: #991b1b;
      
      --bg-page: #f8f9fa;
      --bg-card: #ffffff;
      --border-light: #e5e7eb;
      --border-dark: #111827;
    }}

    body {{
      background-color: var(--bg-page);
      color: var(--c-black);
      font-family: var(--font-rounded);
      -webkit-font-smoothing: antialiased;
    }}

    .font-editorial-serif {{
      font-family: var(--font-rounded) !important;
    }}
    .font-editorial-sans {{
      font-family: var(--font-rounded) !important;
    }}
    .font-editorial-mono {{
      font-family: var(--font-mono) !important;
    }}

    /* Newspaper rules and lines */
    .border-double-rule {{
      border-bottom: 3px double #d1d5db;
    }}
    .border-thick-rule {{
      border-bottom: 2px solid #111827;
    }}

    /* Leaflet Newspaper Theme Overrides */
    .leaflet-container {{
      background: #f1f3f5 !important;
      font-family: var(--font-rounded) !important;
    }}
    .leaflet-popup-content-wrapper, .leaflet-popup-tip {{
      background: #ffffff !important;
      color: #111827 !important;
      border: 1px solid #d1d5db;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      border-radius: 4px;
    }}
    .leaflet-popup-content {{
      margin: 12px 14px;
      line-height: 1.5;
    }}
    .dark-tooltip {{
      background: #ffffff !important;
      color: #111827 !important;
      border: 1px solid #d1d5db !important;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06) !important;
      font-family: var(--font-rounded) !important;
      border-radius: 4px !important;
    }}

    /* Subtle newspaper scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #f1f3f5;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col bg-[#f8f9fa] text-[#111827]">

  <!-- Newspaper Header / Masthead -->
  <header class="bg-white border-b border-gray-300 sticky top-0 z-50 shadow-[0_1px_3px_rgba(0,0,0,0.04)]">
    <!-- Top thin rule & publication bar -->
    <div class="max-w-7xl mx-auto px-4 lg:px-8 py-1 border-b border-gray-100 flex items-center justify-between text-[11px] text-[#4b5563] font-editorial-mono">
      <span>HISTORICAL DEMOGRAPHIC REPORT & QUANTITATIVE DATASET</span>
      <span class="hidden sm:inline">1800–2026 ARCHIVAL EDITION</span>
      <span>基準年：2026</span>
    </div>

    <div class="max-w-7xl mx-auto px-4 lg:px-8 py-3.5 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <!-- Title & Status -->
      <div class="flex items-start gap-3.5">
        <div class="w-10 h-10 rounded border border-gray-300 bg-gray-50 flex items-center justify-center text-lg text-[#111827] shrink-0 font-editorial-serif font-bold">
          ⚖
        </div>
        <div>
          <div class="flex flex-wrap items-center gap-2.5">
            <h1 class="text-xl md:text-2xl font-bold font-editorial-serif tracking-tight text-[#111827]">
              人道事件編年史 (1800–2026)
            </h1>
            <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-gray-100 text-[#991b1b] border border-gray-300">
              90%+ 覆蓋率 · {total_count} 起浩劫
            </span>
          </div>
          <p class="text-xs text-[#4b5563] mt-0.5">
            6 大洲與 5 大分類體系 · 零幻覺與三級文獻考證標準 · 2026年人口等效規模基準 (81.5億)
          </p>
        </div>
      </div>

      <!-- View Switcher Tabs (Editorial Monotone Style) -->
      <div class="flex items-center gap-1.5 self-start md:self-auto bg-gray-100 p-1 rounded border border-gray-200">
        <button id="tab-database" class="nav-tab px-3.5 py-1.5 rounded text-xs font-semibold transition flex items-center gap-1.5 bg-white text-[#111827] shadow-sm border border-gray-300" data-view="view-database">
          <span>📚</span> 資料庫清單
        </button>
        <button id="tab-race" class="nav-tab px-3.5 py-1.5 rounded text-xs font-semibold transition flex items-center gap-1.5 text-[#4b5563] hover:text-[#111827]" data-view="view-race">
          <span>📊</span> Bar Chart Race 競賽
        </button>
        <button id="tab-map" class="nav-tab px-3.5 py-1.5 rounded text-xs font-semibold transition flex items-center gap-1.5 text-[#4b5563] hover:text-[#111827]" data-view="view-map">
          <span>🗺️</span> 各世紀地緣演變地圖
        </button>
      </div>

      <!-- Data Export Links -->
      <div class="hidden lg:flex items-center gap-2">
        <a href="events_master.csv" download class="px-3 py-1.5 rounded bg-white hover:bg-gray-50 text-xs font-medium text-[#4b5563] hover:text-[#111827] border border-gray-300 transition flex items-center gap-1">
          <span>⬇</span> CSV
        </a>
        <a href="events_master.json" target="_blank" class="px-3 py-1.5 rounded bg-white hover:bg-gray-50 text-xs font-medium text-[#4b5563] hover:text-[#111827] border border-gray-300 transition flex items-center gap-1">
          <span>{{ }}</span> JSON
        </a>
      </div>
    </div>
  </header>

  <!-- Main Content Container -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-8 space-y-6">

    <!-- ===================================================================== -->
    <!-- VIEW 1: DATABASE LIST & EXPLORER (原資料庫檢視 - 新聞報紙風格) -->
    <!-- ===================================================================== -->
    <section id="view-database" class="view-panel space-y-6">
      
      <!-- Top KPI Dynamic Stats: Editorial Scorecard -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-white border border-gray-300 rounded p-4 shadow-sm">
          <span class="text-xs font-medium text-[#4b5563]">收錄事件數 (當前篩選)</span>
          <div class="text-2xl md:text-3xl font-bold font-editorial-serif text-[#111827] mt-1" id="stat-count">{total_count}</div>
          <span class="text-xs text-[#4b5563]" id="stat-count-sub">全量 {total_count} 起事件</span>
        </div>
        
        <div class="bg-white border border-gray-300 rounded p-4 shadow-sm">
          <span class="text-xs font-medium text-[#4b5563]">基準罹難總數 (Mid 加總)</span>
          <div class="text-2xl md:text-3xl font-bold font-editorial-serif text-[#991b1b] mt-1" id="stat-deaths">0</div>
          <span class="text-xs text-[#4b5563]">歷史學中值估算</span>
        </div>
        
        <div class="bg-white border border-gray-300 rounded p-4 shadow-sm">
          <span class="text-xs font-medium text-[#4b5563]">2026 當代等效罹難規模</span>
          <div class="text-2xl md:text-3xl font-bold font-editorial-serif text-[#111827] mt-1" id="stat-modern">0</div>
          <span class="text-xs text-[#4b5563]">依現代全球人口等比放縮</span>
        </div>
        
        <div class="bg-white border border-gray-300 rounded p-4 shadow-sm">
          <span class="text-xs font-medium text-[#4b5563]">最高單一區域衝擊率</span>
          <div class="text-2xl md:text-3xl font-bold font-editorial-serif text-[#991b1b] mt-1" id="stat-max-impact">0%</div>
          <span class="text-xs text-[#4b5563] truncate block" id="stat-max-impact-name">-</span>
        </div>
      </div>

      <!-- Filter & Search Controls: News Archive Filter Bar -->
      <div class="bg-white border border-gray-300 rounded p-4 space-y-3.5 shadow-sm">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
          <div class="relative flex-1 max-w-lg">
            <input type="text" id="search-input" placeholder="搜尋事件名稱、國家、關鍵字（如：文革、大屠殺、饑荒）..." 
              class="w-full bg-white border border-gray-300 rounded px-3.5 py-2 text-xs text-[#111827] placeholder-[#4b5563] focus:outline-none focus:border-[#111827] focus:ring-1 focus:ring-[#111827] transition">
          </div>
          <div class="text-xs text-[#4b5563] font-editorial-mono" id="filter-status-text">
            顯示 {total_count} 筆歷史人道慘劇檔案
          </div>
        </div>

        <!-- Filter Row 1: Continents -->
        <div class="flex flex-wrap items-center gap-1.5 pt-2.5 border-t border-gray-200">
          <span class="text-xs font-bold text-[#111827] mr-1">大洲：</span>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-[#111827] text-white border border-[#111827]" data-type="continent" data-val="all">全部大洲</button>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="continent" data-val="Asia">亞洲 (Asia)</button>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="continent" data-val="Europe">歐洲 (Europe)</button>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="continent" data-val="Africa">非洲 (Africa)</button>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="continent" data-val="Americas">美洲 (Americas)</button>
          <button class="filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="continent" data-val="Oceania">大洋洲 (Oceania)</button>
        </div>

        <!-- Filter Row 2: Categories -->
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="text-xs font-bold text-[#111827] mr-1">分類：</span>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-[#991b1b] text-white border border-[#991b1b]" data-type="category" data-val="all">全部分類</button>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="category" data-val="Direct Physical Massacre / Genocide">種族滅絕 / 大屠殺</button>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="category" data-val="Man-made & Policy Famine">人為政策飢荒</button>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="category" data-val="Democide, Purges & Forced Labor">國家謀殺 / 大清洗 / 勞改</button>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="category" data-val="War-Time Civilian Atrocities">戰時平民暴行</button>
          <button class="filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300" data-type="category" data-val="Coercive Population Control">強制人口控制</button>
        </div>
      </div>

      <!-- Events List Container -->
      <div class="space-y-4" id="events-container"></div>
    </section>


    <!-- ===================================================================== -->
    <!-- VIEW 2: BAR CHART RACE (歷史累積傷亡動態競賽 - 經典新聞圖表風) -->
    <!-- ===================================================================== -->
    <section id="view-race" class="view-panel hidden space-y-6">
      <div class="bg-white border border-gray-300 rounded p-6 shadow-sm">
        
        <!-- Control Header -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-gray-200 pb-5">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-xs font-semibold bg-gray-100 text-[#991b1b] border border-gray-300">動態時間軸</span>
              <h2 class="text-xl font-bold font-editorial-serif text-[#111827]">各國累積人道災難罹難人數 · Bar Chart Race (1800–2026)</h2>
            </div>
            <p class="text-xs text-[#4b5563] mt-1">呈現自工業革命至今，各國境內人為人道浩劫（大饑荒、種族滅絕、大清洗、戰時暴行）中值罹難人數隨歷史年代之累積動態演進</p>
          </div>

          <!-- Player Controls: Dignified Minimalist News Style -->
          <div class="flex items-center gap-3">
            <button id="race-play-btn" class="px-4 py-2 rounded bg-[#111827] hover:bg-black text-xs font-bold text-white transition flex items-center gap-2 shadow-sm border border-[#111827]">
              <span id="race-play-icon">▶</span> <span id="race-play-text">播放競賽</span>
            </button>
            <button id="race-reset-btn" class="px-3 py-2 rounded bg-white hover:bg-gray-100 text-xs font-medium text-[#4b5563] hover:text-[#111827] border border-gray-300 transition">
              重設 (1800)
            </button>
            <div class="text-right pl-3 border-l border-gray-200">
              <div class="text-3xl font-black font-editorial-mono text-[#991b1b] tracking-tight" id="race-year-display">1800</div>
              <div class="text-[10px] text-[#4b5563]">當前推進年份</div>
            </div>
          </div>
        </div>

        <!-- Timeline Slider -->
        <div class="py-4 space-y-1.5">
          <input type="range" id="race-timeline-slider" min="1800" max="2026" value="1800" step="1" 
            class="w-full h-2 bg-gray-200 rounded appearance-none cursor-pointer accent-[#111827]">
          <div class="flex justify-between text-[11px] text-[#4b5563] font-editorial-mono">
            <span>1800</span>
            <span>1850 (太平天國/愛爾蘭)</span>
            <span>1900 (世紀之交)</span>
            <span>1945 (二戰浩劫)</span>
            <span>1975 (冷戰狂熱)</span>
            <span>2000 (世紀末)</span>
            <span>2026</span>
          </div>
        </div>

        <!-- Metric Toggle: Raw Deaths vs Modern Equivalent -->
        <div class="flex items-center justify-between text-xs py-2 px-3 bg-gray-50 rounded border border-gray-200">
          <div class="flex items-center gap-2">
            <span class="text-[#111827] font-bold">統計指標：</span>
            <label class="inline-flex items-center gap-1 cursor-pointer">
              <input type="radio" name="race-metric" value="raw" checked class="accent-[#111827]">
              <span class="text-[#111827]">歷史原始罹難 (Mid)</span>
            </label>
            <label class="inline-flex items-center gap-1 cursor-pointer ml-3">
              <input type="radio" name="race-metric" value="modern" class="accent-[#111827]">
              <span class="text-[#111827]">2026 當代人口等效規模</span>
            </label>
          </div>
          <div class="text-[#4b5563] text-[11px]" id="race-current-event-hint">
            歷史平穩期
          </div>
        </div>

        <!-- Bar Chart Race Bars Container -->
        <div class="mt-6 space-y-2.5 min-h-[460px]" id="race-bars-container">
          <!-- Dynamically Injected -->
        </div>
      </div>
    </section>


    <!-- ===================================================================== -->
    <!-- VIEW 3: CENTURY GEOPOLITICS MAP (各世紀地緣演變地圖 - 報刊地理圖表風) -->
    <!-- ===================================================================== -->
    <section id="view-map" class="view-panel hidden space-y-6">
      <div class="bg-white border border-gray-300 rounded p-6 shadow-sm space-y-5">
        
        <!-- Map Header & Century Selector -->
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-gray-200 pb-5">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-xs font-semibold bg-gray-100 text-[#111827] border border-gray-300">GIS 空間分析</span>
              <h2 class="text-xl font-bold font-editorial-serif text-[#111827]">各世紀浩劫地緣演變地圖 (Geopolitical Evolution Map)</h2>
            </div>
            <p class="text-xs text-[#4b5563] mt-1">依歷史世紀分期切換，視覺化呈現人道慘劇熱點從19世紀殖民帝國征服、20世紀前半葉大戰極權，轉移至冷戰意識形態及當代區域衝突之地緣變遷</p>
          </div>

          <!-- Century Switcher Buttons -->
          <div class="flex flex-wrap items-center gap-1 bg-gray-100 p-1 rounded border border-gray-200">
            <button class="map-era-btn px-3 py-1.5 rounded text-xs font-bold transition bg-[#111827] text-white shadow-sm border border-[#111827]" data-era="all">
              全時期 (1800–2026)
            </button>
            <button class="map-era-btn px-3 py-1.5 rounded text-xs font-medium transition bg-transparent text-[#4b5563] hover:text-[#111827]" data-era="19th">
              19世紀 (1800–1899)
            </button>
            <button class="map-era-btn px-3 py-1.5 rounded text-xs font-medium transition bg-transparent text-[#4b5563] hover:text-[#111827]" data-era="ww">
              20世紀前半 (1900–1945)
            </button>
            <button class="map-era-btn px-3 py-1.5 rounded text-xs font-medium transition bg-transparent text-[#4b5563] hover:text-[#111827]" data-era="cold">
              冷戰時期 (1946–1990)
            </button>
            <button class="map-era-btn px-3 py-1.5 rounded text-xs font-medium transition bg-transparent text-[#4b5563] hover:text-[#111827]" data-era="modern">
              當代衝突 (1991–2026)
            </button>
          </div>
        </div>

        <!-- Era Historical Briefing Banner -->
        <div class="p-3.5 rounded bg-gray-50 border border-gray-200 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs" id="map-era-banner">
          <div>
            <span class="font-bold text-[#111827]" id="map-era-title">全歷史時期總覽 (1800–2026)</span>：
            <span class="text-[#4b5563]" id="map-era-desc">全球 160 起重大浩劫事件地理分佈。點擊地圖氣泡標記可檢視各國罹難規模、各類別慘劇清單與歷史考證詳情。</span>
          </div>
          <div class="shrink-0 flex items-center gap-4 text-[11px] font-editorial-mono text-[#4b5563]">
            <span>該時期事件數：<strong class="text-[#111827]" id="map-era-count">{total_count}</strong></span>
            <span>累積罹難：<strong class="text-[#991b1b]" id="map-era-deaths">1.53 億人</strong></span>
          </div>
        </div>

        <!-- Interactive Leaflet Map Container -->
        <div class="relative w-full h-[540px] rounded overflow-hidden border border-gray-300">
          <div id="leaflet-map" class="w-full h-full"></div>
          
          <!-- Map Legend Floating Card (Editorial Monotone Style) -->
          <div class="absolute bottom-4 right-4 z-[1000] bg-white/95 border border-gray-300 p-3 rounded text-[11px] space-y-1.5 shadow-md pointer-events-auto">
            <div class="font-bold text-[#111827] border-b border-gray-200 pb-1">氣泡大小 (罹難人數規模)</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded-full bg-[#991b1b] inline-block border border-gray-800"></span> <span class="text-[#111827]">超大型浩劫 (>1,000萬人)</span></div>
            <div class="flex items-center gap-2"><span class="w-3.5 h-3.5 rounded-full bg-[#374151] inline-block border border-gray-800"></span> <span class="text-[#111827]">大型浩劫 (100萬 ~ 1,000萬)</span></div>
            <div class="flex items-center gap-2"><span class="w-3 h-3 rounded-full bg-[#6b7280] inline-block border border-gray-800"></span> <span class="text-[#111827]">中型浩劫 (10萬 ~ 100萬)</span></div>
            <div class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-[#9ca3af] inline-block border border-gray-800"></span> <span class="text-[#111827]">典型/質性慘劇 (<10萬)</span></div>
          </div>
        </div>

        <!-- Era Selected Country Events Detail Strip -->
        <div class="bg-gray-50 border border-gray-200 rounded p-4 text-xs space-y-2">
          <div class="font-bold text-[#111827] flex items-center justify-between">
            <span id="map-detail-title">📍 點擊地圖上任一國家氣泡，即在此展開該國在該時期的事件清單</span>
            <span class="text-[#4b5563] text-[11px] font-editorial-mono">共 83 個主權實體/地理區域收錄</span>
          </div>
          <div id="map-detail-content" class="text-[#4b5563]">
            請點擊地圖標記檢視詳細數據...
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Embedded Datasets & Runtime Scripts -->
  <script>
    const allEvents = {events_json};
    const geoCoords = {coords_json};
    const BASELINE_2026_POP = 8150000000;

    // =========================================================================
    // 1. VIEW SWITCHING LOGIC (新聞標籤頁切換)
    // =========================================================================
    const tabs = document.querySelectorAll('.nav-tab');
    const views = document.querySelectorAll('.view-panel');

    tabs.forEach(tab => {{
      tab.addEventListener('click', () => {{
        const targetViewId = tab.getAttribute('data-view');

        // Update tabs styling (Editorial News Style)
        tabs.forEach(t => {{
          t.className = "nav-tab px-3.5 py-1.5 rounded text-xs font-semibold transition flex items-center gap-1.5 text-[#4b5563] hover:text-[#111827]";
        }});
        tab.className = "nav-tab px-3.5 py-1.5 rounded text-xs font-semibold transition flex items-center gap-1.5 bg-white text-[#111827] shadow-sm border border-gray-300";

        // Switch visible panel
        views.forEach(v => v.classList.add('hidden'));
        document.getElementById(targetViewId).classList.remove('hidden');

        // Trigger specific view initializations if needed
        if (targetViewId === 'view-map') {{
          setTimeout(initMapIfNeeded, 100);
        }} else if (targetViewId === 'view-race') {{
          if (!raceInitialized) initRace();
        }}
      }});
    }});


    // =========================================================================
    // 2. VIEW 1: DATABASE LIST LOGIC (報紙檔案卡片渲染)
    // =========================================================================
    let currentContinent = 'all';
    let currentCategory = 'all';
    let searchQuery = '';

    function updateKPIs(events) {{
      document.getElementById('stat-count').innerText = events.length;
      document.getElementById('stat-count-sub').innerText = `佔全庫 ${{Math.round(events.length / allEvents.length * 100)}}%`;

      const totalMid = events.reduce((sum, e) => sum + (e.death_toll_mid || 0), 0);
      const totalModern = events.reduce((sum, e) => sum + (e.modern_equivalent_mid || 0), 0);

      document.getElementById('stat-deaths').innerText = totalMid.toLocaleString() + ' 人';
      document.getElementById('stat-modern').innerText = totalModern.toLocaleString() + ' 人';

      if (events.length > 0) {{
        let maxImpactEv = events.reduce((prev, cur) => (cur.regional_impact_pct > prev.regional_impact_pct) ? cur : prev);
        document.getElementById('stat-max-impact').innerText = maxImpactEv.regional_impact_pct + '%';
        document.getElementById('stat-max-impact-name').innerText = `${{maxImpactEv.event_name_zh}} (${{maxImpactEv.iso3}})`;
      }} else {{
        document.getElementById('stat-max-impact').innerText = '0%';
        document.getElementById('stat-max-impact-name').innerText = '-';
      }}
    }}

    function renderDatabaseView() {{
      const container = document.getElementById('events-container');
      container.innerHTML = '';
      const q = searchQuery.toLowerCase().trim();

      const filtered = allEvents.filter(e => {{
        const matchCont = currentContinent === 'all' || e.continent === currentContinent;
        const matchCat = currentCategory === 'all' || e.primary_category === currentCategory;
        const matchSearch = !q || 
          e.event_name_zh.toLowerCase().includes(q) || 
          e.event_name_en.toLowerCase().includes(q) || 
          e.location.toLowerCase().includes(q) || 
          e.iso3.toLowerCase().includes(q) || 
          e.qualitative_description.toLowerCase().includes(q);
        return matchCont && matchCat && matchSearch;
      }});

      updateKPIs(filtered);
      document.getElementById('filter-status-text').innerText = `顯示 ${{filtered.length}} / {total_count} 筆歷史人道慘劇檔案`;

      if (filtered.length === 0) {{
        container.innerHTML = '<div class="bg-white border border-gray-300 rounded p-12 text-center text-[#4b5563] font-editorial-serif">查無符合目前篩選條件的人道慘劇事件。</div>';
        return;
      }}

      filtered.forEach(e => {{
        const card = document.createElement('article');
        // Editorial Card Style: Crisp white, solid subtle border, generous newsprint spacing
        card.className = "bg-white border border-gray-300 rounded p-5 hover:border-gray-400 hover:shadow-sm transition space-y-3.5";

        let noteStyle = "bg-gray-50 text-[#4b5563] border-gray-200";
        if (e.data_access_note.includes('Suppression')) {{
          noteStyle = "bg-red-50/60 text-[#991b1b] border-red-200";
        }} else if (e.data_access_note.includes('Chaos') || e.data_access_note.includes('Gap')) {{
          noteStyle = "bg-amber-50/60 text-[#111827] border-amber-200";
        }} else if (e.data_access_note.includes('Consensus') || e.data_access_note.includes('Exhaustive')) {{
          noteStyle = "bg-gray-50 text-[#111827] border-gray-300";
        }}

        const years = e.start_year === e.end_year ? e.start_year : `${{e.start_year}} – ${{e.end_year}}`;
        const scaleFactor = (BASELINE_2026_POP / e.world_pop_at_time).toFixed(1);

        card.innerHTML = `
          <div class="flex flex-col lg:flex-row lg:items-start justify-between gap-4">
            <div class="space-y-1.5 flex-1">
              <!-- Monotone Editorial Badges -->
              <div class="flex flex-wrap items-center gap-1.5">
                <span class="text-xs font-editorial-mono px-2 py-0.5 rounded bg-gray-100 text-[#111827] border border-gray-300 font-semibold">${{e.event_id}}</span>
                <span class="text-xs px-2 py-0.5 rounded bg-gray-100 text-[#111827] font-semibold border border-gray-300">${{years}}</span>
                <span class="text-xs px-2 py-0.5 rounded bg-white text-[#4b5563] border border-gray-300 font-medium">${{e.continent}} · ${{e.iso3}}</span>
                <span class="text-xs px-2 py-0.5 rounded bg-white text-[#4b5563] border border-gray-300 font-medium">${{e.primary_category}}</span>
                <span class="text-xs px-2 py-0.5 rounded border font-medium ${{e.consensus_level === 'High Consensus' ? 'bg-gray-50 text-[#111827] border-gray-300' : (e.consensus_level === 'State Suppressed' ? 'bg-red-50 text-[#991b1b] border-red-200' : 'bg-gray-50 text-[#4b5563] border-gray-300')}}">${{e.consensus_level}}</span>
              </div>
              
              <!-- Serif Headline (WSJ / NYT style) -->
              <h2 class="text-xl md:text-2xl font-bold font-editorial-serif text-[#111827] tracking-tight pt-1">
                ${{e.event_name_zh}} <span class="text-sm font-normal text-[#4b5563] font-editorial-sans">/ ${{e.event_name_en}}</span>
              </h2>
              
              <div class="text-xs text-[#4b5563] flex flex-wrap items-center gap-x-4 gap-y-1">
                <span>📍 地理位置：<span class="text-[#111827]">${{e.location}}</span></span>
                <span>👥 當時全球人口：<span class="text-[#111827]">${{e.world_pop_at_time.toLocaleString()}} 人</span></span>
              </div>
            </div>

            <!-- Key Metric Box (Classical Newspaper Data Box) -->
            <div class="grid grid-cols-2 gap-4 bg-gray-50 px-4 py-3 rounded border border-gray-200 shrink-0 lg:w-80">
              <div>
                <div class="text-[11px] font-semibold text-[#4b5563] uppercase tracking-wider">原始基準罹難 (Mid)</div>
                <div class="text-lg font-bold font-editorial-serif text-[#991b1b] mt-0.5">${{e.death_toll_mid.toLocaleString()}} 人</div>
                <div class="text-[11px] text-[#4b5563]">區間: ${{e.death_toll_low.toLocaleString()}} ~ ${{e.death_toll_high.toLocaleString()}}</div>
              </div>
              <div class="border-l border-gray-200 pl-4">
                <div class="text-[11px] font-semibold text-[#4b5563] uppercase tracking-wider">2026 當代等效</div>
                <div class="text-lg font-bold font-editorial-serif text-[#111827] mt-0.5">${{e.modern_equivalent_mid.toLocaleString()}} 人</div>
                <div class="text-[11px] text-[#4b5563]">區域衝擊率: ${{e.regional_impact_pct}}% (${{scaleFactor}}x)</div>
              </div>
            </div>
          </div>

          <!-- Editorial Lead Paragraph: Disaster Description -->
          <div class="text-xs text-[#111827] leading-relaxed bg-[#fbfbfb] p-3.5 rounded border-l-2 border-gray-400 border-t border-r border-b border-gray-200 font-editorial-sans">
            <strong class="text-[#111827] font-bold">慘劇機制與定性描述：</strong>${{e.qualitative_description}}
          </div>

          <!-- Footnotes & Data Notes -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs pt-1">
            <div class="space-y-1">
              <span class="text-[#4b5563] font-bold">文獻引用來源 (Citation Hierarchy)：</span>
              <p class="text-[#4b5563] leading-relaxed text-[11px]">${{e.sources_summary}}</p>
            </div>
            <div class="space-y-1">
              <span class="text-[#4b5563] font-bold">數據存取規範與缺失限制 (Data Access Note)：</span>
              <div class="p-2.5 rounded border text-[11px] leading-relaxed ${{noteStyle}}">
                ${{e.data_access_note}}
              </div>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    // Filter Listeners
    document.querySelectorAll('.filter-continent').forEach(btn => {{
      btn.addEventListener('click', e => {{
        document.querySelectorAll('.filter-continent').forEach(b => {{
          b.className = "filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300";
        }});
        e.target.className = "filter-btn filter-continent px-3 py-1 rounded text-xs font-medium transition bg-[#111827] text-white border border-[#111827]";
        currentContinent = e.target.getAttribute('data-val');
        renderDatabaseView();
      }});
    }});

    document.querySelectorAll('.filter-cat').forEach(btn => {{
      btn.addEventListener('click', e => {{
        document.querySelectorAll('.filter-cat').forEach(b => {{
          b.className = "filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-white hover:bg-gray-100 text-[#4b5563] hover:text-[#111827] border border-gray-300";
        }});
        e.target.className = "filter-btn filter-cat px-3 py-1 rounded text-xs font-medium transition bg-[#991b1b] text-white border border-[#991b1b]";
        currentCategory = e.target.getAttribute('data-val');
        renderDatabaseView();
      }});
    }});

    document.getElementById('search-input').addEventListener('input', e => {{
      searchQuery = e.target.value;
      renderDatabaseView();
    }});


    // =========================================================================
    // 3. VIEW 2: BAR CHART RACE RUNTIME LOGIC (新聞風格條狀動態圖)
    // =========================================================================
    let raceInitialized = false;
    let racePlaying = false;
    let raceCurrentYear = 1800;
    let raceTimer = null;
    let raceMetric = 'raw'; // 'raw' or 'modern'

    const countryNames = {{}};
    Object.keys(geoCoords).forEach(iso => {{
      countryNames[iso] = geoCoords[iso][2];
    }});

    function getCumulativeDataByYear(targetYear, metric) {{
      const countryTotals = {{}};
      const occurringEvents = [];

      allEvents.forEach(e => {{
        if (e.start_year <= targetYear) {{
          const val = metric === 'raw' ? (e.death_toll_mid || 0) : (e.modern_equivalent_mid || 0);
          countryTotals[e.iso3] = (countryTotals[e.iso3] || 0) + val;
          if (e.start_year === targetYear) {{
            occurringEvents.push(e);
          }}
        }}
      }});

      const sorted = Object.keys(countryTotals).map(iso => ({{
        iso: iso,
        name: countryNames[iso] || iso,
        total: countryTotals[iso]
      }})).sort((a, b) => b.total - a.total);

      return {{
        topList: sorted.slice(0, 10),
        maxVal: sorted.length > 0 ? sorted[0].total : 1,
        eventsThisYear: occurringEvents
      }};
    }}

    function renderRaceFrame(year) {{
      raceCurrentYear = year;
      document.getElementById('race-year-display').innerText = year;
      document.getElementById('race-timeline-slider').value = year;

      const data = getCumulativeDataByYear(year, raceMetric);
      const container = document.getElementById('race-bars-container');
      container.innerHTML = '';

      const hint = document.getElementById('race-current-event-hint');
      if (data.eventsThisYear.length > 0) {{
        const evNames = data.eventsThisYear.map(e => e.event_name_zh).join('、');
        hint.innerHTML = `<span class="text-[#991b1b] font-bold font-editorial-mono">${{year}}年爆發</span>：<span class="text-[#111827] font-medium">${{evNames}}</span>`;
      }} else {{
        hint.innerHTML = `<span class="text-[#4b5563] font-editorial-mono">${{year}}年</span>：<span class="text-[#4b5563]">累積傷亡態勢推進中...</span>`;
      }}

      const maxVal = Math.max(data.maxVal, 100000);

      data.topList.forEach((item, index) => {{
        const pct = Math.max((item.total / maxVal) * 100, 2);
        const row = document.createElement('div');
        row.className = "flex items-center gap-3 transition-all duration-300";

        // Monotone Editorial Color Scheme:
        // Rank 1: Deep Crimson, Rank 2-3: Charcoal, Rank 4+: Muted Slate
        let barColor = "bg-[#6b7280]";
        if (index === 0) barColor = "bg-[#991b1b]";
        else if (index === 1) barColor = "bg-[#374151]";
        else if (index === 2) barColor = "bg-[#4b5563]";

        row.innerHTML = `
          <div class="w-28 text-right text-xs font-semibold text-[#111827] shrink-0 truncate flex items-center justify-end gap-1.5">
            <span class="text-[10px] text-[#4b5563] font-editorial-mono">#${{index + 1}}</span>
            <span>${{item.name}}</span>
          </div>
          <div class="flex-1 bg-gray-100 rounded h-7 overflow-hidden p-0.5 relative flex items-center border border-gray-200">
            <div class="${{barColor}} h-full rounded transition-all duration-300 flex items-center justify-end pr-2 text-[11px] font-bold text-white shadow-xs" style="width: ${{pct}}%;">
            </div>
            <span class="absolute right-2.5 text-[11px] font-editorial-mono text-[#111827] font-bold">
              ${{item.total.toLocaleString()}} 人
            </span>
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function initRace() {{
      raceInitialized = true;
      renderRaceFrame(1800);

      const playBtn = document.getElementById('race-play-btn');
      const resetBtn = document.getElementById('race-reset-btn');
      const slider = document.getElementById('race-timeline-slider');

      playBtn.addEventListener('click', () => {{
        if (racePlaying) {{
          stopRace();
        }} else {{
          startRace();
        }}
      }});

      resetBtn.addEventListener('click', () => {{
        stopRace();
        renderRaceFrame(1800);
      }});

      slider.addEventListener('input', (e) => {{
        stopRace();
        renderRaceFrame(parseInt(e.target.value));
      }});

      document.querySelectorAll('input[name="race-metric"]').forEach(radio => {{
        radio.addEventListener('change', (e) => {{
          raceMetric = e.target.value;
          renderRaceFrame(raceCurrentYear);
        }});
      }});
    }}

    function startRace() {{
      racePlaying = true;
      document.getElementById('race-play-icon').innerText = '⏸';
      document.getElementById('race-play-text').innerText = '暫停';
      document.getElementById('race-play-btn').className = "px-4 py-2 rounded bg-white hover:bg-gray-100 text-xs font-bold text-[#111827] transition flex items-center gap-2 shadow-sm border border-gray-400";

      if (raceCurrentYear >= 2026) raceCurrentYear = 1800;

      raceTimer = setInterval(() => {{
        if (raceCurrentYear < 2026) {{
          raceCurrentYear++;
          renderRaceFrame(raceCurrentYear);
        }} else {{
          stopRace();
        }}
      }}, 120);
    }}

    function stopRace() {{
      racePlaying = false;
      clearInterval(raceTimer);
      document.getElementById('race-play-icon').innerText = '▶';
      document.getElementById('race-play-text').innerText = '繼續播放';
      document.getElementById('race-play-btn').className = "px-4 py-2 rounded bg-[#111827] hover:bg-black text-xs font-bold text-white transition flex items-center gap-2 shadow-sm border border-[#111827]";
    }}


    // =========================================================================
    // 4. VIEW 3: CENTURY GEOPOLITICS MAP RUNTIME LOGIC (淺色報紙底圖)
    // =========================================================================
    let mapInitialized = false;
    let leafletMapInstance = null;
    let mapLayerGroup = null;
    let currentMapEra = 'all';

    const ERA_CONFIGS = {{
      'all': {{
        title: "全歷史時期總覽 (1800–2026)",
        desc: "全球 160 起重大浩劫事件地理分佈。點擊地圖氣泡標記可檢視各國罹難規模、各類別慘劇清單與歷史考證詳情。",
        filter: e => true
      }},
      '19th': {{
        title: "19世紀：殖民征服、前現代帝國焦土與自由放任政策飢荒 (1800–1899)",
        desc: "焦點在地緣擴張、美洲原住民清除、長江流域焦土戰、大英帝國殖民印度/愛爾蘭飢荒與剛果自由邦橡膠暴行。",
        filter: e => e.start_year >= 1800 && e.start_year <= 1899
      }},
      'ww': {{
        title: "20世紀前半：世界大戰、極權國家大清洗與工業化滅絕 (1900–1945)",
        desc: "焦點轉移至歐洲與東亞：納粹大屠殺、蘇聯大清洗與古拉格、烏克蘭大饑荒、日軍侵華暴行、卡廷慘案與二戰地毯式轟炸。",
        filter: e => e.start_year >= 1900 && e.start_year <= 1945
      }},
      'cold': {{
        title: "冷戰時期：意識形態代理人衝突、極權清洗與強制人口控制 (1946–1990)",
        desc: "焦點轉向亞非拉第三世界：中國大饑荒與文革、柬埔寨紅色高棉、印尼清共、孟加拉獨立、南非種族隔離與拉美軍政府白色恐怖。",
        filter: e => e.start_year >= 1946 && e.start_year <= 1990
      }},
      'modern': {{
        title: "當代時期：後冷戰族群清洗、失敗國家與現代高科技圍困 (1991–2026)",
        desc: "焦點在盧安達大滅絕、波士尼亞種族屠殺、剛果世界大戰、敘利亞內戰化武、葉門飢荒、烏克蘭戰爭與加薩人道危機。",
        filter: e => e.start_year >= 1991 && e.start_year <= 2026
      }}
    }};

    function initMapIfNeeded() {{
      const mapContainer = document.getElementById('leaflet-map');
      if (!mapContainer) return;

      if (mapInitialized && leafletMapInstance) {{
        setTimeout(() => {{
          leafletMapInstance.invalidateSize(true);
        }}, 50);
        return;
      }}
      mapInitialized = true;

      // Initialize Leaflet Map centered around Global view
      leafletMapInstance = L.map('leaflet-map', {{
        center: [20, 15],
        zoom: 2,
        minZoom: 1,
        maxZoom: 8,
        worldCopyJump: true
      }});

      // User's CARTO Basemaps API Key
      const CARTO_API_KEY = 'cb1_4hno_1_e6761d1869b2adebd855a765';

      // 1. Primary Layer: CARTO Positron Light (Light Editorial Map Style)
      const cartoLight = L.tileLayer(`https://basemaps.cartocdn.com/rastertiles/light_all/{{z}}/{{x}}/{{y}}.png?key=${{CARTO_API_KEY}}`, {{
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        maxZoom: 19
      }});

      // 2. Secondary Layer: CARTO Light Retina fallback
      const cartoLightRetina = L.tileLayer(`https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png?key=${{CARTO_API_KEY}}`, {{
        attribution: '&copy; CARTO &copy; OpenStreetMap',
        subdomains: 'abcd',
        maxZoom: 19
      }});

      // 3. Fallback Layer: Standard OpenStreetMap
      const osmFallback = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 19
      }});

      cartoLight.on('tileerror', function() {{
        if (!leafletMapInstance.hasLayer(cartoLightRetina)) {{
          cartoLightRetina.addTo(leafletMapInstance);
        }} else if (!leafletMapInstance.hasLayer(osmFallback)) {{
          osmFallback.addTo(leafletMapInstance);
        }}
      }});

      cartoLight.addTo(leafletMapInstance);

      mapLayerGroup = L.layerGroup().addTo(leafletMapInstance);

      setTimeout(() => {{
        leafletMapInstance.invalidateSize(true);
      }}, 150);

      // Bind Era Switch Buttons
      document.querySelectorAll('.map-era-btn').forEach(btn => {{
        btn.addEventListener('click', (e) => {{
          document.querySelectorAll('.map-era-btn').forEach(b => {{
            b.className = "map-era-btn px-3 py-1.5 rounded text-xs font-medium transition bg-transparent text-[#4b5563] hover:text-[#111827]";
          }});
          btn.className = "map-era-btn px-3 py-1.5 rounded text-xs font-bold transition bg-[#111827] text-white shadow-sm border border-[#111827]";
          currentMapEra = btn.getAttribute('data-era');
          renderMapEra(currentMapEra);
        }});
      }});

      renderMapEra('all');
    }}

    function renderMapEra(eraKey) {{
      const cfg = ERA_CONFIGS[eraKey] || ERA_CONFIGS['all'];
      document.getElementById('map-era-title').innerText = cfg.title;
      document.getElementById('map-era-desc').innerText = cfg.desc;

      const eraEvents = allEvents.filter(cfg.filter);
      const eraDeaths = eraEvents.reduce((acc, c) => acc + (c.death_toll_mid || 0), 0);
      document.getElementById('map-era-count').innerText = `${{eraEvents.length}} 起`;
      document.getElementById('map-era-deaths').innerText = (eraDeaths / 100000000).toFixed(2) + ' 億人';

      mapLayerGroup.clearLayers();

      const countryData = {{}};
      eraEvents.forEach(e => {{
        if (!countryData[e.iso3]) {{
          countryData[e.iso3] = {{
            iso: e.iso3,
            name: countryNames[e.iso3] || e.location,
            totalMid: 0,
            events: []
          }};
        }}
        countryData[e.iso3].totalMid += (e.death_toll_mid || 0);
        countryData[e.iso3].events.push(e);
      }});

      // Draw bubble markers (Editorial News Monotone Palette)
      Object.keys(countryData).forEach(iso => {{
        const c = countryData[iso];
        const coord = geoCoords[iso];
        if (!coord) return;

        const deaths = c.totalMid;

        let radius = 6;
        let color = "#9ca3af";
        let fillOpacity = 0.55;

        if (deaths >= 10000000) {{
          radius = 24;
          color = "#991b1b"; // Deep crimson
          fillOpacity = 0.75;
        }} else if (deaths >= 1000000) {{
          radius = 17;
          color = "#374151"; // Dark charcoal
          fillOpacity = 0.65;
        }} else if (deaths >= 100000) {{
          radius = 11;
          color = "#4b5563"; // Medium charcoal
          fillOpacity = 0.6;
        }} else if (deaths >= 10000) {{
          radius = 8;
          color = "#6b7280";
          fillOpacity = 0.5;
        }} else {{
          radius = 5.5;
          color = "#9ca3af";
          fillOpacity = 0.45;
        }}

        const circle = L.circleMarker([coord[0], coord[1]], {{
          radius: radius,
          fillColor: color,
          color: "#111827",
          weight: 1,
          opacity: 0.8,
          fillOpacity: fillOpacity
        }});

        // Tooltip on Hover (Crisp News Paper Tooltip)
        circle.bindTooltip(`
          <div class="text-xs font-sans">
            <strong class="text-[#111827]">${{coord[2]}} (${{iso}})</strong><br>
            該時期浩劫：<strong class="text-[#991b1b]">${{deaths.toLocaleString()}} 人</strong><br>
            <span class="text-[#4b5563]">事件數：${{c.events.length}} 起</span>
          </div>
        `, {{ direction: 'top', className: 'dark-tooltip' }});

        circle.on('click', () => {{
          showCountryMapDetail(c);
        }});

        mapLayerGroup.addLayer(circle);
      }});
    }}

    function showCountryMapDetail(countryObj) {{
      const titleSpan = document.getElementById('map-detail-title');
      const contentDiv = document.getElementById('map-detail-content');

      titleSpan.innerHTML = `📍 <span class="text-[#111827] font-bold font-editorial-serif">${{countryObj.name}} (${{countryObj.iso}})</span> 浩劫檔案 · 累積中值罹難：<span class="text-[#991b1b] font-bold font-editorial-mono">${{countryObj.totalMid.toLocaleString()}} 人</span> (${{countryObj.events.length}} 起事件)`;

      let html = `<div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 pt-1">`;
      countryObj.events.forEach(e => {{
        const yr = e.start_year === e.end_year ? e.start_year : `${{e.start_year}}–${{e.end_year}}`;
        html += `
          <div class="p-3 rounded bg-white border border-gray-300 space-y-1 shadow-2xs">
            <div class="flex items-center justify-between">
              <span class="font-bold text-[#111827] font-editorial-serif text-xs">${{e.event_name_zh}}</span>
              <span class="font-editorial-mono text-[#991b1b] font-bold text-xs">${{e.death_toll_mid.toLocaleString()}} 人</span>
            </div>
            <div class="flex items-center gap-2 text-[10px] text-[#4b5563]">
              <span class="font-editorial-mono px-1 rounded bg-gray-100 border border-gray-200">${{yr}}</span>
              <span>${{e.primary_category}}</span>
              <span class="text-[#111827]">等效: ${{e.modern_equivalent_mid.toLocaleString()}}</span>
            </div>
            <p class="text-[11px] text-[#4b5563] line-clamp-2 leading-relaxed">${{e.qualitative_description}}</p>
          </div>
        `;
      }});
      html += `</div>`;
      contentDiv.innerHTML = html;
    }}


    // =========================================================================
    // 5. BOOTSTRAP INITIAL VIEW
    // =========================================================================
    renderDatabaseView();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated index.html with newspaper editorial styling and {total_count} events!")