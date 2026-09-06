---
navigation:
  title: 入門指南（1.20+）
  position: 10
---

<div class="notification is-info">
  以下內容僅適用於 Minecraft 1.20 以後的應用能源 2。
</div>

# 入門指南

## 取得最初的材料

<GameScene zoom="4" background="transparent">
  <ImportStructure src="assets/assemblies/meteor_interior.snbt" />
</GameScene>

要開始玩《應用能源 2》，第一件事是找到[隕石坑](ae2-mechanics/meteorites.md)。這種地形相當常見，而且往往在地表留下一個大洞，所以你旅途中大概已經撞見過。
如果還沒有，可以合成一個 <ItemLink id="meteorite_compass" />，它會指向最近的 <ItemLink id="mysterious_cube" />。

找到隕石坑之後，往中心挖進去。你會看到賽特斯石英晶簇、賽特斯石英芽、各種階級的[石英芽床](items-blocks-machines/budding_certus.md)，正中央還有一個神秘的立方體。

把賽特斯石英晶簇和看到的賽特斯石英方塊都挖走。石英芽床也可以帶走，但沒有絲綢之觸的話會掉一個階級。

千萬別去打無瑕的石英芽床，就算附了絲綢之觸也會退化成微瑕，而且沒有任何辦法修回無瑕。

隕石坑正中央的神秘立方體也要挖，裡面有全部四種壓印模具。

## 種賽特斯石英

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_certus_1.snbt" />
</GameScene>

賽特斯石英芽會從[石英芽床](items-blocks-machines/budding_certus.md)上長出來，和紫水晶類似。如果你打掉還沒長成的石英芽，
會掉落一個 <ItemLink id="certus_quartz_dust" />，且不受幸運影響。如果打掉的是完全長成的晶簇，則會掉落四個
<ItemLink id="certus_quartz_crystal" />，幸運則會增加這個數量。

石英芽床共有四個階級：無瑕、微瑕、裂損、重損。

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_blocks.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

石英芽每長大一個階段，芽床就有機率衰變一級，最後變成普通的賽特斯石英方塊。把芽床（或賽特斯石英方塊）連同一個以上的
<ItemLink id="charged_certus_quartz_crystal" /> 丟進水裡，就能修復它，新的芽床也是這樣做出來的。

<RecipeFor id="damaged_budding_quartz" />

無瑕的石英芽床不會衰變，能無限產出賽特斯石英。不過它既無法合成，也沒辦法用鎬挖走，
就算附了絲綢之觸也一樣。（但它*可以*用[空間儲存](ae2-mechanics/spatial-io.md)搬移）

光靠自己，賽特斯石英芽長得非常慢。所幸把 <ItemLink id="growth_accelerator" /> 放在芽床旁邊，
可以大幅加快這個過程。這東西應該列為你最優先要蓋的幾樣設施之一。

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_certus_2.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

如果你的石英還不夠做 <ItemLink id="energy_acceptor" /> 或 <ItemLink id="vibration_chamber" />，
可以做一個 <ItemLink id="crank" /> 插在加速器末端。

自動採收賽特斯石英的作法[在這裡說明](example-setups/simple-certus-farm.md)。

## 順帶一提福魯伊克斯

另一種你會需要的材料是福魯伊克斯，做生長加速器時你已經碰過它了。作法是把充能賽特斯石英、紅石與地獄石英丟進水裡。至於怎麼自動化，「留給讀者當作習題」。

如果你還沒做 <ItemLink id="charger" />，那也得補上，因為 <ItemLink id="charged_certus_quartz_crystal" /> 得靠它才生得出來。

## 壓印幾片處理器

在隕石坑裡打掉神秘立方體時，你會得到四種「壓印模具」。它們用在 <ItemLink id="inscriber" /> 上，製作三種處理器。

<ItemGrid>
  <ItemIcon id="silicon_press" />

  <ItemIcon id="logic_processor_press" />

  <ItemIcon id="calculation_processor_press" />

  <ItemIcon id="engineering_processor_press" />
</ItemGrid>

壓印機和原版熔爐一樣是分面的機器：從頂部或底部送入的物品會進上下兩格，從側面或背面送入的則進中間那格。成品可以從側面或背面取出。

為了方便用漏斗自動化（順便少牽幾條管線），壓印機可以用 <ItemLink id="certus_quartz_wrench" /> 轉向。

先把三種處理器各做幾片備著，下一步要拿來組一套最基本的 ME 系統。至於處理器怎麼自動化生產，一樣「留給讀者當作習題」。

## 物質能源技術：ME 網路與儲存

### 什麼是 ME 儲存？

它唸作 Emm-Eee，是 Matter Energy（物質能源）的縮寫。

物質能源是《應用能源 2》的核心，你可以把它想成瘋狂科學家版本的多方塊儲物箱，它會徹底改變你的倉儲方式。
ME 和 Minecraft 裡其他儲存系統差別極大，剛開始可能得換個腦袋才習慣得了；
但一旦上手，用極小的空間裝下海量物品、到處都能開存取終端機，都還只是冰山一角。

### 開始前該知道什麼？

首先，ME 是把物品存在另一種物品裡的，那就是[儲存單元](items-blocks-machines/storage_cells.md)，共有五個等級，容量逐級遞增。
儲存單元必須放進 <ItemLink id="chest" /> 或 <ItemLink id="drive" /> 才能使用。

<ItemLink id="chest" /> 在單元一放進去時就會顯示裡面的內容，你可以像用 <ItemLink id="minecraft:chest" /> 那樣存取物品，
差別只在於東西實際上是存在儲存單元裡，而不是 <ItemLink id="chest" /> 本身。

<ItemLink id="chest" /> 是認識 ME 概念的好起點，但要真正發揮威力，你得建起一套 [ME 網路](ae2-mechanics/me-network-connections.md)。

## 你的第一套 ME 系統

《應用能源 2》的基本材料與機器都齊了，接下來就能組出你的第一套 ME（物質能源）系統。這會是非常基礎的一套：沒有自動合成，沒有物流，就只是一個好用又能搜尋的倉庫。

<GameScene zoom="6" interactive={true}>
<ImportStructure src="assets/assemblies/tiny_me_system.snbt" />

</GameScene>

*   材料清單：
    * 1 個 <ItemLink id="drive" />
    * 1 個 <ItemLink id="terminal" /> 或 <ItemLink id="crafting_terminal" />
    * 1 個 <ItemLink id="energy_acceptor" />
    * 幾條[線纜](items-blocks-machines/cables.md)，玻璃、包覆或智慧線纜都行，但不能用緻密線纜
    * 幾個[儲存單元](items-blocks-machines/storage_cells.md)，建議用 4k 的，容量與類型數的平衡比較好
    （其實混用 4k 與 1k 再[分區](items-blocks-machines/cell_workbench.md)會更有效率，但那太複雜，這裡先不談）
---
1.  把驅動器放下來。
2.  能量接收器（以及其他好幾種 AE2 [裝置](ae2-mechanics/devices.md)）有方塊與薄板兩種形態，在合成格裡就能互換。如果你的能量接收器是方塊，直接放在驅動器旁邊；如果是薄板，先在驅動器上放一條線纜，再把接收器貼上去。
3.  用你慣用的發電模組，拉一條線纜／管線／導管把電送進能量接收器。
4.  在驅動器上方（或其他跟視線齊高的位置）放一條線纜，把終端機或合成終端機裝上去。
5.  把儲存單元放進驅動器。
6.  收工。
7.  玩玩終端機的各項設定。
8.  沉浸在你至高無上的力量與能耐之中。
9.  然後發現這套網路以整個格局來說其實小得可憐。

### 擴充你的網路

你已經有了基本的倉儲，也能存取它，這是個好開始，不過你大概會想再自動化一些加工流程。

一個很好的例子是在熔爐頂部放一個 <ItemLink id="export_bus" /> 把礦石倒進去，
再在熔爐底部放一個 <ItemLink id="import_bus" /> 把熔好的東西抽出來。

<ItemLink id="export_bus" /> 負責把物品從網路輸出到相連的容器，
<ItemLink id="import_bus" /> 則是把相連容器裡的物品輸入網路。

### 突破上限

到這個階段，你的[裝置](ae2-mechanics/devices.md)大概快到 8 個了。一旦超過 9 個，你就得開始管理[頻道](ae2-mechanics/channels.md)。
大多數裝置（但不是全部）都需要一條頻道才能運作。

網路預設只支援 8 條頻道，超過這個上限後，你得在網路上加一台 <ItemLink id="controller" />，這樣就能大幅擴充規模。
[智慧線纜](items-blocks-machines/cables.md)可以讓你看見頻道在網路裡怎麼繞。剛入門時多用它來理解頻道的行為，如果你紅石和螢光石很多的話更該如此。
