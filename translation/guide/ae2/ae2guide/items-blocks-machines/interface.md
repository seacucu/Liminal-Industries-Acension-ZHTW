---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 介面
  icon: interface
  position: 210
categories:
- devices
item_ids:
- ae2:interface
- ae2:cable_interface
---

# 介面

<Row gap="20">
<BlockImage id="interface" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_interface.snbt" />
</GameScene>
</Row>

介面的行為就像一個小型儲物箱兼流體儲罐：它依照你在欄位裡設定要備多少料，
自動從[網路倉儲](../ae2-mechanics/import-export-storage.md)補進來、或把多的送回去。
它會試著在單一遊戲刻內完成，所以每刻最多能進出 9 組物品，
只要你的物品管線夠快，它就是相當快速的輸入或輸出手段。

另一個好用的特性是：大多數流體儲罐只裝得下一種流體，介面卻能同時存放最多 9 種，而且物品也收。
說穿了它就是帶有額外功能的儲物箱或多流體儲罐，而只要不把它接上任何網路，那些額外功能就不會發動。
所以在「想少量存放一堆不同東西」這類小眾情境下，它相當好用。

## 介面內部是怎麼運作的

如前所述，介面本質上就是一個儲物箱兼儲罐，外掛了幾個超級強化版的 <ItemLink id="import_bus" />
與 <ItemLink id="export_bus" />，再加上一堆 <ItemLink id="level_emitter" />。

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_internals.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 0.3 1.3" max="9.7 1 1.7">
        一堆位準發射器，負責控制要備多少料
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 4 1.3" max="9.7 4.7 1.7">
        一堆位準發射器，負責控制要備多少料
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 1.3 1.3" max="9.7 2 1.7">
        一堆超級強化版的輸入匯流排，每個遊戲刻能搬 1 組物品
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/import_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 3 1.3" max="9.7 3.7 1.7">
        一堆超級強化版的輸出匯流排，每個遊戲刻能搬 1 組物品
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/export_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 1" max="10 3 2">
        9 個各自獨立的內部欄位
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="15" />
</GameScene>

## 特殊互動

介面和其他 AE2 [裝置](../ae2-mechanics/devices.md)之間還有幾項特殊功能：

把 <ItemLink id="storage_bus" /> 貼在一個未設定的介面上，會讓介面所屬網路的整個
[網路倉儲](../ae2-mechanics/import-export-storage.md)呈現給儲存匯流排所屬的網路，
就像介面那一側的網路是一個大儲物箱、而儲存匯流排貼在上面一樣。
只要在介面的篩選欄位裡設定要備任何物品，這個效果就會失效。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_storage.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

樣板供應器和[子網路](../ae2-mechanics/subnetworks.md)上的介面也有特殊互動：如果那個介面沒有做任何設定，
供應器會直接跳過介面，把材料推進該子網路的[倉儲](../ae2-mechanics/import-export-storage.md)，
不但不會把介面塞滿一批批材料，更重要的是，倉儲沒空間時它就不會送下一批。

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

## 變體

介面有兩種變體：一般與薄板／[線纜附件](../ae2-mechanics/cable-subparts.md)。
差別在於它的倉庫能從哪些面存取，以及它對哪些面提供網路連線。

*   一般介面允許從所有面推入、拉出與存取它的倉庫，而且和多數 AE2 機器一樣，像線纜那樣對所有面提供網路連線。

*   薄板介面是[線纜附件](../ae2-mechanics/cable-subparts.md)，所以同一條線纜上可以放好幾個，適合緊湊配置。
    它允許從自己那一面推入、拉出與存取倉庫，但不在該面提供網路連線。

一般與薄板兩種形態可以在合成格裡互換。

## 設定

介面上排的欄位決定它要在自己身上備哪些料。把東西放進去、或從 JEI／REI 拖進去之後，
會出現一個扳手圖示讓你設定數量。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

## 升級

介面支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="fuzzy_card" /> 讓它能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="crafting_card" /> 讓介面能向你的[自動合成](../ae2-mechanics/autocrafting.md)系統送出合成請求，
    以取得它要的物品。它會先試著從倉儲取貨，取不到才請求重新合成。

## 優先權

在介面右上角點一下扳手就能設定優先權。優先權較高的介面會比優先權較低的先拿到物品。

## 配方

<Recipe id="network/blocks/interfaces_interface" />

<RecipeFor id="cable_interface" />
