---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: 子網路
---

# 子網路

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/subnet_demonstration.snbt" />

<DiamondAnnotation pos="6.5 2.5 0.5" color="#00ff00">
        物品管線子網路
    </DiamondAnnotation>

<DiamondAnnotation pos="5.5 2.5 0.5" color="#00ff00">
        流體管線子網路
    </DiamondAnnotation>

<DiamondAnnotation pos="4.5 2.5 0.5" color="#00ff00">
        有篩選的破壞面板
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 2.5 0.5" color="#00ff00">
        成形面板子網路
    </DiamondAnnotation>

<DiamondAnnotation pos="2.5 2.5 0.5" color="#00ff00">
        利用介面與儲存匯流排的互動，做成主網路存取得到的
本地附屬倉庫
    </DiamondAnnotation>

<DiamondAnnotation pos="1.5 1.5 0.5" color="#00ff00">
        另一條物品管線子網路，負責把充能好的東西送回樣板供應器
    </DiamondAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

「子網路」的定義相當寬鬆，大致可以說：任何用來輔助主網路、或負責某項小任務的網路都算。
它們通常小到不需要控制器。主要用途有兩種：

*   限制哪些[裝置](../ae2-mechanics/devices.md)能存取哪些倉儲（你不會希望「管線」子網路上的輸入匯流排碰得到主網路的倉儲，
    否則東西會被塞進儲存單元，而不是送到目的地容器）。
*   替主網路省下頻道，例如讓樣板供應器輸出到一個介面，再由該介面接上好幾台機器的儲存匯流排，只用掉 1 條頻道，
    而不是每台機器各放一個樣板供應器、吃掉好幾條頻道。

線纜的顏色和「能不能做出子網路」沒有關係，唯一的作用是不同顏色的線纜彼此不會連接。

子網路可以是

*   一組輸入匯流排加儲存匯流排，像物品管線或流體管線那樣把東西從一個容器搬到另一個容器
*   一組破壞面板加儲存匯流排，讓破壞面板打下來的東西只能放進儲存匯流排，等於替面板加上篩選
*   一組介面加成形面板，讓送進介面的任何東西都被推到成形面板，放置或丟到世界中
*   一套自動製造賽特斯石英的設施，由主網路上的 <ItemLink id="level_emitter" /> 控管
*   一套專用的倉儲系統，透過「儲存匯流排貼在介面上」這個特殊互動供主網路存取，
    用來收農場的產物而不會把主倉庫塞爆
*   諸如此類

做子網路時 <ItemLink id="quartz_fiber" /> 非常好用。它能在網路之間傳電而不把它們連成同一個網路，
讓你不必到處放能量接收器與電力線纜就能替子網路供電。
