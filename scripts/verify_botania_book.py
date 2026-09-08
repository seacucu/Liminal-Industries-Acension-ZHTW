"""檢查植物魔法辭典內文的結構。

辭典是照英文原文重寫的（translation/botania/），巨集的位置也是照原文擺的，
所以這裡驗的是「有沒有手滑寫壞」：巨集沒收好、連結指向不存在的條目、
中文之間殘留半形空白之類，不通過就讓建置失敗。

另外列出與英文的落差（連結或上色數量對不上）供人判斷。那多半是中文句構
併掉了某個詞，未必是錯，但值得回頭看一眼，所以不算失敗。
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
                 "botania.landing", "botania.brew.", "botaniamisc.challenges")

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

    # 英文原本就有連著兩個 $(p) 的頁（welcome6 用它空一行），照抄不算錯
    double_p = [(k, "有連續的 $(p)") for k in keys
                if "$(p)$(p)" in tr[k] and "$(p)$(p)" not in en.get(k, "")]
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
    print("         這兩類是中文句構把某個詞併掉了，回頭看一眼 "
          "translation/botania/ 對應章節的那一條即可。")

    print("\n" + ("全部通過。" if not failures else f"失敗 {len(failures)} 項：{failures}"))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
