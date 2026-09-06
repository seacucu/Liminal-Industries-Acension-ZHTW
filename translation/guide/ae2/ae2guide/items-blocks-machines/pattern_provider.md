---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 樣板供應器
  icon: pattern_provider
  position: 210
categories:
- devices
item_ids:
- ae2:pattern_provider
- ae2:cable_pattern_provider
---

# 樣板供應器

<Row gap="20">
<BlockImage id="pattern_provider" scale="8" />
<BlockImage id="pattern_provider" p:push_direction="up" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_pattern_provider.snbt" />
</GameScene>
</Row>

樣板供應器是[自動合成](../ae2-mechanics/autocrafting.md)系統與外界互動的主要管道。
它把[樣板](patterns.md)中的材料推給相鄰容器，別的東西也能塞進它以送入網路。
把機器的產出用管線送回附近的樣板供應器（通常就是推出材料的那一個），
往往能省下一條頻道，比用 <ItemLink id="import_bus" /> 把機器產出拉進網路更省。

要注意的是，它是直接從合成 CPU 的[合成儲存器](crafting_cpu_multiblock.md#crafting-storage)推出材料的，
自己的倉庫裡從來不會真的有那些材料，所以你沒辦法從它身上抽料。
你得讓供應器先推給另一個容器（例如木桶），再從那裡抽。

另外要注意，供應器必須一次把所有材料推出去，沒辦法只推半批。這一點很值得善加利用。

樣板供應器和[子網路](../ae2-mechanics/subnetworks.md)上的介面有個特殊互動：如果那個介面沒有做任何設定（請求格是空的），
供應器會直接跳過介面，把材料推進該子網路的[倉儲](../ae2-mechanics/import-export-storage.md)，
不但不會把介面塞滿一批批材料，更重要的是，機器裡沒空間時它就不會送下一批。
這和阻擋模式可以正確配合：供應器監看的是機器裡的欄位有沒有材料，而不是介面裡的欄位。

舉例來說，下面這套設施會把待熔煉的物品與燃料，分別直接推進熔爐對應的欄位。
你可以用這招對同一台機器的多個面、或多台機器供料。

<GameScene zoom="6" background="transparent">
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

這是對多台機器供料的通用示意

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        介面（必須是薄板，不能是整格方塊）
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        儲存匯流排
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        你想用樣板供料的目標
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

同一份樣板可以放在多個樣板供應器上，系統支援並會平行處理。

樣板供應器會盡量以輪詢的方式把批次分送到它的各個面，讓所有相接的機器都能平行運作。

## 變體

樣板供應器有三種變體：一般、定向與薄板／[線纜附件](../ae2-mechanics/cable-subparts.md)。
差別在於它從哪些面推出材料、從哪些面接收物品，以及對哪些面提供網路連線。

* 一般樣板供應器對所有面推出材料、從所有面接收物品，而且和多數 AE2 機器一樣，
    像線纜那樣對所有面提供[網路連線](../ae2-mechanics/me-network-connections.md)。

* 定向樣板供應器是拿 <ItemLink id="certus_quartz_wrench" /> 對一般樣板供應器點擊改變方向做出來的。
    它只對選定的那一面推出材料，仍從所有面接收物品，而且刻意不對選定的那一面提供
  [網路連線](../ae2-mechanics/me-network-connections.md)。這樣它就能在不把網路連起來的前提下推料給 AE2 機器，方便你做子網路。

* 薄板樣板供應器是[線纜附件](../ae2-mechanics/cable-subparts.md)，所以同一條線纜上可以放好幾個，適合緊湊配置。
    它的行為和定向樣板供應器選定的那一面類似：提供樣板、接收物品，而且**不**在自己那一面提供
    [網路連線](../ae2-mechanics/me-network-connections.md)。

一般與薄板兩種形態可以在合成格裡互換。

## 設定

樣板供應器有幾種模式：

*   **阻擋模式**會在機器裡還有材料時，不讓供應器推出新的一批。
*   **合成鎖定**可以依各種紅石條件鎖住供應器，或是鎖到上一次合成的成品被送回該供應器為止。
*   供應器可以設定要不要顯示在 <ItemLink id="pattern_access_terminal" /> 上。

## 優先權

在介面右上角點一下扳手就能設定優先權。同一個物品有多份[樣板](patterns.md)時，
優先權較高的供應器上的樣板會優先被使用，除非網路湊不齊該樣板所需的材料。

## 一個常見的誤解

不知為何一直有人這樣做，我不太懂原因，但還是寫在這裡希望有幫助。
（也許是有人誤以為 <ItemLink id="export_bus" /> 是唯一能把東西送出網路的手段，
不知道樣板供應器本身也會輸出東西）

這樣做不會有你想要的效果。如同[線纜](cables.md)那一頁所說，線纜不是物品管線，
它們沒有內部倉庫，供應器不會往裡面推東西。

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_1.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        這不是高爐
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

由於供應器沒有任何東西可推，它根本無法運作。它在這裡唯一做的事，
就是像一條線纜那樣把 <ItemLink id="export_bus" /> 接上網路。

供應器也不會用某種方式告訴 <ItemLink id="export_bus" /> 該輸出什麼，
輸出匯流排只會照它自己篩選裡設定的東西輸出。

我們在這裡實際上做的事，等於是這樣：

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_2.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        這不是高爐
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

你真正想做的大概是這樣，讓樣板供應器把樣板裡的材料輸出給相鄰的機器：

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_3.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        這不是高爐
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

## 搭配分子組裝機使用

<ItemLink id="molecular_assembler" /> 說穿了就和其他機器一樣：它有一個可以塞東西進去的倉庫，
接著對倉庫裡的東西執行某個動作，然後像許多機器那樣把成品推給相鄰的容器。
所以它和供應器的搭配方式，本來就和其他機器一樣，只是多了一項：

組裝機可以直接從插進它身上的 <ItemLink id="crafting_pattern" />、<ItemLink id="smithing_table_pattern" />
或 <ItemLink id="stonecutting_pattern" /> 取得要做的樣板。
這在產線上很好用，但要是每個合成配方都得配一台專用組裝機，那就很煩了。

因此樣板供應器對組裝機有一項特殊功能：它可以把樣板資料連同材料一起送過去。
這樣你只要在樣板供應器旁邊放一台組裝機，供應器就能用那台組裝機處理它所有的合成、鍛造與切石樣板。

真的就這麼簡單，把樣板放進供應器就好：

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

*注意這裡剛好是 8 個供應器，那正是單一台組裝機、供應器或非緻密線纜所能通過的頻道數上限。*

## 配方

<RecipeFor id="pattern_provider" />

<RecipeFor id="cable_pattern_provider" />
