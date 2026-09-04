"""從本機 Minecraft 資產取出原版 zh_tw 語系檔，作為術語檢查的基準。

原版的非英文語系不在 client jar 裡，而是以 hash 命名存放在啟動器的 assets/objects/。
輸出：build/verify/vanilla_zh_tw.json（不進 git，隨時可重新產生）

用法：
    python scripts/fetch_vanilla_lang.py
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_zh_tw.json")

ASSET_ROOTS = [
    os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "assets"),
    os.path.join(os.environ.get("APPDATA", ""), ".minecraft", "assets"),
]


def main():
    for root in ASSET_ROOTS:
        idx_dir = os.path.join(root, "indexes")
        if not os.path.isdir(idx_dir):
            continue
        for idx in sorted(os.listdir(idx_dir)):
            if not idx.endswith(".json"):
                continue
            objects = json.load(open(os.path.join(idx_dir, idx), encoding="utf-8"))["objects"]
            entry = objects.get("minecraft/lang/zh_tw.json")
            if not entry:
                continue
            h = entry["hash"]
            blob = os.path.join(root, "objects", h[:2], h)
            if not os.path.exists(blob):
                continue
            data = json.load(open(blob, encoding="utf-8"))
            os.makedirs(os.path.dirname(OUT), exist_ok=True)
            json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
            print(f"取自 {os.path.relpath(blob, root)}（index {idx}）")
            print(f"寫入 {os.path.relpath(OUT, ROOT)}，共 {len(data)} 條")
            return 0

    print("找不到原版 zh_tw 語系資產。", file=sys.stderr)
    print("請先在啟動器中以繁體中文啟動過遊戲一次，讓資產下載完成。", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
