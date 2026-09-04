"""稽核實例中所有模組自帶的 zh_tw 品質。

「有 zh_tw」不等於「品質可用」。本腳本對每個 jar 內的 assets/<ns>/lang/zh_tw.json
量測三項指標，用來找出 Botania 那類「有檔但其實是簡中轉換品且不完整」的模組：

  完成度   zh_tw 條數 / en_us 條數
  半形標點 中文句子裡使用 , . ! ? ; : 的比例（高 = 可能由簡中轉換）
  簡中痕跡 殘留簡體字、以及 CN_TERMS 對照表命中的簡中用詞

輸出：build/verify/mod_lang_audit.json 與終端摘要
"""

import json
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_translation import SIMPLIFIED, CN_TERMS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances",
                    "Liminal Industries Acension", "minecraft", "mods")
OUT = os.path.join(ROOT, "build", "verify", "mod_lang_audit.json")

HAN = re.compile(r"[一-鿿]")
HALF = re.compile(r"[,.!?;:]")
FULL = re.compile(r"[，。！？；：]")


def audit_pair(en, tw):
    zh = [v for v in tw.values() if isinstance(v, str) and HAN.search(v)]
    half = sum(1 for v in zh if HALF.search(v))
    full = sum(1 for v in zh if FULL.search(v))
    simp = {k for k, v in tw.items() if isinstance(v, str) and set(v) & SIMPLIFIED}
    terms = {k for k, v in tw.items() if isinstance(v, str)
             and any(cn in v for cn, t in CN_TERMS if cn != t)}
    return {
        "en": len(en), "tw": len(tw),
        "missing": len(set(en) - set(tw)),
        "complete_pct": round(len(set(en) & set(tw)) * 100 / max(1, len(en))),
        "zh_lines": len(zh), "halfwidth": half, "fullwidth": full,
        "halfwidth_pct": round(half * 100 / max(1, len(zh))),
        "simplified": len(simp), "cn_terms": len(terms),
    }


def main():
    results = {}
    for jar in sorted(os.listdir(MODS)):
        if not jar.endswith(".jar"):
            continue
        try:
            with zipfile.ZipFile(os.path.join(MODS, jar)) as z:
                names = z.namelist()
                for n in names:
                    m = re.fullmatch(r"assets/([a-z0-9_.-]+)/lang/zh_tw\.json", n)
                    if not m:
                        continue
                    ns = m.group(1)
                    en_path = f"assets/{ns}/lang/en_us.json"
                    if en_path not in names:
                        continue
                    try:
                        tw = json.loads(z.read(n).decode("utf-8"))
                        en = json.loads(z.read(en_path).decode("utf-8"))
                    except Exception:
                        continue
                    if not isinstance(tw, dict) or len(en) < 20:
                        continue
                    results[ns] = dict(audit_pair(en, tw), jar=jar)
        except zipfile.BadZipFile:
            continue

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(results, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # 可疑 = 完成度低，或半形標點比例高，或有簡中痕跡
    def suspect(r):
        return (r["complete_pct"] < 90 or r["halfwidth_pct"] >= 30
                or r["simplified"] or r["cn_terms"])

    bad = {k: v for k, v in results.items() if suspect(v)}
    good = {k: v for k, v in results.items() if not suspect(v)}

    print(f"掃描 {len(results)} 個自帶 zh_tw 的命名空間\n")
    print(f"{'命名空間':<26}{'完成度':>7}{'缺譯':>7}{'半形%':>7}{'簡體':>6}{'簡中詞':>7}")
    print("-" * 62)
    for ns, r in sorted(bad.items(), key=lambda x: (x[1]["complete_pct"], -x[1]["halfwidth_pct"])):
        print(f"{ns:<26}{r['complete_pct']:>6}%{r['missing']:>7}"
              f"{r['halfwidth_pct']:>6}%{r['simplified']:>6}{r['cn_terms']:>7}")
    print(f"\n可疑 {len(bad)} 個、看起來正常 {len(good)} 個")
    print(f"完整結果：{os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
