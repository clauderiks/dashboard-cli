<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>ClaudeRiks — Developer Hub</title>
<style>
/* ============================================================
   ClaudeRiks — Dark Theme (GitHub + VS Code inspired)
   Single-file application. No external dependencies.
   ============================================================ */

:root{
  --bg:#0d1117;
  --bg-elevated:#0d1117;
  --sidebar:#161b22;
  --panel:#161b22;
  --border:#30363d;
  --primary:#58a6ff;
  --primary-dim:#1f6feb;
  --text:#f0f6fc;
  --text-secondary:#8b949e;
  --success:#3fb950;
  --danger:#f85149;
  --warning:#d29922;
  --purple:#bc8cff;
  --radius-sm:4px;
  --radius-md:8px;
  --radius-lg:12px;
  --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  --topbar-h:52px;
  --sidebar-w:64px;
  --statusbar-h:28px;
  --transition-fast:120ms cubic-bezier(.4,0,.2,1);
  --transition-med:220ms cubic-bezier(.4,0,.2,1);
}

*,*::before,*::after{ box-sizing:border-box; }
html,body{
  height:100%;
  margin:0;
  padding:0;
}
body{
  background:var(--bg);
  color:var(--text);
  font-family:var(--font-ui);
  font-size:14px;
  line-height:1.5;
  -webkit-font-smoothing:antialiased;
  overflow:hidden;
}
::selection{ background:rgba(88,166,255,.3); color:var(--text); }

/* Scrollbars */
::-webkit-scrollbar{ width:10px; height:10px; }
::-webkit-scrollbar-track{ background:transparent; }
::-webkit-scrollbar-thumb{ background:#30363d; border-radius:6px; border:2px solid transparent; background-clip:padding-box; }
::-webkit-scrollbar-thumb:hover{ background:#484f58; background-clip:padding-box; }

button{ font-family:inherit; }
a{ color:var(--primary); text-decoration:none; }
a:hover{ text-decoration:underline; }
code, pre{ font-family:var(--font-mono); }

@keyframes fadeIn{ from{opacity:0; transform:translateY(6px);} to{opacity:1; transform:translateY(0);} }
@keyframes fadeInFast{ from{opacity:0;} to{opacity:1;} }
@keyframes pulse{ 0%,100%{opacity:1;} 50%{opacity:.45;} }
@keyframes spin{ from{transform:rotate(0deg);} to{transform:rotate(360deg);} }
@keyframes slideInRight{ from{opacity:0; transform:translateX(16px);} to{opacity:1; transform:translateX(0);} }
@keyframes blink{ 0%,49%{opacity:1;} 50%,100%{opacity:0;} }
@keyframes shimmer{ 0%{background-position:-200px 0;} 100%{background-position:200px 0;} }
@keyframes popIn{ from{opacity:0; transform:scale(.94);} to{opacity:1; transform:scale(1);} }
@keyframes typingDot{ 0%,60%,100%{transform:translateY(0); opacity:.5;} 30%{transform:translateY(-4px); opacity:1;} }
@keyframes toastIn{ from{opacity:0; transform:translateX(100%);} to{opacity:1; transform:translateX(0);} }
@keyframes glowPulse{ 0%,100%{box-shadow:0 0 0 0 rgba(88,166,255,.4);} 50%{box-shadow:0 0 0 6px rgba(88,166,255,0);} }

/* ============================================================
   APP SHELL
   ============================================================ */
.app{ height:100vh; display:flex; flex-direction:column; }

/* ---------- TOP BAR ---------- */
.topbar{
  height:var(--topbar-h);
  min-height:var(--topbar-h);
  background:var(--sidebar);
  border-bottom:1px solid var(--border);
  display:flex;
  align-items:center;
  padding:0 14px;
  gap:16px;
  z-index:50;
}
.topbar .logo{
  display:flex; align-items:center; gap:8px;
  font-weight:700; font-size:15px; letter-spacing:.2px;
  color:var(--text); cursor:pointer; user-select:none;
  white-space:nowrap;
}
.logo-mark{
  width:26px; height:26px; border-radius:7px;
  background:linear-gradient(135deg, var(--primary), var(--purple));
  display:flex; align-items:center; justify-content:center;
  font-size:14px; font-weight:800; color:#0d1117;
  box-shadow:0 0 0 1px rgba(240,246,252,.08);
}
.logo-sub{ color:var(--text-secondary); font-weight:400; font-size:12px; }

.topbar-search{
  flex:1; max-width:520px; position:relative;
}
.topbar-search input{
  width:100%; background:var(--bg); border:1px solid var(--border);
  color:var(--text); border-radius:var(--radius-md); padding:7px 12px 7px 34px;
  font-size:13px; outline:none; transition:border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.topbar-search input:focus{ border-color:var(--primary); box-shadow:0 0 0 3px rgba(88,166,255,.15); }
.topbar-search svg{ position:absolute; left:10px; top:50%; transform:translateY(-50%); color:var(--text-secondary); pointer-events:none; }
.topbar-search .kbd-hint{
  position:absolute; right:8px; top:50%; transform:translateY(-50%);
  font-size:11px; color:var(--text-secondary); border:1px solid var(--border);
  border-radius:4px; padding:1px 6px; background:var(--sidebar); pointer-events:none;
}

.topbar-actions{ display:flex; align-items:center; gap:6px; margin-left:auto; }
.icon-btn{
  width:34px; height:34px; border-radius:var(--radius-md);
  display:flex; align-items:center; justify-content:center;
  background:transparent; border:1px solid transparent; color:var(--text-secondary);
  cursor:pointer; transition:background var(--transition-fast), color var(--transition-fast), border-color var(--transition-fast);
  position:relative;
}
.icon-btn:hover{ background:rgba(240,246,252,.08); color:var(--text); }
.icon-btn.active{ color:var(--primary); background:rgba(88,166,255,.12); }
.icon-btn .dot{
  position:absolute; top:6px; right:6px; width:7px; height:7px; border-radius:50%;
  background:var(--danger); border:2px solid var(--sidebar);
}
.user-chip{
  width:34px; height:34px; border-radius:50%;
  background:linear-gradient(135deg,#f778ba,#a371f7);
  display:flex; align-items:center; justify-content:center;
  font-size:12px; font-weight:700; color:#0d1117; cursor:pointer;
  border:2px solid transparent; transition:border-color var(--transition-fast);
}
.user-chip:hover{ border-color:var(--primary); }

/* ---------- MAIN BODY LAYOUT ---------- */
.body-wrap{ flex:1; display:flex; min-height:0; }

/* ---------- LEFT SIDEBAR (icon rail) ---------- */
.sidebar{
  width:var(--sidebar-w);
  min-width:var(--sidebar-w);
  background:var(--sidebar);
  border-right:1px solid var(--border);
  display:flex; flex-direction:column;
  align-items:center;
  padding:10px 0;
  gap:2px;
  overflow-y:auto;
  overflow-x:hidden;
}
.nav-item{
  width:44px; height:44px; border-radius:var(--radius-md);
  display:flex; align-items:center; justify-content:center;
  color:var(--text-secondary); cursor:pointer; position:relative;
  transition:background var(--transition-fast), color var(--transition-fast);
  flex-shrink:0;
}
.nav-item svg{ width:20px; height:20px; }
.nav-item:hover{ background:rgba(240,246,252,.08); color:var(--text); }
.nav-item.active{ color:var(--primary); background:rgba(88,166,255,.12); }
.nav-item.active::before{
  content:""; position:absolute; left:-10px; top:50%; transform:translateY(-50%);
  width:3px; height:20px; background:var(--primary); border-radius:0 3px 3px 0;
}
.nav-item .tooltip{
  position:absolute; left:56px; top:50%; transform:translateY(-50%) translateX(-4px);
  background:#1c2128; border:1px solid var(--border); color:var(--text);
  padding:5px 10px; border-radius:var(--radius-sm); font-size:12px; white-space:nowrap;
  opacity:0; pointer-events:none; transition:opacity var(--transition-fast), transform var(--transition-fast);
  z-index:100; box-shadow:0 4px 14px rgba(0,0,0,.4);
}
.nav-item:hover .tooltip{ opacity:1; transform:translateY(-50%) translateX(0); }
.sidebar-spacer{ flex:1; }
.sidebar-divider{ width:28px; height:1px; background:var(--border); margin:6px 0; flex-shrink:0; }

/* ---------- MAIN CONTENT ---------- */
.content{
  flex:1; min-width:0; display:flex; flex-direction:column; overflow:hidden;
  position:relative;
}
.view{
  display:none;
  flex:1; min-height:0; overflow-y:auto; overflow-x:hidden;
  animation:fadeIn var(--transition-med) ease;
}
.view.active{ display:flex; flex-direction:column; }
.view-inner{ padding:24px 28px 60px; max-width:1400px; width:100%; margin:0 auto; }

/* section headers reused everywhere */
.section-title{ display:flex; align-items:center; gap:10px; font-size:20px; font-weight:650; margin:0 0 4px; }
.section-sub{ color:var(--text-secondary); font-size:13px; margin:0 0 20px; }
.section-block{ margin-bottom:32px; }
.section-block h3{ font-size:14px; text-transform:uppercase; letter-spacing:.6px; color:var(--text-secondary); font-weight:650; margin:0 0 12px; display:flex; align-items:center; gap:8px; }

/* ============================================================
   DASHBOARD VIEW
   ============================================================ */
.hero{
  border:1px solid var(--border); border-radius:var(--radius-lg);
  background:linear-gradient(135deg, rgba(88,166,255,.08), rgba(163,113,247,.06));
  padding:32px; margin-bottom:28px; position:relative; overflow:hidden;
  animation:fadeIn .4s ease;
}
.hero::after{
  content:""; position:absolute; right:-60px; top:-60px; width:220px; height:220px;
  border-radius:50%; background:radial-gradient(circle, rgba(88,166,255,.18), transparent 70%);
}
.hero-badge{
  display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600;
  color:var(--primary); background:rgba(88,166,255,.12); border:1px solid rgba(88,166,255,.3);
  padding:4px 10px; border-radius:999px; margin-bottom:14px;
}
.hero h1{ font-size:28px; margin:0 0 10px; font-weight:700; letter-spacing:-.3px; }
.hero p{ color:var(--text-secondary); max-width:560px; margin:0 0 20px; font-size:14px; }
.hero-actions{ display:flex; gap:10px; flex-wrap:wrap; }

.btn{
  border:1px solid var(--border); background:var(--sidebar); color:var(--text);
  padding:8px 16px; border-radius:var(--radius-md); font-size:13px; font-weight:600;
  cursor:pointer; display:inline-flex; align-items:center; gap:8px;
  transition:background var(--transition-fast), border-color var(--transition-fast), transform var(--transition-fast);
}
.btn:hover{ background:#1c2128; border-color:#484f58; }
.btn:active{ transform:scale(.97); }
.btn-primary{ background:var(--primary-dim); border-color:var(--primary-dim); color:#fff; }
.btn-primary:hover{ background:#388bfd; border-color:#388bfd; }
.btn-success{ background:var(--success); border-color:var(--success); color:#0d1117; }
.btn-danger{ background:transparent; border-color:var(--danger); color:var(--danger); }
.btn-danger:hover{ background:rgba(248,81,73,.1); }
.btn-sm{ padding:5px 10px; font-size:12px; }
.btn:disabled{ opacity:.5; cursor:not-allowed; }

.grid-cards{ display:grid; grid-template-columns:repeat(auto-fit, minmax(230px,1fr)); gap:16px; margin-bottom:28px; }
.card{
  background:var(--panel); border:1px solid var(--border); border-radius:var(--radius-lg);
  padding:18px; transition:border-color var(--transition-fast), transform var(--transition-fast), box-shadow var(--transition-fast);
  animation:fadeIn .4s ease;
}
.card:hover{ border-color:#484f58; transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,0,0,.25); }
.card-top{ display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; }
.card-icon{
  width:36px; height:36px; border-radius:var(--radius-md); display:flex; align-items:center; justify-content:center;
}
.card-icon.blue{ background:rgba(88,166,255,.12); color:var(--primary); }
.card-icon.green{ background:rgba(63,185,80,.12); color:var(--success); }
.card-icon.purple{ background:rgba(163,113,247,.12); color:var(--purple); }
.card-icon.orange{ background:rgba(210,153,34,.12); color:var(--warning); }
.card-trend{ font-size:12px; font-weight:600; display:flex; align-items:center; gap:3px; }
.card-trend.up{ color:var(--success); }
.card-trend.down{ color:var(--danger); }
.card .value{ font-size:26px; font-weight:700; margin:0 0 2px; }
.card .label{ color:var(--text-secondary); font-size:12.5px; }

.stats-row{ display:grid; grid-template-columns:repeat(auto-fit, minmax(160px,1fr)); gap:14px; margin-bottom:28px; }
.stat-box{ border:1px solid var(--border); border-radius:var(--radius-md); padding:14px; background:var(--panel); }
.stat-box .num{ font-size:20px; font-weight:700; color:var(--primary); }
.stat-box .lbl{ font-size:12px; color:var(--text-secondary); margin-top:2px; }
.bar-track{ height:6px; background:#21262d; border-radius:3px; margin-top:10px; overflow:hidden; }
.bar-fill{ height:100%; border-radius:3px; background:linear-gradient(90deg, var(--primary), var(--purple)); transition:width 1s ease; }

.two-col{ display:grid; grid-template-columns:1.4fr 1fr; gap:20px; }
@media (max-width: 900px){ .two-col{ grid-template-columns:1fr; } }

.panel{ border:1px solid var(--border); border-radius:var(--radius-lg); background:var(--panel); overflow:hidden; }
.panel-header{ padding:14px 18px; border-bottom:1px solid var(--border); display:flex; align-items:center; justify-content:space-between; }
.panel-header h4{ margin:0; font-size:14px; font-weight:650; }
.panel-body{ padding:6px 0; }

.activity-item{ display:flex; gap:12px; padding:12px 18px; border-bottom:1px solid rgba(48,54,61,.5); }
.activity-item:last-child{ border-bottom:none; }
.activity-dot{ width:8px; height:8px; border-radius:50%; margin-top:6px; flex-shrink:0; }
.activity-dot.commit{ background:var(--primary); }
.activity-dot.merge{ background:var(--purple); }
.activity-dot.issue{ background:var(--warning); }
.activity-dot.release{ background:var(--success); }
.activity-text{ font-size:13px; }
.activity-text b{ font-weight:600; }
.activity-time{ font-size:11.5px; color:var(--text-secondary); margin-top:2px; }

.file-row{ display:flex; align-items:center; gap:10px; padding:10px 18px; border-bottom:1px solid rgba(48,54,61,.5); cursor:pointer; transition:background var(--transition-fast); }
.file-row:hover{ background:rgba(240,246,252,.04); }
.file-row:last-child{ border-bottom:none; }
.file-row .fname{ font-size:13px; flex:1; }
.file-row .fmeta{ font-size:11.5px; color:var(--text-secondary); }

.doc-tile{ display:flex; gap:12px; align-items:flex-start; padding:14px; border:1px solid var(--border); border-radius:var(--radius-md); cursor:pointer; transition:border-color var(--transition-fast), background var(--transition-fast); }
.doc-tile:hover{ border-color:var(--primary); background:rgba(88,166,255,.05); }
.doc-tile .di{ width:32px; height:32px; border-radius:var(--radius-sm); background:rgba(88,166,255,.12); color:var(--primary); display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.doc-tile .dt{ font-size:13px; font-weight:600; margin:0 0 4px; }
.doc-tile .dd{ font-size:12px; color:var(--text-secondary); margin:0; }
.doc-grid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:12px; }

/* Badges & tags */
.badge{ display:inline-flex; align-items:center; gap:4px; font-size:11px; font-weight:600; padding:2px 8px; border-radius:999px; }
.badge.blue{ background:rgba(88,166,255,.12); color:var(--primary); }
.badge.green{ background:rgba(63,185,80,.12); color:var(--success); }
.badge.red{ background:rgba(248,81,73,.12); color:var(--danger); }
.badge.orange{ background:rgba(210,153,34,.12); color:var(--warning); }
.badge.gray{ background:rgba(139,148,158,.12); color:var(--text-secondary); }

/* ============================================================
   DOCUMENTATION VIEW
   ============================================================ */
.docs-layout{ display:flex; flex:1; min-height:0; }
.docs-sidebar{
  width:250px; min-width:250px; border-right:1px solid var(--border);
  padding:18px 8px; overflow-y:auto;
}
.docs-search{ margin:0 10px 14px; }
.docs-search input{
  width:100%; background:var(--bg); border:1px solid var(--border); color:var(--text);
  padding:6px 10px; border-radius:var(--radius-sm); font-size:12.5px; outline:none;
}
.docs-search input:focus{ border-color:var(--primary); }
.docs-group{ margin-bottom:6px; }
.docs-group-title{
  display:flex; align-items:center; gap:6px; padding:7px 12px; font-size:11.5px; font-weight:700;
  text-transform:uppercase; letter-spacing:.5px; color:var(--text-secondary); cursor:pointer; user-select:none;
}
.docs-group-title svg{ transition:transform var(--transition-fast); width:12px; height:12px; }
.docs-group.collapsed .docs-group-title svg{ transform:rotate(-90deg); }
.docs-group.collapsed .docs-links{ display:none; }
.docs-links a{
  display:block; padding:6px 12px 6px 26px; font-size:13px; color:var(--text-secondary);
  border-radius:var(--radius-sm); margin:1px 8px; text-decoration:none;
  transition:background var(--transition-fast), color var(--transition-fast);
}
.docs-links a:hover{ background:rgba(240,246,252,.06); color:var(--text); }
.docs-links a.active{ background:rgba(88,166,255,.12); color:var(--primary); font-weight:600; }

.docs-main{ flex:1; overflow-y:auto; padding:28px 40px; }
.docs-content{ max-width:820px; }
.docs-content h1{ font-size:26px; margin:0 0 6px; }
.docs-content .docs-meta{ color:var(--text-secondary); font-size:12.5px; margin-bottom:22px; padding-bottom:18px; border-bottom:1px solid var(--border); }
.docs-content h2{ font-size:19px; margin:32px 0 12px; padding-bottom:6px; border-bottom:1px solid var(--border); }
.docs-content h3{ font-size:15.5px; margin:22px 0 10px; }
.docs-content p{ color:#c9d1d9; margin:0 0 14px; font-size:14px; }
.docs-content ul, .docs-content ol{ color:#c9d1d9; font-size:14px; padding-left:22px; margin:0 0 14px; }
.docs-content li{ margin-bottom:5px; }
.docs-content code.inline{ background:rgba(110,118,129,.2); padding:1px 6px; border-radius:4px; font-size:12.5px; }
.docs-content table{ width:100%; border-collapse:collapse; margin:0 0 20px; font-size:13px; }
.docs-content th{ text-align:left; background:var(--panel); padding:8px 12px; border:1px solid var(--border); font-weight:650; }
.docs-content td{ padding:8px 12px; border:1px solid var(--border); color:#c9d1d9; }
.docs-content tr:nth-child(even) td{ background:rgba(255,255,255,.015); }

/* code block */
.code-block{ position:relative; background:#010409; border:1px solid var(--border); border-radius:var(--radius-md); margin:0 0 18px; overflow:hidden; }
.code-block-head{ display:flex; align-items:center; justify-content:space-between; padding:8px 14px; background:#161b22; border-bottom:1px solid var(--border); }
.code-block-head .lang{ font-size:11.5px; color:var(--text-secondary); font-weight:600; text-transform:uppercase; letter-spacing:.4px; }
.code-block-actions{ display:flex; gap:6px; }
.copy-btn{
  display:flex; align-items:center; gap:5px; background:transparent; border:1px solid var(--border); color:var(--text-secondary);
  padding:4px 8px; border-radius:var(--radius-sm); font-size:11.5px; cursor:pointer; transition:all var(--transition-fast);
}
.copy-btn:hover{ color:var(--text); border-color:#484f58; background:rgba(255,255,255,.04); }
.copy-btn.copied{ color:var(--success); border-color:var(--success); }
.code-block pre{ margin:0; padding:14px 16px; overflow-x:auto; font-size:12.8px; line-height:1.65; }
.code-line{ display:flex; }
.code-line .ln{ color:#484f58; width:32px; text-align:right; padding-right:16px; user-select:none; flex-shrink:0; }
.code-line .lc{ white-space:pre; }
.tok-kw{ color:#ff7b72; }
.tok-str{ color:#a5d6ff; }
.tok-com{ color:#8b949e; font-style:italic; }
.tok-fn{ color:#d2a8ff; }
.tok-num{ color:#79c0ff; }
.tok-prop{ color:#79c0ff; }
.tok-tag{ color:#7ee787; }
.tok-punc{ color:#c9d1d9; }

/* callouts (Wiki) */
.callout{ display:flex; gap:12px; padding:14px 16px; border-radius:var(--radius-md); border:1px solid; margin:0 0 18px; }
.callout svg{ flex-shrink:0; margin-top:1px; }
.callout-title{ font-weight:700; font-size:13px; margin:0 0 4px; }
.callout-body{ font-size:13.5px; color:#c9d1d9; }
.callout.note{ background:rgba(88,166,255,.08); border-color:rgba(88,166,255,.35); }
.callout.note .callout-title, .callout.note svg{ color:var(--primary); }
.callout.warning{ background:rgba(210,153,34,.08); border-color:rgba(210,153,34,.35); }
.callout.warning .callout-title, .callout.warning svg{ color:var(--warning); }
.callout.tip{ background:rgba(63,185,80,.08); border-color:rgba(63,185,80,.35); }
.callout.tip .callout-title, .callout.tip svg{ color:var(--success); }
.callout.danger{ background:rgba(248,81,73,.08); border-color:rgba(248,81,73,.35); }
.callout.danger .callout-title, .callout.danger svg{ color:var(--danger); }

/* ============================================================
   WIKI VIEW
   ============================================================ */
.wiki-layout{ display:flex; flex:1; min-height:0; }
.wiki-main{ flex:1; overflow-y:auto; padding:28px 40px; }
.wiki-toc{ width:230px; min-width:230px; border-left:1px solid var(--border); padding:24px 18px; overflow-y:auto; }
.wiki-toc h4{ font-size:11.5px; text-transform:uppercase; letter-spacing:.5px; color:var(--text-secondary); margin:0 0 12px; }
.wiki-toc ul{ list-style:none; margin:0; padding:0; }
.wiki-toc li{ margin-bottom:2px; }
.wiki-toc a{
  display:block; padding:5px 10px; font-size:12.5px; color:var(--text-secondary); border-left:2px solid transparent;
  border-radius:0 4px 4px 0; transition:all var(--transition-fast); text-decoration:none;
}
.wiki-toc a:hover{ color:var(--text); background:rgba(255,255,255,.04); }
.wiki-toc a.active{ color:var(--primary); border-left-color:var(--primary); background:rgba(88,166,255,.08); }
.wiki-toc .lvl2{ padding-left:22px; font-size:12px; }

.mermaid-box{
  border:1px solid var(--border); border-radius:var(--radius-md); background:#010409; padding:24px;
  display:flex; align-items:center; justify-content:center; margin:0 0 18px; overflow-x:auto;
}
.flow-node{
  border:1.5px solid var(--primary); color:var(--primary); background:rgba(88,166,255,.08);
  padding:8px 16px; border-radius:var(--radius-sm); font-size:12.5px; font-weight:600; white-space:nowrap;
}
.flow-arrow{ color:var(--text-secondary); font-size:18px; margin:0 6px; }
.flow-row{ display:flex; align-items:center; }
.flow-branch{ display:flex; flex-direction:column; gap:10px; align-items:center; }

/* ============================================================
   FILE EXPLORER + CODE VIEWER
   ============================================================ */
.explorer-layout{ display:flex; flex:1; min-height:0; }
.explorer-tree{ width:270px; min-width:270px; border-right:1px solid var(--border); overflow-y:auto; padding:10px 0; }
.explorer-tree-head{ display:flex; align-items:center; justify-content:space-between; padding:4px 14px 10px; font-size:11.5px; font-weight:700; text-transform:uppercase; letter-spacing:.5px; color:var(--text-secondary); }
.tree-node{ user-select:none; }
.tree-row{
  display:flex; align-items:center; gap:6px; padding:4px 10px 4px 0; font-size:13px; cursor:pointer;
  border-radius:var(--radius-sm); white-space:nowrap; color:#c9d1d9; transition:background var(--transition-fast);
}
.tree-row:hover{ background:rgba(255,255,255,.05); }
.tree-row.selected{ background:rgba(88,166,255,.14); color:var(--text); }
.tree-row .chevron{ width:16px; height:16px; flex-shrink:0; transition:transform var(--transition-fast); color:var(--text-secondary); }
.tree-row.folder.open > .chevron{ transform:rotate(90deg); }
.tree-row .ficon{ width:16px; height:16px; flex-shrink:0; }
.tree-children{ display:none; }
.tree-children.open{ display:block; }

.viewer-panel{ flex:1; display:flex; flex-direction:column; min-width:0; }
.viewer-tabs{ display:flex; border-bottom:1px solid var(--border); overflow-x:auto; background:var(--sidebar); }
.viewer-tab{
  display:flex; align-items:center; gap:8px; padding:9px 16px; font-size:12.5px; color:var(--text-secondary);
  border-right:1px solid var(--border); cursor:pointer; white-space:nowrap; position:relative;
}
.viewer-tab.active{ background:var(--bg); color:var(--text); }
.viewer-tab.active::after{ content:""; position:absolute; left:0; right:0; top:-1px; height:2px; background:var(--primary); }
.viewer-tab .close-x{ opacity:0; width:14px; height:14px; display:flex; align-items:center; justify-content:center; border-radius:3px; }
.viewer-tab:hover .close-x{ opacity:1; }
.viewer-tab .close-x:hover{ background:rgba(255,255,255,.12); }

.viewer-toolbar{ display:flex; align-items:center; justify-content:space-between; padding:8px 16px; border-bottom:1px solid var(--border); }
.viewer-toolbar .path{ font-size:12px; color:var(--text-secondary); display:flex; align-items:center; gap:6px; }
.viewer-toolbar .path b{ color:var(--text); font-weight:600; }
.viewer-toolbar-actions{ display:flex; gap:6px; }

.code-viewer-scroll{ flex:1; overflow:auto; background:#010409; }
.code-viewer-scroll pre{ margin:0; padding:16px 0; font-size:13px; line-height:1.65; }
.code-viewer-scroll .code-line{ padding:0 20px; }
.code-viewer-scroll .code-line:hover{ background:rgba(255,255,255,.03); }
.code-viewer-scroll .code-line.highlight{ background:rgba(88,166,255,.08); border-left:2px solid var(--primary); }

.fullscreen-mode{ position:fixed; inset:0; z-index:1000; background:var(--bg); display:flex; flex-direction:column; }

/* ============================================================
   TERMINAL VIEW
   ============================================================ */
.terminal-wrap{ flex:1; display:flex; flex-direction:column; padding:20px 24px; min-height:0; }
.terminal-window{
  flex:1; display:flex; flex-direction:column; background:#0a0e14; border:1px solid var(--border);
  border-radius:var(--radius-md); overflow:hidden; box-shadow:0 20px 50px rgba(0,0,0,.35); min-height:0;
}
.terminal-titlebar{ display:flex; align-items:center; gap:8px; padding:10px 14px; background:#161b22; border-bottom:1px solid var(--border); }
.tl-dot{ width:11px; height:11px; border-radius:50%; }
.tl-dot.red{ background:#ff5f56; }
.tl-dot.yellow{ background:#ffbd2e; }
.tl-dot.green{ background:#27c93f; }
.terminal-titlebar .ttitle{ margin:0 auto; font-size:12px; color:var(--text-secondary); font-weight:600; }
.terminal-body{ flex:1; overflow-y:auto; padding:14px 18px; font-family:var(--font-mono); font-size:13px; line-height:1.7; }
.term-line{ white-space:pre-wrap; word-break:break-word; margin-bottom:2px; }
.term-prompt{ color:var(--success); font-weight:700; }
.term-path{ color:var(--primary); font-weight:600; }
.term-cmd{ color:var(--text); }
.term-out{ color:#c9d1d9; }
.term-err{ color:var(--danger); }
.term-info{ color:var(--text-secondary); }
.term-input-row{ display:flex; align-items:center; gap:8px; }
.term-input-row input{
  flex:1; background:transparent; border:none; outline:none; color:var(--text);
  font-family:var(--font-mono); font-size:13px;
}
.term-cursor{ display:inline-block; width:7px; height:15px; background:var(--text); animation:blink 1s step-end infinite; vertical-align:middle; margin-left:2px; }
.term-help-table{ margin:6px 0; }
.term-help-row{ display:flex; gap:16px; }
.term-help-row .cmd{ width:110px; color:var(--primary); flex-shrink:0; }

/* ============================================================
   AI ASSISTANT VIEW
   ============================================================ */
.ai-layout{ display:flex; flex:1; min-height:0; }
.ai-history{ width:260px; min-width:260px; border-right:1px solid var(--border); padding:16px 10px; overflow-y:auto; }
.ai-history .new-chat-btn{ width:100%; margin-bottom:14px; justify-content:center; }
.ai-history-item{
  padding:9px 12px; border-radius:var(--radius-md); font-size:12.5px; color:var(--text-secondary);
  cursor:pointer; margin-bottom:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  transition:background var(--transition-fast);
}
.ai-history-item:hover{ background:rgba(255,255,255,.05); color:var(--text); }
.ai-history-item.active{ background:rgba(88,166,255,.12); color:var(--primary); font-weight:600; }
.ai-history-date{ font-size:11px; color:#484f58; text-transform:uppercase; font-weight:700; letter-spacing:.5px; padding:10px 12px 6px; }

.ai-main{ flex:1; display:flex; flex-direction:column; min-width:0; }
.ai-messages{ flex:1; overflow-y:auto; padding:24px 0; }
.ai-msg-row{ display:flex; gap:14px; padding:14px 40px; animation:fadeIn .35s ease; }
.ai-msg-row.user{ background:transparent; }
.ai-msg-row.assistant{ background:rgba(255,255,255,.015); }
.ai-avatar{ width:30px; height:30px; border-radius:7px; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:700; }
.ai-avatar.user{ background:linear-gradient(135deg,#f778ba,#a371f7); color:#0d1117; }
.ai-avatar.assistant{ background:linear-gradient(135deg, var(--primary), var(--purple)); color:#0d1117; }
.ai-msg-content{ flex:1; min-width:0; padding-top:4px; }
.ai-msg-name{ font-size:12.5px; font-weight:700; margin-bottom:4px; }
.ai-msg-text{ font-size:14px; color:#c9d1d9; line-height:1.6; }
.ai-msg-text p{ margin:0 0 10px; }
.ai-msg-text p:last-child{ margin-bottom:0; }
.typing-dots{ display:flex; gap:4px; padding:4px 0; }
.typing-dots span{ width:6px; height:6px; border-radius:50%; background:var(--text-secondary); animation:typingDot 1.2s ease-in-out infinite; }
.typing-dots span:nth-child(2){ animation-delay:.15s; }
.typing-dots span:nth-child(3){ animation-delay:.3s; }

.ai-suggestions{ padding:8px 40px 4px; display:flex; flex-wrap:wrap; gap:8px; }
.suggestion-chip{
  border:1px solid var(--border); background:var(--panel); color:var(--text-secondary);
  padding:7px 13px; border-radius:999px; font-size:12.5px; cursor:pointer;
  transition:all var(--transition-fast);
}
.suggestion-chip:hover{ border-color:var(--primary); color:var(--primary); background:rgba(88,166,255,.08); }

.ai-input-bar{ padding:14px 40px 20px; border-top:1px solid var(--border); }
.ai-input-box{
  display:flex; align-items:flex-end; gap:8px; background:var(--panel); border:1px solid var(--border);
  border-radius:var(--radius-lg); padding:10px 10px 10px 16px; transition:border-color var(--transition-fast);
}
.ai-input-box:focus-within{ border-color:var(--primary); box-shadow:0 0 0 3px rgba(88,166,255,.12); }
.ai-input-box textarea{
  flex:1; background:transparent; border:none; outline:none; resize:none; color:var(--text);
  font-family:inherit; font-size:14px; max-height:140px; line-height:1.5; padding:6px 0;
}
.ai-send-btn{
  width:34px; height:34px; border-radius:var(--radius-md); background:var(--primary-dim); border:none;
  display:flex; align-items:center; justify-content:center; color:#fff; cursor:pointer; flex-shrink:0;
  transition:background var(--transition-fast), transform var(--transition-fast);
}
.ai-send-btn:hover{ background:#388bfd; }
.ai-send-btn:active{ transform:scale(.92); }
.ai-input-hint{ text-align:center; font-size:11px; color:#484f58; margin-top:8px; }

/* ============================================================
   SEARCH VIEW
   ============================================================ */
.search-hero{ padding:40px 28px 20px; text-align:center; }
.search-big-box{ max-width:640px; margin:0 auto 18px; position:relative; }
.search-big-box input{
  width:100%; padding:14px 18px 14px 46px; font-size:15px; background:var(--panel); border:1px solid var(--border);
  border-radius:var(--radius-lg); color:var(--text); outline:none; transition:border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.search-big-box input:focus{ border-color:var(--primary); box-shadow:0 0 0 4px rgba(88,166,255,.14); }
.search-big-box svg{ position:absolute; left:16px; top:50%; transform:translateY(-50%); color:var(--text-secondary); }
.search-filters{ display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-bottom:8px; }
.filter-chip{
  border:1px solid var(--border); background:transparent; color:var(--text-secondary); padding:6px 14px;
  border-radius:999px; font-size:12.5px; cursor:pointer; transition:all var(--transition-fast); display:flex; align-items:center; gap:6px;
}
.filter-chip.active{ background:rgba(88,166,255,.14); border-color:var(--primary); color:var(--primary); }
.filter-chip:hover{ border-color:#484f58; }

.search-results{ max-width:760px; margin:0 auto; padding:10px 28px 40px; }
.search-result-item{
  padding:16px; border:1px solid var(--border); border-radius:var(--radius-md); margin-bottom:10px; cursor:pointer;
  transition:border-color var(--transition-fast), background var(--transition-fast); animation:fadeIn .3s ease;
}
.search-result-item:hover{ border-color:var(--primary); background:rgba(88,166,255,.04); }
.sr-top{ display:flex; align-items:center; gap:8px; margin-bottom:6px; }
.sr-title{ font-size:14px; font-weight:650; color:var(--primary); }
.sr-path{ font-size:11.5px; color:var(--text-secondary); font-family:var(--font-mono); }
.sr-snippet{ font-size:13px; color:#c9d1d9; }
.sr-snippet mark{ background:rgba(210,153,34,.35); color:#fff; border-radius:2px; padding:0 2px; }
.search-empty{ text-align:center; padding:60px 20px; color:var(--text-secondary); }

/* ============================================================
   GIT VIEW
   ============================================================ */
.git-layout{ padding:24px 28px; }
.git-toolbar{ display:flex; align-items:center; gap:10px; margin-bottom:20px; flex-wrap:wrap; }
.branch-select{
  display:flex; align-items:center; gap:8px; border:1px solid var(--border); background:var(--panel);
  padding:7px 14px; border-radius:var(--radius-md); font-size:13px; cursor:pointer; color:var(--text);
}
.git-grid{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }
@media (max-width:900px){ .git-grid{ grid-template-columns:1fr; } }
.commit-item{ display:flex; gap:12px; padding:12px 16px; border-bottom:1px solid rgba(48,54,61,.5); }
.commit-item:last-child{ border-bottom:none; }
.commit-avatar{ width:28px; height:28px; border-radius:50%; background:linear-gradient(135deg,var(--primary),var(--purple)); flex-shrink:0; }
.commit-msg{ font-size:13px; font-weight:600; margin-bottom:3px; }
.commit-meta{ font-size:11.5px; color:var(--text-secondary); }
.commit-hash{ font-family:var(--font-mono); color:var(--primary); background:rgba(88,166,255,.1); padding:1px 6px; border-radius:4px; font-size:11px; }

.branch-item{ display:flex; align-items:center; justify-content:space-between; padding:11px 16px; border-bottom:1px solid rgba(48,54,61,.5); font-size:13px; }
.branch-item:last-child{ border-bottom:none; }
.branch-name{ display:flex; align-items:center; gap:8px; }
.branch-name svg{ color:var(--text-secondary); }

.git-actions-panel{ display:flex; flex-wrap:wrap; gap:10px; }

/* stage/diff area */
.diff-add{ background:rgba(63,185,80,.12); color:#7ee787; }
.diff-remove{ background:rgba(248,81,73,.12); color:#ffa198; }
.diff-line{ display:flex; font-family:var(--font-mono); font-size:12.5px; padding:1px 10px; }
.diff-line .sign{ width:16px; flex-shrink:0; opacity:.7; }

/* ============================================================
   SETTINGS VIEW
   ============================================================ */
.settings-layout{ display:flex; flex:1; min-height:0; }
.settings-nav{ width:220px; min-width:220px; border-right:1px solid var(--border); padding:20px 10px; }
.settings-nav-item{ padding:9px 14px; border-radius:var(--radius-md); font-size:13px; color:var(--text-secondary); cursor:pointer; margin-bottom:2px; transition:all var(--transition-fast); }
.settings-nav-item:hover{ background:rgba(255,255,255,.05); color:var(--text); }
.settings-nav-item.active{ background:rgba(88,166,255,.12); color:var(--primary); font-weight:600; }
.settings-main{ flex:1; overflow-y:auto; padding:28px 40px; }
.settings-panel{ display:none; max-width:640px; }
.settings-panel.active{ display:block; animation:fadeIn .3s ease; }
.setting-row{ display:flex; align-items:center; justify-content:space-between; padding:16px 0; border-bottom:1px solid var(--border); gap:20px; }
.setting-row:last-child{ border-bottom:none; }
.setting-label{ font-size:13.5px; font-weight:600; }
.setting-desc{ font-size:12px; color:var(--text-secondary); margin-top:3px; }
.setting-control select, .setting-control input[type="text"]{
  background:var(--bg); border:1px solid var(--border); color:var(--text); padding:7px 12px;
  border-radius:var(--radius-sm); font-size:13px; outline:none; min-width:180px;
}
.setting-control select:focus, .setting-control input:focus{ border-color:var(--primary); }

/* toggle switch */
.switch{ position:relative; width:40px; height:22px; flex-shrink:0; }
.switch input{ opacity:0; width:0; height:0; }
.slider{ position:absolute; cursor:pointer; inset:0; background:#30363d; border-radius:22px; transition:background var(--transition-fast); }
.slider::before{ content:""; position:absolute; height:16px; width:16px; left:3px; top:3px; background:#f0f6fc; border-radius:50%; transition:transform var(--transition-fast); }
.switch input:checked + .slider{ background:var(--primary-dim); }
.switch input:checked + .slider::before{ transform:translateX(18px); }

/* radio color swatches for theme */
.theme-swatches{ display:flex; gap:12px; }
.theme-swatch{ width:60px; height:40px; border-radius:var(--radius-sm); border:2px solid var(--border); cursor:pointer; position:relative; transition:border-color var(--transition-fast); }
.theme-swatch.selected{ border-color:var(--primary); }
.theme-swatch.selected::after{ content:"✓"; position:absolute; top:2px; right:4px; font-size:11px; color:var(--primary); font-weight:900; }

.slider-range{ width:180px; }

/* ============================================================
   FOOTER / STATUS BAR
   ============================================================ */
.statusbar{
  height:var(--statusbar-h); min-height:var(--statusbar-h); background:var(--primary-dim);
  display:flex; align-items:center; padding:0 14px; font-size:11.5px; color:#fff; gap:16px;
}
.statusbar-item{ display:flex; align-items:center; gap:5px; }
.statusbar-spacer{ flex:1; }

/* ============================================================
   MODALS / TOASTS / MISC
   ============================================================ */
.toast-container{ position:fixed; bottom:44px; right:20px; display:flex; flex-direction:column; gap:8px; z-index:2000; }
.toast{
  display:flex; align-items:center; gap:10px; background:#161b22; border:1px solid var(--border);
  padding:12px 16px; border-radius:var(--radius-md); font-size:13px; box-shadow:0 8px 24px rgba(0,0,0,.4);
  animation:toastIn .3s ease; min-width:240px;
}
.toast.success{ border-left:3px solid var(--success); }
.toast.error{ border-left:3px solid var(--danger); }
.toast.info{ border-left:3px solid var(--primary); }

.cmdk-overlay{
  position:fixed; inset:0; background:rgba(1,4,9,.7); display:none; align-items:flex-start; justify-content:center;
  padding-top:100px; z-index:3000; backdrop-filter:blur(2px);
}
.cmdk-overlay.open{ display:flex; animation:fadeInFast .15s ease; }
.cmdk-box{
  width:100%; max-width:560px; background:var(--panel); border:1px solid var(--border); border-radius:var(--radius-lg);
  box-shadow:0 20px 60px rgba(0,0,0,.5); overflow:hidden; animation:popIn .18s ease;
}
.cmdk-input-wrap{ display:flex; align-items:center; gap:10px; padding:14px 16px; border-bottom:1px solid var(--border); }
.cmdk-input-wrap svg{ color:var(--text-secondary); flex-shrink:0; }
.cmdk-input-wrap input{ flex:1; background:transparent; border:none; outline:none; color:var(--text); font-size:15px; }
.cmdk-list{ max-height:340px; overflow-y:auto; padding:6px; }
.cmdk-item{ display:flex; align-items:center; gap:10px; padding:9px 12px; border-radius:var(--radius-sm); font-size:13.5px; cursor:pointer; color:#c9d1d9; }
.cmdk-item:hover, .cmdk-item.hl{ background:rgba(88,166,255,.12); color:var(--text); }
.cmdk-item svg{ color:var(--text-secondary); flex-shrink:0; }
.cmdk-item .cmdk-kbd{ margin-left:auto; font-size:11px; color:var(--text-secondary); border:1px solid var(--border); border-radius:4px; padding:1px 6px; }

/* skeleton loader */
.skel{ background:linear-gradient(90deg,#21262d 25%,#30363d 37%,#21262d 63%); background-size:400% 100%; animation:shimmer 1.4s ease infinite; border-radius:4px; }

/* utility */
.flex{ display:flex; }
.gap-8{ gap:8px; }
.mt-0{ margin-top:0; }
.text-secondary{ color:var(--text-secondary); }
.hidden{ display:none !important; }
.mono{ font-family:var(--font-mono); }

/* mobile responsiveness */
@media (max-width: 860px){
  :root{ --sidebar-w:56px; }
  .topbar-search{ display:none; }
  .docs-sidebar, .wiki-toc, .explorer-tree, .ai-history{ display:none; }
  .git-grid{ grid-template-columns:1fr; }
  .view-inner{ padding:16px; }
  .settings-nav{ width:150px; min-width:150px; }
  .ai-msg-row{ padding:14px 18px; }
  .ai-input-bar{ padding:12px 18px 16px; }
  .ai-suggestions{ padding:8px 18px 4px; }
  .docs-main, .wiki-main{ padding:20px; }
}
@media (max-width: 560px){
  .grid-cards{ grid-template-columns:1fr 1fr; }
  .logo-sub{ display:none; }
  .hero h1{ font-size:22px; }
  .two-col{ gap:14px; }
}
</style>
</head>
<body>

<div class="app">

  <!-- ============================================================
       TOP BAR
  ============================================================= -->
  <header class="topbar">
    <div class="logo" onclick="switchView('dashboard')">
      <div class="logo-mark">CR</div>
      <span>ClaudeRiks <span class="logo-sub">Developer Hub</span></span>
    </div>

    <div class="topbar-search">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M11.5 11.5L15 15M13 7a6 6 0 11-12 0 6 6 0 0112 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <input id="global-search-input" type="text" placeholder="Tìm kiếm tài liệu, file, API..." onclick="openCommandPalette()" readonly>
      <span class="kbd-hint">Ctrl K</span>
    </div>

    <div class="topbar-actions">
      <button class="icon-btn" title="Thông báo" onclick="toggleNotifications(this)">
        <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M8 1.5a3.5 3.5 0 00-3.5 3.5v1.6c0 .53-.21 1.04-.59 1.41L2.5 9.4c-.5.5-.15 1.35.55 1.35h9.9c.7 0 1.05-.85.55-1.35l-1.41-1.4a2 2 0 01-.59-1.41V5A3.5 3.5 0 008 1.5zM6.2 13a1.8 1.8 0 003.6 0" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="dot"></span>
      </button>
      <button class="icon-btn" title="GitHub" onclick="showToast('info','Mở liên kết GitHub repository')">
        <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8a8 8 0 005.47 7.59c.4.07.55-.17.55-.38v-1.49c-2.23.48-2.7-1.07-2.7-1.07-.36-.93-.89-1.18-.89-1.18-.72-.5.06-.48.06-.48.8.06 1.22.82 1.22.82.71 1.22 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.14-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 014 0c1.53-1.03 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.55.82 1.27.82 2.14 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
      </button>
      <button class="icon-btn" title="Cài đặt nhanh" onclick="switchView('settings')">
        <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M8 10a2 2 0 100-4 2 2 0 000 4z" stroke="currentColor" stroke-width="1.3"/><path d="M12.9 8.7l.9.5-1 1.7-1-.4a3.9 3.9 0 01-1 .6l-.2 1.1H8.4l-.2-1.1a3.9 3.9 0 01-1-.6l-1 .4-1-1.7.9-.5a4 4 0 010-1.4l-.9-.5 1-1.7 1 .4a3.9 3.9 0 011-.6l.2-1.1h1.2l.2 1.1a3.9 3.9 0 011 .6l1-.4 1 1.7-.9.5a4 4 0 010 1.4z" stroke="currentColor" stroke-width="1.1" stroke-linejoin="round"/></svg>
      </button>
      <div class="user-chip" title="Tài khoản" onclick="showToast('info','Menu người dùng')">NV</div>
    </div>
  </header>

  <div class="body-wrap">

    <!-- ============================================================
         SIDEBAR (icon rail, giống VS Code activity bar)
    ============================================================= -->
    <aside class="sidebar" id="sidebar">
      <div class="nav-item active" data-view="dashboard" onclick="switchView('dashboard')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <span class="tooltip">Dashboard</span>
      </div>
      <div class="nav-item" data-view="documentation" onclick="switchView('documentation')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M4 4.5A1.5 1.5 0 015.5 3H15l5 5v11.5A1.5 1.5 0 0118.5 21h-13A1.5 1.5 0 014 19.5v-15z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 12h8M8 16h5M15 3v5h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span class="tooltip">Documentation</span>
      </div>
      <div class="nav-item" data-view="wiki" onclick="switchView('wiki')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M12 4C9 2.5 5 2.5 3 4v15c2-1.5 6-1.5 9 0m0-15c3-1.5 7-1.5 9 0v15c-2-1.5-6-1.5-9 0m0-15v15" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <span class="tooltip">Wiki</span>
      </div>
      <div class="nav-item" data-view="explorer" onclick="switchView('explorer')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M3 7a2 2 0 012-2h4l2 2h8a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2V7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <span class="tooltip">File Explorer</span>
      </div>
      <div class="nav-item" data-view="api" onclick="switchView('api')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M8 8l-5 4 5 4M16 8l5 4-5 4M13 5l-2 14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="tooltip">API</span>
      </div>
      <div class="nav-item" data-view="sdk" onclick="switchView('sdk')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M12 2l3 6 6 1-4.5 4.5L17.5 20 12 17l-5.5 3 1-6.5L3 9l6-1 3-6z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
        <span class="tooltip">SDK</span>
      </div>
      <div class="nav-item" data-view="examples" onclick="switchView('examples')">
        <svg viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="7" height="7" rx="1.4" stroke="currentColor" stroke-width="1.6"/><rect x="14" y="3" width="7" height="7" rx="1.4" stroke="currentColor" stroke-width="1.6"/><rect x="3" y="14" width="7" height="7" rx="1.4" stroke="currentColor" stroke-width="1.6"/><rect x="14" y="14" width="7" height="7" rx="1.4" stroke="currentColor" stroke-width="1.6"/></svg>
        <span class="tooltip">Examples</span>
      </div>
      <div class="nav-item" data-view="ai" onclick="switchView('ai')">
        <svg viewBox="0 0 24 24" fill="none"><path d="M12 2l1.8 4.6L18.5 8l-4.7 1.4L12 14l-1.8-4.6L5.5 8l4.7-1.4L12 2z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M19 14l.9 2.2L22 17l-2.1.8L19 20l-.9-2.2L16 17l2.1-.8L19 14z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
        <span class="tooltip">AI Assistant</span>
      </div>
      <div class="nav-item" data-view="search" onclick="switchView('search')">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.6"/><path d="M21 21l-4.3-4.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span class="tooltip">Search</span>
      </div>
      <div class="nav-item" data-view="git" onclick="switchView('git')">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="6" cy="6" r="2.2" stroke="currentColor" stroke-width="1.6"/><circle cx="6" cy="18" r="2.2" stroke="currentColor" stroke-width="1.6"/><circle cx="18" cy="9" r="2.2" stroke="currentColor" stroke-width="1.6"/><path d="M6 8.2V15.8M6 8.2C6 12 10 9.5 15.8 10.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span class="tooltip">Git</span>
      </div>
      <div class="nav-item" data-view="terminal" onclick="switchView('terminal')">
        <svg viewBox="0 0 24 24" fill="none"><rect x="3" y="4" width="18" height="16" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M7 9l3 3-3 3M13 15h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="tooltip">Terminal</span>
      </div>
      <div class="sidebar-spacer"></div>
      <div class="sidebar-divider"></div>
      <div class="nav-item" data-view="settings" onclick="switchView('settings')">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M19.4 13.5a1.7 1.7 0 000-3l1.2-1.9-2-2-1.9 1.2a1.7 1.7 0 00-3 0L11.9 3H9.4l-1.8 1.8a1.7 1.7 0 00-3 0L2.7 3.6l-2 2 1.2 1.9a1.7 1.7 0 000 3L.7 12.4l2 2 1.9-1.2a1.7 1.7 0 003 0l1.8 1.8h2.5l1.8-1.8a1.7 1.7 0 003 0l1.9 1.2 2-2-1.2-1.9z" stroke="currentColor" stroke-width="0"/></svg>
        <span class="tooltip">Settings</span>
      </div>
    </aside>

    <!-- ============================================================
         MAIN CONTENT
    ============================================================= -->
    <main class="content" id="content">

      <!-- ===================== DASHBOARD ===================== -->
      <section class="view active" data-view="dashboard" id="view-dashboard">
        <div class="view-inner">

          <div class="hero">
            <span class="hero-badge">⚡ Phiên bản 3.4.0 đã sẵn sàng</span>
            <h1>Chào buổi sáng, Nguyễn Văn 👋</h1>
            <p>Đây là tổng quan hoạt động dự án ClaudeRiks hôm nay — theo dõi commit, tài liệu mới, và trạng thái build của bạn tại một nơi duy nhất.</p>
            <div class="hero-actions">
              <button class="btn btn-primary" onclick="switchView('terminal')">
                <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M4 4l4 4-4 4M9 12h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Mở Terminal
              </button>
              <button class="btn" onclick="switchView('documentation')">Xem tài liệu</button>
              <button class="btn" onclick="switchView('ai')">Hỏi AI Assistant</button>
            </div>
          </div>

          <div class="grid-cards">
            <div class="card">
              <div class="card-top">
                <div class="card-icon blue"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M9 17V9m3 8v-4m3 4V5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></div>
                <span class="card-trend up">▲ 12%</span>
              </div>
              <div class="value">2,481</div>
              <div class="label">Lượt truy cập tài liệu / tuần</div>
            </div>
            <div class="card">
              <div class="card-top">
                <div class="card-icon green"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
                <span class="card-trend up">▲ 4</span>
              </div>
              <div class="value">96.4%</div>
              <div class="label">Tỉ lệ build thành công</div>
            </div>
            <div class="card">
              <div class="card-top">
                <div class="card-icon purple"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="1.8"/><circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="1.8"/><path d="M6 8v8" stroke="currentColor" stroke-width="1.8"/></svg></div>
                <span class="card-trend up">▲ 8</span>
              </div>
              <div class="value">153</div>
              <div class="label">Commit trong tháng này</div>
            </div>
            <div class="card">
              <div class="card-top">
                <div class="card-icon orange"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 2v6M12 16v6M4.9 4.9l4.2 4.2M14.9 14.9l4.2 4.2M2 12h6M16 12h6M4.9 19.1l4.2-4.2M14.9 9.1l4.2-4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></div>
                <span class="card-trend down">▼ 2</span>
              </div>
              <div class="value">7</div>
              <div class="label">Issue đang mở</div>
            </div>
          </div>

          <div class="section-block">
            <h3>Tài nguyên hệ thống</h3>
            <div class="stats-row">
              <div class="stat-box">
                <div class="num">42%</div>
                <div class="lbl">CPU sử dụng</div>
                <div class="bar-track"><div class="bar-fill" style="width:42%"></div></div>
              </div>
              <div class="stat-box">
                <div class="num">3.1 GB</div>
                <div class="lbl">Bộ nhớ RAM / 8GB</div>
                <div class="bar-track"><div class="bar-fill" style="width:39%"></div></div>
              </div>
              <div class="stat-box">
                <div class="num">68%</div>
                <div class="lbl">Dung lượng ổ đĩa</div>
                <div class="bar-track"><div class="bar-fill" style="width:68%"></div></div>
              </div>
              <div class="stat-box">
                <div class="num">128 ms</div>
                <div class="lbl">Độ trễ mạng</div>
                <div class="bar-track"><div class="bar-fill" style="width:22%"></div></div>
              </div>
            </div>
          </div>

          <div class="two-col">
            <div class="panel section-block">
              <div class="panel-header">
                <h4>Hoạt động gần đây</h4>
                <button class="btn btn-sm" onclick="switchView('git')">Xem Git</button>
              </div>
              <div class="panel-body" id="activity-list">
                <div class="activity-item">
                  <div class="activity-dot commit"></div>
                  <div>
                    <div class="activity-text"><b>ngvanan</b> đã commit "fix: sửa lỗi hiển thị sidebar khi thu gọn"</div>
                    <div class="activity-time">5 phút trước · main</div>
                  </div>
                </div>
                <div class="activity-item">
                  <div class="activity-dot merge"></div>
                  <div>
                    <div class="activity-text"><b>tranthib</b> đã merge nhánh <span class="mono">feature/api-v2</span> vào <span class="mono">develop</span></div>
                    <div class="activity-time">32 phút trước</div>
                  </div>
                </div>
                <div class="activity-item">
                  <div class="activity-dot release"></div>
                  <div>
                    <div class="activity-text">Đã phát hành phiên bản <b>v3.4.0</b></div>
                    <div class="activity-time">2 giờ trước</div>
                  </div>
                </div>
                <div class="activity-item">
                  <div class="activity-dot issue"></div>
                  <div>
                    <div class="activity-text"><b>lehoangm</b> đã mở issue "Terminal không hỗ trợ lệnh docker compose"</div>
                    <div class="activity-time">5 giờ trước</div>
                  </div>
                </div>
                <div class="activity-item">
                  <div class="activity-dot commit"></div>
                  <div>
                    <div class="activity-text"><b>phamquocd</b> đã commit "docs: cập nhật hướng dẫn cài đặt SDK"</div>
                    <div class="activity-time">1 ngày trước</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="panel section-block">
              <div class="panel-header">
                <h4>Tệp gần đây</h4>
                <button class="btn btn-sm" onclick="switchView('explorer')">Mở Explorer</button>
              </div>
              <div class="panel-body" id="recent-files-list">
                <div class="file-row" onclick="switchView('explorer')">
                  <span>📄</span>
                  <span class="fname">src/components/Sidebar.js</span>
                  <span class="fmeta">2 phút</span>
                </div>
                <div class="file-row" onclick="switchView('explorer')">
                  <span>🎨</span>
                  <span class="fname">styles/theme.css</span>
                  <span class="fmeta">18 phút</span>
                </div>
                <div class="file-row" onclick="switchView('explorer')">
                  <span>📄</span>
                  <span class="fname">server/routes/api.js</span>
                  <span class="fmeta">1 giờ</span>
                </div>
                <div class="file-row" onclick="switchView('explorer')">
                  <span>📘</span>
                  <span class="fname">docs/getting-started.md</span>
                  <span class="fmeta">3 giờ</span>
                </div>
                <div class="file-row" onclick="switchView('explorer')">
                  <span>⚙️</span>
                  <span class="fname">config/webpack.config.js</span>
                  <span class="fmeta">Hôm qua</span>
                </div>
              </div>
            </div>
          </div>

          <div class="section-block">
            <h3>Tài liệu nổi bật</h3>
            <div class="doc-grid">
              <div class="doc-tile" onclick="switchView('documentation')">
                <div class="di">📘</div>
                <div><p class="dt">Bắt đầu nhanh</p><p class="dd">Cài đặt và cấu hình dự án trong 5 phút.</p></div>
              </div>
              <div class="doc-tile" onclick="switchView('api')">
                <div class="di">🔌</div>
                <div><p class="dt">Tham chiếu API</p><p class="dd">Danh sách endpoint và tham số đầy đủ.</p></div>
              </div>
              <div class="doc-tile" onclick="switchView('sdk')">
                <div class="di">📦</div>
                <div><p class="dt">SDK Client</p><p class="dd">Thư viện chính thức cho Node.js, Python.</p></div>
              </div>
              <div class="doc-tile" onclick="switchView('wiki')">
                <div class="di">🗂️</div>
                <div><p class="dt">Kiến trúc hệ thống</p><p class="dd">Sơ đồ luồng dữ liệu và các thành phần.</p></div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ===================== DOCUMENTATION ===================== -->
      <section class="view" data-view="documentation" id="view-documentation">
        <div class="docs-layout">
          <nav class="docs-sidebar">
            <div class="docs-search"><input type="text" placeholder="Lọc tài liệu..." oninput="filterDocsSidebar(this.value)"></div>

            <div class="docs-group">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Bắt đầu
              </div>
              <div class="docs-links">
                <a href="#" class="active" onclick="return loadDoc(event,'intro')">Giới thiệu</a>
                <a href="#" onclick="return loadDoc(event,'install')">Cài đặt</a>
                <a href="#" onclick="return loadDoc(event,'quickstart')">Bắt đầu nhanh</a>
                <a href="#" onclick="return loadDoc(event,'config')">Cấu hình dự án</a>
              </div>
            </div>

            <div class="docs-group">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Hướng dẫn cốt lõi
              </div>
              <div class="docs-links">
                <a href="#" onclick="return loadDoc(event,'routing')">Định tuyến</a>
                <a href="#" onclick="return loadDoc(event,'state')">Quản lý trạng thái</a>
                <a href="#" onclick="return loadDoc(event,'styling')">Styling &amp; Theme</a>
                <a href="#" onclick="return loadDoc(event,'testing')">Kiểm thử</a>
              </div>
            </div>

            <div class="docs-group">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Triển khai
              </div>
              <div class="docs-links">
                <a href="#" onclick="return loadDoc(event,'deploy')">Deploy production</a>
                <a href="#" onclick="return loadDoc(event,'docker')">Docker</a>
                <a href="#" onclick="return loadDoc(event,'ci')">CI/CD</a>
              </div>
            </div>

            <div class="docs-group collapsed">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Nâng cao
              </div>
              <div class="docs-links">
                <a href="#" onclick="return loadDoc(event,'perf')">Tối ưu hiệu năng</a>
                <a href="#" onclick="return loadDoc(event,'security')">Bảo mật</a>
                <a href="#" onclick="return loadDoc(event,'plugins')">Viết Plugin</a>
              </div>
            </div>
          </nav>

          <div class="docs-main">
            <div class="docs-content" id="docs-content">
              <!-- filled dynamically, default below -->
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== WIKI ===================== -->
      <section class="view" data-view="wiki" id="view-wiki">
        <div class="wiki-layout">
          <div class="wiki-main">
            <div class="docs-content">
              <h1>Kiến trúc hệ thống ClaudeRiks</h1>
              <p class="docs-meta">Cập nhật lần cuối: 26/07/2026 · Người chỉnh sửa: Trần Thị B · <span class="badge blue">Wiki</span></p>

              <h2 id="w-tong-quan">Tổng quan</h2>
              <p>Hệ thống ClaudeRiks được thiết kế theo mô hình microservice, tách biệt giữa lớp giao diện, lớp API Gateway, và các dịch vụ nội bộ. Sơ đồ dưới đây mô tả luồng xử lý một request điển hình.</p>

              <div class="mermaid-box">
                <div class="flow-branch">
                  <div class="flow-row">
                    <div class="flow-node">Client / Browser</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-node">API Gateway</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-node">Auth Service</div>
                  </div>
                  <span class="flow-arrow">↓</span>
                  <div class="flow-row">
                    <div class="flow-node">Core Service</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-node">Database</div>
                    <span class="flow-arrow">→</span>
                    <div class="flow-node">Cache Layer</div>
                  </div>
                </div>
              </div>

              <div class="callout note">
                <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.4"/><path d="M8 7v4M8 5v.01" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
                <div><div class="callout-title">Ghi chú</div><div class="callout-body">Toàn bộ giao tiếp giữa Gateway và các service nội bộ sử dụng giao thức gRPC để tối ưu độ trễ.</div></div>
              </div>

              <div class="callout warning">
                <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M8 1.5L15 14H1L8 1.5z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M8 6.5v3M8 11.5v.01" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
                <div><div class="callout-title">Cảnh báo</div><div class="callout-body">Không gọi trực tiếp Database từ tầng Client. Mọi truy vấn phải đi qua Core Service để đảm bảo kiểm soát quyền truy cập.</div></div>
              </div>

              <h2 id="w-auth">Xác thực &amp; Phân quyền</h2>
              <p>Auth Service sử dụng JWT với thời gian sống ngắn (15 phút) kết hợp refresh token lưu trong HttpOnly cookie. Mọi request tới Core Service đều được xác thực chữ ký token trước khi xử lý nghiệp vụ.</p>

              <div class="callout tip">
                <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M8 1.5c-2.5 0-4.5 2-4.5 4.5 0 1.7.9 3.1 2.2 3.9.3.2.5.5.5.9v.7h3.6v-.7c0-.4.2-.7.5-.9 1.3-.8 2.2-2.2 2.2-3.9 0-2.5-2-4.5-4.5-4.5z" stroke="currentColor" stroke-width="1.3"/><path d="M6.5 14h3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
                <div><div class="callout-title">Mẹo</div><div class="callout-body">Dùng lệnh <code class="inline">git tag</code> để đánh dấu phiên bản trước khi thay đổi cấu hình Auth Service ở production.</div></div>
              </div>

              <h2 id="w-cache">Chiến lược Cache</h2>
              <p>Cache Layer dùng chiến lược write-through cho dữ liệu người dùng và write-back cho dữ liệu thống kê không quan trọng về tính nhất quán tức thời.</p>

              <div class="callout danger">
                <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.4"/><path d="M5.5 5.5l5 5m0-5l-5 5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
                <div><div class="callout-title">Nguy hiểm</div><div class="callout-body">Không xóa toàn bộ cache ở production trong giờ cao điểm — thao tác này có thể gây quá tải Database trong vài giây tiếp theo.</div></div>
              </div>

              <h2 id="w-deploy">Triển khai</h2>
              <p>Hệ thống triển khai trên Kubernetes với 3 namespace: <code class="inline">staging</code>, <code class="inline">canary</code>, và <code class="inline">production</code>. Pipeline CI/CD tự động chạy kiểm thử trước khi cho phép merge vào nhánh chính.</p>
            </div>
          </div>

          <aside class="wiki-toc">
            <h4>Trong trang này</h4>
            <ul>
              <li><a href="#w-tong-quan" class="active">Tổng quan</a></li>
              <li><a href="#w-auth">Xác thực &amp; Phân quyền</a></li>
              <li><a href="#w-cache">Chiến lược Cache</a></li>
              <li><a href="#w-deploy">Triển khai</a></li>
            </ul>
          </aside>
        </div>
      </section>

      <!-- ===================== FILE EXPLORER ===================== -->
      <section class="view" data-view="explorer" id="view-explorer">
        <div class="explorer-layout">
          <div class="explorer-tree">
            <div class="explorer-tree-head">
              <span>CLAUDERIKS</span>
              <span style="display:flex;gap:4px;">
                <span class="icon-btn" style="width:24px;height:24px;" title="Thu gọn tất cả" onclick="collapseAllTree()">
                  <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
                </span>
              </span>
            </div>
            <div id="file-tree"></div>
          </div>

          <div class="viewer-panel">
            <div class="viewer-tabs" id="viewer-tabs"></div>
            <div class="viewer-toolbar">
              <div class="path" id="viewer-path"><b>App.js</b></div>
              <div class="viewer-toolbar-actions">
                <button class="copy-btn" onclick="copyViewerCode(this)">📋 Copy</button>
                <button class="copy-btn" onclick="downloadViewerCode()">⬇ Download</button>
                <button class="copy-btn" onclick="toggleFullscreen()">⛶ Fullscreen</button>
              </div>
            </div>
            <div class="code-viewer-scroll" id="code-viewer-scroll">
              <!-- populated by JS -->
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== API ===================== -->
      <section class="view" data-view="api" id="view-api">
        <div class="docs-layout">
          <nav class="docs-sidebar">
            <div class="docs-search"><input type="text" placeholder="Lọc endpoint..." oninput="filterDocsSidebar(this.value)"></div>
            <div class="docs-group">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Người dùng
              </div>
              <div class="docs-links">
                <a href="#" class="active" onclick="return loadApi(event,'get-users')"><span class="badge green" style="margin-right:6px;">GET</span>/users</a>
                <a href="#" onclick="return loadApi(event,'get-user')"><span class="badge green" style="margin-right:6px;">GET</span>/users/:id</a>
                <a href="#" onclick="return loadApi(event,'post-user')"><span class="badge blue" style="margin-right:6px;">POST</span>/users</a>
                <a href="#" onclick="return loadApi(event,'delete-user')"><span class="badge red" style="margin-right:6px;">DEL</span>/users/:id</a>
              </div>
            </div>
            <div class="docs-group">
              <div class="docs-group-title" onclick="toggleGroup(this)">
                <svg viewBox="0 0 12 12" fill="none"><path d="M4 2l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>
                Kho lưu trữ
              </div>
              <div class="docs-links">
                <a href="#" onclick="return loadApi(event,'get-repos')"><span class="badge green" style="margin-right:6px;">GET</span>/repos</a>
                <a href="#" onclick="return loadApi(event,'post-repo')"><span class="badge blue" style="margin-right:6px;">POST</span>/repos</a>
                <a href="#" onclick="return loadApi(event,'patch-repo')"><span class="badge orange" style="margin-right:6px;">PATCH</span>/repos/:id</a>
              </div>
            </div>
          </nav>
          <div class="docs-main">
            <div class="docs-content" id="api-content"></div>
          </div>
        </div>
      </section>

      <!-- ===================== SDK ===================== -->
      <section class="view" data-view="sdk" id="view-sdk">
        <div class="view-inner">
          <div class="section-title">📦 SDK Client chính thức</div>
          <p class="section-sub">Cài đặt và sử dụng ClaudeRiks SDK trong ứng dụng của bạn.</p>

          <div class="grid-cards" style="margin-bottom:24px;">
            <div class="card"><div class="card-top"><div class="card-icon blue">JS</div></div><div class="value">Node.js</div><div class="label">npm install @claudeeriks/sdk</div></div>
            <div class="card"><div class="card-top"><div class="card-icon green">PY</div></div><div class="value">Python</div><div class="label">pip install claudeeriks</div></div>
            <div class="card"><div class="card-top"><div class="card-icon purple">GO</div></div><div class="value">Go</div><div class="label">go get claudeeriks/sdk</div></div>
            <div class="card"><div class="card-top"><div class="card-icon orange">RS</div></div><div class="value">Rust</div><div class="label">cargo add claudeeriks</div></div>
          </div>

          <div class="section-block">
            <h3>Ví dụ khởi tạo client (Node.js)</h3>
            <div class="code-block">
              <div class="code-block-head">
                <span class="lang">javascript</span>
                <div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div>
              </div>
              <pre id="sdk-code-1"><div class="code-line"><span class="ln">1</span><span class="lc"><span class="tok-kw">import</span> { Client } <span class="tok-kw">from</span> <span class="tok-str">'@claudeeriks/sdk'</span>;</span></div><div class="code-line"><span class="ln">2</span><span class="lc"></span></div><div class="code-line"><span class="ln">3</span><span class="lc"><span class="tok-kw">const</span> client = <span class="tok-kw">new</span> <span class="tok-fn">Client</span>({</span></div><div class="code-line"><span class="ln">4</span><span class="lc">  <span class="tok-prop">apiKey</span>: <span class="tok-str">process.env.CLAUDERIKS_KEY</span>,</span></div><div class="code-line"><span class="ln">5</span><span class="lc">  <span class="tok-prop">region</span>: <span class="tok-str">'ap-southeast-1'</span>,</span></div><div class="code-line"><span class="ln">6</span><span class="lc">});</span></div><div class="code-line"><span class="ln">7</span><span class="lc"></span></div><div class="code-line"><span class="ln">8</span><span class="lc"><span class="tok-kw">const</span> repo = <span class="tok-kw">await</span> client.repos.<span class="tok-fn">get</span>(<span class="tok-str">'clauderiks/core'</span>);</span></div><div class="code-line"><span class="ln">9</span><span class="lc"><span class="tok-fn">console</span>.<span class="tok-fn">log</span>(repo.<span class="tok-prop">stars</span>); <span class="tok-com">// -> 1280</span></span></div></pre>
            </div>
          </div>

          <div class="section-block">
            <h3>Ví dụ khởi tạo client (Python)</h3>
            <div class="code-block">
              <div class="code-block-head">
                <span class="lang">python</span>
                <div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div>
              </div>
              <pre id="sdk-code-2"><div class="code-line"><span class="ln">1</span><span class="lc"><span class="tok-kw">from</span> clauderiks <span class="tok-kw">import</span> Client</span></div><div class="code-line"><span class="ln">2</span><span class="lc"></span></div><div class="code-line"><span class="ln">3</span><span class="lc">client = <span class="tok-fn">Client</span>(api_key=<span class="tok-str">"sk_live_xxx"</span>)</span></div><div class="code-line"><span class="ln">4</span><span class="lc">repo = client.repos.<span class="tok-fn">get</span>(<span class="tok-str">"clauderiks/core"</span>)</span></div><div class="code-line"><span class="ln">5</span><span class="lc"><span class="tok-fn">print</span>(repo.stars)  <span class="tok-com"># -> 1280</span></span></div></pre>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== EXAMPLES ===================== -->
      <section class="view" data-view="examples" id="view-examples">
        <div class="view-inner">
          <div class="section-title">🧩 Ví dụ mẫu</div>
          <p class="section-sub">Các đoạn mã mẫu thường dùng để tích hợp nhanh với ClaudeRiks.</p>
          <div class="doc-grid" id="examples-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: Xác thực OAuth2')"><div class="di">🔐</div><div><p class="dt">Xác thực OAuth2</p><p class="dd">Luồng đăng nhập đầy đủ với refresh token.</p></div></div>
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: Webhook lắng nghe sự kiện')"><div class="di">📡</div><div><p class="dt">Webhook Listener</p><p class="dd">Nhận sự kiện real-time từ ClaudeRiks.</p></div></div>
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: Upload file lớn')"><div class="di">📤</div><div><p class="dt">Upload file lớn</p><p class="dd">Chia nhỏ file và upload theo từng phần.</p></div></div>
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: Rate limit retry')"><div class="di">⏱️</div><div><p class="dt">Xử lý Rate Limit</p><p class="dd">Retry tự động khi gặp lỗi 429.</p></div></div>
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: CLI tuỳ biến')"><div class="di">🖥️</div><div><p class="dt">CLI tuỳ biến</p><p class="dd">Xây dựng lệnh CLI riêng dựa trên SDK.</p></div></div>
            <div class="doc-tile" onclick="showToast('info','Đang mở ví dụ: Triển khai Docker Compose')"><div class="di">🐳</div><div><p class="dt">Docker Compose</p><p class="dd">Chạy toàn bộ stack chỉ với một lệnh.</p></div></div>
          </div>
        </div>
      </section>

      <!-- ===================== AI ASSISTANT ===================== -->
      <section class="view" data-view="ai" id="view-ai">
        <div class="ai-layout">
          <div class="ai-history">
            <button class="btn btn-primary new-chat-btn" onclick="newAiChat()">+ Cuộc trò chuyện mới</button>
            <div class="ai-history-date">Hôm nay</div>
            <div class="ai-history-item active">Cách cấu hình webhook</div>
            <div class="ai-history-item">Sửa lỗi CORS trên API</div>
            <div class="ai-history-date">Hôm qua</div>
            <div class="ai-history-item">Tối ưu truy vấn Database</div>
            <div class="ai-history-item">Viết test cho Auth Service</div>
            <div class="ai-history-item">So sánh REST và gRPC</div>
            <div class="ai-history-date">Tuần trước</div>
            <div class="ai-history-item">Thiết lập CI/CD với GitHub Actions</div>
            <div class="ai-history-item">Giải thích JWT refresh token</div>
          </div>

          <div class="ai-main">
            <div class="ai-messages" id="ai-messages">
              <div class="ai-msg-row assistant">
                <div class="ai-avatar assistant">CR</div>
                <div class="ai-msg-content">
                  <div class="ai-msg-name">ClaudeRiks Assistant</div>
                  <div class="ai-msg-text"><p>Xin chào! Mình có thể giúp bạn tra cứu tài liệu, giải thích API, hoặc viết đoạn mã mẫu. Bạn cần hỗ trợ điều gì hôm nay?</p></div>
                </div>
              </div>
            </div>

            <div class="ai-suggestions" id="ai-suggestions">
              <div class="suggestion-chip" onclick="sendSuggestion('Cách tạo webhook mới là gì?')">Cách tạo webhook mới?</div>
              <div class="suggestion-chip" onclick="sendSuggestion('Giải thích sự khác nhau giữa REST và gRPC')">REST vs gRPC?</div>
              <div class="suggestion-chip" onclick="sendSuggestion('Viết ví dụ xác thực JWT bằng Node.js')">Ví dụ xác thực JWT</div>
            </div>

            <div class="ai-input-bar">
              <div class="ai-input-box">
                <textarea id="ai-input" rows="1" placeholder="Nhắn tin cho AI Assistant..." onkeydown="handleAiKeydown(event)" oninput="autoGrow(this)"></textarea>
                <button class="ai-send-btn" onclick="sendAiMessage()">
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 8l12-6-4 6 4 6-12-6z" fill="currentColor"/></svg>
                </button>
              </div>
              <div class="ai-input-hint">AI Assistant có thể mắc lỗi. Hãy kiểm tra lại các thông tin quan trọng.</div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== SEARCH ===================== -->
      <section class="view" data-view="search" id="view-search">
        <div class="search-hero">
          <div class="search-big-box">
            <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.5"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            <input type="text" id="search-input" placeholder="Tìm kiếm tài liệu, API, file, wiki..." oninput="doSearch(this.value)">
          </div>
          <div class="search-filters">
            <div class="filter-chip active" data-scope="all" onclick="setSearchScope(this,'all')">Tất cả</div>
            <div class="filter-chip" data-scope="docs" onclick="setSearchScope(this,'docs')">📘 Documentation</div>
            <div class="filter-chip" data-scope="api" onclick="setSearchScope(this,'api')">🔌 API</div>
            <div class="filter-chip" data-scope="file" onclick="setSearchScope(this,'file')">📄 File</div>
            <div class="filter-chip" data-scope="wiki" onclick="setSearchScope(this,'wiki')">🗂️ Wiki</div>
          </div>
        </div>
        <div class="search-results" id="search-results">
          <div class="search-empty">Nhập từ khoá để bắt đầu tìm kiếm trên toàn bộ hệ thống.</div>
        </div>
      </section>

      <!-- ===================== GIT ===================== -->
      <section class="view" data-view="git" id="view-git">
        <div class="view-inner git-layout">
          <div class="section-title">🔀 Git</div>
          <p class="section-sub">Quản lý nhánh, commit, và phát hành phiên bản cho kho lưu trữ hiện tại.</p>

          <div class="git-toolbar">
            <div class="branch-select" onclick="showToast('info','Danh sách nhánh: main, develop, feature/api-v2')">
              <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="4" cy="4" r="1.6" stroke="currentColor" stroke-width="1.3"/><circle cx="4" cy="12" r="1.6" stroke="currentColor" stroke-width="1.3"/><circle cx="12" cy="6" r="1.6" stroke="currentColor" stroke-width="1.3"/><path d="M4 5.6v4.8M4 5.6C4 8 7 7 10.4 7.6" stroke="currentColor" stroke-width="1.3"/></svg>
              main <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 4.5l3 3 3-3" stroke="currentColor" stroke-width="1.4"/></svg>
            </div>
            <button class="btn" onclick="gitAction('pull')">⬇ Pull</button>
            <button class="btn" onclick="gitAction('push')">⬆ Push</button>
            <button class="btn" onclick="gitAction('commit')">✅ Commit</button>
            <button class="btn" onclick="gitAction('merge')">🔀 Merge</button>
            <button class="btn btn-success" onclick="gitAction('release')">🏷️ Release</button>
          </div>

          <div class="git-grid">
            <div class="panel">
              <div class="panel-header"><h4>Lịch sử commit</h4><span class="badge blue">main</span></div>
              <div class="panel-body">
                <div class="commit-item">
                  <div class="commit-avatar"></div>
                  <div><div class="commit-msg">fix: sửa lỗi hiển thị sidebar khi thu gọn</div><div class="commit-meta"><span class="commit-hash">a3f9c1e</span> · ngvanan · 5 phút trước</div></div>
                </div>
                <div class="commit-item">
                  <div class="commit-avatar"></div>
                  <div><div class="commit-msg">feat: thêm API endpoint /repos/:id/stats</div><div class="commit-meta"><span class="commit-hash">7be21aa</span> · tranthib · 1 giờ trước</div></div>
                </div>
                <div class="commit-item">
                  <div class="commit-avatar"></div>
                  <div><div class="commit-msg">docs: cập nhật hướng dẫn cài đặt SDK</div><div class="commit-meta"><span class="commit-hash">f01d2c8</span> · phamquocd · 1 ngày trước</div></div>
                </div>
                <div class="commit-item">
                  <div class="commit-avatar"></div>
                  <div><div class="commit-msg">chore: nâng cấp dependencies lên phiên bản mới</div><div class="commit-meta"><span class="commit-hash">9e4b7d0</span> · lehoangm · 2 ngày trước</div></div>
                </div>
              </div>
            </div>

            <div class="panel">
              <div class="panel-header"><h4>Nhánh</h4><span class="badge gray">4 nhánh</span></div>
              <div class="panel-body">
                <div class="branch-item"><div class="branch-name"><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="4" cy="4" r="1.6" stroke="currentColor" stroke-width="1.3"/></svg>main</div><span class="badge green">mặc định</span></div>
                <div class="branch-item"><div class="branch-name"><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="4" cy="4" r="1.6" stroke="currentColor" stroke-width="1.3"/></svg>develop</div><span class="badge blue">đang hoạt động</span></div>
                <div class="branch-item"><div class="branch-name"><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="4" cy="4" r="1.6" stroke="currentColor" stroke-width="1.3"/></svg>feature/api-v2</div><span class="badge orange">chưa merge</span></div>
                <div class="branch-item"><div class="branch-name"><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="4" cy="4" r="1.6" stroke="currentColor" stroke-width="1.3"/></svg>hotfix/cors-issue</div><span class="badge red">xung đột</span></div>
              </div>
            </div>
          </div>

          <div class="section-block" style="margin-top:20px;">
            <h3>Thay đổi (diff) chưa commit</h3>
            <div class="code-block">
              <div class="code-block-head"><span class="lang">src/api/client.js</span><div class="code-block-actions"><span class="badge green">+2</span><span class="badge red">-1</span></div></div>
              <pre style="padding:10px 0;">
<div class="diff-line diff-add"><span class="sign">+</span>  timeout: 8000, // tăng timeout mặc định lên 8s</div><div class="diff-line diff-remove"><span class="sign">-</span>  timeout: 5000,</div><div class="diff-line diff-add"><span class="sign">+</span>  retries: 3,</div></pre>
            </div>
          </div>

          <div class="section-block">
            <h3>Nhật ký thao tác</h3>
            <div class="panel">
              <div class="panel-body" id="git-log-list" style="padding:14px 18px; font-family:var(--font-mono); font-size:12.5px; color:var(--text-secondary);">
                <div>$ đang chờ thao tác Git...</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== TERMINAL ===================== -->
      <section class="view" data-view="terminal" id="view-terminal">
        <div class="terminal-wrap">
          <div class="terminal-window">
            <div class="terminal-titlebar">
              <div class="tl-dot red"></div><div class="tl-dot yellow"></div><div class="tl-dot green"></div>
              <div class="ttitle">nguyenvanan@clauderiks: ~/projects/clauderiks</div>
            </div>
            <div class="terminal-body" id="terminal-body">
              <div class="term-line term-info">ClaudeRiks Terminal Simulator v1.0 — gõ "help" để xem danh sách lệnh.</div>
            </div>
            <div class="terminal-titlebar" style="border-top:1px solid var(--border); border-bottom:none;">
              <div class="term-input-row" style="width:100%; padding:0 4px;">
                <span class="term-prompt">➜</span>
                <span class="term-path" id="term-path">~/projects/clauderiks</span>
                <span class="term-prompt">$</span>
                <input type="text" id="term-input" autocomplete="off" spellcheck="false" onkeydown="handleTermKeydown(event)" placeholder="Nhập lệnh...">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===================== SETTINGS ===================== -->
      <section class="view" data-view="settings" id="view-settings">
        <div class="settings-layout">
          <nav class="settings-nav">
            <div class="settings-nav-item active" onclick="switchSettingsPanel(this,'general')">Chung</div>
            <div class="settings-nav-item" onclick="switchSettingsPanel(this,'theme')">Giao diện</div>
            <div class="settings-nav-item" onclick="switchSettingsPanel(this,'editor')">Trình soạn thảo</div>
            <div class="settings-nav-item" onclick="switchSettingsPanel(this,'terminal-set')">Terminal</div>
            <div class="settings-nav-item" onclick="switchSettingsPanel(this,'language')">Ngôn ngữ</div>
            <div class="settings-nav-item" onclick="switchSettingsPanel(this,'notifications-set')">Thông báo</div>
          </nav>

          <div class="settings-main">

            <div class="settings-panel active" id="settings-general">
              <div class="section-title" style="font-size:17px;">Cài đặt chung</div>
              <div class="setting-row">
                <div><div class="setting-label">Tự động lưu</div><div class="setting-desc">Tự động lưu thay đổi tài liệu sau mỗi 30 giây.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Hiệu ứng chuyển động</div><div class="setting-desc">Bật animation mượt khi chuyển trang.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Xác nhận trước khi xoá</div><div class="setting-desc">Hiển thị hộp thoại xác nhận khi xoá file hoặc nhánh.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
            </div>

            <div class="settings-panel" id="settings-theme">
              <div class="section-title" style="font-size:17px;">Giao diện</div>
              <div class="setting-row">
                <div><div class="setting-label">Chủ đề màu</div><div class="setting-desc">Chọn bảng màu hiển thị cho toàn bộ ứng dụng.</div></div>
                <div class="theme-swatches">
                  <div class="theme-swatch selected" style="background:#0d1117;" title="GitHub Dark"></div>
                  <div class="theme-swatch" style="background:#1e1e1e;" title="VS Code Dark+"></div>
                  <div class="theme-swatch" style="background:#282a36;" title="Dracula"></div>
                  <div class="theme-swatch" style="background:#011627;" title="Night Owl"></div>
                </div>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Độ trong suốt nền</div><div class="setting-desc">Điều chỉnh độ mờ của các panel.</div></div>
                <input type="range" class="slider-range" min="0" max="100" value="100">
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Bo góc giao diện</div><div class="setting-desc">Bật/tắt bo góc cho card và nút bấm.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
            </div>

            <div class="settings-panel" id="settings-editor">
              <div class="section-title" style="font-size:17px;">Trình soạn thảo</div>
              <div class="setting-row">
                <div><div class="setting-label">Font chữ</div><div class="setting-desc">Font hiển thị trong Code Viewer.</div></div>
                <div class="setting-control"><select><option>SF Mono</option><option>Fira Code</option><option>JetBrains Mono</option><option>Consolas</option></select></div>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Cỡ chữ</div><div class="setting-desc">Kích thước chữ hiển thị mã nguồn.</div></div>
                <div class="setting-control"><select><option>12px</option><option selected>13px</option><option>14px</option><option>16px</option></select></div>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Hiện số dòng</div><div class="setting-desc">Hiển thị số thứ tự dòng trong Code Viewer.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Word wrap</div><div class="setting-desc">Tự động xuống dòng khi mã quá dài.</div></div>
                <label class="switch"><input type="checkbox"><span class="slider"></span></label>
              </div>
            </div>

            <div class="settings-panel" id="settings-terminal-set">
              <div class="section-title" style="font-size:17px;">Terminal</div>
              <div class="setting-row">
                <div><div class="setting-label">Shell mặc định</div><div class="setting-desc">Loại shell mô phỏng trong Terminal.</div></div>
                <div class="setting-control"><select><option>bash</option><option>zsh</option><option>PowerShell</option><option>fish</option></select></div>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Con trỏ nhấp nháy</div><div class="setting-desc">Bật hiệu ứng nhấp nháy con trỏ terminal.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Lịch sử lệnh tối đa</div><div class="setting-desc">Số lệnh được lưu trong lịch sử.</div></div>
                <div class="setting-control"><select><option>50</option><option selected>100</option><option>500</option></select></div>
              </div>
            </div>

            <div class="settings-panel" id="settings-language">
              <div class="section-title" style="font-size:17px;">Ngôn ngữ</div>
              <div class="setting-row">
                <div><div class="setting-label">Ngôn ngữ hiển thị</div><div class="setting-desc">Ngôn ngữ giao diện ứng dụng.</div></div>
                <div class="setting-control"><select><option selected>Tiếng Việt</option><option>English</option><option>日本語</option><option>한국어</option></select></div>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Định dạng ngày giờ</div><div class="setting-desc">Cách hiển thị ngày tháng trong ứng dụng.</div></div>
                <div class="setting-control"><select><option selected>DD/MM/YYYY</option><option>MM/DD/YYYY</option><option>YYYY-MM-DD</option></select></div>
              </div>
            </div>

            <div class="settings-panel" id="settings-notifications-set">
              <div class="section-title" style="font-size:17px;">Thông báo</div>
              <div class="setting-row">
                <div><div class="setting-label">Thông báo commit mới</div><div class="setting-desc">Nhận thông báo khi có commit mới trên nhánh theo dõi.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Thông báo build thất bại</div><div class="setting-desc">Cảnh báo ngay khi pipeline CI/CD thất bại.</div></div>
                <label class="switch"><input type="checkbox" checked><span class="slider"></span></label>
              </div>
              <div class="setting-row">
                <div><div class="setting-label">Âm thanh thông báo</div><div class="setting-desc">Phát âm thanh khi có thông báo mới.</div></div>
                <label class="switch"><input type="checkbox"><span class="slider"></span></label>
              </div>
            </div>

          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- ============================================================
       FOOTER / STATUS BAR
  ============================================================= -->
  <footer class="statusbar">
    <div class="statusbar-item">🌿 main</div>
    <div class="statusbar-item">⟳ đồng bộ</div>
    <div class="statusbar-item">✔ 0 lỗi · ⚠ 2 cảnh báo</div>
    <div class="statusbar-spacer"></div>
    <div class="statusbar-item">Phiên bản 3.4.0</div>
    <div class="statusbar-item">Build #1042</div>
    <div class="statusbar-item">© 2026 ClaudeRiks</div>
  </footer>

</div>

<!-- Command palette (Ctrl+K) -->
<div class="cmdk-overlay" id="cmdk-overlay" onclick="if(event.target===this) closeCommandPalette()">
  <div class="cmdk-box">
    <div class="cmdk-input-wrap">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.5"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <input type="text" id="cmdk-input" placeholder="Gõ lệnh hoặc tìm trang..." oninput="filterCmdk(this.value)">
    </div>
    <div class="cmdk-list" id="cmdk-list"></div>
  </div>
</div>

<!-- Toast container -->
<div class="toast-container" id="toast-container"></div>

<script>
/* ============================================================
   ClaudeRiks — Application Script
   Toàn bộ logic UI được viết bằng Vanilla JavaScript thuần.
   ============================================================ */
'use strict';

/* -------------------- Global State -------------------- */
const state = {
  currentView: 'dashboard',
  terminalCwd: '~/projects/clauderiks',
  terminalHistory: [],
  terminalHistoryIndex: -1,
  openTabs: [],
  activeTabId: null,
  searchScope: 'all',
  aiChatActive: true
};

/* ============================================================
   VIEW SWITCHING
   ============================================================ */
function switchView(viewName){
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

  const target = document.getElementById('view-' + viewName);
  if(target){ target.classList.add('active'); }

  const navItem = document.querySelector('.nav-item[data-view="' + viewName + '"]');
  if(navItem){ navItem.classList.add('active'); }

  state.currentView = viewName;
  closeCommandPalette();
}

/* ============================================================
   TOAST NOTIFICATIONS
   ============================================================ */
function showToast(type, message){
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = 'toast ' + type;
  const icons = { success:'✅', error:'❌', info:'ℹ️' };
  toast.innerHTML = '<span>' + (icons[type] || 'ℹ️') + '</span><span>' + escapeHtml(message) + '</span>';
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.animation = 'toastIn .25s ease reverse';
    setTimeout(() => toast.remove(), 250);
  }, 3200);
}

function escapeHtml(str){
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

/* ============================================================
   NOTIFICATIONS DROPDOWN (simple toggle demo)
   ============================================================ */
function toggleNotifications(btn){
  showToast('info', 'Bạn có 3 thông báo chưa đọc: 2 commit mới, 1 build thất bại.');
}

/* ============================================================
   COMMAND PALETTE (Ctrl+K)
   ============================================================ */
const cmdkCommands = [
  { label:'Đi tới Dashboard', view:'dashboard', icon:'📊' },
  { label:'Đi tới Documentation', view:'documentation', icon:'📘' },
  { label:'Đi tới Wiki', view:'wiki', icon:'🗂️' },
  { label:'Đi tới File Explorer', view:'explorer', icon:'📁' },
  { label:'Đi tới API', view:'api', icon:'🔌' },
  { label:'Đi tới SDK', view:'sdk', icon:'📦' },
  { label:'Đi tới Examples', view:'examples', icon:'🧩' },
  { label:'Đi tới AI Assistant', view:'ai', icon:'🤖' },
  { label:'Đi tới Search', view:'search', icon:'🔍' },
  { label:'Đi tới Git', view:'git', icon:'🔀' },
  { label:'Đi tới Terminal', view:'terminal', icon:'⌨️' },
  { label:'Đi tới Settings', view:'settings', icon:'⚙️' }
];

function openCommandPalette(){
  const overlay = document.getElementById('cmdk-overlay');
  overlay.classList.add('open');
  const input = document.getElementById('cmdk-input');
  input.value = '';
  renderCmdkList('');
  setTimeout(() => input.focus(), 30);
}
function closeCommandPalette(){
  document.getElementById('cmdk-overlay').classList.remove('open');
}
function renderCmdkList(filter){
  const list = document.getElementById('cmdk-list');
  const f = filter.toLowerCase();
  const filtered = cmdkCommands.filter(c => c.label.toLowerCase().includes(f));
  list.innerHTML = filtered.map(c =>
    '<div class="cmdk-item" onclick="switchView(\'' + c.view + '\')"><span>' + c.icon + '</span><span>' + c.label + '</span><span class="cmdk-kbd">Enter</span></div>'
  ).join('') || '<div class="cmdk-item">Không tìm thấy kết quả</div>';
}
function filterCmdk(val){ renderCmdkList(val); }

document.addEventListener('keydown', function(e){
  if((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k'){
    e.preventDefault();
    openCommandPalette();
  }
  if(e.key === 'Escape'){
    closeCommandPalette();
    exitFullscreen();
  }
});

/* ============================================================
   DOCUMENTATION — content database + markdown-style viewer
   ============================================================ */
const docsDatabase = {
  intro: {
    title:'Giới thiệu ClaudeRiks',
    meta:'Cập nhật: 20/07/2026 · 4 phút đọc',
    html: `
      <p>ClaudeRiks là nền tảng phát triển tất cả trong một, cung cấp tài liệu, API, SDK và công cụ dòng lệnh cho đội ngũ kỹ thuật. Trang này giúp bạn hiểu tổng quan các thành phần chính trước khi bắt đầu.</p>
      <h2>Các thành phần chính</h2>
      <ul>
        <li><b>API Gateway</b> — điểm vào duy nhất cho mọi request từ client.</li>
        <li><b>SDK đa ngôn ngữ</b> — hỗ trợ Node.js, Python, Go, Rust.</li>
        <li><b>CLI Terminal</b> — thao tác nhanh với dự án ngay trong trình duyệt.</li>
      </ul>
      <h2>Yêu cầu hệ thống</h2>
      <table>
        <tr><th>Thành phần</th><th>Phiên bản tối thiểu</th><th>Khuyến nghị</th></tr>
        <tr><td>Node.js</td><td>16.x</td><td>20.x LTS</td></tr>
        <tr><td>Python</td><td>3.8</td><td>3.11+</td></tr>
        <tr><td>RAM</td><td>2GB</td><td>8GB</td></tr>
      </table>
    `
  },
  install: {
    title:'Cài đặt',
    meta:'Cập nhật: 18/07/2026 · 3 phút đọc',
    html: `
      <p>Cài đặt ClaudeRiks CLI thông qua trình quản lý gói yêu thích của bạn.</p>
      <div class="code-block"><div class="code-block-head"><span class="lang">bash</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'npm install -g @clauderiks/cli','plain')}${codeLine(2,'# hoặc','com')}${codeLine(3,'yarn global add @clauderiks/cli','plain')}</pre></div>
      <p>Sau khi cài đặt, kiểm tra phiên bản bằng lệnh sau:</p>
      <div class="code-block"><div class="code-block-head"><span class="lang">bash</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'clauderiks --version','plain')}</pre></div>
    `
  },
  quickstart: {
    title:'Bắt đầu nhanh',
    meta:'Cập nhật: 15/07/2026 · 5 phút đọc',
    html: `
      <p>Tạo dự án mới chỉ với 3 bước đơn giản.</p>
      <h3>Bước 1 — Khởi tạo dự án</h3>
      <div class="code-block"><div class="code-block-head"><span class="lang">bash</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'clauderiks init my-app','plain')}</pre></div>
      <h3>Bước 2 — Cấu hình biến môi trường</h3>
      <div class="code-block"><div class="code-block-head"><span class="lang">bash</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'cp .env.example .env','plain')}</pre></div>
      <h3>Bước 3 — Chạy dự án</h3>
      <div class="code-block"><div class="code-block-head"><span class="lang">bash</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'cd my-app && npm run dev','plain')}</pre></div>
    `
  },
  config: { title:'Cấu hình dự án', meta:'Cập nhật: 12/07/2026 · 6 phút đọc', html:'<p>Tệp cấu hình chính nằm tại <code class="inline">clauderiks.config.js</code>, cho phép tuỳ biến plugin, alias đường dẫn, và biến môi trường theo từng giai đoạn triển khai.</p><h2>Ví dụ cấu hình</h2>' + '<div class="code-block"><div class="code-block-head"><span class="lang">javascript</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>' + codeLine(1,'module.exports = {','plain') + codeLine(2,'  plugins: [require("@clauderiks/plugin-auth")],','plain') + codeLine(3,'  env: "production",','plain') + codeLine(4,'};','plain') + '</pre></div>' },
  routing: { title:'Định tuyến', meta:'Cập nhật: 10/07/2026 · 4 phút đọc', html:'<p>Hệ thống định tuyến hỗ trợ file-based routing tương tự Next.js, tự động sinh route từ cấu trúc thư mục <code class="inline">/pages</code>.</p>' },
  state: { title:'Quản lý trạng thái', meta:'Cập nhật: 08/07/2026 · 5 phút đọc', html:'<p>ClaudeRiks đề xuất sử dụng store tập trung nhẹ, tránh phụ thuộc thư viện ngoài không cần thiết cho các dự án nhỏ và vừa.</p>' },
  styling: { title:'Styling & Theme', meta:'Cập nhật: 05/07/2026 · 3 phút đọc', html:'<p>Toàn bộ theme sử dụng CSS Variables, cho phép chuyển đổi Dark/Light theme tức thời không cần tải lại trang.</p>' },
  testing: { title:'Kiểm thử', meta:'Cập nhật: 02/07/2026 · 4 phút đọc', html:'<p>Chạy toàn bộ test suite bằng lệnh <code class="inline">clauderiks test</code>, hỗ trợ chế độ watch và báo cáo coverage chi tiết.</p>' },
  deploy: { title:'Deploy production', meta:'Cập nhật: 28/06/2026 · 6 phút đọc', html:'<p>Khuyến nghị triển khai qua pipeline CI/CD tự động, tránh deploy thủ công để giảm rủi ro sai sót cấu hình.</p>' },
  docker: { title:'Docker', meta:'Cập nhật: 25/06/2026 · 5 phút đọc', html:'<div class="code-block"><div class="code-block-head"><span class="lang">dockerfile</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>' + codeLine(1,'FROM node:20-alpine','plain') + codeLine(2,'WORKDIR /app','plain') + codeLine(3,'COPY . .','plain') + codeLine(4,'RUN npm install','plain') + codeLine(5,'CMD ["npm", "start"]','plain') + '</pre></div>' },
  ci: { title:'CI/CD', meta:'Cập nhật: 20/06/2026 · 5 phút đọc', html:'<p>Pipeline mặc định chạy 3 giai đoạn: lint, test, và build, trước khi cho phép merge vào nhánh chính.</p>' },
  perf: { title:'Tối ưu hiệu năng', meta:'Cập nhật: 15/06/2026 · 6 phút đọc', html:'<p>Sử dụng lazy-loading cho các module ít dùng và bật cache HTTP ở tầng CDN để giảm tải cho Core Service.</p>' },
  security: { title:'Bảo mật', meta:'Cập nhật: 10/06/2026 · 7 phút đọc', html:'<p>Áp dụng nguyên tắc least privilege cho mọi service account, và xoay vòng secret định kỳ mỗi 90 ngày.</p>' },
  plugins: { title:'Viết Plugin', meta:'Cập nhật: 05/06/2026 · 6 phút đọc', html:'<p>Plugin ClaudeRiks tuân theo interface chuẩn với các hook <code class="inline">onInit</code>, <code class="inline">onRequest</code>, và <code class="inline">onError</code>.</p>' }
};

function codeLine(num, text, kind){
  let content = escapeHtml(text);
  if(kind === 'com'){ content = '<span class="tok-com">' + content + '</span>'; }
  return '<div class="code-line"><span class="ln">' + num + '</span><span class="lc">' + content + '</span></div>';
}

function loadDoc(evt, key){
  evt.preventDefault();
  document.querySelectorAll('#view-documentation .docs-links a').forEach(a => a.classList.remove('active'));
  evt.currentTarget.classList.add('active');
  const doc = docsDatabase[key];
  if(!doc) return false;
  const container = document.getElementById('docs-content');
  container.style.animation = 'none';
  void container.offsetWidth;
  container.style.animation = 'fadeIn .3s ease';
  container.innerHTML =
    '<h1>' + doc.title + '</h1>' +
    '<p class="docs-meta">' + doc.meta + '</p>' +
    doc.html;
  container.scrollTop = 0;
  document.querySelector('.docs-main').scrollTop = 0;
  return false;
}

function toggleGroup(el){
  el.parentElement.classList.toggle('collapsed');
}

function filterDocsSidebar(query){
  const q = query.toLowerCase();
  document.querySelectorAll('.docs-sidebar .docs-links a, #view-api .docs-links a').forEach(a => {
    const match = a.textContent.toLowerCase().includes(q);
    a.style.display = match ? 'block' : 'none';
  });
}

/* init default doc */
window.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('docs-content');
  const doc = docsDatabase.intro;
  container.innerHTML = '<h1>' + doc.title + '</h1><p class="docs-meta">' + doc.meta + '</p>' + doc.html;
});

/* ============================================================
   API VIEW — endpoint reference
   ============================================================ */
const apiDatabase = {
  'get-users': {
    title:'GET /users', method:'green', desc:'Trả về danh sách người dùng có phân trang.',
    html: `<p>Lấy danh sách toàn bộ người dùng trong tổ chức, hỗ trợ tham số phân trang <code class="inline">page</code> và <code class="inline">limit</code>.</p>
    <h2>Tham số truy vấn</h2>
    <table><tr><th>Tên</th><th>Kiểu</th><th>Bắt buộc</th><th>Mô tả</th></tr>
    <tr><td>page</td><td>number</td><td>Không</td><td>Trang hiện tại, mặc định 1</td></tr>
    <tr><td>limit</td><td>number</td><td>Không</td><td>Số bản ghi mỗi trang, tối đa 100</td></tr></table>
    <h2>Ví dụ phản hồi</h2>
    <div class="code-block"><div class="code-block-head"><span class="lang">json</span><div class="code-block-actions"><button class="copy-btn" onclick="copyCodeBlock(this)">📋 Copy</button></div></div><pre>${codeLine(1,'{','plain')}${codeLine(2,'  "data": [{ "id": 1, "name": "Nguyen Van A" }],','plain')}${codeLine(3,'  "page": 1,','plain')}${codeLine(4,'  "total": 42','plain')}${codeLine(5,'}','plain')}</pre></div>`
  },
  'get-user': { title:'GET /users/:id', method:'green', desc:'Lấy chi tiết một người dùng theo ID.', html:'<p>Trả về thông tin chi tiết của một người dùng cụ thể, bao gồm vai trò và trạng thái hoạt động.</p>' },
  'post-user': { title:'POST /users', method:'blue', desc:'Tạo mới người dùng.', html:'<p>Tạo một tài khoản người dùng mới trong hệ thống. Yêu cầu quyền admin.</p>' },
  'delete-user': { title:'DELETE /users/:id', method:'red', desc:'Xoá người dùng theo ID.', html:'<p>Xoá vĩnh viễn tài khoản người dùng. Thao tác này không thể hoàn tác.</p>' },
  'get-repos': { title:'GET /repos', method:'green', desc:'Danh sách kho lưu trữ.', html:'<p>Trả về danh sách các kho lưu trữ mà người dùng hiện tại có quyền truy cập.</p>' },
  'post-repo': { title:'POST /repos', method:'blue', desc:'Tạo kho lưu trữ mới.', html:'<p>Khởi tạo một kho lưu trữ Git mới gắn với tổ chức hiện tại.</p>' },
  'patch-repo': { title:'PATCH /repos/:id', method:'orange', desc:'Cập nhật thông tin kho lưu trữ.', html:'<p>Cập nhật một phần thông tin của kho lưu trữ, ví dụ tên hiển thị hoặc mô tả.</p>' }
};

function loadApi(evt, key){
  evt.preventDefault();
  document.querySelectorAll('#view-api .docs-links a').forEach(a => a.classList.remove('active'));
  evt.currentTarget.classList.add('active');
  const item = apiDatabase[key];
  if(!item) return false;
  const container = document.getElementById('api-content');
  container.innerHTML =
    '<h1><span class="badge ' + item.method + '" style="margin-right:8px;">' + (item.method==='green'?'GET':item.method==='blue'?'POST':item.method==='red'?'DELETE':'PATCH') + '</span>' + item.title + '</h1>' +
    '<p class="docs-meta">' + item.desc + '</p>' + item.html;
  return false;
}
window.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('api-content');
  const item = apiDatabase['get-users'];
  container.innerHTML = '<h1><span class="badge green" style="margin-right:8px;">GET</span>' + item.title + '</h1><p class="docs-meta">' + item.desc + '</p>' + item.html;
});

/* ============================================================
   FILE EXPLORER — tree + code viewer
   ============================================================ */
const fileSystem = {
  name:'clauderiks', type:'folder', open:true, children:[
    { name:'src', type:'folder', open:true, children:[
      { name:'components', type:'folder', open:false, children:[
        { name:'Sidebar.js', type:'file', lang:'javascript' },
        { name:'Topbar.js', type:'file', lang:'javascript' },
        { name:'Dashboard.js', type:'file', lang:'javascript' }
      ]},
      { name:'api', type:'folder', open:false, children:[
        { name:'client.js', type:'file', lang:'javascript' },
        { name:'routes.js', type:'file', lang:'javascript' }
      ]},
      { name:'App.js', type:'file', lang:'javascript' },
      { name:'index.js', type:'file', lang:'javascript' }
    ]},
    { name:'styles', type:'folder', open:false, children:[
      { name:'theme.css', type:'file', lang:'css' },
      { name:'globals.css', type:'file', lang:'css' }
    ]},
    { name:'server', type:'folder', open:false, children:[
      { name:'routes', type:'folder', open:false, children:[
        { name:'api.js', type:'file', lang:'javascript' },
        { name:'auth.js', type:'file', lang:'javascript' }
      ]},
      { name:'server.js', type:'file', lang:'javascript' }
    ]},
    { name:'docs', type:'folder', open:false, children:[
      { name:'getting-started.md', type:'file', lang:'markdown' },
      { name:'api-reference.md', type:'file', lang:'markdown' }
    ]},
    { name:'package.json', type:'file', lang:'json' },
    { name:'README.md', type:'file', lang:'markdown' }
  ]
};

const fileContents = {
  'App.js': [
    "import React from 'react';",
    "import Sidebar from './components/Sidebar';",
    "import Topbar from './components/Topbar';",
    "",
    "// Component gốc của ứng dụng ClaudeRiks",
    "function App() {",
    "  return (",
    "    <div className=\"app-shell\">",
    "      <Topbar />",
    "      <Sidebar />",
    "      <main>{/* nội dung chính */}</main>",
    "    </div>",
    "  );",
    "}",
    "",
    "export default App;"
  ],
  'Sidebar.js': [
    "import React, { useState } from 'react';",
    "",
    "// Thanh điều hướng bên trái, giống VS Code activity bar",
    "export default function Sidebar() {",
    "  const [active, setActive] = useState('dashboard');",
    "  const items = ['dashboard','docs','wiki','explorer'];",
    "  return (",
    "    <aside className=\"sidebar\">",
    "      {items.map(item => (",
    "        <button key={item} onClick={() => setActive(item)}>",
    "          {item}",
    "        </button>",
    "      ))}",
    "    </aside>",
    "  );",
    "}"
  ],
  'theme.css': [
    ":root {",
    "  --bg: #0d1117;",
    "  --sidebar: #161b22;",
    "  --border: #30363d;",
    "  --primary: #58a6ff;",
    "  --text: #f0f6fc;",
    "}",
    "",
    "body {",
    "  background: var(--bg);",
    "  color: var(--text);",
    "}"
  ],
  'api.js': [
    "const express = require('express');",
    "const router = express.Router();",
    "",
    "// Endpoint lấy danh sách người dùng",
    "router.get('/users', async (req, res) => {",
    "  const users = await db.query('SELECT * FROM users');",
    "  res.json({ data: users });",
    "});",
    "",
    "module.exports = router;"
  ],
  'package.json': [
    "{",
    '  "name": "clauderiks",',
    '  "version": "3.4.0",',
    '  "scripts": {',
    '    "dev": "node server.js",',
    '    "build": "webpack --mode production"',
    "  }",
    "}"
  ],
  'README.md': [
    "# ClaudeRiks",
    "",
    "Nền tảng phát triển tất cả trong một cho đội ngũ kỹ thuật.",
    "",
    "## Cài đặt",
    "",
    "npm install -g @clauderiks/cli"
  ]
};

function fileIcon(name, type){
  if(type === 'folder') return '📁';
  if(name.endsWith('.js')) return '📜';
  if(name.endsWith('.css')) return '🎨';
  if(name.endsWith('.md')) return '📘';
  if(name.endsWith('.json')) return '⚙️';
  return '📄';
}

function renderTree(node, depth){
  depth = depth || 0;
  const indent = 14 + depth * 16;
  if(node.type === 'folder'){
    const openClass = node.open ? 'open' : '';
    let html = '<div class="tree-node">';
    html += '<div class="tree-row folder ' + openClass + '" style="padding-left:' + indent + 'px" onclick="toggleTreeFolder(this, event)">';
    html += '<svg class="chevron" viewBox="0 0 16 16" fill="none"><path d="M6 4l4 4-4 4" stroke="currentColor" stroke-width="1.6"/></svg>';
    html += '<span class="ficon">📁</span><span>' + node.name + '</span></div>';
    html += '<div class="tree-children ' + openClass + '">';
    node.children.forEach(child => { html += renderTree(child, depth + 1); });
    html += '</div></div>';
    return html;
  } else {
    return '<div class="tree-row file" style="padding-left:' + (indent + 20) + 'px" onclick="openFile(\'' + node.name + '\', \'' + (node.lang||'plain') + '\', this)">' +
      '<span class="ficon">' + fileIcon(node.name, 'file') + '</span><span>' + node.name + '</span></div>';
  }
}

function toggleTreeFolder(el, evt){
  evt.stopPropagation();
  el.classList.toggle('open');
  const children = el.nextElementSibling;
  if(children){ children.classList.toggle('open'); }
}

function collapseAllTree(){
  document.querySelectorAll('.tree-row.folder').forEach(r => r.classList.remove('open'));
  document.querySelectorAll('.tree-children').forEach(c => c.classList.remove('open'));
  showToast('info', 'Đã thu gọn toàn bộ cây thư mục');
}

function highlightLine(text){
  let t = escapeHtml(text);
  t = t.replace(/(&#39;.*?&#39;|&quot;.*?&quot;)/g, '<span class="tok-str">$1</span>');
  t = t.replace(/\b(function|const|let|var|return|import|export|from|default|if|else|class|new|async|await|require|module\.exports)\b/g, '<span class="tok-kw">$1</span>');
  t = t.replace(/(\/\/.*$)/g, '<span class="tok-com">$1</span>');
  return t;
}

function openFile(name, lang, el){
  document.querySelectorAll('.tree-row.file').forEach(r => r.classList.remove('selected'));
  if(el) el.classList.add('selected');

  if(!state.openTabs.find(t => t.name === name)){
    state.openTabs.push({ name, lang });
  }
  state.activeTabId = name;
  renderTabs();
  renderCodeViewer(name, lang);
}

function renderTabs(){
  const tabsEl = document.getElementById('viewer-tabs');
  tabsEl.innerHTML = state.openTabs.map(tab => {
    const activeClass = tab.name === state.activeTabId ? 'active' : '';
    return '<div class="viewer-tab ' + activeClass + '" onclick="openFile(\'' + tab.name + '\',\'' + tab.lang + '\')">' +
      '<span>' + fileIcon(tab.name,'file') + '</span><span>' + tab.name + '</span>' +
      '<span class="close-x" onclick="closeTab(event,\'' + tab.name + '\')">×</span></div>';
  }).join('');
}

function closeTab(evt, name){
  evt.stopPropagation();
  state.openTabs = state.openTabs.filter(t => t.name !== name);
  if(state.activeTabId === name){
    const last = state.openTabs[state.openTabs.length - 1];
    if(last){ openFile(last.name, last.lang); }
    else {
      state.activeTabId = null;
      document.getElementById('viewer-tabs').innerHTML = '';
      document.getElementById('code-viewer-scroll').innerHTML = '';
      document.getElementById('viewer-path').innerHTML = '<b>Chưa mở tệp nào</b>';
    }
  } else {
    renderTabs();
  }
}

function renderCodeViewer(name, lang){
  const lines = fileContents[name] || ['// Không có nội dung xem trước cho tệp này', '// ' + name];
  const scroll = document.getElementById('code-viewer-scroll');
  let html = '<pre>';
  lines.forEach((line, i) => {
    html += '<div class="code-line"><span class="ln">' + (i+1) + '</span><span class="lc">' + highlightLine(line) + '</span></div>';
  });
  html += '</pre>';
  scroll.innerHTML = html;
  document.getElementById('viewer-path').innerHTML = 'src / <b>' + name + '</b> <span class="badge gray" style="margin-left:6px;">' + lang + '</span>';
}

function copyViewerCode(btn){
  const lines = document.querySelectorAll('#code-viewer-scroll .lc');
  const text = Array.from(lines).map(l => l.textContent).join('\n');
  copyToClipboard(text, btn);
}

function downloadViewerCode(){
  const name = state.activeTabId || 'file.txt';
  const lines = document.querySelectorAll('#code-viewer-scroll .lc');
  const text = Array.from(lines).map(l => l.textContent).join('\n');
  const blob = new Blob([text], { type:'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = name;
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
  showToast('success', 'Đã tải xuống ' + name);
}

function toggleFullscreen(){
  const panel = document.querySelector('.viewer-panel');
  panel.classList.toggle('fullscreen-mode');
}
function exitFullscreen(){
  document.querySelectorAll('.fullscreen-mode').forEach(p => p.classList.remove('fullscreen-mode'));
}

/* generic copy-to-clipboard code block used in docs/sdk pages */
function copyCodeBlock(btn){
  const pre = btn.closest('.code-block').querySelector('pre');
  const lines = pre.querySelectorAll('.lc');
  const text = Array.from(lines).map(l => l.textContent).join('\n');
  copyToClipboard(text, btn);
}

function copyToClipboard(text, btn){
  const fallback = () => {
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try{ document.execCommand('copy'); }catch(e){}
    ta.remove();
  };
  if(navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(text).catch(fallback);
  } else {
    fallback();
  }
  if(btn){
    const original = btn.innerHTML;
    btn.classList.add('copied');
    btn.innerHTML = '✅ Đã chép';
    setTimeout(() => { btn.classList.remove('copied'); btn.innerHTML = original; }, 1600);
  }
  showToast('success', 'Đã sao chép vào clipboard');
}

window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('file-tree').innerHTML = renderTree(fileSystem);
  openFile('App.js', 'javascript');
});

/* ============================================================
   TERMINAL SIMULATOR
   ============================================================ */
const termHelpText = [
  { cmd:'help', desc:'Hiển thị danh sách lệnh khả dụng' },
  { cmd:'clear', desc:'Xoá toàn bộ nội dung terminal' },
  { cmd:'ls', desc:'Liệt kê tệp/thư mục hiện tại' },
  { cmd:'pwd', desc:'Hiển thị đường dẫn hiện tại' },
  { cmd:'cd', desc:'Di chuyển thư mục' },
  { cmd:'mkdir', desc:'Tạo thư mục mới' },
  { cmd:'rm', desc:'Xoá tệp hoặc thư mục' },
  { cmd:'cp', desc:'Sao chép tệp' },
  { cmd:'mv', desc:'Di chuyển / đổi tên tệp' },
  { cmd:'touch', desc:'Tạo tệp rỗng mới' },
  { cmd:'cat', desc:'Hiển thị nội dung tệp' },
  { cmd:'echo', desc:'In chuỗi văn bản ra màn hình' },
  { cmd:'git', desc:'Thao tác quản lý phiên bản Git' },
  { cmd:'gh', desc:'GitHub CLI — quản lý issue, PR' },
  { cmd:'npm', desc:'Quản lý gói Node.js' },
  { cmd:'pnpm', desc:'Trình quản lý gói nhanh, tiết kiệm ổ đĩa' },
  { cmd:'bun', desc:'Runtime & package manager tốc độ cao' },
  { cmd:'node', desc:'Chạy tệp JavaScript bằng Node.js' },
  { cmd:'python', desc:'Chạy tệp Python' },
  { cmd:'docker', desc:'Quản lý container Docker' },
  { cmd:'curl', desc:'Gửi request HTTP tới URL' },
  { cmd:'wget', desc:'Tải tệp từ URL' }
];

function termPrintLine(html){
  const body = document.getElementById('terminal-body');
  const div = document.createElement('div');
  div.className = 'term-line';
  div.innerHTML = html;
  body.appendChild(div);
  body.scrollTop = body.scrollHeight;
}

function termPrintCommandEcho(cmd){
  termPrintLine('<span class="term-prompt">➜</span> <span class="term-path">' + escapeHtml(state.terminalCwd) + '</span> <span class="term-prompt">$</span> <span class="term-cmd">' + escapeHtml(cmd) + '</span>');
}

function simulateCommand(raw){
  const cmd = raw.trim();
  if(cmd === '') return;

  state.terminalHistory.push(cmd);
  state.terminalHistoryIndex = state.terminalHistory.length;

  termPrintCommandEcho(cmd);

  const parts = cmd.split(/\s+/);
  const base = parts[0];
  const args = parts.slice(1);

  switch(base){
    case 'help':
      termHelpText.forEach(h => {
        termPrintLine('<span class="term-info" style="display:inline-block;width:90px;">' + h.cmd + '</span><span class="term-out">' + h.desc + '</span>');
      });
      break;
    case 'clear':
      document.getElementById('terminal-body').innerHTML = '';
      break;
    case 'ls':
      termPrintLine('<span class="term-out">src  styles  server  docs  package.json  README.md</span>');
      break;
    case 'pwd':
      termPrintLine('<span class="term-out">/home/nguyenvanan/projects/clauderiks</span>');
      break;
    case 'cd':
      if(args[0]){
        state.terminalCwd = args[0] === '..' ? '~/projects' : '~/projects/clauderiks/' + args[0];
        document.getElementById('term-path').textContent = state.terminalCwd;
        termPrintLine('<span class="term-out">Đã chuyển tới ' + escapeHtml(state.terminalCwd) + '</span>');
      } else {
        termPrintLine('<span class="term-err">cd: thiếu đường dẫn</span>');
      }
      break;
    case 'mkdir':
      termPrintLine('<span class="term-out">Đã tạo thư mục "' + escapeHtml(args[0] || 'new-folder') + '"</span>');
      break;
    case 'rm':
      termPrintLine('<span class="term-out">Đã xoá "' + escapeHtml(args.join(' ') || 'tệp') + '"</span>');
      break;
    case 'cp':
      termPrintLine('<span class="term-out">Đã sao chép ' + escapeHtml(args[0]||'src') + ' → ' + escapeHtml(args[1]||'dest') + '</span>');
      break;
    case 'mv':
      termPrintLine('<span class="term-out">Đã di chuyển ' + escapeHtml(args[0]||'src') + ' → ' + escapeHtml(args[1]||'dest') + '</span>');
      break;
    case 'touch':
      termPrintLine('<span class="term-out">Đã tạo tệp "' + escapeHtml(args[0] || 'new-file.txt') + '"</span>');
      break;
    case 'cat':
      if(fileContents[args[0]]){
        fileContents[args[0]].forEach(l => termPrintLine('<span class="term-out">' + escapeHtml(l) + '</span>'));
      } else {
        termPrintLine('<span class="term-err">cat: không tìm thấy tệp "' + escapeHtml(args[0]||'') + '"</span>');
      }
      break;
    case 'echo':
      termPrintLine('<span class="term-out">' + escapeHtml(args.join(' ')) + '</span>');
      break;
    case 'git':
      simulateGitCommand(args);
      break;
    case 'gh':
      termPrintLine('<span class="term-out">gh: đã tạo pull request #128 "feat: thêm API v2" thành công</span>');
      break;
    case 'npm':
      simulateNpmCommand(args);
      break;
    case 'pnpm':
      termPrintLine('<span class="term-out">pnpm: đã cài đặt 214 gói trong 3.2s</span>');
      break;
    case 'bun':
      termPrintLine('<span class="term-out">bun: đã cài đặt các gói trong 340ms ⚡</span>');
      break;
    case 'node':
      termPrintLine('<span class="term-out">Đang chạy ' + escapeHtml(args[0]||'index.js') + '...</span>');
      termPrintLine('<span class="term-out">Server đang chạy tại http://localhost:3000</span>');
      break;
    case 'python':
      termPrintLine('<span class="term-out">Đang chạy ' + escapeHtml(args[0]||'main.py') + ' với Python 3.11.4</span>');
      break;
    case 'docker':
      simulateDockerCommand(args);
      break;
    case 'curl':
      termPrintLine('<span class="term-out">HTTP/1.1 200 OK</span>');
      termPrintLine('<span class="term-out">{"status":"ok","service":"clauderiks-api"}</span>');
      break;
    case 'wget':
      termPrintLine('<span class="term-out">Đang tải ' + escapeHtml(args[0] || 'file') + '... 100% hoàn tất</span>');
      break;
    default:
      termPrintLine('<span class="term-err">command not found: ' + escapeHtml(base) + '</span>');
      termPrintLine('<span class="term-info">Gõ "help" để xem danh sách lệnh khả dụng.</span>');
  }
}

function simulateGitCommand(args){
  const sub = args[0];
  if(sub === 'status'){
    termPrintLine('<span class="term-out">Trên nhánh main</span>');
    termPrintLine('<span class="term-out">Thay đổi chưa được stage: src/api/client.js</span>');
  } else if(sub === 'commit'){
    termPrintLine('<span class="term-out">[main a3f9c1e] ' + escapeHtml(args.slice(2).join(' ') || 'commit message') + '</span>');
    termPrintLine('<span class="term-out"> 2 files changed, 14 insertions(+), 3 deletions(-)</span>');
  } else if(sub === 'push'){
    termPrintLine('<span class="term-out">Đang đẩy lên origin/main...</span>');
    termPrintLine('<span class="term-out">Tổng: 5 đối tượng, đã hoàn tất.</span>');
  } else if(sub === 'pull'){
    termPrintLine('<span class="term-out">Đang lấy về từ origin...</span>');
    termPrintLine('<span class="term-out">Already up to date.</span>');
  } else if(sub === 'branch'){
    termPrintLine('<span class="term-out">* main</span>');
    termPrintLine('<span class="term-out">  develop</span>');
    termPrintLine('<span class="term-out">  feature/api-v2</span>');
  } else if(sub === 'log'){
    termPrintLine('<span class="term-out">a3f9c1e fix: sửa lỗi hiển thị sidebar</span>');
    termPrintLine('<span class="term-out">7be21aa feat: thêm API endpoint mới</span>');
  } else if(sub === 'checkout'){
    termPrintLine('<span class="term-out">Switched to branch \'' + escapeHtml(args[1]||'main') + '\'</span>');
  } else if(sub === 'merge'){
    termPrintLine('<span class="term-out">Merge made by the \'ort\' strategy.</span>');
  } else {
    termPrintLine('<span class="term-out">git: mô phỏng lệnh "' + escapeHtml(args.join(' ')) + '"</span>');
  }
}

function simulateNpmCommand(args){
  const sub = args[0];
  if(sub === 'install' || sub === 'i'){
    termPrintLine('<span class="term-out">added 214 packages in 3.8s</span>');
  } else if(sub === 'run'){
    termPrintLine('<span class="term-out">> clauderiks@3.4.0 ' + escapeHtml(args[1]||'dev') + '</span>');
    termPrintLine('<span class="term-out">Server đang chạy tại http://localhost:3000</span>');
  } else if(sub === 'test'){
    termPrintLine('<span class="term-out">Test Suites: 12 passed, 12 total</span>');
    termPrintLine('<span class="term-out">Tests: 87 passed, 87 total</span>');
  } else if(sub === 'build'){
    termPrintLine('<span class="term-out">Build hoàn tất trong 8.2s. Kích thước: 412kb</span>');
  } else {
    termPrintLine('<span class="term-out">npm: mô phỏng lệnh "' + escapeHtml(args.join(' ')) + '"</span>');
  }
}

function simulateDockerCommand(args){
  const sub = args[0];
  if(sub === 'ps'){
    termPrintLine('<span class="term-out">CONTAINER ID   IMAGE           STATUS</span>');
    termPrintLine('<span class="term-out">a1b2c3d4e5f6   clauderiks:api  Up 2 hours</span>');
  } else if(sub === 'build'){
    termPrintLine('<span class="term-out">Successfully built a1b2c3d4e5f6</span>');
  } else if(sub === 'compose'){
    termPrintLine('<span class="term-out">Creating clauderiks_api_1 ... done</span>');
    termPrintLine('<span class="term-out">Creating clauderiks_db_1  ... done</span>');
  } else {
    termPrintLine('<span class="term-out">docker: mô phỏng lệnh "' + escapeHtml(args.join(' ')) + '"</span>');
  }
}

function handleTermKeydown(e){
  const input = e.target;
  if(e.key === 'Enter'){
    simulateCommand(input.value);
    input.value = '';
  } else if(e.key === 'ArrowUp'){
    e.preventDefault();
    if(state.terminalHistoryIndex > 0){
      state.terminalHistoryIndex--;
      input.value = state.terminalHistory[state.terminalHistoryIndex] || '';
    }
  } else if(e.key === 'ArrowDown'){
    e.preventDefault();
    if(state.terminalHistoryIndex < state.terminalHistory.length - 1){
      state.terminalHistoryIndex++;
      input.value = state.terminalHistory[state.terminalHistoryIndex] || '';
    } else {
      state.terminalHistoryIndex = state.terminalHistory.length;
      input.value = '';
    }
  }
}

/* click anywhere in terminal window focuses the input */
document.addEventListener('DOMContentLoaded', () => {
  const win = document.querySelector('.terminal-window');
  if(win){
    win.addEventListener('click', () => {
      const input = document.getElementById('term-input');
      if(input) input.focus();
    });
  }
});

/* ============================================================
   AI ASSISTANT — chat simulation
   ============================================================ */
const aiResponses = {
  default: "Mình đã ghi nhận câu hỏi của bạn. Trong môi trường demo này, các câu trả lời được mô phỏng sẵn nhằm minh hoạ giao diện Chat UI — bao gồm bong bóng tin nhắn, hiệu ứng đang nhập, và gợi ý theo ngữ cảnh.",
  webhook: "Để tạo webhook mới, vào phần Settings của repository, chọn 'Webhooks' → 'Add webhook', sau đó nhập URL endpoint và chọn các sự kiện bạn muốn lắng nghe như push, pull_request, hoặc release.",
  grpc: "REST sử dụng HTTP/1.1 với JSON, dễ đọc và debug nhưng nặng hơn. gRPC dùng HTTP/2 với Protocol Buffers, nhanh hơn và hỗ trợ streaming hai chiều, phù hợp cho giao tiếp nội bộ giữa các service.",
  jwt: "Đây là ví dụ xác thực JWT cơ bản bằng Node.js sử dụng thư viện jsonwebtoken: tạo token với secret key, đính kèm payload chứa userId, và đặt thời gian hết hạn phù hợp cho access token."
};

function autoGrow(el){
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 140) + 'px';
}

function handleAiKeydown(e){
  if(e.key === 'Enter' && !e.shiftKey){
    e.preventDefault();
    sendAiMessage();
  }
}

function appendAiMessage(role, htmlContent){
  const messages = document.getElementById('ai-messages');
  const row = document.createElement('div');
  row.className = 'ai-msg-row ' + role;
  const avatarLabel = role === 'user' ? 'NV' : 'CR';
  const nameLabel = role === 'user' ? 'Bạn' : 'ClaudeRiks Assistant';
  row.innerHTML =
    '<div class="ai-avatar ' + role + '">' + avatarLabel + '</div>' +
    '<div class="ai-msg-content"><div class="ai-msg-name">' + nameLabel + '</div><div class="ai-msg-text">' + htmlContent + '</div></div>';
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
  return row;
}

function sendSuggestion(text){
  document.getElementById('ai-input').value = text;
  sendAiMessage();
}

function pickAiResponse(userText){
  const lower = userText.toLowerCase();
  if(lower.includes('webhook')) return aiResponses.webhook;
  if(lower.includes('grpc') || lower.includes('rest')) return aiResponses.grpc;
  if(lower.includes('jwt') || lower.includes('xác thực')) return aiResponses.jwt;
  return aiResponses.default;
}

function sendAiMessage(){
  const input = document.getElementById('ai-input');
  const text = input.value.trim();
  if(text === '') return;

  appendAiMessage('user', '<p>' + escapeHtml(text) + '</p>');
  input.value = '';
  autoGrow(input);

  const typingRow = appendAiMessage('assistant', '<div class="typing-dots"><span></span><span></span><span></span></div>');

  setTimeout(() => {
    typingRow.remove();
    const responseText = pickAiResponse(text);
    appendAiMessage('assistant', '<p>' + escapeHtml(responseText) + '</p>');
  }, 1100);
}

function newAiChat(){
  document.getElementById('ai-messages').innerHTML =
    '<div class="ai-msg-row assistant"><div class="ai-avatar assistant">CR</div>' +
    '<div class="ai-msg-content"><div class="ai-msg-name">ClaudeRiks Assistant</div>' +
    '<div class="ai-msg-text"><p>Cuộc trò chuyện mới đã bắt đầu. Bạn cần hỗ trợ gì?</p></div></div></div>';
  showToast('success', 'Đã tạo cuộc trò chuyện mới');
}

/* ============================================================
   SEARCH VIEW
   ============================================================ */
const searchIndex = [
  { scope:'docs', title:'Bắt đầu nhanh', path:'/docs/quickstart', snippet:'Tạo dự án mới chỉ với 3 bước đơn giản: khởi tạo, cấu hình, và chạy.' },
  { scope:'docs', title:'Cài đặt', path:'/docs/install', snippet:'Cài đặt ClaudeRiks CLI thông qua npm hoặc yarn global.' },
  { scope:'docs', title:'Định tuyến', path:'/docs/routing', snippet:'Hệ thống định tuyến hỗ trợ file-based routing tương tự Next.js.' },
  { scope:'api', title:'GET /users', path:'/api/users', snippet:'Trả về danh sách người dùng có phân trang theo page và limit.' },
  { scope:'api', title:'POST /repos', path:'/api/repos', snippet:'Khởi tạo một kho lưu trữ Git mới gắn với tổ chức hiện tại.' },
  { scope:'file', title:'Sidebar.js', path:'/src/components/Sidebar.js', snippet:'Thanh điều hướng bên trái, giống VS Code activity bar.' },
  { scope:'file', title:'client.js', path:'/src/api/client.js', snippet:'Cấu hình timeout mặc định và retry cho HTTP client.' },
  { scope:'wiki', title:'Kiến trúc hệ thống', path:'/wiki/architecture', snippet:'Mô hình microservice, tách biệt API Gateway và các dịch vụ nội bộ.' },
  { scope:'wiki', title:'Chiến lược Cache', path:'/wiki/cache', snippet:'Cache Layer dùng chiến lược write-through cho dữ liệu người dùng.' }
];

function setSearchScope(el, scope){
  document.querySelectorAll('#view-search .filter-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  state.searchScope = scope;
  doSearch(document.getElementById('search-input').value);
}

function doSearch(query){
  const container = document.getElementById('search-results');
  const q = query.trim().toLowerCase();
  if(q === ''){
    container.innerHTML = '<div class="search-empty">Nhập từ khoá để bắt đầu tìm kiếm trên toàn bộ hệ thống.</div>';
    return;
  }
  let results = searchIndex.filter(item => {
    const scopeMatch = state.searchScope === 'all' || item.scope === state.searchScope;
    const textMatch = (item.title + ' ' + item.snippet).toLowerCase().includes(q);
    return scopeMatch && textMatch;
  });

  if(results.length === 0){
    container.innerHTML = '<div class="search-empty">Không tìm thấy kết quả nào cho "' + escapeHtml(query) + '".</div>';
    return;
  }

  const scopeIcons = { docs:'📘', api:'🔌', file:'📄', wiki:'🗂️' };
  container.innerHTML = results.map(r => {
    const snippet = r.snippet.replace(new RegExp('(' + escapeRegex(query) + ')', 'ig'), '<mark>$1</mark>');
    return '<div class="search-result-item">' +
      '<div class="sr-top"><span>' + scopeIcons[r.scope] + '</span><span class="sr-title">' + r.title + '</span><span class="sr-path">' + r.path + '</span></div>' +
      '<div class="sr-snippet">' + snippet + '</div></div>';
  }).join('');
}

function escapeRegex(str){
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/* ============================================================
   GIT VIEW — button actions
   ============================================================ */
function gitAction(action){
  const log = document.getElementById('git-log-list');
  const time = new Date().toLocaleTimeString('vi-VN');
  const messages = {
    pull: 'Đã pull thành công từ origin/main (0 thay đổi mới)',
    push: 'Đã push 3 commit lên origin/main',
    commit: 'Đã commit thay đổi: "chore: cập nhật cấu hình timeout"',
    merge: 'Đã merge nhánh feature/api-v2 vào develop',
    release: 'Đã phát hành phiên bản mới v3.4.1'
  };
  const line = document.createElement('div');
  line.textContent = '[' + time + '] $ git ' + action + ' → ' + messages[action];
  log.appendChild(line);
  log.scrollTop = log.scrollHeight;

  const toastType = action === 'release' ? 'success' : 'info';
  showToast(toastType, messages[action]);
}

/* ============================================================
   SETTINGS — panel switching
   ============================================================ */
function switchSettingsPanel(el, panelId){
  document.querySelectorAll('.settings-nav-item').forEach(i => i.classList.remove('active'));
  document.querySelectorAll('.settings-panel').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('settings-' + panelId).classList.add('active');
}

/* theme swatch selection */
document.addEventListener('click', function(e){
  if(e.target.classList && e.target.classList.contains('theme-swatch')){
    document.querySelectorAll('.theme-swatch').forEach(s => s.classList.remove('selected'));
    e.target.classList.add('selected');
    showToast('success', 'Đã áp dụng chủ đề màu mới');
  }
});

/* ============================================================
   WIKI — Table of contents scroll sync
   ============================================================ */
window.addEventListener('DOMContentLoaded', () => {
  const wikiMain = document.querySelector('.wiki-main');
  const tocLinks = document.querySelectorAll('.wiki-toc a');
  if(!wikiMain) return;

  tocLinks.forEach(link => {
    link.addEventListener('click', function(e){
      e.preventDefault();
      const id = this.getAttribute('href').replace('#','');
      const target = document.getElementById(id);
      if(target){
        wikiMain.scrollTo({ top: target.offsetTop - 20, behavior:'smooth' });
      }
      tocLinks.forEach(l => l.classList.remove('active'));
      this.classList.add('active');
    });
  });

  wikiMain.addEventListener('scroll', () => {
    const headings = document.querySelectorAll('.wiki-main h2[id]');
    let currentId = null;
    headings.forEach(h => {
      if(h.offsetTop - 40 <= wikiMain.scrollTop){ currentId = h.id; }
    });
    if(currentId){
      tocLinks.forEach(l => {
        l.classList.toggle('active', l.getAttribute('href') === '#' + currentId);
      });
    }
  });
});

/* ============================================================
   INIT — welcome toast
   ============================================================ */
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => showToast('success', 'Chào mừng bạn quay trở lại ClaudeRiks!'), 500);
});

</script>
</body>
</html>