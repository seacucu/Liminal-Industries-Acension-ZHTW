"""從本機 Minecraft 資產取出原版 zh_tw 與 zh_cn 語系檔。

zh_tw 是正體用詞的權威；zh_cn 則用來產生「簡中術語黑名單」。
同一個 key 兩者不同時，簡中那個寫法就是本專案不該出現的用詞。

原版的非英文語系不在 client jar 裡，而是以 hash 命名存放在啟動器的 assets/objects/。
輸出：build/verify/vanilla_zh_tw.json（不進 git，隨時可重新產生）

用法：
    python scripts/fetch_vanilla_lang.py
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "_workspace", "build", "verify")
LOCALES = ("zh_tw", "zh_cn")

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
            got = {}
            for loc in LOCALES:
                entry = objects.get(f"minecraft/lang/{loc}.json")
                if not entry:
                    continue
                h = entry["hash"]
                blob = os.path.join(root, "objects", h[:2], h)
                if os.path.exists(blob):
                    got[loc] = json.load(open(blob, encoding="utf-8"))
            if "zh_tw" not in got:
                continue
            os.makedirs(OUT_DIR, exist_ok=True)
            for loc, data in got.items():
                out = os.path.join(OUT_DIR, f"vanilla_{loc}.json")
                json.dump(data, open(out, "w", encoding="utf-8"),
                          ensure_ascii=False, indent=0)
                print(f"  vanilla_{loc}.json  {len(data)} 條")
            missing = [l for l in LOCALES if l not in got]
            if missing:
                print(f"  [注意] 找不到 {missing}，簡中術語檢查會失效", file=sys.stderr)
            return 0

    print("找不到原版語系資產。", file=sys.stderr)
    print("請先在啟動器中以繁體中文啟動過遊戲一次，讓資產下載完成。", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
