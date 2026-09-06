"""抽出 GuideME 指南（AE2 指南）的英文原文。

GuideME 的頁面是 markdown，放在 assets/<ns>/<內容根目錄>/ 底下，一頁一個 .md，
夾雜 <GameScene>、<ItemLink>、<RecipeFor> 等自訂標籤。內容根目錄下的第一層若是
語系代碼，該頁就屬於那個語系（LangUtil.getLangFromPageId），找不到當前語系的頁面
就退回預設語系，因此資源包補上 <內容根目錄>/zh_tw/ 即可，且可以分批補。

模組包可以用 kubejs/assets 覆蓋模組自帶的頁面，LIA 就整份換掉了 AE2 指南
（125 頁，其中 31 頁與模組 jar 內容不同，另有 6 頁是 jar 沒有的）。
玩家看到的是覆蓋後的版本，所以抽出時 kubejs/assets 蓋過 jar。

輸出：
    _workspace/build/guide/<ns>/<內容根目錄>/*.md   英文原文（翻譯與檢查的依據）

用法：
    python scripts/extract_guide.py
"""

import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
MODS = os.path.join(INST, "mods")
KUBEJS = os.path.join(INST, "kubejs", "assets")
OUT = os.path.join(ROOT, "_workspace", "build", "guide")
MINE = os.path.join(ROOT, "translation", "guide")

PAGE = re.compile(r"assets/([a-z0-9_.-]+)/([a-z0-9_.-]+)/(.+\.md)")


def scan(jar):
    """回傳 {(ns, 內容根目錄): {頁面路徑: 原始位元組}}。

    以「根目錄下有 index.md」判定那是一本指南，避免把模組隨手附的 README 當成頁面。
    """
    out = {}
    with zipfile.ZipFile(jar) as z:
        names = z.namelist()
        for n in names:
            m = PAGE.fullmatch(n)
            if not m:
                continue
            ns, folder, page = m.groups()
            if f"assets/{ns}/{folder}/index.md" not in names:
                continue
            out.setdefault((ns, folder), {})[page] = z.read(n)
    return out


def main():
    if not os.path.isdir(MODS):
        print(f"找不到實例 mods 目錄：{MODS}", file=sys.stderr)
        return 1

    found = {}
    for jar in sorted(os.listdir(MODS)):
        if not jar.endswith(".jar"):
            continue
        try:
            got = scan(os.path.join(MODS, jar))
        except (OSError, zipfile.BadZipFile):
            continue
        for key, pages in got.items():
            found.setdefault(key, {}).update(pages)

    # kubejs/assets 的優先權高於模組 jar，模組包在這裡換掉的頁面才是玩家看到的
    if os.path.isdir(KUBEJS):
        for (ns, folder) in list(found):
            base = os.path.join(KUBEJS, ns, folder)
            if not os.path.isdir(base):
                continue
            for dp, _, fs in os.walk(base):
                for f in fs:
                    if not f.endswith(".md"):
                        continue
                    full = os.path.join(dp, f)
                    rel = os.path.relpath(full, base).replace("\\", "/")
                    found[(ns, folder)][rel] = open(full, "rb").read()

    if not found:
        print("沒有任何模組使用 GuideME 格式的指南", file=sys.stderr)
        return 1

    for (ns, folder), pages in sorted(found.items()):
        base = os.path.join(OUT, ns, folder)
        words = 0
        for page, raw in sorted(pages.items()):
            path = os.path.join(base, page.replace("/", os.sep))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # 原樣寫出，譯文才能與上游逐位元組比對結構
            with open(path, "wb") as fh:
                fh.write(raw)
            words += len(raw.decode("utf-8").split())

        mine = os.path.join(MINE, ns, folder)
        done = sum(1 for _, _, fs in os.walk(mine) for f in fs if f.endswith(".md")) \
            if os.path.isdir(mine) else 0
        print(f"{ns}/{folder}: 頁面 {len(pages)}、英文 {words} 字、已譯 {done}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
