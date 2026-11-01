import os, sys, json, base64, urllib.request
model, out = sys.argv[1:3]
desc = ("Painted fantasy trading-card illustration, landscape format. A bundle of twelve arrows as the hero subject, centered, "
 "lying on the dark iron anvil of a dwarven blacksmith's forge in a cold northern stone castle. The arrowheads glow red-hot with "
 "a faint ember rune carved into each one, thin wisps of flame and sparks rising from the tips, fletching of dark red feathers, "
 "a leather quiver beside them. Dark moody background with forge fire glow, hammer and tongs, soot and sparks. "
 "Rich detailed digital painting, rim light, high contrast, no text, no letters, no labels, no border, no frame.")
body = {"contents":[{"parts":[{"text": desc}]}],
        "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:3","imageSize":"1K"}}}
req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
    data=json.dumps(body).encode(), headers={"Content-Type":"application/json","x-goog-api-key":os.environ["GOOGLE_API_KEY"]})
r = json.load(urllib.request.urlopen(req, timeout=300))
for p in r["candidates"][0]["content"]["parts"]:
    if "inlineData" in p:
        open(out,"wb").write(base64.b64decode(p["inlineData"]["data"])); print("ok", out); break
else: print(json.dumps(r)[:500])
