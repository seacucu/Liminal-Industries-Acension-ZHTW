---
navigation:
  parent: example-setups/example-setups-index.md
  title: 處理器自動化
  icon: logic_processor
---

# 處理器生產的自動化

自動化[處理器](../items-blocks-machines/processors.md)的方法很多，這只是其中一種。

這套大致的佈局，換成任何物品物流管線、導管、管道或不管那個模組怎麼叫它的東西都做得出來，
只要它能設篩選就行。

![The Process FLow Diagram](../assets/diagrams/processor_flow_diagram.png)

以下詳述只用 AE2、以[「管線」子網路](pipe-subnet.md)實作的作法。

要注意的是，這套設施用到了 <ItemLink id="pattern_provider" />，所以是設計來併進你的[自動合成](../ae2-mechanics/autocrafting.md)系統的。
如果你只是想單獨把處理器生產自動化，把樣板供應器換成另一個木桶，直接把材料放進上面那個木桶即可。

這套作法剛好也向下相容於舊版 AE2，因為就算 <ItemLink id="inscriber" /> 是分面的，
管線子網路照樣會從正確的面進料與取料。

## 關於樣板編碼的一課

你要編碼的[樣板](../items-blocks-machines/patterns.md)，**往往和你在 JEI 裡看到的不一樣**，
也和你按下 JEI 的 + 按鈕所產生的不一樣。以這個例子來說，JEI 會產生兩份分開的樣板：
一份做印刷元件、一份做最終組裝，而且印刷元件那份還會把[模具](../items-blocks-machines/presses.md)算進材料。
那不是我們要的，因為這套設施不是那樣運作的。我們要的是一份「原料進、成品出」的樣板；
模具本來就已經裝在壓印機裡了，不該放進樣板。

---

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/processor_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="5 1 0" max="6 2 1" thickness=".05">
        (1) 樣板供應器：維持預設設定，放入對應的處理樣板。

        <Row>
            ![Logic Pattern](../assets/diagrams/logic_pattern_small.png)
            ![Calculation Pattern](../assets/diagrams/calculation_pattern_small.png)
            ![Engineering Pattern](../assets/diagrams/engineering_pattern_small.png)
        </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.7 2 0" max="5 3 1" thickness=".05">
        (2) 儲存匯流排 #1：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="4.3 2 1" thickness=".05">
        (3) 輸出匯流排 #1：篩選設為矽，裝有 2 張加速卡
        <Row><ItemImage id="silicon" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="4.3 3 1" thickness=".05">
        (4) 輸出匯流排 #2：篩選設為金錠，裝有 2 張加速卡
        <Row><ItemImage id="minecraft:gold_ingot" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="4.3 4 1" thickness=".05">
        (5) 輸出匯流排 #3：篩選設為賽特斯石英水晶，裝有 2 張加速卡
        <Row><ItemImage id="certus_quartz_crystal" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 6 0" max="4.3 5 1" thickness=".05">
        (6) 輸出匯流排 #4：篩選設為鑽石，裝有 2 張加速卡
        <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 0" max="2 2 1" thickness=".05">
        (7) 輸出匯流排 #5：篩選設為紅石粉，裝有 2 張加速卡
        <Row><ItemImage id="minecraft:redstone" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="3 2 1" thickness=".05">
        (8) 壓印機 #1：維持預設設定。裝有矽模具與 4 張加速卡
        <Row><ItemImage id="silicon_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 3 0" max="3 4 1" thickness=".05">
        (9) 壓印機 #2：維持預設設定。裝有邏輯模具與 4 張加速卡
        <Row><ItemImage id="logic_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="3 5 1" thickness=".05">
        (10) 壓印機 #3：維持預設設定。裝有計算模具與 4 張加速卡
        <Row><ItemImage id="calculation_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="3 6 1" thickness=".05">
        (11) 壓印機 #4：維持預設設定。裝有工程模具與 4 張加速卡
        <Row><ItemImage id="engineering_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 0" max="1 3 1" thickness=".05">
        (12) 壓印機 #5：維持預設設定。裝有 4 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 2 0" max="3 1 1" thickness=".05">
        (13) 輸入匯流排 #1：維持預設設定，裝有 2 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 4 0" max="3 3 1" thickness=".05">
        (14) 輸入匯流排 #2：維持預設設定，裝有 2 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 5 0" max="3 4 1" thickness=".05">
        (15) 輸入匯流排 #3：維持預設設定，裝有 2 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 6 0" max="3 5 1" thickness=".05">
        (16) 輸入匯流排 #4：維持預設設定，裝有 2 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 3 0" max="1 3.3 1" thickness=".05">
        (17) 儲存匯流排 #2：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1.7 0" max="1 2 1" thickness=".05">
        (18) 儲存匯流排 #3：維持預設設定。
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 0" max="0.7 3 1" thickness=".05">
        (19) 輸入匯流排 #5：維持預設設定，裝有 2 張加速卡
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="5 0.7 0" max="6 1 1" thickness=".05">
        (20) 儲存匯流排 #4：維持預設設定。
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.3 2.7 0.3" max="3.7 3 0.7" thickness=".05">
        石英纖維替三台壓印機供電，因為壓印機的行為和線纜相同，會傳導能量
  </BoxAnnotation>

<DiamondAnnotation pos="7 1.5 0.5" color="#00ff00">
        通往主網路
    </DiamondAnnotation>

  <IsometricCamera yaw="185" pitch="5" />
</GameScene>

## 設定

* <ItemLink id="pattern_provider" />（1）維持預設設定，放入對應的 <ItemLink id="processing_pattern" />。
  注意樣板是「原料直接到成品處理器」，**不要**把[模具](../items-blocks-machines/presses.md)放進去。

  ![Logic Pattern](../assets/diagrams/logic_pattern.png)
  ![Calculation Pattern](../assets/diagrams/calculation_pattern.png)
  ![Engineering Pattern](../assets/diagrams/engineering_pattern.png)

* <ItemLink id="storage_bus" />（2、17、18、20）維持預設設定。
* <ItemLink id="export_bus" />（3 到 7）篩選各設為對應的材料，並裝有 2 張 <ItemLink id="speed_card" />。
    <Row>
      <ItemImage id="silicon" scale="2" />
      <ItemImage id="minecraft:gold_ingot" scale="2" />
      <ItemImage id="certus_quartz_crystal" scale="2" />
      <ItemImage id="minecraft:diamond" scale="2" />
      <ItemImage id="minecraft:redstone" scale="2" />
    </Row>
* <ItemLink id="import_bus" />（13 到 16、19）維持預設設定，並裝有 2 張 <ItemLink id="speed_card" />。
* <ItemLink id="inscriber" /> 維持預設設定，各裝上對應的[模具](../items-blocks-machines/presses.md)
   與 4 張 <ItemLink id="speed_card" />。
   <Row>
     <ItemImage id="silicon_press" scale="2" />
     <ItemImage id="logic_processor_press" scale="2" />
     <ItemImage id="calculation_processor_press" scale="2" />
     <ItemImage id="engineering_processor_press" scale="2" />
   </Row>

## 運作原理

1. <ItemLink id="pattern_provider" /> 把材料推進木桶。
2. 第一條[管線子網路](pipe-subnet.md)（橙色）把矽、紅石粉，以及對應處理器所需的材料
   （金錠、賽特斯石英水晶或鑽石）從木桶裡拉出來，送進對應的 <ItemLink id="inscriber" />。
3. 前四台 <ItemLink id="inscriber" /> 做出 <ItemLink id="printed_silicon" />，以及 <ItemLink id="printed_logic_processor" />、
   <ItemLink id="printed_calculation_processor" /> 或 <ItemLink id="printed_engineering_processor" />。
4. 第二與第三條[管線子網路](pipe-subnet.md)（綠色）把印好的電路從前四台 <ItemLink id="inscriber" /> 取出，
    送進第五台負責最終組裝的 <ItemLink id="inscriber" />。
5. 第五台 <ItemLink id="inscriber" /> 組裝出[處理器](../items-blocks-machines/processors.md)。
6. 第四條[管線子網路](pipe-subnet.md)（紫色）把處理器放進樣板供應器，也就送回了主網路。
