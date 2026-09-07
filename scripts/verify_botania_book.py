"""檢查植物魔法辭典內文的結構，把 botania_book.py 該修好的事再驗一次。

分兩種：不通過就算失敗的硬檢查，以及只列出來供人判斷的落差報告。
硬檢查針對「畫出來一定不對」的問題（巨集沒收好、連結指向不存在的條目），
落差報告針對「和英文比起來少了東西」的問題，那多半是譯文照舊版英文寫的，
要人工重譯，不該讓建置失敗。
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = os.path.join(ROOT, "translation", "lang", "botania.json")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

BOOK_PREFIXES = ("botania.page.", "botania.entry.", "botania.tagline.",
                 "botania.category.", "botania.challenge.", "botania.subtitle.",
                 "botania.landing")

MACRO = re.compile(r"\$\([^)]*\)")
CJK = "㐀-鿿"
failures = []


def check(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}：{detail}")
    if not ok:
        failures.append(label)


def show(rows, limit=8):
    for k, v in rows[:limit]:
        print(f"        {k}  {v}")
    if len(rows) > limit:
        print(f"        …另有 {len(rows) - limit} 條")


def main():
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))
        entries = {
            n.split("/entries/")[1][:-5]
            for n in z.namelist()
            if "/lexicon/en_us/entries/" in n and n.endswith(".json")
        }
    tr = json.load(open(LANG, encoding="utf-8"))
    keys = [k for k in tr if k.startswith(BOOK_PREFIXES)]
    print(f"1. 範圍：辭典相關鍵 {len(keys)} 條（模組英文共 "
          f"{sum(1 for k in en if k.startswith(BOOK_PREFIXES))} 條）")

    print("\n2. 巨集結構")
    unbalanced = [(k, "$( 與 ) 數量不符") for k in keys
                  if tr[k].count("$(") != len(MACRO.findall(tr[k]))]
    check("巨集都有收尾", not unbalanced, f"{len(unbalanced)} 條")
    show(unbalanced)

    link_bad = [(k, f'$(l:) {tr[k].count("$(l:")} 個、$(/l) {tr[k].count("$(/l)")} 個')
                for k in keys if tr[k].count("$(l:") != tr[k].count("$(/l)")]
    check("連結開合成對", not link_bad, f"{len(link_bad)} 條")
    show(link_bad)

    redundant = [(k, "有連續的 $(0) 或重複的顏色碼") for k in keys
                 if "$(0)$(0)" in tr[k]
                 or re.search(r"\$\((item|thing)\)\$\(\1\)", tr[k])]
    check("沒有重複的顏色巨集", not redundant, f"{len(redundant)} 條")
    show(redundant)

    dead = []
    for k in keys:
        for path in re.findall(r"\$\(l:([^)]*)\)", tr[k]):
            if path.split("#")[0] not in entries:
                dead.append((k, f"連到不存在的條目 {path}"))
    check("連結都指得到條目", not dead, f"{len(dead)} 條")
    show(dead)

    double_p = [(k, "有連續的 $(p)") for k in keys if "$(p)$(p)" in tr[k]]
    check("沒有空段落", not double_p, f"{len(double_p)} 條")
    show(double_p)

    print("\n3. 排版")
    spaced = [(k, f"{len(re.findall(f'[{CJK}] [{CJK}]', tr[k]))} 處")
              for k in keys if re.search(f"[{CJK}] [{CJK}]", tr[k])]
    check("沒有硬換行留下的空白", not spaced, f"{len(spaced)} 條")
    show(spaced)

    half = [(k, "".join(sorted(set(re.findall(f"[{CJK}]([,.!?;:])|([,.!?;:])[{CJK}]",
                                              tr[k])[0]))))
            for k in keys
            if re.search(f"[{CJK}][,.!?;:]|[,.!?;:][{CJK}]", tr[k])]
    check("沒有貼著中文的半形句讀", not half, f"{len(half)} 條")
    show(half)

    print("\n4. 與英文的落差（供人工判斷，不算失敗）")
    lost_link, lost_colour = [], []
    for k in keys:
        if k not in en:
            continue
        a = len(re.findall(r"\$\(l:", en[k])) - len(re.findall(r"\$\(l:", tr[k]))
        if a > 0:
            lost_link.append((k, f"少 {a} 個連結"))
        b = (len(re.findall(r"\$\((item|thing)\)", en[k]))
             - len(re.findall(r"\$\((item|thing)\)", tr[k])))
        if b > 2:
            lost_colour.append((k, f"少 {b} 處上色"))
    print(f"  [INFO] 連結比英文少的頁：{len(lost_link)} 條")
    show(lost_link, 12)
    print(f"  [INFO] 上色比英文少三處以上的頁：{len(lost_colour)} 條")
    show(lost_colour, 12)
    print("         這兩類多半是譯文照舊版英文寫的，需要重譯整頁，"
          "處理方式是寫進 translation/botania-book-manual.json。")

    print("\n" + ("全部通過。" if not failures else f"失敗 {len(failures)} 項：{failures}"))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
