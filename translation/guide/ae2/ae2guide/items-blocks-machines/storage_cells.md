---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 儲存單元
  icon: item_storage_cell_1k
  position: 410
categories:
- tools
item_ids:
- ae2:item_cell_housing
- ae2:fluid_cell_housing
- ae2:cell_component_1k
- ae2:cell_component_4k
- ae2:cell_component_16k
- ae2:cell_component_64k
- ae2:cell_component_256k
- ae2:item_storage_cell_1k
- ae2:item_storage_cell_4k
- ae2:item_storage_cell_16k
- ae2:item_storage_cell_64k
- ae2:item_storage_cell_256k
- ae2:fluid_storage_cell_1k
- ae2:fluid_storage_cell_4k
- ae2:fluid_storage_cell_16k
- ae2:fluid_storage_cell_64k
- ae2:fluid_storage_cell_256k
---

# 儲存單元

<Column>
  <Row>
    <ItemImage id="item_storage_cell_1k" scale="4" />

    <ItemImage id="item_storage_cell_4k" scale="4" />

    <ItemImage id="item_storage_cell_16k" scale="4" />

    <ItemImage id="item_storage_cell_64k" scale="4" />

    <ItemImage id="item_storage_cell_256k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="fluid_storage_cell_1k" scale="4" />

    <ItemImage id="fluid_storage_cell_4k" scale="4" />

    <ItemImage id="fluid_storage_cell_16k" scale="4" />

    <ItemImage id="fluid_storage_cell_64k" scale="4" />

    <ItemImage id="fluid_storage_cell_256k" scale="4" />
  </Row>
</Column>

儲存單元是《應用能源》最主要的儲存手段之一。它們要放進 <ItemLink id="drive" /> 或 <ItemLink id="chest" />。

關於它們在位元組與類型上的容量，說明見[位元組與類型](../ae2-mechanics/bytes-and-types.md)。

單元清空後，手持該單元潛行右鍵，就能把儲存元件從外殼裡取出來。

<Row>
    <Recipe id="upgrade/item_storage_cell_1k_to_4k" />

    把儲存單元和更高階的儲存元件一起放進合成格，就能升級到更高階。裡面的東西會保留，低階的元件則會退還給你。
</Row>

## 類型數不同時的實際容量

[類型的預付成本](../ae2-mechanics/bytes-and-types.md)相當可觀：只用 1 個類型的單元，總容量是用滿 63 個類型時的兩倍。

| 單元                                     | 只用 1 個類型時的總容量 | 用滿 63 個類型時的總容量 |
| ---------------------------------------- | ----------------------------------------: | ------------------------------------------: |
| <ItemLink id="item_storage_cell_1k" />   |                                     8,128 |                                       4,160 |
| <ItemLink id="item_storage_cell_4k" />   |                                    32,512 |                                      16,640 |
| <ItemLink id="item_storage_cell_16k" />  |                                   130,048 |                                      66,560 |
| <ItemLink id="item_storage_cell_64k" />  |                                   520,192 |                                     266,240 |
| <ItemLink id="item_storage_cell_256k" /> |                                 2,080,768 |                                   1,064,960 |


## 分區

單元可以設定成只接受特定物品，作法和 <ItemLink id="storage_bus" /> 的篩選類似，
在 <ItemLink id="cell_workbench" /> 裡設定。

物品可以直接從 JEI／REI 拖進欄位，就算你手上一個都沒有也行。

## 升級

儲存單元支援以下[升級卡](upgrade_cards.md)，透過 <ItemLink id="cell_workbench" /> 裝入：

*   <ItemLink id="fuzzy_card" />（流體單元不支援）讓單元能依損傷程度分區，或忽略物品的 NBT
*   <ItemLink id="inverter_card" /> 把篩選從白名單切換成黑名單
*   <ItemLink id="equal_distribution_card" /> 讓每個類型分到相同的單元位元組空間，避免某一種把整個單元佔滿
*   <ItemLink id="void_card" /> 在單元裝滿時（若裝了平均分配卡，則是該類型的配額用完時）把送進來的物品銷毀，
    可以避免農場塞住。用它記得先設好分區！
*   攜帶式單元還可以裝 <ItemLink id="energy_card" /> 來提高電池容量

## 上色

攜帶式的物品與流體單元可以像皮革盔甲那樣，和染料一起合成來上色。

# 外殼

單元可以用一個儲存元件加一個外殼做成，也可以用外殼的配方把儲存元件圍起來：

<Row>
  <Recipe id="network/cells/item_storage_cell_1k" />

  <Recipe id="network/cells/item_storage_cell_1k_storage" />
</Row>

外殼本身的合成方式如下：

<Row>
  <RecipeFor id="item_cell_housing" />

  <RecipeFor id="fluid_cell_housing" />
</Row>

# 儲存元件

儲存元件是所有 AE2 單元的核心，決定了單元的容量。每提升一級，容量變為 4 倍，成本則是前一級的 3 個。

<Column>
  <Row>
    <RecipeFor id="cell_component_1k" />

    <RecipeFor id="cell_component_4k" />

    <RecipeFor id="cell_component_16k" />
  </Row>

  <Row>
    <RecipeFor id="cell_component_64k" />

    <RecipeFor id="cell_component_256k" />
  </Row>
</Column>

# 物品儲存單元

物品儲存單元最多可容納 63 種不同的物品，各種標準容量都有。

<Column>
  <Row>
    <Recipe id="network/cells/item_storage_cell_1k_storage" />

    <Recipe id="network/cells/item_storage_cell_4k_storage" />

    <Recipe id="network/cells/item_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/item_storage_cell_64k_storage" />

    <Recipe id="network/cells/item_storage_cell_256k_storage" />
  </Row>
</Column>

## 攜帶式物品儲存

它們就像口袋裡的迷你 <ItemLink id="chest" />，或者說是某種背包。可以在 <ItemLink id="charger" /> 裡充電

和一般儲存單元不同的是，它們的位元組容量愈大，能放的類型數反而*愈少*，
而且總位元組容量只有一半。

除了所有單元通用的升級卡之外，它們還接受 <ItemLink id="energy_card" /> 來升級內部電池。

<Column>
  <Row>
    <RecipeFor id="portable_item_cell_1k" />

    <RecipeFor id="portable_item_cell_4k" />

    <RecipeFor id="portable_item_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_item_cell_64k" />

    <RecipeFor id="portable_item_cell_256k" />
  </Row>
</Column>

# 流體儲存單元

流體儲存單元最多可容納 5 種不同的流體，各種標準容量都有。

<Column>
  <Row>
    <Recipe id="network/cells/fluid_storage_cell_1k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_4k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/fluid_storage_cell_64k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_256k_storage" />
  </Row>
</Column>

## 攜帶式流體儲存

它們就像口袋裡的迷你 <ItemLink id="chest" />，或者說是某種背包。可以在 <ItemLink id="charger" /> 裡充電

和一般儲存單元不同的是，它們的位元組容量愈大，能放的類型數反而*愈少*，
而且總位元組容量只有一半。

除了所有單元通用的升級卡之外，它們還接受 <ItemLink id="energy_card" /> 來升級內部電池。

<Column>
  <Row>
    <RecipeFor id="portable_fluid_cell_1k" />

    <RecipeFor id="portable_fluid_cell_4k" />

    <RecipeFor id="portable_fluid_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_fluid_cell_64k" />

    <RecipeFor id="portable_fluid_cell_256k" />
  </Row>
</Column>

# 創造模式儲存單元

<Row>
  <ItemImage id="creative_storage_cell" scale="2" />
</Row>

創造模式單元**並不提供無限儲存空間**。
它們的作用，是成為你替它[分區設定](cell_workbench.md)的那個物品或流體的無限來源與無限去處。
