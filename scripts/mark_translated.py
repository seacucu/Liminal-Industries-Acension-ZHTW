"""把覆蓋率報告中某個模組標記為「本包已譯」。

每翻完一個模組就跑一次，讓報告與實際產出保持同步。先前報告與現實脫節
（Botania 被標成「內建繁中」）就是吃過這個虧。
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT = os.path.join(ROOT, "_workspace", "reference", "LIA_zhTW_Coverage_Report.html")
LANG_DIR = os.path.join(ROOT, "translation", "lang")


def main(argv):
    if len(argv) < 2:
        print("用法：mark_translated.py <modid> <說明>", file=sys.stderr)
        return 1
    modid, note = argv[0], argv[1]
    ns = argv[2] if len(argv) > 2 else modid
    path = os.path.join(LANG_DIR, f"{ns}.json")
    n = len(json.load(open(path, encoding="utf-8"))) if os.path.exists(path) else 0

    s = open(REPORT, encoding="utf-8").read()
    pat = re.compile(r'\{[^{}]*modid:\s*"' + re.escape(modid) + r'"[^{}]*\}')
    m = pat.search(s)
    if not m:
        print(f"報告中找不到 modid={modid}", file=sys.stderr)
        return 1
    old = m.group(0)
    new = re.sub(r'cat:\s*\d+', "cat:0", old)
    new = re.sub(r'note:\s*"[^"]*"',
                 'note:"【本包已譯】' + note.replace('"', "'")
                 + f'　本包提供 {n} 條。"', new)
    open(REPORT, "w", encoding="utf-8").write(s.replace(old, new))
    print(f"報告已更新：{modid} → cat:0（本包 {n} 條）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
