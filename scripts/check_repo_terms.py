"""掃過整個 repo 的用字：簡中術語與破折號。

verify_translation.py 只看 translation/lang/ 的產出，但簡中用詞同樣會出現在
README、腳本註解、名詞表、報告與討論文件裡。專案自己的文字寫成簡中用語，
一樣是錯的，而且 translation/names/ 與 renames.json 裡的錯還會直接進到出貨譯文。

用法：
    python scripts/check_repo_terms.py          # 掃全 repo（含 _workspace）
    python scripts/check_repo_terms.py --repo   # 只掃版控範圍
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from verify_translation import load_cn_terms, cn_exceptions, violates  # noqa: E402

EXTS = (".py", ".json", ".md", ".html", ".txt", ".snbt")
SKIP_DIRS = {".git", "__pycache__", "node_modules"}
# source/ 是上游快照（唯讀），build/ 是產物，兩者不是我們寫的
SKIP_PREFIX = ("source" + os.sep, os.path.join("_workspace", "build") + os.sep)

# 這些檔案的工作就是「列出錯誤寫法」：代換表、黑名單、術語表、逐條查驗頁。
# 它們提到簡中用詞是引用而非使用，掃到了也不是錯。
CITES_BAD_TERMS = {
    os.path.join("scripts", "botania_compose.py"),      # TERM_FIXES 對照表
    os.path.join("scripts", "botania_substitute.py"),   # SUBS 對照表
    os.path.join("scripts", "botania_book.py"),         # DRIFT 對照表
    os.path.join("scripts", "build_cn_terms.py"),       # 黑名單產生器與其說明
    os.path.join("scripts", "verify_translation.py"),   # 人工補充的 CN_TERMS
    os.path.join("scripts", "check_repo_terms.py"),     # 本檔
    os.path.join("translation", "cn-term-exceptions.json"),
    # 逐條列出改寫前後的查驗頁，「前」那一欄本來就是錯的寫法
    os.path.join("_workspace", "reference", "botania-book-review.html"),
    os.path.join("_workspace", "glossary.md"),
    os.path.join("_workspace", "glossary-botania.md"),
    os.path.join("_workspace", "known-issues.md"),      # 記錄踩過的坑
    os.path.join("_workspace", "reference", "botania-name-review.html"),  # 新舊對照
    os.path.join("_workspace", "reference", "LIA_zhTW_Coverage_Report.html"),
}


# 文件裡常需要引用錯誤寫法來說明（「Poison 的正體是劇毒不是中毒」）。
# 判定條件收得很緊：該詞必須被引號包住，而且同一行要有更正語氣的字眼。
# 光有引號不算，光有更正字眼也不算，避免整行被無條件放行。
# 專案規定：任何地方都不使用破折號。該用冒號、逗號或句號的地方就用它們。
DASH = re.compile(r"——|[—–]")


CORRECTION = re.compile(
    r"不是|而非|應為|原為|不該|誤(判|填|寫|用)|舊稱|→"
    r"|簡中(才)?作|是簡中|正體(中文)?(是|作|用)")


def is_citation(term, line):
    return bool(CORRECTION.search(line)) and (
        f"「{term}」" in line or f"「{term}" in line or f"{term}」" in line)


def files(repo_only):
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_base = os.path.relpath(base, ROOT)
        if repo_only and rel_base.startswith("_workspace"):
            continue
        for n in names:
            if not n.endswith(EXTS):
                continue
            rel = os.path.relpath(os.path.join(base, n), ROOT)
            if rel.startswith(SKIP_PREFIX) or rel in CITES_BAD_TERMS:
                continue
            yield rel


def main(argv):
    repo_only = "--repo" in argv
    terms, generated = load_cn_terms()
    if not generated:
        print("缺 cn_terms.json，請先跑 scripts/build_cn_terms.py", file=sys.stderr)
        return 1
    exc = cn_exceptions()
    hits = []
    scanned = 0
    for rel in sorted(files(repo_only)):
        try:
            text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        scanned += 1
        for line_no, line in enumerate(text.split("\n"), 1):
            if not re.search(r"[\u4e00-\u9fff]", line):
                continue
            if DASH.search(line):
                hits.append((rel, line_no, "破折號",
                             "改用冒號、逗號或句號", line.strip()))
            for cn, msg in terms:
                if violates(cn, line, exc.get(cn)) and not is_citation(cn, line):
                    hits.append((rel, line_no, cn, msg, line.strip()))

    print(f"掃描 {scanned} 個檔案，命中 {len(hits)} 處"
          + ("（僅版控範圍）" if repo_only else "（含 _workspace）"))
    by_term = {}
    for rel, ln, cn, msg, line in hits:
        by_term.setdefault((cn, msg), []).append((rel, ln, line))
    for (cn, msg), rows in sorted(by_term.items(), key=lambda x: -len(x[1])):
        print(f"\n  「{cn}」{msg}　×{len(rows)}")
        for rel, ln, line in rows[:6]:
            print(f"      {rel}:{ln}")
            print(f"        {line[:96]}")
        if len(rows) > 6:
            print(f"      …另有 {len(rows) - 6} 處")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
