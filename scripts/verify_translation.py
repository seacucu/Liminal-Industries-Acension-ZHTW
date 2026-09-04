"""譯文品質檢查（Gate G2 / G3）。

檢查 translation/lang/*.json：
  1. 每個 key 都存在於對應的英文抽出檔
  2. 已宣告完成的章節是否全譯（無遺漏）
  3. 無簡體字
  4. 格式保留：%% 轉義、顏色碼、{image:}
  5. 無未翻譯（值與英文原文完全相同）的殘留
  6. 無多餘空白、無空值

用法：
    python scripts/verify_translation.py [章節名 ...]
    不給章節名則檢查所有已出現在譯文檔中的章節。
"""

import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_QUEST = os.path.join(ROOT, "source", "quest_en_us.json")
EN_KUBEJS = os.path.join(ROOT, "source", "kubejs_names.json")
LANG_DIR = os.path.join(ROOT, "translation", "lang")
KEEP = os.path.join(ROOT, "translation", "keep-as-source.json")
RENAME_TARGETS = os.path.join(ROOT, "source", "rename_targets.json")
CLIENT_JAR = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "libraries",
                          "com", "mojang", "minecraft", "1.20.1",
                          "minecraft-1.20.1-client.jar")
def find_mtp():
    """MTP 的檔名會隨版本與啟停用狀態變動，用樣式尋找而非寫死。"""
    rp = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                      "Liminal Industries Acension", "minecraft", "resourcepacks")
    if not os.path.isdir(rp):
        return None
    for f in sorted(os.listdir(rp)):
        low = f.lower()
        if low.startswith("modstranslationpack") and (
                low.endswith(".zip") or low.endswith(".zip.disabled")):
            return os.path.join(rp, f)
    return None


MTP = find_mtp()

# 只收錄「繁體中文不會用到」的簡化字形，避免誤判兩體皆有的字（后、于、里、面…）
SIMPLIFIED = set(
    "们这说时会来对应关学实现发华战单边过还进远运连达迟选适递邮银错钟铁长门问"
    "间闻阅队阳阶际陆险难页顶项顺须预领颜风飞饭馆马驱验体众优传伟伤价侦俭债倾"
    "偿储儿党兰兴养兽冈军农冲净凤凭击划刘则刚创剑劝办务动劳势勋医卖卫厂厅历压"
    "厌厨县参双变叙号叹吗吨听启员响哑唤喷嘱团园图圆圣场坏块坚坛垄垫壮声壳处备"
    "复够头夹夺奋奖妆娄娱婴嫒孙学宁宝实宠审宪对寻导寿将尔尘尝尴层属岁岂岗峡崭"
    "巩带帅师帐帘帜广庆废开异弃张弹强归当录彻径徕忆态怀怜总恋恳恶恼惊惧惨愿懒"
    "戏户扑执扩扫扬扰抛抢护报担拟拢拣挂挚挠挡挤挥损换据捞捡换掷扬摄摆携摇摊撑"
    "敌数斋断无旧时显晕术机杀杂权条来杨极构枢枪柜标栋栏树样档桥梦检棂椭楼榄槛"
    "横档欢欧歼殁殇残殴毁毕毙毡氢氩汇汉汤沟没沥沦沧沪泪泼泽洁洒浃测浊济浏浑浓"
    "涂涌润涨涩淀渊渐渔渗温湾湿溃滚满滤滨滩滯漤潜潍澜灭灯灵灾灿炉炼烁烂烛烟热"
    "焕爱爷牍牵犊状狈独狮狱猎猪猫玑现琼璎瓒瓮产畅畴疗疟疮疯痒痉痴皱盏盐监盘"  # 註：郁為正體（濃郁），不得列入
    "盖盗盘眍睐瞒矫码砖砚础硕确碍碱礼祢祯祷禄离秃种积称稳穑穷窃窍窜窝窥竖竞笔"
    "笋筑筛筹签简箩篮籁类粜粪紧絷纟纠红纡纣纤纥约级纨纩纪纫纬纭纯纰纱纲纳纵纶"
    "纷纸纹纺纽线绀绁练组绅细织终绉绊绋绌绍绎经绑绒结绔绕绗绘给绚绛络绝绞统绠"
    "绡绢绣绥绦继绨绩绪绫续绮绯绰绱绲绳维绵绶绷绸绺绻综绽绾绿缀缁缂缃缄缅缆缇"
    "缈缉缊缋缌缍缎缏缑缒缓缔缕编缗缘缙缚缛缜缝缟缠缡缢缣缤缥缦缧缨缩缪缫缬缭"
    "缮缯缰缱缲缴缵罗罚罢羁翘耢联聂聋职肃肠肤肮肿胀胁脉脍脏脐脑脓脔脸腊腘腭膑"
    "臜舆舣舰舱艰艳艺节芦苇苏苹范茎茧荆荐荞荡荣荤荧荫药莅莱莲莹莺萝萤营萦萧萨"
    "葱蒋蓝蓟蓣蔷蔹蔺蔼蕲蕴薮藓虏虑虚虫虬虾虿蚀蚁蚂蚕蚝蚬蛊蛎蛏蛮蛰蛱蛲蛳蛴蜕"
    "蜗蜡蝇蝈蝉蝎蝼蝾螀螨蟏衅衔补衬衮袄袆袜袭装裆裢裣裤裥褛褴襁襕见观规觅视觇"
    "览觉觊觋觌觍觎觏觐觑觞触觯訚誉誊讠计订讣认讥讦讧讨让讪讫训议讯记讱讲讳讴"
    "论讵讶讷许讹欣论讼讽设访诀证诂诃评诅识诇诈诉诊诋诌词诎诏诐译诒诓诔试诖诗"
    "诘诙诚诛诜话诞诟诠诡询诣诤该详诧诨诩诪诫诬语诮误诰诱诲诳说诵诶请诸诹诺读"
    "诼诽课诿谀谁谂调谄谅谆谇谈谊谋谌谍谎谏谐谑谒谓谔谕谖谗谘谙谚谛谜谝谞谟谠"
    "谡谢谣谤谥谦谧谨谩谪谫谬谭谮谯谰谱谲谳谴谵谶谷豮贝贞负贠贡财责贤败账货质"
    "贩贪贫贬购贮贯贰贱贲贳贴贵贶贷贸费贺贻贼贽贾贿赀赁赂赃资赅赆赇赈赉赊赋赌"
    "赍赎赏赐赑赒赓赔赕赖赗赘赙赚赛赜赝赞赟赠赡赢赣赪赵赶趋趱趸跃跄跖跞践跶跷"
    "跸跹跻踊踌踪踬踯蹑蹒蹰蹿躏躜躯车轧轨轩轪轫转轭轮软轰轱轲轳轴轵轶轷轸轹轺"
    "轻轼载轾轿辀辁辂较辄辅辆辇辈辉辊辋辌辍辎辏辐辑辒输辔辕辖辗辘辙辚辞辩辫边"
    "辽达迁过运还这进远违连迟迳迹适选逊递逦逻遗遥邓邝邬邮邹邺邻郄郏郐郑郓郦"
    "郧郸酝酦酱酽酾酿释里鉴銮錾钅钆钇针钉钊钋钌钍钎钏钐钑钒钓钔钕钖钗钘钙钚钛"
    "钝钞钟钠钡钢钣钤钥钦钧钨钩钪钫钬钭钮钯钰钱钲钳钴钵钶钷钸钹钺钻钼钽钾钿铀"
    "铁铂铃铄铅铆铈铉铊铋铌铍铎铏铐铑铒铕铖铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铦铧"
    "铨铩铪铫铬铭铮铯铰铱铲铳铴铵银铷铸铹铺铻铼铽链铿销锁锂锃锄锅锆锇锈锉锊锋"
    "锌锍锎锏锐锑锒锓锔锕锖锗错锚锛锜锞锟锠锡锢锣锤锥锦锨锩锪锫锬锭键锯锰锱"
)


# 簡中↔正體的「用詞」差異（不是字形差異，字元檢查完全抓不到）。
# 右欄以原版 zh_tw 的實際用詞為準；verify 會自我驗證這張表。
CN_TERMS = [
    ("幽匿", "伏聆"), ("監守者", "伏守者"), ("下界", "地獄"), ("末地", "終界"),
    ("末影人", "終界使者"), ("生物群系", "生態域"), ("刷怪籠", "生怪磚"),
    ("潛影盒", "界伏盒"), ("凋靈", "凋零"), ("惡魂", "地獄幽靈"),
    ("精準採集", "絲綢之觸"), ("時運", "幸運"), ("信標", "烽火台"),
    ("下界合金", "獄髓"), ("去皮", "剝皮"), ("圓石", "鵝卵石"),
]

notes = []


MODS = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")


def mod_en_us(namespace):
    """從實例的模組 jar 取出某命名空間的 en_us，作為完整度比對基準。"""
    if not os.path.isdir(MODS):
        return None
    target = f"assets/{namespace}/lang/en_us.json"
    for jar in sorted(os.listdir(MODS)):
        if not jar.endswith(".jar"):
            continue
        try:
            with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
                if target in z.namelist():
                    return json.loads(z.read(target).decode("utf-8"))
        except (zipfile.BadZipFile, KeyError, ValueError):
            continue
    return None


def keep_scripts():
    """刻意保留原文（含外語）的 key。"""
    if not os.path.exists(KEEP):
        return set()
    return {k for k in json.load(open(KEEP, encoding="utf-8")) if not k.startswith("_")}


def load_lang():
    out = {}
    for f in sorted(os.listdir(LANG_DIR)):
        if f.endswith(".json"):
            out[f[:-5]] = json.load(open(os.path.join(LANG_DIR, f), encoding="utf-8"))
    return out


def main(argv):
    failures = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    langs = load_lang()

    # 英文基準：任務由 keyify 產出，KubeJS 由 extract 產出，模組命名空間取自 jar
    en = json.load(open(EN_QUEST, encoding="utf-8"))
    if os.path.exists(EN_KUBEJS):
        en.update({k: v["en"] for k, v in
                   json.load(open(EN_KUBEJS, encoding="utf-8")).items()})
    # 原版 minecraft 命名空間的英文
    if os.path.exists(CLIENT_JAR):
        with zipfile.ZipFile(CLIENT_JAR) as z:
            en.update(json.loads(
                z.read("assets/minecraft/lang/en_us.json").decode("utf-8")))
    # 模組未提供、由本包直接補上的 key（其英文即整合包的改名）
    if os.path.exists(RENAME_TARGETS):
        for k, v in json.load(open(RENAME_TARGETS, encoding="utf-8")).items():
            en.setdefault(k, v["pack_name"])

    mod_refs = {}
    for ns in langs:
        if ns in ("ftbquests", "kubejs"):
            continue
        ref = mod_en_us(ns)
        if ref is None:
            notes.append(f"命名空間 {ns} 找不到模組 en_us，無法比對完整度")
        else:
            mod_refs[ns] = ref
            en.update(ref)

    tr = {}
    for ns, d in langs.items():
        tr.update(d)
    print(f"譯文檔 {len(langs)} 個命名空間、{len(tr)} 條\n")

    print("1. key 對應")
    unknown = [k for k in tr if k not in en]
    check("每個 key 都存在於英文抽出檔", not unknown, f"{len(unknown)} 個不存在")
    for k in unknown[:5]:
        print(f"        {k}")

    print("\n2. 章節完整度")
    chapters = argv or sorted({m.group(1) for k in tr
                               if (m := re.match(r"ftbquests\.chapter\.([^.]+)\.", k))})
    for ch in chapters:
        need = {k for k in en if k.startswith(f"ftbquests.chapter.{ch}.")}
        have = need & set(tr)
        check(f"任務章節 {ch} 全譯", have == need,
              f"{len(have)}/{len(need)}" + (f"，缺 {sorted(need - have)[:2]}" if have != need else ""))
    for ns, ref in sorted(mod_refs.items()):
        mine = set(langs[ns])
        pct = len(mine & set(ref)) * 100 // max(1, len(ref))
        print(f"  [INFO] 命名空間 {ns}：本包提供 {len(mine)} 條 / 模組 en_us 共 {len(ref)} 條"
              f"（{pct}%，未涵蓋者沿用模組自帶譯文）")

    print("\n3. 簡體字")
    # 清單自我校正：凡出現在原版 zh_tw 的字，必定不是「簡體專用」，予以剔除
    simp = set(SIMPLIFIED)
    corpus = set()
    _vp = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_zh_tw.json")
    if os.path.exists(_vp):
        corpus |= set("".join(json.load(open(_vp, encoding="utf-8")).values()))
    # MTP 是釘宮翻譯組維護的正體語料，用它擴大校正基礎。
    # 但 MTP 本身也有零星簡體殘留（自动拾取、温帶樹林…），
    # 因此要求出現 5 條以上才採信 —— 偶發一兩次的多半是錯字而非正體用法。
    if MTP and os.path.exists(MTP):
        import collections
        freq = collections.Counter()
        with zipfile.ZipFile(MTP) as z:
            for n in z.namelist():
                if not n.endswith("/lang/zh_tw.json"):
                    continue
                try:
                    d = json.loads(z.read(n).decode("utf-8"))
                except ValueError:
                    continue
                for x in d.values():
                    if isinstance(x, str):
                        freq.update(set(x))
        corpus |= {c for c, n in freq.items() if n >= 5}
    if not (MTP and os.path.exists(MTP)):
        # 語料縮水會讓檢查誤報，必須出聲而非靜默降級
        notes.append("找不到 MTP，簡體字檢查僅以原版 zh_tw 為語料，可能誤報")
    _fp = simp & corpus
    simp -= corpus
    if _fp:
        print(f"        （清單自我校正：剔除 {len(_fp)} 個誤收字 "
              f"{''.join(sorted(_fp))}——原版 zh_tw 或 MTP 有在用）")
    bad = {k: sorted(set(v) & simp) for k, v in tr.items() if set(v) & simp}
    check("無簡體字", not bad, f"{len(bad)} 條含簡體")
    for k, chars in list(bad.items())[:5]:
        print(f"        {k}: {''.join(chars)}")

    print("\n3b. 簡中「用詞」（字元檢查抓不到的）")
    vanilla = os.path.join(ROOT, "_workspace", "build", "verify", "vanilla_zh_tw.json")
    if os.path.exists(vanilla):
        vals = "\n".join(json.load(open(vanilla, encoding="utf-8")).values())
        # 自我驗證：右欄必須真的出現在原版 zh_tw，左欄必須不出現
        broken = [f"{cn}→{tw}" for cn, tw in CN_TERMS
                  if cn != tw and (tw not in vals or cn in vals)]
        check("對照表本身與原版 zh_tw 相符", not broken, f"{len(broken)} 組有問題：{broken[:3]}")
        bad_terms = {}
        for k, v in tr.items():
            for cn, tw in CN_TERMS:
                if cn != tw and cn in v:
                    bad_terms.setdefault(k, []).append(f"「{cn}」應為「{tw}」")
        check("無簡中用詞", not bad_terms, f"{len(bad_terms)} 條")
        for k, msgs in list(bad_terms.items())[:5]:
            print(f"        {k}: {'、'.join(msgs)}")
    else:
        # 不可靜默略過：這是唯一能抓到「幽匿」這類簡中用詞的檢查
        check("原版 zh_tw 基準存在", False,
              "缺 build/verify/vanilla_zh_tw.json，請先跑 scripts/fetch_vanilla_lang.py")

    print("\n3c. 非預期文字系統")
    # 譯文混入西里爾、希臘、日文假名、韓文等，多半是輸入或複製錯誤
    foreign = re.compile("[Ѐ-ӿͰ-Ͽ֐-׿"
                         "؀-ۿ぀-ヿ가-힯]")
    allow = keep_scripts()
    fbad = {k: sorted(set(foreign.findall(v))) for k, v in tr.items()
            if foreign.search(v) and k not in allow}
    check("無非預期文字系統", not fbad, f"{len(fbad)} 條")
    for k, ch in list(fbad.items())[:5]:
        print(f"        {k}: {''.join(ch)} <- {tr[k][:40]}")

    # 夾在中文之間、且前後無空白的拉丁字母，多半是打字時混入的外文詞
    #（JEI、ME、Create 這類專名通常前後有空白或標點，故不會誤判）
    # 需含小寫字母 —— 全大寫多半是 TNT、RF、TAB 這類正常縮寫
    sandwiched = re.compile("[一-鿿][A-Za-z]*[a-z][A-Za-z]*[一-鿿]")
    sbad = {k: sandwiched.findall(v) for k, v in tr.items()
            if sandwiched.search(v) and k not in allow}
    check("無夾在中文裡的拉丁字詞", not sbad, f"{len(sbad)} 條")
    for k, m in list(sbad.items())[:5]:
        print(f"        {k}: {m} <- {tr[k][:40]}")

    print("\n4. 格式保留")
    pct_bad = [k for k, v in tr.items()
               if k in en and ("%%" in en[k]) != ("%%" in v)]
    check("%% 轉義與原文一致", not pct_bad, f"{len(pct_bad)} 條不符")
    for k in pct_bad[:5]:
        print(f"        {k}\n          原: {en[k]}\n          譯: {tr[k]}")

    colour_bad = [k for k, v in tr.items() if k in en
                  and set(re.findall(r"&[0-9a-fk-or]", en[k]))
                  != set(re.findall(r"&[0-9a-fk-or]", v))]
    check("顏色碼保留", not colour_bad, f"{len(colour_bad)} 條不符")
    for k in colour_bad[:5]:
        print(f"        {k}\n          原: {en[k]}\n          譯: {tr[k]}")

    img_bad = [k for k, v in tr.items() if "{image:" in v]
    check("譯文不含 {image:}（應留在骨架）", not img_bad, f"{len(img_bad)} 條")

    print("\n5. 殘留與雜訊")
    keep = set()
    if os.path.exists(KEEP):
        keep = {k for k in json.load(open(KEEP, encoding="utf-8")) if not k.startswith("_")}
    same = [k for k, v in tr.items()
            if k in en and v.strip() == en[k].strip() and k not in keep]
    check("無與英文完全相同的殘留", not same,
          f"{len(same)} 條（另有 {len(keep)} 條列於 keep-as-source.json，刻意不譯）")
    for k in same[:5]:
        print(f"        {k} = {tr[k]}")

    empty = [k for k, v in tr.items() if not v.strip()]
    check("無空值", not empty, f"{len(empty)} 條")
    ws = [k for k, v in tr.items() if v != v.strip()]
    check("無前後多餘空白", not ws, f"{len(ws)} 條")

    print("\n" + ("全部通過。" if not failures else f"失敗 {len(failures)} 項：{failures}"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
