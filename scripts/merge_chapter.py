"""把某章節的譯文片段併入 translation/lang/ftbquests.json。

片段檔的 key 為「去掉章節前綴」的短 key，例如 quest7FAC.title。

用法：
    python scripts/merge_chapter.py <章節名> <片段檔.json>
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "translation", "lang", "ftbquests.json")
EN = os.path.join(ROOT, "source", "quest_en_us.json")


def main(chapter, fragment):
    prefix = f"ftbquests.chapter.{chapter}."
    frag = json.load(open(fragment, encoding="utf-8"))
    cur = json.load(open(TARGET, encoding="utf-8"))
    en = json.load(open(EN, encoding="utf-8"))

    need = {k for k in en if k.startswith(prefix)}
    added = {prefix + k: v for k, v in frag.items()}

    unknown = sorted(set(added) - need)
    if unknown:
        print(f"片段中有 {len(unknown)} 個 key 不存在於英文抽出檔：", file=sys.stderr)
        for k in unknown[:10]:
            print(f"    {k}", file=sys.stderr)
        return 1

    cur.update(added)
    missing = sorted(need - set(cur))
    with open(TARGET, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(cur, ensure_ascii=False, indent=2) + "\n")

    print(f"章節 {chapter}：併入 {len(added)} 條，該章共需 {len(need)} 條")
    if missing:
        print(f"仍缺 {len(missing)} 條：")
        for k in missing[:15]:
            print(f"    {k.replace(prefix, '')}    <- {en[k][:60]}")
        if len(missing) > 15:
            print(f"    …另有 {len(missing) - 15} 條")
    else:
        print("該章已全譯。")
    print(f"ftbquests.json 現有 {len(cur)} 條")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
