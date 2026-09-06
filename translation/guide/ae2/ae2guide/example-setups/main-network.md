---
navigation:
  parent: example-setups/example-setups-index.md
  title: 「主網路」範例
  icon: controller
---

# 「主網路」範例

其他很多篇都會提到「主網路」。你或許也會想問，這些[裝置](../ae2-mechanics/devices.md)到底怎麼湊成一套能用的系統。以下是一個範例：

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="3.9 0 1.9" max="9.1 5 7.1" thickness="0.05">
        一大叢樣板供應器與組裝機，替合成、切石與鍛造樣板留下充足的空間。
        棋盤式的排法讓供應器能平行使用多台組裝機，同時保持緊湊。
        以 8 個為一組，頻道就不可能繞錯。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="3.9 0 9.9" max="5.1 3 12.1" thickness="0.05">
        幾台機器，搭配一條管線子網路把它們的產出推回供應器。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 8.9" max="1.1 3 13.1" thickness="0.05">
      幾台終端機與各式小工具。（你大概只需要合成終端機，不必一般終端機_和_合成終端機都放）
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 -0.1" max="2.1 3 8.1" thickness="0.05">
      一整排合成 CPU。少數幾座容量較大，其餘容量較小的則多放幾座。
      實際使用時你大概會想放更多協同處理器，但那樣這個場景會太大。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5.9 0 13.9" max="7.1 1 15.1" thickness="0.05">
      控制器應該放在基地正中央，而且大概要比這個再大一點。做成長條狀相當好用。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="11.9 0 7.9" max="13.1 4 13.1" thickness="0.05">
        各種做倉儲的方式，用驅動器或儲存匯流排都行。注意全部都是 8 個一組。
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="10.9 0 0.9" max="13.1 2 7.1" thickness="0.05">
        各種做倉儲的方式，用驅動器或儲存匯流排都行。注意全部都是 8 個一組。
    </BoxAnnotation>

  <IsometricCamera yaw="315" pitch="30" />
</GameScene>
