---
navigation:
  parent: example-setups/example-setups-index.md
  title: 水桶清空機
  icon: minecraft:bucket
---

# 水桶清空機

另見[水桶裝填機](bucket-filler.md)。

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。

有時候人生就是不方便：你要的是流體本身，偏偏只做得出裝在桶裡的。有些機器可以幫你倒出來
（例如 Thermal Expansion 的流體轉換器），但你不一定剛好裝了那種模組。所幸原版 Minecraft 也有個沒那麼方便的作法：
<ItemLink id="minecraft:dispenser" />。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/bucket_emptier.snbt" />

<BoxAnnotation color="#dddddd" min="2 1 0" max="3 2 1">
        (1) 樣板供應器：合成鎖定設為「接收到紅石訊號時」，並開啟阻擋模式，放入對應的處理樣板。

        <Row>
        ![Fill Pattern](../assets/diagrams/water_empty_pattern_small.png)
        ![Fill Pattern](../assets/diagrams/lava_empty_pattern_small.png)
        </Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2.1 2 0.1" max="2.9 2.2 0.9">
        (2) 介面：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.1 2 1.1" max="3.9 2.2 1.9">
        (3) 儲存匯流排 #1：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="4.05 1.05 0.8" max="4.95 1.95 1">
        (4) 破壞面板：沒有介面可設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.2 1.2 0.8" max="3.8 1.8 1">
        (5) 輸入匯流排：篩選設為桶子。
        <ItemImage id="minecraft:bucket" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1.1 0.1" max="3.2 1.9 0.9">
        (6) 儲存匯流排 #2：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="0 1.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## 設定

* <ItemLink id="pattern_provider" />（1）合成鎖定設為「接收到紅石訊號時」，並開啟阻擋模式，
  放入對應的 <ItemLink id="processing_pattern" />。
  
    ![Charger Pattern](../assets/diagrams/water_empty_pattern.png)
    ![Charger Pattern](../assets/diagrams/lava_empty_pattern.png)

* <ItemLink id="interface" />（2）維持預設設定。
* 第一個 <ItemLink id="storage_bus" />（3）維持預設設定。
* <ItemLink id="annihilation_plane" />（4）沒有介面，無法設定。
* <ItemLink id="import_bus" />（5）篩選設為桶子。
  <ItemImage id="minecraft:bucket" scale="2" />
* 第二個 <ItemLink id="storage_bus" />（6）維持預設設定。

## 運作原理

1. <ItemLink id="pattern_provider" /> 把材料推進 <ItemLink id="interface" />。
   （其實為了效率，它是直接穿過儲存匯流排推出去的，就像那是供應器面的延伸一樣。物品從來沒有真正進到介面裡。）
2. 透過[管線子網路](pipe-subnet.md#providing-to-multiple-places)所述的機制，
   桶子最後進到 <ItemLink id="minecraft:dispenser" /> 裡。
3. <ItemLink id="minecraft:comparator" /> 偵測到發射器裡有桶子，於是同時替發射器供電、並鎖住
   <ItemLink id="pattern_provider" />。
4. 發射器把桶裡的流體倒出去，此時它裡面剩下一個空桶。
5. <ItemLink id="import_bus" /> 把空桶從發射器抽出來，經由 <ItemLink id="storage_bus" />
   存進樣板供應器，也就回到了主網路。
6. 比較器看到發射器空了，供應器隨之解鎖。
