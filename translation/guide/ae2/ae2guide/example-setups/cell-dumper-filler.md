---
navigation:
  parent: example-setups/example-setups-index.md
  title: 儲存單元傾倒與填充機
  icon: io_port
---

# 儲存單元傾倒與填充機

有人會問：「我要怎麼把一個儲存單元快速倒進儲物箱、抽屜牆或背包，或是反過來從那些地方把單元裝滿？」

答案是用 <ItemLink id="io_port" /> 搭配子網路，限制它只能把物品放到哪裡、或只能從哪裡抽。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/cell_dumper_filler.snbt" />

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 1">
        (1) IO 埠：用介面中央的箭頭按鈕，可以切換成「傳輸資料至網路」或「傳輸資料至儲存單元」。
        裝有 3 張加速卡。
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0.7 0" max="1 1 1">
        (2) 儲存匯流排：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#33dd33" min="0 1 0" max="1 2 1">
        想填充或清空的容器放這裡。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0.35 0.35" max="2.3 0.65 0.65">
        石英纖維：只有在電力來自另一個網路時才需要。
  </BoxAnnotation>

<DiamondAnnotation pos="3 0.5 0.5" color="#00ff00">
        通往某個電力來源，例如另一個網路，或一個能量接收器。
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="io_port" />（1）用介面中央的箭頭按鈕，可以切換成「傳輸資料至網路」或「傳輸資料至儲存單元」。
  它裝了 3 張加速卡以達到最高速度。
* <ItemLink id="storage_bus" />（2）維持預設設定。

## 運作原理

### 「傳輸資料至網路」模式

1. <ItemLink id="io_port" /> 試著把插入的[儲存單元](../items-blocks-machines/storage_cells.md)的內容
    倒進[網路倉儲](../ae2-mechanics/import-export-storage.md)。
2. 子網路上唯一的倉儲是 <ItemLink id="storage_bus" />，於是那些物品、流體之類的東西
    就被存進你擺在它前面的容器。
* <ItemLink id="energy_cell" /> 提供了夠大的[能量](../ae2-mechanics/energy.md)緩衝，
    網路才不會因為單一遊戲刻搬運那麼多物品的耗電而斷電。

### 「傳輸資料至儲存單元」模式

1. <ItemLink id="io_port" /> 試著把[網路倉儲](../ae2-mechanics/import-export-storage.md)的內容
   倒進插入的[儲存單元](../items-blocks-machines/storage_cells.md)。
2. 子網路上唯一的倉儲是 <ItemLink id="storage_bus" />，於是那些物品、流體之類的東西
   就從你擺在它前面的容器被抽出來。
* <ItemLink id="energy_cell" /> 提供了夠大的[能量](../ae2-mechanics/energy.md)緩衝，
  網路才不會因為單一遊戲刻搬運那麼多物品的耗電而斷電。
