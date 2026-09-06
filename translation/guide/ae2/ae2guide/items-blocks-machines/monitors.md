---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 監視器
  icon: storage_monitor
  position: 210
categories:
- devices
item_ids:
- ae2:storage_monitor
- ae2:conversion_monitor
---

# 監視器

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/monitors.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

監視器讓你不必開啟介面，就能檢視單一物品或流體，並與之互動。

監視器會繼承它所安裝的那條[線纜](cables.md)的顏色。

如果監視器裝在地板或天花板上，可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉它。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

# 倉儲監視器

顯示某個物品或流體及其數量。放在你的農場旁邊之類的地方……

*不*需要[頻道](../ae2-mechanics/channels.md)。

操作方式：

*   拿著物品右鍵，或拿著流體容器連按兩次右鍵，就能把監視器設定成該物品或流體。
*   空手右鍵可以清除監視器的設定。
*   空手潛行右鍵可以鎖定監視器。

## 配方

<RecipeFor id="storage_monitor" />

# 轉換監視器

轉換監視器和倉儲監視器類似，但它讓你能存取所設定的物品。

如果所設定的物品可以[自動合成](../ae2-mechanics/autocrafting.md)而倉儲裡又沒有庫存，
試著取出時就會改為開啟一個介面，讓你指定要合成的數量。

它*確實*需要一條[頻道](../ae2-mechanics/channels.md)。

額外的操作方式：

*   左鍵取出一組所設定的物品；若倉儲裡沒有庫存，則改為請求合成該物品。
*   拿著任何物品右鍵，就能把該物品送進去。
*   空手右鍵會把你物品欄裡所有所設定的物品全部送進去。

## 配方

<RecipeFor id="conversion_monitor" />
