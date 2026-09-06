---
navigation:
  parent: example-setups/example-setups-index.md
  title: 用位準發射器自動備料
  icon: level_emitter
---

# 用位準發射器自動備料

有人會問：「我要怎麼讓某個物品維持一定的庫存，不夠時自動補產？」

一種作法是用 <ItemLink id="export_bus" />、<ItemLink id="level_emitter" /> 與 <ItemLink id="crafting_card" />，
自動向網路的[自動合成](../ae2-mechanics/autocrafting.md)請求補貨。這套設施適合用來維持「單一物品、大量庫存」。

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (1) 輸出匯流排：篩選設為想要的物品。裝有紅石卡與合成卡。紅石模式設為
        「接收到紅石訊號時啟用」，合成方式設為「不使用已有庫存」。
        <Row><ItemImage id="redstone_card" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
        (2) 位準發射器：設定想要的物品與數量，模式設為「低於設定值時發出訊號」。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (3) 介面：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="export_bus" />（1）篩選設為想要的物品，並裝上 <ItemLink id="redstone_card" /> 與 <ItemLink id="crafting_card" />。
  「紅石模式」設為「接收到紅石訊號時啟用」，「合成方式」設為「不使用已有庫存」。
* <ItemLink id="level_emitter" />（2）設定想要的物品與數量，並設為「低於設定值時發出訊號」。
* <ItemLink id="interface" />（3）維持預設設定。

## 運作原理

1. 當[網路倉儲](../ae2-mechanics/import-export-storage.md)裡該物品的數量低於 <ItemLink id="level_emitter" /> 設定的數量時，
   它就會發出紅石訊號。
2. 收到紅石訊號後（加上它裝有 <ItemLink id="crafting_card" />，且設定為不使用已有庫存），
   <ItemLink id="export_bus" /> 就會請求網路的[自動合成](../ae2-mechanics/autocrafting.md)多做一些，再把它輸出。
3. 有物品被推進來時（而它的內部倉庫又沒有設定要放什麼），<ItemLink id="interface" /> 就會把該物品推進網路倉儲。
