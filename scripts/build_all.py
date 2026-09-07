"""依正確順序重新產生所有衍生檔案。

順序有意義，不可任意調換：

  0. fetch_vanilla_lang  原版 zh_tw/zh_cn → build/verify/（術語檢查的基準語料）
  0b. build_cn_terms     由官方兩體語系檔產生簡中術語黑名單
  1. keyify              上游 snbt → key 化骨架 + quest_en_us.json
  2. extract_kubejs      level.dat 註冊表 + init.js → kubejs_names.json
  3. extract_renames     rename.js → rename_targets.json（含資源命名空間）
  4. build_kubejs_lang   → translation/lang/kubejs.json
  4b. extract_botania_names  Botania jar → build/botania/names.json
  5. botania_compose     → translation/lang/botania.json（**整份重寫**）
  6. botania_substitute  → 併入範圍外的術語與格式修正
  7. distribute_renames  → 分派改名，**必須在 botania_compose 之後**
  8. patchouli build     → translation/patchouli/
 8b. build_books        → build/books/（TConstruct 六本書缺的中文頁）
  9. botania_review      → reference/botania-name-review.html
 9b. extract_manual      IE 手冊 jar → build/manual/（翻譯與檢查的英文基準）
 9c. extract_guide       AE2 指南 jar → build/guide/（同上）
 9d. hide_absent_guides  模組沒裝卻被 MTP 帶進 AE2 指南的頁面 → build/guide-hidden/
 10. verify_translation  → 全項檢查
 11. verify_manual       → 手冊譯文的標記結構檢查
 12. verify_guide        → 指南譯文的標記結構檢查

第 7 步若跑在第 5 步之前，botania_compose 會把模組包的改名沖掉
（例如 item.botania.ender_air_bottle 會從「閾限空氣瓶」變回「終界氣瓶」）。

所有中間產物都在 build/（未納入版控），因此全新 clone 只要跑這支腳本
就能從 source/ 與本機的 LIA 實例重新產生一切。
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STEPS = [
    ("原版 zh_tw/zh_cn 基準", ["fetch_vanilla_lang.py"]),
    ("簡中術語黑名單", ["build_cn_terms.py"]),
    ("骨架與英文抽出", ["keyify.py"]),
    ("KubeJS 註冊表", ["extract_kubejs.py"]),
    ("改名目標解析", ["extract_renames.py"]),
    ("KubeJS 譯文", ["build_kubejs_lang.py"]),
    ("Botania 名稱抽出", ["extract_botania_names.py"]),
    ("Botania 名稱組合", ["botania_compose.py"]),
    ("Botania 術語代換", ["botania_substitute.py"]),
    ("分派模組包改名", ["distribute_renames.py"]),
    ("分派補充物品名", ["distribute_extras.py"]),
    ("名稱缺口盤點", ["extract_gaps.py"]),
    ("說明文字缺口盤點", ["extract_text_gaps.py"]),
    ("補譯缺口名稱", ["compose_all_names.py"]),
    ("補譯說明文字", ["apply_all_text.py"]),
    ("Patchouli 書籍", ["patchouli.py", "build"]),
    ("Mantle 書本頁面", ["build_books.py"]),
    ("Botania 查驗頁", ["botania_review.py"]),
    ("手冊原文抽出", ["extract_manual.py"]),
    ("指南原文抽出", ["extract_guide.py"]),
    ("隱藏未安裝模組的指南", ["hide_absent_guides.py"]),
    ("譯文檢查", ["verify_translation.py"]),
    ("手冊檢查", ["verify_manual.py"]),
    ("指南檢查", ["verify_guide.py"]),
    ("全 repo 用詞檢查", ["check_repo_terms.py"]),
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
