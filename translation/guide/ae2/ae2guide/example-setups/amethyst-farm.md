---
navigation:
  parent: example-setups/example-setups-index.md
  title: 紫水晶農場
  icon: minecraft:amethyst_shard
---

# 紫水晶的養殖

<ItemLink id="growth_accelerator" /> 對紫水晶一樣有效，但平常用 <ItemLink id="annihilation_plane" />
篩選[石英芽](../items-blocks-machines/budding_certus.md)的手法，對紫水晶芽卻行不通。
未成熟的賽特斯石英芽會掉 <ItemLink id="certus_quartz_dust" />，未成熟的紫水晶芽卻什麼都不掉，
而網路永遠存得下「什麼都沒有」，所以破壞面板會照打不誤。

繞過的辦法是替破壞面板附上絲綢之觸。這樣未成熟的紫水晶芽*就會*掉東西了
（各個生長階段的芽方塊本身），也就篩得掉了。

接著得由 <ItemLink id="formation_plane" /> 把 <ItemLink id="minecraft:amethyst_cluster" /> 重新放置出來，
再讓一片沒有絲綢之觸的 <ItemLink id="annihilation_plane" /> 把它打掉，才能拿到 <ItemLink id="minecraft:amethyst_shard" />。

要注意的是晶簇有方向性，所以成形面板的正對面必須有一個實心方塊面。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/amethyst_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 1 1" max="3 2 2">
        (1) 破壞面板 #1：沒有介面可設定，但附上了絲綢之觸。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1 1" max="2.3 2 2">
        (2) 成形面板：篩選設為紫水晶晶簇。
        <ItemImage id="minecraft:amethyst_cluster" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 0.7 1" max="2 1 2">
        (3) 破壞面板 #2：沒有介面可設定，但可以附上幸運。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 1" max="1.3 1 2">
        (4) 儲存匯流排 #1：篩選設為紫水晶碎片。
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 .7" max="1 1 1">
        (5) 儲存匯流排 #2：篩選設為紫水晶碎片。優先權設得比主倉儲高。
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* 第一片 <ItemLink id="annihilation_plane" />（1）沒有介面，無法設定，但必須附上絲綢之觸。
* <ItemLink id="formation_plane" />（2）篩選設為 <ItemLink id="minecraft:amethyst_cluster" />。
* 第二片 <ItemLink id="annihilation_plane" />（3）沒有介面，無法設定，但可以附上幸運。
* 第一個 <ItemLink id="storage_bus" />（4）篩選設為 <ItemLink id="minecraft:amethyst_shard" />。
* 第二個 <ItemLink id="storage_bus" />（5）篩選同樣設為 <ItemLink id="minecraft:amethyst_shard" />，
  並把[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比主倉儲高。

## 運作原理

1. 第一片 <ItemLink id="annihilation_plane" /> 試著打掉面前的東西，但它只打得掉 <ItemLink id="minecraft:amethyst_cluster" />，
    因為子網路上唯一的倉儲是篩選為紫水晶晶簇的 <ItemLink id="formation_plane" />。這招之所以成立，
全靠面板附了絲綢之觸；否則未成熟的芽什麼都不掉，它照樣打得掉。
2. <ItemLink id="formation_plane" /> 把晶簇放到正對面的方塊上。
3. 第二片 <ItemLink id="annihilation_plane" /> 把晶簇打掉，產出 <ItemLink id="minecraft:amethyst_shard" />。
4. 第一個 <ItemLink id="storage_bus" /> 把碎片存進木桶。嚴格說來這裡不必設篩選，因為第二片破壞面板
會遇到的本來就只有長成的晶簇。
5. 第二個 <ItemLink id="storage_bus" /> 讓主網路能存取木桶裡所有的紫水晶碎片。它的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)
設得比較高，這樣紫水晶碎片就會優先被放回木桶，而不是塞進你的主倉儲。
