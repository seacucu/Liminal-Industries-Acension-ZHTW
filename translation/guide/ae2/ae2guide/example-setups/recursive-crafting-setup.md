---
navigation:
  parent: example-setups/example-setups-index.md
  title: 遞迴合成
  icon: minecraft:netherite_upgrade_smithing_template
---

# 一套遞迴合成的設施

如同[自動合成](../ae2-mechanics/autocrafting.md)所述，自動合成的規劃演算法處理不了「主產物本身就是材料之一」的配方。
舉例來說，它就處理不了複製 <ItemLink id="minecraft:netherite_upgrade_smithing_template" />。

一種解法，是利用 <ItemLink id="level_emitter" /> 能假扮成[樣板](../items-blocks-machines/patterns.md)的能力。

接著用它啟動一套會不斷執行該合成的小設施。這裡我們就以複製
<ItemLink id="minecraft:netherite_upgrade_smithing_template" /> 為例。

<RecipeFor id="minecraft:netherite_upgrade_smithing_template" />

***

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/recursive_recipe_setup.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) 介面：設定成備妥所需的其他材料：鑽石與地獄石。
        <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="minecraft:netherrack" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 1 0.3" max="2.7 1.3 0.7">
        (2) 位準發射器：設定為「獄髓升級模板」，模式設為「發出紅石訊號以進行合成」。
        <Row><ItemImage id="minecraft:netherite_upgrade_smithing_template" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
        (3) 輸入匯流排 #1：篩選設為介面正在備的那些物品。裝有紅石卡，紅石模式設為
        「接收到紅石訊號時啟用」。
        <Row>
        <ItemImage id="minecraft:diamond" scale="2" />
        <ItemImage id="minecraft:netherrack" scale="2" />
        <ItemImage id="redstone_card" scale="2" />
        </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="4 1.3 2">
        (4) 儲存匯流排 #1：優先權設得比另一個儲存匯流排高。非常重要。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 0 1" max="4 1 2">
        (5) 分子組裝機：裡面放著複製升級模板的樣板。

        ![Pattern](../assets/diagrams/smithing_template_pattern_small.png)

        另外在你第一次搭建時，要先手動放一個升級模板進去。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        (6) 輸入匯流排 #2：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 1" max="2 1 1.3">
        (7) 儲存匯流排 #2：篩選設為「獄髓升級模板」。優先權設得比另一個儲存匯流排低。
        <ItemImage id="minecraft:netherite_upgrade_smithing_template" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="15" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="interface" />（1）設定成備妥所需的其他材料：鑽石與地獄石。
* <ItemLink id="level_emitter" />（2）設定為「獄髓升級模板」，模式設為「發出紅石訊號以進行合成」。
* 第一個 <ItemLink id="import_bus" />（3）篩選設為介面正在備的那些物品。它裝有紅石卡，紅石模式設為「接收到紅石訊號時啟用」。
* 第一個 <ItemLink id="storage_bus" />（4）的[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)設得比第二個儲存匯流排*高*。
* <ItemLink id="molecular_assembler" />（5）裡面放著複製升級模板的樣板，另外還手動放了一個升級模板進去。

  ![Pattern](../assets/diagrams/smithing_template_pattern.png)

* 第二個 <ItemLink id="import_bus" />（6）維持預設設定。
* 第二個 <ItemLink id="storage_bus" />（7）篩選設為「獄髓升級模板」，[優先權](../ae2-mechanics/import-export-storage.md#storage-priority)比第一個儲存匯流排*低*。

## 運作原理

1. <ItemLink id="level_emitter" /> 因為插了 <ItemLink id="crafting_card" /> 又設為「發出紅石訊號以進行合成」，
   於是假扮成一份[樣板](../items-blocks-machines/patterns.md)。這樣「獄髓升級模板」就會出現在
   [終端機](../items-blocks-machines/terminals.md)裡，成為可以[自動合成](../ae2-mechanics/autocrafting.md)的項目。
2. 收到該物品的合成請求時（不論來自玩家還是系統自己），位準發射器就會啟動。
3. 第一個 <ItemLink id="import_bus" /> 被位準發射器啟用，把 <ItemLink id="interface" /> 備著的材料抽出來。
4. 網路上唯一存得下那些材料的 <ItemLink id="storage_bus" />，是組裝機上的那個。
5. <ItemLink id="molecular_assembler" /> 收到材料（它裡面本來就有 1 個升級模板），執行合成，產出 2 個升級模板。
6. 第二個 <ItemLink id="import_bus" /> 抽走 1 個升級模板。
7. 第一個儲存匯流排優先權較高，所以那個升級模板又被送回組裝機裡。
8. 第二個 <ItemLink id="import_bus" /> 再抽走 1 個升級模板。
9. 組裝機已經放不下另一個升級模板，所以第二個升級模板流向優先權較低的儲存匯流排，被送進介面。
10. <ItemLink id="interface" /> 沒有設定要備升級模板，於是把它送進網路。
