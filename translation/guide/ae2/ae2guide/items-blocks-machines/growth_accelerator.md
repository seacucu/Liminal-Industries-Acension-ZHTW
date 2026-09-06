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

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/growth_accelerator.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

想手動供電的話，在它的頂面或底面放一個 <ItemLink id="crank" />，再右鍵轉動即可。

它只會從兩端有粉紅色福魯伊克斯裝飾的地方接線纜。

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/accelerator_connections.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 配方

<RecipeFor id="growth_accelerator" />
