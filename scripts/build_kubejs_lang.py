"""由 translation/kubejs-names.json 展開成 translation/lang/kubejs.json。

source/kubejs_names.json 是權威 key 清單（自 level.dat 的 Forge 註冊表取得）。
本腳本逐 key 查譯名：先看 _BY_ID 的個別指定，再看英文名對照表。
任何一個 key 找不到譯名都會報錯 —— 不容許靜默漏譯。
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = os.path.join(ROOT, "source", "kubejs_names.json")
MAP = os.path.join(ROOT, "translation", "kubejs-names.json")
OUT = os.path.join(ROOT, "translation", "lang", "kubejs.json")


def main():
    keys = json.load(open(KEYS, encoding="utf-8"))
    raw = json.load(open(MAP, encoding="utf-8"))
    by_id = raw.get("_BY_ID", {})
    by_en = {k: v for k, v in raw.items() if not k.startswith("_")}

    out, missing = {}, []
    for k, info in sorted(keys.items()):
        if k in by_id:
            out[k] = by_id[k]
        elif info["en"] in by_en:
            out[k] = by_en[info["en"]]
        else:
            missing.append((k, info["en"]))

    if missing:
        print(f"缺少譯名 {len(missing)} 條：", file=sys.stderr)
        for k, en in missing[:20]:
            print(f"    {k:<44}{en}", file=sys.stderr)
        return 1

    unused_en = set(by_en) - {i["en"] for i in keys.values()}
    unused_id = set(by_id) - set(keys)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"展開 {len(out)} 個 key（英文名 {len(by_en)} 條 + 個別指定 {len(by_id)} 條）")
    print(f"不重複譯名：{len(set(out.values()))}")
    if unused_en:
        print(f"[注意] 對照表中有 {len(unused_en)} 個英文名沒對到任何 key：{sorted(unused_en)[:5]}")
    if unused_id:
        print(f"[注意] _BY_ID 有 {len(unused_id)} 個 key 不存在：{sorted(unused_id)[:5]}")
    print(f"寫入 {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
