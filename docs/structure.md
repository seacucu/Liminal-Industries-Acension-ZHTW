# LIA 翻譯相關結構勘查結果

> **狀態：已完成。** 三項需進遊戲確認的項目已於 Gate G0 實測通過，結論見文末。

## 實例資訊

| 項目 | 值 |
|------|-----|
| 整合包顯示名稱 | Liminal Industries Acension |
| 實例路徑 | `%APPDATA%\PrismLauncher\instances\Liminal Industries Acension` |
| 偵測到的 LIA 版本 | `1.19`（CurseForge projectID 1389281 / versionID 8728879，作者 Aceplante）|
| Minecraft / 載入器 | 1.20.1 / Forge 47.4.13 |
| 模組數 | 185 |
| 勘查日期 | 2026-09-03 |

另有 `Liminal Industries - Rescripted`（LIR）實例可作對照，非本專案目標。

## 任務書（FTB Quests）

### 存放方式

- [x] **硬寫在 snbt**：明文在 `config/ftbquests/quests/chapters/*.snbt`
- [ ] ~~已外部化為 lang key~~
- [ ] ~~混合~~

**結論明確：零 key 化。** 對 7 個章節檔搜尋 `{ftbquests...}` 形式的 key，零命中。

同時確認 `ftb-quests-forge-2001.4.16.jar` **沒有** 1.21 線才有的 `config/ftbquests/quests/lang/` 分檔功能（jar 內無對應 package）。但它**支援 `{key}` 形式的任務文字**——jar 內含 `ftbquests.translation_key.title` / `.quest_subtitle` / `.chapter_subtitle` / `.quest_desc`、`"This may be a translation key"`、`"No translation for %s in current locale '%s'"`，以及 `QuestKeyReferenceScreen`。ATM9 - To the Sky（同為 1.20.1 Forge）整本任務書即走此機制。

### 實際路徑

```text
config/ftbquests/quests/chapters/escaping.snbt
config/ftbquests/quests/chapters/poolrooms.snbt
config/ftbquests/quests/chapters/sector_1.snbt  ~  sector_5.snbt
config/ftbquests/quests/chapter_groups.snbt     （28 bytes，無文字）
config/ftbquests/quests/data.snbt               （499 bytes）
```

檔案為 **CRLF** 行尾——生成器必須保留。

### 抽樣證據

`sector_1.snbt`：

```
description: [
    "You can use brushes to sweep up carpet dust."
    ""
    "&oNote: The effects of long term carpet dust exposure are unknown."
]
subtitle: "Do not Inhale this..."
title: "This Place could use some Sweeping"
```

明文，非 key。

### 規模

| 項目 | 數量 |
|------|------|
| 章節（chapters） | 7（escaping、poolrooms、sector_1 ~ 5）|
| 任務（quests） | 248 |
| `title` 欄位 | 172 |
| `subtitle` 欄位 | 77 |
| `description` 區塊 | 158（約 1,930 行，含空行）|
| 需譯字串條數 | **559**（見下）|
| 英文字元量 | 約 54,000 |
| 格式標記 | 僅 `&o`（5 處）與 `{image:...}`（6 處）|

565 這個數字有外部佐證：VM 漢化組的 SevenKiyo 已對同一份內容做過 key 化，產出 565 條 `en_us.json`。經比對，**248 個 quest ID 在其版本與本機 1.19 之間七章全數相同（零漂移）**，565 個 key 與 565 條 JSON 完美 1:1，563/565 英文逐字相同——唯二差異是 `%` 依 lang 格式規定轉義為 `%%`。

> VM 的 `CNPack/` 為 All Rights Reserved，本專案**不使用其檔案**，僅以其 key 名稱清單作為自家生成器的驗收標準。

本專案自行生成的骨架為 **559 個 key**，逐章數字與外部基準完全吻合。與 565 的差額是**刻意偏離**：6 個純 `{image:...}` 的 description 行不 key 化、保留字面。那些行不含任何可譯文字，給它 key 只會讓譯者有機會弄壞圖片路徑。

key 命名細節（`scripts/keyify.py`）：

| 項目 | 規則 | 數量 |
|---|---|---|
| 章節標題 | `ftbquests.chapter.<章>.title` | 7 |
| 任務標題 | `…quest<ID>.title` | 155 |
| 任務副標 | `…quest<ID>.subtitle` | 77 |
| 任務內文 | `…quest<ID>.description<N>`，N 只數非空行 | 310 |
| 目標標題 | `…quest<ID>.task.<TASK_ID 十進位>.title` | 10 |

* quest ID 去除前導零，對齊 FTB Quests 自身的 `Long.toHexString` 慣例（`00890E05CBC407AE` → `890E05CBC407AE`）
* task ID 轉為十進位（`461BF68B1EB33759` → `5051902484402091865`）
* description 的空行保留為字面 `""`，不編號、不進 JSON

## KubeJS 自訂內容

| 類型 | 路徑／註冊方式 | 是否可走 lang |
|------|----------------|---------------|
| 自訂方塊／物品／流體 | `kubejs/startup_scripts/init.js`，`event.create(...).displayName('...')` | ✅ 可以（G0 實測）|
| 包內物品改名 | `kubejs/client_scripts/rename.js`，`ClientEvents.lang("en_us", …)` 45 條 | ✅ 可以（G0 實測）|

`init.js` 共 1,273 行，含 164 個直接的 `event.create()`，另有 `wallpaper(id)`、`strippedwallpapers(id, grow)`、`traffic_poles(id, name)` 三個輔助函式迴圈註冊。

**權威數據取自 `level.dat` 的 Forge 註冊表快照**（`scripts/extract_kubejs.py`，與 `init.js` 交叉比對）：

| 註冊表 | kubejs 項目數 |
|---|---|
| block | 146 |
| item | 209（其中 62 個為獨立物品，其餘沿用方塊 key）|
| fluid | 4 |
| **需譯翻譯 key** | **212** |
| 不重複英文名 | **113** |

其中 **154 個有明確 `displayName()`，58 個沒有**——後者由 KubeJS 從 ID 自動生成（`power_house` → “Power House”、`porous_stone` → “Porous Stone”），同樣是玩家看得到的字，**必須一併翻譯**。

> 先前「62 個字串」的估計是錯的：那是 `displayName("字面值")` 的不重複數，漏掉了自動生成的名稱，也漏掉了 `traffic_poles(id, name)` 這種以變數傳入顯示名的呼叫。

重複名稱集中在：`sign` ×23、`Wallpaper` ×20、`Data Chip` ×15、`Wallpaper Slab` ×8、`Floor Tiles` ×7、`Stripped Wallpaper` ×7。

**上游品質問題**：23 個交通標誌方塊（`stop_sign`、`exit_sign`、`skull_sign`、`arrow1_sign`…）的顯示名全部是小寫的 `sign`，彼此無法區分。翻譯時需決定是忠實譯為「標誌」×23，還是依 ID 給出可區分的名稱。

`kubejs/assets/kubejs/` 下只有 `blockstates`、`book_images`、`loot_tables`、`models`、`textures`，**沒有 lang 目錄**——整合包從未替自訂內容提供任何語系檔。

KubeJS 6（`kubejs-forge-2001.6.5-build.16`）的 `BuilderBase` 具備 `translationKey` 欄位（文件字串：「Sets the translation key for this object, e.g. `block.minecraft.stone`」）、`displayName`、`getTranslationKeyGroup`，並有 `GeneratedClientResourcePack`。結構上支持「資源包可覆蓋」，且已於 G0 實測確認。

## 包覆寫的模組 lang

`kubejs/assets/*/lang/en_us.json`，共 7 個命名空間、1,165 條：

| 命名空間 | 條數 |
|---|---|
| ae2 | 1,010 |
| endrem | 77 |
| minecraft | 32 |
| create | 26 |
| farmersdelight | 13 |
| mekanism | 4 |
| tconstruct | 3 |

**已知缺陷**：這些是整合包對既有模組的改名，但只提供 `en_us`。在繁中語系下，MTP 對同一 key 的譯文會勝出，導致整合包的自訂改名**全部失效**。`rename.js` 的 45 條同理（只註冊 `en_us`）。這是上游的真實 bug，本翻譯包應順手修復。

（例外：`kubejs/assets/ae2/lang/zh_tw.json` 已存在，AE2 部分整合包自己處理了。）

## 其他玩家可見文字

| 來源 | 規模 | 處理方式 |
|---|---|---|
| Patchouli 書 `reality_frame`（Building a Reality Frame）| 5 個 JSON，14 KB | `use_resource_pack: false` → 需附 `patchouli_books/reality_frame/zh_tw/` |
| Patchouli 書 `summoning`（Summoning 101）| 24 個 JSON，39 KB | 同上 |
| FancyMenu 標題畫面 | `config/fancymenu/` | 第一版不處理 |
| `kubejs/room_notes.txt` | 2.3 KB | 開發者筆記，非遊戲內文字，不需翻譯 |

## 環境與相依

| 項目 | 現況 |
|---|---|
| ModsTranslationPack | 實例內有 `ModsTranslationPack-1.20.zip.disabled`（**檔名被改過且停用**）。官方檔名為 `ModsTranslationPack-1.20.x.zip`。`pack_format 15`、650 個命名空間，含 `assets/ftbquests/lang/zh_tw.json`（模組 UI），**不含 `kubejs`／`quest` 命名空間 → 與本包零衝突** |
| Resource Pack Overrides | **LIA 已內建** `ResourcePackOverrides-v8.0.3-1.20.1-Forge.jar` + `PuzzlesLib-v8.1.33`，玩家免裝 |
| 既有 RPO 設定 | `config/resourcepackoverrides.json` 已存在（502 bytes），已將 `file/Liminal Resources` 設為 TOP／required／hidden／fixed，並全域 `force_compatible: true`。**必須合併，不可覆蓋** |
| 語系設定 | `options.txt` 的 `lang:zh_tw` 已設定 |

## 翻譯策略結論

1. **任務**：一次性 key 化 snbt（`ftbquests.chapter.<章>.quest<ID>.<欄位>`），譯文全部進單一 lang JSON。key 化後的 snbt 不含譯文，由生成器從 `source/` 快照重新產生。
2. **KubeJS**：優先走資源包 lang 覆蓋 `displayName`；若實測不可行則改用 Vault Patcher，**不修改 `init.js`**（上游更新衝突風險過高）。
3. **資源包結構**：**依 key 所屬模組拆成多個命名空間**（G0 實測結論，不可合併成單一檔案）：

   ```text
   assets/ftbquests/lang/zh_tw.json   任務 559 條
   assets/kubejs/lang/zh_tw.json      KubeJS 自訂內容 212 條
   assets/minecraft/lang/zh_tw.json   包內改名中屬於原版的部分
   assets/<各模組>/lang/zh_tw.json    包內改名中屬於各模組的部分
   ```
4. **交付**：單一補丁 zip 解壓進 `minecraft/`，內含無譯文的 key 化骨架、Patchouli 中文書、合併後的 RPO 設定，以及已放好位置的資源包。另出伺服器版（FTB Quests 任務檔為伺服器權威）。

## 風險與注意

- **上游更新最易壞的路徑**：`config/ftbquests/quests/chapters/*.snbt`（我們的 key 化骨架會被覆蓋）與 `config/resourcepackoverrides.json`（需人工 diff 合併）。對策是保留 `source/` 快照並以生成器重跑，不手改 snbt。
- **與 MTP 可能衝突的 key**：任務 key（`ftbquests.chapter.*`）零衝突；但修復包內改名時會刻意覆蓋 `item.minecraft.*` 等既有 key，需在文件說明這是有意為之。
- **`%` 轉義**：任何含 `%` 的原文移進 lang 檔時必須寫成 `%%`，否則會被當成格式符。
- **多人伺服器**：只裝客戶端補丁時，任務文字仍由伺服器提供，會是英文。

## 實測結論（Gate G0，已完成）

實測程序見 `docs/phase0-test.md`、`docs/phase0b-test.md`。

| 驗證項 | 結果 |
|---|---|
| 資源包可覆蓋 KubeJS `displayName` | ✅ 通過 |
| 資源包可修復 `rename.js` 的改名 | ✅ 通過（需正確命名空間，見下）|
| FTB Quests 2001.4.16 解析來自一般資源包的 `{key}` | ✅ 通過（已用正式 key 命名驗證）|

### 關鍵發現：語系 key 必須放進所屬模組的命名空間

第一輪測試中 `item.minecraft.bread` 放在自訂命名空間 `lia` 底下**失效**，但同一檔案內的 `block.kubejs.*` 與自訂 key 卻生效。原因是 Minecraft 的語系載入是**逐命名空間**進行：對每個命名空間，把各資源包中該命名空間的 `lang/<locale>.json` 依優先度疊加；但**跨命名空間之間沒有優先度**，後處理者覆蓋先處理者。

- 沒有其他來源定義的 key（自訂任務 key）→ 放哪個命名空間都會生效
- **已被原版或模組定義的 key** → 必須放進**該模組的命名空間**，否則會被對方的語系檔蓋回去

改放 `assets/minecraft/lang/zh_tw.json` 後即通過。

> **規則：命名空間 = 擁有該 key 的模組。**
> `item.minecraft.bread` → `assets/minecraft/`；`block.kubejs.*` → `assets/kubejs/`；`ftbquests.*` → `assets/ftbquests/`。
> 這也是 MTP 拆成 650 個命名空間資料夾的原因——不是為了整齊，是必要條件。

### 資源包順序語意

`options.txt` 為 `[vanilla, mod_resources, Moonlight, 測試包]` 時，遊戲內「已選擇」由上至下顯示為 `測試包 → Moonlight → Mod Resources → 預設`。

> **陣列越後面 = 顯示越上面 = 優先度越高。** RPO 的 `default_packs` 採同一慣例，本包需追加在陣列最末端。
