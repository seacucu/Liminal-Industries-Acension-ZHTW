"""還原 Phase 0 測試對 LIA 實例所做的一切改動。

測完 docs/phase0-test.md 的檢查表後執行：
    python scripts/restore_phase0.py
"""

import os
import shutil

INSTANCE = os.path.join(
    os.environ["APPDATA"],
    "PrismLauncher", "instances", "Liminal Industries Acension", "minecraft",
)

BACKUPS = [
    os.path.join(INSTANCE, "config", "ftbquests", "quests", "chapters", "escaping.snbt"),
    os.path.join(INSTANCE, "options.txt"),
]

TEST_PACK = os.path.join(INSTANCE, "resourcepacks", "LIA-zhTW-Phase0-Test.zip")


def main():
    for target in BACKUPS:
        backup = target + ".orig-backup"
        if os.path.exists(backup):
            shutil.copy2(backup, target)
            os.remove(backup)
            print(f"已還原 {os.path.basename(target)}")
        else:
            print(f"找不到備份，跳過：{os.path.basename(target)}")

    if os.path.exists(TEST_PACK):
        os.remove(TEST_PACK)
        print("已移除測試資源包")
    else:
        print("測試資源包不存在，跳過")

    print("\n還原完畢。")


if __name__ == "__main__":
    main()
