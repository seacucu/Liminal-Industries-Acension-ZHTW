---
navigation:
  parent: example-setups/example-setups-index.md
  title: 進階賽特斯農場
  icon: certus_quartz_crystal
  position: 120
---

# 進階賽特斯農場

這基本上就是[半自動賽特斯農場](semiauto-certus-farm.md)，只是完全整合進了你的 ME 系統。

它不再需要你囤一大堆芽床、每隔一陣子手動復原，
而是靠[充能器自動化](charger-automation.md)與[丟進水裡的自動化](throw-in-water-automation.md)自動完成。

**這是一個複雜的建築，有些東西被擋在別的東西後面，請旋轉鏡頭從各個角度看過一遍**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/advanced_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) 破壞面板 #1：沒有介面可設定，但可以附上幸運。
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1.7" max="3 3 2">
        (2) 儲存匯流排 #1：篩選設為賽特斯石英水晶。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    晶簇破壞子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) 破壞面板 #2：沒有介面可設定，但附上了絲綢之觸。
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1.7" max="3 2 2">
        (4) 儲存匯流排 #2：篩選設為賽特斯石英方塊。
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    石英方塊破壞子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) 成形面板：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0.7 2" max="3 1 3">
        (6) 輸入匯流排：篩選設為微瑕的賽特斯石英芽床。
        <BlockImage id="flawed_budding_quartz" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    芽床放置子網路
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="1.7 2 2" max="2 3 3">
        (7) 儲存匯流排 #3：篩選設為賽特斯石英水晶。優先權設得比主倉儲高。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#aaaadd" min="2 1 2" max="3 2 3">
        (8) 介面：設定成在自己身上備妥 1 個微瑕的賽特斯石英芽床，並裝有合成卡。
        <Row><BlockImage id="flawed_budding_quartz" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="1.5 0.5 0" color="#00ff00">
        通往主網路、充能器自動化與丟進水裡的自動化
        <Row>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        </Row>
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
* <ItemLink id="import_bus" />（6）篩選設為 <ItemLink id="flawed_budding_quartz" />。

### 主網路上：

* 第三個 <ItemLink id="storage_bus" />（7）篩選設為 <ItemLink id="certus_quartz_crystal" />，
  並把[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比主倉儲高。
* <ItemLink id="interface" />（8）設定成在自己身上備妥 1 個微瑕的賽特斯石英芽床，並裝有 <ItemLink id="crafting_card" />。

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
2. <ItemLink id="storage_bus" /> 把賽特斯石英方塊存進 <ItemLink id="interface" />，
   好讓[丟進水裡的自動化](throw-in-water-automation.md)拿它去做出新的 <ItemLink id="flawed_budding_quartz" />。

### 芽床放置

芽床放置子網路負責在破壞子網路打掉舊的耗盡芽床之後，放上一塊新的 <ItemLink id="flawed_budding_quartz" />。

1. <ItemLink id="import_bus" /> 從 <ItemLink id="interface" /> 取出一塊芽床，輸入到[網路倉儲](../ae2-mechanics/import-export-storage.md)。
2. 子網路上唯一的倉儲是 <ItemLink id="formation_plane" />，於是芽床被放置出來。

### 主網路上

* <ItemLink id="storage_bus" /> 讓主網路（以及[充能器自動化](charger-automation.md)）能存取木桶裡所有的賽特斯石英水晶。
  它的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比較高，
  這樣賽特斯石英水晶就會優先被放回木桶，而不是塞進你的主倉儲。
* <ItemLink id="interface" /> 一方面讓芽床放置子網路取得 <ItemLink id="flawed_budding_quartz" />，
    另一方面也讓石英方塊破壞子網路有辦法把耗盡的方塊送回主網路。
    <ItemLink id="crafting_card" /> 則讓介面能向主網路的[自動合成](../ae2-mechanics/autocrafting.md)請求新的芽床。
