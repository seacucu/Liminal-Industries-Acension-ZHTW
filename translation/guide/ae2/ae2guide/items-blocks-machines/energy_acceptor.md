---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: 能量接收器
  icon: energy_acceptor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_acceptor
---

# 能量接收器

<Row gap="20">
<BlockImage id="energy_acceptor" scale="8" /> 

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
</GameScene>
</Row>

能量接收器把其他科技模組常見的能量形式，轉換成 AE2 內部使用的[能量](../ae2-mechanics/energy.md)單位 AE。
<ItemLink id="controller" /> 雖然也做得到，但控制器的每一面都很珍貴，所以通常還是用能量接收器比較好。

Forge Energy 與 TechReborn Energy 的換算比例是

*   2 FE = 1 AE（Forge）
*   1 E  = 2 AE（Fabric）

轉換速度完全取決於你的網路能儲存多少 AE，原因在[這一頁](../ae2-mechanics/energy.md)有說明。

## 變體

能量接收器有兩種變體：一般與薄板／[線纜附件](../ae2-mechanics/cable-subparts.md)，後者可以讓某些配置更緊湊。

兩種形態可以在合成格裡互換。

## 配方

<RecipeFor id="energy_acceptor" />

<RecipeFor id="cable_energy_acceptor" />
