"""把 translation/renames.json 依「資源命名空間」分派進 translation/lang/<ns>.json。

命名空間取自 source/rename_targets.json（由 extract_renames.py 產出）。
這一步不能靠 key 前綴猜——item.thermal.rubber 的資源命名空間是 thermal，
但 item.thermal.rubberwood_boat 卻定義在 thermal_foundation 底下，
放錯資料夾會像 Phase 0 的麵包一樣完全失效。
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENAMES = os.path.join(ROOT, "translation", "renames.json")
TARGETS = os.path.join(ROOT, "source", "rename_targets.json")
LANG_DIR = os.path.join(ROOT, "translation", "lang")


def main():
    tr = {k: v for k, v in json.load(open(RENAMES, encoding="utf-8")).items()
          if not k.startswith("_")}
    targets = json.load(open(TARGETS, encoding="utf-8"))

    missing = sorted(set(targets) - set(tr))
    extra = sorted(set(tr) - set(targets))
    if missing:
        print(f"尚未翻譯 {len(missing)} 條：", file=sys.stderr)
        for k in missing:
            print(f"    {k:<48}{targets[k]['pack_name']}", file=sys.stderr)
    if extra:
        print(f"譯文中有 {len(extra)} 條不在改名清單：", file=sys.stderr)
        for k in extra:
            print(f"    {k}", file=sys.stderr)
    if missing or extra:
        return 1

    by_ns = {}
    for key, val in tr.items():
        by_ns.setdefault(targets[key]["asset_namespace"], {})[key] = val

    for ns, entries in sorted(by_ns.items()):
        path = os.path.join(LANG_DIR, f"{ns}.json")
        cur = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
        before = len(cur)
        cur.update(entries)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(cur, fh, ensure_ascii=False, indent=2, sort_keys=True)
        note = "新建" if before == 0 else f"原有 {before}"
        print(f"  assets/{ns:<22} +{len(entries):>2} 條（{note} → {len(cur)}）")

    print(f"\n共 {len(tr)} 條，分派至 {len(by_ns)} 個命名空間")
    return 0


if __name__ == "__main__":
    sys.exit(main())
