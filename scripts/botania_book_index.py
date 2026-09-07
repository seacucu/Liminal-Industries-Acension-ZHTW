"""把辭典的英文原文按「章 → 條目 → 頁」攤成工作底稿。

翻譯是照英文從頭寫的，所以底稿裡只放英文：條目標題、頁碼、原文，
外加該頁英文用到的連結目標與上色詞，讓譯文能把巨集擺回同樣的位置。
輸出到 _workspace/build/botania/english/<category>.json（工作區，不進版控）。
"""

import json
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_workspace", "build", "botania", "english")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

BOOK_PREFIXES = ("botania.page.", "botania.entry.", "botania.tagline.",
                 "botania.category.", "botania.challenge.", "botania.subtitle.",
                 "botania.landing", "botania.brew.")


def main():
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))
        cats, cat_order = {}, {}
        for n in z.namelist():
            if "/lexicon/en_us/categories/" in n and n.endswith(".json"):
                d = json.loads(z.read(n).decode("utf-8"))
                slug = n.split("/")[-1][:-5]
                cats[slug] = d["name"]
                cat_order[slug] = d.get("sortnum", 99)
        entries = []
        for n in sorted(z.namelist()):
            if "/lexicon/en_us/entries/" not in n or not n.endswith(".json"):
                continue
            entries.append((n.split("/entries/")[1][:-5],
                            json.loads(z.read(n).decode("utf-8"))))

    books = {}
    seen = set()
    for path, e in entries:
        slug = e.get("category", "").split(":")[-1]
        cat_key = cats.get(slug, slug)
        b = books.setdefault(slug, {
            "_章": cat_key, "_章英文": en.get(cat_key, ""), "_條目": []})
        item = {"路徑": path, "標題鍵": e["name"], "標題英文": en.get(e["name"], ""),
                "頁": []}
        seen.add(e["name"])
        for i, page in enumerate(e.get("pages", []), 1):
            # 欄位不只 text：flavor（釀造頁的引言）也會印在書上，別漏了
            for field, k in page.items():
                if not isinstance(k, str) or not k.startswith("botania."):
                    continue
                if k in seen:
                    continue
                seen.add(k)
                t = en.get(k, "")
                item["頁"].append({
                    "鍵": k, "頁碼": i, "欄位": field,
                    "類型": page.get("type", "").split(":")[-1],
                    "英文": t,
                    "連結": re.findall(r"\$\(l:([^)]*)\)", t),
                    "字數": len(t),
                })
        b["_條目"].append(item)

    other = {k: en[k] for k in sorted(en)
             if k.startswith(BOOK_PREFIXES) and k not in seen}

    os.makedirs(OUT, exist_ok=True)
    total = 0
    for slug in sorted(books, key=lambda s: (cat_order.get(s, 99), s)):
        b = books[slug]
        n = sum(len(i["頁"]) for i in b["_條目"])
        c = sum(p["字數"] for i in b["_條目"] for p in i["頁"])
        total += c
        json.dump(b, open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"  {slug:<20} 條目 {len(b['_條目']):>3}  頁 {n:>4}  英文 {c:>6} 字")
    json.dump(other, open(os.path.join(OUT, "_其他.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    print(f"  {'_其他':<20} {len(other)} 條（章名、標語、挑戰、封面等）")
    print(f"  合計英文 {total} 字 → {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
