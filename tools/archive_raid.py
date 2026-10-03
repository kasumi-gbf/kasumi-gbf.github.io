"""終わった古戦場の団データ(予選の毎時・本戦各日の毎時)を archive/raid-NNN.json に保存する。

gbfdataは毎時データを直近2回ぶんしか持たず、スプレッドシートのアーカイブ(A3)も書き戻しで
欠けることがあるため、確定した回はリポジトリにファイルとして残し、サーバーはそれを最後の
よりどころとして読む(server.py の archive_get)。

使い方: python3 tools/archive_raid.py 84 [83 ...]
  公開中の貢献度サイト(BASE)の API を叩くだけなので、秘密情報は不要。
  本戦の相手は /api/config?raid=N の保存済み対戦相手を使う(団名だけの日は名前検索の最有力候補)。
"""
import json
import os
import sys
import urllib.parse
import urllib.request

BASE = os.environ.get("ARCHIVE_BASE", "https://gbf-kasumi.onrender.com")
OUT = os.path.join(os.path.dirname(__file__), "..", "archive")
HOURS = [f"{h:02d}:00" for h in range(8, 24)] + ["24:00"]   # server.py の HOURS と同じ


def get(path, **q):
    url = BASE + path + ("?" + urllib.parse.urlencode(q) if q else "")
    with urllib.request.urlopen(url, timeout=300) as r:
        return json.load(r)


def honsen_day(raid, date, opp):
    d = get("/api/live", raid=raid, date=date, opp=opp)
    if d.get("candidates"):                       # 団名が複数ヒット → 最有力(先頭)のIDで引き直す
        d = get("/api/live", raid=raid, date=date, opp=d["candidates"][0]["gid"])
    if d.get("error"):
        return None, d["error"]
    o, p = d["ours"]["cum"], d["opp"]["cum"]
    if not (any(v is not None for v in o.values()) or any(v is not None for v in p.values())):
        return None, "毎時データなし"
    return {"opp_name": d["opp"].get("name") or "", "opp_gid": d["opp"].get("gid"),
            "o": [o.get(h) for h in HOURS], "p": [p.get(h) for h in HOURS]}, None


def main(raids):
    os.makedirs(OUT, exist_ok=True)
    for raid in raids:
        rec = {"raid": raid, "hours": HOURS}
        y = get("/api/yosen", raid=raid)
        ks = [k for k in y["keys"] if y["ours"]["cum"].get(k) is not None or y["border"]["cum"].get(k) is not None]
        if ks:
            rec["yosen"] = {"k": ks, "l": [y["labels"][y["keys"].index(k)] for k in ks],
                            "o": [y["ours"]["cum"].get(k) for k in ks],
                            "r": [(y["ours"].get("rank") or {}).get(k) for k in ks],
                            "b": [y["border"]["cum"].get(k) for k in ks]}
        cfg = get("/api/config", raid=raid)
        rec["honsen"] = {}
        for date, op in sorted((cfg.get("opponents") or {}).items()):
            day, err = honsen_day(raid, date, op.get("gid") or op.get("name"))
            if day:
                rec["honsen"][date] = day
            print(f"  第{raid}回 {date}: " + (f"OK 相手={day['opp_name']}" if day else f"なし({err})"))
        n = len(rec.get("yosen", {}).get("k", []))
        print(f"第{raid}回: 予選 {n}点 / 本戦 {len(rec['honsen'])}日")
        if n or rec["honsen"]:
            with open(os.path.join(OUT, f"raid-{raid:03d}.json"), "w") as f:
                json.dump(rec, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main([int(x) for x in sys.argv[1:]])
