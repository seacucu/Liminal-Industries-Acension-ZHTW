---
navigation:
  title: 訣竅與技巧
  position: 20
---

# 訣竅與技巧

一堆零散的小建議

* 移除 Optifine
* 指南裡的場景只要有縮放與標註顯示／隱藏按鈕，就可以旋轉與拉近
* 網路盡量保持樹狀，避免出現迴路
* 整格的[裝置](ae2-mechanics/devices.md)以 8 個為一組，除非你很清楚[頻道](ae2-mechanics/channels.md)
  在網路裡是怎麼繞的
* 選定一種木材，所有[樣板](items-blocks-machines/patterns.md)都用它。是啦，樣板開啟替代材料有時候也管用，但全部統一用同一種木材可以省掉非常多麻煩。
* 在 <ItemLink id="pattern_access_terminal" /> 裡把[樣板](items-blocks-machines/patterns.md)縱向排開／
  把樣板分散到不同的[供應器](items-blocks-machines/pattern_provider.md)上，這樣配方才能平行處理。
* 加一顆[能量電池](items-blocks-machines/energy_cells.md)，網路才扛得住瞬間的耗電尖峰。
* <ItemLink id="condenser" /> 裡可以丟水
* 保持網路清爽最好的辦法，就是別把劍、盔甲這類雜七雜八的怪物掉落物塞進去。附魔與耐久的每一種組合都會佔掉一個[類型](ae2-mechanics/bytes-and-types.md)。
* 要送回[處理樣板](items-blocks-machines/patterns.md)的成品時，必須觸發一次「物品進入系統」的事件，
  例如經由 <ItemLink id="import_bus" />、<ItemLink id="interface" /> 或 <ItemLink id="pattern_provider" /> 的回收格，
  不能只是把成品用管線送進一個貼著 <ItemLink id="storage_bus" /> 的儲物箱。
* 別忘了指南裡的場景只要有縮放與標註顯示／隱藏按鈕，就可以旋轉與拉近
* <ItemLink id="pattern_provider" /> 只會推出湊滿整批的配方材料，而且只從單一面推出。這在確保機器不會收到半批材料時很好用，
  但有時候你會希望材料送往多個地方。
  這時可以改用 <ItemLink id="interface" />，把它做成一條[「管線」子網路](example-setups/pipe-subnet.md)，
  或是利用它能同時存放多種不同物品堆疊、流體、化學品的特性，當成中繼的儲物箱或儲罐使用。
* 指南裡的場景只要有縮放與標註顯示／隱藏按鈕，就可以拉近與旋轉
