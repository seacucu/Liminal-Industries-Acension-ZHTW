"""指南譯文的結構檢查。

markdown 本身很寬容，改壞了不會報錯，只會在遊戲裡少一個 3D 場景、少一張合成表，
或是變成紅字的 Page does not exist。這支腳本比對譯文與英文原文的骨架：

  1. frontmatter 的欄位與值都相同，只有 navigation.title 可以翻譯
  2. 自訂標籤（<GameScene>、<ItemLink>、<RecipeFor>…）的名稱與屬性完全相同
     （中文語序不同，同一句裡的 <ItemLink> 先後可以變，所以不比順序）
     屬性裡的 id 是資源 ID、src 是路徑，任何一個字動到都會壞
  3. markdown 連結與圖片的目標路徑集合相同（顯示文字才翻譯；
     中文語序與英文不同，同一句裡的連結先後可以變）
  4. 標題階層（# 的數量與順序）相同
  5. 無簡體字、無殘留未譯

相對路徑與上游寫法完全一致：GuideME 認出 _zh_tw 是語系目錄後會把它從頁面 ID
剝掉，連結、parent 與 <ImportStructure src> 因此都照英文原文寫就對了。

用法：
    python scripts/verify_guide.py
"""

import collections
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "_workspace", "build", "guide")
MINE = os.path.join(ROOT, "translation", "guide")

TAG = re.compile(r"<([A-Z][A-Za-z0-9]*)((?:\s+[a-zA-Z_]+=(?:\"[^\"]*\"|\{[^}]*\}))*)\s*/?>")
ATTR = re.compile(r"([a-zA-Z_]+)=(\"[^\"]*\"|\{[^}]*\})")
LINK = re.compile(r"(!?)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s", re.M)

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from verify_translation import SIMPLIFIED  # noqa: E402


def split_frontmatter(text):
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    return parts[1], parts[2] if len(parts) > 2 else ""


def frontmatter_fields(fm):
    """回傳 [(縮排+欄位名, 值)]，順序保留。title 的值另外處理。"""
    out = []
    for line in fm.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^(\s*)([a-zA-Z_]+):\s*(.*)$", line)
        out.append((m.group(1) + m.group(2), m.group(3).strip()) if m else ("", line))
    return out


def skeleton(body):
    tags = [(m.group(1), tuple(sorted(ATTR.findall(m.group(2) or ""))))
            for m in TAG.finditer(body)]
    links = [(m.group(1), m.group(2)) for m in LINK.finditer(body)]
    return tags, links, HEADING.findall(body)


def check(en_text, tw_text):
    bad = []
    en_fm, en_body = split_frontmatter(en_text)
    tw_fm, tw_body = split_frontmatter(tw_text)

    en_fields, tw_fields = frontmatter_fields(en_fm), frontmatter_fields(tw_fm)
    if [k for k, _ in en_fields] != [k for k, _ in tw_fields]:
        bad.append(f"frontmatter 欄位不符：英文 {[k for k, _ in en_fields]}、"
                   f"譯文 {[k for k, _ in tw_fields]}")
    else:
        for (k, ev), (_, tv) in zip(en_fields, tw_fields):
            # title 是側邊欄與頁首顯示的文字，是唯一該翻的欄位
            if k.strip() == "title":
                if not tv or tv == ev:
                    bad.append(f"frontmatter 的 {k} 未翻譯：{tv}")
            elif ev != tv:
                bad.append(f"frontmatter 的 {k} 被改動：英文 {ev!r}、譯文 {tv!r}")

    en_tags, en_links, en_head = skeleton(en_body)
    tw_tags, tw_links, tw_head = skeleton(tw_body)

    if sorted(en_tags) != sorted(tw_tags):
        en_c, tw_c = collections.Counter(en_tags), collections.Counter(tw_tags)
        only_en = sorted((en_c - tw_c).elements())
        only_tw = sorted((tw_c - en_c).elements())
        bad.append(f"自訂標籤不符：缺 {only_en[:3]}、多 {only_tw[:3]}"
                   f"（英文 {len(en_tags)} 個、譯文 {len(tw_tags)} 個）")

    if sorted(en_links) != sorted(tw_links):
        bad.append(f"連結目標不符：英文 {sorted(t for _, t in en_links)}、"
                   f"譯文 {sorted(t for _, t in tw_links)}")

    if en_head != tw_head:
        bad.append(f"標題階層不符：英文 {en_head}、譯文 {tw_head}")

    zh = SIMPLIFIED.intersection(tw_text)
    if zh:
        bad.append(f"含簡體字：{''.join(sorted(zh))}")

    if tw_body.strip() == en_body.strip():
        bad.append("整頁與英文原文相同")

    return bad


def main():
    if not os.path.isdir(EN):
        print("請先執行 scripts/extract_guide.py", file=sys.stderr)
        return 1

    total = fails = missing = 0
    for ns in sorted(os.listdir(EN)):
        if not os.path.isdir(os.path.join(EN, ns)):
            continue
        for folder in sorted(os.listdir(os.path.join(EN, ns))):
            base = os.path.join(EN, ns, folder)
            if not os.path.isdir(base):
                continue
            for dirpath, _, files in sorted(os.walk(base)):
                for f in sorted(files):
                    if not f.endswith(".md"):
                        continue
                    rel = os.path.relpath(os.path.join(dirpath, f), base)
                    rel = rel.replace("\\", "/")
                    mine = os.path.join(MINE, ns, folder, rel.replace("/", os.sep))
                    total += 1
                    if not os.path.exists(mine):
                        missing += 1
                        continue
                    en_text = open(os.path.join(dirpath, f), encoding="utf-8").read()
                    tw_text = open(mine, encoding="utf-8").read()
                    bad = check(en_text, tw_text)
                    if bad:
                        fails += 1
                        print(f"✗ {ns}/{folder}/{rel}")
                        for b in bad:
                            print(f"    {b}")

    print(f"\n頁面 {total}、已譯 {total - missing}、未譯 {missing}、有問題 {fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
