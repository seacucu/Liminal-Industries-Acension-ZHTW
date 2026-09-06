---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 網路工具
  icon: network_tool
  position: 410
categories:
- tools
item_ids:
- ae2:network_tool
---

# 網路工具

<ItemImage id="network_tool" scale="4" />

網路工具是改造版的[扳手](wrench.md)，除了扳手的功能之外，還能顯示網路診斷資訊並存放[升級卡](upgrade_cards.md)。
它保留了扳手快速拆解、以及把[附件](../ae2-mechanics/cable-subparts.md)從線纜上取下的能力，但不能用來旋轉方塊。

它有 9 個欄位可以存放[升級卡](upgrade_cards.md)，只要工具在你的物品欄裡，
這些卡片在任何 AE2 裝置的介面中都能直接取用。

右鍵點擊網路上的任何一部分，都會開啟診斷資訊視窗，效果和右鍵點擊 <ItemLink id="controller" /> 相同。
這個視窗會顯示

*   網路上已使用的頻道數量
*   一個全域設定的切換，可切換能量以 AE 或 E/FE 顯示
*   網路目前儲存的[能量](../ae2-mechanics/energy.md)與最大容量
*   進入網路的能量與網路消耗的能量
*   網路上所有[裝置](../ae2-mechanics/devices.md)與元件的清單

在擺弄[子網路](../ae2-mechanics/subnetworks.md)時，這個視窗也很適合用來判斷兩條線纜或兩個裝置是不是屬於同一個網路。

## 隱藏外牆板

只要任一隻手拿著網路工具，<a href="facades.md">外牆板</a>就會隱藏起來。

外牆板隱藏時，你可以直接與後面的方塊互動，不必先把它拆掉。

## 配方

<RecipeFor id="network_tool" />
