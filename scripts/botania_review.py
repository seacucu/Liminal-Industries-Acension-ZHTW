"""產生 Botania 名稱譯文的查驗頁（自包含 HTML，可搜尋／篩選）。

輸出：_workspace/reference/botania-name-review.html（工作區，不進版控）
"""

import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
LANG = os.path.join(ROOT, "translation", "lang", "botania.json")
OUT = os.path.join(ROOT, "_workspace", "reference", "botania-name-review.html")

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Botania 名稱譯文查驗</title>
<style>
  :root {
    --bg:#0f1115; --card:#171a21; --border:#2a2f3a; --text:#e6e8ec;
    --muted:#9aa3b2; --accent:#6ea8fe; --green:#3ecf8e; --yellow:#e6c35c;
    --orange:#f0a060; --red:#e06c75;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:"Segoe UI","Noto Sans TC","Microsoft JhengHei",sans-serif;
       background:var(--bg);color:var(--text);line-height:1.5}
  header{padding:1.5rem 1.25rem 1rem;border-bottom:1px solid var(--border);
         background:linear-gradient(180deg,#151922,var(--bg))}
  h1{margin:0 0 .35rem;font-size:1.45rem}
  .meta{color:var(--muted);font-size:.9rem}
  main{padding:1.25rem;max-width:1400px;margin:0 auto}
  .summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
           gap:.75rem;margin-bottom:1.25rem}
  .summary .card{background:var(--card);border:1px solid var(--border);
                 border-radius:10px;padding:.9rem 1rem}
  .summary .num{font-size:1.6rem;font-weight:700}
  .summary .label{color:var(--muted);font-size:.82rem}
  .controls{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1rem;align-items:center}
  input[type=search],select{background:var(--card);border:1px solid var(--border);
    color:var(--text);border-radius:8px;padding:.55rem .75rem;font-size:.92rem}
  input[type=search]{min-width:240px;flex:1}
  .chip{display:inline-flex;align-items:center;gap:.35rem;border:1px solid var(--border);
    background:var(--card);color:var(--muted);border-radius:999px;padding:.35rem .7rem;
    font-size:.82rem;cursor:pointer;user-select:none}
  .chip.active{border-color:var(--accent);color:var(--text);background:#1a2436}
  .tablewrap{overflow-x:auto;border:1px solid var(--border);border-radius:10px}
  table{width:100%;border-collapse:collapse;background:var(--card);min-width:860px}
  thead th{text-align:left;padding:.7rem .85rem;background:#1b2030;
    border-bottom:1px solid var(--border);font-size:.82rem;color:var(--muted);white-space:nowrap}
  tbody td{padding:.6rem .85rem;border-bottom:1px solid var(--border);
    vertical-align:top;font-size:.92rem}
  tbody tr:last-child td{border-bottom:none}
  tbody tr:hover{background:#1c2230}
  .key{font-family:ui-monospace,Consolas,monospace;font-size:.78rem;color:var(--muted)}
  .old{color:var(--muted);text-decoration:line-through}
  .none{color:var(--red);font-style:italic}
  .new{color:var(--green);font-weight:600}
  .same{color:var(--text)}
  .badge{display:inline-block;padding:.12rem .45rem;border-radius:6px;font-size:.75rem;
    white-space:nowrap}
  .b-new{background:#1c2f24;color:var(--green)}
  .b-chg{background:#2f2a1a;color:var(--yellow)}
  .b-keep{background:#20242e;color:var(--muted)}
  footer{padding:1.5rem 1.25rem;color:var(--muted);font-size:.85rem;max-width:1400px;margin:0 auto}
  code{background:#1e2430;padding:.1rem .35rem;border-radius:4px}
</style>
</head>
<body>
<header>
  <h1>Botania 名稱譯文查驗</h1>
  <div class="meta">
    範圍：<code>block.botania.*</code> 與 <code>item.botania.*</code> 共 __TOTAL__ 條 ·
    產生於 __DATE__ ·
    術語依據 <code>docs/glossary-botania.md</code>
  </div>
</header>
<main>
  <div class="summary" id="summary"></div>
  <div class="controls">
    <input type="search" id="q" placeholder="搜尋英文、舊譯或新譯…">
    <span class="chip active" data-f="all">全部</span>
    <span class="chip" data-f="new">新譯（原本英文）</span>
    <span class="chip" data-f="chg">已更動</span>
    <span class="chip" data-f="keep">維持原譯</span>
  </div>
  <div class="tablewrap">
    <table>
      <thead><tr>
        <th style="width:90px">狀態</th>
        <th>英文原名</th>
        <th>舊譯</th>
        <th>新譯</th>
        <th style="width:260px">key</th>
      </tr></thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>
</main>
<footer>
  <p>「已更動」代表既有譯文經術語校正或構詞規則改寫；「新譯」代表原本在遊戲內顯示英文。</p>
  <p>此頁由 <code>scripts/botania_review.py</code> 產生，可隨譯文重新產出。</p>
</footer>
<script>
const DATA = __DATA__;
const tbody = document.getElementById('tbody');
const q = document.getElementById('q');
let filter = 'all';

function render() {
  const term = q.value.trim().toLowerCase();
  const rows = DATA.filter(r => {
    if (filter !== 'all' && r.s !== filter) return false;
    if (!term) return true;
    return (r.en + ' ' + (r.old || '') + ' ' + r.new + ' ' + r.k).toLowerCase().includes(term);
  });
  const badge = {new: ['b-new', '新譯'], chg: ['b-chg', '已更動'], keep: ['b-keep', '維持']};
  tbody.innerHTML = rows.map(r => {
    const [cls, label] = badge[r.s];
    const old = r.old === null
      ? '<span class="none">（顯示英文）</span>'
      : (r.s === 'keep' ? '<span class="same">' + esc(r.old) + '</span>'
                        : '<span class="old">' + esc(r.old) + '</span>');
    const nw = r.s === 'keep' ? '<span class="same">' + esc(r.new) + '</span>'
                              : '<span class="new">' + esc(r.new) + '</span>';
    return `<tr><td><span class="badge ${cls}">${label}</span></td>` +
           `<td>${esc(r.en)}</td><td>${old}</td><td>${nw}</td>` +
           `<td class="key">${esc(r.k)}</td></tr>`;
  }).join('');
  document.getElementById('summary').innerHTML = [
    ['總計', DATA.length], ['新譯', DATA.filter(r => r.s === 'new').length],
    ['已更動', DATA.filter(r => r.s === 'chg').length],
    ['維持原譯', DATA.filter(r => r.s === 'keep').length],
    ['目前顯示', rows.length],
  ].map(([l, n]) => `<div class="card"><div class="num">${n}</div><div class="label">${l}</div></div>`).join('');
}
function esc(s) {
  return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
}
q.addEventListener('input', render);
document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
  document.querySelectorAll('.chip').forEach(x => x.classList.remove('active'));
  c.classList.add('active');
  filter = c.dataset.f;
  render();
}));
render();
</script>
</body>
</html>
"""


def main():
    import datetime
    names = json.load(open(NAMES, encoding="utf-8"))
    lang = json.load(open(LANG, encoding="utf-8"))

    rows = []
    for k in sorted(names):
        en, old = names[k]["en"], names[k]["tw"]
        new = lang[k]
        state = "new" if old is None else ("keep" if old == new else "chg")
        rows.append({"k": k, "en": en, "old": old, "new": new, "s": state})

    out = (TEMPLATE
           .replace("__DATA__", json.dumps(rows, ensure_ascii=False))
           .replace("__TOTAL__", str(len(rows)))
           .replace("__DATE__", datetime.date.today().isoformat()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(out)

    from collections import Counter
    c = Counter(r["s"] for r in rows)
    print(f"共 {len(rows)} 條：新譯 {c['new']}、已更動 {c['chg']}、維持原譯 {c['keep']}")
    print(f"寫入 {os.path.relpath(OUT, ROOT)}（{os.path.getsize(OUT)//1024} KB）")


if __name__ == "__main__":
    main()
