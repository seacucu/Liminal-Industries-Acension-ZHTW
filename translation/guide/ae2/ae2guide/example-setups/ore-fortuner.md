---
navigation:
  parent: example-setups/example-setups-index.md
  title: 自動礦石幸運機
  icon: minecraft:raw_iron
---

# 礦石幸運化的自動化

<ItemLink id="annihilation_plane" /> 可以附上任何鎬的附魔，幸運也不例外。
於是一個顯而易見的用法，就是替幾片面板附上幸運，再讓 <ItemLink id="formation_plane" /> 與 <ItemLink id="annihilation_plane" />
快速地放下與打掉礦石。

要注意的是，<ItemLink id="import_bus" /> 有「逐漸加速」的特性，所以這套設施剛開始會慢，幾秒後才會全速運轉。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/ore_fortuner.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 0 2" max="3 1 3">
        (1) 輸入匯流排：裡面放了幾張加速卡。
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 2" max="2 1 2.3">
        (2) 成形面板：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 0.7" max="2 1 1">
        (3) 破壞面板：沒有介面可設定，但附上了幸運。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 0 0" max="3 1 1">
        (4) 儲存匯流排：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="3.5 0.5 2.5" color="#00ff00">
        輸入
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 0.5 0.5" color="#00ff00">
        輸出
    </DiamondAnnotation>

<DiamondAnnotation pos="4 0.5 1.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

*   <ItemLink id="import_bus" />（1）裡放了幾張 <ItemLink id="speed_card" />。陣列裡的成形面板愈多，需要的加速卡也愈多，
    因為加速卡會讓輸入匯流排一次抽更多物品。
*   <ItemLink id="formation_plane" />（2）維持預設設定。
*   <ItemLink id="annihilation_plane" />（3）沒有介面，無法設定，但附上了幸運。
*   <ItemLink id="storage_bus" />（4）維持預設設定。

## 運作原理

1.  綠色子網路上的 <ItemLink id="import_bus" /> 把第一個木桶裡的方塊輸入到[網路倉儲](../ae2-mechanics/import-export-storage.md)。
2.  綠色子網路上唯一的倉儲是 <ItemLink id="formation_plane" />，於是方塊被放置出來。
3.  橘色子網路上的 <ItemLink id="annihilation_plane" /> 把方塊打掉，過程中套用幸運。
4.  橘色子網路上的 <ItemLink id="storage_bus" /> 把打掉的產物存進第二個木桶。
