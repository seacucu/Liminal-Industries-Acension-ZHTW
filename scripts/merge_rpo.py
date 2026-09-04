"""合併 config/resourcepackoverrides.json。

模組包本身已經有一份設定（把 Liminal Resources 鎖在 TOP、全域 force_compatible），
直接覆蓋會弄壞它。本腳本以上游快照為基底，只**追加**本翻譯包所需的條目，
並列出實際差異供人工確認。

順序語意（Phase 0 實測）：default_packs 陣列越後面 = 遊戲內顯示越上面 = 優先度越高，
所以本包要追加在最末端，MTP 次之。

輸出：build/patch/config/resourcepackoverrides.json
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "config", "resourcepackoverrides.json")
OUT = os.path.join(ROOT, "_workspace", "build", "patch", "config", "resourcepackoverrides.json")

PACK = "file/LIA-zhTW.zip"
# MTP 的檔名依下載來源而異：GitHub release 是 -1.20.x.zip，CurseForge 是 -1.20.zip。
# RPO 依檔名精確比對，缺檔的條目會被忽略，所以兩種都列進去最保險。
MTP_NAMES = ["file/ModsTranslationPack-1.20.x.zip",
             "file/ModsTranslationPack-1.20.zip"]


def main():
    base = json.load(open(SRC, encoding="utf-8"))
    added_packs, added_overrides = [], []

    packs = list(base.get("default_packs", []))
    for entry in MTP_NAMES + [PACK]:   # MTP 在前、本包在後 → 本包優先度最高
        if entry not in packs:
            packs.append(entry)
            added_packs.append(entry)
    base["default_packs"] = packs

    overrides = dict(base.get("pack_overrides", {}))
    if PACK not in overrides:
        overrides[PACK] = {
            "default_position": "TOP",
            "fixed_position": True,
            "required": True,
            "force_compatible": True,
        }
        added_overrides.append(PACK)
    base["pack_overrides"] = overrides

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(base, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("以上游快照為基底合併：")
    print(f"  default_packs 追加 {len(added_packs)} 項：{added_packs}")
    print(f"  pack_overrides 追加 {len(added_overrides)} 項：{added_overrides}")
    print("  上游既有條目全數保留：")
    for k in base["pack_overrides"]:
        if k != PACK:
            print(f"      {k}")
    print(f"\n寫入 {os.path.relpath(OUT, ROOT)}")

    # 保險：確認沒有動到上游的任何既有設定
    orig = json.load(open(SRC, encoding="utf-8"))
    for k, v in orig.items():
        if k in ("default_packs", "pack_overrides"):
            continue
        if base[k] != v:
            print(f"[錯誤] 上游欄位 {k} 被改動了", file=sys.stderr)
            return 1
    for p in orig["default_packs"]:
        if p not in base["default_packs"]:
            print(f"[錯誤] 上游的 {p} 不見了", file=sys.stderr)
            return 1
    for k, v in orig["pack_overrides"].items():
        if base["pack_overrides"].get(k) != v:
            print(f"[錯誤] 上游的 pack_overrides.{k} 被改動了", file=sys.stderr)
            return 1
    print("已確認上游設定未被更動。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
