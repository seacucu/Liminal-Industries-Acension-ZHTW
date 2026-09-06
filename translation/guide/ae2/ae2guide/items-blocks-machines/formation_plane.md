---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 成形面板
  icon: formation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:formation_plane
---

# 成形面板

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/formation_plane.snbt" />
</GameScene>

成形面板負責放置方塊與丟出物品。它的行為類似一個只進不出的 <ItemLink id="storage_bus" />：
當 <ItemLink id="import_bus" />、<ItemLink id="interface" /> 這類[裝置](../ae2-mechanics/devices.md)
往[網路倉儲](../ae2-mechanics/import-export-storage.md)送東西而「存」到它身上時，它就放置或丟出。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

這個[裝置](../ae2-mechanics/devices.md)運用的機制，和[管線子網路](../example-setups/pipe-subnet.md)裡儲存匯流排那一套相同，
所以在那些設施裡，只要你想要的是放置方塊或丟出物品而不是搬運，就可以拿它取代儲存匯流排。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

**記得在你的領地保護裡開放假玩家權限**

## 篩選

預設情況下面板什麼都會放。把物品放進它的篩選欄位就等於設定白名單，只有那些指定的物品會被放置。

物品與流體都能直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

## 優先權

在介面右上角點一下扳手就能設定優先權。
進入網路的物品會先送往優先權最高的倉儲。

## 設定

*   面板可以設定成在世界中放置方塊，或是丟出掉落物

## 升級

成形面板支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="capacity_card" /> 增加篩選欄位的數量
*   <ItemLink id="fuzzy_card" /> 讓面板能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="inverter_card" /> 把篩選從白名單切換成黑名單

## 配方

<RecipeFor id="formation_plane" />
