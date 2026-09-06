---
navigation:
  parent: example-setups/example-setups-index.md
  title: 倉儲的種類與網路整潔
  icon: drive
---

# 各種倉儲與網路的整潔

善用篩選、[分區](../items-blocks-machines/cell_workbench.md)與[倉儲優先權](../ae2-mechanics/import-export-storage.md#storage-priority)，
你可以替不同種類的東西建立好幾層倉儲。

倉儲大致可分成：
* 一般倉儲，用來放那些數量從幾個到幾千個不等的雜物。用的是小容量的[儲存單元](../items-blocks-machines/storage_cells.md)，
例如 4k 或 16k。
* 大宗倉儲，用來放數量超過幾千的東西，例如鵝卵石或鐵。用的是 256k 這種大容量單元，或是 MEGA 附屬模組的單元。
* 農場旁的在地倉儲，作法見[專用的在地倉儲](specialized-local-storage.md)與
[各種](simple-certus-farm.md)[賽特斯](semiauto-certus-farm.md)[農場](advanced-certus-farm.md)。

優先權要這樣安排：東西倒進主網路時，先試著存進專用的大宗或在地倉儲；存不進去時（因為篩選與分區擋著），
才放進一般倉儲。
也就是說，東西**不會主動**從一個倉儲搬到另一個，而是隨著進出網路慢慢「遷移」過去。
想主動搬運，就得用 <ItemLink id="io_port" />。

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="../assets/assemblies/network_storage_types.snbt" />

    <BoxAnnotation color="#33dd33" min="11 0 1" max="12 1.3 2" thickness="0.05">
        大宗倉儲。這裡用的是貼在抽屜這類大容量容器上、並設好篩選的儲存匯流排。這個儲存匯流排篩選設為
        煤炭，優先權很高，所以煤炭一進網路就會流到這裡；而從網路取煤炭時，*除了這裡以外*的地方會先被取用，
        於是煤炭就「遷移」進這個抽屜。

        重要提醒：抽屜這類經過最佳化的大容量容器沒問題，但欄位極多又*沒有*最佳化的容器（例如巨型儲物箱），
        搭配儲存匯流排會嚴重拖累效能。
    </BoxAnnotation>

    <BoxAnnotation color="#33dd33" min="11 0 3" max="12 1 4" thickness="0.05">
        大宗倉儲。這裡用的是插在高優先權驅動器裡、做過分區的 256k 單元。這個單元分區設為
        鵝卵石與鐵，並裝了平均分配卡，才不會被鵝卵石塞滿而讓鐵沒地方放。驅動器優先權很高，
        所以鵝卵石或鐵一進網路就會流到這裡；取用時則會先從*除了這裡以外*的地方拿，
        於是鵝卵石與鐵就「遷移」進這個單元。
    </BoxAnnotation>

    <BoxAnnotation color="#33dddd" min="11 0 5" max="12 1 6" thickness="0.05">
        一般倉儲。這裡是一台插滿 16k 單元的驅動器，單元都沒有做分區。驅動器優先權設為中性
        （這裡是 0），所以東西進網路時會先流向專用的大宗或在地倉儲；
        取用時則會先從這裡拿，於是有專屬去處的物品自然而然會從一般倉儲「遷移」出去。
    </BoxAnnotation>

    <BoxAnnotation color="#88ff88" min="11 0 8" max="12 1 9" thickness="0.05">
        這台 IO 埠對維持網路整潔很重要。既然倉儲優先權*不會主動*搬運物品，
        一般倉儲用的單元就該定期用 IO 埠「洗一遍」，把有專屬去處的物品送進專用倉儲。
        這等於替倉儲「重組」，確保同一樣東西不會散落在好幾個地方。
    </BoxAnnotation>

    <BoxAnnotation color="#dd3333" min="14 0 11" max="15 1 12" thickness="0.05">
        怪物農場旁的在地倉儲。這台驅動器裡的單元分區設為你想留下的掉落物，例如骨頭與箭。
        驅動器本身不設優先權，因為真正影響優先權的是主網路那側、用來存取這條子網路的儲存匯流排。
        單元上裝了平均分配卡與溢位銷毀卡。
    </BoxAnnotation>

    <BoxAnnotation color="#dd3333" min="14 1 10" max="15 2.3 11" thickness="0.05">
        怪物農場旁的在地倉儲。這組儲存匯流排與介面的搭配，讓主網路能存取這條子網路的倉儲。
        這個儲存匯流排優先權設得很高，篩選則設為子網路單元裡存放的那些東西。

        重要：由於子網路上還接了垃圾桶，這個儲存匯流排一定要設篩選，
        否則它會開始銷毀*進入網路的每一樣物品、流體等等*！
    </BoxAnnotation>

    <BoxAnnotation color="#dd3333" min="14 0 9" max="15 1.3 10" thickness="0.05">
        怪物農場旁的在地倉儲。這個貼在物質聚合器上的儲存匯流排，優先權設得比驅動器低。
        也就是說，進不了驅動器單元的掉落物會溢流到這裡被銷毀。這一步很重要，
        否則子網路很快就會被快壞掉的弓之類的雜物塞爆。
    </BoxAnnotation>

    <BoxAnnotation color="#dd33dd" min="8 1 11.7" max="9 2.3 13" thickness="0.05">
        西瓜農場旁的在地倉儲。這套設施用的手法和前面各種賽特斯農場範例相同：
        子網路上的儲存匯流排把收成送進木桶，主網路上另一個儲存匯流排（篩選設為西瓜片、優先權很高）
        則讓主網路存取得到那些收成。
    </BoxAnnotation>

  <IsometricCamera yaw="270" pitch="30" />
</GameScene>
