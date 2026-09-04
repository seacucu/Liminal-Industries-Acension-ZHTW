"""產出可安裝的交付物。

三個檔案：

  build/dist/LIA-zhTW.zip                     資源包本體（所有譯文）
  build/dist/LIA-zhTW-Patch-<ver>.zip         客戶端補丁（解壓進 minecraft/）
  build/dist/LIA-zhTW-Patch-Server-<ver>.zip  伺服器補丁（FTB Quests 為伺服器權威）

客戶端補丁內含：
  config/ftbquests/quests/chapters/*.snbt   key 化骨架（不含譯文）
  config/resourcepackoverrides.json         與上游合併後的設定
  patchouli_books/<book>/{book.json,zh_tw/} Patchouli 中文書
  resourcepacks/LIA-zhTW.zip                資源包，位置已放好

執行前請先跑 scripts/build_all.py 產生所有譯文。
"""

import json
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_DIR = os.path.join(ROOT, "translation", "lang")
PATCHOULI = os.path.join(ROOT, "translation", "patchouli")
PACK_ICON = os.path.join(ROOT, "translation", "pack", "pack.png")
SKELETON = os.path.join(ROOT, "_workspace", "build", "skeleton", "config", "ftbquests", "quests", "chapters")
RPO = os.path.join(ROOT, "_workspace", "build", "patch", "config", "resourcepackoverrides.json")
META = os.path.join(ROOT, "source", "meta.json")
LICENSE = os.path.join(ROOT, "LICENSE")
DIST = os.path.join(ROOT, "_workspace", "build", "dist")

PACK_FORMAT = 15          # MC 1.20.1
VERSION = "1.1.0"


def pack_mcmeta(pack_version):
    return json.dumps({
        "pack": {
            "pack_format": PACK_FORMAT,
            "description": [
                {"text": "Liminal Industries Acension 繁體中文\n"},
                {"text": f"適用 LIA {pack_version} · 翻譯包 v{VERSION}", "color": "gray"},
            ],
        }
    }, ensure_ascii=False, indent=2)


# 固定時間戳，讓同一份原始碼永遠產出逐位元組相同的 zip。
# 否則每次打包的 hash 都不同，發布後沒人能驗證 zip 是否真的由這份原始碼產生。
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def _info(arcname):
    zi = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    return zi


def add_bytes(z, arcname, data):
    z.writestr(_info(arcname), data)


def add_file(z, arcname, path):
    with open(path, "rb") as fh:
        z.writestr(_info(arcname), fh.read())


def build_resourcepack(out_path, pack_version):
    langs = sorted(f for f in os.listdir(LANG_DIR) if f.endswith(".json"))
    total = 0
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        add_bytes(z, "pack.mcmeta", pack_mcmeta(pack_version))
        if os.path.exists(PACK_ICON):
            add_file(z, "pack.png", PACK_ICON)
        if os.path.exists(LICENSE):
            add_file(z, "LICENSE", LICENSE)
        for f in langs:
            ns = f[:-5]
            data = json.load(open(os.path.join(LANG_DIR, f), encoding="utf-8"))
            total += len(data)
            add_bytes(z, f"assets/{ns}/lang/zh_tw.json",
                      json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
    return len(langs), total


def build_client(out_path, rp_path, pack_version):
    counts = {"snbt": 0, "patchouli": 0}
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(SKELETON)):
            if f.endswith(".snbt"):
                add_file(z, f"config/ftbquests/quests/chapters/{f}",
                         os.path.join(SKELETON, f))
                counts["snbt"] += 1
        add_file(z, "config/resourcepackoverrides.json", RPO)
        for dirpath, _, files in os.walk(PATCHOULI):
            for f in sorted(files):
                full = os.path.join(dirpath, f)
                rel = os.path.relpath(full, PATCHOULI).replace("\\", "/")
                add_file(z, f"patchouli_books/{rel}", full)
                counts["patchouli"] += 1
        add_file(z, "resourcepacks/LIA-zhTW.zip", rp_path)
        if os.path.exists(LICENSE):
            add_file(z, "LICENSE", LICENSE)
        add_bytes(z, "安裝說明.txt", install_note(pack_version))
    return counts


def build_server(out_path):
    n = 0
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(SKELETON)):
            if f.endswith(".snbt"):
                add_file(z, f"config/ftbquests/quests/chapters/{f}",
                         os.path.join(SKELETON, f))
                n += 1
        if os.path.exists(LICENSE):
            add_file(z, "LICENSE", LICENSE)
    return n


def install_note(pack_version):
    return f"""Liminal Industries Acension 繁體中文翻譯包 v{VERSION}
適用 LIA {pack_version}（Minecraft 1.20.1 / Forge）

安裝方式
--------
1. 在啟動器中選擇 LIA 實例，開啟其資料夾，進入 minecraft 目錄。
2. 把本壓縮檔內的所有檔案拖進 minecraft 目錄，選擇「取代目的地中的檔案」。
   若沒有跳出取代提示，代表你放錯層級了。
3. 另外下載「模組翻譯包」放進 resourcepacks 資料夾：
       https://www.curseforge.com/minecraft/texture-packs/modstranslationpack
   檔名必須是 ModsTranslationPack-1.20.x.zip
   若檔名後面有 (1)、(2) 等後綴，請先改掉，否則不會被自動啟用。
4. 啟動遊戲。資源包順序已由設定檔鎖定，不需手動調整。

多人伺服器
----------
FTB Quests 的任務檔由伺服器提供，只裝客戶端補丁的話任務仍會是英文。
請另外把伺服器版補丁裝到伺服器端。

注意
----
LIA 更新後需重新安裝本補丁，否則任務書會變回英文。
"""


def main():
    for path, label in ((SKELETON, "key 化骨架"), (RPO, "合併後的 RPO 設定"),
                        (PATCHOULI, "Patchouli 中文書")):
        if not os.path.exists(path):
            print(f"缺少{label}：{path}\n請先執行 scripts/build_all.py 與 scripts/merge_rpo.py",
                  file=sys.stderr)
            return 1

    meta = json.load(open(META, encoding="utf-8"))
    pack_version = meta["upstream"]["pack_version"]

    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    rp = os.path.join(DIST, "LIA-zhTW.zip")
    ns_count, entry_count = build_resourcepack(rp, pack_version)
    print(f"資源包        {os.path.basename(rp):<38}"
          f"{ns_count} 個命名空間 / {entry_count} 條 / {os.path.getsize(rp)//1024} KB")

    client = os.path.join(DIST, f"LIA-zhTW-Patch-v{VERSION}.zip")
    c = build_client(client, rp, pack_version)
    print(f"客戶端補丁    {os.path.basename(client):<38}"
          f"snbt {c['snbt']} / Patchouli {c['patchouli']} 檔 / "
          f"{os.path.getsize(client)//1024} KB")

    server = os.path.join(DIST, f"LIA-zhTW-Patch-Server-v{VERSION}.zip")
    n = build_server(server)
    print(f"伺服器補丁    {os.path.basename(server):<38}"
          f"snbt {n} / {os.path.getsize(server)//1024} KB")

    print(f"\n輸出目錄：{os.path.relpath(DIST, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
