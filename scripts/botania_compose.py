"""由詞根 + 修飾語組合出 Botania 的 1,060 條方塊／物品名稱。

作法：
  1. 先對既有 zh_tw 施加術語校正（依 docs/glossary-botania.md）
  2. 把英文名稱拆成「修飾語 + 詞根」，詞根譯名優先取自校正後的既有譯文
  3. 依原版 zh_tw 的構詞規則把修飾語接回去
  4. 組不出來的逐條列出，絕不靜默略過

詞根譯名的人工補充放在 translation/botania-roots.json。
"""

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
ROOTS = os.path.join(ROOT, "translation", "botania-roots.json")
OUT = os.path.join(ROOT, "translation", "lang", "botania.json")

# --- 術語校正：(英文條件, 既有譯文的錯誤寫法, 正確寫法) ------------------
# 以英文為條件，避免盲目字串取代造成誤傷。
# (英文條件, 錯誤寫法, 正確寫法, 英文排除條件)
# 英文條件為 None 代表無條件套用。
TERM_FIXES = [
    (None,           "瑪那鋼", "魔鋼",   None),
    (None,           "瑪那",   "魔力",   None),   # 瑪那只可能是 Mana
    (None,           "魔源",   "魔力",   None),
    (None,           "玻璃板", "玻璃片", None),   # 原版 glass_pane = 玻璃片
    # 口語型的兩岸差異，官方術語表收的是「马铃薯」故抓不到「土豆」
    (None,           "小土豆", "小小馬鈴薯", None),
    (None,           "土豆",   "馬鈴薯", None),
    (None,           "概率",   "機率",   None),
    (None,           "幾率",   "機率",   None),
    (None,           "信號",   "訊號",   None),   # 原版：紅石訊號
    (r"Corporea",    "多媒體", "具現",   None),
    (r"Corporea",    "主媒體", "主具現", None),
    (r"Livingwood",  "活木枝", "活木",   r"Twig"),  # Twig 本來就該是「枝」
    (r"Glimmering",  "微光",   "螢光",   None),
    (r"Chiseled",    "框邊",   "浮雕",   None),
    (r"Cracked",     "裂活",   "裂紋活", None),
    (r"Luminizer",   "微光",   "光導",   None),   # 與 Shimmering=微光 撞名
    (r"Cloak",       "鬥篷",   "斗篷",   None),   # 既有錯字
    (None,           "熏香",   "薰香",   None),   # 正體用「薰」，與本包的薰香石英一致
    (r"Cobbled",     "圓石",   "碎石",   None),   # 圓石為簡中；原版 cobbled_deepslate = 深板岩碎石
    (r"Lavender",    "薰香",   "薰衣草", None),   # Lavender 是薰衣草，不是薰香
    (None,           "籐",     "藤",     None),   # 原版 vines = 藤蔓，統一用「藤」
    (r"Spark Augment", "火花升級", "火花增幅", None),  # 與術語表的 Augment=增幅 對齊
    (None,           "橘色",   "橙色",   None),   # 原版 orange_dye = 橙色染料
]

# 名稱層級的標點正規化：繁中名稱用全形標點
# 括號要先試「空白＋左括號」，否則 item.botania.brew_flask 會留下
# 「裝有%s （%s）的燒瓶」那個多餘的半形空白。
# 冒號換成全形之後，後面那個半形空白要一起收掉，否則
# 「合成模板#1： 1x1」會留著一個突兀的空隙。
PUNCT_FIXES = [(":", "："), ("： ", "："), (" (", "（"), ("(", "（"), (")", "）")]

# --- 修飾語：英文樣式 → 中文構詞（前綴或後綴）----------------------------
# (英文樣式, 中文, 排序權重)。權重決定多個前綴並存時的中文語序，
# 例如 Tall Mystical → 神秘(10) + 高(20) = 「神秘高」，而非「高神秘」。
PREFIX = [
    (r"^Mystical ",   "神秘", 10),
    (r"^Tall ",       "高",   20),
    (r"^Glimmering ", "螢光", 30),
    (r"^Shimmering ", "微光", 30),
    (r"^Floating ",   "浮空", 40),
    (r"^Chiseled ",   "浮雕", 50),
    (r"^Cracked ",    "裂紋", 50),
    (r"^Mossy ",      "青苔", 50),
    (r"^Polished ",   "拋光", 50),
    (r"^Smooth ",     "平滑", 50),
    (r"^Framed ",     "框邊", 50),
    (r"^Stripped ",   "剝皮", 50),   # 原版 stripped_oak_log = 剝皮橡木原木
]
SUFFIX = [
    (r" Plank Slab$",     "材半磚"),   # 需早於 " Slab$"
    (r" Plank Stairs$",   "材階梯"),
    (r" Twig$",           "枝"),
    (r" Slab$",           "半磚"),
    (r" Stairs$",         "階梯"),
    (r" Wall$",           "牆"),
    (r" Fence Gate$",     "柵欄門"),
    (r" Fence$",          "柵欄"),
    (r" Planks$",         "材"),
    (r" Bricks$",         "磚"),
    (r" Brick$",          "磚"),
    (r" Petite$",         ""),      # 由 PETITE 另行處理（需置於花名前）
    (r" Button$",         "按鈕"),
    (r" Pressure Plate$", "壓力板"),
    (r" Trapdoor$",       "地板門"),
    (r" Door$",           "門"),
    (r" Log$",            "原木"),
    (r" Wood$",           "木"),
    (r" Motif$",          "裝飾"),
    (r" Block$",          "方塊"),
]
COLORS = {
    "Black": "黑色", "Blue": "藍色", "Brown": "棕色", "Cyan": "青色",
    "Gray": "灰色", "Green": "綠色", "Light Blue": "淺藍色", "Light Gray": "淺灰色",
    "Lime": "淺綠色", "Magenta": "洋紅色", "Orange": "橙色", "Pink": "粉紅色",
    "Purple": "紫色", "Red": "紅色", "White": "白色", "Yellow": "黃色",
    "Rainbow": "彩虹",
}


def apply_term_fixes(en, tw):
    for cond, bad, good, exclude in TERM_FIXES:
        if exclude and re.search(exclude, en, re.I):
            continue
        if (cond is None or re.search(cond, en, re.I)) and bad in tw:
            tw = tw.replace(bad, good)
    for bad, good in PUNCT_FIXES:
        tw = tw.replace(bad, good)
    return tw


def strip_modifiers(en):
    """回傳 (詞根英文, 前綴中文list, 後綴中文list, 顏色中文or None, petite?)"""
    pre, suf, colour, petite = [], [], None, False
    changed = True
    while changed:
        changed = False
        for pat, cn, order in PREFIX:
            if re.search(pat, en):
                en = re.sub(pat, "", en).strip()
                pre.append((order, cn))
                changed = True
        # 原版用「X柱」（石英柱、紫珀柱），不是「柱狀X方塊」
        m = re.match(r"^Pillar (.*) Block$", en)
        if m:
            en = m.group(1).strip()
            suf.append("柱")
            changed = True
        if en.startswith("Potted "):
            en = en[len("Potted "):].strip()
            suf.append("盆栽")
            changed = True
        for pat, cn in SUFFIX:
            if re.search(pat, en):
                if pat == r" Petite$":
                    petite = True
                else:
                    suf.insert(0, cn)
                en = re.sub(pat, "", en).strip()
                changed = True
        if en.startswith("Block of "):
            en = en[len("Block of "):].strip()
            suf.append("方塊")
            changed = True
        for c in sorted(COLORS, key=len, reverse=True):
            m = re.match(rf"^{re.escape(c)} (?=[A-Z])", en)
            if m:
                en = en[m.end():].strip()
                colour = COLORS[c]
                changed = True
                break
    return en, pre, suf, colour, petite


# 組合後的中文修飾：某些接合處在中文裡不能直接串接。
# 依原版 zh_tw：stone=石頭 但 stone_bricks=石磚、stone_slab=石半磚。
JOIN_FIXES = [("石頭磚", "石磚")]


def compose(root_cn, pre, suf, colour, petite):
    body = "".join(cn for _, cn in sorted(pre)) + root_cn + "".join(suf)
    if petite:
        body = "小型" + body
    if colour:
        body = colour + body
    for bad, good in JOIN_FIXES:
        body = body.replace(bad, good)
    return body


def main():
    data = json.load(open(NAMES, encoding="utf-8"))
    hand = json.load(open(ROOTS, encoding="utf-8")) if os.path.exists(ROOTS) else {}

    # 1. 校正既有譯文
    fixed = {}
    for k, v in data.items():
        if v["tw"]:
            fixed[k] = apply_term_fixes(v["en"], v["tw"])

    # 2. 由「無修飾語」的條目建立詞根字典
    root_dict = dict(hand)
    for k, v in data.items():
        if k not in fixed:
            continue
        r, pre, suf, colour, petite = strip_modifiers(v["en"])
        if not pre and not suf and not colour and not petite and r == v["en"]:
            root_dict.setdefault(r, fixed[k])

    # 3. 逐條組合
    out, unresolved, fallback = {}, [], []
    for k, v in sorted(data.items()):
        r, pre, suf, colour, petite = strip_modifiers(v["en"])
        if r in root_dict:
            out[k] = compose(root_dict[r], pre, suf, colour, petite)
        elif k in fixed:
            out[k] = fixed[k]          # 有既有譯文但拆不出詞根 → 沿用校正後的
            fallback.append((k, v["en"], r))
        else:
            unresolved.append((k, v["en"], r))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"總計 {len(data)} 條")
    print(f"  規則組合 {len(out) - len(fallback)}")
    print(f"  沿用既有 {len(fallback)}  ← 詞根不在字典，構詞規則未套用")
    print(f"  未解決   {len(unresolved)}")
    if fallback:
        import collections
        fr = collections.Counter(r for _, _, r in fallback)
        print("\n沿用既有的詞根（補進字典即可讓規則生效）：")
        for r, n in fr.most_common(12):
            print(f"    {n:>3} × {r}")
    if unresolved:
        miss_roots = sorted({r for _, _, r in unresolved})
        print(f"\n缺少譯名的詞根 {len(miss_roots)} 個（請補進 {os.path.relpath(ROOTS, ROOT)}）：")
        for r in miss_roots[:40]:
            print(f"    {r}")
        if len(miss_roots) > 40:
            print(f"    …另有 {len(miss_roots)-40} 個")
    print(f"\n寫入 {os.path.relpath(OUT, ROOT)}")
    return unresolved


if __name__ == "__main__":
    main()
