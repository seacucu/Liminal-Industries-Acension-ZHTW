---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 能量電池
  icon: energy_cell
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_cell
- ae2:dense_energy_cell
- ae2:creative_energy_cell
---

# 能量電池

<Row gap="20">
  <BlockImage id="energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="8" />
</Row>

能量電池替網路增加[能量](../ae2-mechanics/energy.md)儲存。有一定的電力緩衝，
就能在大量物品進出時把耗電尖峰壓平；儲電量更大的話，
還能讓網路在沒有發電時（例如太陽能板在夜間）繼續運轉，
或是應付[空間儲存](../ae2-mechanics/spatial-io.md)那種瞬間的巨額耗電。

## 電量條

<Row>
<BlockImage id="energy_cell" scale="4" p:fullness="0" />
<BlockImage id="energy_cell" scale="4" p:fullness="1" />
<BlockImage id="energy_cell" scale="4" p:fullness="2" />
<BlockImage id="energy_cell" scale="4" p:fullness="3" />
<BlockImage id="energy_cell" scale="4" p:fullness="4" />
</Row>

電池側面的條紋對應它目前的電量。

*   低於 25% 時 0 條
*   25% 到 50% 之間 1 條
*   50% 到 75% 之間 2 條
*   75% 到 99% 之間 3 條
*   高於 99% 時 4 條

## 電池種類

*   <ItemLink id="energy_cell" /> 可儲存 200k AE，大多數情況下一顆就夠了，網路日常運作的耗電尖峰它輕鬆應付得來。
*   <ItemLink id="dense_energy_cell" /> 可儲存 1.6M AE，適合用在想靠儲備電力跑網路，
    或是要應付大型[空間儲存](../ae2-mechanics/spatial-io.md)設施那種瞬間巨額耗電的場合。
*   <ItemLink id="creative_energy_cell" /> 是測試用的創造模式物品，提供無限的電力之類的。

## 配方

<Row>
  <RecipeFor id="energy_cell" />

  <RecipeFor id="dense_energy_cell" />
</Row>
