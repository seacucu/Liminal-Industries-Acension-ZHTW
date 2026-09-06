---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 賽特斯石英生長
  icon: quartz_cluster
---

# 賽特斯石英生長

## 基本上就是從入門頁複製貼上過來的

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/budding_certus_1.snbt" />
</GameScene>

賽特斯石英芽會從[石英芽床](../items-blocks-machines/budding_certus.md)上長出來，和紫水晶類似。如果你打掉還沒長成的石英芽，
會掉落一個 <ItemLink id="certus_quartz_dust" />，且不受幸運影響。如果打掉的是完全長成的晶簇，則會掉落四個
<ItemLink id="certus_quartz_crystal" />，幸運則會增加這個數量。

石英芽床共有四個階級：無瑕、微瑕、破損、重損。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

石英芽每長大一個階段，芽床就有機率衰變一級，最後變成普通的賽特斯石英方塊。把芽床（或賽特斯石英方塊）連同一個以上的
<ItemLink id="charged_certus_quartz_crystal" /> 丟進水裡，就能修復它，新的芽床也是這樣做出來的。

<RecipeFor id="damaged_budding_quartz" />

無瑕的石英芽床不會衰變，能無限產出賽特斯石英。不過它既無法合成，也沒辦法用鎬挖走，就算附了絲綢之觸也一樣。
（但它*可以*用[空間儲存](../ae2-mechanics/spatial-io.md)搬移）

光靠自己，賽特斯石英芽長得非常慢。所幸把 <ItemLink id="growth_accelerator" /> 放在芽床旁邊，
可以大幅加快這個過程。這東西應該列為你最優先要蓋的幾樣設施之一。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_certus_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

如果你的石英還不夠做 <ItemLink id="energy_acceptor" /> 或 <ItemLink id="vibration_chamber" />，
可以做一個 <ItemLink id="crank" /> 插在加速器末端。

自動採收賽特斯石英的作法[在這裡說明](../example-setups/simple-certus-farm.md)。
