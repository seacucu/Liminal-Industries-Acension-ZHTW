---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 生長加速器
  icon: growth_accelerator
  position: 310
categories:
- machines
item_ids:
- ae2:growth_accelerator
---

# 生長加速器

<BlockImage id="growth_accelerator" p:powered="true" scale="8"/>

把生長加速器放在芽床旁邊，可以大幅加快賽特斯石英或紫水晶[的生長](../ae2-mechanics/certus-growth.md)。

有趣的是，它*也*能加速各種植物的生長。

它的原理是在自然發生的隨機刻之外，額外對相鄰方塊施加「隨機刻」。
理論上這代表 1 台加速器能讓生長快上約 90 倍，而且效果是相加疊加的。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/growth_accelerator.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

電力可以從頂部或底部輸入，走 AE2 的[線纜](cables.md)或其他模組的電力線纜都行，
AE2 自己的電力（AE）與 Forge Energy（FE）它都收。

想手動供電的話，在它的頂面或底面放一個 <ItemLink id="crank" />，再右鍵轉動即可。

頂面與底面可以靠上面那些粉紅色的福魯伊克斯裝飾認出來。

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/accelerator_connections.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 配方

<RecipeFor id="growth_accelerator" />
