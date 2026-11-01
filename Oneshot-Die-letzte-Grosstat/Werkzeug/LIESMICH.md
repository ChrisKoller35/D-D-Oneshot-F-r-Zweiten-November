# Werkzeug

Skripte, mit denen die generierten Teile des Buchs nachgebaut werden.
Alles läuft in einer Claude-Umgebung (Python 3, Node mit Playwright);
Pfade in den Skripten zeigen auf `/mnt/project-files/Oneshot-Die-letzte-Grosstat/`
bzw. ein Scratchpad und müssen in einem neuen Projekt angepasst werden.

- `Buch/build.py` + `template.html` + `marked.min.js` – baut aus allen
  Markdown-Dateien die klickbare Buchseite (`Die-letzte-Grosstat.html`, für
  das Claude-Artifact) und die Offline-Fassung `Buch.html` im Ordner. Nach
  jeder Textänderung neu laufen lassen; danach Artifact unter derselben URL
  neu publizieren und `Buch.html` auf den PC kopieren.
- `Trankkarten/` – Trank- und Giftkarten im Magic-Stil: `gen.py`/`gen2.py`
  holen Bilder vom Google-Bildmodell (braucht `GOOGLE_API_KEY`), `render_mtg.py`
  und `render_gift.py` setzen die Karten als HTML und `shot.js` fotografiert sie
  mit Playwright zu PNG; `data.json`/`gifte.json` sind die Kartentexte.
- `../Monsterboegen/Werkzeug/` – A4-Monsterbögen (`build.py Bilder <out>`,
  `node render.js <out>`).
- Regionskarte: Rezept in `PROJEKTSTAND.md`, Abschnitt Werkzeuge.
