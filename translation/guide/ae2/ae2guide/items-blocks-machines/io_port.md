---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME IO 埠
  icon: io_port
  position: 210
categories:
- devices
item_ids:
- ae2:io_port
---

# ME I/O 埠

<BlockImage id="io_port" p:powered="true" scale="8" />

IO 埠讓你在[儲存單元](../items-blocks-machines/storage_cells.md)與[網路倉儲](../ae2-mechanics/import-export-storage.md)之間快速灌入或倒出內容。

它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。

## 設定

*   IO 埠可以設定成在單元清空、裝滿，或工作完成時，把單元移到輸出欄位。
*   若插入 <ItemLink id="redstone_card" />，就會多出各種紅石條件的選項。
*   介面中央有一個箭頭，用來設定搬運方向：從單元送往[網路倉儲](../ae2-mechanics/import-export-storage.md)，
    或從倉儲送往單元。

## 升級

IO 埠支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="speed_card" /> 提高每次作業搬運的數量
*   <ItemLink id="redstone_card" /> 加上紅石控制，可設為高電位啟用、低電位啟用，或每個脈衝作業一次

## 配方

<RecipeFor id="io_port" />
