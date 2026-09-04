# Liminal Industries Acension 繁體中文翻譯包

[![授權](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange)](LICENSE)

為 Minecraft 整合包 **Liminal Industries Acension**（LIA，作者 Aceplante）製作的繁體中文翻譯包。

| 項目 | |
|---|---|
| 適用 LIA 版本 | **1.19**（CurseForge projectID 1389281）|
| Minecraft / 載入器 | 1.20.1 / Forge 47.4.13 |
| 翻譯包版本 | v1.1.0 |

## 覆蓋率

以整合包內全部模組的 `en_us` 為分母，比對「模組自帶繁中 + MTP + 本包」之後：

| | 英文條目 | 裝本包前缺 | 裝本包後缺 |
|---|---|---|---|
| **物品／方塊／生物名稱** | 9,139 | 2,934 | **0** |
| 全部字串 | 27,778 | 9,422 | 2,975 |

**你在 JEI、物品欄、任務書裡看到的每一個名稱都是中文。** 剩下未翻的 2,975 條全部是設定
與選項介面的文字（最大宗是 FancyMenu 的 1,759 條標題畫面編輯器），玩家在遊玩過程中不會遇到。

## 翻譯了什麼

本包共 **8,526 條、85 個命名空間**。

| 內容 | 條數 |
|---|---|
| Botania — 名稱重譯、辭典書頁、旗幟圖案、音效字幕 | 2,178 |
| Actually Additions — 全模組（含 281 條手冊章節） | 956 |
| Eidolon: Repraised — 全模組（含 368 條 Ars Ecclesia 指南） | 815 |
| MrCrayfish's Furniture: Refurbished — 全模組 | 656 |
| FTB Quests 任務書（七章、248 個任務）＋模組介面 | 602 |
| Tinkers' Construct — 工具改造、材質特性、流體效果 | 529 |
| Table Top Craft — 桌遊名稱與西洋棋介面 | 277 |
| Advanced Loot Info — JEI 的戰利品表檢視器 | 256 |
| KubeJS 自訂方塊／物品（壁紙、泳池磁磚、資料晶片…） | 212 |
| 其餘 76 個命名空間 | 2,045 |

另有 **1,074 條刻意不譯**，逐條在 [`translation/keep-as-source.json`](translation/keep-as-source.json)
寫明理由：設定選項、純格式字串（`%s / %s`）、單位縮寫（CF／FE／mB）、邏輯閘（AND／XOR）、
模組名、佔位文字，以及 Vocaloid 曲名之類**原作在所有語系都保留原文**的內容。

## 安裝

需要兩個檔案：

1. **本翻譯包補丁** — 由 [Releases](../../releases) 下載 `LIA-zhTW-Patch-vX.Y.Z.zip`
2. **模組翻譯包（MTP）** — 由 [CurseForge](https://www.curseforge.com/minecraft/texture-packs/modstranslationpack) 下載，用來覆蓋各模組的通用文字

### 步驟

1. 在啟動器中選擇 LIA 實例 → 開啟資料夾 → 進入 `minecraft` 目錄。
2. 把 `LIA-zhTW-Patch-vX.Y.Z.zip` 內的**所有檔案**拖進 `minecraft` 目錄，選擇**「取代目的地中的檔案」**。
   - 沒跳出取代提示 = 你放錯層級了。
3. 把 MTP 放進 `resourcepacks` 資料夾。
   - 檔名須為 `ModsTranslationPack-1.20.x.zip` 或 `ModsTranslationPack-1.20.zip`
     （官方發布名有 `.x`，但 CurseForge 下載下來常是後者，兩種都認）。
     若檔名後面有 `(1)`、`(2)` 等後綴請先移除，否則不會被自動啟用。
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

本包**不是**簡繁轉換。所有術語都對照原版 zh_TW 與 MTP 查證，並以腳本自動攔截簡中用詞。

## 品質檢查

每次建置都會跑 [`scripts/verify_translation.py`](scripts/verify_translation.py)，20 項檢查全過才算數：

- **簡中用詞** — 對照 **3,271 個簡中寫法**的黑名單。這份黑名單由
  [`scripts/build_cn_terms.py`](scripts/build_cn_terms.py) 自動產生：拿官方原版的 `zh_cn`
  與 `zh_tw` 逐 key 對撞，兩體譯法不同的簡中寫法就進黑名單，再抽一層詞素補足
  （官方值是「幽匿**塊**」，光比對完整值抓不到自己寫出來的「幽匿生物」）。
  誤傷同形正常中文的情況，在
  [`translation/cn-term-exceptions.json`](translation/cn-term-exceptions.json)
  帶語境放行並寫明理由。
- **譯名一致性** — 譯文提到某個物品時，用詞必須與本包給那個物品的譯名相同。
  例如物品名譯為「勿落草」，音效字幕就不能寫「勿擾修爾」。
- **簡體字** — 字表以原版 zh_tw 與 MTP 為語料自我校正，避免把「濃郁」「划算」誤判為簡體。
- 另有：key 對應、章節完整度、非預期文字系統、夾在中文裡的拉丁字詞、`%%` 轉義、
  顏色碼保留（含「§ 後接合法顏色碼」與「無字面 `&` 顏色碼」）、殘留英文、空值、多餘空白。

這些檢查抓到過的真錯包括：Poison 的正體是「劇毒」不是「中毒」、Piercing 是「貫穿」不是
「穿刺」、Enderium 是「熔融終界」不是「末影素」、Armorer 是「製甲師」不是「盔甲匠」、
buried_treasure 是「埋沒的」不是「埋藏的」。

## 開發

```bash
python scripts/build_all.py    # 重新產生所有譯文與檢查（17 步，順序有意義，見檔頭）
python scripts/merge_rpo.py    # 合併 resourcepackoverrides.json
python scripts/build.py        # 打包出三個交付物到 _workspace/build/dist/
```

建置需要本機有一份 LIA 實例——`source/` 只是上游快照，KubeJS 的註冊表、
Botania 的原始語系檔、原版 zh_tw／zh_cn 基準都直接從實例與啟動器資產讀取。
所有產物與工作檔都寫到 `_workspace/`（不納入版控）。

### 譯文怎麼組織

| 目錄 | 內容 |
|---|---|
| `translation/lang/` | **產出**：85 個 `<命名空間>.json`，直接對應資源包的 `assets/<ns>/lang/zh_tw.json` |
| `translation/names/` | **來源**：各模組的名詞表。修飾詞（木材、顏色、混凝土、陶土…）由 [`compose_mod_names.py`](scripts/compose_mod_names.py) 從原版 zh_tw **自動導出**，名詞表只需列去掉修飾後的核心 |
| `translation/text/` | **來源**：說明文字，逐條翻譯 |
| `translation/keep-as-source.json` | 刻意不譯的條目與理由 |

名稱用組字器的好處是一致性：`translation/names/table_top_craft.json` 只有 5 個名詞，
就組出 131 條（43 種材質 × 3 種桌遊）。組不出來的會**中止並列出**，不會靜默略過。

## 已知未翻項目

- **設定與選項介面**（約 2,975 條）— FancyMenu 的標題畫面編輯器、各模組的 config 畫面、
  ClientSort 的排序設定等。這是刻意的取捨：玩家在遊玩過程中不會看到這些。
- **Botania 的 Vocaloid 曲名進度標題**（26 條）— 原作在 ja／zh_cn／zh_tw 三個語系
  都保留原題，本包比照辦理。說明行已全部中文化。
- **AE2 的 GuideME 指南頁面** — 那是 markdown 資產，不走語系檔，本包碰不到。

## 致謝

- **Aceplante** — Liminal Industries Acension 整合包作者
- **Appocryptha** — 原版 Liminal Industries 作者
- **[釘宮翻譯組](https://teamkugimiya.org/)** — ModsTranslationPack，本包的繁中術語基準
- **[VM 漢化組](https://github.com/VM-Chinese-translate-group)** — 其 LIA 簡中專案的 key 化方案為本包生成器提供了驗收標準（僅比對 key 名稱，未使用其譯文）

## 授權

[CC BY-NC-SA 4.0](LICENSE)。僅涵蓋本專案自行產出的內容；不散布整合包本體或任何模組檔案。
