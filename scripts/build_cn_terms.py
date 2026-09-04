"""由原版官方語系檔產生「簡中術語黑名單」。

作法：對每一個 key，若官方 zh_cn 與 zh_tw 的譯法不同，那個簡中寫法就是
本專案不該出現的用詞，正確寫法是對應的 zh_tw。

  entity.minecraft.blaze   zh_cn 烈焰人   zh_tw 烈焰使者   → 「烈焰人」列入黑名單
  block.minecraft.sculk    zh_cn 幽匿     zh_tw 伏聆       → 「幽匿」列入黑名單

這比人工維護對照表可靠得多，先前手寫的 15 組漏掉了「烈焰人」，
而我在譯 sector_5 時明明查過 blaze = 烈焰使者，卻在 sector_2、sector_3 用了簡中寫法。

過濾規則（避免誤報）：
  · 只取名詞性 key（方塊、物品、生物、附魔、效果、生態域、流體）
  · 長度至少 2 個字，且整串都是漢字（排除含變數、標點的句子）
  · **簡中寫法不得出現在官方 zh_tw 全文中**，這條最關鍵：
    若某個寫法正體版本自己也在用，那它就不是簡中專屬用詞
  · 簡中與正體相同者自然排除

輸出：_workspace/build/verify/cn_terms.json
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERIFY = os.path.join(ROOT, "_workspace", "build", "verify")
TW = os.path.join(VERIFY, "vanilla_zh_tw.json")
CN = os.path.join(VERIFY, "vanilla_zh_cn.json")
OUT = os.path.join(VERIFY, "cn_terms.json")

# 名詞性的 key 前綴，這些的值是「術語」，句子型的 key 不取
NOUN_PREFIXES = (
    "block.minecraft.", "item.minecraft.", "entity.minecraft.",
    "enchantment.minecraft.", "effect.minecraft.", "biome.minecraft.",
    "fluid.minecraft.", "attribute.name.", "potion.",
)
HAN_ONLY = re.compile(r"^[一-鿿]{2,}$")


def main():
    if not (os.path.exists(TW) and os.path.exists(CN)):
        print("缺少原版語系檔，請先執行 scripts/fetch_vanilla_lang.py", file=sys.stderr)
        return 1
    tw = json.load(open(TW, encoding="utf-8"))
    cn = json.load(open(CN, encoding="utf-8"))
    tw_corpus = "\n".join(tw.values())

    terms, skipped_shared = {}, []
    for k, cn_v in cn.items():
        if not k.startswith(NOUN_PREFIXES):
            continue
        tw_v = tw.get(k)
        if not tw_v or tw_v == cn_v:
            continue
        if not HAN_ONLY.match(cn_v):
            continue
        if cn_v in tw_corpus:
            # 正體版自己也在用這個寫法 → 不是簡中專屬，不能當黑名單
            skipped_shared.append((cn_v, tw_v))
            continue
        # 同一個簡中寫法可能對到多個正體寫法，保留第一個並記錄全部
        terms.setdefault(cn_v, {"correct": tw_v, "keys": []})["keys"].append(k)

    # 第二層：詞素。
    # 官方 zh_cn 的完整值是「幽匿块」「下界岩」，只比對完整值會漏掉
    # 「幽匿生物」「下界之旅」這種自己組出來的說法。因此再抽出
    # 「在多個簡中術語中反覆出現、但正體全文從未使用」的字串當詞素。
    import collections
    frag = collections.Counter()
    example = {}
    for cn_v, info in terms.items():
        for n in (2, 3, 4):
            for i in range(len(cn_v) - n + 1):
                sub = cn_v[i:i + n]
                frag[sub] += 1
                example.setdefault(sub, (cn_v, info["correct"]))
    morphemes = {}
    for sub, n in frag.items():
        if n < 3 or sub in tw_corpus or sub in terms:
            continue
        # 若更長的片段涵蓋它且次數相同，保留較長者即可
        if any(sub != o and sub in o and frag[o] == n for o in frag):
            continue
        cn_e, tw_e = example[sub]
        morphemes[sub] = {"example_cn": cn_e, "example_tw": tw_e, "count": n}

    os.makedirs(VERIFY, exist_ok=True)
    json.dump({"terms": terms, "morphemes": morphemes},
              open(OUT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2, sort_keys=True)

    print(f"官方語系檔各 {len(tw)} 條")
    print(f"  名詞性且兩體不同的候選：{len(terms) + len(skipped_shared)}")
    print(f"  因『正體版也在用』而排除：{len(skipped_shared)}")
    print(f"  完整術語黑名單：{len(terms)} 個")
    print(f"  詞素黑名單：{len(morphemes)} 個"
          f"（在 3 個以上簡中術語中出現、且正體全文從未使用）")
    print("\n完整術語抽樣：")
    for t in sorted(terms)[:5]:
        print(f"    {t:<12}→ 應為 {terms[t]['correct']}")
    print("\n詞素抽樣（依出現次數）：")
    for sub, info in sorted(morphemes.items(), key=lambda x: -x[1]["count"])[:14]:
        print(f"    {sub:<8}×{info['count']:<4}"
              f"例：{info['example_cn']} → {info['example_tw']}")
    print(f"\n寫入 {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
