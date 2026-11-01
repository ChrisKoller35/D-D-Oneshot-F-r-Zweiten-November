import os, sys, json, base64, urllib.request
model = sys.argv[1]; out = sys.argv[2]; desc = sys.argv[3]
style = ("Painted fantasy trading-card illustration, landscape format. A single potion bottle as the hero subject, centered, "
 "standing on a rough wooden table of an old druid's herb workshop in a cold northern stone castle. "
 "Dark moody background with soft candlelight, dried herbs, moss and roots hanging, faint frost on the stone. "
 "Rich detailed digital painting, glowing liquid, rim light, high contrast, no text, no letters, no labels, no border, no frame. "
 "The potion: ")
body = {"contents":[{"parts":[{"text": style + desc}]}],
        "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:3","imageSize":"1K"}}}
req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
    data=json.dumps(body).encode(), headers={"Content-Type":"application/json","x-goog-api-key":os.environ["GOOGLE_API_KEY"]})
r = json.load(urllib.request.urlopen(req, timeout=300))
for p in r["candidates"][0]["content"]["parts"]:
    if "inlineData" in p:
        open(out,"wb").write(base64.b64decode(p["inlineData"]["data"])); print("ok", out); break
else: print(json.dumps(r)[:500])
