---
navigation:
  parent: example-setups/example-setups-index.md
  title: 簡易賽特斯農場
  icon: certus_quartz_crystal
  position: 110
---

# 簡易賽特斯農場

如同[賽特斯石英生長](../ae2-mechanics/certus-growth.md)所述，要自動採收 <ItemLink id="certus_quartz_crystal" />，
靠的是 <ItemLink id="annihilation_plane" /> 與 <ItemLink id="storage_bus" />。
<ItemLink id="growth_accelerator" /> 大幅加快石英芽的生長，接著由面板把長成的 <ItemLink id="quartz_cluster" /> 打掉。
篩選則利用了一個湊巧好用的性質：未成熟的石英芽掉的是 <ItemLink id="certus_quartz_dust" />，而不是什麼都不掉。

這座農場搭配 <ItemLink id="flawless_budding_quartz" /> 可以全自動運轉；
若用的是微瑕、裂損或重損的石英芽床，你就得手動補回芽床。或者，照[半自動賽特斯農場](semiauto-certus-farm.md)
與[進階賽特斯農場](advanced-certus-farm.md)所說的方式，自動補回。

生長速度的估算見[賽特斯石英生長](../ae2-mechanics/certus-growth.md)。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/simple_certus_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="3.7 1 1" max="4 2 2">
        (1) 破壞面板：沒有介面可設定，但可以附上幸運。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="3.3 2 2">
        (2) 儲存匯流排 #1：篩選設為賽特斯石英水晶。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 .7" max="2 2 1">
        (3) 儲存匯流排 #2：篩選設為賽特斯石英水晶。優先權設得比主倉儲高。
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* 第一個 <ItemLink id="annihilation_plane" />（1）沒有介面，無法設定，但可以附上幸運。
* 第一個 <ItemLink id="storage_bus" />（2）篩選設為 <ItemLink id="certus_quartz_crystal" />。
* 第二個 <ItemLink id="storage_bus" />（3）篩選同樣設為 <ItemLink id="certus_quartz_crystal" />，
  並把[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比主倉儲高。

## 運作原理

1. <ItemLink id="annihilation_plane" /> 會試著打掉面前的東西，但它只打得掉 <ItemLink id="quartz_cluster" />，
   因為子網路上唯一的倉儲是那個篩選為 <ItemLink id="certus_quartz_crystal" /> 的 <ItemLink id="storage_bus" />。
4. 第一個 <ItemLink id="storage_bus" /> 把賽特斯石英水晶存進木桶。
5. 第二個 <ItemLink id="storage_bus" /> 讓主網路能存取木桶裡所有的賽特斯石英水晶。它的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)
   設得比較高，這樣賽特斯石英水晶就會優先被放回木桶，而不是塞進你的主倉儲。
