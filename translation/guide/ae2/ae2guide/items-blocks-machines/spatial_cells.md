---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 空間單元
  icon: spatial_storage_cell_128
  position: 410
categories:
- tools
item_ids:
- ae2:spatial_storage_cell_2
- ae2:spatial_storage_cell_16
- ae2:spatial_storage_cell_128
- ae2:spatial_cell_component_2
- ae2:spatial_cell_component_16
- ae2:spatial_cell_component_128
---

# 空間儲存單元

  <Row>
    <ItemImage id="spatial_storage_cell_2" scale="4" />

    <ItemImage id="spatial_storage_cell_16" scale="4" />

    <ItemImage id="spatial_storage_cell_128" scale="4" />
  </Row>

空間儲存單元用來[存放實體的空間範圍](../ae2-mechanics/spatial-io.md)。
它們要搭配 <ItemLink id="spatial_io_port" /> 使用。

和[儲存單元](../items-blocks-machines/storage_cells.md)不同，空間單元無法重新格式化。

再說一次，**空間單元用過之後，無法重設、重新格式化，也無法改變尺寸。** 想換尺寸就做一個新的單元。


## 配方

  <Row>
    <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_16_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_128_cubed_storage" />
  </Row>

# 外殼

單元可以用一個空間元件加一個外殼做成，也可以用外殼的配方把空間元件圍起來：

<Row>
  <Recipe id="network/cells/spatial_storage_cell_2_cubed" />

  <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />
</Row>

外殼本身的合成方式如下：

  <RecipeFor id="item_cell_housing" />

# 空間元件

空間元件是空間儲存單元的核心。每提升一級，可存放的空間範圍邊長就增加為 8 倍。

  <Row>
    <RecipeFor id="spatial_cell_component_2" />

    <RecipeFor id="spatial_cell_component_16" />

    <RecipeFor id="spatial_cell_component_128" />
  </Row>
