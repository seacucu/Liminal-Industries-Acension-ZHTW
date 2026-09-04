"""把 translation/extra-items.json 依「實際資源命名空間」分派進 translation/lang/。

命名空間不能用 key 的第二段去猜，item.thermal.rubberwood_boat 定義在
assets/thermal_foundation/lang/ 底下，放錯資料夾會完全失效（Phase 0 的麵包就是這樣）。
因此本腳本索引所有模組與原版的 en_us，反查每個 key 由哪個資源命名空間定義；
若任何語系檔都沒有定義（例如 Thermal 的機器名由 CoFH 執行時生成），
才退回使用 key 自身的命名空間。
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRAS = os.path.join(ROOT, "translation", "extra-items.json")
LANG_DIR = os.path.join(ROOT, "translation", "lang")
MODS = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")
CLIENT = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "libraries",
                      "com", "mojang", "minecraft", "1.20.1",
                      "minecraft-1.20.1-client.jar")


def lang_index():
    """key -> 定義它的資源命名空間。"""
    idx = {}
    if os.path.exists(CLIENT):
        with zipfile.ZipFile(CLIENT) as z:
            for k in json.loads(
                    z.read("assets/minecraft/lang/en_us.json").decode("utf-8")):
                idx.setdefault(k, "minecraft")
    if os.path.isdir(MODS):
        for jar in sorted(os.listdir(MODS)):
            if not jar.endswith(".jar"):
                continue
            try:
                with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
                    for n in z.namelist():
                        m = re.fullmatch(r"assets/([a-z0-9_.-]+)/lang/en_us\.json", n)
                        if not m:
                            continue
                        try:
                            d = json.loads(z.read(n).decode("utf-8"))
                        except ValueError:
                            continue
                        for k in d:
                            idx.setdefault(k, m.group(1))
            except zipfile.BadZipFile:
                continue
    return idx


def main():
    extras = {k: v for k, v in json.load(open(EXTRAS, encoding="utf-8")).items()
              if not k.startswith("_")}
    idx = lang_index()

    by_ns, synthesised = {}, []
    for key, val in extras.items():
        ns = idx.get(key)
        if ns is None:
            ns = key.split(".")[1]          # 無人定義 → 用 key 自身的命名空間
            synthesised.append(key)
        by_ns.setdefault(ns, {})[key] = val

    for ns, entries in sorted(by_ns.items()):
        path = os.path.join(LANG_DIR, f"{ns}.json")
        cur = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
        before = len(cur)
        cur.update(entries)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(cur, fh, ensure_ascii=False, indent=2, sort_keys=True)
        note = "新建" if before == 0 else f"原有 {before}"
        print(f"  assets/{ns:<24} +{len(entries):>2} 條（{note} → {len(cur)}）")

    print(f"\n共 {len(extras)} 條，分派至 {len(by_ns)} 個命名空間")
    if synthesised:
        print(f"其中 {len(synthesised)} 條在任何語系檔中都無人定義，"
              f"由本包首次提供（需實機確認是否生效）：")
        for k in synthesised:
            print(f"    {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
