---
navigation:
  parent: example-setups/example-setups-index.md
  title: 物品／流體「管線」子網路
  icon: storage_bus
---

# 物品／流體「管線」子網路

用 AE2 [裝置](../ae2-mechanics/devices.md)模擬物品或流體管線的簡易作法，
凡是你會用到物品或流體管線的場合都適用，包括把合成的成品送回 <ItemLink id="pattern_provider" />。

一般有兩種作法：

## 輸入匯流排 → 儲存匯流排

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) 輸入匯流排：可以設篩選。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) 儲存匯流排：可以設篩選。它（以及其他你想當作目的地的儲存匯流排）
        必須是這個網路上唯一的倉儲。
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        來源
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        目的地
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

貼在來源容器上的 <ItemLink id="import_bus" />（1）把物品或流體輸入進來，試著存進[網路倉儲](../ae2-mechanics/import-export-storage.md)。
由於網路上唯一的倉儲是 <ItemLink id="storage_bus" />（2）（這正是它必須是子網路、不能放在主網路上的原因），
那些物品或流體就被放進目的地容器，也就完成了搬運。電力由 <ItemLink id="quartz_fiber" /> 提供。
輸入匯流排與儲存匯流排都可以設篩選，但不設篩選的話，這套設施會把它碰得到的東西全部搬走。
這套作法也支援多個輸入匯流排與多個儲存匯流排。

## 儲存匯流排 → 輸出匯流排

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) 儲存匯流排：可以設篩選。它（以及其他你想當作來源的儲存匯流排）
        必須是這個網路上唯一的倉儲。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) 輸出匯流排：必須設篩選。
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        來源
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        目的地
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

貼在目的地容器上的 <ItemLink id="export_bus" /> 試著從[網路倉儲](../ae2-mechanics/import-export-storage.md)拉出篩選中的物品。
由於網路上唯一的倉儲是 <ItemLink id="storage_bus" />（這正是它必須是子網路、不能放在主網路上的原因），
那些物品或流體就從來源容器被拉出來，也就完成了搬運。電力由 <ItemLink id="quartz_fiber" /> 提供。
由於輸出匯流排不設篩選就不會動，這套作法只有在你替輸出匯流排設好篩選時才會運作。
這套作法也支援多個儲存匯流排與多個輸出匯流排。

## 一個不會動的配置（輸入匯流排 → 輸出匯流排）

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_export_pipe.snbt" />

<BoxAnnotation color="#dd3333" min="3.7 0 0" max="4 1 1">
        輸入匯流排：網路上沒有倉儲，所以它沒地方可以輸入。
  </BoxAnnotation>

<BoxAnnotation color="#dd3333" min="1 0 0" max="1.3 1 1">
        (2) 輸出匯流排：網路上沒有倉儲，所以它沒東西可以輸出。
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
        來源
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
        目的地
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

只有輸入匯流排加輸出匯流排的配置不會動。輸入匯流排試著從來源容器抽料，
再把物品或流體存進網路倉儲；輸出匯流排試著從網路倉儲取料，把物品或流體放進目的地容器。
但這個網路**沒有任何倉儲**，所以輸入匯流排輸不進去，輸出匯流排也輸不出來，什麼都不會發生。

## 用同一面同時進料與取料

假設你有一台機器，進料與取出成品都得走同一面（例如 <ItemLink id="charger" />）。
把上面兩種管線子網路組合起來，就能同時把材料推進去、把成品拉出來：

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="4 1 1" max="5 1.3 2">
        (1) 輸入匯流排：可以設篩選。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (2) 儲存匯流排：可以設篩選。它（以及其他你想用來推拉物品的儲存匯流排）
        必須是這個網路上唯一的倉儲。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (3) 你想推拉的那個東西：這裡是一台充能器。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 1" max="1 1.3 2">
        (4) 輸出匯流排：必須設篩選。
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
        來源
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
        目的地
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 介面

原來除了輸入匯流排與輸出匯流排之外，還有其他[裝置](../ae2-mechanics/devices.md)也會對[網路倉儲](../ae2-mechanics/import-export-storage.md)推料與取料！
這裡要講的是 <ItemLink id="interface" />。如果塞進去的物品不在介面設定要備料的清單裡，介面就會把它推進網路倉儲，
這一點可以照著「輸入匯流排 → 儲存匯流排」的方式利用。反過來，把介面設定成備某樣物品，
它就會從網路倉儲把該物品拉過來，效果類似「儲存匯流排 → 輸出匯流排」。
介面可以設定成備某些東西、不備另一些，這樣你就能透過儲存匯流排遠端推拉，如果你出於某種理由想這麼做的話。

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/interface_pipes.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        介面
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        儲存匯流排
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.7 0 2" max="4 1 3">
        儲存匯流排
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 2" max="1 1.3 3">
        儲存匯流排
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 一對多、多對一（以及多對多）

當然，<ItemLink id="import_bus" />、<ItemLink id="export_bus" /> 或 <ItemLink id="storage_bus" /> 都不限於只用一個

<GameScene zoom="3" background="transparent">
<ImportStructure src="../assets/assemblies/many_to_many_pipe.snbt" />

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

## 供料到多個地方

從以上這些，我們可以推導出一種作法：把材料從 <ItemLink id="pattern_provider" /> 的一個面送到許多不同的地方，
例如一排機器，或同一台機器的好幾個面。

這裡不能用「輸入 → 儲存」或「儲存 → 輸出」管線，因為 <ItemLink id="pattern_provider" /> 身上從來不會真的有那些材料。
供應器是把材料*推*給相鄰容器的，所以我們需要一個既相鄰、又能把物品輸入網路的容器。

聽起來就是……<ItemLink id="interface" />！
記得把供應器設成定向或薄板附件模式，或是把介面設成薄板附件模式，兩者才不會形成網路連線。

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        介面（必須是薄板，不能是整格方塊）
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        儲存匯流排
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        你想用樣板供料的目標（多台機器，或同一台機器的多個面）
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>
