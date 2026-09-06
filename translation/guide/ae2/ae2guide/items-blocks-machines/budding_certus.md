---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 賽特斯石英芽床
  icon: flawless_budding_quartz
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:flawless_budding_quartz
- ae2:flawed_budding_quartz
- ae2:chipped_budding_quartz
- ae2:damaged_budding_quartz
- ae2:small_quartz_bud
- ae2:medium_quartz_bud
- ae2:large_quartz_bud
- ae2:quartz_cluster
---

# 賽特斯石英芽床

（另見[賽特斯石英生長](../ae2-mechanics/certus-growth.md)）

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

賽特斯石英芽會從石英芽床上長出來，和紫水晶類似。這種方塊可以在[隕石坑](../ae2-mechanics/meteorites.md)裡找到。
石英芽床共有四個階級：無瑕、微瑕、裂損、重損。用 HWYLA、Jade、The One Probe 之類的模組
（或是 F3 畫面）最容易分辨它們。

微瑕、裂損與重損的芽床，每當石英芽長大一個階段就有機率衰變一級，最後變成普通的 <ItemLink id="quartz_block" />。

無瑕的芽床不會因為長芽而衰變，等於是無限的來源。

用一般的鎬打掉時，石英芽床會衰變一級；用附了絲綢之觸的鎬打掉則不會衰變，唯獨無瑕的例外。
**也就是說，無瑕的石英芽床沒辦法用鎬挖起來搬走**。想搬動它，得用[空間儲存](../ae2-mechanics/spatial-io.md)
把它剪下再貼上。

## 配方

微瑕、裂損與重損的芽床，可以把前一階級的芽床（或一個 <ItemLink id="quartz_block" />）
連同一個以上的 <ItemLink id="charged_certus_quartz_crystal" /> 丟進水裡做出來。

無瑕的芽床無法合成，只能在世界中尋獲。

<Row>
  <RecipeFor id="damaged_budding_quartz" />

  <RecipeFor id="chipped_budding_quartz" />

  <RecipeFor id="flawed_budding_quartz" />
</Row>
