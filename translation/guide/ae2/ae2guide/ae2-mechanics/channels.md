---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 頻道
  icon: controller
---

# 頻道

《應用能源 2》的 [ME 網路](me-network-connections.md)需要頻道，才能支撐那些會用到網路倉儲或其他網路服務的[裝置](../ae2-mechanics/devices.md)。
你可以把頻道想成接到各個裝置的 USB 線：一台電腦的 USB 埠就那麼多，能接的裝置數量有限。
大多數機器、整格裝置與一般線纜最多只能通過 8 條頻道，
可以把整格裝置與一般線纜想成一束 8 條的「頻道線」。
不過[緻密線纜](../items-blocks-machines/cables.md#dense-cable)最多能承載 32 條頻道。
其他能傳 32 條的只有 <ItemLink id="me_p2p_tunnel" /> 與[量子網路橋接](../items-blocks-machines/quantum_bridge.md)。
每當一個裝置佔掉一條頻道，就想像從那束線裡抽走一條 USB 線，那條線在下游自然就不能用了。

<GameScene zoom="7" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_demonstration_1.snbt" />

  <LineAnnotation color="#33ff33" from="1 .4 .7" to="2.4 .4 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .7" to="2.4 .6 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .6" to="2.6 .4 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.4 .6 .7" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .4 .7" to="2.4 .4 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .6 .6" to="2.6 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 .6" to="2.6 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.1 .6 1.5" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 1.5" to="2.9 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.6 .6 1.5" to="2.6 .9 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .1 1.5" to="2.4 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .4" to="3.5 .6 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="3.5 .6 .4" to="3.5 .9 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="3.5 .1 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .3" to="1.5 .6 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1.5 .6 .3" to="1.5 .9 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1.5 .1 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#ff3333" from="3.5 .5 .5" to="5.5 .5 .5" alwaysOnTop={true}>
  線纜裡的 8 條頻道都用完了，所以驅動器分不到。
  </LineAnnotation>

  <LineAnnotation color="#993333" from="1 .5 .5" to="1.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="1.5 .5 .5" to="1.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2 .5 .5" to="2.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2.5 .5 .5" to="2.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="3 .5 .5" to="3.25 .5 .5" alwaysOnTop={true}/>

  <DiamondAnnotation pos="3.6 0.5 0.5" color="#ff0000">
        線纜裡的 8 條頻道都用完了，所以驅動器分不到。
    </DiamondAnnotation>

  <IsometricCamera yaw="15" pitch="30" />
</GameScene>

想看清頻道在網路裡怎麼分配與繞行，最簡單的辦法是用[智慧線纜](../items-blocks-machines/cables.md)，它會把頻道的路徑與用量顯示在線纜上。

頻道每經過一個節點會消耗 1⁄128 ae/t。也就是說，一個只有 8 個裝置卻超過 96 個節點的網路，
加上一台 <ItemLink id="controller" /> 之後耗電反而可能下降，因為頻道的分配方式變了。

要特別注意，**頻道和線纜顏色完全無關**，顏色的唯一作用是讓線纜不互相連接。

## 頻道的繞行方式

有 <ItemLink id="controller" /> 的情況下，頻道分三段繞行。
先取經過相鄰機器、通往最近一條[一般線纜](../items-blocks-machines/cables.md)（玻璃、包覆或智慧）的最短路徑；
再取經過該一般線纜、通往最近一條[緻密線纜](../items-blocks-machines/cables.md)（緻密或緻密智慧）的最短路徑；
最後取經過該緻密線纜通往 <ItemLink id="controller" /> 的最短路徑。
如果最短路徑已經塞滿，有些[裝置](devices.md)就會分不到需要的頻道。善用彩色線纜、線纜錨與通道，
確保頻道走在你要的路徑上。

舉例來說，這個例子裡有些驅動器分不到頻道：線纜的總容量其實夠，
但頻道全都想走最短路徑，於是有些線纜被塞爆，有些卻空著。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 3.6" to="1.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.4 0.5 3.6" to="1.4 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 1.6" to="0.6 .5 1.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 1.6" to="0.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 3.4" to="1.4 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 3.4" to="1.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <BoxAnnotation color="#dddddd" min="1.2 0.2 3.2" max="1.8 0.8 3.8" alwaysOnTop={true} thickness="0.05">
        超過 8 條頻道想從這裡穿過去，於是有些被截斷了。
  </BoxAnnotation>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

解法是更謹慎地限制頻道可走的路徑。網路的形狀應該像樹（或像灌木），
盡量減少迴路與模稜兩可的頻道路徑。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue_fix.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 5.6" to="1 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

## 臨時網路

沒有 <ItemLink id="controller" /> 的網路稱為臨時網路，最多可以支撐 8 個需要頻道的裝置。
一旦超過 8 個，網路上所有需要頻道的裝置都會停擺，
這時你要嘛拆掉一些裝置，要嘛加一台 <ItemLink id="controller" />。

和有控制器的網路不同，臨時網路上的[智慧線纜](../items-blocks-machines/cables.md)顯示的是整個網路已使用的頻道數，
而不是流經該條線纜的頻道數。

臨時網路上，每個裝置佔用的是整個網路的 1 條頻道，這和 <ItemLink id="controller" /> 依最短路徑分配頻道的作法差別很大。

## 設計

如同前面[頻道的繞行方式](channels.md#channel-routing)所說，網路最好設計成樹狀結構：緻密線纜從控制器分出去，
一般線纜再從緻密線纜分出去，[裝置](../ae2-mechanics/devices.md)則以 8 個以內為一叢掛在一般線纜上。

以下是一個反面教材：

順著頻道的路徑看，

1. 一離開控制器往右，就被壓在 8 條頻道，因為驅動器的行為和一般線纜相同。
不過這裡用的不是智慧線纜，所以看不出用掉幾條。剩 8 條。
2. 驅動器佔掉一條。
剩 7 條。
3. 兩條往上給終端機。
剩 5 條。
4. 繼續往右，介面又佔掉一條。
剩 4 條。
5. 一條往上給樣板供應器。
剩 3 條。
6. 繼續往右，一條往上給輸入匯流排。
剩 2 條。
7. 那叢供料給組裝機的樣板供應器只分到 2 條，所以其中兩個供應器沒有頻道。

歸根究柢，錯在讓頻道被壓在瓶頸上，又沒有想清楚頻道會怎麼分配。

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/bad_network_structure.snbt" />

<LineAnnotation color="#33ff33" from="6.5 .5 1.5" to="6 .5 1.5" alwaysOnTop={true} thickness="0.4">
  32 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="6 .5 1.5" to="5.5 .5 1.5" alwaysOnTop={true} thickness="0.2">
  8 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 1.5 1.5" alwaysOnTop={true} thickness="0.1">
  2 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 1.5 1.5" to="5.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 2.5 1.5" to="5.5 2.5 1.1" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="4.5 .5 1.5" alwaysOnTop={true} thickness="0.158">
  5 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 1.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="3.5 .5 1.5" alwaysOnTop={true} thickness="0.122">
  3 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="3.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 2.5 1.5" to="3.7 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="1.5 .5 1.5" alwaysOnTop={true} thickness="0.1">
  2 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="1.5 0.3 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="0.5 0.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#33ff33" from="0.5 0.5 1.5" to="0.5 0.5 0.5" alwaysOnTop={true} thickness="0.071">
  1 條頻道
</LineAnnotation>

<LineAnnotation color="#ff3333" from="0.5 1.5 1.5" to="0.5 1.3 1.5" alwaysOnTop={true} thickness="0.071">
  沒有頻道
</LineAnnotation>

<LineAnnotation color="#ff3333" from="1.5 1.5 0.5" to="1.5 1.3 0.5" alwaysOnTop={true} thickness="0.071">
  沒有頻道
</LineAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

---

以下則是良好結構的範例：

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="6.9 0 4.9" max="9.1 4 7.1" thickness="0.05">
        注意樣板供應器是分成一組 8 個。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 4 4" max="8 5 5" thickness="0.05">
        兩條塞滿頻道的一般線纜匯在一起，就代表你需要一條緻密線纜。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 0 13" max="8 1 14" thickness="0.05">
        用不同的線纜顏色，避免相鄰的線纜連在一起。
    </BoxAnnotation>


  <IsometricCamera yaw="315" pitch="30" />
</GameScene>

## 頻道模式

Minecraft 1.18 版的 AE2 10.0.0 新增了幾個選項，可以改變頻道在你世界中的行為。
general 區段裡多了一個設定項（`channels`）來控制它，遊戲內也新增了給管理員用的指令，
可以直接在遊戲中改模式與設定。用 `/ae2 channelmode <模式>` 切換，用 `/ae2 channelmode` 查看目前模式。
在遊戲中切換模式時，所有現有電網都會重新啟動並立刻套用新模式。

這等於復活並改良了 Minecraft 1.12 時期就有的選項，讓那些只想玩得輕鬆一點、
但又不想把整個機制拿掉的玩家有更好的選擇。

下表列出設定檔與指令中可用的模式。

| 設定值    | 說明                                                                                                                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default`  | 標準模式，線纜與臨時網路的頻道容量就是本站各處所述的數值                                                                                                                                                                                                           |
| `x2`       | 所有頻道容量加倍（一般線纜 16、緻密線纜 64，臨時網路支援 16 條頻道）                                                                                                                                                                                                           |
| `x3`       | 所有頻道容量變三倍（一般線纜 24、緻密線纜 92，臨時網路支援 24 條頻道）                                                                                                                                                                                                           |
| `x4`       | 所有頻道容量變四倍（一般線纜 32、緻密線纜 128，臨時網路支援 32 條頻道）                                                                                                                                                                                                           |
| `infinite` | 完全解除頻道限制。控制器依然能*大幅*降低電網的耗電。智慧線纜只會在全暗（沒有頻道通過）與全亮（有 1 條以上頻道通過）之間切換。 |
