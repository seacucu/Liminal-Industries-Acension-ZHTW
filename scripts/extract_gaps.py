"""算出「模組自帶 zh_tw ＋ MTP 都沒有覆蓋」的物品／方塊／生物名。

刻意**不**把本包自己的譯文算進去：translation/lang/botania.json 會被
botania_compose.py 整份重寫，若缺口隨本包產出而縮小，重跑順序就會影響結果。
排除本包後，這份缺口清單只取決於模組與 MTP，是穩定的。

輸出：_workspace/build/gaps/missing_names.json
"""

import collections
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
OUT = os.path.join(ROOT, "_workspace", "build", "gaps", "missing_names.json")
NAME = re.compile(r"^(block|item|entity|fluid|biome)\.")


def langs_in(path):
    out = collections.defaultdict(dict)
    try:
        z = zipfile.ZipFile(path)
    except (OSError, zipfile.BadZipFile):
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

    out = {}
    for ns, d in en.items():
        miss = {k: v for k, v in d.items()
                if NAME.match(k) and k not in tw.get(ns, {}) and isinstance(v, str)}
        if miss:
            out[ns] = miss
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    total = sum(len(v) for v in out.values())
    have = {f[:-5] for f in os.listdir(os.path.join(ROOT, "translation", "names"))}
    covered = sum(len(v) for ns, v in out.items() if ns in have)
    print(f"名稱缺口 {total} 條、{len(out)} 個命名空間"
          f"（已建名詞表 {len(have)} 個，涵蓋 {covered} 條）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
