"""對每個備有說明文字檔的命名空間跑一次 apply_text。

文字檔放在 translation/text/<ns>.json；有檔就是翻過了，沒有就是還沒做到。
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT = os.path.join(ROOT, "translation", "text")
SCRIPT = os.path.join(ROOT, "scripts", "apply_text.py")


def main():
    if not os.path.isdir(TEXT):
        print("  尚無說明文字檔")
        return 0
    failed = []
    for f in sorted(os.listdir(TEXT)):
        if not f.endswith(".json"):
            continue
        ns = f[:-5]
        r = subprocess.run([sys.executable, SCRIPT, ns], capture_output=True,
                           text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        print("  " + (r.stdout + r.stderr).strip().replace("\n", "\n  "))
        if r.returncode:
            failed.append(ns)
    if failed:
        print(f"\n未完成：{failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
