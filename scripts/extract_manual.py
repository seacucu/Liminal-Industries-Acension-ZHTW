"""抽出 BluSunrize 手冊系統（Immersive Engineering 工程師手冊）的英文原文。

手冊正文不在 lang 檔裡，而是 assets/<ns>/manual/<語系>/<條目>.txt 一條目一檔，
由 ManualEntryBuilder 讀取，找不到當前語系就退回 manual/en_us/。因此資源包只要
補上 manual/zh_tw/，整本手冊就會變中文，不需要動模組檔。

輸出：
    _workspace/build/manual/<ns>/en_us/*.txt   英文原文（翻譯的依據）
    _workspace/build/manual/<ns>/meta.json     每條目的錨點與連結目標，供檢查用

用法：
    python scripts/extract_manual.py
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")
OUT = os.path.join(ROOT, "_workspace", "build", "manual")
MINE = os.path.join(ROOT, "translation", "manual")

ENTRY = re.compile(r"assets/([a-z0-9_.-]+)/manual/en_us/([a-z0-9_/-]+)\.txt")
ANCHOR = re.compile(r"<&([^>]+)>")
LINK = re.compile(r"<link;([^;>]+);")


def scan(jar):
    """回傳 {ns: {entry: (英文原文, 該條目的 json 設定或 None)}}。"""
    out = {}
    with zipfile.ZipFile(jar) as z:
        names = set(z.namelist())
        for n in sorted(names):
            m = ENTRY.fullmatch(n)
            if not m:
                continue
            ns, entry = m.group(1), m.group(2)
            cfg = f"assets/{ns}/manual/{entry}.json"
            data = None
            if cfg in names:
                data = json.loads(z.read(cfg).decode("utf-8"))
            raw = z.read(n)
            out.setdefault(ns, {})[entry] = (raw, data)
    return out


def main():
    if not os.path.isdir(MODS):
        print(f"找不到實例 mods 目錄：{MODS}", file=sys.stderr)
        return 1

    found = {}
    for jar in sorted(os.listdir(MODS)):
        if not jar.endswith(".jar"):
            continue
        try:
            got = scan(os.path.join(MODS, jar))
        except (OSError, zipfile.BadZipFile, ValueError):
            continue
        for ns, entries in got.items():
            found.setdefault(ns, {}).update(entries)

    if not found:
        print("沒有任何模組使用 BluSunrize 手冊格式", file=sys.stderr)
        return 1

    for ns, entries in sorted(found.items()):
        en_dir = os.path.join(OUT, ns, "en_us")
        os.makedirs(en_dir, exist_ok=True)
        meta = {}
        words = 0
        for entry, (raw, cfg) in sorted(entries.items()):
            text = raw.decode("utf-8")
            path = os.path.join(en_dir, entry + ".txt")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            words += len(text.split())
            meta[entry] = {
                # 錨點順序不重要，但集合必須與譯文一致，否則特殊元素不會出現
                "anchors": sorted(set(ANCHOR.findall(text))),
                "links": sorted(set(LINK.findall(text))),
                # json 設定裡的 key 就是這條目允許的錨點名
                "elements": sorted(cfg) if isinstance(cfg, dict) else [],
            }
        with open(os.path.join(OUT, ns, "meta.json"), "w", encoding="utf-8") as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=2, sort_keys=True)

        mine = os.path.join(MINE, ns)
        done = 0
        if os.path.isdir(mine):
            done = sum(1 for _, _, fs in os.walk(mine) for f in fs if f.endswith(".txt"))
        print(f"{ns}: 條目 {len(entries)}、英文 {words} 字、已譯 {done}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
