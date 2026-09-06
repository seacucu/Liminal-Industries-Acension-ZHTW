---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 壓印機
  icon: inscriber
  position: 310
categories:
- machines
item_ids:
- ae2:inscriber
---

# 壓印機

<BlockImage id="inscriber" scale="8" />

壓印機用[壓印模具](presses.md)來壓製電路與[處理器](processors.md)，也能把各種物品壓成粉。
AE2 自己的電力（AE）與 Fabric/Forge Energy（E/FE）它都收。它可以設為分面模式，
讓不同面送入的物品進到不同的欄位；為了配合這一點，它可以用 <ItemLink id="certus_quartz_wrench" /> 旋轉。
它也可以設定成把成品推給相鄰容器。

輸入緩衝的大小可以調整。舉例來說，如果你要從一個容器餵料給一大排壓印機，
就該把緩衝調小，材料才會比較平均地分配到各台機器（而不是第一台先囤滿 64 個、其餘全空）。

四種電路模具用來製作[處理器](processors.md)

<Row>
  <ItemImage id="silicon_press" scale="4" />

  <ItemImage id="logic_processor_press" scale="4" />

  <ItemImage id="calculation_processor_press" scale="4" />

  <ItemImage id="engineering_processor_press" scale="4" />
</Row>

命名模具則可以像鐵砧那樣替方塊命名，在 <ItemLink id="pattern_access_terminal" /> 裡標記東西時很好用。

<ItemImage id="name_press" scale="4" />

## 設定

* 壓印機可以設為分面模式（說明如下），也可以設為任何面都能送進任何欄位，由內部篩選決定什麼進哪一格。
    非分面模式下，上下兩格的物品無法被取出。
* 壓印機可以設定成把物品推進相鄰容器。
* 輸入緩衝的大小可以調整：大緩衝適合手動餵料的單台壓印機，
小緩衝則是為了讓大規模平行化的設施更可行。

## 介面與分面

在分面模式下，壓印機依照你從哪一面送入或取出，來決定東西進哪一格。

![Inscriber GUI](../assets/diagrams/inscriber_gui.png) ![Inscriber Sides](../assets/diagrams/inscriber_sides.png)

A. **上方輸入格** 從壓印機的頂面存取（這一格既可推入也可拉出）

B. **中央輸入格** 從壓印機的左、右、前、後面送入（這一格只能推入，不能拉出）

C. **下方輸入格** 從壓印機的底面存取（這一格既可推入也可拉出）

D. **產出格** 從壓印機的左、右、前、後面取出（這一格只能拉出，不能推入）

## 簡易自動化

舉例來說，分面與可旋轉這兩項特性讓你能像這樣把壓印機半自動化：

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/inscriber_hopper_automation.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

或者乾脆切到非分面模式，直接用管線進出。

## 升級

壓印機支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="speed_card" />

## 配方

<RecipeFor id="inscriber" />
