---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 升級卡
  icon: speed_card
  position: 410
categories:
- tools
item_ids:
- ae2:basic_card
- ae2:advanced_card
- ae2:redstone_card
- ae2:capacity_card
- ae2:void_card
- ae2:fuzzy_card
- ae2:speed_card
- ae2:inverter_card
- ae2:crafting_card
- ae2:equal_distribution_card
- ae2:energy_card
---

# 升級卡

<Row>
  <ItemImage id="redstone_card" scale="2" />

  <ItemImage id="capacity_card" scale="2" />

  <ItemImage id="void_card" scale="2" />

  <ItemImage id="fuzzy_card" scale="2" />

  <ItemImage id="speed_card" scale="2" />

  <ItemImage id="inverter_card" scale="2" />

  <ItemImage id="crafting_card" scale="2" />

  <ItemImage id="equal_distribution_card" scale="2" />

  <ItemImage id="energy_card" scale="2" />
</Row>

升級卡會改變 AE2 [裝置](../ae2-mechanics/devices.md)與機器的行為：加快速度、增加篩選欄位、
啟用紅石控制等等。

## 卡片元件

<Row>
  <ItemImage id="basic_card" scale="2" />

  <ItemImage id="advanced_card" scale="2" />
</Row>

各種卡片是用基礎或高級卡片基底做出來的

<Row>
  <RecipeFor id="basic_card" />

  <RecipeFor id="advanced_card" />
</Row>

## 紅石卡

<ItemImage id="redstone_card" scale="2" />

紅石卡加上紅石控制，會在裝置的介面裡多出一個按鈕，用來在各種紅石條件之間切換。

<RecipeFor id="redstone_card" />

## 容量卡

<ItemImage id="capacity_card" scale="2" />

容量卡增加輸入、輸出、儲存匯流排與成形面板的篩選欄位數量。

<RecipeFor id="capacity_card" />

## 溢位銷毀卡

<ItemImage id="void_card" scale="2" />

溢位銷毀卡可以透過 <ItemLink id="cell_workbench" /> 裝進[儲存單元](storage_cells.md)，
在單元裝滿時把送進來的物品刪除。（記得先替單元做好[分區設定](cell_workbench.md)！）
搭配平均分配卡時，只要某個物品在單元中的配額用完，該物品就會被銷毀，就算其他物品的配額還空著也一樣。

<RecipeFor id="void_card" />

## 模糊卡

<ItemImage id="fuzzy_card" scale="2" />

模糊卡讓帶有篩選的裝置與工具能依損傷程度篩選，或忽略物品的 NBT。
這樣你就能不管損傷與附魔、把所有鐵斧一律輸出，或是只輸出有損傷的鑽石劍、放過已修滿的。

下表示範模糊損傷比對的運作方式：左欄是匯流排的設定，最上一列是被比對的物品。

| 25%                    | 損傷 10% 的鎬 | 損傷 30% 的鎬 | 損傷 80% 的鎬 | 完全修復的鎬 |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| 幾乎壞掉的鎬  | ✅                   | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            |
| 完全修復的鎬 | \*\*\*\*            | ✅                   | ✅                   | ✅                   |

| 50%                    | 損傷 10% 的鎬 | 損傷 30% 的鎬 | 損傷 80% 的鎬 | 完全修復的鎬 |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| 幾乎壞掉的鎬  | ✅                   | ✅                   | \*\*\*\*            | \*\*\*\*            |
| 完全修復的鎬 | \*\*\*\*            | \*\*\*\*            | ✅                   | ✅                   |

| 75%                    | 損傷 10% 的鎬 | 損傷 30% 的鎬 | 損傷 80% 的鎬 | 完全修復的鎬 |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| 幾乎壞掉的鎬  | ✅                   | ✅                   | \*\*\*\*            | \*\*\*\*            |
| 完全修復的鎬 | \*\*\*\*            |                     | ✅                   | ✅                   |

| 99%                    | 損傷 10% 的鎬 | 損傷 30% 的鎬 | 損傷 80% 的鎬 | 完全修復的鎬 |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| 幾乎壞掉的鎬  | ✅                   | ✅                   | ✅                   | \*\*\*\*            |
| 完全修復的鎬 | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            | ✅                   |

| 忽略                 | 損傷 10% 的鎬 | 損傷 30% 的鎬 | 損傷 80% 的鎬 | 完全修復的鎬 |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| 幾乎壞掉的鎬  | ✅                   | ✅                   | ✅                   | **✅**               |
| 完全修復的鎬 | **✅**               | **✅**               | **✅**               | ✅                   |

<RecipeFor id="fuzzy_card" />

## 加速卡

<ItemImage id="speed_card" scale="2" />

加速卡讓東西跑得更快：輸入與輸出匯流排每次作業搬更多物品，壓印機與組裝機工作得更快。

<RecipeFor id="speed_card" />

## 反相卡

<ItemImage id="inverter_card" scale="2" />

反相卡把裝置與工具上的篩選從白名單切換成黑名單。

<RecipeFor id="inverter_card" />

## 合成卡

<ItemImage id="crafting_card" scale="2" />

合成卡讓裝置能向你的[自動合成](../ae2-mechanics/autocrafting.md)系統送出合成請求，以取得它要的物品。

<RecipeFor id="crafting_card" />

## 平均分配卡

<ItemImage id="equal_distribution_card" scale="2" />

平均分配卡可以透過 <ItemLink id="cell_workbench" /> 裝進[儲存單元](storage_cells.md)，
依照卡片的[分區設定](cell_workbench.md)把單元切成大小相等的區塊，
避免某一種物品把整個單元佔滿。

<RecipeFor id="equal_distribution_card" />

## 能量卡

<ItemImage id="energy_card" scale="2" />

能量卡替可攜式終端機這類工具增加儲電量，也讓 <ItemLink id="vibration_chamber" /> 更有效率。

<RecipeFor id="energy_card" />
