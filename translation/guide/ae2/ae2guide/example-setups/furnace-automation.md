---
navigation:
  parent: example-setups/example-setups-index.md
  title: 熔爐自動化
  icon: minecraft:furnace
---

# 熔爐自動化

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。
如果你只是想單獨把熔爐自動化，用漏斗跟儲物箱那些就好。

<ItemLink id="minecraft:furnace" /> 的自動化比[充能器](../example-setups/charger-automation.md)這類簡單機器要麻煩一些。
熔爐得從兩個不同的面進料，再從第三個面取出：待熔煉的物品要從頂面推入，
燃料要從側面推入，成品則要從底部拉出。

當然可以在頂部放一個 <ItemLink id="pattern_provider" />、側面放一個 <ItemLink id="export_bus" /> 持續推入燃料、
底部放一個 <ItemLink id="import_bus" /> 把成品輸入網路。不過這樣要吃掉 3 條[頻道](../ae2-mechanics/channels.md)。

以下是只用 1 條頻道的作法：

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/furnace_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) 樣板供應器：用賽特斯石英扳手改成定向版本，並放入對應的處理樣板。

        ![Iron Pattern](../assets/diagrams/furnace_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (2) 介面：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
        (3) 儲存匯流排 #1：篩選設為煤炭。
        <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
        (4) 儲存匯流排 #2：用反相卡把煤炭設成黑名單。
        <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="pattern_provider" />（1）維持預設設定，放入對應的 <ItemLink id="processing_pattern" />。
    再用 <ItemLink id="certus_quartz_wrench" /> 點它，把它改成定向版本。

  ![Iron Pattern](../assets/diagrams/furnace_pattern.png)

* <ItemLink id="interface" />（2）維持預設設定。
* 第一個 <ItemLink id="storage_bus" />（3）篩選設為煤炭，或你想用的任何燃料。
* 第二個 <ItemLink id="storage_bus" />（4）用 <ItemLink id="inverter_card" /> 把你用的燃料設成黑名單。

## 運作原理

1. <ItemLink id="pattern_provider" /> 把材料推進 <ItemLink id="interface" />。
   （其實為了效率，它是直接穿過那些儲存匯流排推出去的，就像它們是供應器面的延伸一樣。物品從來沒有真正進到介面裡。）
2. 介面設定成什麼都不存，於是它試著把材料推進[網路倉儲](../ae2-mechanics/import-export-storage.md)。
3. 綠色子網路上唯一的倉儲是那兩個 <ItemLink id="storage_bus" />。篩選為煤炭的那個從側面把煤炭放進熔爐的燃料格；
    篩選為「非煤炭」的那個則從頂面把待熔煉的物品放進上方欄位。
4. 熔爐做它的熔煉工作。
5. 漏斗從熔爐底部把成品拉出來，放進供應器的回收格，也就回到了主網路。
