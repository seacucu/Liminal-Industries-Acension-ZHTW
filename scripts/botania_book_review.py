"""產生辭典內文改寫的查驗頁（自包含 HTML，可搜尋／篩選）。

資料來自 botania_book.py 寫出的 book-changes.json，所以要先跑過那支。
輸出：_workspace/reference/botania-book-review.html（工作區，不進版控）
"""

import html
import json
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = os.path.join(ROOT, "translation", "lang", "botania.json")
CHANGES = os.path.join(ROOT, "_workspace", "build", "botania", "book-changes.json")
OUT = os.path.join(ROOT, "_workspace", "reference", "botania-book-review.html")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>植物魔法辭典內文查驗</title>
<style>
  :root {{
    --bg:#0f1115; --card:#171a21; --border:#2a2f3a; --text:#e6e8ec;
    --muted:#9aa3b2; --accent:#6ea8fe; --green:#3ecf8e; --yellow:#e6c35c;
  }}
  *{{box-sizing:border-box}}
  body{{margin:0;font-family:"Segoe UI","Noto Sans TC","Microsoft JhengHei",sans-serif;
       background:var(--bg);color:var(--text);line-height:1.6}}
  header{{padding:1.5rem 1.25rem 1rem;border-bottom:1px solid var(--border)}}
  h1{{margin:0 0 .35rem;font-size:1.45rem}}
  .meta{{color:var(--muted);font-size:.9rem}}
  main{{padding:1.25rem;max-width:1200px;margin:0 auto}}
  .summary{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
           gap:.75rem;margin-bottom:1.25rem}}
  .summary .card{{background:var(--card);border:1px solid var(--border);
                 border-radius:10px;padding:.9rem 1rem}}
  .summary .num{{font-size:1.6rem;font-weight:700}}
  .summary .label{{color:var(--muted);font-size:.82rem}}
  .controls{{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1rem;align-items:center}}
  input[type=search]{{background:var(--card);border:1px solid var(--border);
    color:var(--text);border-radius:8px;padding:.55rem .75rem;font-size:.92rem;
    min-width:260px;flex:1}}
  .chip{{display:inline-flex;align-items:center;gap:.35rem;border:1px solid var(--border);
    background:var(--card);color:var(--muted);border-radius:999px;padding:.35rem .7rem;
    font-size:.82rem;cursor:pointer;user-select:none}}
  .chip.active{{border-color:var(--accent);color:var(--text);background:#1a2436}}
  .row{{background:var(--card);border:1px solid var(--border);border-radius:10px;
       padding:.85rem 1rem;margin-bottom:.7rem}}
  .spot{{font-size:.95rem;font-weight:600}}
  .key{{font-family:ui-monospace,Consolas,monospace;font-size:.75rem;color:var(--muted)}}
  .tag{{font-size:.72rem;color:var(--muted);border:1px solid var(--border);
       border-radius:999px;padding:.05rem .5rem;margin-left:.4rem}}
  .en{{color:var(--muted);font-size:.85rem;margin:.4rem 0}}
  .old{{color:#a9707a;font-size:.9rem}}
  .new{{color:var(--green);font-size:.95rem}}
  code{{background:#0b0d11;border-radius:4px;padding:0 .2rem;font-size:.85em;color:var(--yellow)}}
</style>
</head>
<body>
<header>
  <h1>植物魔法辭典內文查驗</h1>
  <div class="meta">botania_book.py 改寫過的每一條，附書中位置與 Botania 英文原文對照。
  人工重譯的排在最前面，那些是整段重寫的，最需要進遊戲確認沒有被書頁裁掉。</div>
</header>
<main>
  <div class="summary">{cards}</div>
  <div class="controls">
    <input type="search" id="q" placeholder="搜尋鍵名或內文…">
    <span class="chip active" data-f="all">全部</span>
    <span class="chip" data-f="manual">人工重譯</span>
    <span class="chip" data-f="link">補回連結</span>
  </div>
  <div id="list">{rows}</div>
</main>
<script>
const rows=[...document.querySelectorAll('.row')];
let filter='all', q='';
function apply(){{
  rows.forEach(r=>{{
    const okF = filter==='all' || r.dataset[filter]==='1';
    const okQ = !q || r.textContent.toLowerCase().includes(q);
    r.style.display = (okF&&okQ) ? '' : 'none';
  }});
}}
document.getElementById('q').addEventListener('input',e=>{{q=e.target.value.toLowerCase();apply();}});
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>{{
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('active'));
  c.classList.add('active'); filter=c.dataset.f; apply();
}}));
</script>
</body>
</html>
"""


def locate(z, lang):
    """鍵 → 這條字在書裡的哪一章、哪一個條目、第幾頁。

    辭典的 book.json 設了 i18n:true，條目檔裡放的是語系鍵，所以直接對得起來。
    有了位置才有辦法拿著清單進遊戲翻，不然只有一堆 botania.page.xxx。
    """
    # 分類的檔名（generating_flowers）和它的語系鍵（generationFlowers）對不起來，
    # 所以先讀分類檔把兩者接上，不要自己猜。
    cats = {}
    for name in z.namelist():
        if "/lexicon/en_us/categories/" in name and name.endswith(".json"):
            data = json.loads(z.read(name).decode("utf-8"))
            cats[name.split("/")[-1][:-5]] = lang.get(data["name"], data["name"])

    where = {}
    for name in z.namelist():
        if "/lexicon/en_us/entries/" not in name or not name.endswith(".json"):
            continue
        entry = json.loads(z.read(name).decode("utf-8"))
        cat = entry.get("category", "").split(":")[-1]
        cat_zh = cats.get(cat, cat)
        entry_zh = lang.get(entry["name"], entry["name"])
        where[entry["name"]] = (cat_zh, entry_zh, None)
        for i, page in enumerate(entry.get("pages", []), 1):
            for field in ("text", "title", "caption"):
                key = page.get(field)
                if isinstance(key, str) and key.startswith("botania."):
                    where.setdefault(key, (cat_zh, entry_zh, i))
    return where


def esc(s):
    s = html.escape(s or "")
    return re.sub(r"(\$\([^)]*\))", r"<code>\1</code>", s)


def main():
    data = json.load(open(CHANGES, encoding="utf-8"))
    changes = data["改寫"]
    lang = json.load(open(LANG, encoding="utf-8"))
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))
        where = locate(z, lang)

    # 人工重譯的排最前面：那些是整段重寫的，字數變了，最可能被書頁裁掉
    def order(item):
        k, v = item
        return (0 if v.get("手動") else 1, where.get(k, ("", "", 0))[:2], k)

    rows, manual, linked = [], 0, 0
    for k, v in sorted(changes.items(), key=order):
        is_manual = "1" if v.get("手動") else "0"
        manual += v.get("手動") is True
        has_link = "1" if "$(l:" in v["後"] and "$(l:" not in v["前"] else "0"
        linked += has_link == "1"
        tag = '<span class="tag">人工重譯</span>' if is_manual == "1" else ""
        cat, entry, page = where.get(k, ("？", "書外的字串", None))
        spot = f"{cat} › {entry}" + (f" › 第 {page} 頁" if page else "")
        rows.append(
            f'<div class="row" data-manual="{is_manual}" data-link="{has_link}">'
            f'<div><span class="spot">{html.escape(spot)}</span>{tag}</div>'
            f'<div><span class="key">{html.escape(k)}</span></div>'
            f'<div class="en">EN　{esc(en.get(k, ""))}</div>'
            f'<div class="old">舊　{esc(v["前"])}</div>'
            f'<div class="new">新　{esc(v["後"])}</div>'
            f"</div>")

    cards = "".join(
        f'<div class="card"><div class="num">{n}</div><div class="label">{lab}</div></div>'
        for n, lab in [(len(changes), "改寫的條目"), (manual, "人工重譯"),
                       (linked, "補回連結的頁"),
                       (len(data["未解出的詞"]), "未解出的詞"),
                       (len(data["分段對不上"]), "分段對不上")])

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(
        TEMPLATE.format(cards=cards, rows="".join(rows)))
    print(f"  {len(rows)} 條 → {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
