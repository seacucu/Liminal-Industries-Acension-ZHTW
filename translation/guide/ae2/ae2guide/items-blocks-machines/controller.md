---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 控制器
  icon: controller
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:controller
---

# 控制器

<BlockImage id="controller" p:state="online" scale="8" />

控制器是 [ME 網路](../ae2-mechanics/me-network-connections.md)的路由中樞。
沒有它的網路屬於「臨時網路」，全網最多只能有 8 個需要頻道的[裝置](../ae2-mechanics/devices.md)。

同一個 [ME 網路](../ae2-mechanics/me-network-connections.md)裡不能有兩台控制器。

控制器每一面提供 32 條[頻道](../ae2-mechanics/channels.md)。

控制器每一格方塊需要 6 AE/t 才能運轉。每格可儲存 8000 AE，
所以較大的網路可能需要額外的儲電。詳見[能量](../ae2-mechanics/energy.md)。

多方塊控制器的形狀相當自由。

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controllers.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

不過還是有幾條規則必須遵守：

1.  同一個 [ME 網路](../ae2-mechanics/me-network-connections.md)上的所有控制器方塊必須相連，否則方塊會變紅。
2.  控制器整體尺寸必須在 7x7x7 以內，否則會變紅。
3.  一格控制器最多只能在一個軸向上有兩個相鄰方塊；違反這條規則的方塊會停用並變紅。

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controller_rules.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

只要規則都遵守且有供電，控制器就會發光並循環變換顏色。

右鍵點擊控制器，會開啟和 <ItemLink id="network_tool" /> 相同的介面

## 配方

<RecipeFor id="controller" />
