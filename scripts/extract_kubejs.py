"""從 level.dat 註冊表 + init.js 抽出 KubeJS 自訂內容的翻譯 key 與英文名。

level.dat 的 Forge 註冊表快照是「實際註冊了什麼」的權威來源；
init.js 提供 displayName。兩者交叉比對，任何一邊多出或少掉都會報錯。

輸出：source/kubejs_names.json
    { "block.kubejs.carpet": {"en": "Carpet", "source": "displayName"}, ... }
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nbt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INIT_JS = os.path.join(ROOT, "source", "kubejs", "startup_scripts", "init.js")
OUT = os.path.join(ROOT, "source", "kubejs_names.json")

LEVEL_DAT = os.path.join(
    os.environ["APPDATA"], "PrismLauncher", "instances",
    "Liminal Industries Acension", "minecraft", "saves",
    "翻譯測試世界", "level.dat",
)

# init.js 裡的輔助函式。每個 entry 是 (每次呼叫產生的 (id 樣板, 顯示名) 清單)。
# 顯示名為 None 代表沿用呼叫端傳入的參數。
HELPERS = {
    "wallpaper": [("{0}", "Wallpaper"), ("{0}_soft", "Wallpaper"), ("{0}_slab", "Wallpaper Slab")],
    "strippedwallpapers": [("{0}", "Stripped Wallpaper")],
    "traffic_poles": [("{0}", None)],  # 第二個參數就是顯示名
}


def registry_ids():
    """從 level.dat 取得各註冊表中的 kubejs ID。"""
    fml = nbt.load(LEVEL_DAT)["fml"]["Registries"]
    out = {}
    for reg in ("block", "item", "fluid"):
        entries = fml.get(f"minecraft:{reg}", {}).get("ids", [])
        out[reg] = {
            e["K"].split(":", 1)[1]
            for e in entries
            if isinstance(e, dict) and str(e.get("K", "")).startswith("kubejs:")
        }
    return out


def auto_name(block_id):
    """KubeJS 沒給 displayName 時的預設：snake_case → Title Case。"""
    return " ".join(w.capitalize() for w in block_id.split("_"))


def parse_init_js():
    """回傳 {registry: {id: display_name_or_None}}，None 代表未指定 displayName。"""
    src = open(INIT_JS, encoding="utf-8").read()

    sections = {}
    for m in re.finditer(r"StartupEvents\.registry\(\s*'(\w+)'", src):
        sections[m.group(1)] = m.start()
    bounds = sorted(sections.items(), key=lambda kv: kv[1])

    result = {}
    for idx, (reg, start) in enumerate(bounds):
        end = bounds[idx + 1][1] if idx + 1 < len(bounds) else len(src)
        body = src[start:end]
        result[reg] = parse_section(body, reg)
    return result


CREATE = re.compile(
    r"""event\.create\(\s*(['"`])(.*?)\1(?:\s*,\s*(['"])(?:\w+)\3)?\s*\)""",
    re.S,
)
DISPLAY = re.compile(r"""\.displayName\(\s*(?:(['"])(.*?)\1|(\w+))\s*\)""", re.S)
HELPER_DEF = re.compile(r"let\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>\s*\{")


def parse_section(body, reg):
    """抽出這個 registry 區塊裡所有 event.create 及其 displayName。"""
    # 1. 找出輔助函式的定義範圍，之後略過（它們的 create 由呼叫端展開）
    helper_spans = []
    for m in HELPER_DEF.finditer(body):
        name = m.group(1)
        if name not in HELPERS:
            continue
        depth, i = 0, m.end() - 1
        while i < len(body):
            if body[i] == "{":
                depth += 1
            elif body[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        helper_spans.append((name, m.start(), i + 1))

    def in_helper(pos):
        return any(s <= pos < e for _, s, e in helper_spans)

    ids = {}

    # 2. 直接呼叫的 event.create
    # 往後掃 displayName 時，邊界要同時考慮「下一個 create（含輔助函式內的）」
    # 與「輔助函式定義的起點」，否則會誤讀到別人的 displayName。
    all_creates = [m.start() for m in CREATE.finditer(body)]
    stops = sorted(all_creates + [s for _, s, _ in helper_spans])

    matches = [m for m in CREATE.finditer(body) if not in_helper(m.start())]
    for m in matches:
        raw_id = m.group(2)
        if "${" in raw_id:
            raise ValueError(f"輔助函式外出現樣板字串 id: {raw_id}")
        nxt = next((s for s in stops if s > m.start()), len(body))
        chunk = body[m.end():nxt]
        d = DISPLAY.search(chunk)
        name = None
        if d:
            if d.group(3):  # displayName(變數)
                raise ValueError(f"{raw_id} 的 displayName 是變數 {d.group(3)}，需手動處理")
            name = d.group(2)
        ids[raw_id] = name

    # 3. 輔助函式呼叫展開
    for hname, tmpl in HELPERS.items():
        call = re.compile(rf"^\s*{hname}\(\s*(['\"])(.*?)\1(?:\s*,\s*(['\"])(.*?)\3)?\s*\)", re.M)
        for m in call.finditer(body):
            arg0, arg1 = m.group(2), m.group(4)
            for id_tmpl, disp in tmpl:
                ids[id_tmpl.format(arg0)] = disp if disp is not None else arg1

    return ids


def main():
    reg = registry_ids()
    parsed = parse_init_js()

    block_ids, item_ids, fluid_ids = reg["block"], reg["item"], reg["fluid"]
    # 方塊的物品形式沿用方塊的翻譯 key，不另計
    standalone_items = item_ids - block_ids - {f"{f}_bucket" for f in fluid_ids}

    declared = {}
    for section in ("block", "item", "fluid"):
        declared.update(parsed.get(section, {}))

    out, stats = {}, {"displayName": 0, "auto": 0}
    missing = []

    def add(prefix, ids):
        for i in sorted(ids):
            if i in declared and declared[i]:
                en, src = declared[i], "displayName"
            else:
                en, src = auto_name(i), "auto"
                if i not in declared:
                    missing.append(i)
            out[f"{prefix}.kubejs.{i}"] = {"en": en, "source": src}
            stats[src] += 1

    add("block", block_ids)
    add("item", standalone_items)
    add("fluid", fluid_ids)

    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2, sort_keys=True)

    print(f"註冊表：block {len(block_ids)} / item {len(item_ids)}"
          f"（獨立 {len(standalone_items)}）/ fluid {len(fluid_ids)}")
    print(f"init.js 解析出 {len(declared)} 個 id"
          f"（其中 {sum(1 for v in declared.values() if v)} 個有 displayName）")
    print(f"產出 {len(out)} 個翻譯 key："
          f"displayName {stats['displayName']}、自動生成 {stats['auto']}")
    print(f"不重複英文名：{len({v['en'] for v in out.values()})}")

    extra = set(declared) - block_ids - item_ids - fluid_ids
    if extra:
        print(f"\n[注意] init.js 有、註冊表沒有（{len(extra)}）：{sorted(extra)[:10]}")
    if missing:
        print(f"\n[注意] 註冊表有、init.js 沒對到（{len(missing)}）：{sorted(missing)[:10]}")
    print(f"\n寫入 {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
