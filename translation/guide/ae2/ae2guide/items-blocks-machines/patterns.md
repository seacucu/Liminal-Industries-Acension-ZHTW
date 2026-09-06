---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 樣板
  icon: crafting_pattern
  position: 410
categories:
- tools
item_ids:
- ae2:blank_pattern
- ae2:crafting_pattern
- ae2:processing_pattern
- ae2:smithing_table_pattern
- ae2:stonecutting_pattern
---

# 樣板

<ItemImage id="crafting_pattern" scale="4" />

樣板是在 <ItemLink id="pattern_encoding_terminal" /> 裡用空白樣板做出來的，
再放進 <ItemLink id="pattern_provider" /> 或 <ItemLink id="molecular_assembler" />。

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
    事實上，它甚至不管材料和成品有沒有任何關聯。你大可告訴它「1 個櫻花木材 = 1 顆下界之星」，
    然後讓你的凋零農場在收到櫻花木材時宰一隻凋零，這樣也能跑。

同一份樣板可以放在多個 <ItemLink id="pattern_provider" /> 上，系統支援並會平行處理。
此外，樣板也可以寫成例如 8 個鵝卵石 = 8 個石頭，而不是 1 個鵝卵石 = 1 個石頭，
這樣樣板供應器每次作業就會一口氣送 8 個鵝卵石進你的熔煉設施，而不是一個一個來。

## 配方

<RecipeFor id="blank_pattern" />
