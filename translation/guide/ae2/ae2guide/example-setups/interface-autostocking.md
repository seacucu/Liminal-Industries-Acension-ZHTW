---
navigation:
  parent: example-setups/example-setups-index.md
  title: 用介面自動備料
  icon: interface
---

# 用介面自動備料

有人會問：「我要怎麼讓各種物品都維持一定的庫存，不夠時自動補產？」

一種作法是用 <ItemLink id="interface" /> 加 <ItemLink id="crafting_card" />，
自動向網路的[自動合成](../ae2-mechanics/autocrafting.md)請求補貨。這套設施比較適合用來維持「種類多、每種數量少」的庫存。

示範用的設施刻意做短一點，免得畫面太寬。實際上最理想的是用 4 個 <ItemLink id="interface" /> 加 4 個 <ItemLink id="storage_bus" />，
剛好把一條一般[線纜](../items-blocks-machines/cables.md)的 8 條[頻道](../ae2-mechanics/channels.md)用滿。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_autostocking.snbt" />

<BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
        (1) 介面：設定成在自己身上備妥想要的物品。裝有合成卡。
        <ItemImage id="crafting_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
        (2) 儲存匯流排：「輸入／輸出模式」設為「僅能取出」。
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="interface" />（1）設定成在自己身上備妥想要的物品：把物品點進它上排的欄位，或從 JEI 拖進去，
   再點欄位上方的扳手圖示設定數量。它們裝有 <ItemLink id="crafting_card" />。
* <ItemLink id="storage_bus" />（2）把「輸入／輸出模式」設為「僅能取出」。

## 運作原理

1. 當 <ItemLink id="interface" /> 沒辦法從[網路倉儲](../ae2-mechanics/import-export-storage.md)取得足夠的設定物品時
   （而且它裝有 <ItemLink id="crafting_card" />），就會請求網路的[自動合成](../ae2-mechanics/autocrafting.md)多做一些。
2. <ItemLink id="storage_bus" /> 讓網路能存取那些介面裡的東西。
