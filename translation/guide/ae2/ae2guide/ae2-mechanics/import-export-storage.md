---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 輸入、輸出與倉儲
---

# 輸入、輸出與倉儲

**你的 ME 系統與外面的世界**

AE2 裡有一個重要概念叫「網路倉儲」，也就是網路內容物實際存放的地方，
通常是[儲存單元](../items-blocks-machines/storage_cells.md)，或是 <ItemLink id="storage_bus" /> 所連接的容器。
多數 AE2 [裝置](../ae2-mechanics/devices.md)都會以某種方式和它互動。

舉例來說，

*   <ItemLink id="import_bus" /> 把東西推進網路倉儲
*   <ItemLink id="export_bus" /> 從網路倉儲拉出東西
*   <ItemLink id="interface" /> 對網路倉儲既推也拉
*   [終端機](../items-blocks-machines/terminals.md)在你存取物品、或是替合成格補料時，同樣既推也拉
*   <ItemLink id="storage_bus" /> 其實不對倉儲推拉，它是對相連的容器推拉，好讓那個容器成為網路倉儲
    （所以實際上是其他裝置在對*它*推拉）

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/import_export_storage.snbt" />

  <BoxAnnotation color="#dddddd" min="8 1 1" max="9 1.3 2">
        輸入匯流排把它所指向的容器裡的東西輸入到網路倉儲
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="8 2 1" max="9 3 1.3">
        從你的物品欄把東西放進終端機，也算是網路的一次輸入
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="7 0 1" max="8 1 2">
        介面在該格沒有設定要備料、或該格的東西比設定的備料量還多時，會從自己的內部倉庫輸入，
        所以把東西推進介面就等於送進網路
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="6 0 1" max="7 1 2">
        樣板供應器會從自己的回收格輸入，所以把東西推進去就等於送進網路
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 1" max="5 2 2">
        驅動器把插進去的儲存單元提供為網路倉儲
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="4 1.3 2">
        儲存匯流排把它所指向的容器當成網路倉儲
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 1" max="2 1.3 2">
        輸出匯流排把網路倉儲裡的東西輸出到它所指向的容器
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 1" max="2 3 1.3">
        從終端機把東西拿出來，也算是網路的一次輸出
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 1 1" max="1 2 2">
        介面在該格設定了要備料時，會輸出到自己的內部倉庫，
        所以從介面把東西拉走就等於從網路取出
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

設計自動化與物流時，務必把「推進網路倉儲」與「從網路倉儲拉出」這兩個動作與事件放在心上。

## 倉儲優先權

在某些介面右上角點一下扳手就能設定優先權。
進入網路的物品會先送往優先權最高的倉儲；
兩個倉儲優先權相同時，若其中一個已經有該物品，就會優先選它。
在同一個優先權群組裡，設有白名單的儲存單元會被視為已經有該物品。
從倉儲取出物品時，則是從優先權最低的那個開始拿。
這套優先權機制的結果是：隨著物品不斷進出網路倉儲，高優先權的倉儲會愈裝愈滿，低優先權的則會被逐漸清空。
