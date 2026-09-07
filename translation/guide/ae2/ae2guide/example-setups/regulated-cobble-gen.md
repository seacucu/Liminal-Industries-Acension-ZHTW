---
navigation:
  parent: example-setups/example-setups-index.md
  title: 自動調節的鵝卵石產生器
  icon: minecraft:cobblestone
---

# 自動調節的鵝卵石產生器

把鵝卵石產生器自動化很簡單，拿一片 <ItemLink id="annihilation_plane" /> 對著一座原版的手動鵝卵石產生器就行。
問題是這樣遲早會讓整個網路塞滿鵝卵石，所以還是得加點調節機制。

由於破壞面板的運作方式（它的行為和 <ItemLink id="import_bus" /> 一樣），我們沒辦法直接放一個 <ItemLink id="level_emitter" />
對著裝了 <ItemLink id="redstone_card" /> 的 <ItemLink id="export_bus" />（因為中間沒有倉儲時，不能從輸入直接接到輸出）。
得繞一點路。

<ItemLink id="toggle_bus" /> 可以用紅石訊號接上或斷開網路的一部分，但每次切換都會害網路重新啟動。
有個簡單的變通辦法：把開關匯流排放在[子網路](../ae2-mechanics/subnetworks.md)上，這樣重啟的就只有子網路。

我們可以做一個自成一體的[子網路](../ae2-mechanics/subnetworks.md)，由 <ItemLink id="annihilation_plane" /> 與 <ItemLink id="storage_bus" />
組成，把東西推進主網路上的 <ItemLink id="interface" />。開關匯流排負責把子網路與 <ItemLink id="quartz_fiber" /> 接上或斷開，
藉此切斷面板的電源。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/regulated_cobble_gen.snbt" />

<BoxAnnotation color="#dddddd" min="3 2 2" max="7 2.3 3">
        (1) 破壞面板：沒有介面可設定，但可以附上效率與耐久來降低耗電。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 2" max="2.3 3 3">
        (2) 儲存匯流排：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 2.3 2" max="2.7 2.7 2.3">
        (3) 開關匯流排：非常重要的一點是，開關匯流排要放在子網路上，
        不能放在主網路上。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 2.3" max="2.7 3.3 2.7">
        (4) 位準發射器：設定為鵝卵石與想要的數量，模式設為「低於設定值時發出訊號」。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 3" max="2 3 2">
        (5) 介面：維持預設設定。
  </BoxAnnotation>

<DiamondAnnotation pos="0 2.5 1.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

<DiamondAnnotation pos="5 1.5 3.5" color="#00ff00">
        含水階梯讓水不會流動，也就不會把岩漿變成黑曜石。
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 設定

* <ItemLink id="annihilation_plane" />（1）沒有介面可設定，但可以附上效率與耐久來降低耗電。
* <ItemLink id="storage_bus" />（2）維持預設設定。
* <ItemLink id="toggle_bus" />（3）必須放在石英纖維的子網路那一側，不能放在主網路上，
  否則每次切換都會害主網路重新啟動。
* <ItemLink id="level_emitter" />（4）設定想要的物品與數量，並設為「低於設定值時發出訊號」。
* <ItemLink id="interface" />（5）維持預設設定。

## 運作原理

1. 鵝卵石產生器產出鵝卵石。
2. <ItemLink id="annihilation_plane" /> 把鵝卵石打掉。
3. <ItemLink id="storage_bus" /> 把鵝卵石存進 <ItemLink id="interface" />，也就送進了主網路。
4. 當主網路裡的鵝卵石數量超過設定值時，<ItemLink id="level_emitter" /> 停止發出訊號，
   <ItemLink id="toggle_bus" /> 隨之關閉。
5. 子網路因此斷電，破壞面板停止運作。
