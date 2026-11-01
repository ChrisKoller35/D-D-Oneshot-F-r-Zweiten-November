# Viertel-A4-Karten: vier pro Blatt. Werte 2024 (Monsterhandbuch / SRD 5.2) bzw. Monsters of the Multiverse.
GOB = "#6b4a1f"; GOBL = "#c7ad83"
HOB = "#7a2a1a"; HOBL = "#cfa08c"
WOLF = "#3f4a52"; WOLFL = "#aab4bc"
OGR = "#5a3b22"; OGRL = "#c2a27f"
TRL = "#3d5a3a"; TRLL = "#a9b39c"
FND = "#7a2410"; FNDL = "#c9a27c"
GRF = "#2f4f6b"; GRFL = "#9fb2c2"
ORK = "#4a3a2a"; ORKL = "#b8a890"

def klein(name, sub, hg, acc, line, img, quelle, core, abil, props, cols, pos="50% 40%"):
    return dict(name=name, sub=sub, hg=hg, acc=acc, line=line, img=img, quelle=quelle, core=core, ab=abil, props=props, cols=cols, pos=pos)

flinke = feat("Flinke Flucht", ("Rückzug · Verstecken",), "Bonusaktion", "Der Goblin zieht sich zurück oder versteckt sich.")
rudel = lambda wer: feat("Rudeltaktik", ("Vorteil",), "", f"Vorteil auf den Angriff, wenn ein Verbündeter {wer} in 1,5 m des Ziels steht und nicht kampfunfähig ist.")

goblin_minion = klein("Goblin-Minion", "Kleines Feenwesen (Goblinoide), chaotisch neutral", "1/8", GOB, GOBL, "goblin-minion.png", MH,
 [("Rüstungsklasse","12",""),("Trefferpunkte","7","(2W6)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(8,15,10,10,8,8),
 [("Fertigkeiten","Heimlichkeit +6"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 9"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","3 Dolche")],
 "<h2>Aktionen</h2>"+feat("Dolch", ("+4","1W4+2 Stich"), "Nah- oder Fernkampf, 1,5 m oder 6/18 m", "Ø 4 Stich.")
 +"<h2>Bonusaktionen</h2>"+flinke
 +box("Im Oneshot (Kapitel 4)", "Die Masse der Horde auf der Ebene. Meist über die Hordenregel (Durchbruch: ein Angriff gegen RK 13), einzeln nur, wenn du es willst."))

goblin_krieger = klein("Goblin-Krieger", "Kleines Feenwesen (Goblinoide), chaotisch neutral", "1/4", GOB, GOBL, "goblin-krieger.png", MH,
 [("Rüstungsklasse","15",""),("Trefferpunkte","10","(3W6)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(8,15,10,10,8,8),
 [("Fertigkeiten","Heimlichkeit +6"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 9"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Leder, Schild, Krummsäbel, Kurzbogen")],
 "<h2>Aktionen</h2>"+feat("Krummsäbel", ("+4","1W6+2 Hieb","+1W4 bei Vorteil"), "Nahkampf, 1,5 m", "Ø 5 Hieb, mit Vorteil auf den Angriff Ø 7.")
 +feat("Kurzbogen", ("+4","1W6+2 Stich","+1W4 bei Vorteil"), "Fernkampf, 24/96 m", "Ø 5 Stich.")
 +"<h2>Bonusaktionen</h2>"+flinke
 +box("Im Oneshot", "<b>Kapitel 2:</b> 4 am Wachposten (mit 2 Worgs und dem Goblin-Boss). <b>Kapitel 4:</b> 4 Bombardiere auf der Höllenfeuer-Maschine, werfen Alchemistenfeuer <span class=\"dice\">+4 · 6/18 m · 1W4 Feuer</span> zu Beginn jedes Zugs des Ziels, bis es löscht (Aktion, GES SG 10); im Käfig Dreiviertel-Deckung."))

goblin_boss = klein("Goblin-Boss", "Kleines Feenwesen (Goblinoide), chaotisch neutral", "1", GOB, GOBL, "goblin-boss.png", MH,
 [("Rüstungsklasse","17",""),("Trefferpunkte","21","(6W6)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(10,15,10,10,8,10),
 [("Fertigkeiten","Heimlichkeit +6"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 9"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Kettenhemd, Schild, Krummsäbel, Kurzbogen")],
 "<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2 Angriffe",), "", "Krummsäbel oder Kurzbogen, beliebig gemischt.")
 +feat("Krummsäbel", ("+4","1W6+2 Hieb","+1W4 bei Vorteil"), "Nahkampf, 1,5 m", "")
 +feat("Kurzbogen", ("+4","1W6+2 Stich","+1W4 bei Vorteil"), "Fernkampf, 24/96 m", "")
 +"<h2>Bonusaktionen</h2>"+flinke
 +"<h2>Reaktionen</h2>"+feat("Angriff umlenken", ("Platztausch",), "wenn er angegriffen wird", "Tauscht den Platz mit einem Verbündeten bis mittelgross in 1,5 m; der wird zum Ziel.")
 +box("Im Oneshot", "<b>Kapitel 2:</b> der Läufer am Wachposten, rennt in Runde 1 die Rampe hoch. <b>Kapitel 3:</b> der Hornist an der unteren Barrikade (Runde 1: Horn). <b>Kapitel 4:</b> oberster Bombardier auf der Maschine."))

hob_krieger = klein("Hobgoblin-Krieger", "Mittelgrosses Feenwesen (Goblinoide), rechtschaffen böse", "1/2", HOB, HOBL, "hobgoblin-krieger.png", MH,
 [("Rüstungsklasse","18",""),("Trefferpunkte","11","(2W8+2)"),("Initiative","+3","(13)"),("Bewegung","9 m","30 Fuss")],
 ab(13,12,12,10,10,9),
 [("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Halbplatte, Schild, Langschwert, Langbogen")],
 "<h2>Merkmale</h2>"+rudel("des Hobgoblins")
 +"<h2>Aktionen</h2>"+feat("Langschwert", ("+3","2W10+1 Hieb"), "Nahkampf, 1,5 m", "Ø 12 Hieb.")
 +feat("Langbogen", ("+3","1W8+1 Stich","+ 3W4 Gift"), "Fernkampf, 45/180 m", "Ø 5 Stich + 7 Gift.")
 +box("Im Oneshot", "<b>Kapitel 3:</b> Barrikaden (mit Bögen) und Ballista-Mannschaften auf Turm 1 und Turm 2. <b>Kapitel 4:</b> 4 als Leibwache vor dem Fäulnistroll, Schildformation (Halbdeckung +2 RK füreinander). <b>Kapitel 5:</b> 4 in der Verengung. <b>Kapitel 6:</b> 6 im Burghof. Kämpfen bis zur Hälfte ihrer Zahl."))

hob_hauptmann = klein("Hobgoblin-Hauptmann", "Mittelgrosses Feenwesen (Goblinoide), rechtschaffen böse · Kettennarbe", "3", HOB, HOBL, "hobgoblin-hauptmann.png", MH,
 [("Rüstungsklasse","17","Halbplatte"),("Trefferpunkte","58","(9W8+18)"),("Initiative","+4","(14)"),("Bewegung","9 m","30 Fuss")],
 ab(15,14,14,12,10,13),
 [("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Halbplatte, Grossschwert, Langbogen")],
 "<h2>Merkmale</h2>"+feat("Aura der Autorität", ("3 m","Vorteil"), "Ausstrahlung", "Er und seine Verbündeten in 3 m haben Vorteil auf Angriffs- und Rettungswürfe, solange er nicht kampfunfähig ist.")
 +"<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2 Angriffe",), "", "Grossschwert oder Langbogen, beliebig gemischt.")
 +feat("Grossschwert", ("+4","2W6+2 Hieb","+ 1W6 Gift"), "Nahkampf, 1,5 m", "Ø 9 Hieb + 3 Gift.")
 +feat("Langbogen", ("+4","1W8+2 Stich","+ 2W4 Gift"), "Fernkampf, 45/180 m", "Ø 6 Stich + 5 Gift.")
 +box("Im Oneshot", "<b>Kapitel 3:</b> je einer an der oberen Barrikade, auf Turm 1 und auf Turm 2; fällt er, feuert seine Ballista nur noch jede dritte Runde. <b>Kapitel 4:</b> 2 flankieren den Fäulnistroll, ausserhalb seiner Aura. <b>Kapitel 5:</b> einer sperrt die Verengung."))

eisenschatten = klein("Hobgoblin-Eisenschatten", "Mittelgrosses Feenwesen (Goblinoide), rechtschaffen neutral", "2", HOB, HOBL, "eisenschatten.png", MOTM,
 [("Rüstungsklasse","15","ungerüstet"),("Trefferpunkte","32","(5W8+10)"),("Initiative","+3","(13)"),("Bewegung","12 m","40 Fuss")],
 ab(14,16,15,14,15,11),
 [("Fertigkeiten","Akrobatik +5, Athletik +4, Heimlichkeit +5"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 12"),("Sprachen","Gemeinsprache, Goblinisch")],
 "<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("4 Angriffe","+ 1× Schattensprung"), "", "Vier Angriffe mit Schlag oder Wurfpfeil; dazu einmal Schattensprung, vor oder nach einem der Angriffe.")
 +feat("Schlag", ("+5","1W4+3 Wucht"), "Nahkampf, 1,5 m", "")
 +feat("Wurfpfeil", ("+5","1W4+3 Stich"), "Fernkampf, 6/18 m", "")
 +feat("Schattensprung", ("9 m",), "Teleport", "Von Dämmerlicht oder Dunkelheit in Dämmerlicht oder Dunkelheit, mit allem, was er trägt.")
 +feat("Zauberwirken", ("SG 12",), "Intelligenz", "<b>Beliebig oft:</b> Kleine Illusion, Taschenspielerei. <b>Je 1/Tag:</b> Person bezaubern, Selbstverkleidung, Stilles Bild.")
 +box("Im Oneshot (Kapitel 3)", "3 Stück im Zwischenraum hinter Bolzenkisten am Fuss von Turm 2. Alle vier Schläge auf denselben Helden, Ziel ist die Kante (Stoss statt Schlag). Sind zwei gefallen, springt der dritte in den Schatten und ist weg."))

ork = klein("Ork", "Mittelgrosser Humanoide (Ork), chaotisch böse", "1/2", ORK, ORKL, "ork.png", "Werte: Monsterhandbuch 2014 (im 2024er Handbuch gibt es keinen Ork)",
 [("Rüstungsklasse","13","Fellrüstung"),("Trefferpunkte","15","(2W8+6)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(16,12,16,7,11,10),
 [("Fertigkeiten","Einschüchtern +2"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),("Sprachen","Gemeinsprache, Orkisch")],
 "<h2>Merkmale</h2>"+feat("Aggressiv", ("Bewegung",), "Bonusaktion", "Bewegt sich bis zu seiner Geschwindigkeit auf einen Feind zu, den er sehen kann.")
 +"<h2>Aktionen</h2>"+feat("Grossaxt", ("+5","1W12+3 Hieb"), "Nahkampf, 1,5 m", "Ø 9 Hieb.")
 +feat("Wurfspeer", ("+5","1W6+3 Stich"), "Nah- oder Fernkampf, 1,5 m oder 9/36 m", "Ø 6 Stich.")
 +box("Im Oneshot (Kapitel 4)", "Die Orks der Horde auf der Ebene. Sie fliehen nie: Sie sterben oder gewinnen."))

wolf = klein("Wolf", "Mittelgrosses Tier, gesinnungslos", "1/4", WOLF, WOLFL, "wolf.png", MH,
 [("Rüstungsklasse","12",""),("Trefferpunkte","11","(2W8+2)"),("Initiative","+2","(12)"),("Bewegung","12 m","40 Fuss")],
 ab(14,15,12,3,12,6),
 [("Fertigkeiten","Wahrnehmung +5, Heimlichkeit +4"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 15")],
 "<h2>Merkmale</h2>"+rudel("des Wolfs")
 +"<h2>Aktionen</h2>"+feat("Biss", ("+4","1W6+2 Stich","liegend"), "Nahkampf, 1,5 m", "Ø 5 Stich. Ein mittelgrosses oder kleineres Ziel liegt danach am Boden.")
 +box("Im Oneshot (Kapitel 4)", "Rudel der Horde auf der Ebene, als Kleinvieh neben Goblins und Worgs."))

worg = klein("Worg", "Grosses Feenwesen, neutral böse", "1/2", WOLF, WOLFL, "worg.png", MH,
 [("Rüstungsklasse","13",""),("Trefferpunkte","26","(4W10+4)"),("Initiative","+1","(11)"),("Bewegung","15 m","50 Fuss")],
 ab(16,13,13,7,11,8),
 [("Fertigkeiten","Wahrnehmung +4"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 14"),("Sprachen","Goblinisch, Worg")],
 "<h2>Aktionen</h2>"+feat("Biss", ("+5","1W8+3 Stich","nächster Angriff mit Vorteil"), "Nahkampf, 1,5 m", "Ø 7 Stich. Der nächste Angriffswurf gegen das Ziel vor Beginn des nächsten Zugs des Worgs hat Vorteil.")
 +box("Im Oneshot", "<b>Kapitel 2:</b> 2 Worgs am Wachposten stellen sich zwischen die Helden und den Goblin-Boss, der zur Barrikade rennt. <b>Kapitel 4:</b> Reittiere der Horde. Worgs fliehen, wenn ihr Reiter fällt."))

winterwolf = klein("Winterwolf", "Grosse Monstrosität, neutral böse", "3", WOLF, WOLFL, "winterwolf.png", MH,
 [("Rüstungsklasse","13",""),("Trefferpunkte","75","(10W10+20)"),("Initiative","+1","(11)"),("Bewegung","15 m","50 Fuss")],
 ab(18,13,14,7,12,8),
 [("Fertigkeiten","Wahrnehmung +5, Heimlichkeit +5"),("Immunitäten","Kälte"),("Sinne","passive Wahrnehmung 15"),("Sprachen","Gemeinsprache, Riesisch")],
 "<h2>Merkmale</h2>"+rudel("des Wolfs")
 +"<h2>Aktionen</h2>"+feat("Biss", ("+6","2W6+4 Stich","liegend"), "Nahkampf, 1,5 m", "Ø 11 Stich. Ein grosses oder kleineres Ziel liegt danach am Boden.")
 +feat("Kälteodem", ("RW KON 12","4W8 Kälte"), "Aufladung 5–6 · Kegel 4,5 m", "Ø 18 Kälte. Erfolg: halber Schaden.")
 +box("Im Oneshot (Kapitel 1c, Ebene 1)", "4 Stück in der Windkammer, zusammen mit 2 Mantikoren. Die Helden kommen durch die Spalte einzeln an: Rudeltaktik auf den Ersten."))

mantikor = klein("Mantikor", "Grosse Monstrosität, rechtschaffen böse", "3", TRL, TRLL, "mantikor.png", MH,
 [("Rüstungsklasse","14",""),("Trefferpunkte","68","(8W10+24)"),("Initiative","+3","(13)"),("Bewegung","9 m","Fliegen 15 m")],
 ab(17,16,17,7,12,8),
 [("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 11"),("Sprachen","Gemeinsprache")],
 "<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("3 Angriffe",), "", "Reissen oder Schwanzstachel, beliebig gemischt.")
 +feat("Reissen", ("+5","1W8+3 Hieb"), "Nahkampf, 1,5 m", "Ø 7 Hieb.")
 +feat("Schwanzstachel", ("+5","1W8+3 Stich"), "Fernkampf, 30/60 m", "Ø 7 Stich.")
 +box("Im Oneshot (Kapitel 1c, Ebene 1)", "2 Stück in der Windkammer, schiessen von den Vorsprüngen drei Stacheln pro Runde, während die 4 Winterwölfe unten angreifen. Sie landen erst, wenn die Wölfe tot sind."))

troll = klein("Troll", "Grosser Riese, chaotisch böse", "5", TRL, TRLL, "troll.png", MH,
 [("Rüstungsklasse","15",""),("Trefferpunkte","94","(9W10+45)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(18,13,20,7,9,7),
 [("Fertigkeiten","Wahrnehmung +5"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 15"),("Sprachen","Riesisch")],
 "<h2>Merkmale</h2>"+feat("Regeneration", ("15 TP",), "zu Beginn jedes Zugs", "Nach Säure oder Feuer setzt sie im nächsten Zug aus. Stirbt nur, wenn er den Zug mit 0 TP beginnt und nicht regeneriert.")
 +feat("Abscheuliche Glieder", ("4/Tag",), "", "Endet sein Zug mit höchstens halben TP und 15+ Hiebschaden in diesem Zug, fällt ein Glied ab und kämpft als Trollglied weiter. Je fehlendem Glied 1 Stufe Erschöpfung; wächst nach, sobald er TP zurückerhält.")
 +"<h2>Aktionen</h2>"+feat("Reissen", ("3 Angriffe","+7","2W6+4 Hieb"), "Nahkampf, 3 m", "Ø 11 Hieb pro Treffer.")
 +"<h2>Bonusaktionen</h2>"+feat("Sturmangriff", ("½ Bewegung",), "geradeaus auf einen sichtbaren Feind", "")
 +box("Im Oneshot (Kapitel 1c, Ebene 2)", "2 Stück in der Tiefhalle beim Gifttroll. Die Ölfässer aus dem Sturmschacht sind das Feuer gegen die Regeneration."))

berserker = klein("Berserker", "Mittelgrosser Humanoide, neutral · Ork-Berserker", "2", ORK, ORKL, "berserker.png", MH,
 [("Rüstungsklasse","13","Fellrüstung"),("Trefferpunkte","67","(9W8+27)"),("Initiative","+1","(11)"),("Bewegung","9 m","30 Fuss")],
 ab(16,12,17,9,11,9),
 [("Sinne","passive Wahrnehmung 10"),("Sprachen","Gemeinsprache (hier Orkisch)"),("Ausrüstung","Fellrüstung, Grossaxt")],
 "<h2>Merkmale</h2>"+feat("Blutrausch", ("unter 34 TP: Vorteil",), "angeschlagen", "Hat er höchstens die Hälfte seiner TP, hat er Vorteil auf Angriffs- und Rettungswürfe.")
 +"<h2>Aktionen</h2>"+feat("Grossaxt", ("+5","1W12+3 Hieb"), "Nahkampf, 1,5 m", "Ø 9 Hieb.")
 +box("Im Oneshot (Kapitel 4)", "4 Stück als Leibwache des Feuerriesen. Im Duell halten sie sich raus; greift ein zweiter Held ein, ist das Duell gebrochen und sie stürmen los."))

oger_kette = klein("Oger-Kettenschläger", "Grosser Riese, chaotisch böse", "3", OGR, OGRL, "oger-kette.png", MOTM,
 [("Rüstungsklasse","11","Fellrüstung"),("Trefferpunkte","59","(7W10+21)"),("Initiative","−1","(9)"),("Bewegung","12 m","40 Fuss")],
 ab(19,8,16,5,7,7),
 [("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 8"),("Sprachen","Gemeinsprache, Riesisch")],
 "<h2>Aktionen</h2>"+feat("Faust", ("+6","2W4+4 Wucht"), "Nahkampf, 1,5 m", "Ø 9 Wucht.")
 +feat("Kettenschlag", ("+6","2W8+4 Wucht","RW KON 14 · betäubt"), "Aufladung 6 · Nahkampf, 3 m", "Ø 13 Wucht. Misserfolg: 1 Minute betäubt; neuer Wurf bei Schaden und am Ende jedes eigenen Zugs.")
 +feat("Kettenfeger", ("RW GES 14","1W8+4 Wucht","liegend"), "alle in 3 m", "Ø 8 Wucht und liegend. Erfolg: halber Schaden, nicht liegend.")
 +box("Im Oneshot (Kapitel 3)", "Einer in der Lücke der oberen Barrikade, einer auf der Plattformtreppe von Turm 1. Beide Stellen sind 1,5 m breit, seine Reichweite 3 m: niemand kommt vorbei ohne Gelegenheitsangriff. Wer betäubt auf der Treppe steht, fällt sie hinunter (1W6 Wucht)."))

oger_bolzen = klein("Oger-Bolzenschleuder", "Grosser Riese, chaotisch böse", "2", OGR, OGRL, "oger-bolzen.png", MOTM,
 [("Rüstungsklasse","13","Fellrüstung"),("Trefferpunkte","59","(7W10+21)"),("Initiative","+1","(11)"),("Bewegung","12 m","40 Fuss")],
 ab(19,12,16,5,7,7),
 [("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 8"),("Sprachen","Gemeinsprache, Riesisch")],
 "<h2>Aktionen</h2>"+feat("Faust", ("+6","2W4+4 Wucht"), "Nahkampf, 1,5 m", "Ø 9 Wucht.")
 +feat("Bolzenschleuder", ("+3","3W10+1 Stich"), "Fernkampf, 36/144 m", "Ø 17 Stich.")
 +box("Im Oneshot (Kapitel 3)", "2 Stück am Plattformrand von Turm 2, schiessen auf den Zwischenraum (keine Deckung) und den Rampenkopf. Im Nahkampf sind sie träge: Sie treten zurück und schiessen weiter, statt ihre Schleudern zu verteidigen."))

bogenschuetze = klein("Bogenschütze", "Mittelgrosser Humanoide (Hobgoblin), rechtschaffen böse", "3", HOB, HOBL, "bogenschuetze.png", MOTM,
 [("Rüstungsklasse","16","besch. Leder"),("Trefferpunkte","75","(10W8+30)"),("Initiative","+4","(14)"),("Bewegung","9 m","30 Fuss")],
 ab(11,18,16,11,13,10),
 [("Fertigkeiten","Akrobatik +6, Wahrnehmung +5"),("Sinne","passive Wahrnehmung 15"),("Sprachen","Gemeinsprache, Goblinisch")],
 "<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2 Angriffe",), "", "Kurzschwert oder Langbogen.")
 +feat("Kurzschwert", ("+6","1W6+4 Stich"), "Nahkampf, 1,5 m", "Ø 7 Stich.")
 +feat("Langbogen", ("+6","1W8+4 Stich"), "Fernkampf, 45/180 m", "Ø 8 Stich.")
 +"<h2>Bonusaktionen</h2>"+feat("Schützenauge", ("3/Tag","+1W10"), "direkt nach einem Angriffs- oder Schadenswurf mit Fernkampfwaffe", "Addiert 1W10 zum Ergebnis.")
 +box("Im Oneshot (Kapitel 3)", "2 Stück an der Brüstung von Turm 2, Dreiviertel-Deckung hinter den Zinnen (+5 RK). Schiessen auf alles, was aus dem Nebel im Zwischenraum kommt."))

hoellenhund = klein("Höllenhund", "Mittelgrosser Unhold, rechtschaffen böse", "3", FND, FNDL, "hoellenhund.png", MH,
 [("Rüstungsklasse","15",""),("Trefferpunkte","58","(9W8+18)"),("Initiative","+1","(11)"),("Bewegung","15 m","50 Fuss")],
 ab(17,12,14,6,13,6),
 [("Fertigkeiten","Wahrnehmung +5"),("Immunitäten","Feuer"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 15"),("Sprachen","versteht Infernalisch, spricht nicht")],
 "<h2>Merkmale</h2>"+rudel("des Hundes")
 +"<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2× Biss",), "", "")
 +feat("Biss", ("+5","1W8+3 Stich","+ 1W6 Feuer"), "Nahkampf, 1,5 m", "Ø 7 Stich + 3 Feuer.")
 +feat("Feueratem", ("RW GES 12","5W6 Feuer"), "Aufladung 5–6 · Kegel 4,5 m", "Ø 17 Feuer. Erfolg: halber Schaden.")
 +box("Im Oneshot (Kapitel 6)", "2 Stück zu Füssen des Throns in Kazzamirs Halle, stehen auf, wenn der Gehörnte Teufel es tut. Sie halten die Helden auseinander, damit er einzelne erwischt. Die Glutschilde sind im Finale erloschen."))

bugbear_k = klein("Bugbear-Krieger", "Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · im Buch: Pitt, der Spion", "1", GOB, GOBL, "bugbear.png", MH,
 [("Rüstungsklasse","14","Fellrüstung"),("Trefferpunkte","33","(6W8+6)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(15,14,13,8,11,9),
 [("Fertigkeiten","Heimlichkeit +6, Überleben +2"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 10"),("Sprachen","Gemeinsprache, Goblinisch"),("Ausrüstung","Fellrüstung, 3 leichte Hämmer")],
 "<h2>Merkmale</h2>"+feat("Entführen", ("keine Extra-Bewegung",), "", "Braucht keine zusätzliche Bewegung, um eine gepackte Kreatur mitzunehmen.")
 +"<h2>Aktionen <em>ein Angriff pro Zug</em></h2>"+feat("Packen", ("+4","2W6+2 Wucht","gepackt"), "Nahkampf, 3 m", "Ø 9 Wucht. Mittelgross oder kleiner: gepackt (Entkommen SG 12).")
 +feat("Leichter Hammer", ("+4","3W4+2 Wucht"), "Nah- oder Fernkampf, 3 m oder 6/18 m", "Ø 9 Wucht. Vorteil gegen ein Ziel, das er selbst gepackt hält.")
 +box("Im Oneshot (Kapitel 1b)", "Der Spion mit Toms Tasche am blinden Spalt der Wurzelkammer, kämpft halbherzig mit. Fällt die Assassine oder er unter 15 TP, ergibt er sich. Kettennarbe am Handgelenk, redet gern."), pos="50% 30%")

bugbear_p = klein("Bugbear-Pirscher", "Mittelgrosses Feenwesen (Goblinoide), chaotisch böse · im Buch: Geschützmeister Rotzahn", "3", GOB, GOBL, "pirscher.png", MH,
 [("Rüstungsklasse","15","Kettenhemd"),("Trefferpunkte","65","(10W8+20)"),("Initiative","+2","(12)"),("Bewegung","9 m","30 Fuss")],
 ab(17,14,14,11,12,11,{"KON":"+4","WEI":"+3"}),
 [("Fertigkeiten","Heimlichkeit +6, Überleben +3"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 11"),("Sprachen","Gemeinsprache, Goblinisch")],
 "<h2>Merkmale</h2>"+feat("Entführen", ("keine Extra-Bewegung",), "", "Nimmt Gepackte ohne zusätzliche Bewegung mit.")
 +"<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2 Angriffe",), "", "Wurfspeer oder Morgenstern.")
 +feat("Wurfspeer", ("+5","3W6+3 Stich"), "3 m oder 9/36 m", "")
 +feat("Morgenstern", ("+5","2W8+3 Stich"), "Nahkampf, 3 m", "Vorteil gegen Gepackte.")
 +"<h2>Bonusaktionen</h2>"+feat("Schneller Griff", ("RW GES 13","gepackt"), "eine Kreatur bis mittelgross in 3 m", "Misserfolg: gepackt (Entkommen SG 13).")
 +box("Im Oneshot", "<b>Kapitel 1b:</b> 2 hinter den Felsbrocken bei der Assassine. <b>Kapitel 3:</b> Geschützmeister auf Turm 2, kettet mit einer Aktion die Ballista ab (Reparatur SG 13)."), pos="50% 30%")

greif = klein("Greif", "Grosse Monstrosität, gesinnungslos · Verbündeter", "2", GRF, GRFL, "greif.png", MH,
 [("Rüstungsklasse","12",""),("Trefferpunkte","59","(7W10+21)"),("Initiative","+2","(12)"),("Bewegung","9 m","Fliegen 24 m")],
 ab(18,15,16,2,13,8),
 [("Fertigkeiten","Wahrnehmung +5"),("Sinne","Dunkelsicht 18 m, passive Wahrnehmung 15")],
 "<h2>Aktionen</h2>"+feat("Mehrfachangriff", ("2× Reissen",), "", "")
 +feat("Reissen", ("+6","1W8+4 Stich","gepackt"), "Nahkampf, 1,5 m", "Ø 8 Stich. Mittelgross oder kleiner: gepackt (Entkommen SG 14) in beiden Vorderklauen.")
 +box("Im Oneshot", "Die Greifen der Burg tragen die Helden: <b>Kapitel 2</b> Flug zum Krähenkamm, <b>Kapitel 6</b> Sturm auf Veldgard. Ein Greif trägt auch den fast 3 m grossen Barbaren (regeltechnisch mittelgross). Fällt ein Reiter, nimmt er in der Horde 2W6 pro Runde (GES SG 12 halb)."))

KLEIN = [
 ("K1-Goblins-und-Hobgoblins", "Kleine Karten 1: Goblins und Hobgoblins", [goblin_minion, goblin_krieger, goblin_boss, hob_krieger]),
 ("K2-Hobgoblins-Ork-Berserker", "Kleine Karten 2: Hauptmann, Eisenschatten, Ork, Berserker", [hob_hauptmann, eisenschatten, ork, berserker]),
 ("K3-Woelfe-und-Mantikor", "Kleine Karten 3: Wölfe und Mantikor", [wolf, worg, winterwolf, mantikor]),
 ("K4-Oger-Bogenschuetze-Troll", "Kleine Karten 4: Oger, Bogenschütze, Troll", [oger_kette, oger_bolzen, bogenschuetze, troll]),
 ("K5-Bugbears-Hoellenhund-Greif", "Kleine Karten 5: Bugbears, Höllenhund, Greif", [bugbear_k, bugbear_p, hoellenhund, greif]),
]
