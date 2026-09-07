---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 破壞面板
  icon: annihilation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:annihilation_plane
---

# 破壞面板

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/annihilation_plane.snbt" />
</GameScene>

破壞面板負責打掉方塊與撿拾掉落物。它的行為類似 <ItemLink id="import_bus" />，把東西推進
[網路倉儲](../ae2-mechanics/import-export-storage.md)。物品必須碰到面板的正面才會被撿走，它不會做範圍收集。

破壞面板可以附上任何鎬的附魔，所以是的，只要你的模組包允許，你大可替幾片附上誇張等級的幸運，
拿去[自動化礦石處理](../example-setups/ore-fortuner.md)。此外，絲綢之觸的效果如你所想，
效率會降低破壞方塊的耗電，耐久則讓它有機率完全不耗電。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

**記得在你的領地保護裡開放假玩家權限**

## 篩選

破壞面板只有在它的網路存得下產生的掉落物時，才會打掉方塊或撿起物品。
也就是說，要替它設篩選，*你得限制它所在的網路能存放什麼*，最常見的作法是把它放在[子網路](../ae2-mechanics/subnetworks.md)上。
用 <ItemLink id="storage_bus" /> 或[儲存單元](../items-blocks-machines/storage_cells.md)做[分區設定](cell_workbench.md)就能達成。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        篩選設為你想打掉的那個東西會掉落的物品。
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
        分區設為你想打掉的那個東西會掉落的物品。
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

再強調一次，它是*依掉落物*來篩選的。舉例來說，如果你想篩選 <ItemLink id="minecraft:amethyst_cluster" /> 的破壞，
那面板就得附上絲綢之觸；否則前面幾個生長階段什麼都不掉，而網路永遠存得下「什麼都沒有」，
面板就會照打不誤。

## 配方

<RecipeFor id="annihilation_plane" />
