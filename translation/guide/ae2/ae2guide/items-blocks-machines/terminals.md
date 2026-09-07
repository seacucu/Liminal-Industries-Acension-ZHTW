---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 終端機
  icon: crafting_terminal
  position: 210
categories:
- devices
item_ids:
- ae2:terminal
- ae2:crafting_terminal
- ae2:pattern_encoding_terminal
- ae2:pattern_access_terminal
---

# 終端機

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/terminals.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="pattern_provider" />、<ItemLink id="import_bus" />、<ItemLink id="storage_bus" /> 這些
是 AE2 網路與世界互動的主要手段；而終端機，則是 AE2 網路與*你*互動的主要手段。
它有好幾種變體，功能各不相同。

終端機會繼承它所安裝的那條[線纜](cables.md)的顏色。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

## 終端機的擺放

終端機往往是新手放下的第一個[線纜附件](../ae2-mechanics/cable-subparts.md)，
所以很常放錯方向、把它裝反。以下是該怎麼做與不該怎麼做的例子：

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/terminal_placement.snbt" />
  <IsometricCamera yaw="195" pitch="30" />

  <LineAnnotation color="#ff3333" from="2.5 .5 .5" to="4.5 2.5 .5" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="2.5 2.5 .5" to="4.5 .5 .5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="-.5 2.5 .5" to="1 .5 .5" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1 .5 .5" to="1.5 1 .5" alwaysOnTop={true} thickness="0.05"/>
</GameScene>

你一樣有一台終端機和一個能量接收器，只是現在終端機方向正確、真的接上了網路，而且整體還更省空間。

# 終端機搜尋

搜尋框吃正規表示式，所以你可以輸入例如 "gtceu:.*ore" 把 Gregtech 的所有礦石都撈出來。
至於正規表示式怎麼學，留給讀者當作習題。

<a name="terminal-ui"></a>

# 終端機

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

基本款終端機，讓你檢視與存取[網路倉儲](../ae2-mechanics/import-export-storage.md)的內容，
並向你的[自動合成](../ae2-mechanics/autocrafting.md)設施下訂單。

## 介面

基本款終端機的介面分成幾個區塊

中央區塊是存取網路倉儲的地方，東西可以放進去也可以拿出來。有幾組滑鼠與按鍵快捷操作：

*   左鍵抓一整組，右鍵抓半組。
*   如果某個物品、流體之類可以[自動合成](../ae2-mechanics/autocrafting.md)，
    按下你綁定為「選取方塊」的鍵（通常是滑鼠中鍵）就會開啟一個介面，讓你指定要合成的數量。
    你也可以輸入 `3*64/2` 這類算式，或是打 `=32` 表示只補到庫存湊滿 32 個為止。
*   按住 Shift 會把顯示的物品凍結在原位，數量變動或有新物品進入系統時就不會重新排列。
*   拿著水桶或其他流體容器右鍵可以把流體存進去；拿著空的流體容器左鍵點擊終端機裡的流體，則可以把它取出來。

左側區塊有幾個設定按鈕：

*   依名稱、模組、數量等不同屬性排序
*   檢視已儲存、可合成，或兩者
*   檢視物品、流體，或兩者
*   變更排列順序
*   開啟詳細的終端機設定視窗
*   調整終端機介面的高度

右側則是 <ItemLink id="view_cell" /> 的欄位

中央區塊右上角的錘子按鈕會開啟[自動合成](../ae2-mechanics/autocrafting.md)狀態介面，
讓你查看各項自動合成的進度，以及每座[合成 CPU](crafting_cpu_multiblock.md) 正在做什麼。

## 配方

<RecipeFor id="terminal" />

<a name="crafting-terminal-ui"></a>

# 合成終端機

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/crafting_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

合成終端機和一般終端機類似，設定與分區完全相同，
但多了一個合成格，而且合成格會自動從[網路倉儲](../ae2-mechanics/import-export-storage.md)補料。
按住 Shift 點成品時要小心！

你應該盡早把終端機升級成合成終端機。

## 介面

合成終端機的介面和一般終端機相同，只是中間多了一個合成格。

另外多出兩個按鈕，分別把合成格裡的東西清進網路倉儲或你的物品欄。

## 配方

<RecipeFor id="crafting_terminal" />

<a name="pattern-encoding-terminal-ui"></a>

# 樣板編碼終端機

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/pattern_encoding_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

樣板編碼終端機和一般終端機類似，設定與分區完全相同，但多了一個[樣板](patterns.md)編碼介面。
它看起來很像合成終端機的介面，但這個合成格並不會真的合成東西。

除了合成終端機之外，你也該有一台這個。

## 介面

樣板編碼終端機的介面和一般終端機相同，另加上[樣板](patterns.md)編碼介面。

樣板編碼介面分成幾個部分：

一個放 <ItemLink id="blank_pattern" /> 的欄位。

一個大箭頭，用來編碼樣板。

一個放已編碼樣板的欄位。把已經編碼過的樣板放進這一格就能編輯它，改完再點「編碼」箭頭。

右側有 4 個分頁，用來切換要編碼的樣板類型

*   合成
*   處理
*   鍛造
*   切石

中央介面會依要編碼的樣板類型而改變：

*   合成模式下：
    *   左鍵放入材料、或從 JEI／REI 拖進來以組成配方。右鍵可以移除材料。
    *   啟用替代材料後，就能做到「任何木材都能做棍子」這類事。除非真的必要，否則不建議開啟。
    *   流體替代則允許用已儲存的流體取代裝著流體的桶子。
    *   你也可以直接從 JEI／REI 的配方畫面把樣板編碼出來。

*   處理模式下：
    * 左鍵或右鍵放入、或從 JEI／REI 拖進來，以指定配方的輸入與輸出。
    * 拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。
    * 手上拿著一整組時，左鍵一次放入整組，右鍵放入一個。對已放入的材料左鍵可整組移除，右鍵則減少一個。
        按下你綁定為「選取方塊」的鍵（通常是滑鼠中鍵）可以精確指定該物品或流體的數量。
    * 產出欄位分成一個主產物，以及若干副產物的空間，讓自動合成演算法知道還會產出哪些東西。
    * 輸入與輸出欄位都可以捲動，所以你最多能放 81 種不同材料與 26 種副產物。
    * 你也可以直接從 JEI／REI 的配方畫面把樣板編碼出來。

*   鍛造與切石模式的介面，分別和鍛造台與切石機的用法相似。

## 配方

<RecipeFor id="pattern_encoding_terminal" />

<a name="pattern-access-terminal-ui"></a>

# 樣板存取終端機

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/pattern_access_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

樣板存取終端機是為了解決一個特定問題：當 <ItemLink id="pattern_provider" /> 與
<ItemLink id="molecular_assembler" /> 密密麻麻堆成一座塔時，你根本碰不到那些供應器去放新樣板。
再說，也許你就是懶，不想為了放一份[樣板](patterns.md)橫跨整個基地走一趟。
樣板存取終端機讓你能存取網路上所有的樣板供應器。

## 介面

這台終端機的介面和其他終端機都不一樣。

它有終端機高度與「要顯示哪些樣板供應器」的設定。

終端機裡的每一列對應一台特定的樣板供應器。

終端機中的樣板供應器，會依照它們連接的方塊、或你替它們取的名字排序
（用鐵砧或 <ItemLink id="name_press" /> 命名）。

## 配方

<RecipeFor id="pattern_access_terminal" />
