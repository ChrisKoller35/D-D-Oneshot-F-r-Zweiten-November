import json, sys, os, html
D = json.load(open("data.json")); only = sys.argv[1:]
HUE = {"1":"#2f8f3a","2":"#1f5a2a","3":"#2a2f2a","4":"#b3261e","5":"#7a4a22","6":"#4f9fd6","7":"#9fb3bf","8":"#d9731c","9":"#7a3fb8","10":"#7a1424","11":"#c2410c","12":"#8a2a12","?":"#a8b82a"}
RAR = {"gewöhnlich":("#111","#555"),"ungewöhnlich":("#8c99a6","#e8eef4"),"selten":("#a6862a","#f6e39a"),"sehr selten":("#c2410c","#ffb070")}
def rar(s):
    for k in ["sehr selten","ungewöhnlich","gewöhnlich","selten"]:
        if s.startswith(k): return RAR[k]
def stk(s): return "∞" if "genug" in s else "?" if "vielleicht" in s else s.split()[0]
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400;1,500&family=Spectral+SC:wght@600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{width:750px;height:1050px;background:transparent}
.card{width:750px;height:1050px;border-radius:34px;background:#0b0b0b;padding:30px 28px 46px;position:relative}
.frame{height:100%;border-radius:12px;padding:16px 16px 14px;display:flex;flex-direction:column;
 background:
  radial-gradient(circle at 20% 15%,rgba(255,255,255,.18),transparent 40%),
  radial-gradient(circle at 80% 85%,rgba(0,0,0,.35),transparent 45%),
  repeating-linear-gradient(115deg,rgba(255,255,255,.05) 0 3px,rgba(0,0,0,.05) 3px 7px),
  linear-gradient(160deg,color-mix(in srgb,var(--h) 80%,#fff),var(--h) 45%,color-mix(in srgb,var(--h) 55%,#000));
 box-shadow:inset 0 0 0 2px rgba(0,0,0,.5),inset 0 0 18px rgba(0,0,0,.5)}
.bar{display:flex;align-items:center;justify-content:space-between;padding:0 14px 0 18px;height:60px;border-radius:10px/30px;
 background:linear-gradient(180deg,color-mix(in srgb,var(--h) 18%,#fbf6ea),color-mix(in srgb,var(--h) 30%,#d8cfbd));
 border:3px solid color-mix(in srgb,var(--h) 40%,#222);box-shadow:0 3px 4px rgba(0,0,0,.55),inset 0 2px 0 rgba(255,255,255,.7);position:relative;z-index:2}
.name{flex:1;min-width:0;white-space:nowrap;overflow:hidden;font-family:'Spectral SC',serif;font-weight:700;font-size:var(--fs);color:#111;line-height:1}
.mana{width:40px;height:40px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;
 font-family:Cinzel,serif;font-weight:700;font-size:22px;color:#111;background:radial-gradient(circle at 35% 30%,#fff,color-mix(in srgb,var(--h) 45%,#ddd));
 box-shadow:-2px 2px 0 #000}
.art{margin:-4px 8px 0;height:452px;border:3px solid #111;border-top-width:6px;overflow:hidden;background:#000;position:relative;z-index:1}
.art img{width:100%;height:100%;object-fit:cover;display:block}
.type{margin-top:-4px}
.type .name{font-size:27px}
.set{width:38px;height:38px;flex:none}
.box{flex:1;margin:-4px 8px 0;padding:18px 22px 14px;border:3px solid color-mix(in srgb,var(--h) 40%,#222);border-top:0;
 background:radial-gradient(ellipse at 50% 30%,color-mix(in srgb,var(--h) 8%,#f8f1df),color-mix(in srgb,var(--h) 22%,#e3d6b8));
 font-family:'Crimson Pro',serif;color:#111;display:flex;flex-direction:column;justify-content:center;gap:12px;box-shadow:inset 0 0 12px rgba(0,0,0,.25)}
.rule{font-size:var(--ws);line-height:1.22}
.rule b{font-weight:700}
.flav{font-style:italic;font-size:calc(var(--ws) - 3px);line-height:1.2;color:#222}
.flav span{display:block;text-align:right;font-style:normal}
.hr{height:1px;background:linear-gradient(90deg,transparent,rgba(0,0,0,.45),transparent)}
.foot{position:absolute;left:44px;right:40px;bottom:12px;display:flex;justify-content:space-between;align-items:flex-end;
 font-family:'Crimson Pro',serif;font-size:15px;color:#ddd;line-height:1.2}
.pt{position:absolute;right:40px;bottom:30px;min-width:96px;height:52px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-family:'Crimson Pro',serif;font-weight:700;font-size:32px;color:#111;padding:0 12px;
 background:linear-gradient(180deg,color-mix(in srgb,var(--h) 18%,#fbf6ea),color-mix(in srgb,var(--h) 30%,#d8cfbd));
 border:3px solid color-mix(in srgb,var(--h) 40%,#222);box-shadow:0 3px 4px rgba(0,0,0,.6)}
"""
SCRIPT = "<script>document.fonts.ready.then(()=>{for(const n of document.querySelectorAll('.bar .name')){let f=parseFloat(getComputedStyle(n).fontSize);while(n.scrollWidth>n.clientWidth&&f>18){f-=1;n.style.fontSize=f+'px'}}})</script>"
def setsym(c1,c2):
    return f"""<svg class=set viewBox="0 0 40 40"><defs><linearGradient id=g x1=0 y1=0 x2=0 y2=1><stop offset=0 stop-color="{c2}"/><stop offset=1 stop-color="{c1}"/></linearGradient></defs>
<path d="M16 4h8v3h-1.5v8.5C29 18 33 23 33 28.5 33 35 27 38 20 38S7 35 7 28.5C7 23 11 18 17.5 15.5V7H16z" fill="url(#g)" stroke="#000" stroke-width="2.2" stroke-linejoin="round"/></svg>"""
def card(d):
    n=len(d["name"]); fs = 34
    L=len(d["wirk"]); ws = 32 if L<120 else 29 if L<200 else 27 if L<260 else 25
    c1,c2=rar(d["selt"]); h=HUE[d["nr"]]
    img=os.path.abspath(f"img/{'S' if d['nr']=='?' else d['nr'].zfill(2)}.png")
    sub = d.get("sub") or ("Toms Rezept" if "Rezept" in d["selt"] else d["farbe"].split(",")[0].capitalize())
    tot = d.get("tot") or ("Nr. "+d["nr"]+"/10" if d["nr"]!="?" else "Nicht auf der Karte")
    typ = d.get("typ","Trank"); von = d.get("von","Druide Tom"); foot = d.get("foot","Toms Tränke")
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>
<div class=card style="--h:{h};--fs:{fs}px;--ws:{ws}px"><div class=frame>
<div class=bar><div class=name>{html.escape(d['name'])}</div><div class=mana>{d['nr']}</div></div>
<div class=art><img src="file://{img}"></div>
<div class="bar type"><div class=name>{html.escape(typ)} — {html.escape(sub)}</div>{setsym(c1,c2)}</div>
<div class=box><div class=rule>{d['wirk']}</div><div class=hr></div>
<div class=flav>«{html.escape(d['tom'])}»<span>— {html.escape(von)}</span></div></div>
</div>
<div class=pt>{stk(d['stk'])}</div>
<div class=foot><span>{tot} · {html.escape(d['selt'].split(' ·')[0].capitalize())}<br>{html.escape(foot)} · Die letzte Grosstat</span><span></span></div>
</div>{SCRIPT}</body></html>"""
os.makedirs("mtg",exist_ok=True); jobs=[]
for d in D:
    if only and d["nr"] not in only: continue
    k='S' if d['nr']=='?' else d['nr'].zfill(2)
    f=os.path.abspath(f"mtg/{k}.html"); open(f,"w").write(card(d)); jobs.append([f,os.path.abspath(f"mtg/{k}.png")])
json.dump(jobs,open("jobs.json","w"))
