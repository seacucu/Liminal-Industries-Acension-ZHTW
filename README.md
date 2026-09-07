# Liminal Industries Acension 繁體中文翻譯包

[![授權](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange)](LICENSE)

Minecraft 模組包 **Liminal Industries Acension**（LIA）的繁體中文翻譯包，共 9,574 條。
任務書、物品與方塊名稱、模組指南書皆已翻譯，包含沉浸工程的工程師手冊、應用能源 2 的指南與植物魔法辭典。

| 適用 LIA 版本 | 1.19（CurseForge projectID 1389281）|
|---|---|
| Minecraft / 載入器 | 1.20.1 / Forge 47.4.13 |
| 翻譯包版本 | v1.2.0 |

## 安裝

需要下載兩個檔案：

1. `LIA-zhTW-Patch-vX.Y.Z.zip`，由 [Releases](../../releases) 取得
2. **ModsTranslationPack**（MTP），由 [CurseForge](https://www.curseforge.com/minecraft/texture-packs/modstranslationpack) 取得，負責各模組的通用文字

步驟：

1. 在啟動器中選擇 LIA 實例，開啟資料夾，進入 `minecraft` 目錄。
2. 將補丁 zip 內的**所有檔案**拖進 `minecraft`，選擇「取代目的地中的檔案」。
   沒跳出取代提示表示放錯層級了。
3. 將 MTP 放進 `resourcepacks`。檔名須為 `ModsTranslationPack-1.20.x.zip`
   或 `ModsTranslationPack-1.20.zip`，結尾若有 `(1)`、`(2)` 請先移除。
4. 啟動遊戲。

資源包順序已鎖定，不需手動拖曳。遊戲內「已選擇」欄位由上到下應為
`LIA-zhTW.zip`、`ModsTranslationPack`、其餘。

本翻譯包不需要額外安裝任何模組。

## 多人伺服器

FTB Quests 的任務檔由伺服器提供，只裝客戶端補丁的話任務書仍是英文。
請另外將 `LIA-zhTW-Patch-Server-vX.Y.Z.zip` 解壓到伺服器端的對應目錄。

## LIA 更新之後

補丁包含 `config/ftbquests/quests/chapters/*.snbt`，模組包更新會覆蓋這些檔案，
任務書會變回英文。請重新安裝對應版本的補丁。

## 未翻譯的部分

設定與選項介面（FancyMenu 的標題畫面編輯器、各模組的 config 畫面等）維持英文。

## 致謝

- **Aceplante**：Liminal Industries Acension 作者
- **Appocryptha**：原版 Liminal Industries 作者
- **[釘宮翻譯組](https://teamkugimiya.org/)**：ModsTranslationPack

## 授權

[CC BY-NC-SA 4.0](LICENSE)。僅涵蓋本專案自行產出的內容，不散布模組包本體或任何模組檔案。
