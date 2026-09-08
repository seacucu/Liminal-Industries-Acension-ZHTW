---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME 儲物箱
  icon: chest
  position: 210
categories:
- devices
item_ids:
- ae2:chest
---

# ME 儲物箱

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/chest.snbt" />
</GameScene>

ME 儲物箱的行為就像一個迷你網路，內建 <ItemLink id="terminal" />、<ItemLink id="drive" /> 與 <ItemLink id="energy_acceptor" />。
它雖然可以當成一套微型的倉儲網路，但只放得下一個[儲存單元](../items-blocks-machines/storage_cells.md)，
這樣用途相當有限。

它真正好用的地方，是專門用來存取裝在它裡面的那個儲存單元。它內建的終端機只看得到、
也只存取得到那個單元裡的東西；而一般網路上的[裝置](../ae2-mechanics/devices.md)則能存取任何
[網路倉儲](../ae2-mechanics/import-export-storage.md)裡的物品，包括 ME 儲物箱。

它有兩種介面，而且物品搬運是分面的。與頂部的終端機互動會開啟內建終端機；
物品可以從這一面送進裝著的儲存單元，但取不出來。與其他任何一面互動則會開啟另一個介面，
裡面有儲存單元的欄位與優先權設定。單元只能透過有單元欄位的那一面，用物品物流手段送入與取出。

它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。

它的 AE 電力緩衝很小，所以如果所在的網路上沒有[能量電池](../items-blocks-machines/energy_cells.md)，
一次存取太多物品可能會讓它斷電。

終端機可以用 <ItemLink id="color_applicator" /> 上色。

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/chest_color.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

ME 儲物箱的設定和 <ItemLink id="terminal" /> 或 <ItemLink id="crafting_terminal" /> 完全相同，
但它不支援 <ItemLink id="view_cell" />。

## 單元狀態燈

儲物箱裡的單元各有一顆指示燈，用來顯示狀態：

| 顏色  | 狀態                                                                           |
| :----- | :------------------------------------------------------------------------------- |
| 綠色  | 空的                                                                            |
| 藍色   | 有東西                                                                |
| 橙色 | [類型](../ae2-mechanics/bytes-and-types.md)已滿，無法再加入新類型     |
| 紅色    | [位元組](../ae2-mechanics/bytes-and-types.md)已滿，無法再放入物品 |
| 黑色  | 沒有電力，或驅動器沒有分到[頻道](../ae2-mechanics/channels.md)                 |

## 優先權

在單元欄位介面右上角點一下扳手就能設定優先權。
進入網路的物品會先送往優先權最高的倉儲。
兩個倉儲或單元優先權相同時，若其中一個已經有該物品，就會優先選它。
在同一個優先權群組裡，有[分區設定](cell_workbench.md)的單元會被視為已經有該物品。
從倉儲取出物品時，則是從優先權最低的那個開始拿。
這套優先權機制的結果是：隨著物品不斷進出網路倉儲，高優先權的倉儲會愈裝愈滿，低優先權的則會被逐漸清空。

## 配方

<RecipeFor id="chest" />
