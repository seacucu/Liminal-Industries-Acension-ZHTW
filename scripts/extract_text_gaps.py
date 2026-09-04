"""算出「模組自帶 zh_tw ＋ MTP 都沒有覆蓋」的說明文字，排除設定與選項介面。

與 extract_gaps.py 的差別：那支只取物品／方塊／生物名稱，這支取其餘所有字串。
同樣刻意不把本包自己的譯文算進去，讓缺口只取決於模組與 MTP。

輸出：_workspace/build/gaps/missing_text.json
"""

import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
OUT = os.path.join(ROOT, "_workspace", "build", "gaps", "missing_text.json")
NAME = re.compile(r"^(block|item|entity|fluid|biome)\.")

# 設定與選項介面：玩家只在設定畫面看到，依專案方針不譯
SKIP_KEY = re.compile(
    r"(^|\.)(config|configuration|options?|settings?|keybind|key|category|"
    r"gui\.config|midnightconfig|cloth|modmenu|fancymenu|configured)(\.|$)", re.I)
SKIP_NS = {"fancymenu", "configured", "cloth_config", "modmenu", "catalogue",
           "framework", "puzzleslib", "yungsapi", "balm", "kotlinforforge"}


def langs_in(path):
    out = collections.defaultdict(dict)
    try:
        import zipfile
        z = zipfile.ZipFile(path)
    except (OSError, Exception):
        return out
    for n in z.namelist():
        m = re.fullmatch(r"assets/([a-z0-9_.-]+)/lang/(en_us|zh_tw)\.json", n)
        if not m:
            continue
        try:
            out[m.group(1)][m.group(2)] = json.loads(z.read(n).decode("utf-8"))
        except (ValueError, KeyError):
            pass
    return out


def main():
    en, tw = collections.defaultdict(dict), collections.defaultdict(dict)
    mods = os.path.join(INST, "mods")
    for jar in sorted(os.listdir(mods)):
        if not jar.endswith(".jar"):
            continue
        for ns, d in langs_in(os.path.join(mods, jar)).items():
            en[ns].update(d.get("en_us", {}))
            tw[ns].update(d.get("zh_tw", {}))
    rp = os.path.join(INST, "resourcepacks")
    mtp = next((f for f in sorted(os.listdir(rp))
                if f.lower().startswith("modstranslationpack")), None)
    if mtp is None:
        print("找不到 MTP，缺口會被高估", file=sys.stderr)
        return 1
    for ns, d in langs_in(os.path.join(rp, mtp)).items():
        tw[ns].update(d.get("zh_tw", {}))

    out, skipped = {}, 0
    for ns, d in en.items():
        miss = {k: v for k, v in d.items()
                if k not in tw.get(ns, {}) and isinstance(v, str) and v.strip()
                and not NAME.match(k)}
        if ns in SKIP_NS:
            skipped += len(miss)
            continue
        keep = {k: v for k, v in miss.items() if not SKIP_KEY.search(k)}
        skipped += len(miss) - len(keep)
        if keep:
            out[ns] = keep
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    print(f"說明文字缺口 {sum(len(v) for v in out.values())} 條、{len(out)} 個命名空間"
          f"（設定與選項類另排除 {skipped} 條）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
