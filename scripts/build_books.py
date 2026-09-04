"""產出 TConstruct 的 Mantle 書本中文頁面。

TConstruct 的六本書不走 lang 檔，內容放在
    assets/tconstruct/book/<書>/<語系>/<章節>/<頁面>.json
Mantle 逐檔挑選語系：某頁在 zh_tw 缺檔就回退成 en_us，所以模組自帶那份
停在舊版時，會出現一本書半中半英。章節名稱另外放在同層的 language.lang，
Mantle 只讀優先度最高的那一份，不做合併，缺一條就直接顯示 key 值本身。

本腳本做兩件事：

  1. 對每個英文頁面，若模組的 zh_tw 已有同名檔就不動它；沒有的才由
     translation/book/tconstruct/pages.json 補上，並套回英文檔的結構。
     模組自己那份有錯的少數頁面則列在同檔的 _override，每條都要寫明理由。
  2. 以 translation/book/tconstruct/lang/<書>.lang 整份取代 language.lang。

輸出：_workspace/build/books/assets/tconstruct/book/...，由 build.py 併進資源包。

模組更新後若新增頁面，本腳本會因為缺譯而中止並列出檔名；若英文條列的長度改變，
也會中止，避免譯文與英文對不上而靜默錯位。
"""

import glob
import json
import shutil
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INST = os.path.join(os.environ.get("APPDATA", ""), "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft")
SRC = os.path.join(ROOT, "translation", "book", "tconstruct")
OUT = os.path.join(ROOT, "_workspace", "build", "books",
                   "assets", "tconstruct", "book")

# 條列型欄位：值是字串陣列，長度必須與英文一致
LIST_FIELDS = ("effects", "properties", "block", "entity")


def find_jar():
    hits = sorted(glob.glob(os.path.join(INST, "mods", "TConstruct-*.jar")))
    if not hits:
        raise SystemExit(f"找不到 TConstruct jar：{os.path.join(INST, 'mods')}")
    return hits[-1]


def book_files(z):
    """回傳 {書名: {語系: {相對路徑: 完整路徑}}}。"""
    out = {}
    pat = re.compile(r"^assets/tconstruct/book/([^/]+)/([a-z]{2}_[a-z]{2})/(.+)$")
    for n in z.namelist():
        if n.endswith("/"):
            continue
        m = pat.match(n)
        if m:
            out.setdefault(m.group(1), {}).setdefault(m.group(2), {})[m.group(3)] = n
    return out


def translate(en, tw, where):
    """把 tw 的譯文套進 en 的結構，回傳新的頁面資料。"""
    out = {}
    for key, val in en.items():
        if key == "title":
            out[key] = tw.get("title", val)
        elif key == "text":
            out[key] = translate_text(val, tw.get("text"), where)
        elif key in LIST_FIELDS:
            new = tw.get(key)
            if new is None:
                out[key] = val
                continue
            if len(new) != len(val):
                raise SystemExit(f"{where}：{key} 有 {len(val)} 條，譯文卻有 {len(new)} 條")
            out[key] = list(new)
        else:
            out[key] = val
    unknown = [k for k in tw
               if k not in en and not (k == "text" and "text" in en)]
    if unknown:
        raise SystemExit(f"{where}：英文檔沒有這些欄位 {unknown}")
    return out


def translate_text(val, new, where):
    if new is None:
        return val
    if isinstance(val, str):
        if not isinstance(new, str):
            raise SystemExit(f"{where}：英文 text 是單一字串，譯文卻是陣列")
        return new
    if isinstance(new, str) or len(new) != len(val):
        n = 1 if isinstance(new, str) else len(new)
        raise SystemExit(f"{where}：text 有 {len(val)} 段，譯文卻有 {n} 段")
    out = []
    for para, text in zip(val, new):
        item = dict(para)
        item["text"] = text
        out.append(item)
    return out


def main():
    raw = json.load(open(os.path.join(SRC, "pages.json"), encoding="utf-8"))
    pages = {k: v for k, v in raw.items() if not k.startswith("_")}
    # 模組自帶譯文有錯時（簡中用詞、異體字、誤譯），在 _override 列出並寫明理由。
    override = {k: v for k, v in raw.get("_override", {}).items()
                if not k.startswith("_")}
    for key, val in override.items():
        if "reason" not in val:
            raise SystemExit(f"_override {key}：必須寫明覆寫理由")
    override = {k: {kk: vv for kk, vv in v.items() if kk != "reason"}
                for k, v in override.items()}

    if os.path.exists(OUT):
        shutil.rmtree(OUT)

    z = zipfile.ZipFile(find_jar())
    books = book_files(z)

    written = 0
    overwritten = 0
    missing = []
    used = set()
    used_override = set()

    for book, langs in sorted(books.items()):
        en = langs.get("en_us", {})
        have = langs.get("zh_tw", {})
        for rel in sorted(en):
            if rel == "language.lang":
                continue
            key = f"{book}/{rel}"
            if rel in have:                    # 模組自己有中文版
                if key not in override:
                    continue
                used_override.add(key)
                tw = override[key]
                overwritten += 1
            else:
                if key not in pages:
                    missing.append(key)
                    continue
                used.add(key)
                tw = pages[key]
            data = json.loads(z.read(en[rel]).decode("utf-8"))
            data = translate(data, tw, key)
            path = os.path.join(OUT, book, "zh_tw", *rel.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=2)
                fh.write("\n")
            written += 1

    stale = sorted((set(pages) - used) | (set(override) - used_override))
    if stale:
        raise SystemExit("以下譯文在英文版中找不到對應頁面，或模組已自行補上／移除：\n  "
                         + "\n  ".join(stale))
    if missing:
        raise SystemExit(f"以下 {len(missing)} 頁模組沒有中文版，本包也還沒翻：\n  "
                         + "\n  ".join(missing))

    langs_written = 0
    for f in sorted(os.listdir(os.path.join(SRC, "lang"))):
        if not f.endswith(".lang"):
            continue
        book = f[:-5]
        if book not in books:
            raise SystemExit(f"lang/{f}：模組沒有這本書")
        check_lang_keys(z, books[book], os.path.join(SRC, "lang", f), book)
        path = os.path.join(OUT, book, "zh_tw", "language.lang")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(open(os.path.join(SRC, "lang", f), encoding="utf-8").read())
        langs_written += 1

    print(f"書本頁面 {written} 檔（其中覆寫模組譯文 {overwritten} 檔）/ "
          f"章節名稱 {langs_written} 本 → {os.path.relpath(OUT, ROOT)}")
    return 0


def parse_lang(text):
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v
    return out


def check_lang_keys(z, langs, path, book):
    """language.lang 是整份取代，缺 key 會露出 key 值本身，所以必須逐條比對英文。"""
    en_path = langs.get("en_us", {}).get("language.lang")
    if not en_path:
        return
    en = parse_lang(z.read(en_path).decode("utf-8"))
    ours = parse_lang(open(path, encoding="utf-8").read())
    miss = sorted(k for k in en if k not in ours)
    extra = sorted(k for k in ours if k not in en)
    if miss:
        raise SystemExit(f"{book}/language.lang 缺少：{miss}")
    if extra:
        raise SystemExit(f"{book}/language.lang 多出英文版沒有的 key：{extra}")


if __name__ == "__main__":
    sys.exit(main())
