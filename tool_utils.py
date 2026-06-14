from pathlib import Path

ROOT = Path(r"C:\Users\15166\Documents\Codex\2026-06-14\codex-codex\aitoolbox")
TOOLS_DIR = ROOT / "tools"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3843355642836530" crossorigin="anonymous"></script>'
BASE_CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}:root{--bg:#f8fafc;--card:#fff;--text:#1e293b;--muted:#64748b;--accent:#6366f1;--border:#e2e8f0}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);min-height:100vh}.container{max-width:700px;margin:0 auto;padding:30px 20px}.back{display:inline-flex;align-items:center;gap:6px;color:var(--accent);text-decoration:none;font-size:.9rem;margin-bottom:24px}.back:hover{text-decoration:underline}header{text-align:center;margin-bottom:30px}header .icon{font-size:3rem}header h1{font-size:2rem;font-weight:800;margin:8px 0}header p{color:var(--muted)}.card{background:var(--card);border-radius:16px;padding:28px;border:1px solid var(--border);box-shadow:0 1px 3px rgba(0,0,0,.06);margin-bottom:20px}.btn{padding:10px 20px;border:none;border-radius:10px;font-size:.9rem;font-weight:600;cursor:pointer;transition:all .2s}.btn-primary{background:var(--accent);color:#fff}.btn-primary:hover{background:#4f46e5}.btn-outline{background:#fff;color:var(--accent);border:1px solid var(--accent)}.btn-outline:hover{background:#eef2ff}input,textarea,select{width:100%;border:2px solid var(--border);border-radius:10px;padding:12px;font-size:.95rem;outline:none;transition:border-color .2s;font-family:inherit}input:focus,textarea:focus{border-color:var(--accent)}.result{background:#1e293b;color:#e2e8f0;min-height:80px;border-radius:12px;padding:16px;font-family:'Courier New',monospace;font-size:.85rem;white-space:pre-wrap;word-break:break-all;margin-top:12px;position:relative;overflow:auto;max-height:400px}.copy-btn{position:absolute;top:8px;right:8px;background:rgba(255,255,255,.15);border:none;color:#fff;padding:4px 10px;border-radius:6px;cursor:pointer;font-size:.75rem}.copy-btn:hover{background:rgba(255,255,255,.25)}label{display:block;font-weight:600;margin-bottom:6px;font-size:.9rem}.row{display:flex;gap:12px;align-items:center;margin-bottom:12px}footer{text-align:center;margin-top:40px;padding-top:20px;border-top:1px solid var(--border);color:var(--muted);font-size:.85rem}footer a{color:var(--accent);text-decoration:none}"""
FOOTER_HTML = '<footer><p>🛠️ <a href="/">AI工具箱</a> · 每日自动更新</p></footer>'

def page(title, desc, icon, name, body, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - AI工具箱</title>
<meta name="description" content="{desc}">
{ADSENSE}
<style>{BASE_CSS}{extra_css}</style>
</head>
<body>
<div class="container">
<a class="back" href="/">← 返回工具箱</a>
<header><div class="icon">{icon}</div><h1>{name}</h1><p>{desc}</p></header>
{body}
{FOOTER_HTML}
</div>
</body>
</html>"""

def write(slug, title, desc, icon, name, body, extra_css=""):
    (TOOLS_DIR / slug).mkdir(parents=True, exist_ok=True)
    (TOOLS_DIR / slug / "index.html").write_text(page(title, desc, icon, name, body, extra_css), encoding="utf-8")

print("Functions ready")
