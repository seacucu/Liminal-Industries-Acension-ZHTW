---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 開關匯流排
  icon: toggle_bus
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:toggle_bus
- ae2:inverted_toggle_bus
---

# 開關匯流排

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/toggle_bus.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

這是一種功能類似 <ItemLink id="fluix_glass_cable" /> 或其他線纜的匯流排，
差別在於它的連線狀態可以用紅石切換，讓你切斷 [ME 網路](../ae2-mechanics/me-network-connections.md)的某一段。

有紅石訊號時它會啟用連線；<ItemLink id="inverted_toggle_bus" /> 的行為則相反，有訊號時反而斷開連線。

要注意的是，切換它們可能會讓網路重新啟動並重新計算已連接的裝置。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

## 配方

<RecipeFor id="toggle_bus" />

<RecipeFor id="inverted_toggle_bus" />
