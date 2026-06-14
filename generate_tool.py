#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI工具箱 - 每日自动生成工具脚本
每天运行一次，自动创建新工具页面并更新首页。
用法: python generate_tool.py
"""

import os, sys, json, random, re, datetime
from pathlib import Path

ROOT = Path(__file__).parent.absolute()
TOOLS_DIR = ROOT / "tools"

# ============================================================
# 工具库（按发布顺序排列）
# slug: URL路径  name: 名称  icon: 图标  desc: 描述
# 每个工具可选 html 字段提供完整 HTML，否则自动生成占位页面
# ============================================================
TOOLS = [
    {
        "slug": "image-compressor",
        "name": "图片压缩工具",
        "icon": "🗜️",
        "desc": "在线压缩PNG/JPEG图片，实时预览，浏览器本地处理。",
        "html_file": "image-compressor/index.html"
    },
    {
        "slug": "qr-generator",
        "name": "二维码生成器",
        "icon": "📱",
        "desc": "输入文字或链接，一键生成二维码图片并下载。",
    },
    {
        "slug": "color-palette",
        "name": "调色板生成器",
        "icon": "🎨",
        "desc": "随机生成美观的配色方案，一键复制色号。",
    },
    {
        "slug": "password-generator",
        "name": "随机密码生成器",
        "icon": "🔐",
        "desc": "自定义长度和字符类型，生成高强度随机密码。",
    },
    {
        "slug": "text-counter",
        "name": "字数统计器",
        "icon": "📝",
        "desc": "实时统计中英文字数、字符数、段落数。",
    },
    {
        "slug": "base64-encoder",
        "name": "Base64 编解码",
        "icon": "🔢",
        "desc": "在线 Base64 编码/解码，支持文本和文件。",
    },
    {
        "slug": "json-formatter",
        "name": "JSON 格式化",
        "icon": "📋",
        "desc": "一键格式化/压缩 JSON，语法高亮，错误提示。",
    },
    {
        "slug": "md5-generator",
        "name": "MD5/SHA 哈希计算",
        "icon": "🔒",
        "desc": "在线计算文本的 MD5、SHA1、SHA256 哈希值。",
    },
    {
        "slug": "url-encoder",
        "name": "URL 编解码",
        "icon": "🔗",
        "desc": "URL 编码/解码，参数解析，开发者必备。",
    },
    {
        "slug": "timestamp-converter",
        "name": "时间戳转换器",
        "icon": "⏰",
        "desc": "Unix 时间戳与日期互转，支持多时区。",
    },
    {
        "slug": "regex-tester",
        "name": "正则表达式测试",
        "icon": "🔍",
        "desc": "在线测试正则表达式，实时匹配结果。",
    },
    {
        "slug": "image-cropper",
        "name": "图片裁剪工具",
        "icon": "✂️",
        "desc": "在线裁剪图片，自定义宽高，保持比例。",
    },
    {
        "slug": "meme-generator",
        "name": "表情包生成器",
        "icon": "😂",
        "desc": "上传图片，添加文字，一键生成表情包。",
    },
    {
        "slug": "gradient-generator",
        "name": "CSS 渐变生成器",
        "icon": "🌈",
        "desc": "可视化创建 CSS 渐变，实时预览，一键复制。",
    },
    {
        "slug": "uuid-generator",
        "name": "UUID 生成器",
        "icon": "🆔",
        "desc": "生成 UUID v1/v4，支持批量生成。",
    },
    {
        "slug": "lorem-ipsum",
        "name": "Lorem Ipsum 生成器",
        "icon": "📄",
        "desc": "生成指定长度的占位文本，中文/英文可选。",
    },
    {
        "slug": "emoji-search",
        "name": "Emoji 搜索器",
        "icon": "🔎",
        "desc": "按关键词搜索 Emoji，一键复制，海量表情。",
    },
    {
        "slug": "unit-converter",
        "name": "单位换算器",
        "icon": "📐",
        "desc": "长度/重量/温度/面积单位换算，即开即用。",
    },
    {
        "slug": "percentage-calc",
        "name": "百分比计算器",
        "icon": "💯",
        "desc": "快速计算百分比、折扣、涨跌幅。",
    },
    {
        "slug": "stopwatch",
        "name": "在线秒表",
        "icon": "⏱️",
        "desc": "精准在线秒表，支持计次和倒计时。",
    },
    {
        "slug": "random-number",
        "name": "随机数生成器",
        "icon": "🎲",
        "desc": "自定义范围生成随机数，可批量、可去重。",
    },
    {
        "slug": "case-converter",
        "name": "大小写转换器",
        "icon": "🔤",
        "desc": "一键转换英文大小写、驼峰、下划线等。",
    },
    {
        "slug": "markdown-preview",
        "name": "Markdown 预览器",
        "icon": "📖",
        "desc": "实时编辑和预览 Markdown，支持导出 HTML。",
    },
    {
        "slug": "html-entity",
        "name": "HTML 实体转义",
        "icon": "🏷️",
        "desc": "HTML 特殊字符编码/解码，防止 XSS 注入。",
    },
    {
        "slug": "ip-lookup",
        "name": "IP 地址查询",
        "icon": "🌍",
        "desc": "查询 IP 地址的归属地、运营商信息。",
    },
    {
        "slug": "user-agent",
        "name": "User-Agent 解析器",
        "icon": "🖥️",
        "desc": "解析浏览器 User-Agent 字符串，显示设备信息。",
    },
    {
        "slug": "csv-to-json",
        "name": "CSV 转 JSON",
        "icon": "📊",
        "desc": "CSV 和 JSON 格式互转，支持自定义分隔符。",
    },
    {
        "slug": "cron-parser",
        "name": "Cron 表达式解析",
        "icon": "🕐",
        "desc": "解析 Cron 定时表达式，显示下次执行时间。",
    },
    {
        "slug": "diff-checker",
        "name": "文本差异对比",
        "icon": "↔️",
        "desc": "对比两段文本的差异，高亮显示增删改。",
    },
    {
        "slug": "barcode-generator",
        "name": "条形码生成器",
        "icon": "📊",
        "desc": "在线生成 EAN-13/Code-128 条形码并下载。",
    },
]

def get_next_tool_index():
    """找到下一个尚未创建的工具索引"""
    for i, tool in enumerate(TOOLS):
        tool_dir = TOOLS_DIR / tool["slug"]
        if not (tool_dir / "index.html").exists():
            return i
    return len(TOOLS)

def generate_tool_page(tool_meta):
    """生成工具完整 HTML 页面"""
    name = tool_meta["name"]
    icon = tool_meta["icon"]
    desc = tool_meta["desc"]

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} - AI工具箱</title>
<meta name="description" content="{desc} 完全免费，浏览器本地处理，无需下载。">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f8fafc;color:#1e293b;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px}}
.container{{max-width:600px;width:100%;text-align:center}}
.back{{display:inline-flex;align-items:center;gap:6px;color:#6366f1;text-decoration:none;font-size:.9rem;margin-bottom:30px;align-self:flex-start}}
.back:hover{{text-decoration:underline}}
.icon{{font-size:4rem;margin-bottom:16px}}
h1{{font-size:2rem;font-weight:800;margin-bottom:8px}}
.desc{{color:#64748b;margin-bottom:32px}}
.placeholder{{background:#fff;border-radius:16px;padding:48px;border:1px solid #e2e8f0;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
.placeholder p{{color:#64748b;font-size:1.1rem}}
.loading{{display:inline-block;width:20px;height:20px;border:3px solid #e2e8f0;border-top-color:#6366f1;border-radius:50%;animation:spin .8s linear infinite;margin-right:8px;vertical-align:middle}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
footer{{margin-top:40px;color:#94a3b8;font-size:.85rem}}
footer a{{color:#6366f1;text-decoration:none}}
</style>
</head>
<body>
<a class="back" href="/">← 返回工具箱</a>
<div class="container">
<div class="icon">{icon}</div>
<h1>{name}</h1>
<p class="desc">{desc}</p>
<div class="placeholder">
<p><span class="loading"></span> 工具功能即将上线...</p>
<p style="margin-top:12px;font-size:.9rem;color:#94a3b8">正在由 AI 自动开发完整功能</p>
</div>
</div>
<footer><p>🛠️ <a href="/">AI工具箱</a> · 每日自动更新</p></footer>
</body>
</html>'''

def update_index_html(new_card_html):
    """在首页插入新工具卡片"""
    index_path = ROOT / "index.html"
    content = index_path.read_text(encoding="utf-8")

    # Remove old "今日新增" badges
    content = re.sub(r'<span class="badge">🆕 今日新增</span>', '', content)
    
    # Find the tools-grid closing and insert new card before it
    # Look for: </div>\n</div>\n\n<footer>
    marker = content.index('</div>\n</div>\n\n<footer>')
    # Find the position right after the last card's closing </a>
    # Search backwards from marker for the last </a> inside the grid
    grid_section = content[:marker]
    last_card_end = grid_section.rfind('</a>')
    if last_card_end == -1:
        last_card_end = grid_section.rfind('</div>')  # fallback

    insert_pos = last_card_end + 5  # after '</a>\n'

    new_content = content[:insert_pos] + '\n' + new_card_html + '\n' + content[insert_pos:]

    # Update tool count
    count = len([d for d in TOOLS_DIR.iterdir() if d.is_dir()])
    new_content = re.sub(
        r'(<div class="stat-num" id="tool-count">)\\d+(</div>)',
        rf'\\g<1>{count}\\g<2>',
        new_content
    )

    index_path.write_text(new_content, encoding="utf-8")

def update_sitemap():
    """更新 sitemap.xml"""
    tools = [d.name for d in sorted(TOOLS_DIR.iterdir()) if d.is_dir()]
    urls = ["https://freetools-daily.vercel.app/"]
    for t in tools:
        urls.append(f"https://freetools-daily.vercel.app/tools/{t}")
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    today = datetime.date.today().isoformat()
    for url in urls:
        xml += '  <url>\n'
        xml += f'    <loc>{url}</loc>\n'
        xml += f'    <lastmod>{today}</lastmod>\n'
        xml += '    <changefreq>weekly</changefreq>\n'
        xml += '    <priority>0.8</priority>\n'
        xml += '  </url>\n'
    xml += '</urlset>\n'
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")

def generate_card_html(tool_meta):
    """生成首页工具卡片 HTML"""
    return f'''<div class="tool-card">
<a class="card" href="/tools/{tool_meta["slug"]}">
<div class="card-icon">{tool_meta["icon"]}</div>
<h2>{tool_meta["name"]}</h2>
<p>{tool_meta["desc"]}</p>
<span class="badge">🆕 今日新增</span>
</a>
</div>'''

def main():
    try:
        idx = get_next_tool_index()
    except Exception as e:
        print(f"ERROR finding next tool: {e}")
        sys.exit(1)

    if idx >= len(TOOLS):
        print(f"WARNING: Tool library exhausted! {len(TOOLS)} tools defined, all created.")
        print("Add more tools to the TOOLS list in generate_tool.py and run again.")
        sys.exit(1)

    tool = TOOLS[idx]
    print(f"Today's tool: {tool['icon']} {tool['name']}")
    print(f"  Path: /tools/{tool['slug']}")

    # Create tool directory
    tool_dir = TOOLS_DIR / tool["slug"]
    tool_dir.mkdir(parents=True, exist_ok=True)

    # Generate tool page
    html = generate_tool_page(tool)
    (tool_dir / "index.html").write_text(html, encoding="utf-8")

    # Update homepage
    card_html = generate_card_html(tool)
    update_index_html(card_html)

    # Update sitemap
    update_sitemap()

    count = len([d for d in TOOLS_DIR.iterdir() if d.is_dir()])
    print(f"DONE! Toolbox now has {count} tools.")
    next_idx = idx + 1
    if next_idx < len(TOOLS):
        print(f"Tomorrow: {TOOLS[next_idx]['icon']} {TOOLS[next_idx]['name']}")
    else:
        print("No more tools defined. Add more to the TOOLS list!")

if __name__ == "__main__":
    main()
