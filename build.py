import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
DATA_JSON = json.dumps(data, ensure_ascii=False)

html = r"""<title>이수의 코트</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

  :root{
    --page:#f6f5ee; --surface:#ffffff; --surface-2:#eef0e2; --surface-3:#e7e9d8;
    --ink:#15180d; --ink-2:#54573f; --ink-3:#8b8d72;
    --line:#e0e1d1; --border:rgba(21,24,13,.11);
    --accent:#5c7a00; --accent-strong:#3f5600; --accent-soft:#e9efd0; --accent-ink:#2c3d00;
    --ball:#c7d900; --clay:#b8471f; --clay-soft:#f6e2d3; --clay-ink:#8a350f;
    --good:#0ca30c; --critical:#d03b3b; --warning:#c98500;
    --good-soft:#e3f3df; --critical-soft:#fbe6e4;
    --shadow:0 1px 2px rgba(21,24,13,.05), 0 10px 28px -16px rgba(21,24,13,.28);
    --court-a:#3f6f1f; --court-b:#356017; --court-line:#f4f2e4;
    color-scheme:light;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --page:#0d1109; --surface:#141a0e; --surface-2:#1a2113; --surface-3:#212a17;
      --ink:#f4f5ec; --ink-2:#c2c5ab; --ink-3:#899073;
      --line:#28321b; --border:rgba(255,255,255,.11);
      --accent:#cfe62a; --accent-strong:#e3f74d; --accent-soft:#243008; --accent-ink:#e3f74d;
      --ball:#e3f74d; --clay:#e2793f; --clay-soft:#2c180d; --clay-ink:#f0a97a;
      --good:#2ecf2e; --critical:#e66767; --warning:#e0a83a;
      --good-soft:#132615; --critical-soft:#2c1414;
      --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 32px -16px rgba(0,0,0,.6);
      --court-a:#1c2a10; --court-b:#16220c; --court-line:#3a4a26;
      color-scheme:dark;
    }
  }
  :root[data-theme="dark"]{
    --page:#0d1109; --surface:#141a0e; --surface-2:#1a2113; --surface-3:#212a17;
    --ink:#f4f5ec; --ink-2:#c2c5ab; --ink-3:#899073;
    --line:#28321b; --border:rgba(255,255,255,.11);
    --accent:#cfe62a; --accent-strong:#e3f74d; --accent-soft:#243008; --accent-ink:#e3f74d;
    --ball:#e3f74d; --clay:#e2793f; --clay-soft:#2c180d; --clay-ink:#f0a97a;
    --good:#2ecf2e; --critical:#e66767; --warning:#e0a83a;
    --good-soft:#132615; --critical-soft:#2c1414;
    --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 32px -16px rgba(0,0,0,.6);
    --court-a:#1c2a10; --court-b:#16220c; --court-line:#3a4a26;
    color-scheme:dark;
  }

  *{box-sizing:border-box;}
  [hidden]{ display:none !important; }
  html,body{margin:0;padding:0;}
  body{
    background:var(--page); color:var(--ink);
    font-family:'Manrope',system-ui,-apple-system,'Segoe UI',sans-serif;
    -webkit-font-smoothing:antialiased;
  }
  ::selection{ background:var(--accent); color:var(--court-b); }

  .wrap{ max-width:1180px; margin:0 auto; padding:0 28px; }

  /* ---------- HERO ---------- */
  .hero{
    position:relative; overflow:hidden; isolation:isolate;
    background:
      repeating-linear-gradient(90deg, var(--court-b) 0 2px, transparent 2px 48px),
      linear-gradient(180deg, var(--court-a), var(--court-b) 72%);
    color:var(--court-line);
    padding:64px 0 40px;
  }
  .hero::before{
    content:""; position:absolute; inset:0; z-index:-1;
    background-image:
      radial-gradient(ellipse 900px 420px at 82% -8%, rgba(255,255,255,.10), transparent 60%);
  }
  .court-lines{ position:absolute; inset:0; z-index:-1; opacity:.9; }
  .hero-top{ display:flex; align-items:flex-start; justify-content:space-between; gap:24px; flex-wrap:wrap; }
  .eyebrow{
    font-family:'JetBrains Mono',monospace; font-size:12.5px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--ball); font-weight:600; display:flex; align-items:center; gap:8px;
  }
  .eyebrow .dot{ width:7px;height:7px;border-radius:50%; background:var(--ball); box-shadow:0 0 0 4px rgba(199,217,0,.22); }
  .title-row{ display:flex; align-items:center; gap:22px; margin-top:14px; flex-wrap:wrap; }
  .ball-mark{ width:74px; height:74px; flex:none; filter:drop-shadow(0 6px 14px rgba(0,0,0,.35)); }
  h1.hero-title{
    font-family:'Anton',sans-serif; font-weight:400; margin:0;
    font-size:clamp(40px,7vw,84px); line-height:.92; letter-spacing:.01em;
    text-wrap:balance; color:#fbfbf4;
  }
  h1.hero-title em{ font-style:normal; color:var(--ball); }
  .hero-sub{
    margin:14px 0 0; font-size:16.5px; color:rgba(244,244,232,.82); max-width:560px; line-height:1.55;
  }
  .hero-meta{
    margin-top:26px; display:flex; gap:10px; flex-wrap:wrap; align-items:center;
  }
  .meta-chip{
    font-family:'JetBrains Mono',monospace; font-size:12px; letter-spacing:.02em;
    background:rgba(0,0,0,.22); border:1px solid rgba(255,255,255,.14); color:rgba(244,244,232,.92);
    padding:7px 12px; border-radius:999px; display:flex; align-items:center; gap:7px;
  }
  .meta-chip b{ color:var(--ball); font-weight:700; }
  .next-banner{
    margin-top:22px; display:flex; align-items:center; gap:14px; flex-wrap:wrap;
    background:rgba(0,0,0,.26); border:1px solid rgba(255,255,255,.16);
    border-left:3px solid var(--ball);
    padding:14px 18px; border-radius:12px; max-width:640px;
  }
  .next-banner .lbl{ font-family:'JetBrains Mono',monospace; font-size:11px; text-transform:uppercase; letter-spacing:.1em; color:var(--ball); font-weight:700; }
  .next-banner .name{ font-weight:700; color:#fbfbf4; }
  .next-banner .sub{ color:rgba(244,244,232,.7); font-size:13.5px; }

  /* ---------- NAV / TABS ---------- */
  .controls-bar{
    position:sticky; top:0; z-index:20; background:var(--page);
    border-bottom:1px solid var(--line);
  }
  .controls-inner{ display:flex; align-items:center; gap:18px; padding:14px 0; flex-wrap:wrap; }
  .tabs{ display:flex; gap:6px; background:var(--surface-2); padding:4px; border-radius:11px; }
  .tab{
    font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:600; letter-spacing:.02em;
    padding:8px 16px; border-radius:8px; border:none; background:transparent; color:var(--ink-2);
    cursor:pointer; transition:background .15s, color .15s;
  }
  .tab[aria-pressed="true"]{ background:var(--surface); color:var(--accent-ink); box-shadow:var(--shadow); }
  .tab:hover:not([aria-pressed="true"]){ color:var(--ink); }

  .grade-filter{ display:flex; gap:6px; flex-wrap:wrap; margin-left:auto; }
  .chip-btn{
    font-size:12.5px; font-weight:600; padding:7px 13px; border-radius:999px;
    border:1px solid var(--border); background:var(--surface); color:var(--ink-2); cursor:pointer;
  }
  .chip-btn[aria-pressed="true"]{ background:var(--accent-soft); border-color:var(--accent); color:var(--accent-ink); }

  .search-box{
    display:flex; align-items:center; gap:8px; background:var(--surface); border:1px solid var(--border);
    border-radius:9px; padding:7px 12px; min-width:180px;
  }
  .search-box input{
    border:none; outline:none; background:transparent; color:var(--ink); font-size:13.5px; width:100%;
    font-family:'Manrope',sans-serif;
  }
  .search-box svg{ flex:none; opacity:.5; }

  main{ padding:36px 0 80px; }
  section{ margin-bottom:52px; }
  .section-head{ display:flex; align-items:baseline; justify-content:space-between; gap:16px; margin-bottom:18px; flex-wrap:wrap; }
  .section-head h2{
    font-family:'Anton',sans-serif; font-weight:400; font-size:24px; letter-spacing:.01em; margin:0; color:var(--ink);
  }
  .section-head .hint{ font-size:13px; color:var(--ink-3); }

  /* ---------- STAT CARDS ---------- */
  .stat-grid{ display:grid; grid-template-columns:repeat(6,1fr); gap:12px; }
  .stat-card{
    background:var(--surface); border:1px solid var(--border); border-radius:14px; padding:18px 16px;
    box-shadow:var(--shadow); display:flex; flex-direction:column; gap:8px; min-width:0;
  }
  .stat-card .k{ font-size:12px; color:var(--ink-3); font-weight:600; letter-spacing:.02em; }
  .stat-card .v{
    font-family:'JetBrains Mono',monospace; font-size:26px; font-weight:700; color:var(--ink);
    font-variant-numeric:tabular-nums; line-height:1.1; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  }
  .stat-card .v small{ font-size:13px; font-weight:600; color:var(--ink-3); }
  .stat-card .d{ font-size:12px; color:var(--ink-3); }
  .stat-card .d.up{ color:var(--good); }
  .stat-card .d.down{ color:var(--critical); }
  .stat-card.accent{ background:var(--accent-soft); border-color:var(--accent); }
  .stat-card.accent .v{ color:var(--accent-ink); }

  @media (max-width:980px){ .stat-grid{ grid-template-columns:repeat(3,1fr); } }
  @media (max-width:600px){ .stat-grid{ grid-template-columns:repeat(2,1fr); } }

  /* ---------- CHARTS ---------- */
  .chart-grid{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }
  @media (max-width:860px){ .chart-grid{ grid-template-columns:1fr; } }
  .chart-card{
    background:var(--surface); border:1px solid var(--border); border-radius:14px; padding:20px 20px 12px;
    box-shadow:var(--shadow);
  }
  .chart-card .ch-head{ display:flex; align-items:center; justify-content:space-between; margin-bottom:6px; }
  .chart-card h3{ margin:0; font-size:14.5px; font-weight:700; }
  .chart-card .ch-note{ font-size:11.5px; color:var(--ink-3); margin-bottom:10px; }
  .table-toggle{
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:600; color:var(--ink-2);
    background:var(--surface-2); border:1px solid var(--border); border-radius:7px; padding:5px 9px; cursor:pointer;
  }
  .table-toggle:hover{ color:var(--ink); }
  svg.chart{ width:100%; height:auto; overflow:visible; }
  .chart-line{ fill:none; stroke:var(--accent-strong); stroke-width:2; }
  .chart-area{ opacity:.14; }
  .chart-dot{ fill:var(--surface); stroke:var(--accent-strong); stroke-width:2; }
  .chart-dot.end{ fill:var(--accent-strong); r:4.5; }
  .chart-grid-line{ stroke:var(--line); stroke-width:1; }
  .chart-axis-label{ font-family:'JetBrains Mono',monospace; font-size:10px; fill:var(--ink-3); }
  .chart-guide{ stroke:var(--ink-3); stroke-width:1; stroke-dasharray:2 3; opacity:0; }
  .chart-hover-dot{ fill:var(--accent-strong); opacity:0; }
  .chart-tip{
    position:absolute; pointer-events:none; background:var(--ink); color:var(--page);
    font-family:'JetBrains Mono',monospace; font-size:11px; padding:7px 10px; border-radius:8px;
    line-height:1.5; opacity:0; transform:translate(-50%,-115%); white-space:nowrap; z-index:5;
    box-shadow:var(--shadow);
  }
  .chart-wrap{ position:relative; }
  .data-table{ display:none; width:100%; border-collapse:collapse; font-family:'JetBrains Mono',monospace; font-size:12px; }
  .data-table.show{ display:table; }
  .data-table th, .data-table td{ text-align:left; padding:6px 8px; border-bottom:1px solid var(--line); }
  .data-table th{ color:var(--ink-3); font-weight:600; }
  .data-table td.num{ text-align:right; font-variant-numeric:tabular-nums; }
  svg.chart.hidden-chart{ display:none; }
  .table-scroll{ overflow-x:auto; }

  /* ---------- HEAD-TO-HEAD SEARCH ---------- */
  .h2h-box{ position:relative; max-width:420px; }
  .h2h-input-wrap{ max-width:none; }
  .h2h-suggest{
    position:absolute; top:calc(100% + 6px); left:0; right:0; z-index:15;
    background:var(--surface); border:1px solid var(--border); border-radius:11px; box-shadow:var(--shadow);
    overflow:hidden; max-height:280px; overflow-y:auto;
  }
  .h2h-suggest button{
    display:flex; align-items:center; justify-content:space-between; gap:10px; width:100%;
    text-align:left; padding:10px 14px; border:none; background:transparent; cursor:pointer;
    font-family:'Manrope',sans-serif; font-size:13.5px; color:var(--ink); border-bottom:1px solid var(--line);
  }
  .h2h-suggest button:last-child{ border-bottom:none; }
  .h2h-suggest button:hover{ background:var(--surface-2); }
  .h2h-suggest .cnt{ font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--ink-3); flex:none; }
  .h2h-suggest .empty{ padding:14px; font-size:13px; color:var(--ink-3); }

  .h2h-card{
    margin-top:18px; background:var(--surface); border:1px solid var(--border); border-radius:14px;
    box-shadow:var(--shadow); overflow:hidden;
  }
  .h2h-head{ padding:18px 20px 16px; border-bottom:1px solid var(--line); display:flex; align-items:center; gap:16px; flex-wrap:wrap; justify-content:space-between; }
  .h2h-name{ font-family:'Anton',sans-serif; font-weight:400; font-size:22px; letter-spacing:.01em; color:var(--ink); }
  .h2h-name .alt{ font-family:'Manrope',sans-serif; font-size:12px; font-weight:600; color:var(--ink-3); margin-left:8px; }
  .h2h-record{ display:flex; gap:22px; flex-wrap:wrap; }
  .h2h-stat{ text-align:right; }
  .h2h-stat .k{ font-size:11px; color:var(--ink-3); font-weight:600; }
  .h2h-stat .v{ font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:var(--ink); font-variant-numeric:tabular-nums; }
  .h2h-stat .v.win{ color:var(--good); }
  .h2h-stat .v.loss{ color:var(--critical); }

  @media (max-width:560px){ .h2h-box{ max-width:none; } }

  /* ---------- TIMELINE ---------- */
  .empty-note{ padding:40px 20px; text-align:center; color:var(--ink-3); font-size:14px; background:var(--surface); border:1px dashed var(--border); border-radius:14px; }
  .t-list{ display:flex; flex-direction:column; gap:10px; }
  .t-card{
    background:var(--surface); border:1px solid var(--border); border-radius:14px; box-shadow:var(--shadow);
    overflow:hidden;
  }
  .t-row{
    display:flex; align-items:center; gap:16px; padding:14px 18px; cursor:pointer; user-select:none;
  }
  .t-date{
    font-family:'JetBrains Mono',monospace; text-align:center; flex:none; width:52px; line-height:1.05;
  }
  .t-date .mo{ font-size:11px; color:var(--ink-3); font-weight:600; }
  .t-date .dy{ font-size:19px; font-weight:700; color:var(--ink); }
  .t-main{ flex:1; min-width:0; }
  .t-name{ font-weight:700; font-size:14.5px; color:var(--ink); display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
  .t-name .grade-pill{
    font-family:'JetBrains Mono',monospace; font-size:10.5px; font-weight:700; padding:2px 7px; border-radius:5px;
    background:var(--surface-3); color:var(--ink-2); flex:none;
  }
  .t-sub{ font-size:12.5px; color:var(--ink-3); margin-top:3px; display:flex; gap:10px; flex-wrap:wrap; }
  .t-results{ display:flex; gap:6px; flex:none; }
  .result-pill{
    font-family:'JetBrains Mono',monospace; font-size:11.5px; font-weight:700; padding:5px 10px; border-radius:7px;
    background:var(--surface-2); color:var(--ink-2); white-space:nowrap;
  }
  .result-pill.tier-top{ background:var(--accent-soft); color:var(--accent-ink); }
  .result-pill.tier-mid{ background:var(--clay-soft); color:var(--clay-ink); }
  .t-points{ text-align:right; flex:none; width:88px; font-family:'JetBrains Mono',monospace; }
  .t-points .p{ font-weight:700; font-size:14px; color:var(--ink); }
  .t-points .r{ font-size:11px; color:var(--ink-3); }
  .t-chev{ flex:none; color:var(--ink-3); transition:transform .18s; }
  .t-card.open .t-chev{ transform:rotate(90deg); }
  .t-card.dnp .t-row{ opacity:.55; }

  @media (max-width:640px){
    .t-row{ flex-wrap:wrap; row-gap:8px; padding:14px 16px; }
    .t-date{ order:1; }
    .t-chev{ order:2; margin-left:auto; }
    .t-main{ order:3; flex:1 1 100%; }
    .t-results{ order:4; flex-wrap:wrap; }
    .t-points{ order:5; margin-left:auto; text-align:right; width:auto; }
  }

  .t-detail{ max-height:0; overflow:hidden; transition:max-height .25s ease; border-top:1px solid var(--line); }
  .t-card.open .t-detail{ border-top:1px solid var(--line); }
  .t-detail-inner{ padding:14px 18px 18px; }
  .match-table{ width:100%; border-collapse:collapse; font-size:12.5px; }
  .match-table th{
    text-align:left; font-family:'JetBrains Mono',monospace; font-size:10.5px; text-transform:uppercase;
    letter-spacing:.05em; color:var(--ink-3); font-weight:600; padding:6px 8px; border-bottom:1px solid var(--line);
  }
  .match-table td{ padding:8px; border-bottom:1px solid var(--line); vertical-align:top; }
  .match-table tr:last-child td{ border-bottom:none; }
  .round-tag{ font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:700; color:var(--ink-2); white-space:nowrap; }
  .opp{ font-weight:600; }
  .opp .team{ font-weight:400; color:var(--ink-3); font-size:11.5px; }
  .partner-line{ font-weight:600; font-size:11px; color:var(--accent-ink); background:var(--accent-soft); display:inline-block; padding:2px 8px; border-radius:6px; margin-bottom:5px; }
  .sets{ font-family:'JetBrains Mono',monospace; font-variant-numeric:tabular-nums; display:flex; gap:6px; flex-wrap:wrap; }
  .set-box{ background:var(--surface-2); border-radius:5px; padding:2px 7px; font-size:12px; }
  .wl-badge{
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:700; padding:3px 9px; border-radius:6px;
    white-space:nowrap;
  }
  .wl-badge.win{ background:var(--good-soft); color:var(--good); }
  .wl-badge.loss{ background:var(--critical-soft); color:var(--critical); }
  .wl-badge.na{ background:var(--surface-2); color:var(--ink-3); }
  .note-chip{ display:block; font-size:11.5px; color:var(--ink-2); background:var(--surface-2); border-radius:6px; padding:4px 8px; margin-top:4px; line-height:1.4; }
  .no-detail{ padding:16px 4px; font-size:13px; color:var(--ink-3); }

  footer{ border-top:1px solid var(--line); padding:26px 0 60px; }
  footer .wrap{ display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; }
  footer p{ margin:0; font-size:12px; color:var(--ink-3); font-family:'JetBrains Mono',monospace; }

  /* ---------- EDITING UI ---------- */
  .btn-primary{
    font-family:'JetBrains Mono',monospace; font-size:12.5px; font-weight:700; letter-spacing:.02em;
    background:var(--accent); color:var(--court-b); border:none; border-radius:9px; padding:9px 16px;
    cursor:pointer; display:inline-flex; align-items:center; gap:6px; white-space:nowrap;
  }
  .btn-primary:hover{ filter:brightness(1.06); }
  .btn-primary:disabled{ opacity:.5; cursor:not-allowed; filter:none; }
  .btn-ghost{
    font-family:'Manrope',sans-serif; font-size:12.5px; font-weight:600;
    background:var(--surface-2); color:var(--ink-2); border:1px solid var(--border); border-radius:8px;
    padding:8px 14px; cursor:pointer;
  }
  .btn-ghost:hover{ color:var(--ink); }
  .btn-danger{
    font-family:'Manrope',sans-serif; font-size:12.5px; font-weight:600;
    background:var(--critical-soft); color:var(--critical); border:1px solid transparent; border-radius:8px;
    padding:8px 14px; cursor:pointer;
  }
  .icon-btn{
    flex:none; width:28px; height:28px; display:inline-flex; align-items:center; justify-content:center;
    border-radius:7px; border:1px solid var(--border); background:var(--surface); color:var(--ink-2);
    cursor:pointer; font-size:13px;
  }
  .icon-btn:hover{ background:var(--surface-2); color:var(--ink); }
  .icon-btn.danger:hover{ background:var(--critical-soft); color:var(--critical); border-color:transparent; }
  .t-actions{ display:flex; gap:6px; flex:none; }
  .match-actions{ display:flex; gap:5px; }

  .hero-side{ display:flex; flex-direction:column; align-items:flex-end; gap:8px; }
  .save-status{
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:600; letter-spacing:.02em;
    display:inline-flex; align-items:center; gap:6px; padding:6px 11px; border-radius:999px;
    background:rgba(0,0,0,.22); border:1px solid rgba(255,255,255,.14); color:rgba(244,244,232,.85);
  }
  .save-status .sdot{ width:7px; height:7px; border-radius:50%; background:var(--ink-3); flex:none; }
  .save-status[data-state="saving"] .sdot{ background:var(--warning); animation:pulse 1s infinite ease-in-out; }
  .save-status[data-state="saved"] .sdot{ background:var(--good); }
  .save-status[data-state="error"] .sdot, .save-status[data-state="conflict"] .sdot{ background:var(--critical); }
  .save-status[data-state="readonly"] .sdot, .save-status[data-state="offline"] .sdot{ background:var(--ink-3); }
  @keyframes pulse{ 0%,100%{ opacity:1; } 50%{ opacity:.35; } }

  .auth-btn{
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:600; letter-spacing:.02em;
    display:inline-flex; align-items:center; gap:6px; padding:6px 12px; border-radius:999px;
    background:rgba(0,0,0,.22); border:1px solid rgba(255,255,255,.14); color:rgba(244,244,232,.92);
    cursor:pointer; white-space:nowrap;
  }
  .auth-btn:hover{ background:rgba(0,0,0,.32); }
  .auth-btn[data-signed-in="true"]{ background:var(--accent-soft); border-color:var(--accent); color:var(--accent-ink); }

  .readonly-note{
    font-size:12.5px; color:var(--ink-3); background:var(--surface-2); border:1px dashed var(--border);
    border-radius:9px; padding:9px 14px; margin-bottom:16px;
  }

  .modal-overlay{
    position:fixed; inset:0; background:rgba(10,12,7,.55); backdrop-filter:blur(2px);
    display:flex; align-items:flex-start; justify-content:center; padding:5vh 16px; z-index:100; overflow-y:auto;
  }
  .modal-overlay[hidden]{ display:none; }
  .modal{
    background:var(--surface); border-radius:16px; box-shadow:var(--shadow); width:100%; max-width:560px;
    padding:22px 24px 24px; margin-bottom:5vh;
  }
  .modal h3{ font-family:'Anton',sans-serif; font-weight:400; font-size:20px; margin:0 0 4px; letter-spacing:.01em; }
  .modal .modal-sub{ font-size:12.5px; color:var(--ink-3); margin:0 0 18px; }
  .form-grid{ display:grid; grid-template-columns:1fr 1fr; gap:12px 14px; }
  .form-grid .full{ grid-column:1 / -1; }
  .field label{ display:block; font-size:11.5px; font-weight:700; color:var(--ink-2); margin-bottom:5px; letter-spacing:.01em; }
  .field input[type="text"], .field input[type="number"], .field input[type="date"], .field select, .field textarea{
    width:100%; font-family:'Manrope',sans-serif; font-size:13.5px; color:var(--ink); background:var(--page);
    border:1px solid var(--border); border-radius:8px; padding:8px 10px; outline:none;
  }
  .field textarea{ resize:vertical; min-height:52px; font-family:'Manrope',sans-serif; }
  .field input:focus, .field select:focus, .field textarea:focus{ border-color:var(--accent); }
  .field.check{ display:flex; align-items:center; gap:8px; flex-direction:row; margin-top:22px; }
  .field.check label{ margin:0; font-size:12.5px; }
  .set-row{ display:flex; align-items:center; gap:8px; margin-bottom:6px; }
  .set-row input{ width:64px; }
  .set-row span{ color:var(--ink-3); font-family:'JetBrains Mono',monospace; }
  .modal-actions{ display:flex; justify-content:space-between; align-items:center; margin-top:20px; gap:10px; }
  .modal-actions .right{ display:flex; gap:8px; margin-left:auto; }
  .modal-error{ font-size:12px; color:var(--critical); margin-top:10px; display:none; }
  .modal-error.show{ display:block; }
  fieldset.doubles-fields{ border:1px dashed var(--border); border-radius:10px; padding:12px; grid-column:1/-1; display:none; }
  fieldset.doubles-fields.show{ display:grid; grid-template-columns:1fr 1fr; gap:12px 14px; }
  fieldset.doubles-fields legend{ font-size:11px; font-weight:700; color:var(--accent-ink); padding:0 4px; }

  @media (max-width:560px){ .form-grid{ grid-template-columns:1fr; } fieldset.doubles-fields.show{ grid-template-columns:1fr; } }

  @media (prefers-reduced-motion: reduce){ *{ transition:none !important; } }
</style>

<header class="hero">
  <svg class="court-lines" viewBox="0 0 1200 420" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <rect x="60" y="40" width="1080" height="340" fill="none" stroke="var(--court-line)" stroke-opacity=".55" stroke-width="2.5"/>
    <rect x="60" y="80" width="1080" height="260" fill="none" stroke="var(--court-line)" stroke-opacity=".4" stroke-width="2"/>
    <line x1="60" y1="210" x2="1140" y2="210" stroke="var(--court-line)" stroke-opacity=".55" stroke-width="2.5" stroke-dasharray="1 10" stroke-linecap="round"/>
    <line x1="390" y1="80" x2="390" y2="340" stroke="var(--court-line)" stroke-opacity=".35" stroke-width="2"/>
    <line x1="810" y1="80" x2="810" y2="340" stroke="var(--court-line)" stroke-opacity=".35" stroke-width="2"/>
    <line x1="600" y1="40" x2="600" y2="380" stroke="var(--court-line)" stroke-opacity=".55" stroke-width="2.5"/>
    <line x1="580" y1="210" x2="620" y2="210" stroke="var(--court-line)" stroke-opacity=".55" stroke-width="4"/>
  </svg>
  <div class="wrap">
    <div class="hero-top">
      <div>
        <div class="eyebrow"><span class="dot"></span>PLAYER RECORD BOARD</div>
        <div class="title-row">
          <svg class="ball-mark" viewBox="0 0 100 100" aria-hidden="true">
            <circle cx="50" cy="50" r="46" fill="var(--ball)"/>
            <path d="M 12 24 Q 50 55 12 76" fill="none" stroke="var(--court-b)" stroke-width="5" stroke-linecap="round"/>
            <path d="M 88 24 Q 50 55 88 76" fill="none" stroke="var(--court-b)" stroke-width="5" stroke-linecap="round"/>
          </svg>
          <h1 class="hero-title">이수의 <em>코트</em></h1>
        </div>
        <p class="hero-sub">신이수 선수의 전국 주니어 테니스대회 시즌 기록관리 현황판 &mdash; 대회 성적, 포인트·랭킹 추이, 경기별 세트 스코어를 한눈에 확인합니다.</p>
        <div class="hero-meta">
          <span class="meta-chip">선수 <b>신이수</b></span>
          <span class="meta-chip">기록 시즌 <b>2025&ndash;2026</b></span>
          <span class="meta-chip">최근 업데이트 <b id="genDate">-</b></span>
        </div>
        <div class="next-banner" id="nextBanner" hidden>
          <div>
            <div class="lbl">NEXT / ONGOING</div>
            <div class="name" id="nextName">-</div>
            <div class="sub" id="nextSub">-</div>
          </div>
        </div>
      </div>
      <div class="hero-side">
        <span class="save-status" id="saveStatus" data-state="idle" hidden><span class="sdot"></span><span id="saveStatusText">저장됨</span></span>
        <button type="button" class="auth-btn" id="authBtn">🔒 관리자 로그인</button>
      </div>
    </div>
  </div>
</header>

<div class="controls-bar">
  <div class="wrap controls-inner">
    <div class="tabs" id="seasonTabs" role="tablist" aria-label="시즌 선택"></div>
    <div class="search-box">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input type="text" id="searchInput" placeholder="대회명 또는 지역 검색" />
    </div>
    <div class="grade-filter" id="gradeFilter"></div>
  </div>
</div>

<main class="wrap">
  <section id="statsSection">
    <div class="section-head"><h2>시즌 요약</h2><span class="hint" id="statsHint"></span></div>
    <div class="stat-grid" id="statGrid"></div>
  </section>

  <section>
    <div class="section-head">
      <h2>포인트 &middot; 랭킹 추이</h2>
      <span class="hint">대회 종료일 기준 &middot; 랭킹은 숫자가 낮을수록 상위권</span>
    </div>
    <div class="chart-grid">
      <div class="chart-card">
        <div class="ch-head"><h3>전국 랭킹 추이</h3><button class="table-toggle" data-target="rankChart">표로 보기</button></div>
        <div class="ch-note">낮을수록 상위 &middot; 축 반전 표시</div>
        <div class="chart-wrap" id="rankChartWrap">
          <svg class="chart" id="rankChart"></svg>
          <div class="chart-tip" id="rankTip"></div>
        </div>
        <div class="table-scroll"><table class="data-table" id="rankTable"></table></div>
      </div>
      <div class="chart-card">
        <div class="ch-head"><h3>보유 포인트 추이</h3><button class="table-toggle" data-target="ptsChart">표로 보기</button></div>
        <div class="ch-note">대회별 획득 후 누적 포인트</div>
        <div class="chart-wrap" id="ptsChartWrap">
          <svg class="chart" id="ptsChart"></svg>
          <div class="chart-tip" id="ptsTip"></div>
        </div>
        <div class="table-scroll"><table class="data-table" id="ptsTable"></table></div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>상대 선수 전적 검색</h2>
      <span class="hint">경기에 기록된 상대 선수 이름으로 맞대결 전적을 찾아봐요</span>
    </div>
    <div class="h2h-box">
      <div class="search-box h2h-input-wrap">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="h2hInput" placeholder="상대 선수 이름 (예: 정이로, 강이안…)" autocomplete="off" />
      </div>
      <div class="h2h-suggest" id="h2hSuggest" hidden></div>
    </div>
    <div id="h2hResult"></div>
  </section>

  <section>
    <div class="section-head">
      <h2>대회 기록</h2>
      <span class="hint" id="listHint"></span>
      <button class="btn-primary" id="addTournamentBtn" hidden>+ 대회 추가</button>
    </div>
    <div class="readonly-note" id="readonlyNote" hidden>지금은 읽기 전용 보기예요. 우측 상단 &ldquo;🔒 관리자 로그인&rdquo;에서 PIN을 입력하면 직접 입력·수정할 수 있어요.</div>
    <div class="t-list" id="tList"></div>
  </section>
</main>

<footer>
  <div class="wrap">
    <p>DATA SOURCE &mdash; TENNIS RECORD 신이수.xlsx (시즌성적표 · 세부성적) + 직접 입력 · Firebase 실시간 동기화</p>
    <p id="genFoot">GENERATED 2026-08-23</p>
  </div>
</footer>

<div class="modal-overlay" id="modalOverlay" hidden>
  <div class="modal" id="modalBody" role="dialog" aria-modal="true"></div>
</div>

<script id="tennis-data" type="application/json">__DATA_JSON__</script>
<script>
(async function(){
  "use strict";
  var FALLBACK_DATA = JSON.parse(document.getElementById('tennis-data').textContent);
  var DATA = FALLBACK_DATA;
  var TODAY = new Date();

  // ---------- Firebase project config ----------
  // Firebase 콘솔 > 프로젝트 설정 > 일반 > 내 앱(웹 앱)에서 복사해 아래 값을 채워주세요.
  // 이 값들은 공개되어도 안전한 "클라이언트 식별자"입니다 (실제 접근 제어는 Firestore 보안 규칙 + PIN 로그인이 담당해요).
  var FIREBASE_CONFIG = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
  };
  var FIREBASE_READY = FIREBASE_CONFIG.apiKey && FIREBASE_CONFIG.apiKey.indexOf('YOUR_') !== 0;

  var ROUND_RANK = {'우승':0,'준우승':1,'4강':2,'8강':3,'16강':4,'32강':5,'64강':6,'128강':7,'256강':8,'예선':9,'본선':9};
  function roundRank(v){
    if(v==null) return 99;
    var s = String(v).replace(/\(.*?\)/g,'').trim();
    if(s==='-'||s==='') return 99;
    return (s in ROUND_RANK) ? ROUND_RANK[s] : 50;
  }
  function resultTier(rank){
    if(rank==null) return '';
    if(rank<=1) return 'tier-top';
    if(rank<=3) return 'tier-mid';
    return '';
  }
  function fmtRound(v){
    if(v==null) return '-';
    return String(v);
  }
  function pad2(n){ n = String(n); return n.length<2 ? '0'+n : n; }
  function parseDateStart(s){
    if(!s) return null;
    var m = /((?:20)?\d{2,4})-(\d{1,2})[.\-](\d{1,2})/.exec(String(s));
    if(!m) return null;
    var y = m[1].length===2 ? '20'+m[1] : m[1];
    return y+'-'+pad2(m[2])+'-'+pad2(m[3]);
  }
  function parseDateEnd(raw, startISO){
    if(!raw || !startISO) return startISO;
    var parts = String(raw).split('~');
    if(parts.length<2) return startISO;
    var endPart = parts[1];
    var full = /((?:20)?\d{2,4})-(\d{1,2})[.\-](\d{1,2})/.exec(endPart);
    if(full){
      var y = full[1].length===2 ? '20'+full[1] : full[1];
      return y+'-'+pad2(full[2])+'-'+pad2(full[3]);
    }
    var md = /(\d{1,2})[.\-](\d{1,2})/.exec(endPart);
    if(md){
      var startY = startISO.slice(0,4);
      var cand = startY+'-'+pad2(md[1])+'-'+pad2(md[2]);
      if(cand < startISO){ cand = (parseInt(startY,10)+1)+'-'+pad2(md[1])+'-'+pad2(md[2]); }
      return cand;
    }
    return startISO;
  }
  function parseRankNum(v){
    if(v==null) return null;
    var s = String(v).trim();
    if(s===''||s==='-') return null;
    var m = /^\d+/.exec(s);
    return m ? parseInt(m[0],10) : null;
  }
  function escAttr(s){
    if(s==null) return '';
    return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  function genId(prefix){ return prefix + '-' + Date.now().toString(36) + Math.random().toString(36).slice(2,6); }

  function normalizeIds(){
    ['2025','2026'].forEach(function(season){
      (DATA[season]||[]).forEach(function(t){
        if(!t.id) t.id = genId(season);
        if(t.matches){
          t.matches.forEach(function(m, idx){
            if(!m.id) m.id = t.id + '-m' + idx;
          });
        }
      });
    });
  }
  normalizeIds();

  function buildAll(){
    var out = [];
    ['2025','2026'].forEach(function(season){
      (DATA[season]||[]).forEach(function(t){
        var c = Object.assign({}, t, {season: season});
        out.push(c);
      });
    });
    out.sort(function(a,b){ return (a.dateStart||'') < (b.dateStart||'') ? -1 : 1; });
    return out;
  }
  var ALL = buildAll();

  function normalizeName(s){
    if(!s) return '';
    return String(s).replace(/\(.*?\)/g,'').replace(/\s+/g,'').trim().toLowerCase();
  }

  function buildOpponentIndex(){
    var map = {};
    ['2025','2026'].forEach(function(season){
      (DATA[season]||[]).forEach(function(t){
        if(!t.matches) return;
        t.matches.forEach(function(m){
          var slots = [
            { name: m.opp_player, team: m.opp_team, rank: m.opp_rank },
            { name: m.opp_player2, team: m.opp_team2 || m.opp_team, rank: m.opp_rank2 }
          ];
          slots.forEach(function(slot){
            if(!slot.name) return;
            var norm = normalizeName(slot.name);
            if(!norm) return;
            if(!map[norm]){ map[norm] = { displayNames: {}, matches: [] }; }
            map[norm].displayNames[slot.name] = true;
            map[norm].matches.push({
              tournamentName: t.name, season: season, dateStart: t.dateStart, dateRaw: t.dateRaw,
              round: m.round, result: m.result, sets: m.sets,
              isDoubles: !!(m.round && String(m.round).indexOf('복식')>=0),
              partner: m.partner, team: slot.team, rank: slot.rank
            });
          });
        });
      });
    });
    return map;
  }
  var OPP_INDEX = buildOpponentIndex();
  var h2hSelected = null;

  function findTournament(season, id){
    return (DATA[season]||[]).filter(function(x){ return x.id===id; })[0] || null;
  }

  var GRADES = ['1급','2급','3급','4급'];

  var state = { season:'all', grade:'all', query:'' };
  var openIds = {};

  // ---------- tabs ----------
  var seasonTabs = document.getElementById('seasonTabs');
  var TABS = [{key:'all', label:'통산'}, {key:'2026', label:'2026년'}, {key:'2025', label:'2025년'}];
  TABS.forEach(function(t){
    var b = document.createElement('button');
    b.className='tab'; b.textContent=t.label; b.setAttribute('role','tab');
    b.setAttribute('aria-pressed', state.season===t.key ? 'true':'false');
    b.addEventListener('click', function(){
      state.season = t.key;
      Array.prototype.forEach.call(seasonTabs.children, function(el,i){ el.setAttribute('aria-pressed', TABS[i].key===t.key ? 'true':'false'); });
      render();
    });
    seasonTabs.appendChild(b);
  });
  state.season = '2026';
  seasonTabs.children[1].setAttribute('aria-pressed','true');
  seasonTabs.children[0].setAttribute('aria-pressed','false');

  var gradeFilter = document.getElementById('gradeFilter');
  var gradeBtns = [];
  function addGradeBtn(key,label){
    var b = document.createElement('button');
    b.className='chip-btn'; b.textContent=label;
    b.setAttribute('aria-pressed', state.grade===key ? 'true':'false');
    b.addEventListener('click', function(){
      state.grade = key;
      gradeBtns.forEach(function(x){ x.el.setAttribute('aria-pressed', x.key===key ? 'true':'false'); });
      render();
    });
    gradeFilter.appendChild(b);
    gradeBtns.push({key:key, el:b});
  }
  addGradeBtn('all','전체 급수');
  GRADES.forEach(function(g){ addGradeBtn(g,g); });

  document.getElementById('searchInput').addEventListener('input', function(e){
    state.query = e.target.value.trim();
    render();
  });

  // ---------- helpers ----------
  function seasonGradeFiltered(){
    return ALL.filter(function(t){
      if(state.season!=='all' && t.season!==state.season) return false;
      if(state.grade!=='all' && t.grade!==state.grade) return false;
      return true;
    });
  }
  function fullyFiltered(){
    var list = seasonGradeFiltered();
    if(state.query){
      var q = state.query.toLowerCase();
      list = list.filter(function(t){
        return (t.name||'').toLowerCase().indexOf(q)>=0 || (t.location||'').toLowerCase().indexOf(q)>=0;
      });
    }
    return list;
  }

  function monthDay(iso){
    if(!iso) return {mo:'', dy:''};
    var d = new Date(iso+'T00:00:00');
    var months=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'];
    return { mo: months[d.getMonth()], dy: String(d.getDate()).padStart(2,'0') };
  }

  // ---------- stat cards ----------
  function computeStats(list){
    var participated = list.filter(function(t){return t.participated;});
    var matches = [], wins=0, losses=0;
    participated.forEach(function(t){
      if(t.matches){ t.matches.forEach(function(m){
        matches.push(m);
        if(m.result && m.result.indexOf('승')>=0) wins++;
        else if(m.result && m.result.indexOf('패')>=0) losses++;
      });}
    });
    var decided = wins+losses;
    var winRate = decided ? Math.round(wins/decided*1000)/10 : null;
    var pointsGained = participated.reduce(function(s,t){ return s + (typeof t.pointsGained==='number'? t.pointsGained:0); }, 0);
    var withPts = participated.filter(function(t){ return typeof t.pointsCurrent==='number' && t.dateStart; }).sort(function(a,b){ return a.dateStart<b.dateStart?-1:1; });
    var latestPoints = withPts.length ? withPts[withPts.length-1].pointsCurrent : null;
    var withRank = participated.filter(function(t){ return typeof t.rankingNum==='number' && t.dateStart; }).sort(function(a,b){ return a.dateStart<b.dateStart?-1:1; });
    var latestRanking = withRank.length ? withRank[withRank.length-1].rankingNum : null;
    var bestRanking = withRank.length ? Math.min.apply(null, withRank.map(function(t){return t.rankingNum;})) : null;
    var bestRow = participated.slice().sort(function(a,b){
      var ra = a.bestRoundRank==null?99:a.bestRoundRank, rb = b.bestRoundRank==null?99:b.bestRoundRank;
      return ra-rb;
    })[0];
    var bestLabel = null;
    if(bestRow && bestRow.bestRoundRank!=null && bestRow.bestRoundRank<99){
      bestLabel = (roundRank(bestRow.resultSingle) <= roundRank(bestRow.resultDouble)) ? bestRow.resultSingle : bestRow.resultDouble;
    }
    return {
      count: participated.length, totalEntries: list.length,
      matchCount: matches.length, wins:wins, losses:losses, winRate:winRate,
      pointsGained: pointsGained, latestPoints: latestPoints,
      latestRanking: latestRanking, bestRanking: bestRanking, bestLabel: bestLabel
    };
  }

  function renderStats(){
    var list = seasonGradeFiltered();
    var s = computeStats(list);
    var grid = document.getElementById('statGrid');
    grid.innerHTML = '';
    var cards = [
      {k:'참가 대회', v: s.count + '<small>회</small>', accent:false},
      {k:'총 경기 수', v: s.matchCount + '<small>경기</small>', accent:false},
      {k:'전적 (승-패)', v: s.wins + '<small>&ndash;</small>' + s.losses, d: s.winRate!=null ? ('승률 '+s.winRate+'%') : '기록 없음', accent:false},
      {k:'획득 포인트 합계', v: s.pointsGained + '<small>pt</small>', accent:false},
      {k:'최근 전국랭킹', v: s.latestRanking!=null ? (s.latestRanking+'<small>위</small>') : '&ndash;', d: s.bestRanking!=null ? ('시즌 최고 '+s.bestRanking+'위') : '', accent:true},
      {k:'최고 성적', v: s.bestLabel ? s.bestLabel : '&ndash;', d:'단식·복식 중 최고 라운드', accent:true},
    ];
    cards.forEach(function(c){
      var div = document.createElement('div');
      div.className = 'stat-card' + (c.accent ? ' accent':'');
      div.innerHTML = '<div class="k">'+c.k+'</div><div class="v">'+c.v+'</div>' + (c.d ? '<div class="d">'+c.d+'</div>' : '');
      grid.appendChild(div);
    });
    var hint = document.getElementById('statsHint');
    hint.textContent = (state.season==='all' ? '통산' : state.season+'년') + (state.grade!=='all' ? ' · '+state.grade : '');
  }

  // ---------- charts ----------
  function buildSeries(list, field){
    return list.filter(function(t){ return t.participated && typeof t[field]==='number' && t.dateStart; })
      .sort(function(a,b){ return a.dateStart<b.dateStart?-1:1; })
      .map(function(t){ return { x:t.dateStart, y:t[field], name:t.name, raw:t }; });
  }

  function drawChart(svgId, tipId, series, opts){
    var svg = document.getElementById(svgId);
    var tip = document.getElementById(tipId);
    var W = 520, H = 200, padL = 40, padR = 14, padT = 16, padB = 26;
    svg.setAttribute('viewBox','0 0 '+W+' '+H);
    svg.innerHTML = '';
    if(series.length < 2){
      var msg = document.createElementNS('http://www.w3.org/2000/svg','text');
      msg.setAttribute('x', W/2); msg.setAttribute('y', H/2);
      msg.setAttribute('text-anchor','middle'); msg.setAttribute('class','chart-axis-label');
      msg.textContent = '표시할 데이터가 부족합니다';
      svg.appendChild(msg);
      return;
    }
    var ys = series.map(function(d){return d.y;});
    var minY = Math.min.apply(null, ys), maxY = Math.max.apply(null, ys);
    if(minY===maxY){ minY -= 1; maxY += 1; }
    var pad = (maxY-minY)*0.12 || 1;
    minY -= pad; maxY += pad;
    var invert = !!opts.invertY;

    function xAt(i){ return padL + (i/(series.length-1)) * (W-padL-padR); }
    function yAt(v){
      var t = (v-minY)/(maxY-minY);
      if(invert) t = 1-t;
      return padT + (1-t) * (H-padT-padB);
    }

    var ns = 'http://www.w3.org/2000/svg';
    // gridlines
    [0,0.5,1].forEach(function(f){
      var gy = padT + f*(H-padT-padB);
      var line = document.createElementNS(ns,'line');
      line.setAttribute('x1',padL); line.setAttribute('x2',W-padR);
      line.setAttribute('y1',gy); line.setAttribute('y2',gy);
      line.setAttribute('class','chart-grid-line');
      svg.appendChild(line);
    });
    var lbl1 = document.createElementNS(ns,'text');
    lbl1.setAttribute('x',4); lbl1.setAttribute('y', yAt(invert?minY:maxY)+3.5);
    lbl1.setAttribute('class','chart-axis-label'); lbl1.textContent = Math.round(invert?minY:maxY);
    svg.appendChild(lbl1);
    var lbl2 = document.createElementNS(ns,'text');
    lbl2.setAttribute('x',4); lbl2.setAttribute('y', yAt(invert?maxY:minY)+3.5);
    lbl2.setAttribute('class','chart-axis-label'); lbl2.textContent = Math.round(invert?maxY:minY);
    svg.appendChild(lbl2);

    var pts = series.map(function(d,i){ return [xAt(i), yAt(d.y)]; });
    var dPath = pts.map(function(p,i){ return (i===0?'M':'L') + p[0].toFixed(1) + ' ' + p[1].toFixed(1); }).join(' ');

    if(opts.area){
      var baseY = yAt(invert ? maxY : minY);
      var areaPath = dPath + ' L' + pts[pts.length-1][0].toFixed(1) + ' ' + baseY.toFixed(1) + ' L' + pts[0][0].toFixed(1) + ' ' + baseY.toFixed(1) + ' Z';
      var area = document.createElementNS(ns,'path');
      area.setAttribute('d', areaPath); area.setAttribute('class','chart-area'); area.setAttribute('fill', 'var(--accent-strong)');
      svg.appendChild(area);
    }

    var path = document.createElementNS(ns,'path');
    path.setAttribute('d', dPath); path.setAttribute('class','chart-line');
    svg.appendChild(path);

    pts.forEach(function(p,i){
      var isEnd = i===pts.length-1;
      var c = document.createElementNS(ns,'circle');
      c.setAttribute('cx',p[0]); c.setAttribute('cy',p[1]);
      c.setAttribute('r', isEnd?4.5:3);
      c.setAttribute('class','chart-dot'+(isEnd?' end':''));
      svg.appendChild(c);
    });

    var guide = document.createElementNS(ns,'line');
    guide.setAttribute('y1',padT); guide.setAttribute('y2',H-padB);
    guide.setAttribute('class','chart-guide'); guide.setAttribute('id',svgId+'-guide');
    svg.appendChild(guide);
    var hoverDot = document.createElementNS(ns,'circle');
    hoverDot.setAttribute('r',5); hoverDot.setAttribute('class','chart-hover-dot');
    hoverDot.setAttribute('id',svgId+'-hoverdot');
    svg.appendChild(hoverDot);

    var hitRect = document.createElementNS(ns,'rect');
    hitRect.setAttribute('x',padL); hitRect.setAttribute('y',0);
    hitRect.setAttribute('width', W-padL-padR); hitRect.setAttribute('height', H);
    hitRect.setAttribute('fill','transparent');
    svg.appendChild(hitRect);

    function showTip(i, evt){
      var d = series[i];
      guide.setAttribute('x1', pts[i][0]); guide.setAttribute('x2', pts[i][0]); guide.style.opacity = 1;
      hoverDot.setAttribute('cx', pts[i][0]); hoverDot.setAttribute('cy', pts[i][1]); hoverDot.style.opacity = 1;
      var dt = new Date(d.x+'T00:00:00');
      var label = (dt.getMonth()+1)+'.'+String(dt.getDate()).padStart(2,'0');
      tip.innerHTML = '<b>'+label+'</b> &middot; ' + d.name.slice(0,16) + (d.name.length>16?'…':'') + '<br/>' + opts.tipLabel + ' <b>' + d.y + (opts.unit||'') + '</b>';
      var rect = svg.getBoundingClientRect();
      var wrapRect = svg.parentElement.getBoundingClientRect();
      var px = (pts[i][0]/W) * rect.width;
      var py = (pts[i][1]/H) * rect.height;
      tip.style.left = px + 'px';
      tip.style.top = py + 'px';
      tip.style.opacity = 1;
    }
    function hideTip(){
      guide.style.opacity = 0; hoverDot.style.opacity = 0; tip.style.opacity = 0;
    }
    hitRect.addEventListener('mousemove', function(evt){
      var rect = svg.getBoundingClientRect();
      var relX = (evt.clientX - rect.left) / rect.width * W;
      var idx = 0, best = Infinity;
      pts.forEach(function(p,i){ var dist = Math.abs(p[0]-relX); if(dist<best){best=dist; idx=i;} });
      showTip(idx, evt);
    });
    hitRect.addEventListener('mouseleave', hideTip);
    hitRect.addEventListener('touchstart', function(evt){
      var t = evt.touches[0];
      var rect = svg.getBoundingClientRect();
      var relX = (t.clientX - rect.left) / rect.width * W;
      var idx = 0, best = Infinity;
      pts.forEach(function(p,i){ var dist = Math.abs(p[0]-relX); if(dist<best){best=dist; idx=i;} });
      showTip(idx, evt);
    }, {passive:true});
  }

  function fillTable(tableId, series, label, unit){
    var t = document.getElementById(tableId);
    var rows = ['<thead><tr><th>날짜</th><th>대회명</th><th>'+label+'</th></tr></thead><tbody>'];
    series.forEach(function(d){
      rows.push('<tr><td>'+d.x+'</td><td>'+d.name+'</td><td class="num">'+d.y+(unit||'')+'</td></tr>');
    });
    rows.push('</tbody>');
    t.innerHTML = rows.join('');
  }

  function renderCharts(){
    var list = seasonGradeFiltered();
    var rankSeries = buildSeries(list, 'rankingNum');
    var ptsSeries = buildSeries(list, 'pointsCurrent');
    drawChart('rankChart','rankTip', rankSeries, {invertY:true, tipLabel:'랭킹', unit:'위'});
    drawChart('ptsChart','ptsTip', ptsSeries, {area:true, tipLabel:'포인트', unit:'pt'});
    fillTable('rankTable', rankSeries, '랭킹', '위');
    fillTable('ptsTable', ptsSeries, '포인트', 'pt');
  }

  document.querySelectorAll('.table-toggle').forEach(function(btn){
    btn.addEventListener('click', function(){
      var target = btn.getAttribute('data-target');
      var svg = document.getElementById(target);
      var table = document.getElementById(target.replace('Chart','Table'));
      var wrap = document.getElementById(target+'Wrap');
      var showingTable = table.classList.contains('show');
      if(showingTable){ table.classList.remove('show'); wrap.style.display=''; btn.textContent='표로 보기'; }
      else { table.classList.add('show'); wrap.style.display='none'; btn.textContent='차트로 보기'; }
    });
  });

  // ---------- timeline ----------
  function matchRow(m, t){
    var wl = 'na', wlLabel = '미기록';
    if(m.result && m.result.indexOf('승')>=0){ wl='win'; wlLabel='승'; }
    else if(m.result && m.result.indexOf('패')>=0){ wl='loss'; wlLabel='패'; }
    var setsHtml = (m.sets||[]).map(function(s){ return '<span class="set-box">'+ (s[0]==null?'-':s[0]) +':'+ (s[1]==null?'-':s[1]) +'</span>'; }).join('');
    var isDoubles = m.round && String(m.round).indexOf('복식')>=0;
    var oppNames = [m.opp_player, m.opp_player2].filter(Boolean).map(function(n){return escapeHtml(String(n));}).join(' · ');
    if(!oppNames) oppNames = '-';
    var oppTeam = m.opp_team || m.opp_team2;
    var oppTeamHtml = oppTeam ? '<span class="team"> · '+escapeHtml(String(oppTeam))+'</span>' : '';
    var oppRanks = [m.opp_rank, m.opp_rank2].filter(function(v){ return v!=null && v!==''; });
    var oppRankHtml = oppRanks.length ? ('상대랭킹 '+oppRanks.join(' / ')) : '';
    var partnerHtml = (isDoubles && m.partner) ? '<div class="partner-line">👥 파트너 '+escapeHtml(String(m.partner))+'</div>' : '';
    var notes = (m.notes||[]).filter(Boolean).map(function(n){ return '<span class="note-chip">📝 '+escapeHtml(n)+'</span>'; }).join('');
    var actionCell = writable ? ('<td class="match-actions"><button type="button" class="icon-btn" data-action="edit-match" data-season="'+t.season+'" data-tid="'+t.id+'" data-mid="'+m.id+'" title="경기 수정">✏️</button></td>') : '';
    return '<tr>'+
      '<td class="round-tag">'+fmtRound(m.round)+'</td>'+
      '<td class="opp">'+partnerHtml+oppNames+oppTeamHtml+ (oppRankHtml? '<div class="team">'+oppRankHtml+'</div>':'') + notes +'</td>'+
      '<td><div class="sets">'+(setsHtml||'<span class="team">기록 없음</span>')+'</div></td>'+
      '<td><span class="wl-badge '+wl+'">'+wlLabel+'</span></td>'+
      actionCell+
      '</tr>';
  }

  function escapeHtml(s){
    return s.replace(/[&<>"']/g, function(c){ return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]; });
  }

  function resultPills(t){
    var out = [];
    if(t.resultSingle && t.resultSingle!=='-'){
      var rr = roundRank(t.resultSingle);
      out.push('<span class="result-pill '+resultTier(rr)+'">단식 '+t.resultSingle+'</span>');
    }
    if(t.resultDouble && t.resultDouble!=='-'){
      var rr2 = roundRank(t.resultDouble);
      out.push('<span class="result-pill '+resultTier(rr2)+'">복식 '+t.resultDouble+'</span>');
    }
    if(!out.length){ out.push('<span class="result-pill">기록 없음</span>'); }
    return out.join('');
  }

  function renderList(){
    var list = fullyFiltered().slice().sort(function(a,b){ return (a.dateStart||'') > (b.dateStart||'') ? -1 : 1; });
    var wrap = document.getElementById('tList');
    document.getElementById('listHint').textContent = list.length + '개 대회';
    if(!list.length){
      wrap.innerHTML = '<div class="empty-note">조건에 맞는 대회 기록이 없습니다.</div>';
      return;
    }
    wrap.innerHTML = '';
    list.forEach(function(t){
      var card = document.createElement('div');
      card.className = 't-card' + (t.participated ? '' : ' dnp');
      var md = monthDay(t.dateStart);
      var hasDetail = t.matches && t.matches.length;
      var pointsHtml = (typeof t.pointsCurrent==='number') ? (t.pointsCurrent+'pt') : '&ndash;';
      var rankHtml = (t.rankingNum!=null) ? (t.rankingNum+'위') : '';
      var actionsHtml = writable ? ('<div class="t-actions"><button type="button" class="icon-btn" data-action="edit-tournament" data-season="'+t.season+'" data-id="'+t.id+'" title="대회 수정">✏️</button></div>') : '';
      var theadExtra = writable ? '<th></th>' : '';
      var addMatchHtml = writable ? ('<div style="margin-top:12px;"><button type="button" class="btn-ghost" data-action="add-match" data-season="'+t.season+'" data-id="'+t.id+'">+ 경기 결과 추가</button></div>') : '';
      card.innerHTML =
        '<div class="t-row">'+
          '<div class="t-date"><div class="mo">'+md.mo+'</div><div class="dy">'+md.dy+'</div></div>'+
          '<div class="t-main">'+
            '<div class="t-name">'+escapeHtml(t.name)+ (t.grade? '<span class="grade-pill">'+t.grade+'</span>':'') +'</div>'+
            '<div class="t-sub"><span>'+ (t.location||'-') +'</span><span>'+ t.season +'시즌</span>' + (t.participated? '' : '<span>불참</span>') + '</div>'+
          '</div>'+
          '<div class="t-results">'+resultPills(t)+'</div>'+
          '<div class="t-points"><div class="p">'+pointsHtml+'</div><div class="r">'+rankHtml+'</div></div>'+
          actionsHtml+
          '<svg class="t-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>'+
        '</div>'+
        '<div class="t-detail"><div class="t-detail-inner">'+
          (hasDetail ?
            '<div class="table-scroll"><table class="match-table"><thead><tr><th>라운드</th><th>상대</th><th>세트 스코어</th><th>결과</th>'+theadExtra+'</tr></thead><tbody>'+t.matches.map(function(m){ return matchRow(m, t); }).join('')+'</tbody></table></div>'
            : '<div class="no-detail">세부 경기 기록이 없습니다.</div>')
          + addMatchHtml
        +'</div></div>';

      var row = card.querySelector('.t-row');
      var detail = card.querySelector('.t-detail');
      row.addEventListener('click', function(e){
        if(e.target.closest('.t-actions, button, a')) return;
        var isOpen = card.classList.contains('open');
        if(isOpen){ card.classList.remove('open'); detail.style.maxHeight = 0; delete openIds[t.id]; }
        else { card.classList.add('open'); detail.style.maxHeight = detail.scrollHeight + 'px'; openIds[t.id] = true; }
      });
      if(openIds[t.id]){ card.classList.add('open'); }
      wrap.appendChild(card);
    });
    wrap.querySelectorAll('.t-card.open .t-detail').forEach(function(d){ d.style.maxHeight = d.scrollHeight + 'px'; });
  }

  document.getElementById('tList').addEventListener('click', function(e){
    var editT = e.target.closest('[data-action="edit-tournament"]');
    if(editT){
      e.stopPropagation();
      var t1 = findTournament(editT.getAttribute('data-season'), editT.getAttribute('data-id'));
      if(t1) openEditTournamentModal(t1);
      return;
    }
    var addM = e.target.closest('[data-action="add-match"]');
    if(addM){
      e.stopPropagation();
      var t2 = findTournament(addM.getAttribute('data-season'), addM.getAttribute('data-id'));
      if(t2) openAddMatchModal(t2);
      return;
    }
    var editM = e.target.closest('[data-action="edit-match"]');
    if(editM){
      e.stopPropagation();
      var t3 = findTournament(editM.getAttribute('data-season'), editM.getAttribute('data-tid'));
      var mid = editM.getAttribute('data-mid');
      var m3 = t3 && t3.matches ? t3.matches.filter(function(x){ return x.id===mid; })[0] : null;
      if(t3 && m3) openEditMatchModal(t3, m3);
      return;
    }
  });

  function renderNextBanner(){
    var todayISO = TODAY.toISOString().slice(0,10);
    var withDates = ALL.filter(function(t){ return t.dateStart; }).map(function(t){
      return Object.assign({}, t, { dateEnd: parseDateEnd(t.dateRaw, t.dateStart) });
    });
    var ongoing = withDates.filter(function(t){ return t.dateStart<=todayISO && t.dateEnd>=todayISO; })
      .sort(function(a,b){ return a.dateStart<b.dateStart?-1:1; })[0];
    var target = ongoing, isOngoing = !!ongoing;
    if(!target){
      target = withDates.filter(function(t){ return t.dateStart>todayISO; })
        .sort(function(a,b){ return a.dateStart<b.dateStart?-1:1; })[0];
    }
    var banner = document.getElementById('nextBanner');
    if(!target){ banner.hidden = true; return; }
    banner.hidden = false;
    var lbl = banner.querySelector('.lbl');
    if(lbl) lbl.textContent = isOngoing ? 'ONGOING · 진행중' : 'NEXT · 다음 대회';
    document.getElementById('nextName').textContent = target.name;
    document.getElementById('nextSub').textContent = (target.location||'') + ' · ' + target.dateRaw;
  }

  function render(){
    renderStats();
    renderCharts();
    renderList();
  }

  // ---------- head-to-head opponent search ----------
  function h2hMatchRow(entry){
    var wl = 'na', wlLabel = '미기록';
    if(entry.result && entry.result.indexOf('승')>=0){ wl='win'; wlLabel='승'; }
    else if(entry.result && entry.result.indexOf('패')>=0){ wl='loss'; wlLabel='패'; }
    var setsHtml = (entry.sets||[]).map(function(s){ return '<span class="set-box">'+ (s[0]==null?'-':s[0]) +':'+ (s[1]==null?'-':s[1]) +'</span>'; }).join('');
    var md = monthDay(entry.dateStart);
    var dateLabel = entry.dateStart ? (md.mo+' '+md.dy) : '-';
    var doublesLine = entry.isDoubles ? ('<div class="team">복식'+(entry.partner? ' · 파트너 '+escapeHtml(String(entry.partner)) : '')+'</div>') : '';
    var teamLine = entry.team ? ('<div class="team">'+escapeHtml(String(entry.team))+ (entry.rank!=null && entry.rank!=='' ? ' · 랭킹 '+escapeHtml(String(entry.rank)) : '')+'</div>') : '';
    return '<tr>'+
      '<td class="round-tag">'+dateLabel+'<div class="team">'+entry.season+'시즌</div></td>'+
      '<td class="opp">'+escapeHtml(entry.tournamentName)+'<div class="team">'+fmtRound(entry.round)+'</div>'+doublesLine+teamLine+'</td>'+
      '<td><div class="sets">'+(setsHtml||'<span class="team">기록 없음</span>')+'</div></td>'+
      '<td><span class="wl-badge '+wl+'">'+wlLabel+'</span></td>'+
      '</tr>';
  }

  function renderH2HDetail(norm){
    h2hSelected = norm;
    var wrap = document.getElementById('h2hResult');
    var entry = OPP_INDEX[norm];
    if(!entry || !entry.matches.length){
      wrap.innerHTML = '<div class="empty-note">해당 이름의 상대 전적을 찾을 수 없어요.</div>';
      return;
    }
    var matches = entry.matches.slice().sort(function(a,b){ return (a.dateStart||'') < (b.dateStart||'') ? 1 : -1; });
    var wins = matches.filter(function(m){ return m.result && m.result.indexOf('승')>=0; }).length;
    var losses = matches.filter(function(m){ return m.result && m.result.indexOf('패')>=0; }).length;
    var decided = wins+losses;
    var winRate = decided ? Math.round(wins/decided*1000)/10 : null;
    var names = Object.keys(entry.displayNames);
    var mainName = names[0];
    var altNames = names.slice(1);
    var altHtml = altNames.length ? ('<span class="alt">(기록상 표기: '+altNames.map(escapeHtml).join(', ')+')</span>') : '';
    wrap.innerHTML =
      '<div class="h2h-card">'+
        '<div class="h2h-head">'+
          '<div class="h2h-name">'+escapeHtml(mainName)+altHtml+'</div>'+
          '<div class="h2h-record">'+
            '<div class="h2h-stat"><div class="k">맞대결</div><div class="v">'+matches.length+'전</div></div>'+
            '<div class="h2h-stat"><div class="k">전적</div><div class="v"><span class="win">'+wins+'승</span> <span class="loss">'+losses+'패</span></div></div>'+
            (winRate!=null ? '<div class="h2h-stat"><div class="k">승률</div><div class="v">'+winRate+'%</div></div>' : '')+
          '</div>'+
        '</div>'+
        '<div class="table-scroll"><table class="match-table"><thead><tr><th>날짜</th><th>대회 · 라운드</th><th>세트 스코어</th><th>결과</th></tr></thead><tbody>'+
          matches.map(h2hMatchRow).join('')+
        '</tbody></table></div>'+
      '</div>';
  }

  function h2hSuggestions(query){
    var q = normalizeName(query);
    if(!q) return [];
    var out = [];
    Object.keys(OPP_INDEX).forEach(function(norm){
      if(norm.indexOf(q)>=0){
        var entry = OPP_INDEX[norm];
        out.push({ norm: norm, label: Object.keys(entry.displayNames)[0], count: entry.matches.length });
      }
    });
    out.sort(function(a,b){ return b.count - a.count; });
    return out.slice(0, 8);
  }

  function wireH2HSearch(){
    var input = document.getElementById('h2hInput');
    var suggestBox = document.getElementById('h2hSuggest');
    function showSuggestions(){
      var q = input.value.trim();
      if(!q){ suggestBox.hidden = true; suggestBox.innerHTML=''; return; }
      var matches = h2hSuggestions(q);
      if(!matches.length){
        suggestBox.innerHTML = '<div class="empty">일치하는 상대 선수 기록이 없어요.</div>';
        suggestBox.hidden = false;
        return;
      }
      suggestBox.innerHTML = matches.map(function(m){
        return '<button type="button" data-norm="'+escAttr(m.norm)+'">'+escapeHtml(m.label)+'<span class="cnt">'+m.count+'경기</span></button>';
      }).join('');
      suggestBox.hidden = false;
    }
    input.addEventListener('input', showSuggestions);
    input.addEventListener('focus', function(){ if(input.value.trim()) showSuggestions(); });
    suggestBox.addEventListener('click', function(e){
      var btn = e.target.closest('button[data-norm]');
      if(!btn) return;
      var norm = btn.getAttribute('data-norm');
      input.value = btn.childNodes[0].textContent;
      suggestBox.hidden = true;
      renderH2HDetail(norm);
    });
    input.addEventListener('keydown', function(e){
      if(e.key==='Enter'){
        e.preventDefault();
        var matches = h2hSuggestions(input.value);
        if(matches.length){ input.value = matches[0].label; suggestBox.hidden = true; renderH2HDetail(matches[0].norm); }
      }
    });
    document.addEventListener('click', function(e){
      if(!e.target.closest('.h2h-box')){ suggestBox.hidden = true; }
    });
  }

  // ---------- Firebase real-time sync + PIN auth ----------
  var fsApi = null, authApi = null, db = null, auth = null, docRef = null;
  var writable = false;
  var docExists = false;
  var seeding = false;
  var saving = false;
  var pendingSave = false;
  var lastSaveError = null;
  var modalOpen = false;
  var pendingRemote = null;

  function setSaveStatus(name, detail){
    var el = document.getElementById('saveStatus');
    var txt = document.getElementById('saveStatusText');
    var labels = {
      saving: '저장 중…', saved: '저장됨 · 실시간 반영돼요', error: '저장 실패 · 다시 시도해주세요',
      readonly: '읽기 전용 보기 · 로그인하면 편집 가능', offline: '연결 대기 중…'
    };
    el.hidden = false;
    el.setAttribute('data-state', name);
    txt.textContent = labels[name] || name;
    el.title = detail || '';
  }

  function updateAuthBtn(){
    var btn = document.getElementById('authBtn');
    btn.setAttribute('data-signed-in', writable ? 'true' : 'false');
    btn.textContent = writable ? '🔓 로그아웃' : '🔒 관리자 로그인';
  }

  function updateWritableUI(){
    var show = writable;
    document.getElementById('addTournamentBtn').hidden = !show;
    document.getElementById('readonlyNote').hidden = show;
    updateAuthBtn();
    if(!FIREBASE_READY){ setSaveStatus('offline', 'index.html 상단의 FIREBASE_CONFIG를 채워주세요 (README 참고).'); }
    else if(!writable){ setSaveStatus('readonly'); }
    else { setSaveStatus('saved'); }
    render();
  }

  function applyRemoteData(remote){
    DATA = remote;
    normalizeIds();
    ALL = buildAll();
    OPP_INDEX = buildOpponentIndex();
    render();
    renderNextBanner();
    if(h2hSelected){ renderH2HDetail(h2hSelected); }
  }

  async function ensureSeeded(){
    if(!FIREBASE_READY || docExists || !writable || seeding) return;
    seeding = true;
    setSaveStatus('saving', '초기 데이터를 Firebase에 업로드하는 중…');
    try {
      await fsApi.setDoc(docRef, DATA);
      docExists = true;
      setSaveStatus('saved');
    } catch(err){
      console.error('[tennis-record] initial seed failed:', err);
      setSaveStatus('error', (err && err.message) || '초기 업로드 실패');
    }
    seeding = false;
  }

  async function saveData(){
    if(!writable || !FIREBASE_READY){ return; }
    if(saving){ pendingSave = true; return; }
    saving = true;
    pendingSave = false;
    setSaveStatus('saving');
    try {
      await fsApi.setDoc(docRef, DATA);
      docExists = true;
      saving = false;
      setSaveStatus('saved');
    } catch(err){
      saving = false;
      lastSaveError = (err && err.message) || '알 수 없는 오류';
      console.error('[tennis-record] save failed:', err);
      setSaveStatus('error', lastSaveError);
    }
    if(pendingSave){ saveData(); }
  }

  function afterMutate(){
    ALL = buildAll();
    OPP_INDEX = buildOpponentIndex();
    render();
    renderNextBanner();
    if(h2hSelected){ renderH2HDetail(h2hSelected); }
    saveData();
  }

  async function initFirebase(){
    if(!FIREBASE_READY){ updateWritableUI(); return; }
    try {
      var appMod = await import('https://www.gstatic.com/firebasejs/10.14.1/firebase-app.js');
      fsApi = await import('https://www.gstatic.com/firebasejs/10.14.1/firebase-firestore.js');
      authApi = await import('https://www.gstatic.com/firebasejs/10.14.1/firebase-auth.js');
      var app = appMod.initializeApp(FIREBASE_CONFIG);
      db = fsApi.getFirestore(app);
      auth = authApi.getAuth(app);
      docRef = fsApi.doc(db, 'tennisRecord', 'main');

      authApi.onAuthStateChanged(auth, function(user){
        writable = !!user;
        updateWritableUI();
        if(writable){ ensureSeeded(); }
      });

      fsApi.onSnapshot(docRef, function(snap){
        if(snap.exists()){
          docExists = true;
          var remote = snap.data();
          if(modalOpen){ pendingRemote = remote; return; }
          applyRemoteData(remote);
        } else {
          docExists = false;
          if(writable){ ensureSeeded(); }
        }
      }, function(err){
        console.error('[tennis-record] snapshot listener error:', err);
        setSaveStatus('error', err && err.message);
      });
    } catch(err){
      console.error('[tennis-record] Firebase init failed:', err);
      setSaveStatus('error', 'Firebase 연결 실패 · FIREBASE_CONFIG와 네트워크를 확인해주세요.');
    }
  }

  function openLoginModal(){
    openModal('관리자 로그인', 'PIN을 입력하면 기록을 직접 입력·수정할 수 있어요.',
      '<div class="form-grid"><div class="field full"><label>PIN</label><input type="password" name="pin" inputmode="numeric" autocomplete="off" required autofocus /></div></div>',
      function(fd){
        var pin = (fd.get('pin')||'').trim();
        if(!pin) throw new Error('PIN을 입력해주세요.');
        return fetch('/api/login', {
          method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({pin: pin})
        }).then(function(res){
          return res.json().then(function(body){
            if(!res.ok || !body.token){ throw new Error(body.error || 'PIN이 올바르지 않아요.'); }
            return authApi.signInWithCustomToken(auth, body.token);
          });
        });
      }
    );
  }

  function wireAuthBtn(){
    document.getElementById('authBtn').addEventListener('click', function(){
      if(!FIREBASE_READY){ alert('아직 Firebase 연결이 설정되지 않았어요. README를 참고해 FIREBASE_CONFIG를 채워주세요.'); return; }
      if(writable){
        if(confirm('로그아웃할까요?')){ authApi.signOut(auth); }
      } else {
        openLoginModal();
      }
    });
  }

  // ---------- modal ----------
  function overlayClickClose(e){ if(e.target.id==='modalOverlay') closeModal(); }
  function closeModal(){
    var overlay = document.getElementById('modalOverlay');
    overlay.hidden = true;
    overlay.removeEventListener('click', overlayClickClose);
    modalOpen = false;
    if(pendingRemote){ var r = pendingRemote; pendingRemote = null; applyRemoteData(r); }
  }
  function openModal(titleHtml, subHtml, bodyHtml, onSubmit, opts){
    opts = opts || {};
    modalOpen = true;
    var overlay = document.getElementById('modalOverlay');
    var modal = document.getElementById('modalBody');
    modal.innerHTML =
      '<h3>'+titleHtml+'</h3>' + (subHtml ? '<p class="modal-sub">'+subHtml+'</p>' : '') +
      '<form id="modalForm" novalidate>' + bodyHtml +
        '<div class="modal-error" id="modalError"></div>' +
        '<div class="modal-actions">' +
          (opts.onDelete ? '<button type="button" class="btn-danger" id="modalDeleteBtn">삭제</button>' : '<span></span>') +
          '<div class="right"><button type="button" class="btn-ghost" id="modalCancelBtn">취소</button><button type="submit" class="btn-primary">저장</button></div>' +
        '</div>' +
      '</form>';
    overlay.hidden = false;
    overlay.addEventListener('click', overlayClickClose);
    document.getElementById('modalCancelBtn').addEventListener('click', closeModal);
    if(opts.onDelete){
      document.getElementById('modalDeleteBtn').addEventListener('click', function(){
        if(confirm('정말 삭제할까요? 되돌릴 수 없어요.')){ opts.onDelete(); closeModal(); }
      });
    }
    document.getElementById('modalForm').addEventListener('submit', function(e){
      e.preventDefault();
      var el = document.getElementById('modalError');
      el.classList.remove('show');
      var submitBtn = e.target.querySelector('button[type="submit"]');
      try {
        var result = onSubmit(new FormData(e.target), e.target);
        if(result && typeof result.then === 'function'){
          if(submitBtn) submitBtn.disabled = true;
          result.then(function(){ closeModal(); }).catch(function(err){
            if(submitBtn) submitBtn.disabled = false;
            el.textContent = (err && err.message) || '처리 중 오류가 발생했어요.';
            el.classList.add('show');
          });
        } else {
          closeModal();
        }
      } catch(err){
        el.textContent = (err && err.message) || '입력값을 확인해주세요.';
        el.classList.add('show');
      }
    });
    if(opts.afterRender) opts.afterRender(modal);
  }

  var ROUND_DATALIST = '<datalist id="roundList"><option value="우승"><option value="준우승"><option value="4강"><option value="8강"><option value="16강"><option value="32강"><option value="64강"><option value="예선"><option value="-"></datalist>';

  function tournamentFormHtml(t){
    t = t || {};
    var seasons = ['2026','2025'];
    var defaultSeason = t.season || (state.season!=='all' ? state.season : '2026');
    var seasonOpts = seasons.map(function(s){ return '<option value="'+s+'"'+(defaultSeason===s?' selected':'')+'>'+s+'년</option>'; }).join('');
    var grades = ['','1급','2급','3급','4급'];
    var gradeOpts = grades.map(function(g){ return '<option value="'+g+'"'+(t.grade===g?' selected':'')+'>'+(g||'급수 없음')+'</option>'; }).join('');
    return ''+
    '<div class="form-grid">'+
      '<div class="field"><label>시즌</label><select name="season">'+seasonOpts+'</select></div>'+
      '<div class="field"><label>급수</label><select name="grade">'+gradeOpts+'</select></div>'+
      '<div class="field full"><label>대회명</label><input type="text" name="name" required value="'+escAttr(t.name)+'" placeholder="예: 2026 순창 챌린저 주니어 대회" /></div>'+
      '<div class="field"><label>일정</label><input type="text" name="dateRaw" value="'+escAttr(t.dateRaw)+'" placeholder="2026-09-04(금)~09-08(화)" /></div>'+
      '<div class="field"><label>장소</label><input type="text" name="location" value="'+escAttr(t.location)+'" placeholder="예: 순창" /></div>'+
      '<div class="field"><label>단식 최종성적</label><input type="text" name="resultSingle" list="roundList" value="'+escAttr(t.resultSingle)+'" placeholder="예: 32강" /></div>'+
      '<div class="field"><label>복식 최종성적</label><input type="text" name="resultDouble" list="roundList" value="'+escAttr(t.resultDouble)+'" placeholder="예: 16강" /></div>'+
      '<div class="field"><label>획득 포인트</label><input type="number" step="0.5" name="pointsGained" value="'+(t.pointsGained!=null?t.pointsGained:'')+'" /></div>'+
      '<div class="field"><label>현재 누적 포인트</label><input type="number" step="0.5" name="pointsCurrent" value="'+(t.pointsCurrent!=null?t.pointsCurrent:'')+'" /></div>'+
      '<div class="field"><label>전국 랭킹</label><input type="text" name="rankingRaw" value="'+escAttr(t.rankingRaw)+'" placeholder="예: 105 또는 105(3.04기준)" /></div>'+
      '<div class="field check"><input type="checkbox" id="fParticipated" name="participated" '+(t.participated!==false?'checked':'')+' /><label for="fParticipated">참가함</label></div>'+
    '</div>'+
    ROUND_DATALIST;
  }

  function buildTournamentFromForm(fd, season, existing){
    var name = (fd.get('name')||'').trim();
    var grade = (fd.get('grade')||'').trim() || null;
    var dateRaw = (fd.get('dateRaw')||'').trim() || null;
    var location = (fd.get('location')||'').trim() || null;
    var resultSingle = (fd.get('resultSingle')||'').trim() || null;
    var resultDouble = (fd.get('resultDouble')||'').trim() || null;
    var pgRaw = fd.get('pointsGained'); var pointsGained = pgRaw==='' || pgRaw==null ? null : Number(pgRaw);
    var pcRaw = fd.get('pointsCurrent'); var pointsCurrent = pcRaw==='' || pcRaw==null ? null : Number(pcRaw);
    var rankingRaw = (fd.get('rankingRaw')||'').trim() || null;
    var participated = fd.get('participated') === 'on';
    var rr1 = roundRank(resultSingle), rr2 = roundRank(resultDouble);
    var bestRoundRank = Math.min(rr1,rr2); if(bestRoundRank>=99) bestRoundRank=null;
    return Object.assign({}, existing||{}, {
      id: (existing && existing.id) || genId(season),
      seq: (existing && existing.seq) || null,
      name: name, grade: grade,
      dateRaw: dateRaw, dateStart: parseDateStart(dateRaw),
      location: location, participated: participated,
      resultSingle: resultSingle, resultDouble: resultDouble,
      pointsGained: (pointsGained==null || isNaN(pointsGained)) ? null : pointsGained,
      pointsCurrent: (pointsCurrent==null || isNaN(pointsCurrent)) ? null : pointsCurrent,
      rankingRaw: rankingRaw, rankingNum: parseRankNum(rankingRaw),
      bestRoundRank: bestRoundRank,
      matches: (existing && existing.matches) || null
    });
  }

  function openAddTournamentModal(){
    openModal('대회 추가', '새 대회 기록을 추가해요.', tournamentFormHtml({}), function(fd){
      var season = fd.get('season');
      var name = (fd.get('name')||'').trim();
      if(!name) throw new Error('대회명을 입력해주세요.');
      var t = buildTournamentFromForm(fd, season, null);
      DATA[season] = DATA[season] || [];
      DATA[season].push(t);
      afterMutate();
    });
  }

  function openEditTournamentModal(t){
    openModal('대회 수정', escapeHtml(t.name), tournamentFormHtml(t), function(fd){
      var newSeason = fd.get('season');
      var name = (fd.get('name')||'').trim();
      if(!name) throw new Error('대회명을 입력해주세요.');
      var updated = buildTournamentFromForm(fd, newSeason, t);
      DATA[t.season] = (DATA[t.season]||[]).filter(function(x){ return x.id!==t.id; });
      DATA[newSeason] = DATA[newSeason] || [];
      DATA[newSeason].push(updated);
      afterMutate();
    }, { onDelete: function(){
        DATA[t.season] = (DATA[t.season]||[]).filter(function(x){ return x.id!==t.id; });
        afterMutate();
      }
    });
  }

  function matchFormHtml(m){
    m = m || {};
    var isDoubles = m.round && String(m.round).indexOf('복식')>=0;
    var setsArr = (m.sets && m.sets.length) ? m.sets : [[null,null]];
    var setsHtml = setsArr.map(function(s,i){
      return '<div class="set-row" data-set-row>'+
        '<input type="number" step="1" data-set-my value="'+(s[0]==null?'':s[0])+'" placeholder="이수" />'+
        '<span>:</span>'+
        '<input type="number" step="1" data-set-opp value="'+(s[1]==null?'':s[1])+'" placeholder="상대" />'+
        (i>0 ? '<button type="button" class="icon-btn danger" data-remove-set title="세트 삭제">&times;</button>' : '')+
      '</div>';
    }).join('');
    return ''+
    '<div class="form-grid">'+
      '<div class="field"><label>라운드</label><input type="text" name="round" list="roundList2" value="'+escAttr(m.round)+'" placeholder="예: 32강" /></div>'+
      '<div class="field"><label>결과</label><select name="result"><option value="">미기록</option><option value="승"'+(m.result==='승'?' selected':'')+'>승</option><option value="패"'+(m.result==='패'?' selected':'')+'>패</option></select></div>'+
      '<div class="field"><label>상대 소속</label><input type="text" name="opp_team" value="'+escAttr(m.opp_team)+'" /></div>'+
      '<div class="field"><label>상대 선수명</label><input type="text" name="opp_player" value="'+escAttr(m.opp_player)+'" /></div>'+
      '<div class="field"><label>상대 랭킹</label><input type="text" name="opp_rank" value="'+escAttr(m.opp_rank)+'" /></div>'+
      '<div class="field check"><input type="checkbox" id="fDoubles" name="isDoubles" '+(isDoubles?'checked':'')+' /><label for="fDoubles">복식 경기예요</label></div>'+
      '<fieldset class="doubles-fields'+(isDoubles?' show':'')+'" id="doublesFields">'+
        '<legend>복식 상대 · 파트너</legend>'+
        '<div class="field"><label>파트너 (이수와 같은 편)</label><input type="text" name="partner" value="'+escAttr(m.partner)+'" /></div>'+
        '<div class="field"><label>상대2 팀</label><input type="text" name="opp_team2" value="'+escAttr(m.opp_team2)+'" /></div>'+
        '<div class="field"><label>상대2 선수명</label><input type="text" name="opp_player2" value="'+escAttr(m.opp_player2)+'" /></div>'+
        '<div class="field"><label>상대2 랭킹</label><input type="text" name="opp_rank2" value="'+escAttr(m.opp_rank2)+'" /></div>'+
      '</fieldset>'+
      '<div class="field full"><label>세트 스코어</label><div id="setsWrap">'+setsHtml+'</div><button type="button" class="btn-ghost" id="addSetBtn">+ 세트 추가</button></div>'+
      '<div class="field full"><label>메모</label><textarea name="notes">'+escapeHtml((m.notes||[]).join('\n'))+'</textarea></div>'+
    '</div>'+
    '<datalist id="roundList2"><option value="예선"><option value="64강"><option value="32강"><option value="16강"><option value="8강"><option value="4강"><option value="준우승"><option value="우승"></datalist>';
  }

  function wireMatchForm(modal){
    var doublesCb = modal.querySelector('[name="isDoubles"]');
    var fieldset = modal.querySelector('#doublesFields');
    doublesCb.addEventListener('change', function(){ fieldset.classList.toggle('show', doublesCb.checked); });
    var setsWrap = modal.querySelector('#setsWrap');
    function wireRemove(btn){
      btn.addEventListener('click', function(){ btn.closest('.set-row').remove(); });
    }
    setsWrap.querySelectorAll('[data-remove-set]').forEach(wireRemove);
    modal.querySelector('#addSetBtn').addEventListener('click', function(){
      var div = document.createElement('div');
      div.className = 'set-row'; div.setAttribute('data-set-row','');
      div.innerHTML = '<input type="number" step="1" data-set-my placeholder="이수" /><span>:</span><input type="number" step="1" data-set-opp placeholder="상대" /><button type="button" class="icon-btn danger" data-remove-set title="세트 삭제">&times;</button>';
      setsWrap.appendChild(div);
      wireRemove(div.querySelector('[data-remove-set]'));
    });
  }

  function parseSetsFromForm(formEl){
    var rows = formEl.querySelectorAll('[data-set-row]');
    var sets = [];
    rows.forEach(function(row){
      var my = row.querySelector('[data-set-my]').value.trim();
      var opp = row.querySelector('[data-set-opp]').value.trim();
      if(my!=='' || opp!==''){ sets.push([my===''?null:Number(my), opp===''?null:Number(opp)]); }
    });
    return sets;
  }

  function buildMatchFromForm(fd, formEl, existing){
    var isDoubles = fd.get('isDoubles') === 'on';
    var round = (fd.get('round')||'').trim() || null;
    if(isDoubles && round && round.indexOf('복식')<0){ round = round + '(복식)'; }
    var notesRaw = (fd.get('notes')||'').trim();
    var notes = notesRaw ? notesRaw.split('\n').map(function(s){ return s.trim(); }).filter(Boolean) : [];
    var oppRankRaw = (fd.get('opp_rank')||'').trim();
    return Object.assign({}, existing||{}, {
      id: (existing && existing.id) || genId('m'),
      round: round,
      opp_team: (fd.get('opp_team')||'').trim() || null,
      opp_player: (fd.get('opp_player')||'').trim() || null,
      opp_rank: oppRankRaw===''? null : oppRankRaw,
      result: fd.get('result') || null,
      sets: parseSetsFromForm(formEl),
      partner: isDoubles ? ((fd.get('partner')||'').trim() || null) : null,
      opp_player2: isDoubles ? ((fd.get('opp_player2')||'').trim() || null) : null,
      opp_team2: isDoubles ? ((fd.get('opp_team2')||'').trim() || null) : null,
      opp_rank2: isDoubles ? ((fd.get('opp_rank2')||'').trim() || null) : null,
      notes: notes
    });
  }

  function openAddMatchModal(t){
    openModal('경기 결과 추가', escapeHtml(t.name), matchFormHtml({}), function(fd, formEl){
      var m = buildMatchFromForm(fd, formEl, null);
      t.matches = t.matches || [];
      t.matches.push(m);
      afterMutate();
    }, { afterRender: wireMatchForm });
  }

  function openEditMatchModal(t, m){
    openModal('경기 결과 수정', escapeHtml(t.name), matchFormHtml(m), function(fd, formEl){
      var updated = buildMatchFromForm(fd, formEl, m);
      var idx = t.matches.indexOf(m);
      if(idx>=0) t.matches[idx] = updated;
      afterMutate();
    }, { afterRender: wireMatchForm, onDelete: function(){
        var idx = t.matches.indexOf(m);
        if(idx>=0) t.matches.splice(idx,1);
        afterMutate();
      }
    });
  }

  document.getElementById('addTournamentBtn').addEventListener('click', openAddTournamentModal);
  wireH2HSearch();
  wireAuthBtn();

  document.getElementById('genDate').textContent = DATA.generatedDate;
  document.getElementById('genFoot').textContent = 'GENERATED ' + DATA.generatedDate;
  updateWritableUI();
  renderNextBanner();
  render();
  window.addEventListener('resize', renderCharts);
  await initFirebase();
})();
</script>
"""

html = html.replace("__DATA_JSON__", DATA_JSON)
with open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print("written", len(html), "bytes")
