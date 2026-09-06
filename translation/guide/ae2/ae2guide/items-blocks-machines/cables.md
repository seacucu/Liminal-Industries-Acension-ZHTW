---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 線纜
  icon: fluix_glass_cable
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:white_glass_cable
- ae2:orange_glass_cable
- ae2:magenta_glass_cable
- ae2:light_blue_glass_cable
- ae2:yellow_glass_cable
- ae2:lime_glass_cable
- ae2:pink_glass_cable
- ae2:gray_glass_cable
- ae2:light_gray_glass_cable
- ae2:cyan_glass_cable
- ae2:purple_glass_cable
- ae2:blue_glass_cable
- ae2:brown_glass_cable
- ae2:green_glass_cable
- ae2:red_glass_cable
- ae2:black_glass_cable
- ae2:fluix_glass_cable
- ae2:white_covered_cable
- ae2:orange_covered_cable
- ae2:magenta_covered_cable
- ae2:light_blue_covered_cable
- ae2:yellow_covered_cable
- ae2:lime_covered_cable
- ae2:pink_covered_cable
- ae2:gray_covered_cable
- ae2:light_gray_covered_cable
- ae2:cyan_covered_cable
- ae2:purple_covered_cable
- ae2:blue_covered_cable
- ae2:brown_covered_cable
- ae2:green_covered_cable
- ae2:red_covered_cable
- ae2:black_covered_cable
- ae2:fluix_covered_cable
- ae2:white_covered_dense_cable
- ae2:orange_covered_dense_cable
- ae2:magenta_covered_dense_cable
- ae2:light_blue_covered_dense_cable
- ae2:yellow_covered_dense_cable
- ae2:lime_covered_dense_cable
- ae2:pink_covered_dense_cable
- ae2:gray_covered_dense_cable
- ae2:light_gray_covered_dense_cable
- ae2:cyan_covered_dense_cable
- ae2:purple_covered_dense_cable
- ae2:blue_covered_dense_cable
- ae2:brown_covered_dense_cable
- ae2:green_covered_dense_cable
- ae2:red_covered_dense_cable
- ae2:black_covered_dense_cable
- ae2:fluix_covered_dense_cable
- ae2:white_smart_cable
- ae2:orange_smart_cable
- ae2:magenta_smart_cable
- ae2:light_blue_smart_cable
- ae2:yellow_smart_cable
- ae2:lime_smart_cable
- ae2:pink_smart_cable
- ae2:gray_smart_cable
- ae2:light_gray_smart_cable
- ae2:cyan_smart_cable
- ae2:purple_smart_cable
- ae2:blue_smart_cable
- ae2:brown_smart_cable
- ae2:green_smart_cable
- ae2:red_smart_cable
- ae2:black_smart_cable
- ae2:fluix_smart_cable
- ae2:white_smart_dense_cable
- ae2:orange_smart_dense_cable
- ae2:magenta_smart_dense_cable
- ae2:light_blue_smart_dense_cable
- ae2:yellow_smart_dense_cable
- ae2:lime_smart_dense_cable
- ae2:pink_smart_dense_cable
- ae2:gray_smart_dense_cable
- ae2:light_gray_smart_dense_cable
- ae2:cyan_smart_dense_cable
- ae2:purple_smart_dense_cable
- ae2:blue_smart_dense_cable
- ae2:brown_smart_dense_cable
- ae2:green_smart_dense_cable
- ae2:red_smart_dense_cable
- ae2:black_smart_dense_cable
- ae2:fluix_smart_dense_cable
---
# 線纜

<GameScene zoom="3" background="transparent">
  <ImportStructure src="../assets/assemblies/cables.snbt" />
  <IsometricCamera yaw="180" pitch="30" />
</GameScene>

ME 網路雖然也能靠相鄰的 ME 機器串起來，但線纜才是把網路延伸到大範圍的主要手段。

用不同顏色的線纜可以確保相鄰的線纜不會互相連接，讓[頻道](../ae2-mechanics/channels.md)分配得更有效率。
線纜顏色也會影響接在上面的終端機顏色，所以你的終端機不必全是紫色的。福魯伊克斯線纜可以接上任何顏色。

要特別注意，**頻道和線纜顏色完全無關**

## 一個重要提醒

**如果你剛接觸 AE2、還不熟悉頻道，那就盡量到處用智慧線纜與緻密智慧線纜。
它會把頻道在網路裡的走法顯示出來，讓你更容易理解它們的行為。**

## 另一個提醒

**它們不是物品、流體、能量之類的管線。** 它們沒有內部倉庫，樣板供應器與機器不會往裡面「推」東西，
它們唯一的作用就是把 AE2 [裝置](../ae2-mechanics/devices.md)串成一個網路。

## 玻璃線纜

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/fluix_glass_cable.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="fluix_glass_cable" /> 是最容易製作的線纜，可以傳輸電力與最多 8 條[頻道](../ae2-mechanics/channels.md)。
它有 17 種顏色，預設是福魯伊克斯色，用 16 種染料的任一種都能染色。

要合成有色線纜，用 8 條同型的線纜圍住任一種染料即可
（線纜的顏色無所謂，但型別必須相同，玻璃就全玻璃、智慧就全智慧）。
你也可以在世界中用任何相容於 Forge 的油漆刷替線纜上色。

把任何有色線纜和一個水桶一起合成，就能洗掉顏色。

用羊毛把線纜包起來就成了 <ItemLink id="fluix_covered_cable" />；
做成 <ItemLink id="fluix_smart_cable" /> 則能讓你更清楚地掌握[頻道](../ae2-mechanics/channels.md)的狀況。

<RecipeFor id="fluix_glass_cable" />

<RecipeFor id="blue_glass_cable" />

## 包覆線纜

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

包覆線纜在遊戲性上並沒有比 <ItemLink id="fluix_glass_cable" /> 多任何好處，
但如果你偏好包覆的外觀，它就是另一個美觀上的選擇。

上色方式和 <ItemLink id="fluix_glass_cable" /> 相同。四條 <ItemLink id="fluix_covered_cable" />
加上紅石與螢光石，可以合成 <ItemLink id="fluix_covered_dense_cable" />。

<Recipe id="network/cables/covered_fluix" />

<RecipeFor id="blue_covered_cable" />

## 緻密線纜

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

容量更大的線纜，可以承載 32 條頻道，而一般線纜只能承載 8 條。
不過它不支援匯流排，所以在接匯流排或面板之前，你得先從緻密線纜降到較細的線纜
（例如 <ItemLink id="fluix_glass_cable" /> 或 <ItemLink id="fluix_smart_cable" />）。

緻密線纜會稍微改寫頻道的「最短路徑」行為：頻道會先取通往緻密線纜的最短路徑，
再取經過該緻密線纜通往控制器的最短路徑。

<Recipe id="network/cables/dense_covered_fluix" />

<RecipeFor id="blue_covered_dense_cable" />

## 智慧線纜

<Row>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
</Row>

它們的外觀和 <ItemLink id="fluix_covered_cable" /> 有幾分相似，但具備診斷功能：
它會把線纜上的頻道用量視覺化，頻道以發亮的彩色線條呈現，沿著線纜上的黑色條紋延伸，
讓你一眼看出網路上的頻道是怎麼被使用的。一般智慧線纜的前四條頻道顯示為與線纜同色的線條，
後四條則顯示為白線。緻密智慧線纜則是每一條紋路代表 4 條頻道。

在有 <ItemLink id="controller" /> 的網路上，線纜上的線條顯示的是頻道實際走的路徑。

臨時網路上的智慧線纜則改為顯示整個網路已使用的頻道數，而不是流經該條線纜的頻道數。

它們的上色方式同樣和 <ItemLink id="fluix_glass_cable" /> 相同。

<Recipe id="network/cables/smart_fluix" />

<Recipe id="network/cables/dense_smart_fluix" />

<RecipeFor id="blue_smart_cable" />
