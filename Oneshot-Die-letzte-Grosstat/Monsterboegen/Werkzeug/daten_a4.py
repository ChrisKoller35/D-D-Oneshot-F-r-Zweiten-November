# A4-Bögen, ein Monster pro Blatt.
def a4(name, sub, hg, acc, line, img, quelle, core, abil, props, cols, hh="110mm", ch="118mm", pos="50% 40%", xp=None):
    return dict(name=name, sub=sub, hg=hg, acc=acc, line=line, img=img, quelle=quelle, core=core, ab=abil, props=props, cols=cols, hh=hh, ch=ch, pos=pos, xp=xp or XP[hg])

# ---------------- Nymeria (bestehend) ----------------
drache = a4("Nymeria", "Uralter Silberdrache · Gigantischer Drache (metallisch), rechtschaffen gut", "23", "#2f4f6b", "#9fb2c2", "drache.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Uralter Silberdrache · Übungsbonus +7",
 [("Rüstungsklasse","22",""),("Trefferpunkte","468","(24W20+216)"),("Initiative","+14","(24)"),("Bewegung","12 m","Fliegen 24 m")],
 [("STR","30","+10","+10"),("GES","10","+0","+7"),("KON","29","+9","+9"),("INT","18","+4","+4"),("WEI","15","+2","+9"),("CHA","26","+8","+8")],
 [("Fertigkeiten","Geschichte +11, Wahrnehmung +16, Heimlichkeit +7"),("Immunitäten","Kälte"),("Sinne","Blindsicht 18 m, Dunkelsicht 36 m, passive Wahrnehmung 26"),("Sprachen","Gemeinsprache, Drakonisch")],
 "".join([
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
  box("Im Oneshot", "Nymeria, die Sturmhüterin. Kämpft in Kapitel 4 gegen die Höllenfeuer-Maschine, geführt von einem Spieler (siehe Spieler-Handout): pro Zug Sturzflug auf die Maschine oder Odem auf die Horde. Bei 0 TP zieht sie sich ins Sturmgebiet zurück, sie stirbt nicht. Nicht gegen den Feuerriesen, den Fäulnistroll oder den Gehörnten Teufel."),
 ]), hh="86mm", ch="150mm", pos="50% 30%", xp="50 000 EP<br>Hort 62 000")

# ---------------- Höllenfeuer-Maschine (bestehend, umbenannt) ----------------
maschine = a4("Höllenfeuer-Maschine", "Hellfire Engine · Riesiges Konstrukt, rechtschaffen böse · die Belagerungsmaschine der Horde", "16", "#7a2410", "#c9a27c", "maschine.png",
 "Werte: Monsters of the Multiverse, Hellfire Engine · Übungsbonus +5",
 [("Rüstungsklasse","18",""),("Trefferpunkte","216","(16W12+112)"),("Initiative","+3","(13)"),("Bewegung","12 m","40 Fuss")],
 [("STR","20","+5","+5"),("GES","16","+3","+8"),("KON","24","+7","+7"),("INT","2","−4","−4"),("WEI","10","+0","+5"),("CHA","1","−5","+0")],
 [("Resistenzen","Kälte, Psycho; Hieb, Stich, Wucht von nichtmagischen, nicht versilberten Angriffen"),("Immunitäten","Feuer, Gift"),("Zustandsimmunitäten","Bezaubert, Erschöpft, Gelähmt, Taub, Verängstigt, Vergiftet, Bewusstlos"),("Sinne","Dunkelsicht 36 m, passive Wahrnehmung 10"),("Sprachen","versteht Infernalisch, spricht nicht")],
 "".join([
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
  box("Hausregel Oneshot: Der Kessel", "<b>RK 12 · 60 TP</b> · Wucht und Donner doppelt · immun gegen Feuer, Gift, Psycho. "
  "Birst er: <span class=\"dice\">6W6 Feuer · 6 m · RW GES 14 halb</span>, Feuer am Boden 3 Runden (schwieriges Gelände, 2W6 Feuer beim Betreten), Maschine steht 2 Runden später still. "
  "Alle 4 Bombardiere (Goblin-Krieger, Karte K1) tot: Kessel läuft in 3 Runden leer. Jede Runde: eine Höllenwaffe ins Heer (−1 Schlachtenleiste) und Schritt geradeaus; schiesst auf Nymeria, solange sie über ihr ist. Das mittlere der drei Ziele in Kapitel 4."),
 ]), hh="114mm", ch="112mm")

# ---------------- Assassine (bestehend, umbenannt) ----------------
nadel = a4("Assassine", "Mittelgrosser Humanoide, neutral · im Buch: Nadel, Meuchlerin der Horde (Kapitel 1b)", "8", "#3d4a3a", "#a9b39c", "nadel.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Assassine · Übungsbonus +3",
 [("Rüstungsklasse","16",""),("Trefferpunkte","97","(15W8+30)"),("Initiative","+10","(20)"),("Bewegung","9 m","30 Fuss")],
 [("STR","11","+0","+0"),("GES","18","+4","+7"),("KON","14","+2","+2"),("INT","16","+3","+6"),("WEI","11","+0","+0"),("CHA","10","+0","+0")],
 [("Fertigkeiten","Akrobatik +7, Wahrnehmung +6, Heimlichkeit +10"),("Resistenzen","Gift"),("Sinne","passive Wahrnehmung 16"),("Sprachen","Gemeinsprache, Diebessprache"),("Ausrüstung","Leichte Armbrust, Kurzschwert, beschlagenes Leder")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Entrinnen", ("RW GES gelungen = 0",), "", "Bei einem Effekt mit GES-Rettungswurf für halben Schaden: Erfolg kein Schaden, Misserfolg nur halber Schaden. Nicht, solange sie kampfunfähig ist."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3 Angriffe",), "", "Drei Angriffe mit Kurzschwert oder Leichter Armbrust, beliebig gemischt."),
  feat("Kurzschwert", ("+7","1W6+4 Stich","+ 5W6 Gift","vergiftet"), "Nahkampf, Reichweite 1,5 m", "Ø 7 Stich + 17 Gift. Das Ziel ist vergiftet bis zum Beginn ihres nächsten Zuges."),
  feat("Leichte Armbrust", ("+7","1W8+4 Stich","+ 6W6 Gift"), "Fernkampf, 24/96 m", "Ø 8 Stich + 21 Gift."),
  "<h2>Bonusaktionen</h2>",
  feat("Raffinierte Aktion", ("Spurt · Rückzug · Verstecken",), "", "Sie spurtet, zieht sich zurück oder versteckt sich."),
  box('Im Oneshot: Hinterhalt im Fluchtgang <span class="nb">(Kapitel 1b)</span>', "Hängt in den Wurzeln über dem Eingang der Wurzelkammer. "
  '<span class="dice">Wahrnehmung SG 15</span> «Da hängt was in den Wurzeln»: wer besteht, ist nicht überrascht (überrascht = Nachteil auf Initiative). '
  "Erster Zug: drei Kurzschwert-Angriffe auf den ersten Helden in der Kammer, bis zu ~70 Schaden. Dann Armbrust aus dem Dunkeln. Dazu 2 Bugbear-Pirscher hinter den Felsbrocken und der Bugbear-Krieger (Pitt) am blinden Spalt. Fallen beide Pirscher, flieht sie mit Raffinierter Aktion."),
  box("Leichtere Variante: Bugbear-Pirscher (HG 3)", "<b>RK 15 · 65 TP (10W8+20) · 9 m</b> · Mehrfachangriff: 2× Wurfspeer oder Morgenstern.<br>"
  '<b>Wurfspeer</b> <span class="dice">+5 · 3W6+3 Stich</span> Reichweite 3 m oder 9/36 m. '
  '<b>Morgenstern</b> <span class="dice">+5 · 2W8+3 Stich</span> Reichweite 3 m, Vorteil gegen Gepackte. '
  '<b>Schneller Griff</b> (Bonusaktion) <span class="dice">RW GES 13 · gepackt</span> (Entkommen SG 13). Dazu nur ein Pirscher, Pitt kämpft nicht.'),
 ]), hh="118mm", ch="124mm", pos="50% 35%")

# ---------------- Bugbear-Krieger (bestehend, umbenannt) ----------------
bugbear = a4("Bugbear-Krieger", "Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · im Buch: Pitt, der Spion der Horde", "1", "#6b4a1f", "#c7ad83", "bugbear.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Bugbear-Krieger · Übungsbonus +2",
 [("Rüstungsklasse","14",""),("Trefferpunkte","33","(6W8+6)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(15,14,13,8,11,9),
 [("Fertigkeiten","Heimlichkeit +6, Überleben +2"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Fellrüstung, 3 leichte Hämmer")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Entführen", ("keine Extra-Bewegung",), "", "Braucht keine zusätzliche Bewegung, um eine Kreatur zu bewegen, die es gepackt hält."),
  "<h2>Aktionen <em>kein Mehrfachangriff, ein Angriff pro Zug</em></h2>",
  feat("Packen", ("+4","2W6+2 Wucht","gepackt"), "Nahkampf, Reichweite 3 m", "Ø 9 Wucht. Ein mittelgrosses oder kleineres Ziel ist gepackt (Entkommen SG 12)."),
  feat("Leichter Hammer", ("+4","3W4+2 Wucht"), "Nah- oder Fernkampf, 3 m oder 6/18 m", "Ø 9 Wucht. <b>Vorteil</b>, wenn es das Ziel selbst gepackt hält."),
  box('Im Oneshot: Pitt am blinden Spalt <span class="nb">(Kapitel 1b)</span>', "Pitt kommt nachts durch den alten Fluchtgang, den in der Burg niemand kannte, in den Keller zu Toms Labor und steht dort am Koffer. Entdeckt, flieht er durch die Luke. "
  "In der Wurzelkammer steht er mit Toms Tasche am blinden Spalt und kämpft halbherzig mit (Packen, Leichter Hammer). Kettennarbe am Handgelenk. "
  '<span class="dice">Fällt die Assassine oder unter 15 TP</span> lässt er den Hammer fallen und ergibt sich. Hat die Assassine die Tasche, flieht er in den Ausgangsgang. Leichtere Variante: Pitt kämpft nicht.'),
 ]), hh="136mm", ch="70mm", pos="50% 45%")

# ---------------- Bugbear-Pirscher (bestehend) ----------------
pirscher = a4("Bugbear-Pirscher", "Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · 2 im Fluchtgang; im Buch auch Geschützmeister Rotzahn (Turm 2)", "3", "#5a3b22", "#c2a27f", "pirscher.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Bugbear-Pirscher · Übungsbonus +2",
 [("Rüstungsklasse","15",""),("Trefferpunkte","65","(10W8+20)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(17,14,14,11,12,11,{"KON":"+4","WEI":"+3"}),
 [("Fertigkeiten","Heimlichkeit +6, Überleben +3"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 11"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Kettenhemd, 6 Wurfspeere, Morgenstern")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Entführen", ("keine Extra-Bewegung",), "", "Braucht keine zusätzliche Bewegung, um eine Kreatur zu bewegen, die es gepackt hält."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("2 Angriffe",), "", "Zwei Angriffe mit Wurfspeer oder Morgenstern."),
  feat("Wurfspeer", ("+5","3W6+3 Stich"), "Nah- oder Fernkampf, 3 m oder 9/36 m", "Ø 13 Stich."),
  feat("Morgenstern", ("+5","2W8+3 Stich"), "Nahkampf, Reichweite 3 m", "Ø 12 Stich. <b>Vorteil</b>, wenn es das Ziel selbst gepackt hält."),
  "<h2>Bonusaktionen</h2>",
  feat("Schneller Griff", ("RW GES 13","gepackt"), "eine Kreatur bis mittelgross in 3 m", "Misserfolg: gepackt (Entkommen SG 13)."),
  box('Im Oneshot: hinter den Felsbrocken <span class="nb">(Kapitel 1b)</span>', "Zwei Pirscher warten hinter zwei Felsbrocken (halbe Deckung, +2 RK) und greifen an, sobald die Assassine zugeschlagen hat. "
  "Taktik: Schneller Griff, mit Entführen hinter den Felsen zerren, dort zweimal Morgenstern mit Vorteil. Sie fliehen nicht. Leichtere Variante: nur einer."),
  box('Geschützmeister auf Turm 2 <span class="nb">(Kapitel 3)</span>', "Wartet versteckt hinter der Ballista (Heimlichkeit +6). Schneller Griff auf den Helden, der der Ballista am nächsten ist, dann zweimal Morgenstern mit Vorteil und wegschleifen. "
  "<b>Abketten</b> (Aktion): kettet die Spannvorrichtung einer Ballista ab; Reparatur mit Handwerkszeug SG 13 (eine Aktion), mit Orvins Geschützkunde automatisch. «MEINE Dinger. Finger weg.»"),
 ]), hh="118mm", ch="88mm", pos="50% 45%")

# ---------------- Feuerriese ----------------
feuerriese = a4("Feuerriese", "Riesiger Riese (5,5 m / 18 Fuss), rechtschaffen böse · das rechte Ziel auf der Ebene · die Horde nennt ihn Riesenork", "9", "#8a3a12", "#d1a57c", "feuerriese.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Feuerriese · Übungsbonus +4",
 [("Rüstungsklasse","18","Plattenrüstung"),("Trefferpunkte","162","(13W12+78)"),("Initiative","+3","(13)"),("Bewegung","9 m","30 Fuss")],
 ab(25,9,23,10,14,13,{"GES":"+3","KON":"+10","CHA":"+5"}),
 [("Fertigkeiten","Athletik +11, Wahrnehmung +6"),("Immunitäten","Feuer"),("Sinne","passive Wahrnehmung 16"),("Sprachen","Riesisch (hier: Orkisch und Gemeinsprache, laut)")],
 "".join([
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("2 Angriffe",), "", "Flammenschwert oder Hammerwurf, beliebig gemischt."),
  feat("Flammenschwert", ("+11","4W6+7 Hieb","+ 3W6 Feuer"), "Nahkampf, Reichweite 3 m · im Buch: der glühende Mühlstein", "Ø 21 Hieb + 10 Feuer. Der Mühlstein glüht vom Hordenfeuer."),
  feat("Hammerwurf", ("+11","3W10+7 Wucht","+ 1W8 Feuer","4,5 m Stoss"), "Fernkampf, 18/72 m · im Buch: der geschleuderte Mühlstein", "Ø 23 Wucht + 4 Feuer. Das Ziel wird bis zu 4,5 m / 15 Fuss gerade von ihm weggestossen und hat <b>Nachteil</b> auf seinen nächsten Angriffswurf vor dem Ende seines nächsten Zugs. Er zieht den Stein an der Kette zurück; die Kette reisst nie."),
  box('Bresche <span class="nb">(jede Runde ohne Gegner)</span>', "Solange kein Held ihn angreift oder beschäftigt, schlägt er in den Keil des Heeres: <b>−1 Schlachtenleiste pro Runde</b>. Greift ihn ein Held an, hört er sofort auf: «Endlich jemand.»"),
  box("Das Duell (Story-Regel)", "Fordert ein Held ihn zum Zweikampf (<b>Einschüchtern oder Überzeugen SG 13</b> oder gutes Rollenspiel), ruft er die Horde zurück. Nur der Held und der Riese kämpfen; Milo gibt dem Helden sofort einen Inspirationswürfel (W6). "
  "Greift ein anderer Held ein, ist das Duell gebrochen: die 4 Berserker (Karte K2) greifen an, der Riese brüllt «FEIGLINGE» und wirft den Mühlstein auf den Störenfried. Fällt er im Duell, jubelt die Horde kurz: die nächste Durchbruch-Runde ist frei. "
  "Wer am Boden liegt, bekommt «Steh auf» und eine Runde Zeit. Geht es nicht, bricht die Gruppe das Duell."),
  box("Für den Erzähler", "Zwei Schläge mit +11, im Schnitt 62 Schaden pro Runde, wenn beide treffen. Das ist gewollt. Was hilft: Glutschild (nimmt den Feuerteil), Toms Tränke, Milos Kräuter. "
  "Er ist <b>immun gegen Feuer</b>: der berstende Kessel der Maschine tut ihm nichts, er steht in den Flammen und lacht. Er wirft, was in Reichweite liegt, notfalls Milo (Hammerwurf ohne Feuer, Milo nimmt 3W6 Wucht beim Aufschlag)."),
 ]), hh="124mm", ch="108mm", pos="50% 35%")

# ---------------- Fäulnistroll ----------------
faeulnistroll = a4("Fäulnistroll", "Grosser Riese (3 m / 10 Fuss), chaotisch böse · der Bannerträger, das linke Ziel auf der Ebene", "9", "#4a5a2a", "#b5bd98", "faeulnistroll.png",
 "Werte: Monsters of the Multiverse, Rot Troll · Übungsbonus +4",
 [("Rüstungsklasse","16","natürliche Rüstung"),("Trefferpunkte","138","(12W10+72)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(18,13,22,5,8,4),
 [("Fertigkeiten","Wahrnehmung +3"),("Immunitäten","Nekrotisch"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 13"),("Sprachen","Riesisch"),("Keine Regeneration","anders als gewöhnliche Trolle")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Ranzige Zersetzung", ("2W10 nekrotisch","1,5 m"), "am Ende jedes seiner Züge", "Jede Kreatur in 1,5 m / 5 Fuss um ihn nimmt Ø 11 nekrotischen Schaden, ausser er hat seit dem Ende seines letzten Zugs <b>Säure- oder Feuerschaden</b> genommen. Der Priester im Korb ist ausgenommen (Regel, nicht Logik)."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("Biss + 2× Klaue",), "", ""),
  feat("Biss", ("+8","1W10+4 Stich","+ 3W10 nekrotisch"), "Nahkampf, 1,5 m", "Ø 9 Stich + 16 nekrotisch."),
  feat("Klaue", ("+8","2W6+4 Hieb","+ 2W6 nekrotisch"), "Nahkampf, 1,5 m", "Ø 11 Hieb + 7 nekrotisch."),
  box("Das Kettenbanner (Objekt auf seinem Rücken)", "Bannerstange <b>RK 15 · 30 TP</b>, immun gegen Gift und Psycho, Spitze in 4 m / 13 Fuss Höhe. Oder: auf den Troll klettern <span class=\"dice\">Athletik SG 15</span> (Aktion) und reissen <span class=\"dice\">Athletik SG 15</span> (Aktion). Fällt der Troll, fällt das Banner mit. "
  "<b>Solange es steht:</b> alle Horde-Kreaturen in 18 m / 60 Fuss kämpfen bis zum Tod und fliehen nicht, auch nicht, wenn die anderen Ziele fallen. "
  "<b>Fällt es:</b> die Horde in 18 m flieht nach Osten, der Priester kniet und kämpft nicht weiter, eines von drei Zielen ist gefallen. Der Priester allein reicht nicht."),
  box('Im Oneshot <span class="nb">(Kapitel 4, links)</span>', "Geht, wohin der Priester zeigt, sonst auf das Nächste, das blutet. Langsam und nicht klug. Im Eisenkorb zwischen seinen Schultern sitzt der <b>Kriegspriester</b> (eigener Bogen), der ihn heilt. "
  "Drumherum 4 Hobgoblin-Krieger in Schildformation (Halbdeckung, Rudeltaktik) und 2 Hobgoblin-Hauptmänner ausserhalb der Aura (Karten K1/K2). "
  "Feuer oder Säure schaltet die Aura bis zum Ende seines nächsten Zugs ab; Tom sagt es, falls die Spieler es nicht merken: «Fäulnis. Brennt sie weg.» Die Glutschilde halten Feuer fern, nicht die Fäulnis. Fällt er, stürzt der Priester aus dem Korb (1W6 Wucht, liegend)."),
 ]), hh="118mm", ch="114mm", pos="50% 35%")

# ---------------- Kriegspriester ----------------
kriegspriester = a4("Kriegspriester", "Mittelgrosser Humanoide (Hobgoblin, Kleriker) · im Buch: der Hochpriester, der den Gehörnten Teufel gerufen hat · im Korb auf dem Fäulnistroll", "9", "#8a6a1a", "#d6c08a", "kriegspriester.png",
 "Werte: Monsters of the Multiverse, War Priest · Übungsbonus +4",
 [("Rüstungsklasse","18","Platte · 20 im Korb"),("Trefferpunkte","117","(18W8+36)"),("Initiative","+0","(10)"),("Bewegung","9 m","im Korb: die des Trolls")],
 ab(16,10,14,11,17,13,{"KON":"+6","WEI":"+7"}),
 [("Fertigkeiten","Einschüchtern +5, Religion +4"),("Sinne","Dunkelsicht 18 m (Hobgoblin), passive Wahrnehmung 13"),("Sprachen","Goblinisch, Gemeinsprache")],
 "".join([
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("2× Streitkolben","+ Heiliges Feuer"), "", "Zwei Angriffe mit dem Streitkolben <b>und</b> Heiliges Feuer."),
  feat("Streitkolben", ("+7","2W6+3 Wucht","+ 3W6 gleissend"), "Nahkampf, 1,5 m · im Buch: der Kettenkolben", "Ø 10 Wucht + 10 gleissend."),
  feat("Heiliges Feuer", ("RW WEI 15","2W8+3 gleissend","blind"), "ein Ziel in 18 m, das er sieht", "Misserfolg: Ø 12 gleissend und blind bis zum Beginn seines nächsten Zugs. Erfolg: halber Schaden, nicht blind. Das Glühen der Ketten."),
  feat("Zauberwirken", ("SG 15",), "Weisheit · jeder Zauber nur einmal", "<b>Beliebig oft:</b> Licht, Die Sterbenden verschonen, Thaumaturgie.<br><b>Je 1/Tag:</b> Verbannung, Befehl, Magie bannen, Flammenschlag, Hüter des Glaubens, Person festhalten, Geringere Wiederherstellung, Wiederbeleben."),
  feat("Flammenschlag", ("RW GES 15","4W6 Feuer","+ 4W6 gleissend"), "1/Tag · Zylinder Radius 3 m, 12 m hoch · 18 m", "Erfolg: halber Schaden. Steht der Troll mit drin, schaltet das seine Aura eine Runde ab; der Priester zielt lieber daneben."),
  feat("Hüter des Glaubens", ("20 gleissend","RW GES 15 halb"), "1/Tag · 3 m · 8 Stunden", "Ein glühendes Kettengebilde neben dem Troll. Wer sich ihm auf 3 m nähert, nimmt 20 gleissend (Erfolg: 10). Verschwindet nach 60 Schaden insgesamt."),
  feat("Person festhalten", ("RW WEI 15","gelähmt"), "1/Tag · 18 m · Konzentration, 1 Minute", "Gegen den gefährlichsten Nahkämpfer. Neuer Wurf am Ende jedes eigenen Zugs."),
  feat("Verbannung", ("RW CHA 15",), "1/Tag · 18 m · Konzentration", "Gegen Nymeria, falls sie über ihm ist. Sie schafft den Wurf fast immer, aber die Spieler sollen es sehen."),
  "<h2>Bonusaktionen</h2>",
  feat("Heilendes Licht", ("2/Tag","2W8+3 TP"), "er selbst oder eine Kreatur in 18 m", "Immer auf den Troll, nie auf sich."),
  box("Der Korb", "Sitzt im Eisenkorb zwischen den Schultern des Trolls, neben der Bannerstange: <b>Halbdeckung (+2 RK = 20)</b>, freie Sicht über die Horde, und er steht <b>nicht</b> in der Aura des Trolls. Wer auf den Troll klettert, steht neben dem Korb und kann ihn im Nahkampf angreifen. Fällt der Troll, stürzt er aus dem Korb (1W6 Wucht, liegend) und kämpft zu Fuss weiter."),
  box("Reihenfolge und Ende", "1. Runde 1: Hüter des Glaubens neben den Troll. 2. Sobald ein Held an den Troll will: Flammenschlag. 3. Person festhalten auf den gefährlichsten Nahkämpfer. 4. Verbannung gegen Nymeria. 5. Heilendes Licht immer auf den Troll. "
  "Er predigt aus dem Korb, nennt die Helden beim Namen und fragt, wofür sie kämpfen; Milo antwortet immer («Für Grossmutter. Und weil euch sonst keiner kocht.»). <b>Fällt das Banner:</b> er kniet und betet, kämpft nicht weiter, flieht nicht."),
 ]), hh="96mm", ch="140mm", pos="50% 30%")

# ---------------- Gehörnter Teufel ----------------
teufel = a4("Gehörnter Teufel", "Grosser Unhold (Teufel), rechtschaffen böse · im Buch: Kazzamir, der Gehörnte · Anführer der Horde, Finale in Veldgard", "11", "#6b1a1a", "#c99a8a", "teufel.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Gehörnter Teufel · Übungsbonus +4 · TP für die Gruppe verschärft",
 [("Rüstungsklasse","18",""),("Trefferpunkte","250","(Standard 199)"),("Initiative","+7","(17)"),("Bewegung","9 m","Fliegen 18 m")],
 ab(22,17,21,12,16,18,{"STR":"+10","GES":"+7","WEI":"+7","CHA":"+8"}),
 [("Resistenzen","Kälte"),("Immunitäten","Feuer, Gift; Zustand Vergiftet"),("Sinne","Dunkelsicht 45 m (auch durch magische Dunkelheit), passive Wahrnehmung 13"),("Sprachen","Infernalisch, Telepathie 36 m (er spricht in den Köpfen, nicht mit dem Mund)")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Teuflische Wiederkehr", (), "", "Stirbt er ausserhalb der Neun Höllen, verschwindet sein Körper in Schwefelrauch, und er erhält sofort einen neuen mit allen TP, irgendwo in den Neun Höllen. Für den Oneshot: besiegt und fort."),
  feat("Magieresistenz", ("Vorteil",), "", "Vorteil auf Rettungswürfe gegen Zauber und andere magische Effekte."),
  "<h2>Aktionen <em>keine Bonusaktionen, Reaktionen oder legendären Aktionen</em></h2>",
  feat("Mehrfachangriff", ("3 Angriffe",), "", "Glühende Gabel oder Flammenwurf, beliebig gemischt. Einen der drei Angriffe kann er durch den Höllenschweif ersetzen."),
  feat("Glühende Gabel", ("+10","2W8+6 Stich","+ 2W8 Feuer"), "Nahkampf, Reichweite 3 m", "Ø 15 Stich + 9 Feuer."),
  feat("Flammenwurf", ("+8","5W8+4 Feuer"), "Fernkampf, 45 m", "Ø 26 Feuer. Ein brennbarer Gegenstand, der nicht getragen wird, fängt Feuer (die Hordenbanner in der Halle!)."),
  feat("Höllenschweif", ("RW GES 17","1W8+6 nekrotisch","Höllenwunde"), "eine Kreatur in 3 m, die er sieht", "Misserfolg: Ø 10 nekrotisch und eine <b>Höllenwunde</b>, falls das Ziel noch keine hat. Solange die Wunde offen ist, verliert das Ziel zu Beginn <b>jedes seiner Züge</b> <span class=\"dice\">3W6 TP</span>. Sie schliesst sich nach 1 Minute, sobald ein Zauber dem Ziel TP zurückgibt, oder wenn das Ziel oder jemand in 1,5 m eine Aktion nutzt und <span class=\"dice\">Weisheit (Heilkunde) SG 17</span> schafft."),
  box('Im Oneshot: Kazzamirs Halle <span class="nb">(Kapitel 6)</span>', "Nur die Helden und Milo gegen ihn und seine 2 <b>Höllenhunde</b> (Karte K5), die zu Füssen des Throns liegen und die Helden auseinanderhalten. 7 200 EP, mit den Hunden rund 8 600: deutlich über «hoch» für drei Helden der Stufe 8 plus Milo. Im Schnitt 45 bis 50 Schaden pro Runde; er kann einen Helden in zwei Runden umwerfen. "
  "<b>Was die Gruppe braucht:</b> Feuer meiden (immun), Waffen und Zauber mit Angriffswurf; wissen, dass der <b>Glutschild erloschen</b> ist; die Höllenwunde <b>sofort</b> schliessen (beim ersten Schweif-Treffer einmal klar sagen, dass sie weiterblutet und wie man sie stillt); Milos Hinweis und die drei Netze aus Szenario E."),
  box("Leichter, wenn nötig (Erzählerentscheidung)", "Er beginnt mit <b>199 TP</b> statt 250 («das dritte Banner hat ihn getroffen»), oder die Hunde bleiben liegen. In Runde 1 macht er nur <b>zwei</b> Angriffe, er testet die Helden. Härter braucht es nicht."),
 ]), hh="104mm", ch="132mm", pos="50% 30%")

# ---------------- Schreckenstroll ----------------
schreckenstroll = a4("Schreckenstroll", "Riesiger Riese, chaotisch böse · Endboss der Echohallen, Bossraum (Spiegelkammer)", "13", "#2f4a3a", "#9fb5a5", "schreckenstroll.png",
 "Werte: Monsters of the Multiverse, Dire Troll · Übungsbonus +5",
 [("Rüstungsklasse","15","natürliche Rüstung"),("Trefferpunkte","172","(15W12+75)"),("Initiative","+2","(12)"),("Bewegung","12 m","40 Fuss")],
 ab(22,15,21,9,11,5,{"WEI":"+5","CHA":"+2"}),
 [("Fertigkeiten","Wahrnehmung +10"),("Resistenzen","Hieb, Stich, Wucht aus nichtmagischen Angriffen"),("Zustandsimmunitäten","Verängstigt, Vergiftet"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 20"),("Sprachen","Riesisch")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Regeneration", ("10 TP","nach Säure/Feuer: 5 TP"), "zu Beginn seines Zugs", "Hat er Säure- oder Feuerschaden genommen, erhält er zu Beginn seines nächsten Zugs nur 5 TP. Er <b>stirbt nur</b>, wenn er bei 0 TP von einem Angriff getroffen wird, der 10 oder mehr Säure- oder Feuerschaden macht."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("Biss + 4× Klaue",), "", "Treffen Biss und alle vier Klauen ein Ziel, sind das rund 80 Schaden in einer Runde."),
  feat("Biss", ("+11","1W8+6 Stich","+ 1W10 Gift"), "Nahkampf, Reichweite 3 m", "Ø 10 Stich + 5 Gift."),
  feat("Klaue", ("+11","3W6+6 Hieb"), "Nahkampf, Reichweite 3 m", "Ø 16 Hieb pro Treffer."),
  feat("Klauenwirbel", ("RW GES 19","8W10 Hieb"), "Aufladung 5–6 · jede Kreatur in 3 m um ihn", "Ø 44 Hieb. Erfolg: halber Schaden."),
  box('Im Oneshot: der Bossraum <span class="nb">(Kapitel 1c)</span>', "10 000 EP: für vier Kämpfer der Stufe 8 deutlich über «hoch» (8 400). Mit Absicht, die Liga der grossen Ziele aus Kapitel 4. <b>Nicht abschwächen</b>, dafür die Rast im Sturmschacht grosszügig geben. "
  "Die Resistenz gegen nichtmagische Waffen spielt bei der Gruppe keine Rolle (Orvins Schliffe +1, Silberzahn). Was zählt: <b>Feuer oder Säure</b> am Ende, sonst steht er wieder auf. Die zwei Ölfässer der Horde aus dem Sturmschacht sind der Notnagel. Der Klauenwirbel trifft alle, die in 3 m stehen: nicht alle auf einmal ran."),
 ]), hh="136mm", ch="92mm", pos="50% 35%")

# ---------------- Champion ----------------
champion = a4("Champion", "Mittelgrosser Humanoide (Hobgoblin), rechtschaffen böse · im Buch: Kettenhauptmann Bruchhand · oben an der Treppe von Turm 2", "9", "#4a2a2a", "#c0a0a0", "champion.png",
 "Werte: Monsters of the Multiverse, Champion · Übungsbonus +4",
 [("Rüstungsklasse","18","Plattenrüstung"),("Trefferpunkte","143","(22W8+44)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(20,15,14,10,14,12,{"STR":"+9","KON":"+6"}),
 [("Fertigkeiten","Athletik +9, Einschüchtern +5, Wahrnehmung +6"),("Sinne","passive Wahrnehmung 16"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Platte, Grossschwert, Kurzbogen; Kazzamirs Kette als Wappen auf rotem Grund")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Unbeugsam", ("2/Tag",), "", "Wiederholt einen misslungenen Rettungswurf. Festhalten, Betäuben und Furcht prallen meist ab; darauf sollen die Spieler nicht bauen."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3 Angriffe",), "", "Grossschwert oder Kurzbogen."),
  feat("Grossschwert", ("+9","2W6+5 Hieb","+ 2W6 Hieb mit 72+ TP"), "Nahkampf, 1,5 m", "Ø 12 Hieb, solange er mehr als die Hälfte seiner TP hat (72 oder mehr) zusätzlich Ø 7: bis zu ~57 Schaden auf ein Ziel pro Runde. Sag nach dem ersten Treffer ruhig, dass er «noch frisch» schlägt."),
  feat("Kurzbogen", ("+6","1W6+2 Stich","+ 2W6 Stich mit 72+ TP"), "Fernkampf, 24/96 m", "Nutzt ihn nur, wenn niemand die Treppe hochkommt."),
  "<h2>Bonusaktionen</h2>",
  feat("Zweite Luft", ("20 TP",), "1× pro kurzer oder langer Rast", "Nutzt sie, sobald er unter 72 TP ist, um wieder über die Schwelle zu kommen."),
  box('Im Oneshot: die Treppe <span class="nb">(Kapitel 3, Turm 2)</span>', "Steht oben an der Plattformtreppe hinter dem Pechtopf (GES SG 13, 3W6 Feuer an der Treppe) und rührt sich nicht von dort. Mit dem Hobgoblin-Hauptmann in 3 m bekommt er dessen <b>Aura der Autorität</b> (Vorteil auf Angriffe und Rettungswürfe). "
  "Er flieht nie. Fällt er, brechen die restlichen Hobgoblins auf Turm 2 sofort, und der Kriegsmagier hebt ab. Ein Hobgoblin in schwarzer Platte mit der Kette als Wappen, das Grossschwert über der Schulter. Christophs Wunsch wegen der starken Charaktere."),
 ]), hh="126mm", ch="102mm", pos="50% 30%")

# ---------------- Gifttroll ----------------
gifttroll = a4("Gifttroll", "Grosser Riese, chaotisch böse · Ebene 2 der Echohallen, die Tiefhalle, mit 2 Trollen", "7", "#3d5a3a", "#a9b39c", "gifttroll.png",
 "Werte: Monsters of the Multiverse, Venom Troll · Übungsbonus +3",
 [("Rüstungsklasse","15","natürliche Rüstung"),("Trefferpunkte","94","(9W10+45)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(18,13,20,7,9,7),
 [("Fertigkeiten","Wahrnehmung +5"),("Immunitäten","Gift; Zustand Vergiftet"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 15"),("Sprachen","Riesisch")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Giftspritzer", ("2W8 Gift","1,5 m"), "wenn er Schaden nimmt (ausser Psycho)", "Jede Kreatur in 1,5 m um ihn nimmt Ø 9 Gift. Jeder Nahkampftreffer kostet den Angreifer also Gift."),
  feat("Regeneration", ("10 TP",), "zu Beginn seines Zugs", "Hat er Säure- oder Feuerschaden genommen, setzt sie zu Beginn seines nächsten Zugs aus. Er stirbt nur, wenn er seinen Zug mit 0 TP beginnt und nicht regeneriert."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("Biss + 2× Klaue",), "", ""),
  feat("Biss", ("+7","1W6+4 Stich","+ 1W8 Gift","vergiftet"), "Nahkampf, 1,5 m", "Ø 7 Stich + 4 Gift; das Ziel ist vergiftet bis zum Beginn seines nächsten Zugs."),
  feat("Klaue", ("+7","2W6+4 Hieb","+ 1W8 Gift"), "Nahkampf, 1,5 m", "Ø 11 Hieb + 4 Gift."),
  feat("Giftsprühen", ("RW KON 16","4W8 Gift","vergiftet 1 Min"), "Aufladung 6 · Würfel 4,5 m", "Er schlitzt sich selbst auf (7 Hieb, nicht verringerbar) und sprüht Gift. Misserfolg: Ø 18 Gift und eine Minute vergiftet (neuer Wurf am Ende jedes eigenen Zugs). Erfolg: halber Schaden, nicht vergiftet."),
  box('Im Oneshot: die Tiefhalle <span class="nb">(Kapitel 1c, Ebene 2)</span>', "Gifttroll und 2 Trolle (Karte K4): 6 500 EP, für vier Kämpfer der Stufe 8 «hoch». Leichter: Gifttroll und ein Troll (4 700 EP, «mittel»). "
  "Alle drei regenerieren; die zwei Ölfässer der Horde aus dem Sturmschacht sind das Feuer, falls die Gruppe keins hat. Wer den Gifttroll im Nahkampf angeht, nimmt pro Treffer Giftspritzer: Fernkampf und Zauber lohnen sich hier."),
 ]), hh="126mm", ch="104mm", pos="50% 35%")

# ---------------- Chimäre ----------------
chimaere = a4("Chimäre", "Grosse Monstrosität, chaotisch böse · Ebene 1 der Echohallen, die Brutkammer: ein Paar mit Gelege", "6", "#7a3a10", "#d0a888", "chimaere.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Chimäre · Übungsbonus +3",
 [("Rüstungsklasse","14",""),("Trefferpunkte","114","(12W10+48)"),("Initiative","+0","(10)"),("Bewegung","9 m","Fliegen 18 m")],
 ab(19,11,19,3,14,10),
 [("Fertigkeiten","Wahrnehmung +8"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 18"),("Sprachen","versteht Drakonisch, spricht nicht")],
 "".join([
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("Rammen + Biss + Klaue",), "", "Den Klauenangriff kann sie durch den Feueratem ersetzen, wenn er geladen ist."),
  feat("Biss", ("+7","2W6+4 Stich","4W6+4 bei Vorteil"), "Nahkampf, 1,5 m", "Ø 11 Stich, oder Ø 18, wenn sie Vorteil auf den Angriff hatte."),
  feat("Klaue", ("+7","1W6+4 Hieb"), "Nahkampf, 1,5 m", "Ø 7 Hieb."),
  feat("Rammen", ("+7","1W12+4 Wucht","liegend"), "Nahkampf, 1,5 m", "Ø 10 Wucht. Ein mittelgrosses oder kleineres Ziel liegt danach am Boden."),
  feat("Feueratem", ("RW GES 15","7W8 Feuer"), "Aufladung 5–6 · Kegel 4,5 m", "Ø 31 Feuer. Erfolg: halber Schaden."),
  box('Im Oneshot: die Brutkammer <span class="nb">(Kapitel 1c, Ebene 1)</span>', "Zwei Chimären bewachen ihr Gelege: 4 600 EP, für vier Kämpfer der Stufe 8 «mittel». Leichter: eine (2 300 EP, «niedrig»). "
  "Rammen wirft um, dann Biss mit Vorteil gegen den Liegenden (4W6+4). Beide Feueratems auf einen Haufen Helden sind das Risiko: bis zu 62 Feuer. Sie fliegen, verlassen die Kammer aber nicht, solange das Gelege steht."),
 ]), hh="140mm", ch="88mm", pos="50% 40%")

# ---------------- Wyvern ----------------
wyvern = a4("Wyvern", "Grosser Drache, gesinnungslos · im Buch: die Felsdrachen der Horde, 3 Stück, angekettet im Hordenlager", "6", "#4a5560", "#aab4bc", "wyvern.png",
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Wyvern · Übungsbonus +3",
 [("Rüstungsklasse","14",""),("Trefferpunkte","127","(15W10+45)"),("Initiative","+0","(10)"),("Bewegung","9 m","Fliegen 24 m")],
 ab(19,10,16,5,12,6),
 [("Fertigkeiten","Wahrnehmung +4"),("Sinne","Dunkelsicht 36 m, passive Wahrnehmung 14"),("Sprachen","keine")],
 "".join([
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("Biss + Stachel",), "", ""),
  feat("Biss", ("+7","2W8+4 Stich"), "Nahkampf, 1,5 m", "Ø 13 Stich."),
  feat("Stachel", ("+7","2W6+4 Stich","+ 7W6 Gift","vergiftet"), "Nahkampf, Reichweite 3 m", "Ø 11 Stich + 24 Gift; das Ziel ist vergiftet bis zum Beginn seines nächsten Zugs. Im Nahkampf ist ein Wyvern für die Gruppe ein harter Gegner, drei sind tödlich. Deshalb die Ballisten."),
  box('Im Oneshot: die Drachenjagd <span class="nb">(Kapitel 3, Szene 4, Minigame)</span>', "Die Wyvern sind im Hordenlager angekettet und steigen erst auf, wenn Turm 2 gefallen ist. Dann von der Ballista aus: <span class=\"dice\">1W20+6 gegen RK 13 · 3W10</span>, drei Treffer pro Wyvern; die Feuerschilde halten drei Runden. "
  "Ein Wyvern, der Turm 2 angreift, bleibt eine Runde in Reichweite und wird mit <b>Vorteil</b> beschossen, wenn ein zweiter Held ihn ablenkt (Angriff, Zauber, Lärm). Keine Sturztode."),
  box("Lärmscheu und Abschuss", "<b>Lärmscheu:</b> Donnerschaden, ein Horn, ein Donnerzauber oder etwas vergleichbar Lautes in 18 m: der Wyvern weicht eine Runde lang irritiert aus. "
  "<b>Sturzflug aufs Heer:</b> solange einer unbeschossen über der Ebene fliegt, reisst er pro Runde ein Loch in die Reihen (Schlachtenleiste). "
  "<b>Abschuss:</b> fällt ein Wyvern in der Luft auf 0 TP, stürzt er in die Horde: <span class=\"dice\">3W10 Wucht</span> auf alles in 3 m und <b>+1 Schlachtenleiste</b>."),
 ]), hh="136mm", ch="92mm", pos="50% 40%")

# ---------------- Hobgoblin-Verwüster ----------------
verwuester = a4("Hobgoblin-Verwüster", "Mittelgrosses Feenwesen (Goblinoide), rechtschaffen neutral · im Buch: Kriegsmagier Vask, Beobachtungsstand von Turm 2", "4", "#7a2a1a", "#cfa08c", "verwuester.png",
 "Werte: Monsters of the Multiverse, Hobgoblin Devastator · Übungsbonus +2 · Hausregel: volle TP (7W8+14 = 70 statt 45)",
 [("Rüstungsklasse","13","besch. Leder"),("Trefferpunkte","70","(Standard 45)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(13,12,14,16,13,11),
 [("Fertigkeiten","Arkane Kunde +5"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 11"),("Sprachen","Gemeinsprache, Goblinisch"),("Kettennarbe","am Unterarm")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Heeresmagie", (), "", "Wirkt er einen Zauber, der Schaden macht oder einen Rettungswurf verlangt, nimmt er sich und beliebig viele Verbündete davon aus: Er feuert bedenkenlos in den Nahkampf."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("2 Angriffe",), "", "Kampfstab oder Verheerender Blitz."),
  feat("Verheerender Blitz", ("Zauberangriff +5","4W8+3 Energie","liegend"), "Fernkampf, 18 m", "Ø 21 Energie, und das Ziel liegt am Boden. Zwei davon pro Runde sind sein gefährlichster Angriff, nicht die Zauber."),
  feat("Kampfstab", ("+3","1W6+1 Wucht","+ 3W8 Energie"), "Nahkampf, 1,5 m · beidhändig 1W8+1", "Ø 4 Wucht + 13 Energie."),
  feat("Zauberwirken", ("SG 13",), "Intelligenz", "<b>Beliebig oft:</b> Magierhand, Taschenspielerei.<br><b>Je 2/Tag:</b> Feuerball, Fliegen, Nebelwolke, Windstoss, Blitzstrahl."),
  feat("Feuerball", ("RW GES 13","8W6 Feuer"), "Radius 6 m · 45 m", "Ø 28 Feuer, Erfolg halb. Sobald zwei Helden beieinander stehen."),
  feat("Blitzstrahl", ("RW GES 13","8W6 Blitz"), "Linie 30 m × 1,5 m", "Ø 28 Blitz, Erfolg halb."),
  feat("Nebelwolke", ("Radius 6 m",), "Konzentration · bis 1 Stunde", "Stark verschleiert. Windstoss oder starker Wind vertreibt sie."),
  feat("Fliegen", ("18 m Fluggeschwindigkeit",), "Konzentration · 10 Minuten", "Hebt ab, wenn ihn jemand erreicht; dann verzieht sich der Nebel (nur eine Konzentration)."),
  feat("Windstoss", ("RW STR 13","4,5 m Stoss"), "Linie 18 m × 3 m · Konzentration", "Vertreibt Nebel und Rauch."),
  box('Im Oneshot: Nebel, Feuer, Blitz <span class="nb">(Kapitel 3, Turm 2)</span>', "Steht auf dem Beobachtungsstand (Leiter, 3 m), Sichtlinie auf beide Ballisten und den Zwischenraum. "
  "<b>1.</b> Nebelwolke auf den Fuss seiner Plattform (Runde 1, oder schon vorher, wenn das Horn geblasen wurde): die Eisenschatten schlagen aus dem Nebel, Bogenschützen und Bolzenschleudern schiessen auf alles, was herauskommt, und wer die Treppe sucht, findet den Pechtopf blind. "
  "<b>2.</b> Feuerball oder Blitzstrahl, sobald zwei Helden beieinander stehen. <b>3.</b> Sonst jede Runde zwei Verheerende Blitze. Erreicht ihn jemand: Fliegen und weiter vom Fels aus. "
  "<b>4.</b> Bei einem Drittel seiner TP flieht er fliegend Richtung Kessel; lass ihn, oder lass die Ballista entscheiden (ein Treffer, und er stürzt). Fällt der Champion, hebt er sofort ab."),
 ]), hh="100mm", ch="134mm", pos="50% 35%")

A4 = [
 ("01-Uralter-Silberdrache-Nymeria", drache),
 ("02-Hoellenfeuer-Maschine", maschine),
 ("03-Assassine", nadel),
 ("04-Bugbear-Krieger", bugbear),
 ("05-Bugbear-Pirscher", pirscher),
 ("06-Feuerriese", feuerriese),
 ("07-Faeulnistroll", faeulnistroll),
 ("08-Kriegspriester", kriegspriester),
 ("09-Gehoernter-Teufel", teufel),
 ("10-Schreckenstroll", schreckenstroll),
 ("11-Champion", champion),
 ("12-Gifttroll", gifttroll),
 ("13-Chimaere", chimaere),
 ("14-Wyvern", wyvern),
 ("15-Hobgoblin-Verwuester", verwuester),
]

# ---------------- Silberdrachen als spontane Optionen (1.11.2026, ohne Bild, ohne Infokästen) ----------------
adult_silber = a4("Ausgewachsener Silberdrache", "Riesiger Drache (metallisch), rechtschaffen gut", "16", "#2f4f6b", "#9fb2c2", None,
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Ausgewachsener Silberdrache · Übungsbonus +5",
 [("Rüstungsklasse","19",""),("Trefferpunkte","216","(16W12+112)"),("Initiative","+10","(20)"),("Bewegung","12 m","Fliegen 24 m")],
 [("STR","27","+8","+8"),("GES","10","+0","+5"),("KON","25","+7","+7"),("INT","16","+3","+3"),("WEI","13","+1","+6"),("CHA","22","+6","+6")],
 [("Fertigkeiten","Geschichte +8, Wahrnehmung +11, Heimlichkeit +5"),("Immunitäten","Kälte"),("Sinne","Blindsicht 18 m, Dunkelsicht 36 m, passive Wahrnehmung 21"),("Sprachen","Gemeinsprache, Drakonisch")],
 "".join([
  "<h2>Merkmale</h2>",
  feat("Legendäre Resistenz", ("3/Tag",), "im Hort 4/Tag", "Misslingt ihm ein Rettungswurf, kann er stattdessen entscheiden, dass er gelingt."),
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3× Zerfetzen",), "", "Einen Angriff darf er ersetzen durch <b>Lähmungsodem</b> oder durch <b>Eismesser</b> (Zauberwirken)."),
  feat("Zerfetzen", ("+13","2W8+8 Hieb","+ 1W8 Kälte"), "Nahkampf, Reichweite 3 m", "Ø 17 Hieb + 4 Kälte pro Treffer."),
  feat("Kälteodem", ("RW KON 20","12W8 Kälte"), "Aufladung 5–6 · Kegel 18 m", "Ø 54 Kälte. Erfolg: halber Schaden."),
  feat("Lähmungsodem", ("RW KON 20","kampfunfähig → gelähmt"), "Kegel 18 m", "1. Misserfolg: kampfunfähig bis zum Ende seines nächsten Zuges, dann neuer Rettungswurf. 2. Misserfolg: gelähmt; neuer Rettungswurf am Ende jedes eigenen Zuges, nach 1 Minute automatisch Erfolg."),
  feat("Zauberwirken", ("SG 19","Zauberangriff +11"), "Charisma, keine Materialkomponenten", "<b>Beliebig oft:</b> Magie entdecken, Monster festhalten, Eismesser (Grad 2), Gestaltwandel (nur Tier oder Humanoide, ohne temporäre TP, ohne Konzentration).<br><b>Je 1/Tag:</b> Eissturm, Zone der Wahrheit."),
  feat("Eismesser", ("+11","1W10 Stich","RW GES 19","3W6 Kälte"), "Zauber Grad 2 · 18 m", "Splitter trifft ein Ziel, dann Explosion: das Ziel und alle in 1,5 m um es, Rettungswurf sonst 3W6 Kälte (auch bei Fehlschlag des Angriffs)."),
  feat("Monster festhalten", ("RW WEI 19","gelähmt"), "Zauber · 27 m · Konzentration", "Gelähmt bis 1 Minute; neuer Rettungswurf am Ende jedes eigenen Zuges."),
  feat("Eissturm", ("RW GES 19","2W8 Wucht","+ 4W6 Kälte"), "1/Tag · Grad 4 · Zylinder Radius 6 m", "Reichweite 90 m. Erfolg: halber Schaden. Der Boden ist bis zum Ende seines nächsten Zuges schwieriges Gelände."),
  "<h2>Legendäre Aktionen <em>3 pro Runde (im Hort 4), direkt nach dem Zug einer anderen Kreatur</em></h2>",
  feat("Frosthauch", ("RW WEI 19","gelähmt"), "", "Wirkt <b>Monster festhalten</b>. Erst wieder ab Beginn seines nächsten Zuges."),
  feat("Kältesturm", ("RW GES 19","4W6 Kälte","9 m weg"), "Linie 18 m × 3 m", "Misserfolg: Schaden und 9 m von ihm weggestossen. Erfolg: halber Schaden, kein Stoss. Erst wieder ab Beginn seines nächsten Zuges."),
  feat("Ansprung", ("½ Bewegung","Zerfetzen +13"), "", "Bewegt sich bis zur halben Geschwindigkeit und macht einen Zerfetzen-Angriff (2W8+8 Hieb + 1W8 Kälte)."),
 ]), hh="34mm", ch="196mm", xp="15 000 EP<br>Hort 18 000")

jung_silber = a4("Junger Silberdrache", "Grosser Drache (metallisch), rechtschaffen gut", "9", "#2f4f6b", "#9fb2c2", None,
 "Werte: Monsterhandbuch 2024 (SRD 5.2), Junger Silberdrache · Übungsbonus +4",
 [("Rüstungsklasse","18",""),("Trefferpunkte","168","(16W10+80)"),("Initiative","+4","(14)"),("Bewegung","12 m","Fliegen 24 m")],
 [("STR","23","+6","+6"),("GES","10","+0","+4"),("KON","21","+5","+5"),("INT","14","+2","+2"),("WEI","11","+0","+4"),("CHA","19","+4","+4")],
 [("Fertigkeiten","Geschichte +6, Wahrnehmung +8, Heimlichkeit +4"),("Immunitäten","Kälte"),("Sinne","Blindsicht 9 m, Dunkelsicht 36 m, passive Wahrnehmung 18"),("Sprachen","Gemeinsprache, Drakonisch")],
 "".join([
  "<h2>Aktionen</h2>",
  feat("Mehrfachangriff", ("3× Zerfetzen",), "", "Einen Angriff darf er ersetzen durch <b>Lähmungsodem</b>."),
  feat("Zerfetzen", ("+10","2W8+6 Hieb"), "Nahkampf, Reichweite 3 m", "Ø 15 Hieb pro Treffer."),
  feat("Kälteodem", ("RW KON 17","11W8 Kälte"), "Aufladung 5–6 · Kegel 9 m", "Ø 49 Kälte. Erfolg: halber Schaden."),
  feat("Lähmungsodem", ("RW KON 17","kampfunfähig → gelähmt"), "Kegel 9 m", "1. Misserfolg: kampfunfähig bis zum Ende seines nächsten Zuges, dann neuer Rettungswurf. 2. Misserfolg: gelähmt; neuer Rettungswurf am Ende jedes eigenen Zuges, nach 1 Minute automatisch Erfolg."),
 ]), hh="34mm", ch="196mm")

A4 += [
 ("16-Ausgewachsener-Silberdrache", adult_silber),
 ("17-Junger-Silberdrache", jung_silber),
]
