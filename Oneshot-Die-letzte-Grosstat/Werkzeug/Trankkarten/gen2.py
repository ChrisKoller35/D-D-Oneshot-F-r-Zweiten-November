import os, sys, json, base64, urllib.request
model, out, desc = sys.argv[1:4]
style = ("Painted fantasy trading-card illustration, landscape format. A single poison vial as the hero subject, centered, "
 "standing on a dark shelf inside a druid's locked poison cabinet in a cold northern stone castle. "
 "Dark ominous background, a single candle, cobwebs, dried poisonous plants like nightshade, hemlock and foxglove, small skulls, faint frost. "
 "Rich detailed digital painting, eerie glow, rim light, high contrast, no text, no letters, no labels, no border, no frame. "
 "The poison: ")
body = {"contents":[{"parts":[{"text": style + desc}]}],
        "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:3","imageSize":"1K"}}}
req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
    data=json.dumps(body).encode(), headers={"Content-Type":"application/json","x-goog-api-key":os.environ["GOOGLE_API_KEY"]})
r = json.load(urllib.request.urlopen(req, timeout=300))
for p in r["candidates"][0]["content"]["parts"]:
    if "inlineData" in p:
        open(out,"wb").write(base64.b64decode(p["inlineData"]["data"])); print("ok", out); break
else: print(json.dumps(r)[:500])
