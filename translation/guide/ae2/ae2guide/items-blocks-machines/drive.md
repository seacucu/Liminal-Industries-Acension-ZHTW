---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME 驅動器
  icon: drive
  position: 210
categories:
- devices
item_ids:
- ae2:drive
---

# ME 驅動器

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/drive.snbt" />
</GameScene>

驅動器就是你插[儲存單元](storage_cells.md)的那個[裝置](../ae2-mechanics/devices.md)，
插上去之後它們才會成為[網路倉儲](../ae2-mechanics/import-export-storage.md)。它有 10 個欄位，每格放一個單元。

如果你出於某種理由想這麼做，也可以用漏斗或 AE2 匯流排之類的物品物流手段，把單元推入或拉出它的倉庫。

它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。

## 單元狀態燈

驅動器裡的單元各有一顆指示燈，用來顯示狀態：

| 顏色  | 狀態                                                                           |
| :----- | :------------------------------------------------------------------------------- |
| 綠色  | 空的                                                                            |
| 藍色   | 有東西                                                                |
| 橙色 | [類型](../ae2-mechanics/bytes-and-types.md)已滿，無法再加入新類型     |
| 紅色    | [位元組](../ae2-mechanics/bytes-and-types.md)已滿，無法再放入物品 |
| 黑色  | 沒有電力，或驅動器沒有分到[頻道](../ae2-mechanics/channels.md)                 |

## 優先權

在介面右上角點一下扳手就能設定優先權。
進入網路的物品會先送往優先權最高的倉儲。
兩個倉儲或單元優先權相同時，若其中一個已經有該物品，就會優先選它。
在同一個優先權群組裡，有[分區設定](cell_workbench.md)的單元會被視為已經有該物品。
從倉儲取出物品時，則是從優先權最低的那個開始拿。
這套優先權機制的結果是：隨著物品不斷進出網路倉儲，高優先權的倉儲會愈裝愈滿，低優先權的則會被逐漸清空。

## 配方

<RecipeFor id="drive" />
