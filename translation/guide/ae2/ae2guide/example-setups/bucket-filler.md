---
navigation:
  parent: example-setups/example-setups-index.md
  title: 水桶裝填機
  icon: minecraft:water_bucket
---

# 水桶裝填機

另見[水桶清空機](bucket-emptier.md)。

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。

有時候人生就是不方便：你要的是一桶桶裝好的流體，而不是流體本身。有些機器可以幫你裝
（例如 Thermal Expansion 的流體轉換器），但你不一定剛好裝了那種模組。所幸原版 Minecraft 也有個沒那麼方便的作法：
<ItemLink id="minecraft:dispenser" />。

**要注意的是，你往往根本不需要這麼做，因為[樣板編碼終端機](../items-blocks-machines/terminals.md#pattern-encoding-terminal)的流體替代
功能，可以讓配方直接使用流體本身，而不是裝著流體的桶子。**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/bucket_filler.snbt" />

<BoxAnnotation color="#dddddd" min="2 1 0" max="3 2 1">
        (1) 樣板供應器：合成鎖定設為「接收到紅石訊號時」，放入對應的處理樣板。

        <Row>
        ![Fill Pattern](../assets/diagrams/water_fill_pattern_small.png)
        ![Fill Pattern](../assets/diagrams/lava_fill_pattern_small.png)
        </Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1.1 0.1" max="3.2 1.9 0.9">
        (2) 介面：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.1 1.1 0.8" max="3.9 1.9 1">
        (3) 儲存匯流排 #1：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="4.05 1.05 0.8" max="4.95 1.95 1">
        (4) 成形面板：用反相卡把桶子設成黑名單。
        <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.2 2 1.2" max="3.8 2.2 1.8">
        (5) 輸入匯流排：用反相卡把桶子設成黑名單。
        <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2.1 2 0.1" max="2.9 2.2 0.9">
        (6) 儲存匯流排 #2：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="0 1.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## 設定

* <ItemLink id="pattern_provider" />（1）合成鎖定設為「接收到紅石訊號時」，放入對應的 <ItemLink id="processing_pattern" />。
  
    ![Charger Pattern](../assets/diagrams/water_fill_pattern.png)
    ![Charger Pattern](../assets/diagrams/lava_fill_pattern.png)

* <ItemLink id="interface" />（2）維持預設設定。
* 第一個 <ItemLink id="storage_bus" />（3）維持預設設定。
* <ItemLink id="formation_plane" />（4）用反相卡把桶子設成黑名單。
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
* <ItemLink id="import_bus" />（5）用反相卡把桶子設成黑名單。
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
* 第二個 <ItemLink id="storage_bus" />（6）維持預設設定。

## 運作原理

1. <ItemLink id="pattern_provider" /> 把材料推進 <ItemLink id="interface" />。
   （其實為了效率，它是直接穿過儲存匯流排與成形面板推出去的，就像那是供應器面的延伸一樣。物品從來沒有真正進到介面裡。）
2. 透過[管線子網路](pipe-subnet.md#providing-to-multiple-places)與 <ItemLink id="formation_plane" /> 所述的機制，
   桶子最後進到 <ItemLink id="minecraft:dispenser" /> 裡，流體則由成形面板放置出來。
3. <ItemLink id="minecraft:comparator" /> 偵測到發射器裡有桶子，於是同時替發射器供電、並鎖住
   <ItemLink id="pattern_provider" />。
4. 發射器用桶子把流體舀起來，此時它裡面是一個裝滿的桶子。
5. <ItemLink id="import_bus" /> 把裝滿的桶子從發射器抽出來，經由 <ItemLink id="storage_bus" />
   存進樣板供應器，也就回到了主網路。
6. 比較器看到發射器空了，供應器隨之解鎖。
