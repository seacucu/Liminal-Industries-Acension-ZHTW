"""把 FTB Quests 的明文 snbt 轉成 key 化骨架，並抽出 en_us.json。

輸入：source/config/ftbquests/quests/chapters/*.snbt（上游原檔，明文）
輸出：
    build/skeleton/config/ftbquests/quests/chapters/*.snbt   key 化骨架（不含譯文）
    source/quest_en_us.json                                  key → 英文原文

key 命名規則（FTB Quests 社群慣例）：
    ftbquests.chapter.<章節>.title
    ftbquests.chapter.<章節>.quest<QUEST_ID>.title
    ftbquests.chapter.<章節>.quest<QUEST_ID>.subtitle
    ftbquests.chapter.<章節>.quest<QUEST_ID>.description<N>      N 只數非空行
    ftbquests.chapter.<章節>.quest<QUEST_ID>.task.<TASK_ID_十進位>.title

注意事項：
  * 檔案為 CRLF，逐行改寫並原樣保留行尾與所有未觸及的內容
  * description 中的空行保留為字面 "" ，不編號、不進 JSON
  * 值裡的 % 必須轉義成 %%（Minecraft 語系檔格式規定）
  * snbt 的 \\" 跳脫需還原成真正的引號再寫進 JSON
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "config", "ftbquests", "quests", "chapters")
OUT_SNBT = os.path.join(ROOT, "_workspace", "build", "skeleton", "config", "ftbquests", "quests", "chapters")
OUT_JSON = os.path.join(ROOT, "source", "quest_en_us.json")

QUEST_ID = re.compile(r'^\t\t\tid: "([0-9A-Fa-f]{16})"')
CHAPTER_TITLE = re.compile(r'^(\t)(title): ("(?:[^"\\]|\\.)*")\s*$')
QUEST_FIELD = re.compile(r'^(\t\t\t)(title|subtitle): ("(?:[^"\\]|\\.)*")\s*$')
TASK_TITLE = re.compile(r'^(\t{4,})title: ("(?:[^"\\]|\\.)*")\s*$')
TASK_ID = re.compile(r'^(\t{4,})id: "([0-9A-Fa-f]{16})"')
DESC_ONELINE = re.compile(r'^(\t\t\t)description: \[((?:"(?:[^"\\]|\\.)*"(?:, ?)?)+)\]\s*$')
DESC_OPEN = re.compile(r'^\t\t\tdescription: \[\s*$')
DESC_CLOSE = re.compile(r'^\t\t\t\]\s*$')
DESC_ITEM = re.compile(r'^(\t\t\t\t)("(?:[^"\\]|\\.)*")\s*$')
STRING = re.compile(r'"(?:[^"\\]|\\.)*"')


def unquote(snbt_string):
    """snbt 字串字面 → 實際文字（處理 \\" 與 \\\\）。"""
    body = snbt_string[1:-1]
    return re.sub(r'\\(.)', lambda m: m.group(1), body)


def to_lang_value(text):
    """寫進語系檔前的處理：% 必須轉義成 %%。"""
    return text.replace("%", "%%")


IMAGE_ONLY = re.compile(r'^\{image:[^}]*\}$')


def is_image_line(text):
    """純圖片標記的 description 行不含可譯文字，保留字面不 key 化。"""
    return bool(IMAGE_ONLY.match(text.strip()))


class Chapter:
    def __init__(self, path):
        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8", newline="") as fh:
            self.lines = fh.read().splitlines(keepends=True)
        self.entries = {}   # key -> 英文原文
        self.stats = {"chapter_title": 0, "title": 0, "subtitle": 0,
                      "description": 0, "task_title": 0}

    # --- 定位每個 quest 物件的行範圍，並取出它的 id -------------------
    def quest_spans(self):
        spans, start, depth = [], None, 0
        for i, line in enumerate(self.lines):
            if re.match(r'^\t\t\{\s*$', line):
                start, depth = i, 1
            elif start is not None:
                depth += line.count("{") - line.count("}")
                if depth == 0:
                    spans.append((start, i))
                    start = None
        out = []
        for s, e in spans:
            qid = None
            for line in self.lines[s:e + 1]:
                m = QUEST_ID.match(line)
                if m:
                    qid = m.group(1)
                    break
            if qid is None:
                raise ValueError(f"{self.name}: 第 {s+1} 行的 quest 沒有 id")
            # 對齊 FTB Quests 自身的 Long.toHexString 慣例：去掉前導零
            out.append((s, e, format(int(qid, 16), "X")))
        return out

    def key(self, *parts):
        return ".".join(("ftbquests", "chapter", self.name) + parts)

    def record(self, key, text, kind):
        if key in self.entries:
            raise ValueError(f"key 重複：{key}")
        self.entries[key] = to_lang_value(text)
        self.stats[kind] += 1

    # --- 主流程 -------------------------------------------------------
    def process(self):
        out = list(self.lines)

        # 章節標題（depth 1，且不在任何 quest 內）
        spans = self.quest_spans()
        inside = set()
        for s, e, _ in spans:
            inside.update(range(s, e + 1))

        for i, line in enumerate(self.lines):
            if i in inside:
                continue
            m = CHAPTER_TITLE.match(line)
            if m:
                k = self.key("title")
                self.record(k, unquote(m.group(3)), "chapter_title")
                out[i] = f'{m.group(1)}title: "{{{k}}}"{self._eol(line)}'

        for s, e, qid in spans:
            self._process_quest(out, s, e, qid)

        self.lines_out = out

    @staticmethod
    def _eol(line):
        return line[len(line.rstrip("\r\n")):]

    def _process_quest(self, out, s, e, qid):
        q = f"quest{qid}"
        i = s
        while i <= e:
            line = self.lines[i]
            eol = self._eol(line)

            m = QUEST_FIELD.match(line)
            if m:
                field = m.group(2)
                k = self.key(q, field)
                self.record(k, unquote(m.group(3)), field)
                out[i] = f'{m.group(1)}{field}: "{{{k}}}"{eol}'
                i += 1
                continue

            m = DESC_ONELINE.match(line)
            if m:
                items = STRING.findall(m.group(2))
                rendered, n = [], 0
                for it in items:
                    text = unquote(it)
                    if text == "" or is_image_line(text):
                        rendered.append(it)
                        continue
                    n += 1
                    k = self.key(q, f"description{n}")
                    self.record(k, text, "description")
                    rendered.append(f'"{{{k}}}"')
                out[i] = f'{m.group(1)}description: [{", ".join(rendered)}]{eol}'
                i += 1
                continue

            if DESC_OPEN.match(line):
                j, n = i + 1, 0
                while j <= e and not DESC_CLOSE.match(self.lines[j]):
                    im = DESC_ITEM.match(self.lines[j])
                    if im:
                        text = unquote(im.group(2))
                        if text != "" and not is_image_line(text):
                            n += 1
                            k = self.key(q, f"description{n}")
                            self.record(k, text, "description")
                            out[j] = f'{im.group(1)}"{{{k}}}"{self._eol(self.lines[j])}'
                    j += 1
                i = j + 1
                continue

            m = TASK_TITLE.match(line)
            if m:
                depth = len(m.group(1))
                tid = None
                for back in range(i - 1, s - 1, -1):
                    tm = TASK_ID.match(self.lines[back])
                    if tm and len(tm.group(1)) == depth:
                        tid = tm.group(2)
                        break
                if tid is None:
                    raise ValueError(f"{self.name} 第 {i+1} 行的 task title 找不到同層 id")
                k = self.key(q, "task", str(int(tid, 16)), "title")
                self.record(k, unquote(m.group(2)), "task_title")
                out[i] = f'{m.group(1)}title: "{{{k}}}"{eol}'
                i += 1
                continue

            i += 1


def main():
    os.makedirs(OUT_SNBT, exist_ok=True)
    all_entries, totals = {}, {}

    paths = sorted(f for f in os.listdir(SRC) if f.endswith(".snbt"))
    for fname in paths:
        ch = Chapter(os.path.join(SRC, fname))
        ch.process()
        with open(os.path.join(OUT_SNBT, fname), "w", encoding="utf-8", newline="") as fh:
            fh.write("".join(ch.lines_out))
        all_entries.update(ch.entries)
        for k, v in ch.stats.items():
            totals[k] = totals.get(k, 0) + v
        print(f"  {ch.name:<12} {len(ch.entries):>4} keys  "
              + "  ".join(f"{k}={v}" for k, v in ch.stats.items() if v))

    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(all_entries, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"\n合計 {len(all_entries)} 個 key")
    for k, v in totals.items():
        print(f"  {k:<15} {v}")
    print(f"\n骨架 -> {os.path.relpath(OUT_SNBT, ROOT)}")
    print(f"英文 -> {os.path.relpath(OUT_JSON, ROOT)}")


if __name__ == "__main__":
    main()
