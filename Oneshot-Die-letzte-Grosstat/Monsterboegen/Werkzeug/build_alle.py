# Baut alle Monsterbögen: A4 (ein Monster pro Blatt) und Viertel-A4 (vier Monster pro Blatt).
# Aufruf: python3 build_alle.py <bildordner> <ausgabeordner>   danach: node render.js <ausgabeordner>
import sys, os, base64, html
IMG, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

FONTS = "@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');"
BASE = FONTS + """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm}
body{font-family:'Crimson Pro',serif;color:#2a1d12;background:#f3e9d2;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.dice{display:inline-block;background:#2a1d12;color:#ffe9b8;font-weight:600;border-radius:1.2mm;padding:0 1.6mm;line-height:1.5}
"""
# ---------- A4-Bogen (wie bisher) ----------
CSS_A4 = BASE + """
.page{width:210mm;height:297mm;position:relative;overflow:hidden;
 background:radial-gradient(ellipse at 50% 40%,#f8f0dc 0%,#efe1c0 70%,#e2cfa4 100%)}
.hero{position:relative;height:var(--hh);overflow:hidden;border-bottom:1.2mm solid var(--acc)}
.hero img{width:100%;height:100%;object-fit:cover;object-position:var(--pos);display:block}
.hero:after{content:"";position:absolute;inset:auto 0 0 0;height:22mm;background:linear-gradient(transparent,rgba(10,8,6,.78))}
.title{position:absolute;left:9mm;right:9mm;bottom:3.2mm;z-index:2;color:#fff;display:flex;align-items:flex-end;justify-content:space-between;gap:4mm}
.title h1{font-family:Cinzel,serif;font-weight:900;font-size:25pt;line-height:1;letter-spacing:.3pt;text-shadow:0 1px 4px #000}
.title .sub{font-style:italic;font-size:11pt;margin-top:1mm;text-shadow:0 1px 3px #000}
.hg{font-family:Cinzel,serif;font-weight:700;font-size:10pt;text-align:center;border:.5mm solid #fff;border-radius:2mm;padding:1.2mm 2.6mm;background:var(--acc);white-space:nowrap;line-height:1.15}
.hg b{font-size:17pt;display:block}
.body{padding:3.4mm 9mm 0 9mm}
.core{display:grid;grid-template-columns:repeat(4,1fr);gap:2mm;margin-bottom:2.4mm}
.core div{background:var(--acc);color:#fff;border-radius:1.6mm;padding:1.2mm 2mm;text-align:center;line-height:1.1}
.core small{display:block;font-family:Cinzel,serif;font-size:6.6pt;letter-spacing:.6pt;opacity:.9}
.core b{font-size:13.5pt}
.core i{font-style:normal;font-size:8.5pt;opacity:.9}
table.ab{width:100%;border-collapse:collapse;margin-bottom:2mm;font-size:10pt}
table.ab th{font-family:Cinzel,serif;font-size:8pt;color:var(--acc);padding:0 0 .4mm}
table.ab td{text-align:center;border-top:.3mm solid var(--line);border-bottom:.3mm solid var(--line);padding:.6mm 0;line-height:1.15}
table.ab td b{font-size:11.5pt}
table.ab td span{display:block;font-size:8pt;color:#6b5236}
.props{font-size:9.6pt;line-height:1.28;columns:2;column-gap:7mm;margin-bottom:1.6mm}
.props p{break-inside:avoid}
.props b{color:var(--acc)}
.cols{columns:2;column-gap:7mm;column-fill:auto;height:var(--ch)}
h2{font-family:Cinzel,serif;font-weight:700;font-size:10.5pt;color:var(--acc);border-bottom:.45mm solid var(--acc);margin:1.4mm 0 1.2mm;padding-bottom:.3mm;break-after:avoid}
h2 em{font-family:'Crimson Pro',serif;font-style:italic;font-weight:400;font-size:8.6pt;color:#5d4630;letter-spacing:0}
.f{break-inside:avoid;margin-bottom:1.5mm;font-size:9.3pt;line-height:1.24}
.f .n{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4mm 1.6mm;margin-bottom:.2mm}
.f .n b{font-size:10.4pt;font-weight:700}
.f .n .tag{font-size:7.8pt;color:#6b5236;font-style:italic}
.dice{font-size:9pt}
.f p{color:#3a2a1b}
.box{break-inside:avoid;border:.45mm solid var(--acc);background:rgba(255,255,255,.45);border-radius:1.6mm;padding:1.6mm 2.4mm;margin:1.6mm 0;font-size:9pt;line-height:1.24}
.box h3{font-family:Cinzel,serif;font-size:9pt;color:var(--acc);margin-bottom:.6mm}
.box h3 .nb{font-family:"Crimson Pro",serif;font-weight:700}
.foot{position:absolute;left:9mm;right:9mm;bottom:3.6mm;font-size:7.4pt;color:#7a6145;display:flex;justify-content:space-between;border-top:.3mm solid var(--line);padding-top:.8mm}
"""
# ---------- Viertel-A4 (vier Karten pro Blatt) ----------
CSS_Q = BASE + """
.sheet{width:210mm;height:297mm;position:relative;overflow:hidden;display:grid;grid-template-columns:105mm 105mm;grid-template-rows:148.5mm 148.5mm;background:#fff}
.card{width:105mm;height:148.5mm;position:relative;overflow:hidden;border:.2mm dashed #b9a98c;
 background:radial-gradient(ellipse at 50% 35%,#f8f0dc 0%,#efe1c0 70%,#e2cfa4 100%);--acc:#5a3b22;--line:#c2a27f}
.card .hero{position:relative;height:42mm;overflow:hidden;border-bottom:.8mm solid var(--acc)}
.card .hero img{width:100%;height:100%;object-fit:cover;object-position:var(--pos,50% 40%);display:block}
.card .hero:after{content:"";position:absolute;inset:auto 0 0 0;height:15mm;background:linear-gradient(transparent,rgba(10,8,6,.8))}
.card .title{position:absolute;left:4mm;right:4mm;bottom:1.8mm;z-index:2;color:#fff;display:flex;align-items:flex-end;justify-content:space-between;gap:2mm}
.card .title h1{font-family:Cinzel,serif;font-weight:900;font-size:15pt;line-height:1;text-shadow:0 1px 3px #000}
.card .title .sub{font-style:italic;font-size:8pt;margin-top:.6mm;text-shadow:0 1px 2px #000}
.card .hg{font-family:Cinzel,serif;font-weight:700;font-size:6.6pt;text-align:center;border:.35mm solid #fff;border-radius:1.4mm;padding:.7mm 1.6mm;background:var(--acc);white-space:nowrap;line-height:1.1}
.card .hg b{font-size:11.5pt;display:block}
.card .body{padding:2mm 4mm 0 4mm}
.card .core{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2mm;margin-bottom:1.4mm}
.card .core div{background:var(--acc);color:#fff;border-radius:1.2mm;padding:.7mm 1mm;text-align:center;line-height:1.05}
.card .core small{display:block;font-family:Cinzel,serif;font-size:5.4pt;letter-spacing:.4pt;opacity:.9}
.card .core b{font-size:10.5pt}
.card .core i{font-style:normal;font-size:6.8pt;opacity:.9}
.card table.ab{width:100%;border-collapse:collapse;margin-bottom:1.2mm;font-size:7.8pt}
.card table.ab th{font-family:Cinzel,serif;font-size:6pt;color:var(--acc);padding:0 0 .2mm}
.card table.ab td{text-align:center;border-top:.25mm solid var(--line);border-bottom:.25mm solid var(--line);padding:.35mm 0;line-height:1.1}
.card table.ab td b{font-size:8.8pt}
.card table.ab td span{display:block;font-size:6.2pt;color:#6b5236}
.card .props{font-size:7.9pt;line-height:1.25;margin-bottom:.8mm}
.card .props b{color:var(--acc)}
.card .props span{margin-right:2mm}
.card h2{font-family:Cinzel,serif;font-weight:700;font-size:8pt;color:var(--acc);border-bottom:.3mm solid var(--acc);margin:1mm 0 .8mm;padding-bottom:.2mm}
.card h2 em{font-family:'Crimson Pro',serif;font-style:italic;font-weight:400;font-size:6.6pt;color:#5d4630}
.card .f{margin-bottom:1mm;font-size:8pt;line-height:1.22}
.card .f .n{display:flex;flex-wrap:wrap;align-items:baseline;gap:.3mm 1.2mm;margin-bottom:.1mm}
.card .f .n b{font-size:8.8pt;font-weight:700}
.card .f .n .tag{font-size:6.9pt;color:#6b5236;font-style:italic}
.card .dice{font-size:7.5pt;border-radius:.9mm;padding:0 1.1mm;line-height:1.45}
.card .f p{color:#3a2a1b}
.card .box{border:.3mm solid var(--acc);background:rgba(255,255,255,.45);border-radius:1.2mm;padding:1mm 1.6mm;margin:1mm 0;font-size:7.5pt;line-height:1.22}
.card .box h3{font-family:Cinzel,serif;font-size:7.4pt;color:var(--acc);margin-bottom:.3mm}
.card .foot{position:absolute;left:4mm;right:4mm;bottom:1.6mm;font-size:5.6pt;color:#7a6145;display:flex;justify-content:space-between;border-top:.25mm solid var(--line);padding-top:.4mm}
"""

def img64(p):
    return "data:image/%s;base64,%s" % ("png" if p.endswith(".png") else "jpeg", base64.b64encode(open(p,"rb").read()).decode())
def mod(v): m=(v-10)//2; return ("+%d"%m) if m>=0 else "−%d"%(-m)
def ab(s,d,c,i,w,ch, saves={}):
    rows=[]
    for k,v in zip(("STR","GES","KON","INT","WEI","CHA"),(s,d,c,i,w,ch)):
        rows.append((k,str(v),mod(v),saves.get(k,mod(v))))
    return rows
def ab_table(rows):
    th = "".join(f"<th>{k}</th>" for k,_,_,_ in rows)
    td = "".join(f"<td><b>{v}</b> ({m})<span>RW {s}</span></td>" for _,v,m,s in rows)
    return f'<table class="ab"><tr>{th}</tr><tr>{td}</tr></table>'
def feat(name, dice=(), tag="", text=""):
    d = "".join(f'<span class="dice">{x}</span>' for x in dice)
    tag = ohne_buch(tag)
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="f"><div class="n"><b>{name}</b>{t}{d}</div><p>{text}</p></div>'
import re
def box(title, text): return ""   # seit 1.11.2026: keine Infokästen mehr auf den Bögen (Wunsch Christoph); Texte bleiben in den Datendateien
def ohne_buch(s): return re.split(r"\s*[·;]\s*(?:\d+ im |im Buch)", s)[0]   # Hinweise «im Buch: …» aus Untertiteln/Tags weglassen
XP = {"1/8":"25 EP","1/4":"50 EP","1/2":"100 EP","1":"200 EP","2":"450 EP","3":"700 EP","4":"1 100 EP","5":"1 800 EP","6":"2 300 EP","7":"2 900 EP","8":"3 900 EP","9":"5 000 EP","11":"7 200 EP","13":"10 000 EP","16":"15 000 EP","23":"50 000 EP"}
MH = "Werte: Monsterhandbuch 2024 (SRD 5.2)"; MOTM = "Werte: Monsters of the Multiverse"

def hero_img(m):   # Bogen ohne Bild (img=None): leerer Kopf in der Akzentfarbe
    return f'<img src="{img64(os.path.join(IMG,m['img']))}">' if m.get("img") else ""
def hero_style(m):
    return "" if m.get("img") else ' style="background:linear-gradient(160deg,%s 0%%,#1a1410 100%%)"' % m["acc"]

def page_a4(m):
    core = "".join(f"<div><small>{a}</small><b>{b}</b> <i>{c}</i></div>" for a,b,c in m["core"])
    props = "".join(f"<p><b>{k}</b> {v}</p>" for k,v in m["props"])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{m['name']}</title><style>{CSS_A4}
:root{{--acc:{m['acc']};--line:{m['line']};--hh:{m['hh']};--pos:{m['pos']};--ch:{m['ch']}}}</style></head><body><div class="page">
<div class="hero"{hero_style(m)}>{hero_img(m)}<div class="title"><div><h1>{m['name']}</h1><div class="sub">{ohne_buch(m['sub'])}</div></div>
<div class="hg">HG<b>{m['hg']}</b>{m.get('xp',XP[m['hg']])}</div></div></div>
<div class="body"><div class="core">{core}</div>{ab_table(m['ab'])}<div class="props">{props}</div>
<div class="cols">{m['cols']}</div></div>
<div class="foot"><span>{m['quelle']}</span><span>Oneshot «Die letzte Grosstat»</span></div>
</div></body></html>"""

def card_q(m):
    core = "".join(f"<div><small>{a}</small><b>{b}</b> <i>{c}</i></div>" for a,b,c in m["core"])
    props = " ".join(f"<span><b>{k}</b> {v}</span>" for k,v in m["props"])
    return f"""<div class="card" style="--acc:{m['acc']};--line:{m['line']};--pos:{m.get('pos','50% 40%')}">
<div class="hero"><img src="{img64(os.path.join(IMG,m['img']))}"><div class="title"><div><h1>{m['name']}</h1><div class="sub">{ohne_buch(m['sub'])}</div></div>
<div class="hg">HG<b>{m['hg']}</b>{XP[m['hg']]}</div></div></div>
<div class="body"><div class="core">{core}</div>{ab_table(m['ab'])}<div class="props">{props}</div>{m['cols']}</div>
<div class="foot"><span>{m['quelle']}</span><span>«Die letzte Grosstat»</span></div></div>"""

def sheet_q(title, cards):
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{title}</title><style>{CSS_Q}</style></head><body><div class="sheet">{''.join(card_q(c) for c in cards)}</div></body></html>"""

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten_a4.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "daten_klein.py"), encoding="utf-8").read())

only = set(sys.argv[3:])
for key, m in A4:
    if only and key not in only: continue
    open(os.path.join(OUT, key + ".html"), "w", encoding="utf-8").write(page_a4(m)); print("html", key)
for key, title, cards in KLEIN:
    if only and key not in only: continue
    open(os.path.join(OUT, key + ".html"), "w", encoding="utf-8").write(sheet_q(title, cards)); print("html", key)
