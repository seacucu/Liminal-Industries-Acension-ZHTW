"""把 translation/botania/ 的辭典譯文套進 botania.json，並讓品名跟著術語表走。

植物魔法辭典（Lexica Botania）是照 Botania 的英文原文重寫的，成品放在
translation/botania/ 底下，一章一個檔，另有 _其他.json 收章名、條目標語、
藥劑名與無障礙字幕。辭典的 book.json 設了 i18n:true，246 個條目、11 個分類
的標題與內文全都是語系鍵，所以整本書可以純靠資源包覆蓋，不必動 Patchouli
的書本檔案。

這支腳本只做三件事：

  1. 依 translation/botania-book-terms.json 校正方塊、物品、生物的名稱，
     讓書裡寫的和玩家在物品欄看到的是同一個詞
  2. 把分章譯文覆蓋到 botania.json 的辭典鍵上
  3. 對不上英文原文的鍵一律列出來，絕不靜默略過

內文不做任何自動改寫：書上出現什麼字，就是分章檔裡寫了什麼字，巨集的位置
也是照英文重建的。結構有沒有寫壞交給 verify_botania_book.py 檢查。
"""

import json
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = os.path.join(ROOT, "translation", "lang", "botania.json")
BOOK = os.path.join(ROOT, "translation", "botania")
TERMS = os.path.join(ROOT, "translation", "botania-book-terms.json")
RENAMES = os.path.join(ROOT, "translation", "renames.json")
NAMES = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
REPORT = os.path.join(ROOT, "_workspace", "build", "botania", "book-changes.json")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

BOOK_PREFIXES = ("botania.page.", "botania.entry.", "botania.tagline.",
                 "botania.category.", "botania.challenge.", "botania.subtitle.",
                 "botania.landing", "botania.brew.", "botaniamisc.challenges")


def load(path, default=None):
    if not os.path.exists(path):
        return {} if default is None else default
    return json.load(open(path, encoding="utf-8"))


def apply_term_names(lang, names, en, terms, modpack_renames):
    """把術語表的決定套回品名。

    決定一次就好：改了 Pixie Dust 的譯名，物品欄、生物名與辭典內文要一起變，
    不然玩家在 JEI 看到的和書上寫的又是兩個名字。模組包自己改過名的條目不碰，
    那是 distribute_renames 的地盤。
    """
    english = {k: d["en"] for k, d in names.items()}
    for key, value in en.items():           # names.json 只收方塊與物品
        if key.startswith("entity.botania.") and key not in english:
            english[key] = value

    renamed = {}
    for key, word in sorted(english.items()):
        zh = terms.get(word)
        if not zh or key in modpack_renames:
            continue
        old = lang.get(key)
        if not old or old == zh:
            continue
        lang[key] = zh
        renamed[key] = (old, zh)
    return renamed


def load_book():
    """讀 translation/botania/*.json，回傳 (鍵 → 譯文, 鍵 → 來源章節, 撞鍵)。"""
    text, origin, clash = {}, {}, []
    for name in sorted(os.listdir(BOOK)):
        if not name.endswith(".json"):
            continue
        chapter = name[:-5]
        for key, value in load(os.path.join(BOOK, name)).items():
            if key.startswith("_"):
                continue
            if key in text and text[key] != value:
                clash.append((key, origin[key], chapter))
            text[key] = value
            origin[key] = chapter
    return text, origin, clash


def main():
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))

    lang = load(LANG)
    names = load(NAMES)
    terms = {k: v for k, v in load(TERMS).items() if not k.startswith("_")}
    modpack_renames = load(RENAMES)

    print("1. 品名校正（術語表）")
    renamed = apply_term_names(lang, names, en, terms, modpack_renames)
    print(f"  依術語表改名 {len(renamed)} 條")
    for key, (old, new) in sorted(renamed.items())[:12]:
        print(f"    {old} → {new}   {key}")
    if len(renamed) > 12:
        print(f"    …另有 {len(renamed) - 12} 條")

    print("\n2. 套用分章譯文")
    text, origin, clash = load_book()
    en_book = {k for k in en if k.startswith(BOOK_PREFIXES)}
    changed, unknown = {}, []
    for key, value in text.items():
        if key not in en_book:
            unknown.append(key)
            continue
        before = lang.get(key)
        lang[key] = value
        if before != value:
            changed[key] = {"英文": en.get(key, ""), "譯文": value,
                            "章": origin[key]}
    missing = sorted(en_book - set(text))

    print(f"  辭典鍵 {len(en_book)} 條，分章檔提供 {len(text)} 條")
    print(f"  寫入 {len(changed)} 條")
    if clash:
        print(f"  [FAIL] 同一個鍵出現在多個章節檔且內容不同：{len(clash)} 條")
        for key, a, b in clash[:10]:
            print(f"    {key}  {a} / {b}")
    if unknown:
        print(f"  [FAIL] 英文原文沒有這些鍵：{len(unknown)} 條")
        for key in sorted(unknown)[:10]:
            print(f"    {key}")
    if missing:
        print(f"  [FAIL] 還沒翻的辭典鍵：{len(missing)} 條")
        for key in missing[:10]:
            print(f"    {key}")

    json.dump(lang, open(LANG, "w", encoding="utf-8", newline="\r\n"),
              ensure_ascii=False, indent=2, sort_keys=True)
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    json.dump({"改寫": changed, "改名": {k: list(v) for k, v in renamed.items()}},
              open(REPORT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\n寫入 {os.path.relpath(LANG, ROOT)}")
    return 1 if (clash or unknown or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
