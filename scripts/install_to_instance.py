"""把客戶端補丁裝進本機的 LIA 實例，供 G4 實機驗收。

會先把每個要覆蓋的檔案備份成 <檔名>.pre-lia-zhtw，並記錄新增的檔案清單，
之後可用 scripts/uninstall_from_instance.py 完整還原。

用法：
    python scripts/install_to_instance.py
    python scripts/uninstall_from_instance.py
"""

import json
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "_workspace", "build", "dist")
INST = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
MANIFEST = os.path.join(ROOT, "_workspace", "build", "install_manifest.json")
SUFFIX = ".pre-lia-zhtw"


def main():
    patch = next((f for f in sorted(os.listdir(DIST))
                  if f.startswith("LIA-zhTW-Patch-v")), None)
    if patch is None:
        print("找不到補丁，請先執行 scripts/build.py", file=sys.stderr)
        return 1

    backed_up, created = [], []
    with zipfile.ZipFile(os.path.join(DIST, patch)) as z:
        for name in z.namelist():
            if name.endswith("/"):
                continue
            dest = os.path.join(INST, name.replace("/", os.sep))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.exists(dest):
                bak = dest + SUFFIX
                if not os.path.exists(bak):
                    shutil.copy2(dest, bak)
                    backed_up.append(name)
            else:
                created.append(name)
            with z.open(name) as src, open(dest, "wb") as out:
                shutil.copyfileobj(src, out)

    json.dump({"patch": patch, "backed_up": backed_up, "created": created},
              open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"已安裝 {patch}")
    print(f"  覆蓋（已備份 {SUFFIX}）：{len(backed_up)} 個")
    for n in backed_up:
        print(f"      {n}")
    print(f"  新增：{len(created)} 個")
    print(f"\n紀錄：{os.path.relpath(MANIFEST, ROOT)}")

    mtp_dir = os.path.join(INST, "resourcepacks")
    names = os.listdir(mtp_dir)
    # 官方發布名是 -1.20.x.zip，但 CurseForge 下載下來常是 -1.20.zip，
    # 因此 merge_rpo 兩個檔名都寫進 default_packs，這裡的判定要一致
    known = ["ModsTranslationPack-1.20.x.zip", "ModsTranslationPack-1.20.zip"]
    if not any(n in names for n in known):
        cand = [n for n in names if n.lower().startswith("modstranslationpack")]
        print("\n[注意] resourcepacks 內沒有 RPO 認得的 MTP 檔名：")
        print(f"        需要 {' 或 '.join(known)}")
        print(f"        目前有 {cand if cand else '（無）'}")
        print("        RPO 依檔名精確比對，檔名不符就不會自動啟用。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
