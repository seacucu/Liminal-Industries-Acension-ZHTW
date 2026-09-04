# 已知未翻與已知限制

## 一、其他模組自帶 zh_tw 的品質缺口

`scripts/audit_mod_langs.py` 稽核了實例中 36 個自帶 `zh_tw` 的命名空間。扣掉 MTP 已覆蓋的部分，**10 個命名空間的缺口會被玩家看到**。本專案第一版只處理了 botania：

| 命名空間 | en_us | 模組已譯 | 缺譯 | 其他問題 | 本包處理 |
|---|---|---|---|---|---|
| botania | 3,472 | 2,496 | 980 | 半形標點 30%、簡體 3、簡中用詞 14、色碼誤用 `&` 25 | ✅ 名稱 1,060 條重譯 + 391 條術語與格式修正 |
| tconstruct | 2,791 | 2,375 | 523 | 簡體 3 | ❌ |
| neapolitan | 276 | 151 | 145 | 簡體 1 | ❌ |
| jade | 280 | 211 | 70 | — | ❌ |
| supplementaries | 607 | 555 | 52 | 簡體 2 | ❌ |
| copycats | 67 | 27 | 40 | — | ❌ |
| entity_model_features | 278 | 268 | 10 | 半形標點 30% | ❌ |
| create | 3,366 | 3,357 | 9 | 簡體 17、簡中用詞 1 | ❌ |
| mekanism | 1,656 | 1,655 | 1 | 半形標點 25%、簡體 2 | ❌ |
| cofh_core | 215 | 215 | 0 | 簡體 8 | ❌ |

> 「內建繁中」不等於「品質可用」。`reference/LIA_zhTW_Coverage_Report.html` 的第 1 類是依公開資訊判定的，只有 botania 經過實際拆 jar 驗證並已更正。其餘 9 個若要處理，應先照同樣程序核實。

## 二、完全沒有繁中的模組

| 模組 | 狀況 |
|---|---|
| **Thermal Series** | `thermal` 命名空間完全沒有繁中。jar 只帶 `thermal_foundation` 的 121 條 UI 字串，MTP 不涵蓋 `thermal`。任務書提到的 Rock Gen（造岩機）等物品在遊戲內顯示英文 |
| **End Remastered** | 模組無任何中文，MTP 亦不涵蓋。LIA 覆寫了其中 77 條英文（39 條與模組原文不同）。**12 顆眼睛是「逃離」整章的核心**，已納入本包翻譯範圍 |

## 三、Botania 本次未處理的部分

範圍限定在 `block.botania.*` 與 `item.botania.*` 的名稱。以下維持現狀：

- `botania.page.*`（1,008 條，植物魔法辭典內文）——只做了術語代換，未重譯
- 既有譯文的**半形標點**（719 條）——屬重譯範疇
- 仍缺譯的非名稱條目——遊戲內顯示英文

## 三之二、翻譯範圍已涵蓋的部分

| 項目 | 條數 | 說明 |
|---|---|---|
| FTB Quests 任務書 | 559 | 七章全譯 |
| KubeJS 自訂方塊／物品 | 212 | 由 level.dat 註冊表取得權威清單 |
| Botania 名稱重譯 + 術語代換 | 1,451 | 見支線 B |
| End Remastered | 77 | 模組無任何中文，12 顆眼睛是「逃離」章的核心 |
| 整合包改名（rename.js） | 46 | 分派至 20 個資源命名空間 |
| Patchouli 兩本書 | 59 條文字 | 現實框架建造指南、召喚入門 |

## 四、整合包自身的缺陷（本包已修或記錄）

| 項目 | 說明 | 處理 |
|---|---|---|
| `rename.js` 45 條改名 | 只註冊 `en_us`，繁中語系下全數失效 | 納入翻譯範圍 |
| `kubejs/assets/*/lang/en_us.json` | 7 個命名空間 1,165 條，同樣只有 en_us | endrem 77 條納入；其餘評估中 |
| 23 個交通標誌方塊 | 顯示名全部是小寫 `sign`，彼此無法區分 | 已依 ID 給可辨識名稱（停止標誌、出口標誌…），屬刻意偏離原文 |
| `rename.js` 有一條失效 | `actually_additions:rice` 命名空間寫錯（應為 `actuallyadditions`），該改名從未生效 | 本包不修——修了會與上游英文顯示不一致 |
| Thermal 5 個物品無 lang key | `thermal:rubber`／`cured_rubber`／`rubber_block`／`cured_rubber_block`／`sawdust` 在任何模組語系檔中都沒有翻譯 key | 由本包直接提供 zh_tw |
| Botania 色碼誤用 | 21 條用 `&` 而非 `§`，遊戲內會顯示成字面的「&7 級」。zh_tw 是唯一犯此錯的主要語系 | 已修 |
| Botania 數值誤植 | `manaweave.desc0` 英文 40%%、譯文寫 35% | 已修 |
| 16 個 Azulejo | 英文全部同名 | 統一為「葡式花磚」並加序號 |

## 四之二、需覆寫上游檔案之處

除了 key 化的 snbt 與 `config/resourcepackoverrides.json` 之外，還有：

| 檔案 | 原因 |
|---|---|
| `patchouli_books/<book>/book.json` ×2 | Patchouli 的書名與封面文字寫在 `book.json`，非語系檔。要翻譯書名就必須覆寫 |

## 五、其他文字面

| 來源 | 狀況 |
|---|---|
| FancyMenu 標題畫面 | `config/fancymenu/`，第一版不處理 |
| `kubejs/room_notes.txt` | 開發者筆記，非遊戲內文字，不需翻譯 |

## 六、結構性限制

- **key 化 snbt 是 config 覆寫**：LIA 更新時會被覆蓋，需重跑生成器並重裝補丁
- **`config/resourcepackoverrides.json` 需合併**：整合包自身已有設定，不可直接覆蓋
- **多人伺服器**：只裝客戶端補丁時任務仍為英文，需另裝伺服器版
