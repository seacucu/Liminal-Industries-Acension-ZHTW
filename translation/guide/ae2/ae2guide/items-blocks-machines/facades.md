---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 外牆板
  icon: facade
  icon_components:
    "ae2:facade_item": "minecraft:stone"
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:facade
---

# 外牆板

外牆板可以讓你的基地看起來更整潔。它能包覆兩種粗細的線纜，而且可以用很多種方塊來做。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/facades_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

它可以包覆線纜的所有面，但會讓[附件](../ae2-mechanics/cable-subparts.md)與線纜的連接處露出來。

<GameScene zoom="6"  interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

聰明地運用它，可以美化基地，也可以做出每一面材質都不同的方塊。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_3.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 隱藏外牆板

只要任一隻手拿著<a href="network_tool.md">網路工具</a>，外牆板就會隱藏起來。

外牆板隱藏時，你可以直接與後面的方塊互動，不必先把它拆掉。

## 配方

把你想要材質的那個方塊放在 4 個 <ItemLink id="cable_anchor" /> 中間。

![Facade Recipe](../assets/diagrams/facade_recipe.png)
