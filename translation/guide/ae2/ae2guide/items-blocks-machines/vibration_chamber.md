---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 諧振倉
  icon: vibration_chamber
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:vibration_chamber
---

# 諧振倉

<BlockImage id="vibration_chamber" p:active="true" scale="8" />

替網路提供[能量](../ae2-mechanics/energy.md)的主要手段雖然是 <ItemLink id="energy_acceptor" />，
但諧振倉可以直接產生少量到中等的 AE。

在預設狀態下（沒有任何[升級卡](upgrade_cards.md)、設定維持預設），它每刻產生 40 AE。

當網路的[能量](../ae2-mechanics/energy.md)儲存滿了，諧振倉會降速以節省燃料，但沒辦法完全停機。

## 設定

*   諧振倉提供了一個全域設定的入口，可切換能量以 AE 或 E/FE 顯示。

## 升級

諧振倉支援以下[升級卡](upgrade_cards.md)：

*   <ItemLink id="energy_card" /> 讓效率增加 50%，最多疊到 +150%，也就是基礎效率的 250%。
*   <ItemLink id="speed_card" /> 讓燃燒速率增加 50%，最多疊到 +150%，也就是基礎輸出的 250%。

## 設定檔

諧振倉的各項參數可以在你的 .minecraft\ 目錄下 config 資料夾裡的 ae2 資料夾中，
編輯 common.json 來調整。

*   baseEnergyPerFuelTick 設定諧振倉未升級時的基礎效率。
*   minEnergyPerGameTick 設定最低的發電量（就算網路完全不需要能量，諧振倉還是會慢慢燒掉一些燃料）。
*   maxEnergyPerGameTick 設定諧振倉未升級時的最大輸出與速度。

## 配方

<RecipeFor id="vibration_chamber" />
