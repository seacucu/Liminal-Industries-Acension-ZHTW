---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 位準發射器
  icon: level_emitter
  position: 220
categories:
- devices
item_ids:
- ae2:level_emitter
- ae2:energy_level_emitter
---

# 位準發射器

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/level_emitter.snbt" />
</GameScene>

位準發射器依照[網路倉儲](../ae2-mechanics/import-export-storage.md)裡某個物品的數量發出紅石訊號。

另外還有一種版本，是依照你網路中儲存的[能量](../ae2-mechanics/energy.md)發出紅石訊號。

物品與流體都能直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

拿流體容器（例如水桶或流體儲罐）右鍵，設定的會是裡面那種流體，而不是水桶或儲罐這個物品本身。

它們屬於[線纜附件](../ae2-mechanics/cable-subparts.md)。

和其他[裝置](../ae2-mechanics/devices.md)不同，位準發射器*不*需要[頻道](../ae2-mechanics/channels.md)。

## 設定

*   位準發射器可以設為「大於等於」或「小於」兩種模式
*   插入 <ItemLink id="crafting_card" /> 後，可以設為「合成期間發出紅石訊號」或
    「發出紅石訊號以進行合成」

## 升級

位準發射器支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="fuzzy_card" /> 讓發射器能依損傷程度篩選，或忽略物品的 NBT
*   <ItemLink id="crafting_card" /> 啟用合成相關功能

## 合成相關功能

插入 <ItemLink id="crafting_card" /> 後，發射器會切換到合成模式。

這會啟用兩個選項：

第一個選項「合成期間發出紅石訊號」，讓發射器在你的[自動合成](../ae2-mechanics/autocrafting.md)
正透過 <ItemLink id="pattern_provider" /> 生產某個特定物品時發出紅石訊號。
這很適合用來讓某些耗電的自動化設施只在真正要用時才啟動。

第二個選項「發出紅石訊號以進行合成」，在某些特定情境下極為好用，
例如無限農場，或是那些產出帶有機率、無法保證出貨的自動化設施。
這個設定會替發射器篩選欄位裡的物品，生出一份虛擬的[樣板](patterns.md)給[自動合成](../ae2-mechanics/autocrafting.md)使用。
（為了讓它正常運作，你的 <ItemLink id="pattern_provider" /> 裡**不該存在**同一個物品的實體樣板）

這種「樣板」完全不定義、甚至不在乎材料是什麼，
它講的只是「只要這個位準發射器發出紅石訊號，ME 系統遲早會收到這個物品」。
這通常用來啟停那些不需要投入材料的無限農場，
或是啟動[一套處理遞迴配方的系統](../example-setups/recursive-crafting-setup.md)（標準的自動合成理解不了那種配方），
例如你有一台能複製鵝卵石的機器時的「1 個鵝卵石 = 2 個鵝卵石」。

## 配方

<RecipeFor id="level_emitter" />

<RecipeFor id="energy_level_emitter" />
