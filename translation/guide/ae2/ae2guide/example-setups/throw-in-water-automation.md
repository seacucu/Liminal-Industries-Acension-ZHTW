---
navigation:
  parent: example-setups/example-setups-index.md
  title: 丟進水裡的自動化
  icon: fluix_crystal
---

# 丟進水裡類配方的自動化

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。

有些配方需要把物品丟進水裡（類似的設施也能把物品丟到別的地方）。
這可以用 <ItemLink id="formation_plane" />、<ItemLink id="annihilation_plane" /> 加上一些配套設施來自動化
（說穿了就是兩條改造過的[管線子網路](pipe-subnet.md)）。

這套設施要搭配[充能器自動化](charger-automation.md)一起用，由後者提供 <ItemLink id="charged_certus_quartz_crystal" />。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (1) 樣板供應器：維持預設設定，放入對應的處理樣板。

        ![Fluix Pattern](../assets/diagrams/fluix_pattern_small.png) ![Flawed Budding Pattern](../assets/diagrams/flawed_budding_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 1" max="2 1 2">
        (2) 介面：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 .7 1" max="2 1 2">
        (3) 成形面板：設定為把輸入物以掉落物的形式丟出。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 2 1" max="2 2.3 2">
        (4) 破壞面板：沒有介面可設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (5) 儲存匯流排：篩選設為那些樣板的產物
        <Row><ItemImage id="fluix_crystal" scale="2" /><BlockImage id="flawless_budding_quartz" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="3.9 0.5 1.5" color="#00ff00">
        通往主網路與充能器自動化
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
    </DiamondAnnotation>

  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

## 設定與樣板

* <ItemLink id="pattern_provider" />（1）維持預設設定，放入對應的 <ItemLink id="processing_pattern" />
  * <ItemLink id="fluix_crystal" /> 直接用 JEI／REI 的預設配方就行：

    ![Fluix Pattern](../assets/diagrams/fluix_pattern.png)

  * <ItemLink id="flawed_budding_quartz" /> 最好直接從 <ItemLink id="quartz_block" /> 做，
    這樣可以避免「某個配方的材料正好是另一個配方的產物」而害儲存匯流排篩不掉的問題：

    ![Flawed Budding Pattern](../assets/diagrams/flawed_budding_pattern.png)

* <ItemLink id="interface" />（2）維持預設設定。
* <ItemLink id="formation_plane" />（3）設定為把輸入物以掉落物的形式丟出。
* <ItemLink id="annihilation_plane" />（4）沒有介面，無法設定。
* <ItemLink id="storage_bus" />（5）篩選設為那些樣板的產物。

## 運作原理

1.  <ItemLink id="pattern_provider" /> 把材料推進側面那個位於綠色子網路上的 <ItemLink id="interface" />。
2.  介面（預設設定為什麼都不存）試著把內容推進[網路倉儲](../ae2-mechanics/import-export-storage.md)。
3.  綠色子網路上唯一的倉儲是 <ItemLink id="formation_plane" />，於是它把收到的物品丟進水裡。
4.  橘色子網路上的 <ItemLink id="annihilation_plane" /> 試著把剛丟下去的物品撿起來，但撿不動，
    因為樣板供應器頂上那個 <ItemLink id="storage_bus" />（橘色子網路上唯一的倉儲）只接受合成的產物。
5.  物品在世界中完成它的轉換。
6.  現在破壞面板撿得動面前的物品了，因為儲存匯流排允許存放它們。
7.  儲存匯流排把產物存進樣板供應器，也就送回了網路。
