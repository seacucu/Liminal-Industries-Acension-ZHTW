---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: P2P 通道
  icon: me_p2p_tunnel
  position: 210
categories:
- devices
item_ids:
- ae2:me_p2p_tunnel
- ae2:redstone_p2p_tunnel
- ae2:item_p2p_tunnel
- ae2:fluid_p2p_tunnel
- ae2:fe_p2p_tunnel
- ae2:light_p2p_tunnel
---

# 點對點通道

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

P2P 通道讓物品、流體、紅石訊號、電力、光線與[頻道](../ae2-mechanics/channels.md)
能在網路裡移動，卻不會直接和網路互動。P2P 通道有很多種變體，每一種只運送它專屬的那類東西。
它們本質上就像傳送門，把兩個相隔遙遠的方塊面直接接在一起。它們不是雙向的，輸入端與輸出端是分明的。

![Portal](../assets/assemblies/p2p_portal.png)

舉例來說，對著物品 P2P 的那個漏斗，會表現得像是直接接在木桶上，物品因而流動。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_hopper_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

不過，兩個緊鄰的木桶彼此之間並不會搬運物品。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_barrel_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

還有其他變體，例如紅石 P2P。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_redstone.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

還有 ME P2P，它搬運的是頻道。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_channels.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## P2P 通道的種類與調諧

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="90" />
</GameScene>

P2P 通道有很多種。只有 ME P2P 通道可以直接合成，其餘都是拿特定物品右鍵點擊其他 P2P 通道轉換而成：
- ME P2P 通道：用任何[線纜](../items-blocks-machines/cables.md)右鍵點擊。
- 紅石 P2P 通道：用各種紅石元件右鍵點擊。
- 物品 P2P 通道：用儲物箱或漏斗右鍵點擊。
- 流體 P2P 通道：用水桶或玻璃瓶右鍵點擊。
- 能量 P2P 通道：用幾乎任何含有能量的物品右鍵點擊。
- 光源 P2P 通道：用火把或螢光石右鍵點擊。

某些通道有特殊限制。舉例來說，ME P2P 通道的頻道無法穿過另一個 ME P2P 通道；
而能量 P2P 通道會靠提高自身的[能量](../ae2-mechanics/energy.md)消耗，間接對通過的 FE 或 E 抽取 5% 的稅。

## P2P 最常見的用法

P2P 通道最常見的用途，是用 ME P2P 通道來壓縮[頻道](../ae2-mechanics/channels.md)的傳輸密度。
你不必拉一整束緻密線纜，單一條緻密線纜就能載著大量頻道跑。

這個例子裡，8 個 ME P2P 輸入端從主網路的 <ItemLink id="controller" /> 取走 256 條頻道（8*32），
再由 8 個 ME P2P 輸出端送到別處。注意每個 P2P 通道的輸入端或輸出端各只佔 1 條頻道，
於是我們就能讓大量頻道走過一條細線纜。而且因為這些 P2P 通道位於專用的[子網路](../ae2-mechanics/subnetworks.md)上，
這麼做甚至不會用掉主網路的任何頻道！另外也注意，P2P 通道雖然可以直接貼在控制器上，
中間夾一條[緻密智慧線纜](../items-blocks-machines/cables.md#smart-cable)會讓頻道更容易看清楚。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/p2p_compact_channels.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 1.3 6.3" max="2 2.7 6.7">
        石英纖維在主網路與 P2P 子網路之間共享電力。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.1 0 5.7" max="5 2.3 6.4">
        通道的輸入端可以直接貼在控制器上，也可以拉線纜過去。
  </BoxAnnotation>

  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

另一個例子（包含搭配[量子橋接](quantum_bridge.md)的用法），請看這張我懶得美化的小畫家示意圖：

![P2P and quantum bridges](../assets/diagrams/p2p_quantum_network.png)

## 巢狀嵌套

不過，你沒辦法靠這招讓一條線纜送出無限條頻道。ME P2P 通道的頻道不會穿過另一個 ME P2P 通道，
所以它們不能遞迴嵌套。注意看紅色線纜上外層那些 ME P2P 通道是離線的。
要注意這只適用於 ME P2P 通道，其他類型的 P2P 通道是可以穿過 ME P2P 通道的，
從圖中紅石 P2P 通道運作正常就看得出來。

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_nesting.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

## 連結

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_linking_frequency.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

P2P 通道的兩端用 <ItemLink id="memory_card" /> 連結。頻率會以 2x2 的色塊顯示在通道背面。
- 潛行右鍵可以產生一組新的 P2P 連結頻率。
- 右鍵則是貼上設定、升級卡或連結頻率。

你潛行右鍵的那一端會是輸入端，右鍵的那一端則是輸出端。輸出端可以有多個，
但對 ME P2P 通道而言，輸入端流進來的頻道會被分配給各個輸出端，所以你沒辦法複製頻道。

## 配方

<RecipeFor id="me_p2p_tunnel" />
