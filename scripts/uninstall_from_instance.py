"""還原 scripts/install_to_instance.py 對 LIA 實例做的所有改動。"""

import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
MANIFEST = os.path.join(ROOT, "_workspace", "build", "install_manifest.json")
SUFFIX = ".pre-lia-zhtw"


def main():
    if not os.path.exists(MANIFEST):
        print("找不到安裝紀錄，無事可還原。", file=sys.stderr)
        return 1
    m = json.load(open(MANIFEST, encoding="utf-8"))

    restored = removed = 0
    for name in m["backed_up"]:
        dest = os.path.join(INST, name.replace("/", os.sep))
        bak = dest + SUFFIX
        if os.path.exists(bak):
            shutil.copy2(bak, dest)
            os.remove(bak)
            restored += 1
    for name in m["created"]:
        dest = os.path.join(INST, name.replace("/", os.sep))
        if os.path.exists(dest):
            os.remove(dest)
            removed += 1

    # 清掉安裝時新建、現已淨空的目錄
    for name in sorted(m["created"], key=len, reverse=True):
        d = os.path.dirname(os.path.join(INST, name.replace("/", os.sep)))
        while d.startswith(INST) and d != INST and os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
            d = os.path.dirname(d)

    renamed = 0
    for new, old in m.get("renamed", []):
        rp = os.path.join(INST, "resourcepacks")
        if os.path.exists(os.path.join(rp, new)):
            shutil.move(os.path.join(rp, new), os.path.join(rp, old))
            renamed += 1

    os.remove(MANIFEST)
    print(f"已還原 {restored} 個覆蓋的檔案、移除 {removed} 個新增的檔案"
          + (f"、還原 {renamed} 個檔名。" if renamed else "。"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
