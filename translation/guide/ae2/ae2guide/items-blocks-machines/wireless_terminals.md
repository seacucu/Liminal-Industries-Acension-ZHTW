---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 無線終端機
  icon: wireless_crafting_terminal
  position: 410
categories:
- tools
item_ids:
- ae2:wireless_terminal
- ae2:wireless_crafting_terminal
---

# 無線終端機

<Row>
  <ItemImage id="wireless_terminal" scale="4" />

  <ItemImage id="wireless_crafting_terminal" scale="4" />
</Row>

無線終端機是有線[終端機](terminals.md)的可攜版本。介面和有線版本完全相同，
差別只在於原本放 <ItemLink id="view_cell" /> 的欄位，換成了放[升級卡](upgrade_cards.md)的欄位。

要把它和某個網路配對，就把終端機插進該網路上 <ItemLink id="wireless_access_point" /> 右上角的欄位
（就是畫著無線終端機圖案、下方有個箭頭的那一格）。

它們必須在 <ItemLink id="wireless_access_point" /> 的範圍內才能運作。

它們的電力可以在 <ItemLink id="charger" /> 裡補充。

# 無線終端機

<ItemImage id="wireless_terminal" scale="4" />

你的基本款終端機，現在可以帶著走了！只要在 <ItemLink id="wireless_access_point" /> 的範圍內，
不管人在哪裡都能檢視與存取[網路倉儲](../ae2-mechanics/import-export-storage.md)的內容，
並向你的[自動合成](../ae2-mechanics/autocrafting.md)設施下訂單。

## 介面

見[終端機](terminals.md)

## 升級

無線終端機支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="energy_card" /> 用來提高電池容量

## 配方

<RecipeFor id="wireless_terminal" />

# 無線合成終端機

<ItemImage id="wireless_crafting_terminal" scale="4" />

無線合成終端機和一般的無線終端機類似，設定與分區完全相同，
但多了一個合成格，而且合成格會自動從[網路倉儲](../ae2-mechanics/import-export-storage.md)補料。
按住 Shift 點成品時要小心！

## 介面

見[終端機](terminals.md)

## 升級

無線合成終端機支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="energy_card" /> 用來提高電池容量

## 配方

<RecipeFor id="wireless_crafting_terminal" />
