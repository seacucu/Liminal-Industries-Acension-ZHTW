---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 空間錨
  icon: spatial_anchor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:spatial_anchor
---

# 空間錨

<BlockImage id="spatial_anchor" p:powered="true" scale="8"/>

AE2 網路必須位於已載入的區塊中，上面的[裝置](../ae2-mechanics/devices.md)才能運作；
只載入一部分的話，運作可能會不正常。空間錨正是為此而生：它會強制載入所屬網路所佔的區塊。
只要有一條線纜跨過區塊邊界，那個新區塊就會一併載入。

它的「載入」效果會沿著[量子橋接](quantum_bridge.md)傳遞，但不會跨維度。
所以如果你有一條通往地獄的量子橋接，基地那邊的網路和地獄那邊的網路都各需要一個空間錨。

預設情況下，它也會讓載入的區塊維持隨機刻，這一點可以在 AE2 的設定檔裡關掉。

如果你出於某種理由想轉它，它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。

## 設定

*   空間錨提供了一個全域設定的入口，可切換能量以 AE 或 E/FE 顯示。
*   可以在世界中顯示一個全息圖，標出目前正被載入的區塊。

## 能量

空間錨的[能量](../ae2-mechanics/energy.md)消耗依下列公式計算：

e = 80 + (x\*(x+1))/2

其中 x 是被載入的區塊數量

## 配方

<RecipeFor id="spatial_anchor" />
