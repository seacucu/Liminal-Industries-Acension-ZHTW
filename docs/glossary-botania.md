# Botania 術語表（支線 B0）

範圍：`block.botania.*`（729）與 `item.botania.*`（331），共 **1,060 條**方塊與物品名稱。
`botania.page.*` 等書頁內容**不重譯**，但會做一次純術語代換（見文末），讓整個模組內部一致。

## 為什麼需要這份表

Botania jar 自帶的 `assets/botania/lang/zh_tw.json` 是**簡中轉換品且不完整**：

| 指標 | 數值 |
|---|---|
| 完成度 | 2,496 / 3,472（72%）；名稱類 803 / 1,060 |
| 遊戲內顯示英文 | 980 條（名稱類 257 條）|
| 半形標點 | 2,436 條中文裡有 719 條 |
| 殘留簡體字 | 3 條 |
| 簡中用詞 | 至少 14 條（信標、刷怪籠、精準採集…）|

更嚴重的是**內部自相矛盾**——同一個材料有兩個名字：

| 英文 | 既有譯法分布 | 問題 |
|---|---|---|
| Mana | 瑪那 ×39、魔源 ×6、魔力 ×1 | 三種 |
| Manasteel | 魔鋼 ×10、瑪那鋼 ×2 | 同一材料兩個名字 |
| Livingwood | 活木 ×13、活木枝 ×2 | 不一致 |
| Glimmering | 螢光 ×16、微光 ×2 | 與 Shimmering（微光 ×16）撞名 |
| Chiseled | 浮雕 ×15、框邊 ×1 | 不一致，且與 Framed 撞名 |
| Azulejo | 阿茲勒赫瓷磚 ×12、煉獄磚塊、靈魂磚塊、霜凍磚塊、瓦塊 | 同一英文名五種譯法 |

## 權威順序

1. **原版 zh_tw**（最高，不可違背）——建材、顏色、通用構詞
2. **既有 zh_tw 的多數譯法**——僅在不違背 1 且內部一致時沿用
3. **本表新定**——上述兩者都無解時

## 建材與構詞（取自原版 zh_tw，不可改）

| 英文 | 繁中 | 原版佐證 |
|---|---|---|
| Chiseled X | 浮雕X | `chiseled_stone_bricks` = 浮雕石磚 |
| Cracked X | 裂紋X | `cracked_stone_bricks` = 裂紋石磚 |
| Mossy X | 青苔X | `mossy_stone_bricks` = 青苔石磚 |
| Polished X | 拋光X | `polished_andesite` = 拋光安山岩 |
| X Bricks | X磚 | `stone_bricks` = 石磚 |
| X Slab | X半磚 | `stone_brick_slab` = 石磚半磚 |
| X Stairs | X階梯 | `stone_brick_stairs` = 石磚階梯 |
| X Wall | X牆 | `stone_brick_wall` = 石磚牆 |
| X Planks | X材 | `oak_planks` = 橡木材、`bamboo_planks` = 竹材 |
| Block of X | X方塊 | `iron_block` = 鐵方塊、`gold_block` = 黃金方塊 |
| Potted X | X盆栽 | `potted_dandelion` = 蒲公英盆栽 |
| X Mushroom | X蘑菇 | `brown_mushroom` = 棕色蘑菇 |
| Smooth X | 平滑X | `smooth_stone` = 平滑石頭 |
| Cobbled X | X碎石 | `cobbled_deepslate` = 深板岩碎石（**不是**簡中的「圓石」；`cobblestone` 本身才是鵝卵石）|

> 這批修正影響最大的是 **Block of X**（既有全用「X塊」，12 條需改為「X方塊」）與 **Planks**（既有用「X板」，9 條需改為「X材」）。

## Botania 核心材料

| 英文 | 採用 | 說明 |
|---|---|---|
| Mana | **魔力** | 使用者定案。既有的 `瑪那`（39）、`魔源`（6）全部改為魔力 |
| Manasteel | **魔鋼** | 既有多數（10/12）得以保留，且與 Mana=魔力 一致；`瑪那鋼`（2 條）改為魔鋼 |
| Terrasteel | 泰拉鋼 | 沿用 |
| Elementium | 源質鋼 | 沿用 |
| Gaia Spirit | 蓋亞魂 | 沿用 |
| Livingwood | **活木** | 統一；`活木枝` 廢除（僅出現在 Livingwood Avatar）|
| Livingrock | 活石 | 沿用 |
| Dreamwood | 夢之木 | 沿用 |
| Mana Pool | 魔力池 | 依 Mana=魔力 |
| Mana Spreader | 魔力發射器 | 依 Mana=魔力 |
| Spark | 火花 | 沿用 |
| Lens | 透鏡 | 沿用 |
| Rune | 符文 | 沿用（Rune of Air = 風之符文）|
| Petal | 花瓣 | 名稱類；Petal Apothecary = 花藥台（沿用）|
| Pylon | 塔柱 | 既有無樣本，本表新定 |
| Portuguese X | 葡式X | 使用者定案，與葡式花磚一致（**不用**「葡萄牙」）|
| Corporea | **具現／具現化** | 使用者定案。既有的「多媒體」直接繼承自簡中「多媒体」，是誤譯——Corporea 是物品網路／索取系統 |

## 發光／花朵體系（消除撞名）

| 英文 | 採用 | 原因 |
|---|---|---|
| Glimmering X | **螢光X** | 既有多數（16/18）|
| Shimmering X | **微光X** | 既有一致（16/16）|
| Mystical X | 神秘X | 沿用既有；見下方正字說明 |
| Floating X | 浮空X | 沿用（16 條一致）|
| X Petite | 小型X | 對應 Botania 的迷你花變體 |
| Tall Mystical X | **神秘高X** | 使用者定案：語序為「神秘」＋「高」＋花名，非「高神秘」|

> Glimmering 原有 2 條誤用「微光」，與 Shimmering 撞名，一併修正。

## 已定案的三項

### ① Corporea → 具現／具現化 ✅

既有的「多媒體」直接繼承自簡中「多媒体」，是誤譯——Corporea 是 Botania 的物品網路／索取系統。

影響 15 條（既有 6 + 缺譯 9）：具現索引、具現火花、具現漏斗、具現攔截器、具現固定器、具現水晶魔方、具現方塊、具現磚系列。

### ② Azulejo → 葡式花磚 ✅

使用者定案。16 個方塊在英文裡全都叫 Azulejo，既有卻有五種譯法（阿茲勒赫瓷磚 ×12、煉獄磚塊、靈魂磚塊、霜凍磚塊、瓦塊），統一為**葡式花磚**——台灣對 azulejo 的通行稱法，並與同系列的 Portuguese Pavement（葡式路面）呼應。

16 個同名方塊以序號區分：葡式花磚、葡式花磚 2…葡式花磚 16。

### ③ Mana → 魔力，Manasteel → 魔鋼 ✅

使用者定案。既有的多數譯法「魔鋼」得以保留，Mana 全面採「魔力」，內部一致。

### 正字說明：神秘（沿用，不用「祕」）

「神祕」為教育部標準字體，但三個參考來源都以「神秘」為主——原版 zh_tw 1:0、Botania 既有 66:0、MTP 45:9。使用者裁示**沿用「神秘」**，與既有生態一致。

## 命名模式（供 B1 逐條套用）

```
Glimmering Livingwood          → 螢光活木
Chiseled Livingrock Bricks     → 浮雕活石磚
Livingwood Plank Slab          → 活木材半磚
Block of Terrasteel            → 泰拉鋼方塊
Manasteel Axe                  → 魔鋼斧
Diluted Mana Pool              → 稀釋魔力池
Corporea Index                 → 具現索引
Mystical Black Flower          → 黑色神秘花
Tall Mystical Black Flower     → 黑色神秘高花
Potted Mystical Black Flower   → 黑色神秘花盆栽
Floating Bellethorne Petite    → 浮空小型鈴刺花
Black Portuguese Pavement Wall → 黑色葡式路面牆
```

顏色詞一律採原版譯名並置於最前（`黑色`、`藍色`、`棕色`…），與既有譯法一致。

## 已知的合理例外

| 項目 | 說明 |
|---|---|
| Tiny Planet | 英文有兩個同名物件：`block.botania.tiny_planet_block`（魔力環繞器）與 `item.botania.tiny_planet`（行星項鏈）。中文給了不同名稱**比英文更清楚**，屬有意保留 |
| Petal Apothecary 變體 | Talc／Fuchsite／Solite 等石材變體，既有依生態域譯為平原／森林／沙漠花藥台。與 Botania 的變質石材設計相符，沿用 |


## 範圍外的術語代換

範圍外的 323 條（`botania.page.*` 231、`botania.tagline.*` 31、`botania.entry.*` 23、其餘 38）**不重譯**，只做機械性的字串取代，避免「物品欄寫魔力、辭典寫瑪那」。

| 取代 | 原因 |
|---|---|
| 瑪那 → 魔力 | 與範圍內一致 |
| 多媒體 → 具現 | 同上 |
| 瑪那鋼 → 魔鋼 | 同上 |
| 魔源 → 魔力 | 同上 |
| 信標 → 烽火台 | 原版 zh_tw |
| 刷怪籠 → 生怪磚 | 原版 zh_tw |
| 精準採集 → 絲綢之觸 | 原版 zh_tw |
| 凋靈 → 凋零 | 原版 zh_tw |
| 殘留簡體字 3 條 | 逐條修正 |

**不處理**：半形標點（719 條）與譯文風格。那屬於重譯範疇，不在本次。
