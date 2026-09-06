---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME 輸出匯流排
  icon: export_bus
  position: 220
categories:
- devices
item_ids:
- ae2:export_bus
---

# 輸出匯流排

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/export_bus.snbt" />
</GameScene>

輸出匯流排從[網路倉儲](../ae2-mechanics/import-export-storage.md)取出物品與流體
（裝了附屬模組的話還包括其他東西），再推進它所貼著的容器。

為了減輕效能負擔，輸出匯流排若一段時間沒有輸出東西，就會進入類似「睡眠模式」的低速運轉；
一旦成功輸出了什麼，它就會醒來並加速到全速（每秒 4 次作業）。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

## 篩選

預設情況下匯流排什麼都不會輸出。把物品放進篩選欄位就等於設定白名單，
讓那些指定的物品得以被輸出。

物品與流體都能直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

## 升級

輸出匯流排支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="capacity_card" /> 增加篩選欄位的數量，並多出一個設定，用來決定篩選項目的輸出順序。
*   <ItemLink id="speed_card" /> 提高每次作業搬運的數量
*   <ItemLink id="fuzzy_card" /> 讓匯流排能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="crafting_card" /> 讓匯流排能向你的[自動合成](../ae2-mechanics/autocrafting.md)系統送出合成請求，
    以取得它要的物品。可以設定成「倉儲裡有就先拿」，或是「一律請求重新合成一份」。
*   <ItemLink id="redstone_card" /> 加上紅石控制，可設為高電位啟用、低電位啟用，或每個脈衝作業一次

## 速度

| 加速卡數量 | 每次作業搬運的物品數 |
|:-------------------|:--------------------------|
| 0                  | 1                         |
| 1                  | 8                         |
| 2                  | 32                        |
| 3                  | 64                        |
| 4                  | 96                        |

## 配方

<RecipeFor id="import_bus" />
