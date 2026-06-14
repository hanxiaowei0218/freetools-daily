import sys; sys.path.insert(0, r"C:\Users\15166\Documents\Codex\2026-06-14\codex-codex\aitoolbox")
exec(open(r"C:\Users\15166\Documents\Codex\2026-06-14\codex-codex\aitoolbox\tool_base.py", encoding="utf-8-sig").read())

# UUID Generator
W("uuid-generator", "UUID 生成器", "在线生成UUID v4，支持批量生成。", "🆔", "UUID 生成器",
'<div class="card"><button class="btn btn-primary" onclick="gen()" style="width:100%;margin-bottom:12px">🔄 生成 UUID v4</button><div class="result" id="r"><button class="copy-btn" onclick="copy(this,r.innerText.trim())">📋 复制</button>点击按钮生成</div><button class="btn btn-outline" onclick="genBatch()" style="width:100%;margin-top:12px">📦 批量生成 10 个</button></div><script>function uuid(){return"xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,function(c){var r=Math.random()*16|0;return(c=="x"?r:r&0x3|0x8).toString(16)})}function gen(){r.innerHTML="<button class=copy-btn onclick=\\"copy(this,r.innerText.trim())\\">📋 复制</button>"+uuid()}function genBatch(){r.innerHTML="<button class=copy-btn onclick=\\"copy(this,r.innerText.trim())\\">📋 复制</button>"+Array.from({length:10},uuid).join("\\n")}gen();function copy(btn,t){navigator.clipboard.writeText(t);btn.textContent="✅ 已复制";setTimeout(function(){btn.textContent="📋 复制"},1500)}</script>')

print("uuid-generator done")
