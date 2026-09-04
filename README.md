# Liminal Industries Acension 繁體中文翻譯包

[![授權](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange)](LICENSE)

為 Minecraft 整合包 **Liminal Industries Acension**（LIA，作者 Aceplante）製作的繁體中文翻譯包。
重點放在**任務書的引導品質**——玩家能照著任務書一路把進度做完。

| 項目 | |
|---|---|
| 適用 LIA 版本 | **1.19**（CurseForge projectID 1389281）|
| Minecraft / 載入器 | 1.20.1 / Forge 47.4.13 |
| 翻譯包版本 | v1.0.0 |

## 翻譯了什麼

| 內容 | 條數 |
|---|---|
| FTB Quests 任務書（七章、248 個任務） | 559 |
| Botania 方塊與物品名稱（重譯）＋術語校正 | 1,451 |
| KubeJS 自訂方塊／物品（壁紙、泳池磁磚、資料晶片…） | 212 |
| End Remastered（12 顆眼睛與相關進度） | 77 |
| 整合包自訂改名（閾限果醬、跨界箱、薄紙板…） | 46 |
| Patchouli 書籍（現實框架建造指南、召喚入門） | 59 |
| **合計** | **2,404** |

## 安裝

需要兩個檔案：

1. **本翻譯包補丁** — 由 [Releases](../../releases) 下載 `LIA-zhTW-Patch-vX.Y.Z.zip`
2. **模組翻譯包（MTP）** — 由 [CurseForge](https://www.curseforge.com/minecraft/texture-packs/modstranslationpack) 下載，用來覆蓋各模組的通用文字

### 步驟

1. 在啟動器中選擇 LIA 實例 → 開啟資料夾 → 進入 `minecraft` 目錄。
2. 把 `LIA-zhTW-Patch-vX.Y.Z.zip` 內的**所有檔案**拖進 `minecraft` 目錄，選擇**「取代目的地中的檔案」**。
   - 沒跳出取代提示 = 你放錯層級了。
3. 把 MTP 放進 `resourcepacks` 資料夾。
   - **檔名必須是 `ModsTranslationPack-1.20.x.zip`**（注意有 `.x`）。若檔名後面有 `(1)`、`(2)` 等後綴請先移除，否則不會被自動啟用。
4. 啟動遊戲。

資源包順序已由 `config/resourcepackoverrides.json` 鎖定，**不需要手動拖曳**。
遊戲內「已選擇」欄位由上到下應為：`LIA-zhTW.zip` → `ModsTranslationPack` → 其餘。

> 本翻譯包**不需要**額外安裝任何模組。Resource Pack Overrides 已內建於 LIA。

### 多人伺服器

FTB Quests 的任務檔由**伺服器**提供。只裝客戶端補丁的話，任務書仍會顯示英文。
請另外把 `LIA-zhTW-Patch-Server-vX.Y.Z.zip` 解壓到伺服器端的對應目錄。

### LIA 更新之後

本補丁包含 `config/ftbquests/quests/chapters/*.snbt`。整合包更新會覆蓋這些檔案，
任務書會變回英文——請重新安裝對應版本的補丁。

## 與 VM 漢化組的簡中翻譯包有何不同

| | 本包 | [VM 簡中](https://github.com/VM-Chinese-translate-group/Liminal-Industries-Acension-Chinese) |
|---|---|---|
| 語言 | 繁體中文（臺灣用語） | 簡體中文 |
| 來源 | 從英文原文重新翻譯 | 獨立的簡中專案 |
| 術語基準 | 原版 zh_TW → 模組內建繁中 → MTP | 簡中生態 |

本包**不是**簡繁轉換。所有術語都對照原版 zh_TW 與 MTP 查證，並以腳本自動攔截簡中用詞
（例如 sculk 是「伏聆」不是「幽匿」、cobbled 是「碎石」不是「圓石」）。

## 已知未翻項目

下列模組在這個整合包裡**完全沒有繁體中文**，且 MTP 也不涵蓋，因此相關物品在遊戲內顯示英文：

- **Thermal Series** — 分餾塔、熱解爐、感應熔煉爐、造岩機等
- **Eidolon Repraised** — 坩堝、火盆、Ars Ecclesia 等
- **Actually Additions** — 原子重組儀、賦能儀等
- **simpleradio** — 無線對講機相關

任務書提到這些機器時會使用中文譯名並在必要處附上原文，方便你在 JEI 搜尋。

另外兩點：

- **Botania 只重譯了方塊與物品名稱。** 植物魔法辭典的內文沒有重譯，只做了術語代換
  （瑪那→魔力等），所以名稱與內文一致，但內文仍保有原譯的行文與半形標點。
- 其餘模組（Tinkers' Construct、Supplementaries、Jade 等）自帶的繁中並不完整，
  未涵蓋處會顯示英文。這不是本包能處理的範圍。

## 開發

```bash
python scripts/build_all.py    # 重新產生所有譯文與檢查（順序有意義，見檔頭）
python scripts/merge_rpo.py    # 合併 resourcepackoverrides.json
python scripts/build.py        # 打包出三個交付物到 _workspace/build/dist/
```

建置需要本機有一份 LIA 實例——`source/` 只是上游快照，KubeJS 的註冊表、
Botania 的原始語系檔、原版 zh_tw 基準都直接從實例與啟動器資產讀取。

所有產物與工作檔都寫到 `_workspace/`（不納入版控）：骨架、驗證基準、
Botania 逐條查驗頁、三個交付 zip。

譯文全部經 `scripts/verify_translation.py` 檢查：key 對應、章節完整度、簡體字、
簡中用詞、非預期文字系統、`%%` 轉義、顏色碼保留、殘留英文。
簡體字清單以原版 zh_tw 與 MTP 為語料自我校正，避免把「濃郁」「划算」誤判為簡體。

## 致謝

- **Aceplante** — Liminal Industries Acension 整合包作者
- **Appocryptha** — 原版 Liminal Industries 作者
- **[釘宮翻譯組](https://teamkugimiya.org/)** — ModsTranslationPack，本包的繁中術語基準
- **[VM 漢化組](https://github.com/VM-Chinese-translate-group)** — 其 LIA 簡中專案的 key 化方案為本包生成器提供了驗收標準（僅比對 key 名稱，未使用其譯文）

## 授權

[CC BY-NC-SA 4.0](LICENSE)。僅涵蓋本專案自行產出的內容；不散布整合包本體或任何模組檔案。
