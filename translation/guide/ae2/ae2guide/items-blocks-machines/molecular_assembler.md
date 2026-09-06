---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 分子組裝機
  icon: molecular_assembler
  position: 310
categories:
- machines
item_ids:
- ae2:molecular_assembler
---

# 分子組裝機

<BlockImage id="molecular_assembler" scale="8" />

分子組裝機會把送進來的物品，依照相鄰 <ItemLink id="pattern_provider" /> 所指定的作業，
或是依照插在它身上的 <ItemLink id="crafting_pattern" />、<ItemLink id="smithing_table_pattern" />、<ItemLink id="stonecutting_pattern" /> 來加工，
再把成品推給相鄰容器。

下圖這台組裝機裝了一份「1 個橡木原木 = 4 個橡木木材」的合成樣板。橡木原木從上方漏斗送進來時，
組裝機就會合成並把橡木木材吐進下方漏斗。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 分子組裝機的主要用法

不過它主要的用法還是貼在 <ItemLink id="pattern_provider" /> 旁邊。這種情況下樣板供應器有特殊行為：
它會把對應樣板的資訊連同材料一起送給相鄰的組裝機。由於組裝機會自動把成品彈到相鄰容器
（也就是送進樣板供應器的回收格），所以樣板供應器上貼一台組裝機，就足以把合成樣板自動化。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 升級

分子組裝機支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="speed_card" />

## 配方

<RecipeFor id="molecular_assembler" />

## 注意

Optifine 會弄壞「推給相鄰容器」這項功能，所以大多數用到組裝機的合成設施都會失效。
