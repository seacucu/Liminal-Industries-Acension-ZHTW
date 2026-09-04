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
    # 以下由官方 zh_cn 黑名單（scripts/build_cn_terms.py）抓出，右欄為原版 zh_tw
    ("刷怪籠", "生怪磚"),
    ("刷怪場", "生怪場"),
    ("箱子", "儲物箱"),
    ("交互", "互動"),
    ("再生藥水", "回復藥水"),
    ("急迫", "挖掘加速"),
    ("抗性提升", "抗性"),
    ("橡木木板", "橡木材"),
    ("製作木板", "製作木材"),
    ("烈焰棒", "烈焰桿"),
    ("黏液球", "史萊姆球"),
    ("灰化土", "灰壤"),
    ("曲奇", "餅乾"),
    ("烈焰人", "烈焰使者"),
    # 資訊領域的兩岸用語。官方語系檔只收名詞性 key，抓不到這類，需人工列。
    # 已排除三個誤判：程序（儀式的「程序」是正體常用）、質量（Tiny Planet 的
    # mass）、配置（「設備配置得當」是正體常用）。
    ("激活", "啟用"),
    ("網絡", "網路"),
    ("緩存", "緩衝"),      # 英文原文是 buffer
    ("鼠標", "滑鼠"),
    ("優先級", "優先順序"),
    ("文本", "文字"),
    ("信息", "資訊"),
    ("默認", "預設"),
    ("被設置成", "被設定成"),
    ("菜單", "選單"),
    ("信號", "訊號"),      # 原版 zh_tw：紅石訊號
    ("幾率", "機率"),
    ("概率", "機率"),
    ("夢之木棍", "夢之木枝"),   # 與 item.botania.dreamwood_twig 一致
    ("木棍", "木棒"),          # 原版 item.minecraft.stick = 木棒
    ("圖標", "圖示"),
    ("小土豆", "小小馬鈴薯"),
    ("土豆", "馬鈴薯"),
    ("雪傀儡", "雪人"),
    # 原譯把按鍵名直接夾在中文裡（「採花袋shift右擊」），遊戲內很難讀
    ("shift右擊", " Shift+右鍵點擊"),
    ("它mod", "它模組"),
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
    # 英文原本是三種玩笑拼法 Lexica Botania / Botana / Botonia，
    # 既有 zh_tw 三者同名，JEI 搜尋會出現數本無法區分的辭典
    "item.botania.lexicon.bevo": "植物魔法辭曲",
    "item.botania.lexicon.saice": "植物魔法詞典",
}

# 範圍外、Botania 自己缺譯或譯錯的條目，由本包補上
EXTRA = {
    # 辭典首頁的整段介紹，Botania 的 zh_tw 根本沒有這兩個 key
    "botania.landing": "魔法與科技，渾然天成。$(br2)植物魔法是一個以自然魔法為主題的科技模組。"
                       "核心概念是運用大地的力量——也就是魔力——製作出各種魔法花朵與裝置。",
    "botania.desc": "魔法與科技，渾然天成",
    # advancement.botania:lexiconUse 不列在這裡：那是曲名「現実的論理主義者」，
    # ja_jp / zh_cn / zh_tw 三個語系皆保留日文原題，與其餘 25 個曲名一致。
    # 我曾誤把它當成汙染改成「現實的邏輯主義者」，已還原為沿用模組原值。
}


EXTRA_ADVANCEMENT = {
    # Botania 的進度標題全是 Vocaloid 曲名，Vazkii 刻意在每個語系都保留原文
    # （ja/zh_cn/de/fr 皆同），因此標題不譯，只補說明行與非曲名的分類名。
    "advancement.botania_challenge": "植物魔法挑戰",
    "advancement.botania_challenge.desc": "為進階植物魔法師準備的挑戰",
    "advancement.botania:alfPortalBread.desc": "送麵包給精靈",
    "advancement.botania:allLooniumMobs.desc": "擊殺每一種由聚寶花生成的怪物",
    "advancement.botania:gaiaGuardianHardmode.desc":
        "在蓋亞儀式 II 中召喚並擊敗強化過的蓋亞守護者",
    "advancement.botania:lokiRingMany.desc": "用洛基之戒一次額外放置超過 255 個方塊",
    "advancement.botania:old_flower_pickup.desc": "發現太陽花裝飾或夜顛茄裝飾",
    "advancement.botania:tinyPotatoBirthday.desc": "在 7 月 19 日慶祝小小馬鈴薯的生日",
}


# 模組 zh_tw 與 ja_jp 相同 ⇒ 那是刻意保留的日文原題（曲名、引用），不是翻譯漏洞。
# 覆寫這種條目必須在此列出理由，否則腳本會擋下來。
# 我曾把 advancement.botania:lexiconUse（現実的論理主義者）誤判為簡中汙染而改掉。
OVERRIDE_ORIGINAL_OK = {
    "block.botania.gourmaryllis.reference":
        "花朵的 reference 欄共 52 條，其中 50 條在 zh_tw 都已中文化"
        "（僅兩條德文 Flügel der Freiheit 例外），故此條中文化才是一致的做法",
}


def spaced_variants(term):
    """術語本身，以及被單一空白切開的所有形式（長的先試，避免部分吃掉）。"""
    return [term] + [term[:i] + " " + term[i:] for i in range(1, len(term))]


def fix_formats(en, tw):
    """修正既有 zh_tw 的格式錯誤（有英文原文可對照時才動）。"""
    notes = []
    # 1. 顏色碼：zh_tw 誤用 & ，其餘語系（en/zh_cn/ja/de/fr/ru）皆用 §
    # zh_tw 是唯一誤用 & 的語系（en/zh_cn/ja/de/fr/ru 全用 §）。
    # 不能要求「英文也有 §」——有 4 條是譯者自行加的格式，英文原文沒有顏色碼。
    if re.search(r"&[0-9a-fk-or]", tw):
        tw = re.sub(r"&([0-9a-fk-or])", "§" + chr(92) + "1", tw)  # 保留顏色字母
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
            # 書頁文字是硬換行的，術語常被空白切開（「瑪 那」），逐一比對變體
            for variant in spaced_variants(bad):
                if variant in new:
                    counts[bad] = counts.get(bad, 0) + new.count(variant)
                    new = new.replace(variant, good)
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
    for k, v in EXTRA.items():
        merged[k] = v
    for k, v in EXTRA_ADVANCEMENT.items():
        merged[k] = v
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        ja = json.loads(z.read("assets/botania/lang/ja_jp.json").decode("utf-8"))
    stomped = sorted(k for k, v in merged.items()
                     if k in tw and k in ja and tw[k] == ja[k] and v != tw[k]
                     and k not in OVERRIDE_ORIGINAL_OK)
    if stomped:
        detail = [f"    {k}: {tw[k]!r} -> {merged[k]!r}" for k in stomped]
        raise SystemExit(
            "覆寫了刻意保留的日文原題（模組 zh_tw == ja_jp）。"
            "若確實該中文化，請加進 OVERRIDE_ORIGINAL_OK 並寫明理由："
            + chr(10) + chr(10).join(detail))

    json.dump(merged, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"範圍外條目 {sum(1 for k in tw if not k.startswith(IN_SCOPE))}")
    print(f"  實際變動 {len(changed)} 條")
    for bad, n in sorted(counts.items(), key=lambda x: -x[1]):
        good = dict(SUBS).get(bad, "")
        arrow = f" → {good}" if good else ""
        print(f"    {bad}{arrow:<14}{n} 處")
    print(f"  格式修正：顏色碼 &→§ {fmt['colour']} 條、百分號 %→%% {fmt['percent']} 條")
    print(f"  個別覆寫 {len(IN_SCOPE_FIXES)} 條、補譯 {len(EXTRA)} 條、"
          f"進度說明 {len(EXTRA_ADVANCEMENT)} 條")
    print(f"\n合併後 {os.path.relpath(OUT, ROOT)} 共 {len(merged)} 條"
          f"（範圍內 {len(existing)} + 範圍外 {len(changed)}）")


if __name__ == "__main__":
    main()
