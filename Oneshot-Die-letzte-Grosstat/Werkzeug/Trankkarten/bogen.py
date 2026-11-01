# Druckbogen A4 (300 dpi), 3x3 Karten 63x88 mm, Karten stossen aneinander, Schnittmarken an den Ecken.
# Aufruf: python3 bogen.py <ausgabe-basis> <karte.png>:<anzahl> [...]
import sys, os
from PIL import Image, ImageDraw
W,H=2480,3508; CW,CH=744,1039; X0=(W-3*CW)//2; Y0=(H-3*CH)//2
base=sys.argv[1]; cards=[]
for a in sys.argv[2:]:
    p,n=a.rsplit(":",1); cards+= [p]*int(n)
pages=[]
for i in range(0,len(cards),9):
    pg=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(pg)
    for k,p in enumerate(cards[i:i+9]):
        im=Image.open(p).convert("RGBA").resize((CW,CH),Image.LANCZOS)
        x=X0+(k%3)*CW; y=Y0+(k//3)*CH; pg.paste(im,(x,y),im)
    for r in range(4):
        for c in range(4):
            x=X0+c*CW; y=Y0+r*CH
            d.line([(x-40,y),(x-10,y)],fill="black",width=2); d.line([(x+10,y),(x+40,y)],fill="black",width=2)
            d.line([(x,y-40),(x,y-10)],fill="black",width=2); d.line([(x,y+10),(x,y+40)],fill="black",width=2)
    pages.append(pg)
for i,pg in enumerate(pages,1): pg.save(f"{base}-Seite-{i}.png",dpi=(300,300))
pages[0].save(f"{base}.pdf",save_all=True,append_images=pages[1:],resolution=300)
print(len(pages),"Seiten,",len(cards),"Karten")
