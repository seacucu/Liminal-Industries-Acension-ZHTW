"""對 Botania 範圍外的既有 zh_tw 做純術語代換（不重譯）。

範圍內（block./item. 名稱）由 botania_compose.py 產出；本腳本處理其餘條目，
只替換術語與明顯錯字，讓「物品欄」與「植物魔法辭典內文」不會出現兩套叫法。

明確不處理：半形標點、譯文風格、缺譯條目 —— 那些屬於重譯範疇。

輸出併入 translation/lang/botania.json
"""

import json
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "translation", "lang", "botania.json")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

# (錯誤寫法, 正確寫法)。順序重要：長詞先於短詞。
SUBS = [
    ("瑪那鋼", "魔鋼"),
    ("瑪那", "魔力"),
    ("魔源", "魔力"),
    ("主媒體", "主具現"),
    ("多媒體", "具現"),
    ("信標", "烽火台"),      # 原版 zh_tw
    ("刷怪籠", "生怪磚"),    # 原版 zh_tw
    ("精準採集", "絲綢之觸"),  # 原版 zh_tw
    ("凋靈", "凋零"),        # 原版 zh_tw
    ("鬥篷", "斗篷"),        # 錯字
    ("炉", "爐"),            # 殘留簡體
    ("$(0)里更", "$(0)裡更"),  # 殘留簡體：方位詞的「里」應為「裡」
]

IN_SCOPE = ("block.botania.", "item.botania.")

# 逐條修正的既有錯誤（key, 錯誤片段, 正確片段, 說明）
LINE_FIXES = [
    ("botania.armorset.manaweave.desc0", "35%", "40%",
     "既有譯文數值誤植：英文為 40%%，譯文寫 35%"),
]

# 範圍內（block./item.）但由 compose 的後備路徑沿用既有譯文者，個別覆寫
IN_SCOPE_FIXES = {
    # 英文是 "How unpleasant"；zh_cn 照抄了 ja_jp 的日文，對繁中讀者無意義
    "block.botania.gourmaryllis.reference": "真令人不快",
}


def fix_formats(en, tw):
    """修正既有 zh_tw 的格式錯誤（有英文原文可對照時才動）。"""
    notes = []
    # 1. 顏色碼：zh_tw 誤用 & ，其餘語系（en/zh_cn/ja/de/fr/ru）皆用 §
    if re.search(r"&[0-9a-fk-or]", tw) and "§" in en:
        tw = re.sub(r"&([0-9a-fk-or])", r"§", tw)
        notes.append("colour")
    # 2. 百分號：語系檔中的字面 % 必須寫成 %%
    if "%%" in en and "%%" not in tw and "%" in tw:
        tw = re.sub(r"(?<!%)%(?!%)", "%%", tw)
        notes.append("percent")
    return tw, notes


def main():
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        tw = json.loads(z.read("assets/botania/lang/zh_tw.json").decode("utf-8"))
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))

    existing = json.load(open(OUT, encoding="utf-8"))

    line_fix_map = {k: (bad, good) for k, bad, good, _ in LINE_FIXES}

    changed, counts, fmt = {}, {}, {"colour": 0, "percent": 0}
    for k, v in tw.items():
        if k.startswith(IN_SCOPE):
            continue                     # 範圍內已由 compose 產出
        new = v
        for bad, good in SUBS:
            if bad in new:
                counts[bad] = counts.get(bad, 0) + new.count(bad)
                new = new.replace(bad, good)
        if k in line_fix_map:
            bad, good = line_fix_map[k]
            assert bad in new, f"{k} 找不到待修片段 {bad}"
            new = new.replace(bad, good)
            counts["逐條修正"] = counts.get("逐條修正", 0) + 1
        new, ns = fix_formats(en.get(k, ""), new)
        for n in ns:
            fmt[n] += 1
        if new != v:
            changed[k] = new

    merged = dict(existing)
    overlap = set(changed) & set(existing)
    assert not overlap, f"與範圍內重疊：{sorted(overlap)[:5]}"
    merged.update(changed)
    for k, v in IN_SCOPE_FIXES.items():
        assert k in merged, f"IN_SCOPE_FIXES 的 {k} 不存在"
        merged[k] = v
    json.dump(merged, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"範圍外條目 {sum(1 for k in tw if not k.startswith(IN_SCOPE))}")
    print(f"  實際變動 {len(changed)} 條")
    for bad, n in sorted(counts.items(), key=lambda x: -x[1]):
        good = dict(SUBS).get(bad, "")
        arrow = f" → {good}" if good else ""
        print(f"    {bad}{arrow:<14}{n} 處")
    print(f"  格式修正：顏色碼 &→§ {fmt['colour']} 條、百分號 %→%% {fmt['percent']} 條")
    print(f"\n合併後 {os.path.relpath(OUT, ROOT)} 共 {len(merged)} 條"
          f"（範圍內 {len(existing)} + 範圍外 {len(changed)}）")


if __name__ == "__main__":
    main()
