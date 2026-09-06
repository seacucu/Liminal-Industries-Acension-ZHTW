---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 物質加農砲
  icon: matter_cannon
  position: 410
categories:
- tools
item_ids:
- ae2:matter_cannon
---

# 物質加農砲

<ItemImage id="matter_cannon" scale="4" />

物質加農砲是一把可攜式磁軌砲，能把 <ItemLink id="matter_ball" />、金屬粒之類的小物品當彈丸射出。
傷害取決於射出的物品：金粒這種「較重」的東西（10 點傷害）比物質球這種輕的（2 點傷害）打得痛得多。
每次射擊的基礎耗電為 1600 AE。

當設定項「matterCannonBlockDamage」為 true 時，這把砲會依方塊硬度與彈藥傷害破壞方塊。

它的電力可以在 <ItemLink id="charger" /> 裡補充。

物質加農砲的行為和[儲存單元](storage_cells.md)類似，要替它裝彈，最省事的方式是把它插進
<ItemLink id="chest" /> 的儲存單元欄位。

## 升級

物質加農砲支援以下[升級卡](upgrade_cards.md)，透過 <ItemLink id="cell_workbench" /> 裝入：

*   <ItemLink id="fuzzy_card" /> 讓單元能依損傷程度分區，或忽略物品的 NBT
*   <ItemLink id="inverter_card" /> 把篩選從白名單切換成黑名單
*   <ItemLink id="speed_card" /> 提高每次射擊的耗電，讓威力更強
*   <ItemLink id="void_card" /> 在單元裝滿時把送進來的物品銷毀。用它記得先設好分區！
*   <ItemLink id="energy_card" /> 用來提高電池容量

## 配方

<RecipeFor id="matter_cannon" />
