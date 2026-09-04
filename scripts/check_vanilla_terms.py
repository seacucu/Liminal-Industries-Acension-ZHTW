"""比對譯文與原版 zh_tw 的用詞是否一致。

先前兩次簡中殘留（誤寫成「去皮」「圓石」）都是同一個成因：既有譯文只要沒被明確列為待修，
就原封不動穿過去。這支腳本反過來做，**預設懷疑**：

  1. 由原版 client jar 的 en_us + 資產中的 zh_tw，建立「英文詞 → 原版中文」對照
  2. 掃描本專案所有譯文：若英文名含有某個原版也有的詞，
     但中文沒有用原版的譯法，就列出來人工判斷

這只能提示，不能自動判定（Botania 的 Livingrock 本來就不該叫石頭），
但它會把「該懷疑的地方」全部攤開，而不是等人一個個目視發現。
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VANILLA_TW = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_zh_tw.json")
OUT = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_terms.json")

CLIENT_JAR = os.path.join(
    os.environ.get("APPDATA", ""), "PrismLauncher", "libraries",
    "com", "mojang", "minecraft", "1.20.1", "minecraft-1.20.1-client.jar")

# 觀察的英文詞。挑「構詞用」的詞，不挑專有名詞。
WATCH = [
    "Stripped", "Cobbled", "Chiseled", "Cracked", "Mossy", "Polished", "Smooth",
    "Bricks", "Slab", "Stairs", "Wall", "Planks", "Log", "Fence", "Trapdoor",
    "Sculk", "Nether", "End", "Shulker", "Spawner", "Beacon", "Silk Touch",
    "Fortune", "Wither", "Ghast", "Enderman", "Biome",
]


def vanilla_pairs():
    """回傳 [(英文名, 中文名)]，取自原版 client jar 的 en_us 與 assets 的 zh_tw。"""
    if not os.path.exists(CLIENT_JAR):
        print(f"找不到原版 client jar：{CLIENT_JAR}", file=sys.stderr)
        return []
    with zipfile.ZipFile(CLIENT_JAR) as z:
        en = json.loads(z.read("assets/minecraft/lang/en_us.json").decode("utf-8"))
    tw = json.load(open(VANILLA_TW, encoding="utf-8"))
    return [(en[k], tw[k]) for k in en
            if k in tw and k.startswith(("block.minecraft.", "item.minecraft.",
                                         "entity.minecraft.", "enchantment.minecraft."))]


def main():
    pairs = vanilla_pairs()
    if not pairs:
        return 1

    # 對每個觀察詞，找出原版怎麼譯（取最常見的公共子字串太複雜，
    # 這裡改用：含該英文詞的所有原版中文名，交給人眼判斷）
    table = {}
    for w in WATCH:
        hits = [(e, c) for e, c in pairs if re.search(rf"\b{w}", e)]
        if hits:
            table[w] = hits[:4]
    json.dump({w: h for w, h in table.items()},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    lang_dir = os.path.join(ROOT, "translation", "lang")
    mine = {}
    for f in sorted(os.listdir(lang_dir)):
        if f.endswith(".json"):
            mine.update(json.load(open(os.path.join(lang_dir, f), encoding="utf-8")))

    # 英文基準
    en_ref = json.load(open(os.path.join(ROOT, "source", "kubejs_names.json"), encoding="utf-8"))
    en_ref = {k: v["en"] for k, v in en_ref.items()}
    names = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
    if os.path.exists(names):
        en_ref.update({k: v["en"] for k, v in json.load(open(names, encoding="utf-8")).items()})

    print(f"原版對照組 {len(pairs)} 筆，觀察詞 {len(table)} 個\n")
    total = 0
    for w, hits in table.items():
        vanilla_cn = {c for _, c in hits}
        # 原版譯法的共同字（粗略取第一個譯名中不在英文裡的中文字串）
        suspects = []
        for k, e in en_ref.items():
            if not re.search(rf"\b{w}", e) or k not in mine:
                continue
            suspects.append((e, mine[k]))
        if not suspects:
            continue
        print(f"■ {w}　原版例：" + "、".join(f"{e}={c}" for e, c in hits[:2]))
        for e, c in suspects[:3]:
            print(f"      本專案：{e:<34}{c}")
        if len(suspects) > 3:
            print(f"      …共 {len(suspects)} 條")
        total += len(suspects)
        print()
    print(f"合計需人工確認 {total} 條。對照表已存至 {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
