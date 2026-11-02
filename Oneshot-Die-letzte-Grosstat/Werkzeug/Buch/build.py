import os, json, re, tempfile
# Pfade relativ zum Skript (Werkzeug/Buch/ liegt im Oneshot-Ordner), seit 25.10.2026 ohne Anpassen lauffaehig.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..')) + '/'
# Artifact-Fassung: Zielpfad per Umgebungsvariable BUCH_OUT, sonst Temp-Ordner
OUT = os.environ.get('BUCH_OUT') or os.path.join(tempfile.gettempdir(), 'Die-letzte-Grosstat.html')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def nice(name):
    name = re.sub(r'\.md$', '', name)
    name = re.sub(r'^\d\d[a-z]?-', '', name)
    rep = {'ae':'ä','oe':'ö','ue':'ü','Ae':'Ä','Oe':'Ö','Ue':'Ü'}
    # careful replacement only for known names
    fixes = {
      'Erzaehler':'Erzähler','Faehigkeiten':'Fähigkeiten','Ultimative-Faehigkeiten':'Ultimative Fähigkeiten',
      'Die-letzte-Grosstat':'Die letzte Großtat','Tuermen':'Türmen','Geschuetztuerme':'Geschütztürme',
      'Sturmhueterin':'Sturmhüterin','Kettenfuerstin':'Kettenfürstin','Traenke':'Tränke','Uebersicht':'Übersicht',
      'Geschuetze':'Geschütze','Hauptquest-Die-letzte-Grosstat':'Hauptquest: Die letzte Großtat',
      'Oneshot-Die-letzte-Grosstat':'Die letzte Großtat','Chimaere':'Chimäre',
      'Gehoernte':'Gehörnte','Kettenwaechter':'Kettenwächter','Winterwoelfe':'Winterwölfe','Verbuendete-Karten':'Verbündete – Druckbögen','Verbuendete':'Verbündete'
    }
    for k,v in fixes.items(): name = name.replace(k, v)
    return name.replace('-', ' ')

def pid(rel):
    return re.sub(r'[^a-z0-9]+','-', rel.lower().replace('.md','')).strip('-')

# Order
order_top = ['README.md','Story','NPC','Feinde','Orte','Karten','Regeln','Quests','Belohnungen','Monsterboegen','Trankkarten','Verbuendete-Karten']
pages = {}   # id -> {title, path, html}
tree = []    # nested nav

# Nicht ins Buch (seit 1.11.2026, Thread «Buchnavigation vereinfachen»): interne Ordner und Arbeitsdateien.
# Die Dateien bleiben im Ordner, sie erscheinen nur nicht in der Navigation.
NICHT_IM_BUCH = {'Audio', 'Monster-Screenshots', 'Werkzeug', 'Sessions', 'PROJEKTSTAND.md', 'LIESMICH.md', 'README.md'}
# Ordner, die im Buch nur als eine Seite erscheinen (Karten liegen als Bilder im Ordner)
EINZELSEITE = {'Monsterboegen/': 'Monsterboegen/Monsterkarten.md', 'Trankkarten/': 'Trankkarten/Trankkarten.md', 'Verbuendete-Karten/': 'Verbuendete-Karten/Verbuendete-Karten.md'}

def walk(dirrel):
    entries = sorted(os.listdir(ROOT+dirrel))
    items = []
    if dirrel in EINZELSEITE:
        rel = EINZELSEITE[dirrel]
        return [{'type':'page','id':pid(rel),'title':nice(os.path.basename(rel)),'path':rel}]
    files = [e for e in entries if e.endswith('.md') and (e not in NICHT_IM_BUCH or (dirrel=='' and e=='README.md'))]
    dirs = [e for e in entries if os.path.isdir(ROOT+dirrel+e) and e not in NICHT_IM_BUCH and not e.startswith('_')]
    for f in files:
        rel = dirrel+f
        items.append({'type':'page','id':pid(rel),'title':nice(f),'path':rel})
    for d in dirs:
        ch = walk(dirrel+d+'/')
        if not ch: continue   # Ordner ohne .md (nur Bilder) nicht in die Navigation
        items.append({'type':'group','title':nice(d),'path':dirrel+d+'/','children':ch})
    # Karten.md zuerst, dann die uebrigen Kartenseiten
    if dirrel == 'Karten/':
        items.sort(key=lambda it: 0 if it.get('path')=='Karten/Karten.md' else 1)
    return items

def collect(items):
    for it in items:
        if it['type']=='page':
            md = open(ROOT+it['path'], encoding='utf-8').read()
            pages[it['id']] = {'title':it['title'],'path':it['path'],'md':md}
        else: collect(it['children'])

# top level with custom order
top = walk('')
def key(it):
    name = it['path'].rstrip('/').split('/')[-1]
    return order_top.index(name) if name in order_top else 99
top.sort(key=key)
# Monsterkarten und Trankkarten stehen als einzelne Seiten in der Navigation, nicht als Ordner
top = [it['children'][0] if it['type']=='group' and it['path'] in EINZELSEITE else it for it in top]
# Story: order Story-Gesamt, Erzaehler, Spieler
for it in top:
    if it['type']=='group' and it['path']=='Story/':
        it['children'].sort(key=lambda c: 0 if c['type']=='page' else (1 if 'Erzaehler' in c['path'] else 2))
collect(top)
# README title
pages['readme']['title'] = 'Überblick'
for it in top:
    if it['type']=='page' and it['path']=='README.md': it['title']='Überblick'

# map paths -> ids for link resolution
path2id = {p['path']:i for i,p in pages.items()}
dir2id = {}
for i,p in pages.items():
    d = os.path.dirname(p['path'])+'/'
    if p['path'].endswith('Beschreibung.md'): dir2id[d]=i
    if p['path'].endswith('Story-Gesamt.md'): dir2id['Story/']=i
# Seit 1.11.2026 gibt es unter Feinde/ nur noch die Kampfuebersicht; alte Verweise auf Feinde/<Ordner>/ landen dort.
FEINDE_ID = path2id.get('Feinde/Uebersicht.md')
if FEINDE_ID: pages[FEINDE_ID]['title'] = 'Kampfübersicht'
for i,p in pages.items():
    d = os.path.dirname(p['path'])+'/'
    if d not in dir2id: dir2id[d]=i

# ---------------------------------------------------------------------------
# Eine Quelle pro Fakt (seit 31.10.2026):
# In einer Quelldatei steht ein benannter Block zwischen
#     <!-- quelle: NAME -->   ...   <!-- /quelle -->
# Andere Seiten holen ihn mit einer eigenen Zeile
#     <!-- einbinden: NAME -->
# ins Buch. Die Markdown-Datei selbst enthaelt dann nur den Verweis; der
# Text wird beim Bauen eingesetzt, mit einem Hinweis auf die Quelle.
# Geaendert wird so ein Fakt nur in der Quelldatei.
# ---------------------------------------------------------------------------
BLOCK_RE = re.compile(r'<!--\s*quelle:\s*([A-Za-z0-9_\-]+)\s*-->\n?(.*?)<!--\s*/quelle\s*-->\n?', re.S)
INCL_RE  = re.compile(r'^[ \t]*<!--\s*einbinden:\s*([A-Za-z0-9_\-]+)\s*-->[ \t]*$', re.M)
blocks = {}   # name -> (text, page id)
for i,p in pages.items():
    for m in BLOCK_RE.finditer(p['md']):
        if m.group(1) in blocks:
            raise SystemExit('Quelle doppelt definiert: %s (%s und %s)' % (m.group(1), pages[blocks[m.group(1)][1]]['path'], p['path']))
        blocks[m.group(1)] = (m.group(2).strip('\n'), i)
    # Marker in der Quellseite selbst entfernen, Text bleibt stehen
    p['md'] = BLOCK_RE.sub(lambda m: m.group(2), p['md'])
for i,p in pages.items():
    def sub_incl(m):
        name = m.group(1)
        if name not in blocks:
            print('WARNUNG: Einbindung ohne Quelle:', name, 'in', p['path'])
            return '> **Fehlt:** Quelle `%s` nicht gefunden.' % name
        text, src = blocks[name]
        if src == i: return text
        return text + '\n\n*Quelle: [%s](#%s) – Änderungen nur dort.*' % (pages[src]['title'], src)
    p['md'] = INCL_RE.sub(sub_incl, p['md'])

p_cur=None
def resolve(ref, frompath):
    ref = ref.strip()
    if ref.startswith('../') or ref.startswith('./'):
        base = os.path.dirname(frompath)
        ref = os.path.normpath(os.path.join(base, ref)).replace('\\','/')
        if not ref.endswith('.md') and not ref.endswith('/'): ref += '/'
    if ref in path2id: return path2id[ref]
    if ref in dir2id: return dir2id[ref]
    # relative sibling file like Stats/Stats.md from NPC/X/Beschreibung.md
    base = os.path.dirname(frompath)
    cand = os.path.normpath(os.path.join(base, ref)).replace('\\','/')
    if cand in path2id: return path2id[cand]
    if cand+'/' in dir2id: return dir2id[cand+'/']
    # bare filename: search within the same NPC/Feind folder
    top2 = '/'.join(p_cur['path'].split('/')[:2])+'/'
    for pp,ii in path2id.items():
        if pp.startswith(top2) and pp.endswith('/'+ref): return ii
    if ref.startswith('Feinde/') and FEINDE_ID: return FEINDE_ID
    return None

for i,p in pages.items():
    p_cur = p
    md = p['md']
    def sub_code(m):
        tid = resolve(m.group(1), p['path'])
        if tid: return '[%s](#%s)' % (pages[tid]['title'], tid)
        return m.group(0)
    md = re.sub(r'`((?:\.\./|\./)?(?:[A-Za-z0-9\-]+/)*[A-Za-z0-9\-]+(?:\.md|/))`', sub_code, md)
    def sub_link(m):
        tid = resolve(m.group(2), p['path'])
        if tid: return '[%s](#%s)' % (m.group(1), tid)
        return m.group(0)
    md = re.sub(r'\[([^\]]+)\]\(((?!#|http)[^)]+)\)', sub_link, md)
    if p['path'].startswith('Karten/'):
        md = re.sub(r'(## [^\n]*\(`([^`]+\.(?:svg|png|jpg))`\))', lambda m: m.group(1)+'\n\n<img class="map" src="Karten/'+m.group(2).replace('.png','.jpg')+'" alt="'+m.group(2)+'">', md)
    p['md'] = md

data = {'tree':top, 'pages':pages}
tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
html = tpl.replace('/*__DATA__*/', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
open(OUT,'w',encoding='utf-8').write(html)

# Offline-Fassung fuer den Ordner (kein CDN, keine Webfonts, PNG statt JPG)
_marked = open(os.path.join(HERE, 'marked.min.js'), encoding='utf-8').read()
off = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>', '<script>'+_marked+'</script>')  # marked.min.js enthaelt kein </script
off = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n?', '', off)
off = re.sub(r'((?:Karten/\d\d|Monsterboegen/(?:\d\d|K\d)|Trankkarten/(?:\d\d|Gifte/G\d\d)|Verbuendete-Karten/\d\d)-[A-Za-z0-9\-]+)\.jpg', r'\1.png', off)
off = re.sub(r'(Bilder/[A-Za-z0-9\-]+)\.jpg', r'\1.png', off)   # NPC-Portraets
off = off.replace('<title>Die letzte Großtat</title>', '<title>Die letzte Großtat</title>\n<!-- Offline-Fassung des Kampagnenbuchs: liegt im Ordner Oneshot-Die-letzte-Grosstat, Karten relativ aus Karten/. Erzeugt von build.py; nach jeder Textaenderung neu bauen. -->')
assert '<script src="https://cdnjs' not in off and 'fonts.googleapis.com/css2' not in off
open(ROOT+'Buch.html','w',encoding='utf-8').write(off)
print('offline', len(off)//1024, 'KB')
print(len(pages), 'pages', len(html)//1024, 'KB')
