"""依正確順序重新產生所有衍生檔案。

順序有意義，不可任意調換：

  1. keyify              上游 snbt → key 化骨架 + quest_en_us.json
  2. extract_kubejs      level.dat 註冊表 + init.js → kubejs_names.json
  3. extract_renames     rename.js → rename_targets.json（含資源命名空間）
  4. build_kubejs_lang   → translation/lang/kubejs.json
  5. botania_compose     → translation/lang/botania.json（**整份重寫**）
  6. botania_substitute  → 併入範圍外的術語與格式修正
  7. distribute_renames  → 分派改名，**必須在 botania_compose 之後**
  8. patchouli build     → translation/patchouli/
  9. botania_review      → reference/botania-name-review.html
 10. verify_translation  → 全項檢查

第 7 步若跑在第 5 步之前，botania_compose 會把整合包的改名沖掉
（例如 item.botania.ender_air_bottle 會從「閾限空氣瓶」變回「終界氣瓶」）。
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STEPS = [
    ("骨架與英文抽出", ["keyify.py"]),
    ("KubeJS 註冊表", ["extract_kubejs.py"]),
    ("改名目標解析", ["extract_renames.py"]),
    ("KubeJS 譯文", ["build_kubejs_lang.py"]),
    ("Botania 名稱組合", ["botania_compose.py"]),
    ("Botania 術語代換", ["botania_substitute.py"]),
    ("分派整合包改名", ["distribute_renames.py"]),
    ("Patchouli 書籍", ["patchouli.py", "build"]),
    ("Botania 查驗頁", ["botania_review.py"]),
    ("譯文檢查", ["verify_translation.py"]),
]


def main():
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    failed = []
    for label, argv in STEPS:
        script = os.path.join(ROOT, "scripts", argv[0])
        r = subprocess.run([sys.executable, script] + argv[1:],
                           cwd=ROOT, env=env, capture_output=True,
                           text=True, encoding="utf-8")
        mark = "OK  " if r.returncode == 0 else "FAIL"
        print(f"[{mark}] {label}")
        if r.returncode != 0:
            failed.append(label)
            for line in (r.stdout + r.stderr).strip().split("\n")[-12:]:
                print(f"        {line}")
    print()
    if failed:
        print(f"失敗 {len(failed)} 步：{failed}")
        return 1
    print("全部完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
