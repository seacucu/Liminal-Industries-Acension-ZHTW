"""Patchouli 書籍的抽取與回填。

Patchouli 的書頁是 JSON，只有少數欄位是文字；其餘（物品 ID、座標、多方塊圖樣）
一律不可動。本腳本只碰白名單欄位，其他原樣複製。

用法：
    python scripts/patchouli.py extract   # source/ → source/patchouli_en_us.json
    python scripts/patchouli.py build     # 譯文 → translation/patchouli/<book>/zh_tw/
"""

import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "patchouli_books")
EN = os.path.join(ROOT, "source", "patchouli_en_us.json")
TR = os.path.join(ROOT, "translation", "patchouli.json")
OUT = os.path.join(ROOT, "translation", "patchouli")

# 只有這些欄位是給玩家看的文字
TEXT_FIELDS = {"name", "description", "title", "text", "landing_text"}


def walk(node, path, hits):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in TEXT_FIELDS and isinstance(v, str):
                hits.append((path + [k], v))
            else:
                walk(v, path + [k], hits)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + [str(i)], hits)


def each_file():
    for book in sorted(os.listdir(SRC)):
        bdir = os.path.join(SRC, book)
        if not os.path.isdir(bdir):
            continue
        for dirpath, _, files in os.walk(bdir):
            for f in sorted(files):
                if f.endswith(".json"):
                    full = os.path.join(dirpath, f)
                    yield book, os.path.relpath(full, bdir).replace("\\", "/"), full


def extract():
    out = {}
    for book, rel, full in each_file():
        data = json.load(open(full, encoding="utf-8"))
        hits = []
        walk(data, [], hits)
        for path, text in hits:
            out[f"{book}/{rel}#{'/'.join(path)}"] = text
    json.dump(out, open(EN, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    uniq = len(set(out.values()))
    print(f"抽出 {len(out)} 條可譯文字（不重複 {uniq} 條）")
    print(f"寫入 {os.path.relpath(EN, ROOT)}")


def set_path(node, path, value):
    for p in path[:-1]:
        node = node[int(p)] if isinstance(node, list) else node[p]
    last = path[-1]
    if isinstance(node, list):
        node[int(last)] = value
    else:
        node[last] = value


def build():
    tr = {k: v for k, v in json.load(open(TR, encoding="utf-8")).items()
          if not k.startswith("_")}
    en = json.load(open(EN, encoding="utf-8"))

    missing = sorted(set(en) - set(tr))
    if missing:
        print(f"尚未翻譯 {len(missing)} 條：", file=sys.stderr)
        for k in missing[:15]:
            print(f"    {k}\n        {en[k][:70]}", file=sys.stderr)
        return 1

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    count = 0
    for book, rel, full in each_file():
        data = json.load(open(full, encoding="utf-8"))
        hits = []
        walk(data, [], hits)
        for path, _ in hits:
            key = f"{book}/{rel}#{'/'.join(path)}"
            set_path(data, path, tr[key])
            count += 1
        # en_us/... → zh_tw/...；book.json 之類不在語系目錄下的原樣保留位置
        dest_rel = rel.replace("en_us/", "zh_tw/", 1)
        dest = os.path.join(OUT, book, dest_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=4)
            fh.write("\n")
    print(f"回填 {count} 條，輸出至 {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "extract":
        extract()
    elif cmd == "build":
        sys.exit(build())
    else:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
