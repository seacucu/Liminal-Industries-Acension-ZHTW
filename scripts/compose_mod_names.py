"""以「修飾詞 + 名詞核心」組出某模組所有缺譯的物品／方塊名。

修飾詞（木材、顏色、染料等）一律從原版 zh_tw 推導，不手寫——
先前 Cobbled 被寫成「圓石」、Stripped 寫成「去皮」都是手寫惹的禍。

名詞核心放在 translation/names/<ns>.json，只需列去掉修飾後的部分。
組不出來的會列出來，必須補進名詞表，不會靜默略過。

用法：
    python scripts/compose_mod_names.py <命名空間> [--dry]
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAPS = os.path.join(ROOT, "_workspace", "build", "gaps", "missing_names.json")
NAMES = os.path.join(ROOT, "translation", "names")
LANG_DIR = os.path.join(ROOT, "translation", "lang")
VANILLA_TW = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_zh_tw.json")
CLIENT = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "libraries",
                      "com", "mojang", "minecraft", "1.20.1",
                      "minecraft-1.20.1-client.jar")


def modifiers():
    """從原版語系檔導出「英文修飾詞 → 中文」。"""
    ven = json.loads(zipfile.ZipFile(CLIENT).read(
        "assets/minecraft/lang/en_us.json").decode("utf-8"))
    vtw = json.load(open(VANILLA_TW, encoding="utf-8"))
    out = {}
    # 木材：<wood>_planks「橡木材」→ 橡木；顏色：<colour>_wool「黑色羊毛」→ 黑色
    for key_suffix, en_suffix, tw_suffix in (("planks", "Planks", "材"),
                                             ("wool", "Wool", "羊毛")):
        for k, v in ven.items():
            m = re.fullmatch(rf"block\.minecraft\.(\w+)_{key_suffix}", k)
            if not m or k not in vtw:
                continue
            e, t = v[: -len(en_suffix)].strip(), vtw[k]
            if t.endswith(tw_suffix):
                out[e] = t[: -len(tw_suffix)]
    return out


def main(argv):
    ns = argv[0]
    dry = "--dry" in argv
    gaps = json.load(open(GAPS, encoding="utf-8"))[ns]
    path = os.path.join(LANG_DIR, f"{ns}.json")
    have = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    raw = json.load(open(os.path.join(NAMES, f"{ns}.json"), encoding="utf-8"))
    nouns = {k: v for k, v in raw.items() if not k.startswith("_")}
    mods = modifiers()
    # 模組自己的修飾詞寫法（例如 AA 用 LightBlue／Silver 而非原版的 Light Blue／Light Gray）
    mods.update(raw.get("_modifiers", {}))
    order = sorted(mods, key=len, reverse=True)

    done, failed = {}, []
    for key, en in gaps.items():
        # 名詞表若直接命中整串（單件物品），優先採用
        if en in nouns:
            done[key] = nouns[en]
            continue
        prefix = ""
        rest = en
        for e in order:
            if rest.startswith(e + " "):
                prefix, rest = mods[e], rest[len(e) + 1:]
                break
        if rest in nouns:
            done[key] = prefix + nouns[rest]
        elif key in have:
            # 名詞表沒有這個核心、但譯文已存在 ⇒ 由模組專用腳本負責（如 botania_compose）
            continue
        else:
            failed.append((key, en))

    print(f"{ns}：缺 {len(gaps)} 條 → 組出 {len(done)}，未組出 {len(failed)}")
    for key, en in failed[:25]:
        print(f"    未組出  {en}")
    if failed:
        print(f"\n請把上列核心補進 translation/names/{ns}.json")
        return 1
    if dry:
        return 0
    cur = dict(have)
    before = len(cur)
    cur.update(done)
    json.dump(cur, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    print(f"寫入 translation/lang/{ns}.json（{before} → {len(cur)} 條）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
