---
navigation:
  parent: example-setups/example-setups-index.md
  title: 半自動賽特斯農場
  icon: certus_quartz_crystal
  position: 115
---

# 半自動賽特斯農場

可惜的是，[簡易賽特斯農場](simple-certus-farm.md)要全自動運轉就得有 <ItemLink id="flawless_budding_quartz" />，
而那需要動用[空間 IO](../ae2-mechanics/spatial-io.md)，或是直接把農場蓋在[隕石坑](../ae2-mechanics/meteorites.md)上。

不過 AE2 本來就能放置與破壞方塊，所以說不定可以讓農場*自己替你換掉石英芽床*。
（你得定期往輸入木桶裡補一些 <ItemLink id="flawed_budding_quartz" />，
並從裝廢芽床的木桶裡把 <ItemLink id="quartz_block" /> 取走）

想做到全自動，請見[進階賽特斯農場](advanced-certus-farm.md)。

這座農場比[簡易賽特斯農場](simple-certus-farm.md)複雜一些，因為它其實是三套設施擠在一起。

生長速度的估算見[賽特斯石英生長](../ae2-mechanics/certus-growth.md)。

**這是一個複雜的建築，有些東西被擋在別的東西後面，請旋轉鏡頭從各個角度看過一遍**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/semiauto_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) 破壞面板 #1：沒有介面可設定，但可以附上幸運。
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1" max="2.3 3 2">
        (2) 儲存匯流排 #1：篩選設為賽特斯石英水晶。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    晶簇破壞子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) 破壞面板 #2：沒有介面可設定，但附上了絲綢之觸。
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1" max="2.3 2 2">
        (4) 儲存匯流排 #2：篩選設為賽特斯石英方塊。
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    石英方塊破壞子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) 成形面板：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0 1" max="2.3 1 2">
        (6) 輸入匯流排：維持預設設定。
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    芽床放置子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="0.7 2 1" max="1 3 2">
        (7) 儲存匯流排 #3：篩選設為賽特斯石英水晶。優先權設得比主倉儲高。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

    <DiamondAnnotation pos="1.5 0.5 1.5" color="#00ff00">
        手動放入微瑕的賽特斯石英芽床。
        <BlockImage id="flawed_budding_quartz" scale="2" />
    </DiamondAnnotation>

    <DiamondAnnotation pos="1.5 1.5 1.5" color="#00ff00">
        手動取出賽特斯石英方塊。
        <BlockImage id="quartz_block" scale="2" />
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="165" pitch="5" />
</GameScene>

## 設定

### 晶簇破壞：

* 第一片 <ItemLink id="annihilation_plane" />（1）沒有介面，無法設定，但可以附上幸運。
* 第一個 <ItemLink id="storage_bus" />（2）篩選設為 <ItemLink id="certus_quartz_crystal" />。

### 石英方塊破壞：

* 第二片 <ItemLink id="annihilation_plane" />（3）沒有介面，無法設定，但必須附上絲綢之觸。
* 第二個 <ItemLink id="storage_bus" />（4）篩選設為 <ItemLink id="quartz_block" />。

### 芽床放置：

* <ItemLink id="formation_plane" />（5）維持預設設定。
* <ItemLink id="import_bus" />（6）維持預設設定。

### 主網路上：

* 第三個 <ItemLink id="storage_bus" />（7）篩選設為 <ItemLink id="certus_quartz_crystal" />，
  並把[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比主倉儲高。

## 運作原理

### 晶簇破壞：

晶簇破壞子網路的運作方式和[簡易賽特斯農場](simple-certus-farm.md)裡的子網路非常相似。

1. <ItemLink id="annihilation_plane" /> 試著打掉面前的東西，但它只打得掉 <ItemLink id="quartz_cluster" />，
   因為子網路上唯一的倉儲是篩選為 <ItemLink id="certus_quartz_crystal" /> 的 <ItemLink id="storage_bus" />。
2. <ItemLink id="storage_bus" /> 把賽特斯石英水晶存進木桶。

### 石英方塊破壞

石英方塊破壞子網路負責在芽床耗盡、變成普通的 <ItemLink id="quartz_block" /> 之後把它打掉。
運作方式和晶簇破壞類似。

1. <ItemLink id="annihilation_plane" /> 試著打掉面前的東西，但它只打得掉 <ItemLink id="quartz_block" />，
   因為子網路上唯一的倉儲是篩選為 <ItemLink id="quartz_block" /> 的 <ItemLink id="storage_bus" />。
   這片面板必須附上絲綢之觸，芽床被打掉時才不會衰變，面板也才不會提早把它打掉。
2. <ItemLink id="storage_bus" /> 把賽特斯石英方塊存進裝廢芽床的木桶，
   你得手動把它和 <ItemLink id="charged_certus_quartz_crystal" /> 一起丟進水裡讓它復原。

### 芽床放置

芽床放置子網路負責在破壞子網路打掉舊的耗盡芽床之後，放上一塊新的 <ItemLink id="flawed_budding_quartz" />。

1. <ItemLink id="import_bus" /> 從輸入木桶裡取出一塊芽床。
2. 子網路上唯一的倉儲是 <ItemLink id="formation_plane" />，於是芽床被放置出來。

### 主網路上

* <ItemLink id="storage_bus" /> 讓主網路（以及[充能器自動化](charger-automation.md)）能存取木桶裡所有的賽特斯石英水晶。
  它的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比較高，
  這樣賽特斯石英水晶就會優先被放回木桶，而不是塞進你的主倉儲。
