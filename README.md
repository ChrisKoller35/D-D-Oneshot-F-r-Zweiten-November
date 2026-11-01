# D&D Story Vorgeschichte – Oneshot «Die letzte Grosstat»

Vollständiger Projektstand des Oneshots: Buch (Markdown-Quellen und `Buch.html`), Karten, Monsterbögen, Trankkarten, Monster-Screenshots, Audio und Entwürfe.

## Ordner

- `Oneshot-Die-letzte-Grosstat/` – das eigentliche Projekt. Einstieg: `PROJEKTSTAND.md` (Arbeitsregeln, Entscheidungen, Stand pro Kapitel).
- `Druckpaket/` – älteres Druckpaket als ZIP (veraltet, nur zur Sicherheit behalten).
- `Monster Beschreibung Buch/` – Fotos aus dem Monsterhandbuch.
- `_Entwuerfe/` und `_to_delete/` – Entwürfe und aussortierte Inhalte. Nichts davon löschen, nur verschieben.

## Auf einen anderen PC holen

1. Git installieren: https://git-scm.com/downloads
2. Im gewünschten Ordner eine Eingabeaufforderung öffnen und ausführen:

```
git clone https://github.com/ChrisKoller35/D-D-Oneshot-F-r-Zweiten-November.git
```

3. Später den neusten Stand holen:

```
git pull
```

## Buch bauen

Im Ordner `Oneshot-Die-letzte-Grosstat/`:

```
python Werkzeug/Buch/build.py
```

Das erzeugt `Buch.html` neu aus den Markdown-Quellen.
