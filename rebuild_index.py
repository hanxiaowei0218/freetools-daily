# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"C:\Users\15166\Documents\Codex\2026-06-14\codex-codex\aitoolbox")
index_path = ROOT / "index.html"

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI工具箱 - 每日一个免费在线小工具</title>
<meta name="description" content="每天自动生成一个实用的在线工具，免费、无需下载、即开即用。">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧰</text></svg>">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3843355642836530" crossorigin="anonymous"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#f8fafc;--card:#fff;--text:#1e293b;--muted:#64748b;--accent:#6366f1;--border:#e2e8f0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
header{padding:60px 0 40px;text-align:center}
header h1{font-size:2.5rem;font-weight:800;background:linear-gradient(135deg,var(--accent),#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
header p{color:var(--muted);font-size:1.1rem;margin-top:8px}
.stats{display:flex;justify-content:center;gap:40px;margin-top:24px}
.stat{text-align:center}
.stat-num{font-size:2rem;font-weight:700;color:var(--accent)}
.stat-label{font-size:.85rem;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;padding:20px 0 60px}
.card{background:var(--card);border-radius:16px;padding:28px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid var(--border);transition:transform .2s,box-shadow .2s;text-decoration:none;color:inherit;display:block}
.card:hover{transform:translateY(-4px);box-shadow:0 12px 40px rgba(99,102,241,.12)}
.card-icon{font-size:2.5rem;margin-bottom:12px}
.card h2{font-size:1.2rem;margin-bottom:6px}
.card p{color:var(--muted);font-size:.9rem;line-height:1.5}
footer{text-align:center;padding:40px 0;color:var(--muted);font-size:.85rem;border-top:1px solid var(--border)}
footer a{color:var(--accent);text-decoration:none}
@media(max-width:640px){header h1{font-size:1.8rem}.grid{grid-template-columns:1fr}.stats{gap:24px}}
</style>
</head>
<body>
<div class="container">
<header>
<h1>🛠️ AI工具箱</h1>
<p>每天自动生成一个实用在线工具 · 完全免费 · 无需下载</p>
<div class="stats">
<div class="stat"><div class="stat-num" id="tool-count">29</div><div class="stat-label">在线工具</div></div>
<div class="stat"><div class="stat-num">100%</div><div class="stat-label">免费使用</div></div>
<div class="stat"><div class="stat-num">本地</div><div class="stat-label">数据处理</div></div>
</div>
</header>

<div class="grid" id="tools-grid">

"""

tools_data = """image-compressor|图片压缩工具|🗜️|在线压缩PNG/JPEG图片，实时预览，浏览器本地处理。
qr-generator|二维码生成器|📱|输入文字或链接，一键生成二维码图片并下载。
password-generator|随机密码生成器|🔐|自定义长度和字符类型，一键生成高强度随机密码。
text-counter|字数统计器|📝|实时统计中英文字数、字符数、段落数、阅读时间。
json-formatter|JSON 格式化工具|📋|在线格式化、压缩、验证JSON数据，语法高亮。
base64-encoder|Base64 编解码|🔢|在线Base64编码/解码，支持文本和文件。
color-palette|调色板生成器|🎨|随机生成美观配色方案，一键复制色号。
url-encoder|URL 编解码|🔗|URL编码/解码，参数解析，开发者必备。
timestamp-converter|时间戳转换器|⏰|Unix时间戳与日期互转，支持多时区。
uuid-generator|UUID 生成器|🆔|生成UUID v4，支持批量生成。
lorem-ipsum|Lorem Ipsum 生成器|📄|生成中英文占位文本，自定义段落数。
case-converter|大小写转换器|🔤|一键转换大小写、驼峰、下划线等格式。
percentage-calc|百分比计算器|💯|快速计算百分比、折扣、涨跌幅。
random-number|随机数生成器|🎲|自定义范围生成随机数，可批量可去重。
stopwatch|在线秒表|⏱️|精准在线秒表，支持计次和倒计时。
gradient-generator|CSS 渐变生成器|🌈|可视化创建CSS渐变色，一键复制代码。
emoji-search|Emoji 搜索器|🔎|按关键词搜索Emoji，一键复制。
unit-converter|单位换算器|📐|长度/重量/温度/面积/速度在线换算。
csv-to-json|CSV 转 JSON|📊|CSV和JSON格式互转，支持自定义分隔符。
cron-parser|Cron 表达式解析|🕐|解析Cron定时表达式，显示下次执行时间。
markdown-preview|Markdown 预览器|📖|实时编辑和预览Markdown，支持多种语法。
html-entity|HTML 实体转义|🏷️|HTML特殊字符编码/解码，防XSS注入。
regex-tester|正则表达式测试|🔍|在线测试正则表达式，实时高亮匹配。
ip-lookup|IP 地址查询|🌍|查询IP归属地、运营商信息。
user-agent|User-Agent 解析器|🖥️|解析浏览器UA，显示设备和系统信息。
diff-checker|文本差异对比|↔️|对比两段文本差异，高亮增删改。
barcode-generator|条形码生成器|📊|在线生成条形码并下载PNG图片。
image-cropper|图片裁剪工具|✂️|在线裁剪图片，自定义宽高。
meme-generator|表情包生成器|😂|上传图片，添加文字，一键生成表情包。"""

for line in tools_data.strip().split("\n"):
    slug, name, icon, desc = line.split("|")
    html += f'<div class="tool-card">\n<a class="card" href="/tools/{slug}">\n<div class="card-icon">{icon}</div>\n<h2>{name}</h2>\n<p>{desc}</p>\n</a>\n</div>\n\n'

html += """</div>
</div>

<div style="max-width:1100px;margin:0 auto 20px;padding:0 20px">
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3843355642836530" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>

<footer>
<p>🛠️ AI工具箱 · 每日自动更新 · 数据不上传服务器 · <a href="/sitemap.xml">站点地图</a></p>
</footer>
</body>
</html>"""

index_path.write_text(html, encoding="utf-8")
print("DONE")
