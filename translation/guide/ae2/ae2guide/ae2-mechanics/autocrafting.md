---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 自動合成
  icon: pattern_provider
---

# 自動合成

### 重頭戲

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/autocraft_setup_greebles.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

自動合成是 AE2 的核心功能之一。你不必再像個*苦力*一樣，親手把每一種前置材料按正確數量一個個做出來，
而是直接叫 ME 系統代勞。也可以自動合成物品再輸出到某處，
或是靠巧妙的機制設計讓特定物品維持一定庫存。它同樣支援流體，
如果你裝了提供其他材料型別的附屬模組（例如 Mekanism 的氣體），那些材料也一樣適用。相當好用。

這個主題相當複雜，坐穩了，我們開始。

一套自動合成設施由三個部分構成：
- 發出合成請求的東西
- 合成 CPU
- <ItemLink id="pattern_provider" />。

整個流程是這樣：

1.  某個東西產生了一筆合成請求。可能是你在終端機裡點了某個可自動合成的物品，
    也可能是裝了合成卡的輸出匯流排或介面，要求生產它所設定要輸出或備料的物品。

*   （**重要：**想替已經有庫存的東西下合成請求時，要用你綁定為「選取方塊」的那個鍵（通常是滑鼠中鍵），這可能會和物品欄整理類模組衝突）

2.  ME 系統算出滿足這筆請求所需的材料與前置合成步驟，並把它們存進選定的合成 CPU。

3.  持有對應[樣板](../items-blocks-machines/patterns.md)的 <ItemLink id="pattern_provider" /> 把樣板中指定的材料推給相鄰的容器。
    如果是工作台配方（也就是「合成樣板」），對象會是 <ItemLink id="molecular_assembler" />。
    如果是非工作台配方（也就是「處理樣板」），對象則是其他方塊、機器，或某套精心設計的紅石控制設施。

4.  合成結果得用某種方式送回系統，可以透過輸入匯流排、介面，或是把結果推回樣板供應器。
    **注意，必須觸發一次「物品進入系統」的事件，不能只是把結果用管線送進一個貼著 <ItemLink id="storage_bus" /> 的儲物箱。**

5.  如果這次合成是同一筆請求中另一項合成的前置步驟，產物會存在該合成 CPU 裡，接著用於下一步。

# 樣板

<ItemImage id="crafting_pattern" scale="4" />

樣板是在 <ItemLink id="pattern_encoding_terminal" /> 裡用空白樣板做出來的。

樣板依用途分成好幾種：

*   <ItemLink id="crafting_pattern" /> 編碼的是工作台配方。它可以直接放進 <ItemLink id="molecular_assembler" />，
    讓組裝機一收到材料就做出成品；不過它主要的用法，是放在緊鄰分子組裝機的 <ItemLink id="pattern_provider" /> 裡。
    這種情況下樣板供應器有特殊行為：它會把對應的樣板連同材料一起送給相鄰的組裝機。
    由於組裝機會自動把成品彈到相鄰容器，所以樣板供應器上貼一台組裝機，就足以把合成樣板自動化。

***

*   <ItemLink id="smithing_table_pattern" /> 和合成樣板非常相似，只是它編碼的是鍛造台配方。
    它同樣由樣板供應器加分子組裝機自動化，運作方式完全相同。
    事實上，合成、鍛造與切石三種樣板可以用在同一套設施上。

***

*   <ItemLink id="stonecutting_pattern" /> 和合成樣板非常相似，只是它編碼的是切石機配方。
    它同樣由樣板供應器加分子組裝機自動化，運作方式完全相同。
    事實上，合成、鍛造與切石三種樣板可以用在同一套設施上。

***

*   <ItemLink id="processing_pattern" /> 是自動合成彈性的主要來源。它是最泛用的一種，
    講的無非是「如果樣板供應器把這些材料推給相鄰容器，ME 系統遲早會收到這些物品」。
    你要用任何模組的機器、或熔爐之類的東西做自動合成，靠的都是它。正因為它極為泛用，
    也完全不管推出材料到收到成品之間發生了什麼，你可以玩得很花：
    把材料丟進一整條複雜的工廠產線，讓它自己分類、從無限產出的農場取用其他材料、
    順便把整部《蜂電影》的劇本印出來都行，ME 系統一概不管，只要最後收到樣板上指定的成品就好。
    事實上，它甚至不管材料和成品有沒有任何關聯。你大可告訴它「1 個櫻花木材 = 1 顆地獄之星」，
    然後讓你的凋零農場在收到櫻花木材時宰一隻凋零，這樣也能跑。

同一份樣板可以放在多個 <ItemLink id="pattern_provider" /> 上，系統支援並會平行處理。
此外，樣板也可以寫成例如 8 個鵝卵石 = 8 個石頭，而不是 1 個鵝卵石 = 1 個石頭，
這樣樣板供應器每次作業就會一口氣送 8 個鵝卵石進你的熔煉設施，而不是一個一個來。

## 最泛用的那種「樣板」

其實還有比處理樣板更「泛用」的「樣板」。裝了合成卡的 <ItemLink id="level_emitter" /> 可以設定成
「為了合成某物而發出紅石訊號」。這種「樣板」完全不定義、甚至不在乎材料是什麼，
它講的只是「只要這個位準發射器發出紅石訊號，ME 系統遲早會收到這個物品」。
這通常用來啟停那些不需要投入材料的無限農場，
或是啟動一套處理遞迴配方的系統（標準的自動合成理解不了那種配方），例如你有一台能複製鵝卵石的機器時的「1 個鵝卵石 = 2 個鵝卵石」。

# 合成 CPU

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

合成 CPU 負責管理合成請求與作業。多步驟的合成作業進行時，中間產物由它暫存；
它同時決定了作業規模的上限，以及某種程度上的完成速度。它是多方塊結構，
必須排成長方體，且至少要有一個合成儲存器。

合成 CPU 由這些方塊組成：

*   （必要）[合成儲存器](../items-blocks-machines/crafting_cpu_multiblock.md)，容量分級與一般單元相同（1k、4k、16k、64k、256k）。
    它存放合成過程中的材料與中間產物，所以作業牽涉的材料愈多，CPU 就需要愈大或愈多的儲存器。
*   （選用）<ItemLink id="crafting_accelerator" />，讓系統從樣板供應器一次送出更多批材料。
    舉例來說，一個被 6 台分子組裝機包圍的樣板供應器，就能同時餵滿（也就是同時用到）全部 6 台，而不是一次只用一台。
*   （選用）<ItemLink id="crafting_monitor" />，顯示該 CPU 目前正在處理的作業。可以用 <ItemLink id="color_applicator" /> 染色。
*   （選用）<ItemLink id="crafting_unit" />，單純用來填滿空間，好讓 CPU 湊成長方體。

每個合成 CPU 一次只處理一筆請求或作業，所以如果你想同時要一片計算處理器和 256 個平滑石頭，就得有兩座 CPU 多方塊結構。

CPU 可以設定成只接受玩家的請求、只接受自動化（輸出匯流排與介面）的請求，或兩者皆可。

# 樣板供應器

<Row>
<BlockImage id="pattern_provider" scale="4" />

<BlockImage id="pattern_provider" p:push_direction="up" scale="4" />

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/blocks/cable_pattern_provider.snbt" />
</GameScene>
</Row>

<ItemLink id="pattern_provider" /> 是自動合成系統與外界互動的主要管道。它把[樣板](../items-blocks-machines/patterns.md)中的材料推給相鄰容器，
別的東西也能塞進它以送入網路。把機器的產出用管線送回附近的樣板供應器（通常就是推出材料的那一個），
往往能省下一條頻道，比用 <ItemLink id="import_bus" /> 把機器產出拉進網路更省。

要注意的是，它是直接從合成 CPU 的[合成儲存器](../items-blocks-machines/crafting_cpu_multiblock.md#crafting-storage)推出材料的，
自己的倉庫裡從來不會真的有那些材料，所以你沒辦法從它身上抽料。
你得讓供應器先推給另一個容器（例如木桶），再從那裡抽。

另外要注意，供應器必須一次把所有材料推出去，沒辦法只推半批。這一點很值得善加利用。

樣板供應器和[子網路](../ae2-mechanics/subnetworks.md)上的介面有個特殊互動：如果那個介面沒有做任何設定（請求格是空的），
供應器會直接跳過介面，把材料推進該子網路的[倉儲](../ae2-mechanics/import-export-storage.md)，
不但不會把介面塞滿一批批材料，更重要的是，倉儲沒空間時它就不會送下一批。

同一份樣板可以放在多個樣板供應器上，系統支援並會平行處理。

樣板供應器會盡量以輪詢的方式把批次分送到它的各個面，讓所有相接的機器都能平行運作。

## 變體

樣板供應器有三種變體：一般、定向與薄板。差別在於它從哪些面推出材料、從哪些面接收物品，以及對哪些面提供網路連線。

*   一般樣板供應器對所有面推出材料、從所有面接收物品，而且和多數 AE2 機器一樣，像線纜那樣對所有面提供網路連線。

*   定向樣板供應器是拿 <ItemLink id="certus_quartz_wrench" /> 對一般樣板供應器點擊改變方向做出來的。
    它只對選定的那一面推出材料，仍從所有面接收物品，而且刻意不對選定的那一面提供網路連線。
    這樣它就能在不把網路連起來的前提下推料給 AE2 機器，方便你做子網路。

*   薄板樣板供應器是一種[線纜附件](../ae2-mechanics/cable-subparts.md)，所以同一條線纜上可以放好幾個，適合緊湊配置。
    它的行為和定向樣板供應器選定的那一面類似：提供樣板、接收物品，且不在自己那一面提供網路連線。

一般與薄板兩種形態可以在合成格裡互換。

## 設定

樣板供應器有幾種模式：

*   **阻擋模式**會在機器裡還有材料時，不讓供應器推出新的一批。
*   **合成鎖定**可以依各種紅石條件鎖住供應器，或是鎖到上一次合成的成品被送回該供應器為止。
*   供應器可以設定要不要顯示在 <ItemLink id="pattern_access_terminal" /> 上。

## 優先權

在介面右上角點一下扳手就能設定優先權。同一個物品有多份[樣板](../items-blocks-machines/patterns.md)時，
優先權較高的供應器上的樣板會優先被使用，除非網路湊不齊該樣板所需的材料。

# 分子組裝機

<BlockImage id="molecular_assembler" scale="4" />

<ItemLink id="molecular_assembler" /> 會把送進來的物品，依照相鄰 <ItemLink id="pattern_provider" /> 所指定的作業，
或是依照插在它身上的 <ItemLink id="crafting_pattern" />、<ItemLink id="smithing_table_pattern" />、<ItemLink id="stonecutting_pattern" /> 來加工，
再把成品推給相鄰容器。

它主要的用法是貼在 <ItemLink id="pattern_provider" /> 旁邊。這種情況下樣板供應器有特殊行為：
它會把對應樣板的資訊連同材料一起送給相鄰的組裝機。由於組裝機會自動把成品彈到相鄰容器
（也就是送進樣板供應器的回收格），所以樣板供應器上貼一台組裝機，就足以把合成樣板自動化。

<GameScene zoom="4" background="transparent">
<ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>
