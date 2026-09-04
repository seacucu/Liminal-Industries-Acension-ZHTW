# 術語表

對齊順序：**原版 zh_tw → 模組內建繁中 → MTP → 本表自訂**。

> **鐵則：每一條都必須附上實際查證過的來源檔與 key，不得憑印象填寫。**
> 本表曾把 sculk 誤填為簡中的「幽匿」並標成「原版內建」——原版 zh_tw 實際用的是**伏聆**。
> 這類錯誤全是正體字，字元級的簡體檢查抓不到，只能靠對著來源檔查。
> `scripts/verify_translation.py` 的第 3b 項會用原版 zh_tw 當基準攔截已知的簡中用詞。

## 世界觀

| 英文 | 繁中 | 來源／說明 |
|---|---|---|
| Backrooms | 後室 | 後室社群通用譯名 |
| Poolrooms | 泳池間 | 後室社群通用譯名 |
| the Overworld | 主世界 | 原版 zh_tw（`commands.setworldspawn.failure.not_overworld` 等 6 處）|
| sculk | **伏聆** | 原版 zh_tw `block.minecraft.sculk`；衍生詞：伏聆觸媒／伏聆振測器／伏聆嘯口／伏聆脈絡。**不是「幽匿」（簡中）** |
| Warden | 伏守者 | 原版 zh_tw `entity.minecraft.warden`。**不是「監守者」（簡中）** |
| Guardian | 深海守衛 | 原版 zh_tw `entity.minecraft.guardian` |
| liminal space | 閾限空間 | 保留原詞概念；整合包名稱本身不譯 |

## 已有官方／既有譯名（必須沿用）

| 英文 | 繁中 | 來源 |
|---|---|---|
| Kekimurus | 貪食花 | Botania 內建 zh_tw：`block.botania.kekimurus`（沿用；見下方警告）|
| mana | **魔力** | 本包定名。Botania 內建 zh_tw 用「瑪那」，但該檔本身有 瑪那／魔源／魔力 三種譯法（見 `docs/glossary-botania.md`）。支線 B 已將 Botania 的物品方塊名稱統一為魔力 |
| Molten Silver | 熔融銀 | Tinkers' Construct 內建 zh_tw：`fluid.tconstruct.molten_silver` |
| Aluminium / Aluminum | 鋁 | Immersive Engineering 內建 zh_tw：`ingot_aluminum` = 鋁錠 |
| Ender Chest（原始名） | 終界箱 | MTP：`block.enderchests.chest.*`（本包已改名，見下）|

> **⚠ Botania 的 `zh_tw` 本身是簡中機器轉換品**：2,496 條中有 662 條使用半形標點，並混有「刷怪籠」（正體應為生怪磚）、「精準採集」（絲綢之觸）、「信標」（烽火台）等簡中用詞。
> 因此本專案岔出**支線 B** 自行重譯 Botania 的物品與方塊名稱（見 `docs/glossary-botania.md`）。
> 沿用其譯名的前提是「那是玩家實際看到的字」；既然我們接手重譯，該前提就不再成立——Mana 因此定為**魔力**而非瑪那。
> 未納入重譯範圍者（如貪食花）仍沿用，以免任務書與物品欄對不起來。

## 整合包自訂內容（本翻譯包定名）

| 英文 | 繁中 | 說明 |
|---|---|---|
| Pool Tiles | 泳池磁磚 | KubeJS `kubejs:pool_tile` |
| Golden Pool Tiles | 金色泳池磁磚 | KubeJS |
| Reality Alloy | 現實合金 | KubeJS `kubejs:reality_alloy` |
| Reality Storage Cell | 現實儲存元件 | KubeJS |
| Data Chip | 資料晶片 | KubeJS `kubejs:data_chip*` |
| Interplanar Chest | 跨界箱 | LIA 以 `rename.js` 將 `enderchests:ender_chest` 改名為 Interplanar Chest；**沿用整合包的改名意圖，不用 MTP 的「終界箱」** |
| Waterproof Map | 防水地圖 | LIA 改名 `supplementaries:slice_map` |
| Exotic Eye | 異域之眼 | End Remastered **無任何中文**，MTP 亦不涵蓋 → 由本包定名 |
| Ancient Portal Frame | 遠古傳送門框架 | 同上 |
| Rock Gen | 造岩機 | Thermal Series **無中文**（見「已知缺口」）；任務原文寫作 “extruder”，實際物品是 `thermal:device_rock_gen` |

### End Remastered 的 12 顆眼睛

模組本身沒有任何中文，且 LIA 覆寫了其中 39 條英文。任務書「逃離」整章都圍繞它們，因此由本包定名：

| 英文 | 繁中 |
|---|---|
| Magical Eye | 魔法之眼 |
| Evil Eye | 邪惡之眼 |
| Wither Eye | 凋零之眼 |
| Lost Eye | 遺失之眼 |
| Undead Eye | 不死之眼 |
| Cold Eye | 冰冷之眼 |
| Cryptic Eye | 神祕之眼 |
| Black Eye | 漆黑之眼 |
| Forged Eye | 鍛造之眼 |
| Dragon Eye | 巨龍之眼 |
| Old Eye | 古老之眼 |
| Rogue Eye | 流亡之眼 |
| Exotic Eye | 異域之眼 |

> 共 13 條：LIA 的傳送門需要 12 顆，`Exotic Eye` 為泳池間專屬。

## 刻意偏離原文之處

| 項目 | 原文 | 本包做法 | 理由 |
|---|---|---|---|
| 23 個交通標誌方塊 | 全部叫 `sign` | 依 ID 給可辨識名稱：停止標誌、出口標誌、骷髏標誌、閾限警告標誌… | 英文 23 個同名，JEI 與物品欄完全無法區分。使用者裁示保留可辨識名稱 |
| 16 個 Azulejo | 全部叫 `Azulejo` | 葡式花磚（加序號） | 同上；且「葡式花磚」是台灣對 azulejo 的通行說法 |
| 純 `{image:...}` 的任務內文行 | — | 不 key 化，保留字面 | 不含可譯文字，給 key 只會讓譯者有機會弄壞圖片路徑 |
| Botania `.reference` 的日文彩蛋 | How unpleasant | 真令人不快 | 既有繁中直接照抄日文，對繁中讀者無意義 |

## 通用譯法

| 項目 | 約定 |
|---|---|
| questbook | 任務書 |
| dimension | 維度 |
| chapter | 章節 |
| 第二人稱 | 用「你」，不用「您」 |
| 標點 | 全形標點；省略號用「……」；數字與單位間不加空格（12 顆、192 格）|
| 英數與中文之間 | 不強制加空格，但物品／模組專名保持原樣時前後留空格以利閱讀 |
| 語氣 | 保留原文的乾冷幽默與不安感，不改寫成說明書口吻 |

## 簡中用詞對照（`verify_translation.py` 會自動攔截）

左欄是簡中用詞，右欄是原版 zh_tw 的實際用詞。此表已用原版語系檔自我驗證：右欄必定出現在原版、左欄必定不出現。

| 簡中 | 正體（原版）| | 簡中 | 正體（原版）|
|---|---|---|---|---|
| 幽匿 | 伏聆 | | 刷怪籠 | 生怪磚 |
| 監守者 | 伏守者 | | 潛影盒 | 界伏盒 |
| 下界 | 地獄 | | 凋靈 | 凋零 |
| 末地 | 終界 | | 惡魂 | 地獄幽靈 |
| 末影人 | 終界使者 | | 精準採集 | 絲綢之觸 |
| 生物群系 | 生態域 | | 時運 | 幸運 |
| 信標 | 烽火台 | | 下界合金 | 獄髓 |

遇到新的分歧詞就補進 `scripts/verify_translation.py` 的 `CN_TERMS`——檢查會自動驗證新增項是否真的符合原版。

## 格式保留規則

翻譯時**必須原樣保留**：

- 顏色與樣式碼：`&o`（斜體）等，共 5 處
- 圖片標記：`{image:...}`，共 6 處（骨架中保留為字面，不進譯文檔）
- `%%`：原文中的 `%` 在語系檔必須寫成 `%%`，共 2 處

## 已知缺口（非本包能解決）

| 模組 | 狀況 |
|---|---|
| Thermal Series | `thermal` 命名空間**完全沒有繁中**。模組 jar 只帶 `thermal_foundation` 的 121 條 UI 字串，MTP 不涵蓋 `thermal`。任務會提到的 Rock Gen 等物品在遊戲內顯示為英文 |
| End Remastered | 模組無任何中文；本包翻譯其在 LIA 內被覆寫的 77 條 |
