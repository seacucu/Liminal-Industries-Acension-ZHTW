---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME 輸入匯流排
  icon: import_bus
  position: 220
categories:
- devices
item_ids:
- ae2:import_bus
---

# 輸入匯流排

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/import_bus.snbt" />
</GameScene>

輸入匯流排從它所貼著的容器中抽出物品與流體（裝了附屬模組的話還包括其他東西），
再推進[網路倉儲](../ae2-mechanics/import-export-storage.md)。

為了減輕效能負擔，輸入匯流排若一段時間沒有輸入到東西，就會進入類似「睡眠模式」的低速運轉；
一旦成功輸入了什麼，它就會醒來並加速到全速（每秒 4 次作業）。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

## 篩選

預設情況下匯流排會把它碰得到的東西全部輸入。把物品放進篩選欄位就等於設定白名單，
只有那些指定的物品會被輸入。

物品與流體都能直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

## 升級

輸入匯流排支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="capacity_card" /> 增加篩選欄位的數量
*   <ItemLink id="speed_card" /> 提高每次作業搬運的數量
*   <ItemLink id="fuzzy_card" /> 讓匯流排能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="inverter_card" /> 把篩選從白名單切換成黑名單
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
