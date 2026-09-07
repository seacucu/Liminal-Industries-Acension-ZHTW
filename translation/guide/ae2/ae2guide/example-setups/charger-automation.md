---
navigation:
  parent: example-setups/example-setups-index.md
  title: 充能器自動化
  icon: charger
---

# 充能器自動化

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。
如果你只是想單獨把 <ItemLink id="charger" /> 自動化，用漏斗跟儲物箱那些就好。

<ItemLink id="charger" /> 的自動化相當單純：由 <ItemLink id="pattern_provider" /> 把材料推進充能器，
再用一條[管線子網路](pipe-subnet.md)或其他物品管線把成品推回供應器。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/charger_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) 樣板供應器：維持預設設定，放入對應的處理樣板。它同時也替充能器供電。

        ![Charger Pattern](../assets/diagrams/charger_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="1 1.3 1">
        (2) 輸入匯流排：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (3) 儲存匯流排：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="pattern_provider" />（1）維持預設設定，放入對應的 <ItemLink id="processing_pattern" />。
  它同時也替 <ItemLink id="charger" /> 提供[能量](../ae2-mechanics/energy.md)，因為它的行為就像一條[線纜](../items-blocks-machines/cables.md)。
  
    ![Charger Pattern](../assets/diagrams/charger_pattern.png)

* <ItemLink id="import_bus" />（2）維持預設設定。
* <ItemLink id="storage_bus" />（3）維持預設設定。

## 運作原理

1. <ItemLink id="pattern_provider" /> 把材料推進 <ItemLink id="charger" />。
2. 充能器做它的充能工作。
3. 綠色子網路上的 <ItemLink id="import_bus" /> 把成品從充能器拉出來，並試著存進[網路倉儲](../ae2-mechanics/import-export-storage.md)。
4. 綠色子網路上唯一的倉儲是那個 <ItemLink id="storage_bus" />，於是成品被存進樣板供應器，也就回到了主網路。
