"""Gate G1 驗收：檢查 key 化骨架與抽出的英文檔。

1. key 集合是否與外部基準（VM 漢化組的 key 名稱清單）完全一致
   —— 只比對 key 名稱，不引用其任何譯文
2. 骨架 snbt 是否已無殘留明文（title / subtitle / description / task title）
3. 骨架與上游原檔的差異是否僅限於預期改寫的那些行
4. 格式保留：% 轉義、顏色碼、{image:...}
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "config", "ftbquests", "quests", "chapters")
SKEL = os.path.join(ROOT, "build", "skeleton", "config", "ftbquests", "quests", "chapters")
EN = os.path.join(ROOT, "source", "quest_en_us.json")
BASELINE = os.path.join(ROOT, "build", "verify", "vm_key_names.json")

KEYED = re.compile(r'^"?\{ftbquests\.[^}]+\}"?$')
TEXT_FIELDS = re.compile(r'^(\t+)(title|subtitle): (".*")\s*$')

failures = []
notes = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def main():
    en = json.load(open(EN, encoding="utf-8"))

    print("1. key 集合比對")
    if os.path.exists(BASELINE):
        base = set(json.load(open(BASELINE, encoding="utf-8")))
        mine = set(en)
        missing, extra = base - mine, mine - base
        # 刻意偏離：純 {image:...} 的 description 行不 key 化，保留字面。
        # 那些行不含可譯文字，給 key 只會讓譯者有機會弄壞圖片路徑。
        image_only = {k for k in missing if re.search(r"\.image\d+$", k)}
        missing -= image_only
        check("除已知偏離外與外部基準一致",
              not missing and not extra,
              f"缺 {len(missing)}、多 {len(extra)}" if (missing or extra)
              else f"{len(mine)} 個 key（基準 {len(base)}，扣除 {len(image_only)} 個圖片行）")
        for k in sorted(missing)[:5]:
            print(f"        缺: {k}")
        for k in sorted(extra)[:5]:
            print(f"        多: {k}")
        check("圖片行在骨架中保留字面",
              _literal_images() == len(image_only),
              f"骨架含 {_literal_images()} 個字面 {{image:}}，預期 {len(image_only)}")
    else:
        notes.append("找不到外部基準，略過比對")

    print("\n2. 骨架殘留明文檢查")
    residual = []
    for fname in sorted(os.listdir(SKEL)):
        for n, line in enumerate(open(os.path.join(SKEL, fname), encoding="utf-8"), 1):
            m = TEXT_FIELDS.match(line)
            if m and not KEYED.match(m.group(3)):
                residual.append(f"{fname}:{n} {line.strip()[:70]}")
            if (re.match(r'^\t\t\t\t"', line)
                    and not KEYED.match(line.strip())
                    and line.strip() != '""'
                    and not line.strip().startswith('"{image:')
                    and _in_description(fname, n)):
                residual.append(f"{fname}:{n} {line.strip()[:70]}")
    check("title / subtitle / task title / description 全部已 key 化",
          not residual, f"{len(residual)} 處殘留")
    for r in residual[:8]:
        print(f"        {r}")

    print("\n3. 骨架 vs 上游原檔的差異範圍")
    bad_diff = []
    total_changed = 0
    for fname in sorted(os.listdir(SKEL)):
        a = open(os.path.join(SRC, fname), encoding="utf-8", newline="").read().splitlines(True)
        b = open(os.path.join(SKEL, fname), encoding="utf-8", newline="").read().splitlines(True)
        if len(a) != len(b):
            bad_diff.append(f"{fname}: 行數不同 {len(a)} vs {len(b)}")
            continue
        for n, (x, y) in enumerate(zip(a, b), 1):
            if x == y:
                continue
            total_changed += 1
            if not KEYED.search(y.strip()) and '{ftbquests.' not in y:
                bad_diff.append(f"{fname}:{n} 改動不是 key 化: {y.strip()[:60]}")
    check("行數不變、每一處改動都是替換成 key",
          not bad_diff, f"共改動 {total_changed} 行")
    for d in bad_diff[:8]:
        print(f"        {d}")

    print("\n4. 格式保留")
    pct = [k for k, v in en.items() if "%" in v]
    bad_pct = [k for k in pct if re.search(r'(?<!%)%(?!%)', en[k])]
    check("% 已全部轉義為 %%", not bad_pct, f"{len(pct)} 條含 %")
    colour = [k for k, v in en.items() if re.search(r'&[0-9a-fk-or]', v)]
    image = [k for k, v in en.items() if "{image:" in v]
    print(f"        含顏色碼 {len(colour)} 條、含 {{image:}} {len(image)} 條（翻譯時必須保留）")

    empty = [k for k, v in en.items() if not v.strip()]
    check("無空值", not empty, f"{len(empty)} 條為空")

    print("\n" + ("全部通過。" if not failures else f"失敗 {len(failures)} 項：{failures}"))
    for n in notes:
        print("注意:", n)
    return 1 if failures else 0


def _literal_images():
    """骨架中保留為字面的 {image:...} 行數。"""
    n = 0
    for fname in os.listdir(SKEL):
        for line in open(os.path.join(SKEL, fname), encoding="utf-8"):
            if line.strip().startswith('"{image:'):
                n += 1
    return n


_desc_cache = {}


def _in_description(fname, lineno):
    """判斷某行是否位於 description: [ ... ] 區塊內。"""
    if fname not in _desc_cache:
        spans, open_at = [], None
        for n, line in enumerate(open(os.path.join(SKEL, fname), encoding="utf-8"), 1):
            if re.match(r'^\t\t\tdescription: \[\s*$', line):
                open_at = n
            elif open_at and re.match(r'^\t\t\t\]\s*$', line):
                spans.append((open_at, n))
                open_at = None
        _desc_cache[fname] = spans
    return any(s < lineno < e for s, e in _desc_cache[fname])


if __name__ == "__main__":
    sys.exit(main())
