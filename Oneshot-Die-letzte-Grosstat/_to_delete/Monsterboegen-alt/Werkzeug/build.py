# Baut die A4-Monsterbögen (HTML -> PDF + PNG). Aufruf: python3 build.py <bildordner> <ausgabeordner>
import sys, os, base64, html
IMG, OUT = sys.argv[1], sys.argv[2]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm}
body{font-family:'Crimson Pro',serif;color:#2a1d12;background:#f3e9d2;-webkit-print-color-adjust:exact;print-color-adjust:exact}
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
.dice{display:inline-block;background:#2a1d12;color:#ffe9b8;font-weight:600;font-size:9pt;border-radius:1.2mm;padding:0 1.6mm;line-height:1.5}
.dice + .dice{margin-left:0}
.f p{color:#3a2a1b}
.box{break-inside:avoid;border:.45mm solid var(--acc);background:rgba(255,255,255,.45);border-radius:1.6mm;padding:1.6mm 2.4mm;margin:1.6mm 0;font-size:9pt;line-height:1.24}
.box h3{font-family:Cinzel,serif;font-size:9pt;color:var(--acc);margin-bottom:.6mm}
.box h3 .nb{font-family:"Crimson Pro",serif;font-weight:700}
.foot{position:absolute;left:9mm;right:9mm;bottom:3.6mm;font-size:7.4pt;color:#7a6145;display:flex;justify-content:space-between;border-top:.3mm solid var(--line);padding-top:.8mm}
"""

def img64(p):
    return "data:image/%s;base64,%s" % ("png" if p.endswith(".png") else "jpeg", base64.b64encode(open(p,"rb").read()).decode())

def ab_table(ab):
    th = "".join(f"<th>{k}</th>" for k,_,_,_ in ab)
    td = "".join(f"<td><b>{v}</b> ({m})<span>RW {s}</span></td>" for _,v,m,s in ab)
    return f'<table class="ab"><tr>{th}</tr><tr>{td}</tr></table>'

def feat(name, dice=(), tag="", text=""):
    d = "".join(f'<span class="dice">{x}</span>' for x in dice)
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<div class="f"><div class="n"><b>{name}</b>{t}{d}</div><p>{text}</p></div>'

def page(m):
    core = "".join(f"<div><small>{a}</small><b>{b}</b> <i>{c}</i></div>" for a,b,c in m["core"])
    props = "".join(f"<p><b>{k}</b> {v}</p>" for k,v in m["props"])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{m['name']}</title><style>{CSS}
:root{{--acc:{m['acc']};--line:{m['line']};--hh:{m['hh']};--pos:{m['pos']};--ch:{m['ch']}}}</style></head><body><div class="page">
<div class="hero"><img src="{img64(m['img'])}"><div class="title"><div><h1>{m['name']}</h1><div class="sub">{m['sub']}</div></div>
<div class="hg">HG<b>{m['hg']}</b>{m['xp']}</div></div></div>
<div class="body">{'<div class="core">'+core+'</div>'}{ab_table(m['ab'])}<div class="props">{props}</div>
<div class="cols">{m['cols']}</div></div>
<div class="foot"><span>{m['quelle']}</span><span>Oneshot «Die letzte Grosstat»</span></div>
</div></body></html>"""

# ---------------- Uralter Silberdrache ----------------
drache = dict(
 name="Argentys", sub="Uralter Silberdrache · Gigantischer Drache (metallisch), rechtschaffen gut",
 hg="23", xp="50 000 EP<br>Hort 62 000", acc="#2f4f6b", line="#9fb2c2", hh="92mm", pos="50% 30%", ch="144mm",
 img=os.path.join(IMG, "drache.png"),
 quelle="Werte: Monsterhandbuch 2024 (SRD 5.2), Uralter Silberdrache · Übungsbonus +7",
 core=[("Rüstungsklasse","22",""),("Trefferpunkte","468","(24W20+216)"),("Initiative","+14","(24)"),("Bewegung","12 m","Fliegen 24 m")],
 ab=[("STR","30","+10","+10"),("GES","10","+0","+7"),("KON","29","+9","+9"),("INT","18","+4","+4"),("WEI","15","+2","+9"),("CHA","26","+8","+8")],
 props=[("Fertigkeiten","Geschichte +11, Wahrnehmung +16, Heimlichkeit +7"),
        ("Immunitäten","Kälte"),
        ("Sinne","Blindsicht 18 m, Dunkelsicht 36 m, passive Wahrnehmung 26"),
        ("Sprachen","Gemeinsprache, Drakonisch")],
 cols="".join([
  "<h2>Merkmale</h2>",
  feat("Legendäre Resistenz", ("4/Tag",), "im Hort 5/Tag", "Misslingt ihr ein Rettungswurf, kann sie stattdessen entscheiden, dass er gelingt."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3× Zerfetzen",), "", "Einen Angriff darf sie ersetzen durch <b>Lähmungsodem</b> oder durch <b>Eismesser</b> (Zauberwirken)."),
  feat("Zerfetzen", ("+17","2W8+10 Hieb","+ 2W8 Kälte"), "Nahkampf, Reichweite 4,5 m", "Ø 19 Hieb + 9 Kälte pro Treffer."),
  feat("Kälteodem", ("RW KON 24","15W8 Kälte"), "Aufladung 5–6 · Kegel 27 m", "Ø 67 Kälte. Erfolg: halber Schaden."),
  feat("Lähmungsodem", ("RW KON 24","kampfunfähig → gelähmt"), "Kegel 27 m", "1. Misserfolg: kampfunfähig bis zum Ende ihres nächsten Zuges, dann neuer Rettungswurf. 2. Misserfolg: gelähmt; neuer Rettungswurf am Ende jedes eigenen Zuges, nach 1 Minute automatisch Erfolg."),
  feat("Zauberwirken", ("SG 23","Zauberangriff +15"), "Charisma, keine Materialkomponenten", "<b>Beliebig oft:</b> Magie entdecken, Monster festhalten, Eismesser (Grad 2), Gestaltwandel (nur Tier oder Humanoide, ohne temporäre TP, ohne Konzentration).<br><b>Je 1/Tag:</b> Wetterkontrolle, Eissturm (Grad 7), Teleportieren, Zone der Wahrheit."),
  feat("Eismesser", ("+15","1W10 Stich","RW GES 23","3W6 Kälte"), "Zauber Grad 2 · 18 m", "Splitter trifft ein Ziel, dann Explosion: das Ziel und alle in 1,5 m um es, Rettungswurf sonst 3W6 Kälte (auch bei Fehlschlag des Angriffs)."),
  feat("Monster festhalten", ("RW WEI 23","gelähmt"), "Zauber · 27 m · Konzentration", "Gelähmt bis 1 Minute; neuer Rettungswurf am Ende jedes eigenen Zuges."),
  feat("Eissturm", ("RW GES 23","5W10 Wucht","+ 4W6 Kälte"), "1/Tag · Grad 7 · Zylinder Radius 6 m", "Reichweite 90 m. Erfolg: halber Schaden. Der Boden ist bis zum Ende ihres nächsten Zuges schwieriges Gelände."),
  "<h2>Legendäre Aktionen <em>3 pro Runde (im Hort 4), direkt nach dem Zug einer anderen Kreatur</em></h2>",
  feat("Frosthauch", ("RW WEI 23","gelähmt"), "", "Wirkt <b>Monster festhalten</b>. Erst wieder ab Beginn ihres nächsten Zuges."),
  feat("Kältesturm", ("RW GES 23","4W6 Kälte","9 m weg"), "Linie 18 m × 3 m", "Misserfolg: Schaden und 9 m von ihr weggestossen. Erfolg: halber Schaden, kein Stoss. Erst wieder ab Beginn ihres nächsten Zuges."),
  feat("Ansprung", ("½ Bewegung","Zerfetzen +17"), "", "Bewegt sich bis zur halben Geschwindigkeit und macht einen Zerfetzen-Angriff (2W8+10 Hieb + 2W8 Kälte)."),
  '<div class="box"><h3>Im Oneshot</h3>Argentys, die Sturmhüterin. Kämpft in Kapitel 4 gegen Grollhorn, geführt von einem Spieler (siehe Spieler-Handout). Bei 0 TP zieht sie sich ins Sturmgebiet zurück, sie stirbt nicht. Nicht gegen Urgash, Skrall oder Kazzamir.</div>',
 ]))

# ---------------- Höllenfeuer-Maschine ----------------
maschine = dict(
 name="Grollhorn", sub="Höllenfeuer-Maschine · Riesiges Konstrukt, typischerweise rechtschaffen böse",
 hg="16", xp="15 000 EP", acc="#7a2410", line="#c9a27c", hh="114mm", pos="50% 40%", ch="112mm",
 img=os.path.join(IMG, "maschine.png"),
 quelle="Werte: Monsters of the Multiverse, Hellfire Engine · Übungsbonus +5",
 core=[("Rüstungsklasse","18",""),("Trefferpunkte","216","(16W12+112)"),("Initiative","+3","(13)"),("Bewegung","12 m","")],
 ab=[("STR","20","+5","+5"),("GES","16","+3","+8"),("KON","24","+7","+7"),("INT","2","−4","−4"),("WEI","10","+0","+5"),("CHA","1","−5","+0")],
 props=[("Resistenzen","Kälte, Psycho; Hieb, Stich, Wucht von nichtmagischen, nicht versilberten Angriffen"),
        ("Immunitäten","Feuer, Gift"),
        ("Zustandsimmunitäten","Bezaubert, Erschöpft, Gelähmt, Taub, Verängstigt, Vergiftet, Bewusstlos"),
        ("Sinne","Dunkelsicht 36 m, passive Wahrnehmung 10"),
        ("Sprachen","versteht Infernalisch, spricht nicht")],
 cols="".join([
  "<h2>Merkmale</h2>",
  feat("Unveränderliche Gestalt", (), "", "Immun gegen jeden Zauber und Effekt, der ihre Gestalt verändern würde."),
  feat("Magieresistenz", ("Vorteil",), "", "Vorteil auf Rettungswürfe gegen Zauber und andere magische Effekte."),
  feat("Ungewöhnliche Natur", (), "", "Braucht weder Luft, Nahrung, Wasser noch Schlaf."),
  "<h2>Aktionen <em>Fleischbrecherschritt und eine Höllenwaffe</em></h2>",
  feat("Fleischbrecherschritt", ("RW GES 18","8W6 Wucht","liegend"), "Bewegung in gerader Linie", "Fährt bis zu ihrer Geschwindigkeit geradeaus und darf Felder von grossen oder kleineren Kreaturen betreten. Erfolg: aufs nächste freie Feld neben dem Weg geschoben. Misserfolg: liegend, Ø 28 Wucht. Bleibt sie auf dem Feld stehen, ist die Kreatur festgesetzt; befreien mit <b>STR-Wurf SG 18</b> (selbst oder jemand in 1,5 m)."),
  "<h2>Höllenwaffen <em>eine wählen oder W6 würfeln</em></h2>",
  feat("1–2 Knochenschmelzer", ("RW GES 20","2W10 Feuer","+ 4W8 Säure"), "Kegel 18 m", "Ø 11 Feuer + 18 Säure, Erfolg halb. Bei Misserfolg <b>brennt</b> das Ziel: am Ende jedes eigenen Zuges <span class=\"dice\">1W10 Feuer + 2W8 Säure</span>, bis es oder jemand in 1,5 m mit einer Aktion das Öl abkratzt."),
  feat("3–4 Blitzflegel", ("+10","3W8+5 Wucht","+ 5W8 Blitz"), "Nahkampf, Reichweite 4,5 m", "Ø 18 Wucht + 22 Blitz. Dazu bis zu drei weitere Kreaturen in 9 m um das Ziel: <span class=\"dice\">RW GES 20 · 5W8 Blitz</span>, Erfolg halb."),
  feat("5–6 Donnerkanone", ("RW GES 20","5W10 Wucht","+ 3W12 Donner"), "Punkt in 36 m, Radius 9 m", "Ø 27 Wucht + 19 Donner, Erfolg halb."),
  feat("Höllenfluch", (), "bei jeder Höllenwaffe", "Wer durch eine Höllenwaffe stirbt, steigt in 1W4 Stunden als Lemure in Avernus auf. Danach helfen nur <i>Wunsch</i> oder: Lemure töten und <i>Wahre Wiederbelebung</i> auf den Körper. Konstrukte und Teufel sind immun."),
  '<div class="box"><h3>Hausregel Oneshot: Der Kessel</h3><b>RK 12 · 60 TP</b> · Wucht und Donner doppelt · immun gegen Feuer, Gift, Psycho. '
  'Birst er: <span class="dice">6W6 Feuer · 6 m · RW GES 14 halb</span>, Feuer am Boden 3 Runden (schwieriges Gelände, 2W6 Feuer beim Betreten), Maschine steht 2 Runden später still. '
  'Alle 4 Bombardiere tot: Kessel läuft in 3 Runden leer. Jede Runde: eine Höllenwaffe ins Heer (−1 Schlachtenleiste) und Schritt geradeaus; schiesst auf Argentys, solange sie über ihr ist.</div>',
 ]))

# ---------------- Nadel (Assassine) ----------------
nadel = dict(
 name="Nadel", sub="Assassine · Mittelgrosser Humanoide, neutral · Meuchlerin der Horde",
 hg="8", xp="3 900 EP", acc="#3d4a3a", line="#a9b39c", hh="118mm", pos="50% 35%", ch="124mm",
 img=os.path.join(IMG, "nadel.png"),
 quelle="Werte: Monsterhandbuch 2024 (SRD 5.2), Assassine · Übungsbonus +3",
 core=[("Rüstungsklasse","16",""),("Trefferpunkte","97","(15W8+30)"),("Initiative","+10","(20)"),("Bewegung","9 m","")],
 ab=[("STR","11","+0","+0"),("GES","18","+4","+7"),("KON","14","+2","+2"),("INT","16","+3","+6"),("WEI","11","+0","+0"),("CHA","10","+0","+0")],
 props=[("Fertigkeiten","Akrobatik +7, Wahrnehmung +6, Heimlichkeit +10"),
        ("Resistenzen","Gift"),
        ("Sinne","passive Wahrnehmung 16"),
        ("Sprachen","Gemeinsprache, Diebessprache"),
        ("Ausrüstung","Leichte Armbrust, Kurzschwert, beschlagenes Leder")],
 cols="".join([
  "<h2>Merkmale</h2>",
  feat("Entrinnen", ("RW GES gelungen = 0",), "", "Bei einem Effekt mit GES-Rettungswurf für halben Schaden: Erfolg kein Schaden, Misserfolg nur halber Schaden. Nicht, solange sie kampfunfähig ist."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3 Angriffe",), "", "Drei Angriffe mit Kurzschwert oder Leichter Armbrust, beliebig gemischt."),
  feat("Kurzschwert", ("+7","1W6+4 Stich","+ 5W6 Gift","vergiftet"), "Nahkampf, Reichweite 1,5 m", "Ø 7 Stich + 17 Gift. Das Ziel ist vergiftet bis zum Beginn ihres nächsten Zuges."),
  feat("Leichte Armbrust", ("+7","1W8+4 Stich","+ 6W6 Gift"), "Fernkampf, 24/96 m", "Ø 8 Stich + 21 Gift."),
  "<h2>Bonusaktionen</h2>",
  feat("Raffinierte Aktion", ("Spurt · Rückzug · Verstecken",), "", "Sie spurtet, zieht sich zurück oder versteckt sich."),
  '<div class="box"><h3>Im Oneshot: Hinterhalt im Fluchtgang <span class="nb">(Kapitel 1b)</span></h3>Hängt in den Wurzeln über dem Eingang der Wurzelkammer. '
  '<span class="dice">Wahrnehmung SG 15</span> «Da hängt was in den Wurzeln»: wer besteht, ist nicht überrascht (überrascht = Nachteil auf Initiative). '
  'Erster Zug: drei Kurzschwert-Angriffe auf den ersten Helden in der Kammer, bis zu ~70 Schaden. Dann Armbrust aus dem Dunkeln. Dazu 2 Bugbear-Pirscher hinter den Felsbrocken und Pitt am blinden Spalt. Fallen beide Pirscher, flieht sie mit Raffinierter Aktion.</div>',
  '<div class="box"><h3>Leichtere Variante: Bugbear-Pirscher (HG 3)</h3><b>RK 15 · 65 TP (10W8+20) · 9 m</b> · Mehrfachangriff: 2× Wurfspeer oder Morgenstern.<br>'
  '<b>Wurfspeer</b> <span class="dice">+5 · 3W6+3 Stich</span> Reichweite 3 m oder 9/36 m. '
  '<b>Morgenstern</b> <span class="dice">+5 · 2W8+3 Stich</span> Reichweite 3 m, Vorteil gegen Gepackte. '
  '<b>Schneller Griff</b> (Bonusaktion) <span class="dice">RW GES 13 · gepackt</span> (Entkommen SG 13). Dazu nur ein Pirscher, Pitt kämpft nicht.</div>',
 ]))

# ---------------- Bugbear-Krieger ----------------
bugbear = dict(
 name="Pitt", sub="Bugbear-Krieger · Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · der Spion der Horde",
 hg="1", xp="200 EP", acc="#6b4a1f", line="#c7ad83", hh="136mm", pos="50% 45%", ch="70mm",
 img=os.path.join(IMG, "bugbear.png"),
 quelle="Werte: Monsterhandbuch 2024 (SRD 5.2), Bugbear-Krieger · Übungsbonus +2",
 core=[("Rüstungsklasse","14",""),("Trefferpunkte","33","(6W8+6)"),("Initiative","+2","(12)"),("Bewegung","9 m","")],
 ab=[("STR","15","+2","+2"),("GES","14","+2","+2"),("KON","13","+1","+1"),("INT","8","−1","−1"),("WEI","11","+0","+0"),("CHA","9","−1","−1")],
 props=[("Fertigkeiten","Heimlichkeit +6, Überleben +2"),
        ("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),
        ("Sprachen","Gemeinsprache, Goblinisch"),
        ("Ausrüstung","Fellrüstung, 3 leichte Hämmer")],
 cols="".join([
  "<h2>Merkmale</h2>",
  feat("Entführen", ("keine Extra-Bewegung",), "", "Braucht keine zusätzliche Bewegung, um eine Kreatur zu bewegen, die es gepackt hält."),
  "<h2>Aktionen <em>kein Mehrfachangriff, ein Angriff pro Zug</em></h2>",
  feat("Packen", ("+4","2W6+2 Wucht","gepackt"), "Nahkampf, Reichweite 3 m", "Ø 9 Wucht. Ein mittelgrosses oder kleineres Ziel ist gepackt (Entkommen SG 12)."),
  feat("Leichter Hammer", ("+4","3W4+2 Wucht"), "Nah- oder Fernkampf, 3 m oder 6/18 m", "Ø 9 Wucht. <b>Vorteil</b>, wenn es das Ziel selbst gepackt hält."),
  '<div class="box"><h3>Im Oneshot: Pitt am blinden Spalt <span class="nb">(Kapitel 1b)</span></h3>Pitt kommt nachts durch den alten Fluchtgang, den in der Burg niemand kannte, in den Keller zu Toms Labor und steht dort am Koffer. Entdeckt, flieht er durch die Luke. '
  'In der Wurzelkammer steht er mit Toms Tasche am blinden Spalt und kämpft halbherzig mit (Packen, Leichter Hammer). Kettennarbe am Handgelenk. '
  '<span class="dice">Fällt Nadel oder unter 15 TP</span> lässt er den Hammer fallen und ergibt sich. Hat Nadel die Tasche, flieht er in den Ausgangsgang. Leichtere Variante: Pitt kämpft nicht.</div>',
  ]))

# ---------------- Bugbear-Pirscher ----------------
pirscher = dict(
 name="Bugbear-Pirscher", sub="Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · 2 Stück im Fluchtgang",
 hg="3", xp="700 EP", acc="#5a3b22", line="#c2a27f", hh="124mm", pos="50% 45%", ch="80mm",
 img=os.path.join(IMG, "pirscher.png"),
 quelle="Werte: Monsterhandbuch 2024 (SRD 5.2), Bugbear-Pirscher · Übungsbonus +2",
 core=[("Rüstungsklasse","15",""),("Trefferpunkte","65","(10W8+20)"),("Initiative","+2","(12)"),("Bewegung","9 m","")],
 ab=[("STR","17","+3","+3"),("GES","14","+2","+2"),("KON","14","+2","+4"),("INT","11","+0","+0"),("WEI","12","+1","+3"),("CHA","11","+0","+0")],
 props=[("Fertigkeiten","Heimlichkeit +6, Überleben +3"),
        ("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 11"),
        ("Sprachen","Gemeinsprache, Goblinisch"),
        ("Ausrüstung","Kettenhemd, 6 Wurfspeere, Morgenstern")],
 cols="".join([
  "<h2>Merkmale</h2>",
  feat("Entführen", ("keine Extra-Bewegung",), "", "Braucht keine zusätzliche Bewegung, um eine Kreatur zu bewegen, die es gepackt hält."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("2 Angriffe",), "", "Zwei Angriffe mit Wurfspeer oder Morgenstern."),
  feat("Wurfspeer", ("+5","3W6+3 Stich"), "Nah- oder Fernkampf, 3 m oder 9/36 m", "Ø 13 Stich."),
  feat("Morgenstern", ("+5","2W8+3 Stich"), "Nahkampf, Reichweite 3 m", "Ø 12 Stich. <b>Vorteil</b>, wenn es das Ziel selbst gepackt hält."),
  "<h2>Bonusaktionen</h2>",
  feat("Schneller Griff", ("RW GES 13","gepackt"), "eine Kreatur bis mittelgross in 3 m", "Misserfolg: gepackt (Entkommen SG 13)."),
  '<div class="box"><h3>Im Oneshot: hinter den Felsbrocken <span class="nb">(Kapitel 1b)</span></h3>Zwei Pirscher warten hinter zwei Felsbrocken (halbe Deckung, +2 RK) und greifen an, sobald Nadel zugeschlagen hat. '
  'Taktik: Schneller Griff, mit Entführen hinter den Felsen zerren, dort zweimal Morgenstern mit Vorteil. Sie fliehen nicht. Leichtere Variante: nur einer.</div>',
 ]))

for key, m in (("01-Uralter-Silberdrache-Argentys", drache), ("02-Hoellenfeuer-Maschine-Grollhorn", maschine), ("03-Assassine-Nadel", nadel), ("04-Bugbear-Krieger", bugbear), ("05-Bugbear-Pirscher", pirscher)):
    open(os.path.join(OUT, key + ".html"), "w").write(page(m))
    print("html", key)
