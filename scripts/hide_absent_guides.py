"""把「模組沒裝、頁面卻還在」的 AE2 指南條目從側邊欄藏起來。

AE2 的指南是由 GuideME 提供的，它會掃描所有命名空間底下的 ae2guide 目錄，
把找到的頁面通通收進同一本指南。附屬模組就是這樣替 AE2 指南加章節的。

問題是模組翻譯包為了通用，替一大票 AE2 附屬模組都附了譯好的指南頁，
而那些模組本模組包並沒有收錄。頁面照樣被收進側邊欄，點進去卻滿是紅字，
因為它引用的物品、合成表與立體結構檔都不存在。對新手來說那是純粹的干擾。

GuideME 的 navigation 這個 frontmatter 欄位是選填的，NavigationTree 只會替
有該欄位的頁面建節點。所以只要用同路徑覆蓋一份「拿掉 frontmatter 的副本」，
那一頁就不會出現在側邊欄，也不會被 CategoryIndex 與物品索引收錄。
內文保留，萬一日後真的裝了那個模組，至少內容還在。

判定「有沒有裝」看的是實例的 mods 目錄有沒有任何 jar 提供該命名空間，
所以哪天模組包收錄了其中某個附屬模組，它的指南就會自動不再被藏起來。

輸出：
    _workspace/build/guide-hidden/<資源包內的原路徑>

用法：
    python scripts/hide_absent_guides.py
"""

import os
import re
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
OUT = os.path.join(ROOT, "_workspace", "build", "guide-hidden")

# GuideME 只會把 ae2guide 目錄底下的頁面收進 AE2 指南，其他 guides 目錄屬於
# 各模組自己的書，模組沒裝就根本不會有指南實例去讀它們，不必處理。
PAGE = re.compile(r"assets/([a-z0-9_.-]+)/ae2guide/(.+\.md)")
ASSET_NS = re.compile(r"assets/([a-z0-9_.-]+)/")


def installed_namespaces():
    out = set()
    mods = os.path.join(INST, "mods")
    for jar in sorted(os.listdir(mods)):
        if not jar.endswith(".jar"):
            continue
        try:
            names = zipfile.ZipFile(os.path.join(mods, jar)).namelist()
        except (OSError, zipfile.BadZipFile):
            continue
        for n in names:
            m = ASSET_NS.match(n)
            if m:
                out.add(m.group(1))
    return out


def find_mtp():
    rp = os.path.join(INST, "resourcepacks")
    for f in sorted(os.listdir(rp)):
        if f.lower().startswith("modstranslationpack") and f.lower().endswith(".zip"):
            return os.path.join(rp, f)
    return None


def strip_frontmatter(text):
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    return parts[2].lstrip("\n") if len(parts) > 2 else text


def main():
    mtp = find_mtp()
    if mtp is None:
        print("找不到模組翻譯包，無法判斷有哪些外來的指南頁", file=sys.stderr)
        return 1

    have = installed_namespaces()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)

    counts = {}
    with zipfile.ZipFile(mtp) as z:
        for n in z.namelist():
            m = PAGE.fullmatch(n)
            if not m or m.group(1) in have:
                continue
            ns = m.group(1)
            path = os.path.join(OUT, n.replace("/", os.sep))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            body = strip_frontmatter(z.read(n).decode("utf-8"))
            with open(path, "wb") as fh:
                fh.write(body.encode("utf-8"))
            counts[ns] = counts.get(ns, 0) + 1

    if not counts:
        print("沒有需要隱藏的指南頁")
        return 0
    print(f"隱藏 {sum(counts.values())} 頁，來自 {len(counts)} 個未安裝的模組：")
    for ns, c in sorted(counts.items()):
        print(f"  {ns:<22} {c:>3} 頁")
    return 0


if __name__ == "__main__":
    sys.exit(main())
