"""解析 kubejs/client_scripts/rename.js，產出「翻譯 key → 模組包改名後的英文」。

模組包用 ClientEvents.lang("en_us", …) 改名，只註冊了英文；繁中語系下這些改名
全部失效。本腳本找出每個被改名物品的實際翻譯 key，供我們在 zh_tw 補上。

key 來源優先序：模組 jar 的 en_us → 原版 client jar 的 en_us。
找不到 key 或註冊表中不存在的項目會逐條列出，不靜默略過。

輸出：source/rename_targets.json
"""

import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nbt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "kubejs", "client_scripts", "rename.js")
OUT = os.path.join(ROOT, "source", "rename_targets.json")

INST = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
MODS = os.path.join(INST, "mods")
LEVEL = os.path.join(INST, "saves", "翻譯測試世界", "level.dat")
CLIENT = os.path.join(os.environ["APPDATA"], "PrismLauncher", "libraries",
                      "com", "mojang", "minecraft", "1.20.1",
                      "minecraft-1.20.1-client.jar")

# key -> (英文, 定義它的資源命名空間)
# 注意：物品的命名空間不一定等於資源命名空間。
# 例如 item.thermal.rubber 定義在 assets/thermal_foundation/lang/ 裡。
_index = None


def lang_index():
    global _index
    if _index is not None:
        return _index
    _index = {}
    with zipfile.ZipFile(CLIENT) as z:
        for k, v in json.loads(
                z.read("assets/minecraft/lang/en_us.json").decode("utf-8")).items():
            _index.setdefault(k, (v, "minecraft"))
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
                    for k, v in d.items():
                        if isinstance(v, str):
                            _index.setdefault(k, (v, m.group(1)))
        except zipfile.BadZipFile:
            continue
    return _index


def registry():
    reg = nbt.load(LEVEL)["fml"]["Registries"]
    out = set()
    for r in ("minecraft:item", "minecraft:block"):
        out |= {e["K"] for e in reg[r]["ids"] if isinstance(e, dict)}
    return out


# 物品 id 與翻譯 key 對不上、或模組根本沒提供 key 的例外。
# 每一條都經過實測確認（見 docs/known-issues.md）。
KEY_OVERRIDES = {
    # enderchests 三種儲物箱共用同一個顯示名，key 不含 ender_chest
    "enderchests:ender_chest": [("block.enderchests.chest.private", "enderchests"),
                                ("block.enderchests.chest.public", "enderchests"),
                                ("block.enderchests.chest.team", "enderchests")],
    # Thermal 這幾個物品在任何模組語系檔中都沒有 key，由本包直接提供
    "thermal:rubber":             [("item.thermal.rubber", "thermal")],
    "thermal:cured_rubber":       [("item.thermal.cured_rubber", "thermal")],
    "thermal:rubber_block":       [("block.thermal.rubber_block", "thermal")],
    "thermal:cured_rubber_block": [("block.thermal.cured_rubber_block", "thermal")],
    "thermal:sawdust":            [("item.thermal.sawdust", "thermal")],
}


def resolve_key(item_id):
    """回傳 [(翻譯 key, 資源命名空間)]；找不到則空清單。"""
    if item_id in KEY_OVERRIDES:
        return KEY_OVERRIDES[item_id]
    ns, path = item_id.split(":", 1)
    idx = lang_index()
    for prefix in ("item.", "block."):
        k = f"{prefix}{ns}.{path}"
        if k in idx:
            return [(k, idx[k][1])]
    return []


def main():
    src = open(SRC, encoding="utf-8").read()
    renames = re.findall(r"renameItem\(\s*'([^']+)'\s*,\s*'([^']+)'\s*\)", src)
    exists = registry()

    out, unresolved, dead = {}, [], []
    for item_id, new_name in renames:
        if item_id not in exists:
            dead.append((item_id, new_name))
            continue
        keys = resolve_key(item_id)
        if not keys:
            unresolved.append((item_id, new_name))
            continue
        for key, asset_ns in keys:
            out[key] = {"id": item_id, "pack_name": new_name,
                        "mod_name": lang_index().get(key, ("（模組未提供）",))[0],
                        "asset_namespace": asset_ns}

    json.dump(out, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"rename.js 共 {len(renames)} 條")
    print(f"  已解析出 key   {len(out)}")
    print(f"  註冊表不存在   {len(dead)}")
    for i, n in dead:
        print(f"      {i:<40}→ {n}   ← 上游命名空間寫錯，改名從未生效")
    print(f"  找不到 key     {len(unresolved)}")
    for i, n in unresolved:
        print(f"      {i:<40}→ {n}")
    print(f"\n寫入 {os.path.relpath(OUT, ROOT)}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
