"""把 translation/text/<ns>.json 的說明文字併進 translation/lang/<ns>.json。

與 compose_mod_names 分開：名稱可以用「修飾詞＋名詞」組出來，說明文字不行，
必須逐條翻譯。這裡只做「key 對照 + 併入」，並確認每一條都真的還缺。

用法：
    python scripts/apply_text.py <命名空間> [--dry]
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAPS = os.path.join(ROOT, "_workspace", "build", "gaps", "missing_text.json")
TEXT = os.path.join(ROOT, "translation", "text")
LANG_DIR = os.path.join(ROOT, "translation", "lang")


def main(argv):
    ns = argv[0]
    dry = "--dry" in argv
    gaps = json.load(open(GAPS, encoding="utf-8")).get(ns, {})
    src = json.load(open(os.path.join(TEXT, f"{ns}.json"), encoding="utf-8"))
    mine = {k: v for k, v in src.items() if not k.startswith("_")}
    # 模組自帶譯文有錯時，在 _override 列出 key 與理由即可覆寫。
    # 一般 key 仍必須在缺口清單中，避免拼錯的 key 靜默寫進去。
    override = src.get("_override", {})
    mine.update({k: v["value"] for k, v in override.items()})

    unknown = [k for k in mine if k not in gaps and k not in override]
    if unknown:
        print(f"{ns}：{len(unknown)} 個 key 不在缺口清單中（可能已有譯文或拼錯）",
              file=sys.stderr)
        for k in unknown[:8]:
            print(f"    {k}", file=sys.stderr)
        return 1

    rest = len(gaps) - len(mine)
    print(f"{ns}：缺 {len(gaps)} 條 → 本次補 {len(mine)}，尚餘 {rest}")
    if dry:
        return 0
    path = os.path.join(LANG_DIR, f"{ns}.json")
    cur = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    before = len(cur)
    cur.update(mine)
    json.dump(cur, open(path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    print(f"寫入 translation/lang/{ns}.json（{before} → {len(cur)} 條）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
