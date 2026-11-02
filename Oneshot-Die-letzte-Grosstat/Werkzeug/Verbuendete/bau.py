# Baut die Nordgar-Karte mit Infoboxen zu den Verbündeten und je eine A4-Karte pro Hauptmann.
# Texte kommen aus dem Buch (NPC/Die-Verbuendeten/Beschreibung.md und Stats/Stats.md,
# NPC/Marschallin-Hedda/Beschreibung.md und Stats/Stats.md). Nichts wird hier neu erfunden.
# Aufruf: python3 bau.py <ausgabeordner>   danach: node render.js <ausgabeordner>
import sys, os, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)

def lese(rel): return open(os.path.join(ROOT, rel), encoding='utf-8').read()
def md2html(t):
    t = re.sub(r'\s*\((?:→|->)[^)]*\)', '', t)          # (→ Datei) Verweise weg
    t = re.sub(r'`[^`]*`', '', t)
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)\*', r'<i>\1</i>', t)
    return re.sub(r'\s*\n\s*', ' ', t).strip()
def absaetze(block):
    return [md2html(a) for a in re.split(r'\n\s*\n', block.strip()) if a.strip() and not a.strip().startswith('<img') and not re.match(r'^\*[^*]+\*$', a.strip()) and not a.strip().startswith('Werte →') and not a.strip().startswith('Beschreibung →')]
def abschnitt(text, titel_re):
    m = re.search(r'^## (' + titel_re + r')[^\n]*\n(.*?)(?=^## |\Z)', text, re.S | re.M)
    return m.group(2) if m else ''
def stats(block):
    tab = re.findall(r'^\| ([^|]+?) \| ([^|]*?) \|$', block, re.M)
    d = {}
    for a, b in tab:
        if a.strip() == '': continue
        d[a.strip()] = b.strip()
    # Attribute stehen als "STR 18 (+4) | GES 12 (+1)"
    attr = re.findall(r'(STR|GES|KON|INT|WEI|CHA) (\d+) \(([+−-]\d+)\)', block)
    feats = [md2html(a) for a in re.split(r'\n(?=\*\*|\*Kriegspferd)|\n\s*\n', block) if a.strip().startswith('**') or a.strip().startswith('*Kriegspferd')]
    return d, attr, feats

verb_b = lese('NPC/Die-Verbuendeten/Beschreibung.md')
verb_s = lese('NPC/Die-Verbuendeten/Stats/Stats.md')
hed_b = lese('NPC/Marschallin-Hedda/Beschreibung.md')
hed_s = lese('NPC/Marschallin-Hedda/Stats/Stats.md')

LEUTE = [
 dict(key='02-Marschallin-Hedda', name='Marschallin Hedda Eisenbrecht', kurz='Hedda Eisenbrecht', titel='Marschallin', land='Nordgar', truppe='Oberbefehlshaberin des letzten Heeres Nordgars',
      bild='Bilder/Marschallin-Hedda.png', acc='#3b4a5c', line='#9aa6b4', kampf='Langschwert und Schild, Plattenrüstung',
      text=absaetze(hed_b.split('## Erscheinung & Wesen',1)[1]) if '## Erscheinung' in hed_b else [], st=stats(hed_s),
      pos=dict(left='2.5%', top='64.5%', width='29%'), punkt=(34.8, 57.5), richtung='Burg Rabenwacht'),
 dict(key='03-Aurel-Vanthis', name='Ritter Aurel Vanthis', kurz='Aurel Vanthis', titel='Ritter', land='Sildoras', truppe='Hauptmann der Sonnenlanzen (Reiterei)',
      bild='Bilder/Aurel-Vanthis.png', acc='#8b2a1f', line='#c99a8a', kampf='Sonnenlanze, zu Pferd',
      text=absaetze(abschnitt(verb_b, 'Sildoras')), st=stats(abschnitt(verb_s, 'Ritter Aurel Vanthis')),
      pos=dict(left='35%', top='86.2%', width='31%'), richtung='Weinland im Süden, jenseits der Südberge'),
 dict(key='04-Brannok-Grauhammer', name='Brannok Grauhammer', kurz='Brannok Grauhammer', titel='Hauptmann', land='Dhurgan', truppe='Hauptmann der Hammergarde (Zwerge)',
      bild='Bilder/Brannok-Grauhammer.png', acc='#5a3b22', line='#c2a27f', kampf='Grauhammer (Schlachthammer)',
      text=absaetze(abschnitt(verb_b, 'Dhurgan')), st=stats(abschnitt(verb_s, 'Brannok Grauhammer')),
      pos=dict(left='2.5%', top='32%', width='29%'), richtung='Zwergenfeste im Westgebirge'),
 dict(key='05-Thuluk-Wolkentreter', name='Thuluk Wolkentreter', kurz='Thuluk Wolkentreter', titel='Anführer', land='Skarn', truppe='Anführer der Goliaths vom Hochland',
      bild='Bilder/Thuluk-Wolkentreter.png', acc='#4a5a4a', line='#a8b4a6', kampf='Riesenaxt, wirft Felsen',
      text=absaetze(abschnitt(verb_b, 'Skarn')), st=stats(abschnitt(verb_s, 'Thuluk Wolkentreter')),
      pos=dict(left='2.5%', top='6.5%', width='29%'), richtung='Hochtäler über der Baumgrenze'),
 dict(key='06-Sarenne-Ilwyn', name='Hauptfrau Sarenne Ilwyn', kurz='Sarenne Ilwyn', titel='Hauptfrau', land='Thalvien', truppe='Hauptfrau der Grünpfeile (Halbelfen)',
      bild='Bilder/Sarenne-Ilwyn.png', acc='#2f5a2f', line='#9db89b', kampf='Langbogen',
      text=absaetze(abschnitt(verb_b, 'Thalvien')), st=stats(abschnitt(verb_s, 'Hauptfrau Sarenne Ilwyn')),
      pos=dict(left='68.5%', top='61%', width='29%'), richtung='Waldreich im Südosten, jenseits des Sturmgebiets'),
]
for p in LEUTE:
    assert p['text'] and p['st'][0].get('RK') and p['st'][0].get('TP'), p['key']
    p['rk'] = p['st'][0]['RK'].split(' (')[0]; p['tp'] = p['st'][0]['TP']

FONTS = "@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');"
BASE = FONTS + """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm}
body{font-family:'Crimson Pro',serif;color:#2a1d12;background:#f3e9d2;-webkit-print-color-adjust:exact;print-color-adjust:exact}
"""
from PIL import Image
def img(rel, breite=1100):
    # Bilder verkleinert als JPG neben die HTML-Dateien legen, damit die PDFs klein bleiben
    if rel.endswith('.png') and rel.startswith('Bilder/'):
        ziel = os.path.join(OUT, '_%s-%d.jpg' % (os.path.basename(rel)[:-4], breite))
        if not os.path.exists(ziel):
            im = Image.open(os.path.join(ROOT, rel)).convert('RGB'); im.thumbnail((breite, breite*2)); im.save(ziel, quality=86)
        return 'file://' + ziel
    return 'file://' + os.path.join(ROOT, rel)

# ---------- 1. Die Karte mit Infoboxen ----------
CSS_MAP = BASE + """
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#1d1510}
.map{position:absolute;left:0;top:0;width:210mm;height:281.6mm;display:block}
.box{position:absolute;background:rgba(246,236,214,.94);border:.55mm solid var(--acc);border-radius:2mm;padding:1.6mm 2.2mm 1.8mm 2.2mm;
 box-shadow:0 1mm 3mm rgba(0,0,0,.45);display:grid;grid-template-columns:15mm 1fr;gap:0 2.2mm;align-items:start}
.box img{width:15mm;height:19mm;object-fit:cover;object-position:50% 12%;border:.4mm solid var(--acc);border-radius:1.4mm;grid-row:1/4;background:#ddd}
.box .land{font-family:Cinzel,serif;font-weight:900;font-size:10pt;color:var(--acc);letter-spacing:.3pt;line-height:1.05}
.box .name{font-weight:700;font-size:9.6pt;line-height:1.1;margin-top:.5mm}
.box .truppe{font-style:italic;font-size:7.6pt;color:#5d4630;line-height:1.15;margin-top:.3mm}
.box .wo{font-size:7.4pt;color:#5d4630;line-height:1.15;margin-top:.6mm;grid-column:1/3}
.box .kampf{font-size:8.2pt;line-height:1.15;margin-top:.8mm;grid-column:1/3}
.box .kampf b{color:var(--acc)}
.box .werte{grid-column:1/3;display:flex;gap:1.6mm;margin-top:1.2mm}
.box .werte div{flex:1;background:var(--acc);color:#fff;border-radius:1.2mm;text-align:center;padding:.6mm 0;line-height:1.05}
.box .werte small{display:block;font-family:Cinzel,serif;font-size:5.6pt;letter-spacing:.5pt;opacity:.9}
.box .werte b{font-size:11pt}
.punkt{position:absolute;width:4mm;height:4mm;border-radius:50%;border:.6mm solid #fff;background:var(--acc);box-shadow:0 0 2mm rgba(0,0,0,.6);transform:translate(-50%,-50%)}
.linie{position:absolute;height:0;border-top:.5mm dashed #fff;filter:drop-shadow(0 0 .6mm rgba(0,0,0,.8));transform-origin:0 0}
.legende{position:absolute;left:3mm;bottom:2.5mm;width:30%;font-size:7pt;line-height:1.2;color:#f3e9d2;opacity:.9}
"""
def box(p):
    return f"""<div class="box" style="--acc:{p['acc']};left:{p['pos']['left']};top:{p['pos']['top']};width:{p['pos']['width']}">
<img src="{img(p['bild'], 300)}" alt="">
<div class="land">{p['land']}</div>
<div class="name">{p['name']}</div>
<div class="truppe">{p['truppe']}</div>
<div class="wo">{p['richtung']}</div>
<div class="kampf"><b>Kämpft mit:</b> {p['kampf']}</div>
<div class="werte"><div><small>RK</small><b>{p['rk']}</b></div><div><small>TP</small><b>{p['tp']}</b></div></div>
</div>"""
hedda = LEUTE[0]
karte = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Nordgar und die Verbündeten</title><style>{CSS_MAP}</style></head><body>
<div class="page">
<img class="map" src="{img('Karten/04-Region-Nordgar.png')}" alt="Nordgar">
{''.join(box(p) for p in LEUTE)}
<div class="linie" style="left:{hedda['punkt'][0]}%;top:{hedda['punkt'][1]}%;width:9mm;transform:rotate(118deg)"></div>
<div class="punkt" style="--acc:{hedda['acc']};left:{hedda['punkt'][0]}%;top:{hedda['punkt'][1]}%"></div>
<div class="legende">Verbündete von Nordgar – Werte: Rüstungsklasse (RK) und Trefferpunkte (TP) aus dem Kampagnenbuch</div>
</div></body></html>"""
open(os.path.join(OUT, '01-Nordgar-Karte-Verbuendete.html'), 'w', encoding='utf-8').write(karte)

# ---------- 2. Eine A4-Karte pro Hauptmann ----------
CSS_CARD = BASE + """
.page{width:210mm;height:297mm;position:relative;overflow:hidden;--acc:#5a3b22;--line:#c2a27f;
 background:radial-gradient(ellipse at 50% 40%,#f8f0dc 0%,#efe1c0 70%,#e2cfa4 100%)}
.kopf{background:var(--acc);color:#fff;padding:5mm 9mm 4mm;display:flex;justify-content:space-between;align-items:flex-end;gap:4mm;border-bottom:1.2mm solid #2a1d12}
.kopf h1{font-family:Cinzel,serif;font-weight:900;font-size:22pt;line-height:1;letter-spacing:.3pt}
.kopf .sub{font-style:italic;font-size:11pt;margin-top:1.4mm;opacity:.95}
.kopf .land{font-family:Cinzel,serif;font-weight:700;font-size:9pt;text-align:center;border:.5mm solid #fff;border-radius:2mm;padding:1.2mm 3mm;white-space:nowrap;line-height:1.15}
.kopf .land b{display:block;font-size:15pt}
.body{display:grid;grid-template-columns:82mm 1fr;gap:0 7mm;padding:5mm 9mm 0 9mm}
.links img{width:82mm;height:108mm;object-fit:cover;object-position:50% 8%;display:block;border:.6mm solid var(--acc);border-radius:2mm;margin-bottom:3mm}
.links p{font-size:10.6pt;line-height:1.32;margin-bottom:1.8mm;text-align:justify;hyphens:auto}
.links p b{color:var(--acc)}
.rechts .core{display:grid;grid-template-columns:repeat(4,1fr);gap:2mm;margin-bottom:2.4mm}
.rechts .core div{background:var(--acc);color:#fff;border-radius:1.6mm;padding:1.2mm 1.5mm;text-align:center;line-height:1.1}
.rechts .core small{display:block;font-family:Cinzel,serif;font-size:6.4pt;letter-spacing:.5pt;opacity:.9}
.rechts .core b{font-size:13pt}
.rechts .core i{font-style:normal;font-size:7.6pt;opacity:.9;display:block}
table.ab{width:100%;border-collapse:collapse;margin-bottom:2mm;font-size:10pt}
table.ab th{font-family:Cinzel,serif;font-size:8pt;color:var(--acc);padding:0 0 .4mm}
table.ab td{text-align:center;border-top:.3mm solid var(--line);border-bottom:.3mm solid var(--line);padding:.6mm 0;line-height:1.15}
table.ab td b{font-size:11.5pt}
table.ab td span{display:block;font-size:8pt;color:#6b5236}
.props{font-size:10pt;line-height:1.3;margin-bottom:1.6mm}
.props p{margin-bottom:.4mm}
.props b{color:var(--acc)}
h2{font-family:Cinzel,serif;font-weight:700;font-size:10.5pt;color:var(--acc);border-bottom:.45mm solid var(--acc);margin:1.4mm 0 1.4mm;padding-bottom:.3mm}
.f{margin-bottom:2mm;font-size:10pt;line-height:1.3;color:#3a2a1b}
.f b{color:#2a1d12}
.f > b:first-child{font-size:10.8pt;color:var(--acc)}
.foot{position:absolute;left:9mm;right:9mm;bottom:3.6mm;font-size:7.4pt;color:#7a6145;display:flex;justify-content:space-between;border-top:.3mm solid var(--line);padding-top:.8mm}
"""
ZUS = ['Rettungswürfe', 'Fertigkeiten', 'Resistenzen', 'Sinne', 'Sprachen']
def card(p):
    d, attr, feats = p['st']
    core = [('Rüstungsklasse', p['rk'], d['RK'].split(' (')[1].rstrip(')') if ' (' in d['RK'] else ''),
            ('Trefferpunkte', p['tp'], ''), ('Bewegung', d.get('Bewegung','').split(' (')[0], d.get('Bewegung','').split(' (')[1].rstrip(')') if ' (' in d.get('Bewegung','') else ''),
            ('Herausforderung', d.get('HG','').split(' (')[0], d.get('HG','').split(' (')[1].rstrip(')') if ' (' in d.get('HG','') else '')]
    core_h = ''.join(f'<div><small>{a}</small><b>{b}</b><i>{c}</i></div>' for a,b,c in core)
    ab_h = '<table class="ab"><tr>' + ''.join(f'<th>{a}</th>' for a,_,_ in attr) + '</tr><tr>' + ''.join(f'<td><b>{v}</b><span>{m}</span></td>' for _,v,m in attr) + '</tr></table>'
    props = ''.join(f'<p><b>{k}:</b> {html.escape(d[k])}</p>' for k in ZUS if k in d)
    typ = html.escape(d.get('Typ',''))
    f_h = ''.join(f'<div class="f">{f}</div>' for f in feats)
    text = ''.join(f'<p>{t}</p>' for t in p['text'])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{p['name']}</title><style>{CSS_CARD}</style></head><body>
<div class="page" style="--acc:{p['acc']};--line:{p['line']}">
<div class="kopf"><div><h1>{p['name']}</h1><div class="sub">{p['truppe']} · {typ}</div></div><div class="land">Land<b>{p['land']}</b></div></div>
<div class="body">
<div class="links"><img src="{img(p['bild'])}" alt="{p['name']}">{text}</div>
<div class="rechts"><div class="core">{core_h}</div>{ab_h}<div class="props">{props}</div><h2>Kampf</h2>{f_h}</div>
</div>
<div class="foot"><span>Die letzte Großtat · Verbündete von Nordgar</span><span>Werte: Kampagnenbuch, NPC-Seiten</span></div>
</div></body></html>"""
for p in LEUTE:
    open(os.path.join(OUT, p['key'] + '.html'), 'w', encoding='utf-8').write(card(p))
print('HTML geschrieben:', len(LEUTE) + 1)
