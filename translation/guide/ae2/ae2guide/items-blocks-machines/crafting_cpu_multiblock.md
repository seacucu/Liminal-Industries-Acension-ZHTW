---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 合成 CPU 多方塊（儲存器、協同處理器、監控器、單元）
  icon: 1k_crafting_storage
  position: 210
categories:
- devices
item_ids:
- ae2:1k_crafting_storage
- ae2:4k_crafting_storage
- ae2:16k_crafting_storage
- ae2:64k_crafting_storage
- ae2:256k_crafting_storage
- ae2:crafting_accelerator
- ae2:crafting_monitor
- ae2:crafting_unit
---

# 合成 CPU

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="crafting_accelerator" scale="4" />

  <BlockImage id="crafting_monitor" scale="4" />

  <BlockImage id="crafting_unit" scale="4" />
</Row>

合成 CPU 負責管理合成請求與作業。多步驟的合成作業進行時，中間產物由它暫存；
它同時決定了作業規模的上限，以及某種程度上的完成速度。
詳見[自動合成](../ae2-mechanics/autocrafting.md)。

每個合成 CPU 一次只處理一筆請求或作業，所以如果你想同時要一片計算處理器和 256 個平滑石頭，就得有兩座 CPU 多方塊結構。

CPU 可以設定成只接受玩家的請求、只接受自動化（輸出匯流排與介面）的請求，或兩者皆可。

右鍵點擊會開啟合成狀態介面，讓你查看該 CPU 正在處理的作業進度。

## 設定

*   CPU 可以設定成只接受玩家的請求、只接受自動化的請求（例如裝了
    <ItemLink id="crafting_card" /> 的 <ItemLink id="export_bus" />），或兩者皆可。

## 搭建方式

合成 CPU 是多方塊結構，必須排成沒有空隙的實心長方體，由數種元件組成。

每座 CPU 至少要有一格合成儲存器（事實上最小可用的 CPU 就是單獨一格 1k 合成儲存器）。

# 合成單元

<BlockImage id="crafting_unit" scale="4" />

（選用）當你其他元件不夠時，合成單元單純用來填滿空間，好讓 CPU 湊成實心長方體。
它同時也是其他元件的基礎材料。

<RecipeFor id="crafting_unit" />

# 合成儲存器

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="4k_crafting_storage" scale="4" />

  <BlockImage id="16k_crafting_storage" scale="4" />

  <BlockImage id="64k_crafting_storage" scale="4" />

  <BlockImage id="256k_crafting_storage" scale="4" />
</Row>

（必要）合成儲存器的容量分級與一般單元相同（1k、4k、16k、64k、256k）。
它存放合成過程中的材料與中間產物，所以作業牽涉的材料愈多，CPU 就需要愈大或愈多的儲存器。

<Column>
  <Row>
    <RecipeFor id="1k_crafting_storage" />

    <RecipeFor id="4k_crafting_storage" />

    <RecipeFor id="16k_crafting_storage" />
  </Row>

  <Row>
    <RecipeFor id="64k_crafting_storage" />

    <RecipeFor id="256k_crafting_storage" />
  </Row>
</Column>

# 協同處理合成單元

<BlockImage id="crafting_accelerator" scale="4" />

（選用）協同處理器讓系統更頻繁地從 <ItemLink id="pattern_provider" /> 送出材料批次，
好跟上那些處理速度很快的機器。舉例來說，一個被 <ItemLink id="molecular_assembler" /> 包圍的樣板供應器，
推料速度可以超過單一台組裝機的處理速度，於是材料批次就會分散給周圍的多台組裝機。

<RecipeFor id="crafting_accelerator" />

# 合成監控器

<BlockImage id="crafting_monitor" scale="4" />

（選用）合成監控器顯示該 CPU 目前正在處理的作業。
螢幕可以用 <ItemLink id="color_applicator" /> 上色。

<RecipeFor id="crafting_monitor" />
