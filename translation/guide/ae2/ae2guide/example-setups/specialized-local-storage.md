---
navigation:
  parent: example-setups/example-setups-index.md
  title: 專用的在地倉儲
  icon: drive
---

# 專用的在地倉儲

利用[介面的一項特殊行為](../items-blocks-machines/interface.md#special-interactions)，
可以讓一個[子網路](../ae2-mechanics/subnetworks.md)把自己倉儲的內容呈現給主網路，
而它自己看不到主網路的倉儲，而且只佔用 1 條[頻道](../ae2-mechanics/channels.md)。

這很適合放在某座農場旁邊當在地倉儲，產物就不會滿出來灌進你的主倉儲。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/local_storage.snbt" />

<BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
        (1) 某種把物品輸入進來的手段（這裡用的是介面）
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
        (2) 驅動器：裡面放幾個單元。單元應該分區設定成農場產出的東西。
        單元可以裝平均分配卡與溢位銷毀卡。
        <Row><ItemImage id="item_storage_cell_4k" scale="2" /> <ItemImage id="equal_distribution_card" scale="2" /> <ItemImage id="void_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
        (3) 合成終端機：它看得到子網路上那台驅動器的內容，但看不到主網路倉儲的內容。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
        (4) 介面 #2：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
        (5) 儲存匯流排：優先權設得比主倉儲高，篩選可以設成農場產出的東西。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
        合成終端機：它同時看得到主網路倉儲*與*子網路的內容。
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* 第一個 <ItemLink id="interface" />（1）單純接收農場送來的物品，再推進子網路。
* <ItemLink id="drive" />（2）裡面放幾個[儲存單元](../items-blocks-machines/storage_cells.md)。
  單元應該[分區](../items-blocks-machines/cell_workbench.md)設定成農場產出的東西。
  單元可以裝 <ItemLink id="equal_distribution_card" /> 與 <ItemLink id="void_card" />。
* 第二個 <ItemLink id="interface" />（4）維持預設設定。
* <ItemLink id="storage_bus" /> 的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)
  設得比主倉儲高。篩選可以設成農場產出的東西。

## 運作原理

* 子網路上的 <ItemLink id="interface" /> 把 <ItemLink id="drive" /> 的內容呈現給主網路上的 <ItemLink id="storage_bus" />。
也就是說，儲存匯流排可以直接從驅動器裡的單元存取物品。
* 儲存匯流排的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比較高，
  這樣物品就會優先被放回子網路，而不是塞進你的主倉儲。
* 重點在於，子網路裡的單元裝滿之後，物品不會滿出來流進主網路。如果那座農場是塞住就會壞掉的類型，
  可以改用 <ItemLink id="void_card" /> 把多餘的物品直接刪掉。
* 如果農場產出多種物品，<ItemLink id="equal_distribution_card" /> 可以避免某一種物品把所有單元佔滿、
  害其他物品存不進去。
