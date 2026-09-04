"""對每個備有名詞表的命名空間跑一次 compose_mod_names。

名詞表放在 translation/names/<ns>.json；有表就翻，沒表就是還沒做到。
任何一個組不出來都會讓整個流程失敗，不會靜默略過。
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = os.path.join(ROOT, "translation", "names")
SCRIPT = os.path.join(ROOT, "scripts", "compose_mod_names.py")


def main():
    failed = []
    for f in sorted(os.listdir(NAMES)):
        if not f.endswith(".json"):
            continue
        ns = f[:-5]
        r = subprocess.run([sys.executable, SCRIPT, ns], capture_output=True,
                           text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        out = (r.stdout + r.stderr).strip()
        print("  " + out.replace("\n", "\n  "))
        if r.returncode:
            failed.append(ns)
    if failed:
        print(f"\n未完成：{failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
