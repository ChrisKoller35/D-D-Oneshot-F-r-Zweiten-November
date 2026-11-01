# Monsterbögen und Monsterkarten

Alle Gegner des Oneshots als Druckbögen, Stand 25.10.2026. (Hinweis 31.10.2026: Im Buch heißen Champion und Hobgoblin-Verwüster nicht mehr Bruchhand und Vask; der Verwüster steht jetzt auf Turm 1 rechts, der Champion bleibt auf Turm 2 rechts; der Bugbear-Pirscher kommt nur noch bei Nadel in Kapitel 1b vor. Die gedruckten Bögen tragen noch die alten Untertitel.) Titel ist immer die Monsterbezeichnung; der Name aus dem Buch (Nadel, Pitt, Bruchhand, Rotzahn, Vask, Kazzamir) steht klein im Untertitel. Werte: Monsterhandbuch 2024 (SRD 5.2) und Monsters of the Multiverse, geprüft gegen die Screenshot-Sammlung; Würfelformel direkt neben jedem Fähigkeitsnamen. Seit 1.11.2026 stehen keine Infokästen mehr auf den Bögen und keine «im Buch: …»-Hinweise in Untertiteln; die Texte liegen weiterhin in `daten_a4.py`/`daten_klein.py`, `build_alle.py` lässt sie beim Bauen weg.

## A4, ein Monster pro Blatt (`01` bis `17`)

01 Uralter Silberdrache (Argentys) · 02 Höllenfeuer-Maschine · 03 Assassine · 04 Bugbear-Krieger · 05 Bugbear-Pirscher · 06 Feuerriese · 07 Fäulnistroll · 08 Kriegspriester · 09 Gehörnter Teufel · 10 Schreckenstroll · 11 Champion · 12 Gifttroll · 13 Chimäre · 14 Wyvern · 15 Hobgoblin-Verwüster · 16 Ausgewachsener Silberdrache · 17 Junger Silberdrache (16 und 17 seit 1.11.2026: spontane Optionen, bewusst ohne Bild und ohne Infokästen)

## Viertel-A4, vier Karten pro Blatt (`K1` bis `K5`, je 105 × 148 mm, Schnittlinien gestrichelt)

- K1: Goblin-Minion, Goblin-Krieger, Goblin-Boss, Hobgoblin-Krieger
- K2: Hobgoblin-Hauptmann, Hobgoblin-Eisenschatten, Ork, Berserker
- K3: Wolf, Worg, Winterwolf, Mantikor
- K4: Oger-Kettenschläger, Oger-Bolzenschleuder, Bogenschütze, Troll
- K5: Bugbear-Krieger, Bugbear-Pirscher, Höllenhund, Greif (Verbündeter)

## Sammel-PDFs

`Monsterboegen-A4-alle.pdf` (01 bis 17), `Monsterkarten-klein-alle.pdf` (K1 bis K5), `Monsterboegen-und-Karten-alle.pdf` (alles). PNG = Vorschau. `Bilder/` = Illustrationen (Google-Bildmodell), `Bilder/Varianten/` = Alternativen.

## Nachbauen (`Werkzeug/`)

`python3 build_alle.py ../Bilder <out>` baut alle HTML-Seiten (Daten in `daten_a4.py` und `daten_klein.py`), `node render.js <out>` macht daraus PDF und PNG und meldet Überlauf. Neue Bilder: `python3 gen_bilder.py <bildordner> [key ...]` (braucht `GOOGLE_API_KEY`). Alte Fassungen (Bogen «Grollhorn», «Nadel») liegen in `_to_delete/Monsterboegen-alt/`.
