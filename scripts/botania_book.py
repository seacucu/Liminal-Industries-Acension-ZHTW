"""修正植物魔法辭典（Lexica Botania）內文的排版、巨集與術語問題。

辭典的 book.json 設了 i18n:true，246 個條目、11 個分類的標題與內文全都是
語系檔的鍵值，所以整本書可以純靠資源包覆蓋，不必動 Patchouli 書本檔案。

本腳本處理 botania_substitute.py 開頭明確排除的那一批：

  1. 硬換行空格   舊版辭典是固定寬度排版，譯者每十餘字手動塞一個半形空白。
                  Patchouli 改用原版字型排版器後中文本來就會自動斷行，
                  這些空白全變成句子中間的莫名空隙。
  2. 半形句讀     全書用 , 和 . 斷句（半形 2,475 個對全形 388 個）。
  3. 遺失的連結   譯文把 $(l:…)…$(/l) 整個吃掉，書裡的跳轉沒了。
  4. 遺失的上色   $(item)／$(thing) 同理。
  5. 分段與未譯   $(p) 數量不符、殘留舊版英文、術語與品名不同步。

輸入：Botania jar 的 en_us/zh_tw ＋ translation/lang/botania.json
      （即 botania_compose + botania_substitute 的產物）
輸出：併回 translation/lang/botania.json，書本鍵全數收進本包

人工資料：
  translation/botania-book-terms.json   本包對 Botania 術語的決定（最高優先，
                                        會回頭改品名與生物名）
  translation/botania-book-manual.json  逐條覆寫的譯文（重譯、梗、破折號改寫）

改寫過的每一條都會寫進 _workspace/build/botania/book-changes.json 供查驗。
"""

import json
import os
import re
import sys
import zipfile

# botania_substitute 的術語表在這裡再跑一次：它處理原始 zh_tw 時，被硬換行
# 切成 $(item)瑪$(0)$(item)那發射器$(0) 的詞它掃不到，狀態機重排之後
# 才浮出來。共用同一份表，兩邊不會走音。
from botania_substitute import SUBS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG = os.path.join(ROOT, "translation", "lang", "botania.json")
TERMS = os.path.join(ROOT, "translation", "botania-book-terms.json")
MANUAL = os.path.join(ROOT, "translation", "botania-book-manual.json")
KEEP = os.path.join(ROOT, "translation", "keep-as-source.json")
RENAMES = os.path.join(ROOT, "translation", "renames.json")
NAMES = os.path.join(ROOT, "_workspace", "build", "botania", "names.json")
REPORT = os.path.join(ROOT, "_workspace", "build", "botania", "book-changes.json")
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")

BOOK_PREFIXES = ("botania.page.", "botania.entry.", "botania.tagline.",
                 "botania.category.", "botania.challenge.", "botania.subtitle.",
                 "botania.landing")

# 花朵的 reference 與骰子的詩句也會印在辭典頁面上，是散文不是品名，
# 所以同樣要做標點正規化。botania_compose 只管品名，不碰這些。
FLAVOUR_SUFFIXES = (".reference", ".poem0", ".poem1", ".poem2", ".poem3")

MACRO = re.compile(r"\$\([^)]*\)")

# 全形化對照。半形句讀貼著中文時才換，數值與英文句子不動。
PUNCT = {",": "，", ".": "。", ";": "；", ":": "：", "!": "！", "?": "？"}
CJKP = "，。、；：？！（）「」『』…—％·《》～"

# 書內文仍在用的舊譯名 → 現行品名。
# (舊, 新, 限定鍵前綴)。限定為 None 代表全書套用；長詞必須排在短詞前面。
#
# 這批不是風格偏好，是同一個東西在物品欄叫一個名字、在辭典裡叫另一個名字。
# 上色巨集被硬換行切斷過（$(item)瑪$(0)$(item)那發射器$(0)），所以
# botania_substitute 的字串代換掃不到，得等顏色狀態機把詞接回來才看得見，
# 也因此本表排在 serialize(flatten(...)) 之後。
DRIFT = [
    # 品名改過，書裡沒跟著改
    ("微光活木", "螢光活木", None),
    ("微光發射器", "光導發射器", None),
    ("探測微光", "探測光導", None),
    # Shimmering=微光 與 Luminizer=微光 撞名，只有光導那幾頁能換
    ("微光", "光導", "botania.page.luminizerTransport"),
    ("微光", "光導", "botania.entry.luminizerTransport"),
    ("阿茲勒赫瓷磚", "葡式花磚", None),
    ("行星項鏈", "魔力環繞器", None),
    ("裂活石磚", "裂紋活石磚", None),
    ("苔活石磚", "青苔活石磚", None),
    ("苔活木板", "青苔活木材", None),
    ("框邊活木板", "框邊活木材", None),
    ("框紋活木板", "花紋框邊活木材", None),
    ("框邊活石磚", "浮雕活石磚", None),
    ("活木板", "活木材", None),
    ("紅色石英", "紅石英", None),
    ("煙熏石英", "煙燻石英", None),
    ("熏香石英", "薰香石英", None),
    ("熏香", "薰香", None),
    # 辭典內文用的舊品名
    ("紅石瑪那發射器", "魔力發射器（紅石）", None),
    ("紅石魔力發射器", "魔力發射器（紅石）", None),
    ("花瓣藥劑台", "花藥台", None),
    ("瓶裝終界空氣", "閾限空氣瓶", None),
    ("終界空氣", "閾限空氣", None),
    ("磁化戒指", "磁化指環", None),
    ("磁化透鏡", "魔力透鏡：磁化", None),
    ("引燃透鏡", "魔力透鏡：引燃", None),
    ("火花升級", "火花增幅", None),
    ("魔力探測器", "魔力檢測器", None),
    ("堅毅之藤", "堅毅之籐", None),
    ("熱爆花", "熵花", None),
    ("移殼杆", "移殼桿", None),
    ("浮空花朵", "浮空花", None),
    ("魔力水晶", "魔力塔柱", None),
    ("煉金催化", "煉金催化器", None),
    ("展示框", "物品展示框", None),
    ("煤塊", "煤炭方塊", None),
    # 章節名。書裡至少四種寫法，統一成目錄上的分類名，讀者才找得到那一章。
    ("產能類花朵", "產能類植物", None),
    ("功能性或產能花朵", "功能類或產能類植物", None),
    ("產能類花", "產能類植物", None),
    ("產能花", "產能類植物", None),
    ("功能類花", "功能類植物", None),
    ("功能植物", "功能類植物", None),
    ("功能花", "功能類植物", None),
    ("神秘設備", "神秘工具", None),
    ("微光石木板", "微光木材", None),
    # 錯字與兩岸用語。這批是 verify_translation 的簡中術語表抓出來的，
    # 右欄一律取原版 zh_tw 的寫法。
    ("緩沖", "緩衝", None),
    ("搜索", "搜尋", None),
    ("刷怪塔", "生怪塔", None),
    ("圓石", "鵝卵石", None),
    ("音符盒", "音階盒", None),
    ("浮冰", "冰磚", None),
    ("中毒", "劇毒", None),
    ("木板", "木材", None),
    ("MOD", "模組", None),          # 全書只有四處，一律用中文
    # 這兩條的「精靈」英文是 Pixie，不是 Elf，只能逐鍵換
    ("精靈", "妖精", "botania.tagline.pixieRing"),
    ("精靈之舞", "妖精之舞", "botania.tagline.gaiaRitualHardmode"),
]



# ---------------------------------------------------------------- 字元工具
def is_cjk(c):
    return c is not None and "㐀" <= c <= "鿿"


def is_cjkp(c):
    return c is not None and c in CJKP


def cjkish(c):
    return is_cjk(c) or is_cjkp(c)


def split_macros(s):
    """切成 [(是否巨集, 片段), …]，巨集內部一律不動。"""
    out, i = [], 0
    for m in MACRO.finditer(s):
        if m.start() > i:
            out.append((False, s[i:m.start()]))
        out.append((True, m.group(0)))
        i = m.end()
    if i < len(s):
        out.append((False, s[i:]))
    return out


def to_cells(s):
    """純文字字元展開成 [字元, 所屬片段序號]，巨集不佔格。

    這樣取鄰居時會自動跨過巨集，$(0) 前後的標點與空白才判得準。
    """
    parts = split_macros(s)
    cells = []
    for i, (is_macro, text) in enumerate(parts):
        if is_macro:
            continue
        for c in text:
            cells.append([c, i])
    return parts, cells


def from_cells(parts, cells):
    """把處理過的字元收回原來的片段順序。"""
    buf = {}
    for c, i in cells:
        buf.setdefault(i, []).append(c)
    out = []
    for i, (is_macro, text) in enumerate(parts):
        out.append(text if is_macro else "".join(buf.get(i, [])))
    return "".join(out)


def peek(cells, i, step):
    """往 step 方向找第一個非空白字元，用來判斷「實際的」鄰居。"""
    j = i + step
    while 0 <= j < len(cells) and cells[j][0] == " ":
        j += step
    return cells[j][0] if 0 <= j < len(cells) else None


# ---------------------------------------------------------------- 字元層修正
def fix_ellipsis(cells):
    """半形省略號改全形。三個以上的點一律收成兩個 …。"""
    out, i, n = [], 0, 0
    while i < len(cells):
        if (cells[i][0] == "." and i + 2 < len(cells)
                and cells[i + 1][0] == "." and cells[i + 2][0] == "."):
            j = i
            while j < len(cells) and cells[j][0] == ".":
                j += 1
            out.append(["…", cells[i][1]])
            out.append(["…", cells[i][1]])
            n += 1
            i = j
        else:
            out.append(cells[i])
            i += 1
    return out, n


def fix_split_dash(cells):
    """硬換行把破折號 —— 切成 — — 的，接回去。"""
    out, i, n = [], 0, 0
    while i < len(cells):
        if (cells[i][0] == "—" and i + 2 < len(cells)
                and cells[i + 1][0] == " " and cells[i + 2][0] == "—"):
            out.append(cells[i])
            n += 1
            i += 1                      # 丟掉空白，下一圈接上第二個破折號
        else:
            out.append(cells[i])
            i += 1
    return out, n


def fix_pairs(cells):
    """成對的半形括號與雙引號，在中文語境下改成全形與直角引號。"""
    n = 0
    stack = []
    for i, cell in enumerate(cells):
        if cell[0] == "(":
            stack.append(i)
        elif cell[0] == ")" and stack:
            a = stack.pop()
            inner = "".join(x[0] for x in cells[a + 1:i])
            before = peek(cells, a, -1)
            if any(is_cjk(x) for x in inner) or cjkish(before):
                cells[a][0] = "（"
                cell[0] = "）"
                n += 1
    quotes = [i for i, cell in enumerate(cells) if cell[0] == '"']
    if len(quotes) % 2 == 0:
        for a, b in zip(quotes[0::2], quotes[1::2]):
            inner = "".join(x[0] for x in cells[a + 1:b])
            near = is_cjk(peek(cells, a, -1)) or is_cjk(peek(cells, b, 1))
            if any(is_cjk(x) for x in inner) or near:
                cells[a][0] = "「"
                cells[b][0] = "」"
                n += 1
    return cells, n


def fix_punct(cells):
    """半形句讀貼著中文時改全形；小數、版本號、純英文句子不動。"""
    n = 0
    for i, cell in enumerate(cells):
        if cell[0] not in PUNCT:
            continue
        if cjkish(peek(cells, i, -1)) or cjkish(peek(cells, i, 1)):
            cell[0] = PUNCT[cell[0]]
            n += 1
    return cells, n


def fix_hyphen(cells):
    """中文句中被當破折號用的半形連字號，改成冒號。"""
    n = 0
    for i, cell in enumerate(cells):
        if cell[0] != "-":
            continue
        if cjkish(peek(cells, i, -1)) and cjkish(peek(cells, i, 1)):
            cell[0] = "："
            n += 1
    return cells, n


def fix_western_spacing(cells):
    """中文與夾在其中的西文詞、數字之間補一個空白。

    拉丁字母只處理含小寫的詞（Baubles、Kickstarter、ClariS），與
    verify_translation 判定「夾在中文裡的拉丁字詞」同一條線；TNT、RF、SS
    這種全大寫縮寫不動。數字則一律補，書裡本來就是「約 30 秒」與
    「每秒2次」兩種寫法並存。
    """
    out, i, n = [], 0, 0
    while i < len(cells):
        c = cells[i][0]
        if not c.isascii() or not (c.isalpha() or c.isdigit()):
            out.append(cells[i])
            i += 1
            continue
        digits = c.isdigit()
        j = i
        while j < len(cells) and cells[j][0].isascii() and (
                cells[j][0].isdigit() if digits else cells[j][0].isalpha()):
            j += 1
        word = "".join(x[0] for x in cells[i:j])
        if digits or any(x.islower() for x in word):
            # 空白要掛在鄰居那一段。掛進西文那一段的話，
            # $(thing)15$(0)種 會變成 $(thing) 15 $(0)種，空白跑進上色裡。
            if out and is_cjk(out[-1][0]):
                out.append([" ", out[-1][1]])
                n += 1
            out.extend(cells[i:j])
            if j < len(cells) and is_cjk(cells[j][0]):
                out.append([" ", cells[j][1]])
                n += 1
        else:
            out.extend(cells[i:j])
        i = j
    return out, n


def fix_dimensions(cells):
    """25x25 這種尺寸寫法改成全形乘號。"""
    n = 0
    for i, cell in enumerate(cells):
        if cell[0] not in "xX" or not (0 < i < len(cells) - 1):
            continue
        if not (cells[i - 1][0].isdigit() and cells[i + 1][0].isdigit()):
            continue
        left = i - 1
        while left > 0 and cells[left - 1][0].isdigit():
            left -= 1
        if "".join(x[0] for x in cells[left:i]) == "0":
            continue                    # 0x1a4 是十六進位，不是 0×1a4
        cell[0] = "×"
        n += 1
    return cells, n


def fix_spaces(cells):
    """去掉舊版固定寬度排版留下的硬換行空白。

    只有兩側都是中文字或中文標點才刪；中文與拉丁字母、數字之間的空白是
    正常的排版留白，保留。連續空白一律收成一個。
    """
    out, n = [], 0
    for i, cell in enumerate(cells):
        if cell[0] != " ":
            out.append(cell)
            continue
        prev = out[-1][0] if out else None
        nxt = cells[i + 1][0] if i + 1 < len(cells) else None
        if nxt == " ":                            # 連續空白只留最後一個
            n += 1
            continue
        if prev is None or nxt is None or (cjkish(prev) and cjkish(nxt)):
            n += 1
            continue
        if is_cjkp(prev) or is_cjkp(nxt):     # 全形標點自帶留白
            n += 1
            continue
        out.append(cell)
    while out and out[0][0] == " ":
        out.pop(0)
        n += 1
    while out and out[-1][0] == " ":
        out.pop()
        n += 1
    return out, n


def typography(s, _depth=0):
    """跑完所有字元層級的修正。

    各道之間會互相影響：句讀全形化之後，原本判不出是中文語境的括號才判得出來
    （「，(……)」要先變成「，」才輪得到括號）。所以跑到不再變動為止。
    """
    parts, cells = to_cells(s)
    counts = {}
    cells, counts["省略號"] = fix_ellipsis(cells)
    cells, counts["破折號"] = fix_split_dash(cells)
    cells, counts["成對符號"] = fix_pairs(cells)
    cells, counts["半形句讀"] = fix_punct(cells)
    cells, counts["連字號"] = fix_hyphen(cells)
    cells, counts["硬換行空格"] = fix_spaces(cells)
    cells, counts["尺寸乘號"] = fix_dimensions(cells)
    cells, counts["中外文留白"] = fix_western_spacing(cells)
    out = from_cells(parts, cells)
    if out != s and _depth < 4:
        again, more = typography(out, _depth + 1)
        for name, n in more.items():
            counts[name] = counts.get(name, 0) + n
        return again, counts
    return out, counts


# ---------------------------------------------------------------- 巨集層修正
SPAN = re.compile(r"\$\(l:([^)]*)\)(.*?)\$\(/l\)|\$\((item|thing)\)(.*?)\$\(0\)",
                  re.S)
DOUBLE_P = re.compile(r"(?:\$\(p\)){2,}")


def build_drift(key, extra=()):
    """組出這個鍵適用的舊譯名對照，以及一次掃完的比對式。

    改名的目標詞自己也放進對照表映射回自己，長詞優先比對，
    「煉金催化 → 煉金催化器」才不會把已經正確的「煉金催化器」接成「器器」。
    """
    table = {}
    for old, new in extra:
        table[old] = new
        table.setdefault(new, new)
    for old, new, scope in DRIFT:
        if scope and not key.startswith(scope):
            continue
        table[old] = new
        table.setdefault(new, new)
    if not table:
        return None, None
    pattern = "|".join(re.escape(w) for w in
                       sorted(table, key=len, reverse=True))
    return table, re.compile(pattern)


def apply_drift(key, text, extra=()):
    table, pattern = build_drift(key, extra)
    if not table:
        return text, 0
    n = 0

    def swap(m):
        nonlocal n
        new = table[m.group(0)]
        if new != m.group(0):
            n += 1
        return new

    return pattern.sub(swap, text), n


def collapse_double_p(s):
    """舊版譯文刪掉整段後常留下連續的 $(p)，收成一個。"""
    return DOUBLE_P.subn("$(p)", s)


# --- 顏色與連結狀態機 -----------------------------------------------------
# 舊版辭典是逐行排版的，每一行都得自己重下一次顏色碼，轉成 Patchouli 之後
# 就留下各種交錯的爛攤子：
#     $(thing)$(thing)魔力$(0)流失$(0)   魔力上色、流失沒有
#     $(item)玻璃$(item)小瓶$(0)$(0)     畫出來對，但巨集重複
#     $(item)$(l:…)$(item)源質$(0)$(/l)鋼$(0)   連結只蓋住半個詞
# 用正規表示式逐一去補是補不完的。改成把字串攤平成「每個字現在是什麼顏色、
# 屬於哪個連結」，改完再依狀態重新輸出，寫法自然就是最簡的那一種。
COLOUR_TOKEN = {"$(0)": None, "$(item)": "item", "$(thing)": "thing"}
COLOUR_CODE = re.compile(r"^\$\((?:[0-9a-f]|#[0-9a-fA-F]{6})\)$")


def flatten(s):
    """攤平成事件串：('t', 字元, 顏色, 連結) 與 ('s', 結構性巨集)。"""
    events, colour, link = [], None, None
    for is_macro, chunk in split_macros(s):
        if not is_macro:
            events.extend(("t", c, colour, link) for c in chunk)
        elif chunk in COLOUR_TOKEN:
            colour = COLOUR_TOKEN[chunk]
        elif COLOUR_CODE.match(chunk):
            colour = chunk[2:-1]
        elif chunk.startswith("$(l:"):
            link = chunk[4:-1]
        elif chunk == "$(/l)":
            link = None
        else:
            if chunk == "$()":          # 全重設，順帶把顏色清掉
                colour = None
            events.append(("s", chunk))
    return events


def serialize(events):
    """依狀態輸出最簡寫法。連結在外、顏色在內，與 Botania 英文原文同構。"""
    out, colour, link = [], None, None

    def set_link(target):
        nonlocal colour, link
        if target == link:
            return
        if colour is not None:
            out.append("$(0)")
            colour = None
        if link is not None:
            out.append("$(/l)")
        if target is not None:
            out.append(f"$(l:{target})")
        link = target

    for ev in events:
        if ev[0] == "s":
            out.append(ev[1])
            if ev[1] == "$()":
                colour = None
            continue
        _, ch, col, lk = ev
        set_link(lk)
        if col != colour:
            out.append("$(0)" if col is None else f"$({col})")
            colour = col
        out.append(ch)
    if colour is not None:
        out.append("$(0)")
    if link is not None:
        out.append("$(/l)")
    return "".join(out)


def mark_terms(key, text, en_text, term_map, unresolved):
    """依英文原文，把每個該上色或該掛連結的詞整段標好。

    直接改「字」的顏色與連結，不做巨集開合的縫補，所以被切成兩半的詞、
    只蓋到一半的連結、多出來的重設，全都在重新輸出時一併消失。
    """
    events = flatten(text)
    pos = [i for i, e in enumerate(events) if e[0] == "t"]
    chars = "".join(events[i][1] for i in pos)

    wanted = {}
    for kind, path, raw, inner in spans_of(en_text):
        if kind == "link":
            # 連結內層自己帶什麼顏色，就照英文那一層走
            colour = ("thing" if "$(thing)" in raw
                      else "item" if "$(item)" in raw else None)
        else:
            colour = kind
        wanted[(inner, colour, path)] = wanted.get((inner, colour, path), 0) + 1

    claimed, added, relinked = set(), 0, 0
    for (term, colour, path), need in sorted(wanted.items(),
                                             key=lambda x: -len(x[0][0])):
        zh = resolve(term, term_map)
        if not zh or len(zh) < 2:
            if path:
                unresolved.append((key, "查不到中文", term))
            continue
        def colour_at(i):
            return events[pos[i]][2] if 0 <= i < len(pos) else None

        spots, start = [], 0
        while True:
            a = chars.find(zh, start)
            if a < 0:
                break
            b = a + len(zh)
            start = a + 1
            if any(i in claimed for i in range(a, b)):
                continue
            # 不切開既有的上色區段：若這個詞只是某段已上色文字的一部分，
            # 標下去會變成「$(item)魔鋼錠，$(thing)魔力$(item)鑽石…」那種夾心。
            if colour_at(a) is not None and colour_at(a - 1) == colour_at(a):
                continue
            if colour_at(b - 1) is not None and colour_at(b) == colour_at(b - 1):
                continue
            spots.append((a, b))
        if not spots:
            if path:
                unresolved.append((key, "詞不在譯文", f"{term} / {zh}"))
            continue
        # 已經上了色或掛了連結的位置優先，才不會在別處另起爐灶
        spots.sort(key=lambda ab: -sum(
            1 for i in range(*ab)
            if events[pos[i]][2] == colour or events[pos[i]][3] == path))
        for a, b in spots[:need]:
            before = [(events[pos[i]][2], events[pos[i]][3]) for i in range(a, b)]
            for i in range(a, b):
                j = pos[i]
                events[j] = ("t", events[j][1], colour, path or events[j][3])
                claimed.add(i)
            after = [(events[pos[i]][2], events[pos[i]][3]) for i in range(a, b)]
            if before != after:
                added += 1
                if path and any(x[1] != path for x in before):
                    relinked += 1
    return serialize(events), added, relinked


def spans_of(s):
    """取出所有被標記的區段：(種類, 連結目標, 內層原文, 內層純文字)。"""
    out = []
    for m in SPAN.finditer(s):
        if m.group(1) is not None:
            out.append(("link", m.group(1), m.group(2),
                        MACRO.sub("", m.group(2)).strip()))
        else:
            out.append((m.group(3), None, m.group(4),
                        MACRO.sub("", m.group(4)).strip()))
    return out


def build_term_map(names, lang, vanilla_en, vanilla_tw, terms):
    """英文詞 → 中文詞。

    順序刻意讓 botania-book-terms.json 贏過一切：模組自帶的 zh_tw 品質很差，
    術語常常是隨手翻的，沒有理由讓它壓過本包想好的譯名。品名表與原版語系檔
    只負責填這份人工決定沒有涵蓋到的詞。
    """
    m = {}
    for key, d in names.items():
        if key.endswith((".reference", ".desc", ".poem")):
            continue
        zh = lang.get(key) or d.get("tw")
        if zh:
            m.setdefault(d["en"], zh)
    for key, e in vanilla_en.items():
        zh = vanilla_tw.get(key)
        if zh and key.startswith(("block.minecraft.", "item.minecraft.",
                                  "entity.minecraft.")):
            m.setdefault(e, zh)
    m.update(terms)
    return m


def apply_term_names(lang, names, en, tw, terms, modpack_renames):
    """把人工決定的譯名套回品名，並回報書裡要跟著換掉的舊寫法。

    決定一次就好：改了 Pixie Dust 的譯名，物品欄、生物名與辭典內文要一起變，
    不然玩家在 JEI 看到的和書上寫的又是兩個名字。模組包自己改過名的條目不碰，
    那是 distribute_renames 的地盤。
    """
    english = {k: d["en"] for k, d in names.items()}
    for key, value in en.items():           # names.json 只收方塊與物品
        if key.startswith("entity.botania.") and key not in english:
            english[key] = value

    renamed, drift = {}, []
    for key, word in sorted(english.items()):
        zh = terms.get(word)
        if not zh or key in modpack_renames:
            continue
        old = lang.get(key, tw.get(key))
        if not old or old == zh:
            continue
        lang[key] = zh
        renamed[key] = (old, zh)
        drift.append((old, zh))
    return renamed, drift


def resolve(term, term_map):
    """查中文詞，順便處理英文複數。查不到回 None，由呼叫端記錄。"""
    if term in term_map:
        return term_map[term]
    for suffix, base in (("ies", "y"), ("es", ""), ("s", "")):
        if term.endswith(suffix):
            cand = term[:-len(suffix)] + base
            if cand in term_map:
                return term_map[cand]
    return None


def restore_paragraphs(key, text, en_text, short):
    """英文有、譯文只少一個的 $(p)，補在比例位置最接近的中文句末。

    只補一個。差兩個以上通常代表整頁是照舊版英文譯的，段落結構根本對不上，
    硬塞只會塞出 $(p)$(p)$(p)；那種情況記進 short 清單，留給人工處理。
    """
    n_en = en_text.count("$(p)")
    n_tw = text.count("$(p)")
    if n_en <= n_tw:
        return text, 0
    if n_en - n_tw > 1:
        short.append((key, n_en, n_tw))
        return text, 0

    plain_en = MACRO.sub("", en_text)
    m = list(re.finditer(r"\$\(p\)", en_text))[n_tw]
    ratio = len(MACRO.sub("", en_text[:m.start()])) / max(1, len(plain_en))

    parts = split_macros(text)
    plain = "".join(t for is_macro, t in parts if not is_macro)
    target = ratio * len(plain)
    best, best_d, seen = None, None, 0
    for idx, (is_macro, t) in enumerate(parts):
        if is_macro:
            continue
        for j, c in enumerate(t):
            seen += 1
            if c not in "。！？」":
                continue
            if t[j + 1:j + 2] in ("", None) and parts[idx + 1:idx + 2] and \
                    parts[idx + 1][1] == "$(p)":
                continue                      # 這裡已經有分段了
            d = abs(seen - target)
            if best_d is None or d < best_d:
                best, best_d = (idx, j + 1), d
    if best is None:
        short.append((key, n_en, n_tw))
        return text, 0
    idx, j = best
    parts[idx] = (False, parts[idx][1][:j] + "$(p)" + parts[idx][1][j:])
    return "".join(x[1] for x in parts), 1


# ---------------------------------------------------------------- 主流程
def main():
    jar = next(j for j in sorted(os.listdir(MODS)) if j.startswith("Botania"))
    with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
        en = json.loads(z.read("assets/botania/lang/en_us.json").decode("utf-8"))
        tw = json.loads(z.read("assets/botania/lang/zh_tw.json").decode("utf-8"))

    lang = json.load(open(LANG, encoding="utf-8"))
    names = json.load(open(NAMES, encoding="utf-8"))
    # 兩份人工資料裡以底線開頭的鍵是給人看的說明，不是資料
    terms = {k: v for k, v in json.load(open(TERMS, encoding="utf-8")).items()
             if not k.startswith("_")}
    manual = {k: v for k, v in json.load(open(MANUAL, encoding="utf-8")).items()
              if not k.startswith("_")}
    vdir = os.path.join(ROOT, "_workspace", "build", "verify")
    vanilla_en = json.load(open(os.path.join(vdir, "vanilla_en_us.json"),
                                encoding="utf-8"))
    vanilla_tw = json.load(open(os.path.join(vdir, "vanilla_zh_tw.json"),
                                encoding="utf-8"))

    modpack_renames = set(json.load(open(RENAMES, encoding="utf-8")))
    renamed, name_drift = apply_term_names(lang, names, en, tw, terms,
                                           modpack_renames)
    term_map = build_term_map(names, lang, vanilla_en, vanilla_tw, terms)

    keys = [k for k in en if k.startswith(BOOK_PREFIXES)]
    totals = {}
    changes, unresolved, short_paras = {}, [], []
    stale_manual = [k for k in manual if k not in en]
    if stale_manual:
        sys.exit(f"botania-book-manual.json 有不存在的鍵：{stale_manual}")

    # keep-as-source 登記的條目裡，只有「一字不差就是英文原文」的那些要連排版
    # 都不動（0x1a4 會被當成尺寸寫法改掉）。其餘多半是本包自己寫的中文譯文，
    # 登記在那裡是為了別的檢查，照樣要做標點正規化。
    keep = {x for x in json.load(open(KEEP, encoding="utf-8"))
            if not x.startswith("_")}

    for k in keys:
        before = lang.get(k, tw.get(k, ""))
        if k in keep and before == en.get(k):
            totals["保留原文"] = totals.get("保留原文", 0) + 1
            if before:
                lang[k] = before
            continue
        if k in manual:
            after = manual[k]
            if after != before:
                changes[k] = {"前": before, "後": after, "手動": True}
            lang[k] = after
            totals["手動覆寫"] = totals.get("手動覆寫", 0) + 1
            continue

        text, counts = typography(before)
        for name, n in counts.items():
            if n:
                totals[name] = totals.get(name, 0) + n

        # 先把被切斷的上色接起來，術語代換才看得到完整的詞
        text = serialize(flatten(text))
        text, n = collapse_double_p(text)
        totals["多餘的分段"] = totals.get("多餘的分段", 0) + n
        text, n = apply_drift(k, text, name_drift)
        totals["舊譯名"] = totals.get("舊譯名", 0) + n
        for bad, good in SUBS:
            if bad in text:
                totals["殘留簡中用語"] = totals.get("殘留簡中用語", 0) + text.count(bad)
                text = text.replace(bad, good)

        # 標詞也要跑到不動為止：把一個詞接成完整區段之後，原本被判為
        # 「在別人的區段中間」而跳過的位置才會露出來。
        marked = 0
        for _ in range(3):
            text, n, relinked = mark_terms(k, text, en[k], term_map,
                                           unresolved if not marked else [])
            totals["補回連結"] = totals.get("補回連結", 0) + relinked
            marked += n
            if not n:
                break
        totals["重標上色與連結"] = totals.get("重標上色與連結", 0) + marked
        text, n = restore_paragraphs(k, text, en[k], short_paras)
        totals["補回分段"] = totals.get("補回分段", 0) + n

        if text != before:
            changes[k] = {"前": before, "後": text}
        if text or k in lang:
            lang[k] = text

    for k in [x for x in lang if x.endswith(FLAVOUR_SUFFIXES)]:
        before = lang[k]
        after, counts = typography(before)
        if after != before:
            changes[k] = {"前": before, "後": after}
            lang[k] = after
            for name, n in counts.items():
                if n:
                    totals[name] = totals.get(name, 0) + n

    json.dump(lang, open(LANG, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    json.dump({"改寫": changes, "未解出的詞": unresolved,
               "分段對不上": short_paras},
              open(REPORT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    if renamed:
        print(f"  依術語表改名 {len(renamed)} 條：")
        for key, (old, new) in sorted(renamed.items()):
            print(f"    {old} → {new}　（{key}）")
    print(f"  書本鍵 {len(keys)} 條，改寫 {len(changes)} 條")
    for name, n in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"    {name}：{n}")
    if unresolved:
        print(f"  [注意] {len(unresolved)} 個詞查不到中文，未補：")
        for row in unresolved[:20]:
            print(f"    {row[0]}  {row[1]}  {row[2]}")
        if len(unresolved) > 20:
            print(f"    …另有 {len(unresolved) - 20} 筆，詳見 book-changes.json")
    if short_paras:
        print(f"  [注意] {len(short_paras)} 頁的段落數與英文差兩段以上，未動：")
        print("    " + "、".join(k.split(".")[-1] for k, _, _ in short_paras))


if __name__ == "__main__":
    main()
