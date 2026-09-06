---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 充能器
  icon: charger
  position: 310
categories:
- machines
item_ids:
- ae2:charger
---

# 充能器

<BlockImage id="charger" scale="8" />

充能器提供了一種替支援的工具與 <ItemLink id="certus_quartz_crystal" /> 充能的手段。

電力可以從頂部或底部輸入，走 AE2 的[線纜](cables.md)或其他模組的電力線纜都行，
AE2 自己的電力（AE）與 Forge Energy（FE）它都收。物品可以從任意一面送入或取出。
由於只有成品取得出來，所以不必特地設篩選來避免把還沒充能的賽特斯水晶抽走。
為了方便自動化，它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。

它可以把 <ItemLink id="certus_quartz_crystal" /> 做成 <ItemLink id="charged_certus_quartz_crystal" />，
也可以把 <ItemLink id="minecraft:compass" /> 做成 <ItemLink id="meteorite_compass" />。

想手動供電的話，在它的頂面或底面放一個 <ItemLink id="crank" />，右鍵轉到物品充飽為止。

它同時也是[福魯伊克斯學者](fluix_researcher.md)的工作站。

## 簡易自動化

舉例來說，可旋轉這項特性讓你能像這樣把充能器半自動化：

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 配方

<RecipeFor id="charger" />
