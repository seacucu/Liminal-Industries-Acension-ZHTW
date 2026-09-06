"""手冊譯文的結構檢查。

手冊正文夾雜著版面標記，改壞了不會報錯，只會在遊戲裡默默少一張配方圖或
變成一個點不動的連結。這支腳本比對譯文與英文原文的標記是否一致：

  1. 錨點 <&x> 集合相同（錨點決定配方圖、多方塊預覽插在哪一段）
  2. 錨點名都存在於該條目的 json 設定裡
  3. 連結 <link;目標;文字> 的目標集合相同（中文語序不同，出現順序可以不同）
  4. <keybind;...> 原樣保留；<config;...> 的型別與設定路徑不變
     （<config;b;路徑;甲;乙> 後面兩段是顯示文字，本來就該翻譯）
  5. §r 的數量相同，且英文用過的顏色碼譯文都還在；% 不轉義（手冊正文不是語系檔，寫 %% 會原樣顯示）
  6. 前兩行（標題、副標）存在且已翻譯
  7. 無簡體字、無殘留未譯（與英文完全相同）

用法：
    python scripts/verify_manual.py
"""

import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "_workspace", "build", "manual")
MINE = os.path.join(ROOT, "translation", "manual")

TOKEN = re.compile(r"<[^>]*>")
ANCHOR = re.compile(r"^<&(.+)>$")
LINK = re.compile(r"^<link;([^;>]+)(?:;(.*))?>$", re.S)
CONFIG = re.compile(r"^<config;([^;>]+);([^;>]+)")
COLOR = re.compile(r"§(.)")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from verify_translation import SIMPLIFIED  # noqa: E402


def parse(text):
    anchors, links, other = [], [], []
    for tok in TOKEN.findall(text):
        m = ANCHOR.fullmatch(tok)
        if m:
            anchors.append(m.group(1))
            continue
        m = LINK.fullmatch(tok)
        if m:
            links.append((m.group(1), (m.group(2) or "")))
            continue
        # <config;b;路徑;甲;乙> 的後兩段是要顯示給玩家看的文字，會跟著翻譯，
        # 只有型別與設定路徑必須原樣保留
        m = CONFIG.match(tok)
        if m:
            other.append(f"<config;{m.group(1)};{m.group(2)}>")
            continue
        other.append(tok)
    return anchors, links, other


def check(ns, entry, en_text, tw_text, meta):
    bad = []
    ea, el, eo = parse(en_text)
    ta, tl, to = parse(tw_text)

    if sorted(ea) != sorted(ta):
        bad.append(f"錨點不符：缺 {sorted(set(ea) - set(ta))}、多 {sorted(set(ta) - set(ea))}")
    allowed = set(meta.get("elements") or [])
    if allowed:
        stray = sorted(set(ta) - allowed)
        if stray:
            bad.append(f"錨點不在 {entry}.json 的元素清單裡：{stray}")

    # 中文語序常與英文不同，連結在句中的先後可以變，但整篇連到哪些條目不能變
    if sorted(t for t, _ in el) != sorted(t for t, _ in tl):
        bad.append(f"連結目標不符：英文 {sorted(t for t, _ in el)}、"
                   f"譯文 {sorted(t for t, _ in tl)}")
    for target, label in tl:
        # link 的第二段可省略（顯示文字＝目標本身），但寫了就不能是空的
        if label is not None and label.strip() == "" and ";" in f"<link;{target};{label}>":
            bad.append(f"連結 {target} 的顯示文字是空的")

    if eo != to:
        bad.append(f"其他標記被改動：英文 {eo}、譯文 {to}")

    # 少一個 §r 會讓格式滲進後面的段落，所以 §r 要一個不差。
    # 其餘顏色碼只看有沒有：英文常把 §l 重複寫在同一個詞的每個英文字上，
    # 那是為了讓粗體撐過換行，中文不斷字，寫一次就夠（模組自帶的 zh_cn 也是這樣）。
    en_codes = collections.Counter(COLOR.findall(en_text))
    tw_codes = collections.Counter(COLOR.findall(tw_text))
    if en_codes["r"] != tw_codes["r"]:
        bad.append(f"§r 數量不符：英文 {en_codes['r']}、譯文 {tw_codes['r']}")
    lost = sorted(c for c in en_codes if c != "r" and not tw_codes[c])
    if lost:
        bad.append(f"顏色碼整組消失：{['§' + c for c in lost]}")

    if "%%" in tw_text and "%%" not in en_text:
        bad.append("出現 %%：手冊正文不是語系檔，百分號不需要轉義")

    lines = tw_text.splitlines()
    en_lines = en_text.splitlines()
    if len(lines) < 2 or not lines[0].strip():
        bad.append("前兩行必須是標題與副標，標題不可為空")
    else:
        # 少數條目本來就沒有副標，這時譯文也要留一行空的，行號才對得上
        if bool(lines[1].strip()) != bool(en_lines[1].strip()):
            bad.append("副標的有無必須與英文一致")
        if lines[0] == en_lines[0]:
            bad.append(f"標題未翻譯：{lines[0]}")

    zh = SIMPLIFIED.intersection(tw_text)
    if zh:
        bad.append(f"含簡體字：{''.join(sorted(zh))}")

    if tw_text.strip() == en_text.strip():
        bad.append("整篇與英文原文相同")

    return bad


def main():
    if not os.path.isdir(EN):
        print("請先執行 scripts/extract_manual.py", file=sys.stderr)
        return 1

    total = fails = missing = 0
    for ns in sorted(os.listdir(EN)):
        en_dir = os.path.join(EN, ns, "en_us")
        if not os.path.isdir(en_dir):
            continue
        meta = json.load(open(os.path.join(EN, ns, "meta.json"), encoding="utf-8"))
        for dirpath, _, files in sorted(os.walk(en_dir)):
            for f in sorted(files):
                if not f.endswith(".txt"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, f), en_dir).replace("\\", "/")
                entry = rel[:-4]
                mine = os.path.join(MINE, ns, rel)
                total += 1
                if not os.path.exists(mine):
                    missing += 1
                    continue
                en_text = open(os.path.join(dirpath, f), encoding="utf-8").read()
                tw_text = open(mine, encoding="utf-8").read()
                bad = check(ns, entry, en_text, tw_text, meta.get(entry, {}))
                if bad:
                    fails += 1
                    print(f"✗ {ns}/{entry}")
                    for b in bad:
                        print(f"    {b}")

    done = total - missing
    print(f"\n條目 {total}、已譯 {done}、未譯 {missing}、有問題 {fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
