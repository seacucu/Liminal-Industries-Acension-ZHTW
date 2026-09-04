"""從 Botania jar 抽出方塊與物品名稱，供 botania_compose.py 使用。

輸出：build/botania/names.json
    { "block.botania.carpet": {"en": "…", "tw": "…或 null"}, … }

tw 取自 jar 自帶的 zh_tw（那是一份簡中轉換品且不完整，正是要重譯的原因），
在此保留下來只是為了讓 compose 能沿用其中仍可用的詞根並列出差異。
"""

import json
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
MODS = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

PREFIXES = ("block.botania.", "item.botania.")


def main():
    if not os.path.isdir(MODS):
        print(f"找不到實例的 mods 目錄：{MODS}", file=sys.stderr)
        return 1
    jar = next((j for j in sorted(os.listdir(MODS)) if j.startswith("Botania")), None)
    if jar is None:
        print("mods 目錄中找不到 Botania jar", file=sys.stderr)
        return 1

    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))
        try:
            tw = json.loads(z.read("assets/botania/lang/zh_tw.json").decode("utf-8"))
        except KeyError:
            tw = {}

    names = {k: {"en": v, "tw": tw.get(k)}
             for k, v in en.items() if k.startswith(PREFIXES)}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(names, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    translated = sum(1 for v in names.values() if v["tw"])
    print(f"來源 {jar}")
    print(f"  名稱條目 {len(names)}（已有 zh_tw {translated}、缺 {len(names)-translated}）")
    print(f"寫入 {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
