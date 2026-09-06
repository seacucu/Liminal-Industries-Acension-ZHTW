---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 能量
  icon: energy_cell
---

# 能量

你的網路需要能量才能運轉。網路有一池共用的能量，[裝置](../ae2-mechanics/devices.md)直接從中取用，
而 <ItemLink id="vibration_chamber" />、<ItemLink id="energy_acceptor" />（以及 <ItemLink id="controller" />）則負責往裡面加。
拿 <ItemLink id="network_tool" /> 對網路上任一處右鍵，或是右鍵點擊網路的控制器（如果有的話），
就能看到該網路的能量數據。因為儲存與分配是整個網路共用的，所以不存在傳輸速率上限：
裝置想抽多少電就抽多少，能量接收器的輸入速度實際上也沒有上限，唯一的限制是你的儲電量。

## 能量輸入

<Row>
  <BlockImage id="energy_acceptor" scale="4" />

  <GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
  </GameScene>

  <BlockImage id="controller" p:state="online" scale="4" />

  <BlockImage id="vibration_chamber" p:active="true" scale="4" />
  
  <BlockImage id="crystal_resonance_generator" scale="4" />
</Row>

AE2 內部不使用 Forge Energy（Forge 版）或 TechReborn Energy（Fabric 版），而是把它們轉換成自己的單位 AE。
這個轉換是單向的。負責轉換的是 <ItemLink id="energy_acceptor" /> 與 <ItemLink id="controller" />，
不過控制器的面拿去接[頻道](../ae2-mechanics/channels.md)更值得。
<ItemLink id="vibration_chamber" /> 也能自己發電，<ItemLink id="crystal_resonance_generator" /> 則能被動供電，但 AE2 的設計本來就是要搭配發電能力更強的科技模組。

也因此，在規劃基地的供電架構時，最好把整個 AE2 網路當成一台大型的多方塊機器來看待。

Forge Energy 與 TechReborn Energy 的換算比例是

*   2 FE = 1 AE（Forge）
*   1 E  = 2 AE（Fabric）

## 能量儲存

<Row>
  <BlockImage id="energy_cell" scale="4" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="4" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="4" />
</Row>

理由相當明顯：一個網路在單一遊戲刻內，能輸入或消耗的能量不會超過它存得下的量。
如果網路只存得下 800 AE，那麼[裝置](../ae2-mechanics/devices.md)要電時最多只能用掉 800 AE（假設電是滿的），
能量接收器一次也最多只能灌進 800 AE（假設電是空的）。

這是很多怪現象的共同原因：有人組了一套只有能量接收器、驅動器、終端機和幾個裝置的小網路，
然後想把整個物品欄的鵝卵石一口氣倒進去。要在單一遊戲刻內塞進那麼多鵝卵石，
需要的能量超過網路的儲電量，於是石頭沒全進去，網路的電被抽乾，接著重新啟動。

**加幾顆能量電池就能解決。**

網路本身每條線纜、每台機器或每個元件內建 25 AE 的緩衝。

<ItemLink id="controller" /> 有少量的內部儲電，8,000 AE

<ItemLink id="energy_cell" /> 可儲存 200k AE，大多數情況下一顆就夠了，網路日常運作的耗電尖峰它輕鬆應付得來。

<ItemLink id="dense_energy_cell" /> 可儲存 1.6M AE，適合用在想靠儲備電力跑網路，
或是要應付大型[空間儲存](spatial-io.md)設施那種瞬間巨額耗電的場合。

<ItemLink id="creative_energy_cell" /> 是測試用的創造模式物品，提供無限的電力之類的。
