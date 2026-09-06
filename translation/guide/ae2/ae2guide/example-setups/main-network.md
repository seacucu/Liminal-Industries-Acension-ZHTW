---
navigation:
  parent: example-setups/example-setups-index.md
  title: 「主網路」範例
  icon: controller
---

# 「主網路」範例

其他很多篇都會提到「主網路」。你或許也會想問，這些[裝置](../ae2-mechanics/devices.md)到底怎麼湊成一套能用的系統。以下是一個範例：

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/small_base_network.snbt" />

    <BoxAnnotation color="#33dd33" min="5 1 10" max="9 7 14" thickness="0.05">
        一大叢樣板供應器與組裝機，替合成、切石與鍛造樣板留下充足的空間。
        棋盤式的排法讓供應器能平行使用多台組裝機，同時保持緊湊。
        以 8 個為一組，頻道就不可能繞錯。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="13 10 12" max="14 11 14" thickness="0.05">
        控制器其實不用蓋那麼大，你在別人基地裡看到的那些巨大圓環與方陣，
        主要就是為了好看。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="13 12 13" max="14 13 14" thickness="0.05">
        每個像樣的網路都該有一顆能量電池，好讓每個遊戲刻能灌進更多電，
        並把電力的起伏壓平。
    </BoxAnnotation>
    
    <BoxAnnotation color="#33dd33" min="2 1 10" max="4 4 13" thickness="0.05">
        你大概會想用其他模組的電力來源，反應爐、太陽能板、發電機之類的。
        諧振倉算堪用，但 AE2 的設計本來就是要放在模組包裡、
        吃你基地的主要發電設施。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="15 1 9" max="16 3 14" thickness="0.05">
        外牆板可以把東西藏在牆後面。
    </BoxAnnotation>
    <BoxAnnotation color="#33dd33" min="15 3 12" max="16 10 14" thickness="0.05">
        外牆板可以把東西藏在牆後面。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="13 9 7" max="14 10 9" thickness="0.05">
        一般倉儲不需要那麼多驅動器與單元，2 到 4 台驅動器份量的 4k 或 16k
        單元幾乎一定夠用。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="13 9 10" max="14 11 11" thickness="0.05">
        大宗倉儲則要用篩選成特定物品的大容量單元，放在另外幾台優先權較高的
        驅動器裡。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="10 9 13" max="11.7 13 14" thickness="0.05">
        用介面做的自動備料。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="6 10 12" max="9 12 15" thickness="0.05">
        把充能器自動化那套設施擴充到多台充能器的自然結果。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="2 10 12" max="5 11 15" thickness="0.05">
        另一種處理器自動化的作法，因為 1.20 的壓印機已經能自動彈出產物了。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="3 10 10" max="4 12 11" thickness="0.05">
        另一種處理器自動化的作法，因為 1.20 的壓印機已經能自動彈出產物了。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="7.2 9.2 8.2" max="7.8 10 8.8" thickness="0.05">
        無線存取點放在正中央，因為它的範圍是球形的。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="14 1 2" max="16 5 7" thickness="0.05">
        典型的配置是 1 到 2 座大型合成 CPU 處理大工作，再加幾座小的，
        在大 CPU 忙碌時處理次要工作。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="5 3 6" max="6 4 7" thickness="0.05">
        子網路上的裝置若超過 8 個（例如要分送到 8 個以上的地方），
        有時它自己也需要一台控制器。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="7.3 1 3.3" max="9.7 4 6" thickness="0.05">
        賽特斯農場。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="10.3 1 2.3" max="12.7 3.7 5" thickness="0.05">
        丟進水裡的自動化。
    </BoxAnnotation>

  <IsometricCamera yaw="135" pitch="15" />
</GameScene>
