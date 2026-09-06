---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 量子橋接
  icon: quantum_ring
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:quantum_link
- ae2:quantum_ring
---

# 量子網路橋接

![A formed Quantum Network Bridge](../assets/diagrams/quantum_bridge_demonstration.png)

量子網路橋接可以把一個[網路](../ae2-mechanics/me-network-connections.md)延伸到無限遠，甚至跨越維度。
它總共能承載 32 條頻道（不管線纜怎麼接在各個面上），
本質上就是一條無線的[緻密線纜](cables.md#dense-cable)。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_2.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="6 2 3">
        兩端之間一條想像中的線纜
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

要特別注意，**兩端都必須位於已載入的區塊中**，所以兩端相距很遠時，
就得用 <ItemLink id="spatial_anchor" /> 或其他區塊載入器。

# 量子環

<BlockImage id="quantum_ring" scale="8" />

用八個這種方塊圍住一個 <ItemLink id="quantum_link" />，就能組成一座量子網路橋接。
只有緊鄰 <ItemLink id="quantum_link" /> 的那 4 個 <ItemLink id="quantum_ring" /> 方塊接受網路連線，
四個角落的方塊接不了線纜。

## 配方

<RecipeFor id="quantum_ring" />

# 量子連結倉

<BlockImage id="quantum_link" scale="8" />

一個這種方塊被 <ItemLink id="quantum_ring" /> 圍起來，就能組成一座量子網路橋接。
這個方塊不接任何線纜，只有在整座橋接完成時才會被視為網路的一部分。

它的內部只能放一顆 <ItemLink id="quantum_entangled_singularity" />，而且可以自動化存取。

## 配方

<RecipeFor id="quantum_link" />
