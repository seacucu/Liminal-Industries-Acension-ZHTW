---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 處理器
  icon: logic_processor
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:logic_processor
- ae2:calculation_processor
- ae2:engineering_processor
- ae2:printed_silicon
- ae2:printed_logic_processor
- ae2:printed_calculation_processor
- ae2:printed_engineering_processor
- ae2:silicon
---

# 處理器

<Row>
  <ItemImage id="logic_processor" scale="4" />

  <ItemImage id="calculation_processor" scale="4" />

  <ItemImage id="engineering_processor" scale="4" />
</Row>

處理器是 AE2 [裝置](../ae2-mechanics/devices.md)與機器最主要的材料之一，
也是你會遇到的第一個大型自動化挑戰。處理器有三種，分別用金、<ItemLink id="certus_quartz_crystal" />
與鑽石製作。作法是在 <ItemLink id="inscriber" /> 上使用[壓印模具](presses.md)，經過多道工序完成
（通常是靠一連串壓印機加上有篩選的管線來達成）。

## 生產步驟

<Column gap="5">
  1.  備齊所需材料：矽、紅石、金、<ItemLink id="certus_quartz_crystal" />、鑽石。

  <RecipeFor id="silicon" />

  <br />

  2.  壓印出前置的印刷電路元件

  <Row>
    <RecipeFor id="printed_silicon" />

    <RecipeFor id="printed_logic_processor" />
  </Row>

  <Row>
    <RecipeFor id="printed_calculation_processor" />

    <RecipeFor id="printed_engineering_processor" />
  </Row>

  <br />

  3.  最終組裝

  <Row>
    <RecipeFor id="logic_processor" />

    <RecipeFor id="calculation_processor" />
  </Row>

  <RecipeFor id="engineering_processor" />
</Column>
