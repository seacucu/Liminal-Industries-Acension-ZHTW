---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 空間 IO
  icon: spatial_storage_cell_2
---

# 空間 IO

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/spatial_storage_1x1x1.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="2 2 2">
        要搬移的空間範圍
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />

</GameScene>

空間 IO 讓你把世界中一整塊實體空間剪下再貼上。可以用它搬走 <ItemLink id="flawless_budding_quartz" />、
在基地裡留一個房間隨時抽換內裝以應付不同用途，甚至搬走終界傳送門！

它的原理是把指定的範圍與空間儲存維度中同樣大小的一塊空間*對調*：
塔陣裡的東西被送進空間儲存維度，該維度裡的東西則被送到塔陣中。

也就是說，只要你有辦法在維度之間往返（空間 IO *確實*做得出傳送裝置，
但作法非常複雜、有點不穩，也超出本指南的範圍），就能把它們當成自訂尺寸的緊湊機器或口袋維度來用。

# 多方塊結構

空間 IO 的元件必須照特定方式排列才能運作，也才能界定要剪下貼上的範圍。

所有元件必須位於同一個[網路](me-network-connections.md)上，而且一個網路只能有一組空間 IO 設施。
因此建議把它放在[子網路](subnetworks.md)上。

## 空間 IO 埠

<BlockImage id="spatial_io_port" p:powered="true" scale="4" />

<ItemLink id="spatial_io_port" /> 負責控制整個空間 IO 作業。它會顯示多方塊結構的各項數據，
並放置[空間單元](../items-blocks-machines/spatial_cells.md)。

它顯示的資訊有
- 網路目前的[能量](energy.md)與上限
- 執行這次作業所需的能量。這個數字可能相當大，而且是瞬間抽走的，所以務必備妥足夠的[能量電池](../items-blocks-machines/energy_cells.md)裝得下。
- 塔陣的效率
- 界定出來的範圍大小

要執行空間 IO 作業，把空間儲存單元放進輸入格，再給空間 IO 埠一個紅石脈衝。
它就會把塔陣內的範圍與空間儲存維度裡的範圍*對調*。也就是說，如果你先把一組方塊送進空間儲存維度，
*接著在塔陣裡擺上另一組方塊*，再把單元放回輸入格並觸發 IO 埠，
第二組方塊會消失，第一組方塊則會回來。

**小心，範圍內的任何實體都會一起被帶走，包括你自己。要是沒有離開的手段，你就會被困在空間儲存維度裡，
待在一個漆黑而空無一物的箱子中。** 拿來惡整朋友剛剛好！

## 空間塔

<BlockImage id="spatial_pylon" p:powered_on="true" scale="4" />

<ItemLink id="spatial_pylon" /> 是空間 IO 設施的主體，負責界定作用範圍。

範圍的算法是：取所有空間塔外緣的邊界盒，再朝各方向各縮進 1 格。

規則如下：
- 最小尺寸 3x3x3（界定出 1x1x1 的範圍）
- 所有空間塔都必須位於外緣的邊界盒上
- 所有空間塔都必須在同一個網路上
- 每根塔至少要 2 格長

舉例來說，假設你想界定一個 3x3x3 的範圍。依照規則 2，所有空間塔都必須落在該範圍外側的 5x5x5 殼上。
只要都在那層厚度 1 格的 5x5x5 殼裡，怎麼排幾乎都行。

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/spatial_storage_3x3x3_pylon_demonstration.snbt" />

<BoxAnnotation color="#33dd33" min="1 1 1" max="4 4 4">
        要搬移的空間範圍
  </BoxAnnotation>

<BoxAnnotation color="#3333ff" min="5 5 0" max="0 0 5">
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

比較合理的排法是這樣：

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/better_spatial_storage_3x3x3.snbt" />

<BoxAnnotation color="#33dd33" min="1 1 1" max="4 4 4">
        要搬移的空間範圍
  </BoxAnnotation>

<BoxAnnotation color="#3333ff" min="5 5 0" max="0 0 5">
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 效率

塔陣的效率取決於你把那層殼填滿了多少。用最省的配置去包一個很大的範圍會極沒效率，
所需能量甚至可能高達*數十億* AE。

## 單元的尺寸

[空間單元](../items-blocks-machines/spatial_cells.md)一旦用過，就會被永久固定成一組 XYZ 尺寸（例如 3x4x2），
並與空間儲存維度中的某塊空間綁定。**空間單元用過之後，無法重設、重新格式化，也無法改變尺寸。**
想換尺寸就做一個新的單元。

這裡說的尺寸和單元名稱上的數字不是同一回事，一個 16³ 單元的尺寸可以是*不超過* 16x16x16 的任意組合。

還要注意的是這個範圍有方向性，不能旋轉。2x2x3 和 3x2x2 雖然一樣大，卻不是同一回事。

如果單元的 XYZ 尺寸與界定出來的範圍（在 IO 埠上看得到）不符，IO 埠就不會動作。
