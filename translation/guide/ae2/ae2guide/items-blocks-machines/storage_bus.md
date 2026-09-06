---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME 儲存匯流排
  icon: storage_bus
  position: 220
categories:
- devices
item_ids:
- ae2:storage_bus
---

# 儲存匯流排

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/storage_bus.snbt" />
</GameScene>

一直捨不得把你那面亂七八糟的箱子牆換掉嗎？儲存匯流排來了！

儲存匯流排把它所貼著的容器變成[網路倉儲](../ae2-mechanics/import-export-storage.md)的一部分。
它的作法是讓網路看得見那個容器的內容，並在[裝置](../ae2-mechanics/devices.md)對網路倉儲推料與取料時，
代為對那個容器推入與抽出。

由於 AE2 的設計哲學是「靠各[裝置](../ae2-mechanics/devices.md)功能互動而湧現出機制」，
你其實*不一定*要拿儲存匯流排來做*倉儲*。透過[子網路](../ae2-mechanics/subnetworks.md)讓一個
（或一組）儲存匯流排成為某個網路上*唯一*的倉儲，就能把它當成物品搬運的來源或目的地。
（見[「管線子網路」](../example-setups/pipe-subnet.md)）

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

## 篩選

預設情況下匯流排什麼都存。把物品放進篩選欄位就等於設定白名單，只有那些指定的物品會被存放。

物品與流體都能直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

## 優先權

在介面右上角點一下扳手就能設定優先權。
進入網路的物品會先送往優先權最高的倉儲。
兩個倉儲優先權相同時，若其中一個已經有該物品，就會優先選它。
在同一個優先權群組裡，設有篩選的倉儲會被視為已經有該物品。
從倉儲取出物品時，則是從優先權最低的那個開始拿。
這套優先權機制的結果是：隨著物品不斷進出網路倉儲，高優先權的倉儲會愈裝愈滿，低優先權的則會被逐漸清空。

## 設定

*   匯流排可以依相鄰容器目前的內容自動設定分區（篩選）
*   可以設定要不要讓網路看見相鄰容器中「匯流排抽不出來」的物品
    （例如儲存匯流排就抽不出 <ItemLink id="inscriber" /> 中央輸入格的東西）
*   匯流排可以設定成存取兩端都套用篩選，或只在存入時套用
*   匯流排可以設為雙向傳輸、僅能存入或僅能取出

## 升級

儲存匯流排支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="capacity_card" /> 增加篩選欄位的數量
*   <ItemLink id="fuzzy_card" /> 讓匯流排能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="inverter_card" /> 把篩選從白名單切換成黑名單
*   <ItemLink id="void_card" /> 在相鄰容器裝滿時把送進來的物品銷毀，可以避免農場塞住。用它記得先設好分區！

## 配方

<RecipeFor id="storage_bus" />
