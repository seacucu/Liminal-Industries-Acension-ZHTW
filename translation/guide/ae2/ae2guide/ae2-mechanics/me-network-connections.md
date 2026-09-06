---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 網路連線
  icon: fluix_glass_cable
---

# 網路連線

## 「網路」是什麼意思？

「網路」是一群[裝置](../ae2-mechanics/devices.md)，由能夠傳遞[頻道](../ae2-mechanics/channels.md)的方塊串起來，
例如[線纜](../items-blocks-machines/cables.md)，或是整格的機器與[裝置](../ae2-mechanics/devices.md)。
（<ItemLink id="charger" />、<ItemLink id="interface" />、<ItemLink id="drive" /> 等等）
嚴格說來，單獨一條線纜其實就是一個網路。

## 順帶談談裝置擺在哪

對於具備特定網路功能的[裝置](../ae2-mechanics/devices.md)來說（例如 <ItemLink id="interface" />
對[網路倉儲](../ae2-mechanics/import-export-storage.md)推拉、<ItemLink id="level_emitter" />
讀取網路倉儲的內容、<ItemLink id="drive" /> 本身就是網路倉儲，諸如此類），
裝置擺在哪個位置完全不重要。

再說一次，**裝置的實體位置不重要**。重要的只有它有沒有接上網路（當然，還有接上的是哪一個網路）。

## 網路連線

想知道一個網路上接了什麼，最簡單的辦法是用 <ItemLink id="network_tool" />。它會列出網路上的每一個元件，
所以要是看到不該出現的東西，或是該有的東西沒出現，那就有問題了。

舉例來說，這是兩個各自獨立的網路。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        網路 1
  </BoxAnnotation>

<BoxAnnotation color="#915dcd" min="2 0 0" max="3 2 2">
        網路 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

這同樣是兩個獨立的網路，因為 <ItemLink id="quartz_fiber" /> 只共享[能量](../ae2-mechanics/energy.md)，
並不會建立網路連線。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        網路 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="1.3 0 0" max="3 2 2">
        網路 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

但這個只是一個網路，不是兩個。[量子橋接](../items-blocks-machines/quantum_bridge.md)的作用就像一條無線的[緻密線纜](../items-blocks-machines/cables.md#dense-cable)，
所以兩端屬於同一個網路。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="7 3 3">
        全部是同一個網路
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

這個也只是一個網路。[線纜](../items-blocks-machines/cables.md)的顏色和網路連線沒有關係，唯一的作用是不同顏色的線纜彼此不會連接。
所有顏色都能接上福魯伊克斯（也就是「無色」）線纜。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        全部是同一個網路
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 比較不直覺的連線

這個例子裡只有一個網路，因為 <ItemLink id="pattern_provider" /> 是整格的裝置，行為就像一條線纜，
<ItemLink id="inscriber" /> 也是。於是網路連線就這樣穿過了供應器與壓印機。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        全部是同一個網路
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

想避免這種情形（很多牽涉到[子網路](../ae2-mechanics/subnetworks.md)的自動合成設施都需要），
可以拿 <ItemLink id="certus_quartz_wrench" /> 右鍵點擊供應器，讓它變成單向的，這樣它就不會從某一面傳遞頻道。

<Row gap="40">
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="2 2 2">
        網路 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="2 0 0" max="4 2 2">
        網路 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_directional_connection.snbt" />

  <BoxAnnotation color="#ee3333" min="1 .3 .3" max="1.3 .7 .7">
        注意看，線纜並沒有接上去
  </BoxAnnotation>

  <IsometricCamera yaw="255" pitch="30" />
</GameScene>
</Row>

其他同樣不提供定向網路連線的，還有大部分的[線纜附件](../ae2-mechanics/cable-subparts.md)類[裝置](../ae2-mechanics/devices.md)，
例如 <ItemLink id="import_bus" />、<ItemLink id="storage_bus" /> 與 <ItemLink id="cable_interface" />。

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/subpart_no_connection.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
