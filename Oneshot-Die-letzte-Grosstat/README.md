# Oneshot: Die letzte Großtat

Ein eigenständiger Oneshot: eine Schlacht um ein Land, in einem
Abend oder zwei. Keine Verbindung zu anderen Kampagnen – die Helden
können danach überallhin.

> Hinweis: Ordner- und Dateinamen verwenden `ae/oe/ue` statt Umlauten
> In den Texten stehen normale
> Umlaute.

**Rahmen:** 3 Helden, Stufe 8, mit starker Ausrüstung (je ein
seltener und zwei ungewöhnliche magische Gegenstände), plus der
NPC-Gefährte **Milo Klee** (Bauer, Koch und Heiler mit wenigen Zaubern, Stufe 8) (→ `NPC/Milo-Klee/`). Spielzeit: ein langer Abend
(5–6 Stunden) oder zwei normale Abende. Kürzungs-Tipps stehen in
`Story/Story-Gesamt.md`, Abschnitt „Spielzeit".

**Alle Gegner stammen aus dem Monsterhandbuch (2024) und aus Monsters
of the Multiverse.** Nichts ist erfunden – nur Namen und die
Begegnungen drumherum. Der **Anführer der Horde** ist **Kazzamir, der
Gehörnte**, ein Gehörnter Teufel (HG 11).

## Die Story in einem Satz

Nach Monaten Krieg wendet sich das Blatt in Nordgar, einem Land
im hohen Norden: Die Horde, die sich bis vor die Hauptstadt gebrannt
hatte, ist bis an den Felsenpass zurückgedrängt, und
die Helden werden zur Speerspitze des Gegenangriffs: Sie nehmen die
Geschütztürme im Felsenpass, schießen die Drachen der Horde vom
Himmel, entscheiden die Feldschlacht, rasten im verlassenen
Hordenlager hinter der Verengung und brechen am nächsten Tag in die Burg Veldgard
ein, wo der Anführer der Horde, ein Gehörnter Teufel, in der großen Halle auf sie wartet.

→ Vollständige Story: [Story/Story-Gesamt.md](Story/Story-Gesamt.md)

## Ordnerstruktur

- **Buch.html** – Das ganze Kampagnenbuch als eine Seite zum Anklicken, läuft
  ohne Internet direkt aus diesem Ordner (Karten aus `Karten/`). Wird bei
  jeder Textänderung neu erzeugt; die Markdown-Dateien bleiben die Quelle.
- **Story/** – Die Geschichte
  - `Story-Gesamt.md` – Die komplette Story in Reihenfolge mit Verweisen
  - Erzähler-Kapitel und Spieler-Handouts sind seit 1.11.2026 aus dem Buch genommen (liegen in `_to_delete/`); Toms Tränke-Karte steht bei Druide Tom
- **NPC/** – Verbündete, pro NPC ein Ordner mit **Stats/** und **Faehigkeiten/**
  - Milo Klee (der NPC-Gefährte), Druide Tom, Schmied Orvin, Marschallin
    Hedda, Rittmeisterin Lenja (Greifen), Sturmmagier Elion (der Bote),
    Silberdrachin Nymeria, Soldaten und Trupp Eisenwacht
    (Hauptmann Corvin Rask, Meuchler, Soldaten für die Feiern)
- **Feinde/** – seit 1.11.2026 nur noch **eine Seite**: `Feinde/Uebersicht.md`,
  die Kampfübersicht (Kampf für Kampf: welche Monster, wie viele, HG, RK, TP,
  dazu die Kurzregel, wie das Ziel fällt). Werte gelten nach den
  Statblock-Bildern in `Monster-Screenshots/`; gedruckte Bögen in `Monsterboegen/`.
  Die alten Einzelseiten (Horde, Kazzamir, große Ziele, Drachen, Nadel,
  Drachenhort-Bestien) liegen in `_to_delete/Feinde-alt-2026-11-01/`
- **Orte/** – Burg Rabenwacht, Felsenpass, Sturmgebiet, Hordenlager, Burg Veldgard, Der Fluchtgang (1b), Der Drachenhort (1c)
- **Karten/** – Skizzen (Burg Rabenwacht, Schlachtfeld, Region) als SVG und Karten.html
- **Regeln/** – Geschütze und Drachenjagd (eine Seite)
- **Quests/** – Hauptquest
- **Belohnungen/** – Tränke, Schliffe, Belohnungen nach dem Sieg
- **Trankkarten/** – Druckbare Karten zu Toms Tränken und Giften (PNG je Karte, Druckbögen A4; Gifte im Unterordner Gifte/)
- **Sessions/** – Protokoll des Spielabends

## Ablauf

1. **Kriegsrat und Siegesfeier** (Rabenwacht: Aufräumen, Heddas Verhör, Gespräch im Hof, Besprechungsbüro, Feier)
   - optional **1b: Der Tunnel des Spions** (Verfolgung, Hinterhalt, Tränke zurück)
   - optional **1c: Die gekettete Drachin** (Nymeria in Ketten, Dungeon Drachenhort, Schwert Silberzahn; überspringt Kapitel 2–4)
2. **Der Weg zu den Türmen** (Greifen, dann leise oder dreist)
3. **Die Geschütztürme** (Ballisten, Drachenjagd)
4. **Die Schlacht auf der Ebene** (Feuerbälle, drei große Ziele)
5. **Das Hordenlager** (Verengung, Rast, Siegestrunk)
6. **Sturm auf Veldgard** (die große Halle, Kazzamir der Gehörnte)
7. **Nach der Schlacht** (Preis, Totenfeuer, Milos Abschied)

## Geografie

Nordgar liegt im hohen Norden. Seine Hauptstadt **Dunmar**
liegt ganz im Süden des Landes; bis vor ihre Tore kam die Horde, bevor
sie zurückgedrängt wurde. Was südlich von Nordgar liegt, bleibt
offen – die Stadt für Milos Laden hat noch keinen Namen.

**Der Felsenpass** (Karten → `Karten/Karten.md`): Burg Rabenwacht steht
im offenen Land, ein Stück vor den Bergen, nicht am Eingang des Passes.
Der Pass beginnt mit der breiten Ebene (Kapitel 4), verengt sich an
einem Felsvorsprung (Verengung), dahinter liegt links der Kessel mit dem
Hordenlager (Kapitel 5), und rechts läuft die Schlucht offen aus – kein
Tor, keine Schleuse. Am offenen Ende, wo das Land wieder grün wird
(Wiesen, Flussauen), steht Burg Veldgard (Kapitel 6).

## Noch offen / zum Anpassen

- Die Türme heißen schlicht «Turm 1 rechts» (unten) und «Turm 2 rechts» (oben); die linken nimmt die Eisenwacht unter Hauptmann Corvin Rask. Die Namen der Burgen und NPCs sind Vorschläge.
