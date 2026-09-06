---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 物質聚合器
  icon: condenser
  position: 310
categories:
- machines
item_ids:
- ae2:condenser
---

# 物質聚合器

<BlockImage id="condenser" scale="8" />

物質聚合器可以當垃圾桶用，也可以用來製作 <ItemLink id="matter_ball" /> 與[奇點](singularities.md)。
凡是儲存單元存得下的物品、流體之類，它都收。

## 設定與配方

*   垃圾桶模式下，物質聚合器會把送進來的東西全部銷毀
*   物質球模式下，它會把你丟進去的東西做成 <ItemLink id="matter_ball" />。
    這個模式需要在聚合器頂部的欄位放一個儲存元件。每顆物質球要吃掉 256 個物品或 256 桶流體，
    所以一個 <ItemLink id="cell_component_1k" />（提供 8192 位元的容量）綽綽有餘。
*   奇點模式下，它會把你丟進去的東西做成[奇點](singularities.md)。
    這個模式同樣需要在頂部欄位放一個儲存元件。每顆奇點要吃掉 256,000 個物品或 256,000 桶流體，
    所以一個 <ItemLink id="cell_component_64k" />（提供 524,288 位元的容量）綽綽有餘。

要注意的是，在後兩種會產出資源的模式下，物質聚合器*有可能*塞住：
一旦能量與產物的緩衝都完全填滿，它就不再接受任何輸入。

## 配方

<RecipeFor id="condenser" />
