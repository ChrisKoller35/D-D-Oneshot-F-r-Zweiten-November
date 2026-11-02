# Projektstand «Die letzte Großtat» – Übergabe

Stand: 2. November 2026 (UTC, nachmittags; Buch Version 81, GitHub main = Projektordner). Diese Datei ist das Gedächtnis des
Projekts in aufgeräumter Form, damit in einem neuen Chat oder Thread sofort
weitergearbeitet werden kann. Pro Kapitel steht in Abschnitt 4 eine
**Stand**-Zeile (fertig / in Arbeit / offen) und darunter **Offen**, also die
Fragen an Christoph, die zu diesem Kapitel noch zu klären sind. Quelle der Wahrheit sind die Markdown-Dateien in
diesem Ordner; `Buch.html` ist das daraus gebaute Kampagnenbuch zum Anklicken.

## 1. Arbeitsregeln

- **Sprache:** Christoph schreibt Deutsch (Schweizer Schreibweise mit «ss»).
  Antworten auf Deutsch. Buchtexte verwenden ß; Datei- und Ordnernamen ae/oe/ue.
- **Vorlesetexte schreibt nur Christoph**, direkt auf Schweizerdeutsch. Er
  sagt, wo sie eingefügt werden; sie werden wörtlich und **unkorrigiert**
  übernommen. Claude schreibt **keine** Vorlesetexte, auch keine hochdeutschen
  Vorlagen mehr (abgestimmt 25.10.2026). Bisher von Christoph: Intro und Heddas
  Auftritt (Kapitel 1). Fehlende Stellen stehen pro Kapitel unter «Offen».
- **Gegner nur offizielle Monster** (Monsterhandbuch 2024, Monsters of the
  Multiverse), Werte aus Christophs Sammlung `Monster-Screenshots/` (im Projektordner
  und auf dem PC) oder dem 2024-Regelwerk, nie aus 2014-Erinnerung. Nur Namen sind neu.
- **Vor jedem neuen Monsterbogen und vor neuen Trank-/Giftkarten kurz
  nachfragen**, nie von sich aus anlegen. Christoph hat zu den Karten noch
  Inputs.
- **Masse immer in Fuss UND Metern** angeben. Christoph mischt Einheiten
  («Fuss» kann Meter meinen): bei Massen rückfragen.
- **Erzähltexte** mit Aussehen, Geruch, Gefühl. Orte und Dinge schlicht
  benennen («Turm 1 rechts», «Turm 2 rechts»).
- **Arbeitsweise:** Christoph gibt immer selbst den Input, woran gearbeitet
  wird; nicht von sich aus das nächste Kapitel anfangen. Pro Kapitel ein
  eigener Thread, der Hauptchat bleibt für Kurzes. Offene Fragen werden
  gesammelt in einem eigenen Thread geklärt. Den Spieltermin hat Christoph
  selbst im Blick.
- **Nach jeder Änderung:** Markdown ändern, `Buch.html` neu bauen, PC-Kopie
  nachziehen, kurz melden.
- **Eine Quelle pro Fakt (seit 31.10.2026):** Besatzungen, Werte, Regeln
  und Namen stehen genau **einmal** ausgeschrieben, nämlich dort, wo sie
  hingehören (Besatzung im Kapitel, Werte im Feinde-/NPC-Ordner, Regeln
  in `Regeln/`). Übersichtsseiten verweisen nur oder binden den Block beim
  Buchbau ein: In der Quelldatei steht der Text zwischen
  `<!-- quelle: NAME -->` und `<!-- /quelle -->`, andere Seiten holen ihn
  mit einer Zeile `<!-- einbinden: NAME -->`; `build.py` setzt ihn ein und
  schreibt «Quelle: … – Änderungen nur dort» darunter. Wo etwas steht:
  Abschnitt 1b. Beim Schreiben neuer Texte keine Zahlen oder Listen aus
  anderen Dateien abschreiben, sondern verweisen (→ Datei) oder einbinden.
- **Kleine Änderung (Ziel: ein, zwei Minuten):** Nur im Quellen-Register
  (1b) nachschauen, wo der Fakt steht, nur diese eine Datei ändern,
  `python3 Werkzeug/Buch/build.py` laufen lassen (unter 5 Sekunden),
  Buchseite neu publizieren, eine Zeile melden. Nicht den ganzen Ordner
  nach Erwähnungen durchsuchen; wenn der Grep trotzdem Treffer in anderen
  Dateien zeigt, ist das ein Duplikat, das durch einen Verweis ersetzt
  gehört.

## 1b. Quellen-Register (wo ein Fakt genau einmal steht)

| Fakt | Einzige Quelle | Wer bindet ein / verweist |
|---|---|---|
| Besatzung Rampe, Turm 1, Zwischenraum, Turm 2 (Kapitel 3) | `Orte/Felsenpass.md`, Tabelle «Stelle / Besatzung» (Block `besatzung-felsband`) | `Feinde/Die-Horde/Beschreibung.md` (eingebunden); `Story/Story-Gesamt.md` (nur Verweis) |
| Alarmstufen auf dem Felsband | Kapitel 3, Absatz «Alarmstufen» | Horde-Fähigkeiten (Hornist) verweist |
| Wachposten Kapitel 2, Burghof Kapitel 6 (Kapitel 5 kampflos) | das jeweilige Kapitel | Horde-Beschreibung «Besetzungen» verweist |
| Drachenjagd-Regeln (Treffer, Angriffe, Veteranen-Gruppen, Initiative) | `Regeln/Geschuetze.md` («Geschütze und Drachenjagd», seit 1.11.2026 die einzige Regelseite) | Kampfübersicht, Story-Gesamt (nur Verweis) |
| Werte der Hordenkreaturen (RK, TP, Angriffe) | `Feinde/Uebersicht.md`, Tabelle «Werte der Hordenkreaturen» | Kapitel nennen nur Namen |
| Standort einer Hordenkreatur (welcher Turm) | nur die Besatzungstabelle in Kapitel 3 | Werte- und Fähigkeitstexte sagen «ihr Turm / seine Stellung» |
| Welche Gegner in welchem Kampf (Anzahl, HG, RK, TP, wie ein Ziel fällt) | `Feinde/Uebersicht.md` (Kampfübersicht, seit 1.11.2026 die einzige Seite unter Feinde; bindet `besatzung-felsband` ein) | Orte, Regeln, Karten verweisen; `build.py` leitet alte `Feinde/<Ordner>/`-Verweise auf diese Seite |
| Werte der NPC | der jeweilige `NPC/…/Stats/` | Kapitel verweisen |
| Kettennarben (wer eine trägt) | `Feinde/Uebersicht.md`, Absatz «Kettennarben» | – |
| Schildträger-Gruppen (RK, TP, Angriff) | `NPC/Soldaten-und-Trupp-Eisenwacht/Stats/Stats.md` | Drachenjagd-Kurzfassung nennt die 65 TP als einzige Ausnahme (Spielregel der Szene) |
| Hedda und Hauptleute (Werte) | `NPC/Marschallin-Hedda/Stats/`, `NPC/Die-Verbuendeten/Stats/` | Kapitel 4 Szene 3 verweist |
| Tränke, Gifte, Schliffe | `NPC/Druide-Tom/Handout-Toms-Traenke.md`, `Belohnungen/Uebersicht.md` (Schliffe) | Kapitel verweisen |

Noch nicht zusammengeführt (auf Zuruf): die Kapitel nennen bei der Szene
oft RK/TP eines Gegners nochmals («RK 18, 143 TP»), damit man am Tisch
nicht blättern muss. Das ist bewusst so gelassen; bei Wertänderungen
dort mit Grep nachziehen.

## 2. Die Gruppe

3 Spieler, Stufe 8, starke Ausrüstung (je ein seltener und zwei ungewöhnliche
Gegenstände; einer ist Barbar, fast 3 m / 10 Fuss gross, regeltechnisch
mittelgross – ein normaler Greif trägt ihn, Hinweis steht bei den Greifen),
plus NPC-Gefährte **Milo Klee** (Bauer, Koch, Heiler; **Kleriker 8,
Lebensdomäne**, 104 TP, RK 19, nach Christophs Charakterbogen vom
1.11.2026; seit 31.10.2026 statt des Schurken Bram). Balance für vier
Kämpfer Stufe 8.

## 3. Welt und Rahmen

- Oneshot, **eigenständig**, keine Verbindung zur Hauptkampagne.
- Land **Nordgar** im hohen Norden (weite Felder, Weiden, Burgen,
  Garnisonsstädte), Hauptstadt **Dunmar** ganz im Süden. Kein Zusammenfluss
  zweier Flüsse.
- Die **Horde** (Goblins, Hobgoblins, Orks; «Kettenhorde» gestrichen,
  Kettennarben und Skralls Kettenbanner bleiben) kam im Frühjahr über den
  **Felsenpass** aus dem Osten bis vor Dunmar und wurde zurückgedrängt. Heute:
  Schlacht um **Burg Rabenwacht** (offenes Land vor dem Pass). Endfestung
  **Burg Veldgard** am offenen Ende des Passes, im Land **Veldaren** (bis
  26.10.2026 «Auenstein» und «Auenland»).
- Felsenpass: Ebene (Kampffeld), Felsvorsprung mit Verengung, dahinter links
  der Kessel mit dem Hordenlager (Zelte, keine Gebäude), rechts läuft die
  Schlucht offen nach Veldgard aus. Kein Tor, keine Schleuse.
- **Verbündete** (Christoph, 26.10.2026, in der Ausgangslage): **Sildoras**
  (Weinland im Süden, die Sonnenlanzen, 300 Reiter in roten Mänteln),
  Zwergenfeste **Dhurgan** (Westgebirge, die Hammergarde, Armbrüste und
  Pioniere), Goliath-Clans vom Hochland **Skarn** (ein Dutzend Träger),
  Waldreich **Thalvien** (Südosten, die Grünpfeile, Bogenschützen).
  Zusammen ein Viertel des Heeres, alle unter Hedda. **Seit 31.10.2026**
  mit Hintergrund und Hauptleuten in `NPC/Die-Verbuendeten/` (Christoph
  abgenommen): Ritter Aurel Vanthis (Sonnenlanzen), Brannok Grauhammer
  (Hammergarde; Tilda Fenn und Brida Steinhand gehören dazu), Thuluk
  Wolkentreter (Goliaths; Skadi gehört dazu), Sarenne Ilwyn (Grünpfeile,
  Halbelfen, eigene Kompanie abseits, mag die Zwerge nicht). Erwähnt in
  Kapitel 1 (Kriegsrat, Fest), Kapitel 7 (Totenfeuer). Nicht in Kapitel 3
  eingebaut (Vorschlag dazu in `_Entwuerfe/Verbuendete-Laender-Vorschlag.md`,
  nur auf Zuruf). **Kampfwerte seit 31.10.2026** (Thread «Kampfwerte für
  Hedda und die Hauptleute festlegen») in
  `NPC/Die-Verbuendeten/Stats/Stats.md` (Christoph abgenommen): je Werte, TP, RK, eine Angriffs- und
  eine Schutzfähigkeit (Aurel HG 8, 110 TP, Sturm der Sonnenlanzen /
  Sonnenschild; Brannok HG 9, 127 TP, Wo es knirscht gegen Konstrukte /
  Fels im Sturm; Thuluk HG 9, 150 TP, Felswurf / Steinhaut; Sarenne HG 8,
  104 TP, Blattschuss / Laub im Wind; bewusst ohne magische oder versilberte
  Waffen, damit sie die Maschine nur anhalten, nicht töten, und sie greifen
  den Kessel nicht an, Christoph 31.10.2026). Hedda auf 120 TP, HG 8, mit «Befehl:
  Schlagt zu!» und «Unbeugsam». Zweck: Sie halten in Kapitel 4 die
  Höllenfeuer-Maschine 3–4 Runden auf, bis die Helden kommen (Erzählerregel
  in der Stats-Datei, Hinweis in Kapitel 4 Szene 3).
- **Lenja** (Christoph, 31.10.2026): Zwergin, nur Charakterbeschreibung,
  keine eigenen Werte/Fähigkeiten mehr (Datei nach `_to_delete/`), kein
  «Atemrhythmus»; Greifen-Werte bleiben in `NPC/Rittmeisterin-Lenja/Stats/`.
- Völker (Vorschlag, nicht im Buch): Menschen, Zwerge, Goliaths, Halblinge;
  Gnome und Elfen als Einzelfiguren; Orks nur in der Horde.

## 4. Feste Entscheidungen pro Kapitel

**Kapitel 1 – Kriegsrat und Siegesfeier.** Beginnt nachmittags beim
Einrichten (26.10.2026: Schlacht fand draussen statt, Burg grösstenteils
intakt, freigeräumt nur für die Zeltreihen um die Burg und im Hof). Christophs Intro wörtlich nach dem Info-Text (endet im grossen
Saal; Anschluss: Schreie aus dem Raum am Hof). Heddas Auftritt ebenfalls
Christophs Text (blutiges Kurzschwert, zwei Gefangene, Vorschlag
Besprechungsbüro). Tom und Orvin kommen nur auf Verlangen ins Büro. Bote zur
Drachin nur auf Nachfrage: Sturmmagier Elion schaltet Nymeria frei. Toms
Labor liegt im Keller. Neben-NPC eingetragen (Christoph kann streichen): Bote
Bastian Kolk; Hauptmann Corvin Rask (Trupp Eisenwacht, 8 Meuchler, nimmt die
linken Türme); Meuchler Jorik (Heddas Sohn), Ilva Kurzschritt, Kessa Vorrin (seit
31.10.2026), Ruben Tal (Skadi seit 31.10.2026 nicht mehr in der Eisenwacht, sondern bei den
Goliaths aus Skarn); Feier: Koch Melle, Wenzel Brack, Tilda Fenn; Hordenlager: Hauke Dorn,
Brida Steinhand, Ole Vinter.
- Stand: **fertig** (Text und Begegnungen), Abnahme der Neben-NPC offen.
- Offen: Woher kam die Horde? Buch sagt Osten (Felsenpass), Christophs Intro
  sagt «vom Norde her». Hedda: «Eisenbrecht» oder «Weisenbrecht»?
  Neben-NPC-Namen abnehmen.
  Gebäudezuordnung auf der Burgskizze `Karten/01-Burg-Rabenwacht.svg`.
  Vorlesetext fehlt: Heddas Lagebericht (nice to have: Feier, Spion, Nacht).

**Tränke und Schliffe.** Toms Tränke = 11 Stück (Heiltränke ohne «Höchster»,
Vitalität, Heldenhaftigkeit, Riesenstärke/Feuerriese, Wachstum, Fliegen,
Unsichtbarkeit, Trank der Verkleidung als Hausrezept mit echter anderer
Gestalt für 1 h; seit 29.10.2026 auf Karte und Handout bewusst OHNE Nennung
von Goblin/Hobgoblin/Ork, damit der Türme-Plan nicht verraten wird, neues
Bild ohne Goblingesichter); Schnelligkeit nur «vielleicht 1×».
**Seit 1.11.2026:** Nr. 11 Trank des Feueratems (2 Stück, 2024 DMG, Bonusaktion,
9 m, GES DC 13, 4W6 Feuer, 3 Stösse) und bei Orvin **Feuerpfeile** (12 Pfeile,
+1W6 Feuer wie *Flammenpfeile*, einmalig; 2.11.2026 von Christoph von 3W6 auf 1W6
gesetzt, dafür Schreckenstroll-Regel: bei 0 TP tötet jedes Feuer/jede Säure),
beides als Feuerquelle gegen den Schreckenstroll;
Karten `Trankkarten/11-…` und `12-…`, Druckbogen `Trankkarten/Feuer/`.
Gestrichen: Feuerschutz, Öl der Schärfe, Unverwundbarkeit, Höchster Heiltrank.
Toms Giftschrank: 14 Gifte nach Spielleiterhandbuch, ein Gift pro Held
(Kazzamir, Maschine, Teufel sind giftimmun). Zwei Tränke pro Held, in Kapitel 5
zwei weitere für die Gruppe. Orvins Schliffe: jede Waffe +1
(nie über +2 gesamt), **eine** Rüstung +1, Glutschild = Feuerresistenz nur auf
Schilden, jeder mit Schild kann einen haben, vor der Schlacht für 10 Stunden
aktivierbar (im Finale erloschen). Kettenbrecher, Greifenriemen, Bolzenfeder
ohne Limit.
- Stand: **fertig** (Liste, Schliffe, Trank- und Giftkarten). Neue Karten nur
  nach Rückfrage; Christoph hat noch Inputs.

**Kapitel 1b – Tunnel des Spions (optional).** Alter Fluchtgang der Burg,
führt von einer Senke in den Hügeln vor der Burg in den Keller; in Rabenwacht
wusste niemand davon; führt **nicht** zu den Türmen, hat keinen weiteren
Nutzen. Pitt = **Bugbear-Krieger** (HG 1, 2024-Werte: RK 14, 33 TP), kam nachts
durch den Gang, stahl Toms Phiolentasche; kein Verkleidungstrank, kein
Trossknecht, kein Bauer. Kettennarbe bleibt, er redet gern, ergibt sich unter
15 TP. Hinterhalt in der Wurzelkammer: **Nadel** (Assassine HG 8, 2024: RK 16,
97 TP, drei Kurzschwert-Angriffe je +5W6 Gift) + **2 Bugbear-Pirscher** (HG 3)
+ Pitt. Gewinn: nur die Tränke.
- Stand: **fertig** (Umbau 24./25.10.).
- Offen: Passen nach dem Umbau zum Bugbear Kettennarbe, zweiter Versuch in
  Kapitel 5 und Auftritt am Totenfeuer noch? (vorerst belassen, Notiz im
  Buch). Vorlesetext: nice to have.

**Kapitel 1c – Die gekettete Drachin (optional).** Nymeria an einem
Siegelstein, Schwert Silberzahn in den Echohallen. **Dungeon neu seit
25.10.2026** (Thread «Dungeon der Sturmland-Sidequest besetzen»): heisst
**Ebene 1, Ebene 2, Bossraum**; **nur Bestien des Sturmgebiets, keine
Drachen, keine Teufel** (Christoph). Ebene 1: Windkammer mit 2 Mantikoren
(ohne Namen) und 4 Winterwölfen, Brutkammer mit 2 Chimären und Gelege;
Sturmschacht als Abstieg (Rast, zwei Ölfässer der Horde = Feuer gegen
Trolle); Ebene 2: Tiefhalle mit Gifttroll (MotM HG 7) und 2 Trollen;
Bossraum: Spiegelkammer mit **Schreckenstroll** (MotM HG 13, bewusst
brutal, stirbt nur durch Feuer/Säure bei 0 TP). Kazzamirs Kettenwächter
(Kettenteufel + Bartteufel) gestrichen, Ordner nach `_to_delete/`. Ordner:
`Feinde/Mantikore-der-Windspalte/`, `Feinde/Winterwoelfe-der-Windkammer/`,
`Feinde/Chimaere-der-Echohallen/`, `Feinde/Trolle-der-Tiefhalle/`,
`Feinde/Schreckenstroll/`. **Kampfkarten seit 27.10.2026** (Thread «Top-down-Karten
für den Dungeon erstellen»): `Karten/06-Echohallen-Ebene-1.png` bis
`11-Echohallen-Spiegelkammer.png` (Draufsicht, 5-Fuss-Raster, Bildmodell), je
eine zweite Fassung in `Karten/Echohallen-Varianten/`, Legende in
`Karten/Karten.md`; Abnahme durch Christoph offen. Richtwert 2 h 45. Montage ohne Maschine; Gruppe
landet in Kapitel 5. Silberzahn zerbricht bei der Befreiung (Christoph 1.11.2026), keine Beute. **Wer sie
gekettet hat (NEU 1.11.2026, Thread «Nymeria Bild, Namen und
Vorgeschichte», ersetzt die Lich-Fassung vom 27.10.):** eine fremde
Frau, Abenteurerin und Kartenzeichnerin, halb verhungert, von Nymeria
gerettet; kam jährlich mit Karten; eines Tages Karte ziehen und drehen
= Zauber, Magie in Kristall gezogen, magische Ketten versiegeln sie;
die Frau zeigt sich als Dämonisches (weisses Gesicht, zu breites
Lachen, leere weisse Augen) und löst sich in schwarzem Rauch auf. Die
anderen Drachen konnten das Siegel nicht brechen; das Schwert im
Drachenhort-Schatz neutralisiert Zauber, der grosse Drache passte nicht
durch den Menschen-Durchgang, die kleinen kamen nie zurück. Text auf
Nymerias NPC-Seite (Abschnitt «Wie sie in Ketten kam», «Wesen»
gestrichen). Kein Lich mehr. Zeitpunkt (letztes Jahr / vor den
Angriffen / früher): ein paar Monate vor dem Angriff der Horde (Christoph 1.11.2026, nur Notiz, nicht im Buch). Porträt
`Bilder/Silberdrachin-Nymeria.png` (Christoph, 1.11.2026). **Name seit 1.11.2026 abends: Nymeria Valcastre** (vorher Argentys; Christophs Wahl aus Vorschlägen, im Text kurz «Nymeria»; Ordner, Bild und Monsterbogen 01 umbenannt).
- Stand: **fertig** (Besetzung von Christoph entschieden 25.10.2026,
  Werte aus den Screenshots, vier Kämpfer Stufe 8).
- Offen: Hat die Gruppe verlässlich Feuer/Säure (Frage an Christoph,
  sonst reichen die Ölfässer nur für die kleinen Trolle)? Monsterbögen A4
  nur auf Zuruf. Vorlesetexte fehlen: Sturmschacht, Tiefhalle, Bossraum.

**Kapitel 2 – Der Weg zu den Türmen.** Greifen bis zum Krähenkamm, kein
Klettern, nur die **Rampe**. Leise = Nebelsteig, Wachposten umgehen, im Rauch
die Rampe hinauf. Dreist = als Hobgoblin-Trupp mit Losung «Kettenbruch».
Wachposten am Rampenfuss: 4 Goblins, 2 Worgs, Goblin-Boss, der hochrennt und
die untere Barrikade warnt. Kein Versorgungs- oder Geheimgang (nur Idee im
Hinterkopf).
- Stand: **in Arbeit**, Umbau auf das Felsband gemacht, Abnahme durch
  Christoph offen.
- Offen: Vorlesetexte fehlen: Greifenflug, Ankunft an der Rampe.

**Kapitel 3 – Die Geschütztürme (Gelände final 25.10.).** Die «Türme» sind
reine Ballisten-Stellungen: gemauerte Plattformen mit Brüstung und je einer
Steintreppe, keine Räume. Beidseits der Schlucht ein Felsband mit je zwei
Stellungen, Heldenseite rechts. Rampe 40 m / 130 Fuss, links der Abgrund, mit
zwei Barrikaden: untere (2 Hobgoblin-Krieger mit Bögen, Goblin-Hornist =
Alarm für das ganze Band), obere am Rampenkopf (2 Krieger, 1 Hauptmann, 1
Oger-Kettenschläger in der Lücke). **Besatzungen getauscht am 31.10.2026
(Christoph, Thread «Turmbesatzungen am Felsenpass tauschen»):** Turm 1 direkt
am Rampenkopf (3 m hoch, eine Ballista, Pechtopf an der Treppe GES 13 / 3W6
Feuer, Beobachtungsstand) trägt jetzt die schwere Besatzung: 2 Krieger,
1 Hauptmann, 2 Bogenschützen, 2 Oger-Bolzenschleudern, Hobgoblin-Verwüster
(70 TP) auf dem Beobachtungsstand. Zwischenraum **7 m / 22 Fuss** (3 Hobgoblin-Eisenschatten im
Hinterhalt, eine Ballista von Turm 2 auf den Zwischenraum gedreht). Turm 2
(4,5 m hoch, zwei Ballisten): 2 Krieger, 1 Hauptmann, 1 Oger-Kettenschläger
auf der Treppe und **Champion (MotM, HG 9) oben an der Treppe** (bleibt dort,
Christoph 31.10. spät: «der Champion muss noch zu Turm 2 rechts»). **Bugbear-Pirscher
(Geschützmeister) gestrichen**, kommt nur noch bei Nadel (Kap. 1b) vor;
Abketten in `Regeln/Geschuetze.md` nur noch als optionale Regel. Die
Eigennamen Bruchhand, Rotzahn, Vask sind überall durch Monsterbezeichnungen
ersetzt (Champion, Hobgoblin-Verwüster); nur die gedruckten Monsterbögen
tragen sie noch im Untertitel. Szene 2 = Turm 1 (20 Min., Beschuss und
Magie), Szene 3 = Zwischenraum und Turm 2 (15 Min., Kampf um die Treppe). Beschuss von Turm 1 wirkt schon
auf die obere Barrikade. **Keine Drachen im Turmkampf** (Christoph,
25.10.2026): Die Drachen sind im Hordenlager angekettet und steigen erst auf,
wenn Turm 2 rechts gefallen ist; dann Szene 4 = Minigame Drachenjagd. **Die
Drachen sind drei junge rote Drachen (Monsterhandbuch 2024, HG 10), keine
Wyvern** (Christoph, 25.10.2026 abends); Ordner `Feinde/Rote-Drachen/`.
**Drachenjagd neu seit 31.10.2026** (Christophs Vorgaben, Thread
«Drachenjagd-Szene mit Soldatengruppen ausarbeiten»): eine einzelne
Szene mit vereinfachten Regeln (`Regeln/Drachenjagd.md`). Unten
**5 Schildträger-Gruppen** (20er-Gruppen mit Veteranen-Werten aus dem
Thread «Truppengruppen fürs Schlachtfeld anlegen»: RK 17, +5, fest 12
Schaden, 65 TP je Gruppe; Datei
`NPC/Soldaten-und-Trupp-Eisenwacht/Stats/Stats.md`), **eigener Pool pro
Gruppe** (Christoph 31.10.2026: weiche Fassung, jeder Drachenangriff
trifft nur eine Gruppe, der Erzähler wählt welche; gemeinsamer Pool 325
nur als harte Variante), Gruppe auf 0 = weg und −1 Leiste; **keine
Initiative**, sie handeln am Rundenende. **3 Drachen ohne TP**, je zwei
Ballistentreffer (1W20+6 gegen 15), natürliche 19–20 = sofort tot. Je
zwei Angriffe: **Sturzflug** +10 auf eine Ballista (RK 15, zwei Treffer =
zerstört, Bedienung GES 15 oder 2W6+6+1W6) oder eine Gruppe (RK 17, 25
auf die Gruppe), danach bleibt er bis zu seinem nächsten Zug dort, auch
bei zerstörter Ballista (Christoph 31.10.2026); **Flammenattacke**
nur auf Soldaten, fest 20 auf eine Gruppe, danach schlagen die Gruppen am
Rundenende zurück. Heldenschaden mit Waffen/Zaubern: **Schadenszähler,
60 = 1 Treffer** (Christoph gewählt, 31.10.2026). Spott und Kette packen
bleiben. Alte Regel (drei Treffer, Feueratem auf die Plattform, Leiste
ab Runde 4) überall ersetzt (Kap. 3 Szene 4 und Szenarien, Rote Drachen,
Geschütze, Schlachtenleiste, Story-Gesamt). Keine Sturztode.
- Stand: **fertig** – Gelände und Besetzung abgenommen 25.10.2026;
  Besatzungstausch Turm 1/Turm 2 vom 31.10.2026 (spät abends) umgesetzt,
  Abnahme durch Christoph offen (PC-Kopie vom 31.10. enthält ihn noch nicht);
  Drachenjagd nach Christophs Vorgaben vom 31.10.2026 umgebaut,
  Christoph am 31.10.2026 abends: «der Rest ist cool»; Pools pro
  Gruppe und Bleiben nach dem Sturzflug auf seinen Wunsch eingebaut.
  **Keine feste Zielregel** für die Drachen (Christoph: er will jeden
  Zug flexibel steuern, damit die Gruppe es schafft).
- Offen: nichts Neues zur Drachenjagd. Monsterbogen `14-Wyvern` ist
  überholt, Bogen «Junger Roter Drache» nur auf Zuruf; weitere Bögen
  (Hobgoblin-Verwüster, Oger, Eisenschatten, Bogenschütze) ebenfalls nur
  auf Zuruf. Vorlesetexte fehlen: Rampe, Turm 1, Aufstieg der Drachen,
  Ende der Drachenjagd.

**Kapitel 4 – Die Schlacht auf der Ebene (grosse Ziele final 25.10.).** Alle
drei grossen Ziele müssen fallen. **Die grossen Ziele tragen keine
Eigennamen mehr** (Christoph, 25.10.2026: «Urgash», «Skrall», «Moderzahn»,
«Grollhorn» gestrichen, nur Monsterbezeichnungen; Ordner
`Feinde/Hellfire-Engine/`, `Feinde/Feuerriese/`,
`Feinde/Kriegspriester-und-Faeulnistroll/`). Aufstellung vom Heer aus:
**links** der Fäulnistroll mit dem Banner, **Mitte** die Hellfire Engine,
**rechts** der Feuerriese. **Hellfire Engine** = Höllenfeuer-Maschine (MotM
HG 16, Kessel RK 12 / 60 TP oder 4 Goblin-Bombardiere; −1 Leiste pro
Runde). **Feuerriese** (HG 9, RK 18, 162 TP, glühender Mühlstein =
Flammenschwert, immun Feuer; die Horde nennt ihn Riesenork) + 4 Berserker;
Duell-Regel bleibt. **Fäulnistroll** (MotM HG 9, 138 TP, keine
Regeneration, nekrotische Aura 2W10, Feuer/Säure schaltet sie eine Runde
ab) trägt das Kettenbanner im Rücken; daneben ein **Eisenkorb**, in dem der
**Kriegspriester** (MotM HG 9, RK 20 im Korb, Heiliges Feuer, Flammenschlag,
heilt den Troll; der «Hochpriester», der Kazzamir gerufen hat) sitzt –
Christophs Idee. Drumherum 4 Hobgoblin-Krieger und 2 Hauptmänner. Ziel
fällt, wenn der Troll fällt (Priester stürzt aus dem Korb), das Banner
gerissen wird (klettern + reissen, je Athletik DC 15) oder die Stange 30 TP
nimmt; der Priester allein reicht nicht. Christoph weiss, dass alle drei
brutal stark sind, und will es so («es wird Wege geben»). **Nymeria** = Uralter Silberdrache (2024, HG 23, RK 22,
468 TP) als Spielerbogen (Handout): pro Zug Sturzflug auf die Maschine oder
Odem auf die Horde; die Maschine schiesst auf sie statt aufs Heer; bei 0 TP
Rückzug; führt: Befreier aus 1c, sonst wer den Boten vorschlug, sonst reihum.
- Stand: **in Arbeit** – die drei grossen Ziele sind von Christoph
  entschieden (25.10.2026, Thread «Grosse Gegner für die Schlacht
  festlegen»); Szenen 1–3 und Szenarien sind darauf angepasst, aber noch
  nicht als Ganzes abgenommen.
- Offen: Kessel (60 TP) knackt Nymeria meist im
  ersten Sturzflug: mehr Kessel-TP? Monsterbögen für alle drei Ziele liegen seit
  25.10.2026 in `Monsterboegen/` (06 bis 08). Vorlesetexte fehlen: Entscheidung, Flug
  über die Schlacht, «Die Horde bricht».

**Kapitel 5 – Das Hordenlager.** Zeltlager im Kessel. **Kein Kampf** (Christoph,
1.11.2026): Die Horde flieht am eigenen Lager vorbei den offenen Pass hinunter, die
Helden nehmen Verengung und Kessel kampflos ein und errichten dort ihr eigenes Lager.
Der frühere «bewusst kleine Kampf» (Hobgoblin-Hauptmann + 4 Hobgoblins an der Enge)
ist gestrichen. Rast, Siegestrunk, Heddas Plan, Nymerias Fragen, Pitt (zweiter
Versuch, falls nicht gefasst).
- Stand: **offen**, noch nicht durchgegangen; Kampflosigkeit eingebaut in
  `Story/Story-Gesamt.md`, `Orte/Hordenlager.md`, `Feinde/Die-Horde/Beschreibung.md`.
- Offen: Pitt-Frage (siehe 1b). Vorlesetexte fehlen: Marsch, Einnahme, Rast.

**Kapitel 6 – Sturm auf Veldgard.** Per Greif in die Burg; Finale nur Helden
+ Bram gegen **Kazzamir** (Gehörnter Teufel HG 11, 250 TP) + **2 Höllenhunde**
(Werte Monsterhandbuch 2024, Screenshot fehlt noch in der Sammlung). Kein
resistenz-ignorierendes Höllenfeuer; Glutschilde sind im Finale erloschen.
- Stand: **offen**, Finale auf Stufe 8 nachgeschärft, Rest nicht durchgegangen.
  **Karte 5** `Karten/05-Burg-Veldgard.svg` (Burg von oben: Landeplatz, Hof,
  Torhaus, Gang, Halle, Legende in `Karten/Karten.md`) seit 25.10.2026 als
  Entwurf im Buch, Abnahme durch Christoph offen (Thread «Burgkarte von oben
  für den Endboss zeichnen»).
- Offen: Höllenhund-Werte am 25.10.2026 gegen die offiziellen 2024-Daten
  geprüft (SRD 5.2, frei lesbar) und in Kazzamirs Stats eingetragen;
  Screenshot für die Sammlung und A4-Monsterbogen (braucht Bild, also
  GOOGLE_API_KEY) noch offen. Vorlesetexte fehlen:
  Morgen vor Veldgard, Eindringen, Kazzamirs Halle, Ende der Schlacht.

**Kapitel 7 – Nach der Schlacht.** Preis (Schlachtenleiste), Totenfeuer,
Abschiedsfeier, Milos Abschiedsessen und sein Laden.
- Stand: **offen**, noch nicht durchgegangen.
- Offen: Pitt am Totenfeuer (siehe 1b). Vorlesetexte fehlen: Preis,
  Totenfeuer, Milos Abschied.

**1.11.2026, Feinde zu einer Kampfübersicht zusammengefasst** (Thread
«Feinde zu einer Kampfübersicht zusammenfassen», Christophs Wunsch: die
vielen Einzelkategorien unter FEINDE durch eine übersichtliche Liste
ersetzen, welche Monster in welchen Kämpfen vorkommen): `Feinde/` enthält
nur noch `Uebersicht.md` (Nav: FEINDE → Kampfübersicht). Pro Kampf eine
Tabelle (Gegner, Anzahl, HG, RK, TP, Quelle MM/MotM) und zwei, drei
Punkte Besonderes (wie ein großes Ziel fällt, Regeneration, Duell,
leichtere Fassung); am Ende die Werte-Tabelle der Hordenkreaturen, Moral
und Kettennarben. Erzählertexte (Erscheinung, Wesen, typische Sätze,
Kazzamirs Finale-Staging, Fähigkeiten-Seiten) stehen **nicht** mehr im
Buch, sondern nur noch in `_to_delete/Feinde-alt-2026-11-01/`
(rückholbar). Monsterbögen und Kampfkarten bleiben; Hinweise «Druckbogen
X verwenden» sind mit den Feinde-Seiten weg. `build.py` leitet alle alten
Verweise `Feinde/<Ordner>/…` auf die Kampfübersicht. Hobgoblin-Verwüster
steht mit 45 TP (MotM); die alte Seite nannte zusätzlich 70 TP
(verschärft) – Entscheid offen.

**1.11.2026, Echohallen → Drachenhort** (Christoph, Thread «Feinde zu
einer Kampfübersicht zusammenfassen»): Der Dungeon aus Kapitel 1c heißt
jetzt **Drachenhort** (`Orte/Drachenhort.md`, vorher `Orte/Die-Echohallen.md`);
Text in Story-Gesamt, README, Karten, Belohnungen, Toms Tränke, Nebenquest
Sturmhüterin umgestellt. In der Kampfübersicht heißen die Teile nur noch
Ebene 1 (Mantikore, Winterwölfe, Chimären), Ebene 2 (Gifttroll, 2 Trolle),
Bossraum – Schatzkammer (Schreckenstroll); kein Gelege mehr. Die Raumnamen
Windkammer/Brutkammer/Sturmschacht/Tiefhalle/Spiegelkammer stehen noch in
`Orte/Drachenhort.md` und `Karten/Karten.md` (Kartendateien heißen weiter
`06-Echohallen-…` bis `11-Echohallen-…`), Umstellung offen. Ältere
Erwähnungen «Echohallen» weiter unten in dieser Datei sind Geschichte.

**1.11.2026, Regeln verschlankt** (Christoph, Thread «Feinde zu einer
Kampfübersicht zusammenfassen»): `Regeln/` enthält nur noch
`Geschuetze.md` («Geschütze und Drachenjagd»): Ballisten (1W20+6 gegen 15,
zwei Treffer = Drache stürzt, natürliche 19–20 sofort tot, 60 Heldenschaden
= 1 Treffer), Drachen mit Feueratem (20 fest auf eine Gruppe) und Sturzflug
(+10, Ballista RK 15 / Gruppe RK 17 für 25), fünf Veteranen-Gruppen mit
Schilden (RK 17, 65 Pool, +5 für 12 am Rundenende), Initiative für Drachen
und Helden. **Greifenflug, Schlachtenleiste und die lange Drachenjagd sind
gestrichen** (`_to_delete/Regeln-alt-2026-11-01/`, dort auch die alte
Geschütze-Seite); alle Verweise und Leisten-Werte (−1/+1 Leiste) in NPC,
Quests, Orte, Story-Gesamt, README entfernt. Quellblock `drachenjagd-kurz`
existiert nicht mehr.

## 4b. Woran wir zuletzt gearbeitet haben (24./25. Oktober 2026)

**31.10.2026, Doppelte Angaben zusammengeführt** (Thread «Doppelte Angaben
im Buch zusammenführen», Anlass: der Besatzungstausch brauchte Änderungen
an acht Stellen): `build.py` kann Blöcke einbinden (`<!-- quelle: … -->` /
`<!-- einbinden: … -->`). Besatzungstabelle nur noch in Kapitel 3,
eingebunden in Felsenpass und Horde-Beschreibung; Horde-Stats, Werte-
und Fähigkeitstexte ohne Turmnummern; Story-Gesamt Akt 3 ohne
Gegnerliste. Drachenjagd-Kurzfassung nur in `Regeln/Drachenjagd.md`,
eingebunden in Kapitel 3 Szene 4; Rote Drachen, Geschütze,
Schlachtenleiste, Story-Gesamt verweisen nur noch. Kettennarben-Liste nur
bei der Horde. Arbeitsregel «Eine Quelle pro Fakt» und Quellen-Register
(Abschnitt 1b) ergänzt.

- Gruppe auf Stufe 8 gehoben, Turmkämpfe und Finale nachgeschärft (Höllenhunde).
- Trank- und Giftkarten im Magic-Stil fertig; Trankliste und Orvins Schliffe final.
- Regionskarte von Christoph übermalt, ausgebessert, abgenommen und ins Buch
  übernommen.
- Monsterbögen A4: Nymeria, Hellfire Engine (Bogen heisst noch «Grollhorn»), Nadel, Pitt, Bugbear-Pirscher.
- Nymeria von «erwachsen» auf Uralter Silberdrache (HG 23) umgestellt, inkl.
  Spielerbogen und Kapitel 4.
- Kapitel 1b neu aufgestellt: Pitt als Bugbear-Krieger aus dem Fluchtgang,
  Nadel mit zwei Bugbear-Pirschern; Toms Labor im Keller.
- Kapitel 2/3 komplett auf das Felsband umgebaut (Rampe mit zwei Barrikaden,
  offene Ballisten-Stellungen, 22 Fuss Zwischenraum, kein Geheimgang).
- Liste der Stellen erstellt, an denen schweizerdeutsche Vorlesetexte fehlen
  (Abschnitt 6).
- Projektordner und PC-Ordner abgeglichen, Audio nachkopiert, `Buch.html`
  als Offline-Buch eingeführt, Werkzeuge in den Ordner gelegt.

**31.10.2026, Bram → Milo Klee:** Der NPC-Gefährte «Bram der Held»
(Schurke, Sänger) ist gestrichen, weil ein Spieler neu einen Barden
spielt. Ersatz: **Milo Klee**, Bauer, Koch und bescheidener Heiler
(Christophs Figur: Großmutter war eine Heldin, ihr Ring, kein Talent
für Zauber, nur ein paar Heilzauber, dafür guter Koch; will danach in
einer Stadt eine Bäckerei oder ein Wirtshaus aufmachen). Ordner
`NPC/Milo-Klee/` (Werte **seit 1.11.2026 nach Christophs Charakterbogen**:
Kleriker 8, Lebensdomäne, 104 TP, RK 19, WEI 18, Zauber bis Grad 4,
Göttliche Macht, Lucky Points, Heiliges Feuer als einziger
Angriffszauber; PDF in `_Entwuerfe/Milo-Klee-Charakterbogen.pdf`).
Christoph: Kann er nicht als NPC mitkommen, wird er in der Küche
eingebaut – aktuell kommt er mit. Zusätze aus dem Buch (nicht auf dem
Bogen, streichbar): «Großmutters
Ring» (1× pro Abenteuer, Held bleibt auf 1 TP, Stein danach grau) statt
«Mit viel Glück»; «Großmutters Kräuter» (3× 1W6 Inspiration) statt der
erfundenen Heldengeschichte; «Milos Küche» (1W8+3 temporäre TP nach
jeder Rast); «Nachlader» bleibt; «Großmutters Geschichten» statt «Ohr
des Sängers» (Nymeria-Legende, Kazzamir-Satz). Keine Ablenkung mehr:
Kapitel 2 leiser Weg ohne NPC-Ablenkung, dreister Weg: ein Held spielt
den Hauptmann (Trank der Verkleidung), Milo den gefangenen Koch.
Handout «Brams Lied» ersetzt durch `Story/Spieler/Handout-Milos-Kochbuch.md`
(Eintopf-Rezept mit Regel, Großmutters Brief auf der Rückseite,
Rezeptkarten als Abschiedsgeschenk in Kapitel 7). Alle Erwähnungen in
Kapiteln, Orten, Feinden, Regeln, Handouts, README, Buch-Untertitel,
Monsterbögen 06/08/09 (neu gerendert) umgestellt. Alte Dateien in
`_to_delete/NPC-Bram-der-Held/` und `_to_delete/Handout-Brams-Lied.md`.
Offen: Abnahme der Buch-Zusätze (Ring, Küche, Kräuter) und des Handouts;
Name der Stadt für Milos Laden; Großmutter hat keinen Namen (auf Zuruf).

**Nächster Schritt:** Kapitel 3 ist abgenommen (25.10.2026: keine Drachen im
Turmkampf, Drachenjagd als Szene 4 mit drei jungen roten Drachen statt Wyvern,
Champion «Bruchhand» zusätzlich auf Turm 2). Offen bleibt die Abnahme von Kapitel 2 (Greifenflug, Wachposten);
danach Kapitel 4 (die Ebene) kapitelweise durchgehen. Christoph nennt, wann
welches Kapitel dran ist.

**26.10.2026, Umbenennung:** NPC «Raik Silbersaite» heisst jetzt überall
**Bram der Held** (Ordner `NPC/Bram-der-Held/`, Handout
`Story/Spieler/Handout-Brams-Lied.md`, Genitiv «Brams»; im Fliesstext nur
«Bram»). Monsterbögen 06/08/09, Sammel-PDFs und Trankkarte 07 neu gerendert.
Das Druckpaket-ZIP enthält noch den alten Namen.

**26.10.2026, Umbenennung Land und Burg:** «Auenland» heisst jetzt
**Veldaren**, «Burg Auenstein» heisst **Burg Veldgard** (Christoph: Auenland
klang nach Herr der Ringe; gewählt aus Fantasy-Vorschlägen). Überall ersetzt:
alle Markdown-Dateien, `Orte/Burg-Veldgard.md`,
`Story/Erzaehler/06-Sturm-auf-Veldgard.md`, Karte 5
`Karten/05-Burg-Veldgard.svg/.png` (Beschriftung «Auen» → «Veldaren»),
Karte 3 und `Karten.html` (Abschnitt `#veldgard`), Schriftzug auf der gemalten
Regionskarte (Karte 4) per Bildmodell retuschiert, Monsterbögen 09 und K5
und Sammel-PDFs neu gerendert. Druckpaket-ZIP enthält noch die alten Namen.

**25.10.2026, Kleinigkeiten:** Bram auf Stufe 8 gehoben (GES 18, 51 TP, +7,
Hinterhältiger Angriff 3W6); Höllenhund-Werte geprüft und voll
eingetragen; Buch-Untertitel von «Stufe 7» auf «Stufe 8, plus Bram»
korrigiert.

**27.10.2026, Kapitel 1c:** Sechs Kampfkarten für die Echohallen (Karten 6 bis 11)
mit dem Google-Bildmodell gemalt, in `Karten/` abgelegt, Legenden in `Karten.md`
und `Karten.html`, Buch gebaut, Buchseite Version 17. `build.py` setzt in der
Offline-Fassung jetzt alle `Karten/NN-*.jpg` auf `.png` zurück.

**25.10.2026, Kapitel 1c:** Dungeon der Sturmland-Sidequest auf Ebene 1 /
Ebene 2 / Bossraum umgebaut, nur Bestien (Mantikore, Winterwölfe, Chimären,
Trolle, Schreckenstroll), Kettenteufel gestrichen; Vorschlag mit allen
Optionen liegt in `_Entwuerfe/Echohallen-zwei-Ebenen-Vorschlag.md`.

**25.10.2026, neues Projekt:** Arbeitsplan abgestimmt (Thread «Arbeitsplan
für den Oneshot festlegen»), diese Datei um Stand/Offen pro Kapitel ergänzt.
Kapitel 3 abgenommen (Champion Bruchhand auf Turm 2). Kapitel 4: die drei
grossen Ziele festgelegt (Hellfire Engine, Feuerriese, Fäulnistroll mit
Kriegspriester im Korb), alle Eigennamen der grossen Ziele gestrichen,
Feinde-Ordner umbenannt (`Hellfire-Engine`, `Feuerriese`,
`Kriegspriester-und-Faeulnistroll`).
API-Schlüssel sind im neuen Projekt noch nicht hinterlegt (Abschnitt 8).

## 5. Material im Ordner

- `Buch.html` – Kampagnenbuch zum Anklicken, läuft offline aus dem Ordner.
- `Story/` (nur noch Story-Gesamt), `NPC/`, `Feinde/`,
  `Orte/`, `Regeln/`, `Quests/`, `Belohnungen/`.
- **1.11.2026 (Buchseite Version 40, danach 42):** Erzähler-Kapitel 01–07 und
  Spieler-Handouts (Nymeria, Karte Felsenpass, Marschbefehl, Milos Kochbuch)
  auf Wunsch aus dem Buch genommen, liegen in `_to_delete/Story-Erzaehler/`
  und `_to_delete/Story-Spieler/`. Toms Tränke-Karte bleibt und steht jetzt
  unter `NPC/Druide-Tom/Handout-Toms-Traenke.md`. Quellenblock
  `besatzung-felsband` (Besatzungstabelle) ist von Kapitel 3 nach
  `Orte/Felsenpass.md` gewandert. Verweise auf `Story/Erzaehler/…` in
  Quests, Horde, Nymeria, Schlachtenleiste stehen noch als Text drin
  (laufen ins Leere).
  Zudem bei «Die Verbündeten» (Thalvien) der Punkt «Aufhänger: Späher
  haben das Sturmgebiet gesehen …» entfernt (Version 42).
  Druide Tom (Version 44): Beschreibung geleert (Platzhalter «wird neu
  geschrieben», Christoph schreibt sie neu), Stats und Fähigkeiten raus;
  alte Fassung in `_to_delete/Druide-Tom-alt/`. Unter Tom steht nur noch
  die Tränke-Karte.
  Hedda (Version 46): «Typische Sätze» und «Beziehung zu Milo» aus der
  Beschreibung raus, Unterseite Fähigkeiten raus (alt in
  `_to_delete/Hedda-alt/`); Stats bleiben. Verweise in Schlachtenleiste und
  Trupp Eisenwacht zeigen nun auf Heddas Beschreibung.
  Milo Klee (Version 46/47): Abschnitte «Was Milo NICHT tut», «Nachlader»,
  «Grossmutters Geschichten», «Grossmutters Kräuter», «Grossmutters Ring»,
  «Heilzauber» und der Satz zum Kochen im Hordenlager aus den Fähigkeiten
  raus; es bleibt nur «Milos Küche». «Christophs Charakterbogen» im Buchtext
  durch «Milos Charakterbogen» ersetzt
- **1.11.2026, NPC-Aufräumen (Buchseite Version 49):** Auf Christophs
  Wunsch alle NPC-Seiten vorsortiert: erfundene Abschnitte («Funktion in
  der Story», «Was er/sie weiss», «Typische Sätze», «Aufhänger», «Wie du
  ihn spielst», «Was X NICHT tut», Beziehungen, Zitate) entfernt, nur
  Rolle, Aussehen, Ausrüstung/Qualifikation, Stats und Belohnungen
  behalten. Komplette alte Fassung in `_to_delete/NPC-alt-2026-11-01/`.
  Mitentfernt (hingen an gestrichenen Abschnitten): Orvins Geschützkunde
  und Ordensguss, Milos Nachlader-Regel in Regeln/Geschuetze und
  Drachenjagd, Grossmutters Ring beim Feuerriesen-Wurf, Nymerias «Drei
  Fragen», «Vor dem Tor» und «Was sie NICHT tut», Pitts «Narbe (Story)»,
  Elions «Übersetzer». Quests und Story-Gesamt erwähnen Nymerias drei
  Fragen noch. Christoph schaut die NPC-Seiten noch durch.
- **1.11.2026 (Version 51): Es gibt KEINEN Sturmtrank** von Tom mehr.
  Überall entfernt (Handout, Belohnungen, Nymeria, Elion, Sturmgebiet,
  Echohallen, beide Nebenquests). Pitt stiehlt jetzt Toms Tränke
  allgemein; die Folge «Kazzamirs Bote reizt Nymeria» ist weg. Elion
  schafft den Sturmflug durch seine Zauber.
- **1.11.2026 (Version 51): NPC-Seite «Spion Pitt» gestrichen** – Pitt ist
  nur ein Bugbear-Krieger (Feinde → Kampfübersicht, Kapitel 1b). Alte
  Seite in `_to_delete/NPC-Spion-Pitt/`; Nebenquest Der Spion bleibt.
- **1.11.2026 (Version 56): Fluchtgang gekürzt** auf einen Absatz: beginnt
  im Keller, endet 600 m weiter hinter dem Dornbusch in der Senke. Aufbau,
  Verschliessen und Erzähler-Hinweis raus (alt in `_to_delete/`).
- **1.11.2026 (Version 57):** Hordenlager nur noch Überblick (erster
  Absatz: Verengung, Kessel, offener Pass); Sturmgebiet komplett geleert,
  Platzhalter «Wird später ergänzt» (Christoph füllt es neu). Alte
  Fassungen in `_to_delete/`.
- **1.11.2026 (Version 58):** Drei Bilder von Christoph zu Burg Rabenwacht
  (Aussenansicht, Grundriss Ebene 1, Grundriss Ebene 2) als
  `Karten/12–14-Burg-Rabenwacht-*.png` abgelegt und oben auf
  `Orte/Burg-Rabenwacht.md` eingebunden (nur Bildunterschriften, kein
  Text). Für die Buchseite als JPG mitpubliziert.
- **1.11.2026 (Version 59):** Drei Bilder zum Drachenhort (Ebene 1, Ebene 2,
  Bossraum – Schatzkammer) als `Karten/15–17-Drachenhort-*.png` abgelegt und
  oben auf `Orte/Drachenhort.md` eingebunden. Regionskarte
  `Karten/04-Region-Nordgar.png` durch Christophs überarbeitete Fassung
  («Vier Weiler und ein Wäldchen», 1083×1452 px) ersetzt; alte Karte in
  `_to_delete/04-Region-Nordgar-alt-2026-11-01.png`.
- **1.11.2026 (Version 60):** Christophs Battlemap «Kampf um die Türme» als
  `Karten/18-Battlemap-Kampf-um-die-Tuerme.png` abgelegt und oben auf
  `Orte/Felsenpass.md` eingebunden. Battlemap «Kellergang, erster Kampf» als
  `Karten/19-Battlemap-Kellergang.png` auf `Orte/Der-Fluchtgang.md`
  eingebunden.
- **1.11.2026 (Version 61):** Burg Rabenwacht: Abschnitte «Orte in der Burg»
  und «Erzähler-Hinweis» raus (alt in `_to_delete/`). Navigation KARTEN:
  Ordner ohne .md (`Echohallen-Varianten`, `Regionskarte-Render`) erscheinen
  nicht mehr (`build.py`); neue Seite `Karten/Drachenhort.md` mit Christophs
  drei Drachenhort-Bildern, Karten.md steht in der Gruppe zuerst. Beide
  Nebenquests (Der Spion, Die Sturmhüterin) raus, nach
  `_to_delete/Quests-Nebenquests/`; nur die Hauptquest bleibt.
  Belohnungen nur noch Toms Tränke, Orvins Schliffe (Scharf, Glutschild)
  und Feuerpfeile; Hart, Kettenbrecher, Greifenriemen, Bolzenfeder,
  Silberzahn, Hordenlager-Beute, Orden, Gold, Ehrenbürgerschaft, Milos
  Abschied, «Statt Stufe» raus (alt in `_to_delete/`). Orvins Fähigkeiten
  entsprechend angepasst.
- **1.11.2026 (Version 62):** Kartenseite: unter der Nordgar-Karte nur noch
  die Länderliste (Nordgar, Sildoras, Dhurgan, Skarn, Thalvien mit
  Anführer), Beschreibungstext der Karte raus.
- **1.11.2026 (Version 63):** Christophs Karte von Burg Veldgard ersetzt
  die SVG-Draufsicht (Karte 5): `Karten/05-Burg-Veldgard.png`, eingebunden
  oben auf `Orte/Burg-Veldgard.md` und auf der Kartenseite; Legende der
  alten Draufsicht raus. Alte SVG/PNG in `_to_delete/Karten-alt-2026-11-01/`.
- **1.11.2026 abends (Version 67):** Neun NPC-Porträts von Christoph in
  `Bilder/` (Hedda, Aurel, Brannok, Thuluk, Sarenne, Orvin, Lenja, Elion,
  Corvin Rask), auf den NPC-Seiten eingebunden (`<img class="portrait">`,
  nur Name als Bildunterschrift). build.py setzt `Bilder/*.jpg` offline auf
  .png zurück; CSS `img.portrait` im Template. Milo-Porträt seit Version 70
  (`Bilder/Milo-Klee.png`); Nymeria macht der Bilder-Thread.
- **1.11.2026 abends (Version 69): Milos Charakterbogen Version 2**
  (`_Entwuerfe/Milo-Klee-Charakterbogen-2.pdf`, zwei Seiten «Werte & Infos»
  und «Zauber & Heilung»). Aufgeteilt: Stats = Werte & Infos, Fähigkeiten =
  Glück & Ressourcen, Zauberwirken, Göttliche Macht, dazu Milos Küche.
  Hackbeil und Bratpfanne (nicht auf dem Bogen) gestrichen. (Nymeria-Legende
  und Kazzamir-Hinweis damit nicht mehr bei Milo).
- **1.11.2026 (Version 64, Thread «Buchnavigation vereinfachen»):** Unten
  in der Navigation nur noch zwei Seiten: **Monsterkarten**
  (`Monsterboegen/Monsterkarten.md`: alle 17 A4-Bögen und 5 Viertel-A4-Blätter
  als Bilder) und **Trankkarten** (`Trankkarten/Trankkarten.md`: Toms Tränke,
  Feuerpfeile, Toms Giftschrank als Bilder). `build.py` lässt `Audio`,
  `Monster-Screenshots`, `Werkzeug`, `PROJEKTSTAND.md` und alle `LIESMICH.md`
  aus dem Buch (Liste `NICHT_IM_BUCH`, Ordner-zu-Seite `EINZELSEITE`); die
  Dateien bleiben im Ordner. Für die Buchseite liegen JPG-Kopien der Bögen
  und Karten publiziert (`Monsterboegen/*.jpg`, `Trankkarten/*.jpg`,
  `Trankkarten/Gifte/*.jpg`); die Offline-`Buch.html` nimmt die PNG aus dem
  Ordner. Raster-CSS (`.bogen-grid`, `.karten-grid`) in `template.html`.
  Audio (4 Goblin-Schreie) nicht im Buch, Dateien bleiben in `Audio/`.
- `Karten/` – SVG-Skizzen (01 Burg: Gebäudezuordnung offen, 02 Schlachtfeld,
  03 Region, 05 Burg Veldgard von oben) und die gemalte, von Christoph übermalte und abgenommene
  Regionskarte `04-Region-Nordgar.png` (Grenzen nie verschieben); alte
  Fassungen in `Regionskarte-Render/`.
- `Trankkarten/` – 11 Trank- und 15 Giftkarten im Magic-Stil (Christophs
  Wahl) mit A4-Druckbögen (63 × 88 mm). `Trankkarten/Nachdruck/` (29.10.2026):
  Nachdruck-Bögen mit 3× Vitalität, 3× Grosser Heiltrank, 3× Vorzüglicher
  Heiltrank, 3× Unsichtbarkeit, 4× Verkleidung; Bögen bauen mit
  `Werkzeug/Trankkarten/bogen.py <basis> <karte.png>:<anzahl> …`.
- `Monsterboegen/` – seit 25.10.2026 **alle** Gegner: 15 A4-Bögen (01 bis 15,
  Titel = Monsterbezeichnung) und 5 Viertel-A4-Blätter K1 bis K5 mit je vier
  kleinen Karten; Sammel-PDFs; `LIESMICH.md` dort listet alles. Werkzeug:
  `Monsterboegen/Werkzeug/` (`build_alle.py`, `daten_*.py`, `render.js`,
  `gen_bilder.py`).
- `Verbuendete-Karten/` (2.11.2026, Buch V79, Navigation «Verbündete – Druckbögen»):
  Nordgar-Karte mit Infoboxen zu Hedda und den vier Hauptleuten (Name, Land,
  womit sie kämpfen, RK/TP) als A4-PDF (`01-…`), je ein A4-Bogen pro Person
  mit Porträt, Buchtext und Werten (`02` bis `06`), Sammel-PDF
  `Verbuendete-alle-A4.pdf`. Texte werden beim Bauen aus
  `NPC/Die-Verbuendeten/` und `NPC/Marschallin-Hedda/` gelesen (nichts
  doppelt gepflegt): `python3 Werkzeug/Verbuendete/bau.py <out>` dann
  `node Werkzeug/Verbuendete/render.js <out>`, Ergebnis in den Ordner kopieren.
  Lage der Boxen: Skarn oben links (Richtung im Buch nicht festgelegt), Dhurgan
  links, Sildoras unten, Thalvien rechts unten, Hedda bei Burg Rabenwacht.
- `Audio/` – vier Goblin-Schrei-MP3 (ElevenLabs; Christoph: «gar nicht so
  schlecht», später weiter).
- `Werkzeug/` – Skripte zum Nachbauen (siehe `Werkzeug/LIESMICH.md`).
- `Monster-Screenshots/` (86 PNG + Uebersicht.md) liegt seit 25.10.2026
  auch im Projektordner. `_to_delete/` (von Christoph selbst zu löschen,
  enthält seit 25.10.2026 auch den alten Kettenwächter-Ordner) und
  `_Entwuerfe/` (Vorschläge, nicht im Buch).

## 6. Offene Fragen an Christoph

Die Fragen stehen seit dem 25.10.2026 direkt beim Kapitel in Abschnitt 4
unter «Offen» und werden dort gestrichen, sobald sie geklärt sind. Hier nur die
Übersicht, welche Kapitel noch Fragen haben: 1 (Namen, Herkunft der Horde,
Milo-Abnahme, Burgskizze), 1b/5/7 (Pitt), 1c (Feuer/Säure in der Gruppe), 3 (nur
noch Monsterbögen auf Zuruf), 4 (Kessel-TP, Abnahme als Ganzes), 6
(Höllenhund-Screenshot). Vorlesetexte liefert Christoph, wenn er dazu kommt; die Stellen
stehen ebenfalls pro Kapitel.

## 7. Artefakt-Seiten (Claude)

- **Buchseite (neues Projekt, ab 25.10.2026):**
  https://claude.ai/artifact/W6QfwkKVBnUHqMzu3FBMap – bei Änderungen immer
  unter diesem Link neu publizieren (Karten als Dateien mitgeben:
  `Karten/01–03*.svg` und `04-Region-Nordgar.jpg`, verkleinerte JPG-Kopie).
- Alte Buchseite (altes Projekt): https://claude.ai/artifact/Wtvh3nm9FtCue155E41LT5
  (Stand Version 36, wird nicht mehr aktualisiert)
- Kartenseite: https://claude.ai/artifact/KPXBymW3DsKnkkYc3ANdos
- Trank- und Giftkarten: https://claude.ai/artifact/K9YHSZc7TWUxQdFLbVRi5C
- Monsterbögen: https://claude.ai/artifact/UvZq642hScqd5xqTwM5rJg
- Ideen-Doku: https://claude.ai/artifact/CFxeMHmnhDnaFyRu37ENMy

Diese Seiten gehören zum alten Projekt. In einem neuen Projekt baut man sie
mit den Skripten in `Werkzeug/` neu; `Buch.html` ersetzt die Buchseite auch
ohne Claude.

## 8. Werkzeuge und Umgebung

- **GitHub-Repo (seit 1.11.2026):**
  https://github.com/ChrisKoller35/D-D-Oneshot-F-r-Zweiten-November – Spiegel
  des ganzen Ordners «D&D Story vorgeschichte» (plus README.md und .gitignore).
  Quelle der Wahrheit bleibt der Projektordner; nach Änderungen Ordner ins Repo
  kopieren, Branch + PR, Merge auf Christophs Zuruf. Stand 2.11.2026 15:20 UTC:
  PR #2 gemergt, `main` = Projektordner (Feuerpfeile 1W6, Troll-Regel,
  Verbündete-Druckbögen, «Auf einen Blick», Seitenleiste 640 px, Buch V81).
  Laptop-Klon `C:\Users\KBZGB064908\Documents\d & d oneshot 2 november`:
  lokale, uncommittete Änderungen vom 2.11. (Template, Trankkarten.md,
  Buch.html, Beschreibung.md) sind alle in `main` enthalten → dort
  `git stash` (oder `git checkout -- .`) und `git pull origin main`.

- **Buch bauen:** `Werkzeug/Buch/build.py` – läuft seit 25.10.2026 ohne
  Pfadanpassung (Pfade relativ zum Skript); Ziel der Artifact-Fassung per
  Umgebungsvariable `BUCH_OUT`, `Buch.html` landet direkt im Ordner. Ordner
  mit `_` am Anfang (z. B. `../_Entwuerfe/`) werden nicht ins Buch genommen.
- **Monsterbögen:** `Monsterboegen/Werkzeug/build_alle.py ../Bilder <out>` und
  `node render.js <out>`; Bilder mit `gen_bilder.py`; offizielle 2024-Werte als
  JSON von `raw.githubusercontent.com` (5etools-mirror-3, `bestiary-xmm.json`,
  `bestiary-mpmm.json`), gegen die Screenshots geprüft.
- **Trank-/Giftkarten:** `Werkzeug/Trankkarten/` (gen.py/gen2.py für Bilder,
  render_mtg.py/render_gift.py + shot.js für PNG).
- **Regionskarte (Rezept):** Google-Bildmodell per REST `generateContent`
  (Header `x-goog-api-key`), Bild 1 = Christophs Karte mit weissem Rand
  (verhindert Beschnitt), Bilder 2+3 = Stilreferenzen, `responseModalities`
  IMAGE, Seitenverhältnis 3:4, 2K. Prompt: «GEOMETRY IS LOCKED», Flächen pro
  Farbe beschreiben, Beschriftung Nordgar/Dunmar/Rabenwacht/Veldgard.
  Text-Edits mit `gemini-3.1-flash-image`, danach nur den geänderten Bereich
  per Maske ins Original einsetzen.
- **Wichtig für Claude-Projekte:** Threads, die mit dem PC verbunden sind,
  erreichen `generativelanguage.googleapis.com` **nicht**. Bilder nur in
  Threads ohne PC-Verbindung rendern, PC-Kopie dann durch einen verbundenen
  Thread. Auch `cdnjs` und PyPI-CDN sind gesperrt; `npm pack` funktioniert.
- **API-Keys:** `GOOGLE_API_KEY` und `ELEVENLABS_API_KEY` sind seit dem
  25.10.2026 (abends) auch im neuen Projekt in der Umgebung gesetzt
  (Projekteinstellungen → Umgebung); Bilder und Audio gehen wieder. ElevenLabs: nur
  Text-to-Speech (eleven_v3), kein Sound-Effects-Recht (unter API-Keys
  einschaltbar). Keine Schlüssel in Dateien schreiben.
- **PC-Kopie:** `C:\Users\chris\Documents\D-D-Story\Oneshot-Die-letzte-Grosstat\`;
  Projektordner und PC waren am 25.10.2026 identisch (Prüfsummen).
