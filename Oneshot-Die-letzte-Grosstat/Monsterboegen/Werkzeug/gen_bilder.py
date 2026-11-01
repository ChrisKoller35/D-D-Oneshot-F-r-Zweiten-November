# Erzeugt Illustrationen für die Monsterbögen mit dem Google-Bildmodell.
# Aufruf: python3 gen_bilder.py <ausgabeordner> [nur-diese-keys...]   (braucht GOOGLE_API_KEY)
import os, sys, json, base64, time, urllib.request
OUT = sys.argv[1]; only = set(sys.argv[2:])
KEY = os.environ["GOOGLE_API_KEY"]
MODEL = "gemini-3.1-flash-image"
STYLE = ("Painterly dark fantasy illustration, oil-painting texture, dramatic torchlight and cold northern daylight, "
         "muted earthy palette with warm highlights, detailed, in the style of a tabletop roleplaying monster manual. "
         "No text, no letters, no watermark, no frame, no border.")
BIG = {
 "feuerriese": "A towering fire giant warlord, 18 feet tall, coal-black skin and flaming orange hair, wearing crude plate armor riveted together from plundered human breastplates, swinging a huge glowing millstone on a chain that drips molten sparks, striding across a trampled snowy battlefield before a horde of orcs and goblins, burning siege banners behind him",
 "faeulnistroll": "A huge rot troll, grey-green decaying flesh hanging in strips, black necrotic ooze dripping, bones showing, carrying on its back a tall war banner of black iron chains on a red cloth, with an iron basket strapped between its shoulders in which a hobgoblin priest in plate armor stands, marching through a goblin horde on a snowy plain",
 "kriegspriester": "A hobgoblin war priest in blackened plate armor with glowing chain symbols, holding a heavy iron maul wreathed in holy fire, standing in an iron basket on the back of a rotting troll, preaching with one hand raised, radiant light and dark smoke, chaotic battlefield below",
 "teufel": "A horned devil, large and muscular, red-black skin, great curved horns, leathery wings spread, holding a long glowing iron fork, whip-like barbed tail, seated on a throne of chains in a dark stone castle hall hung with torn war banners, two hell hounds at its feet, infernal fire",
 "schreckenstroll": "A gigantic dire troll, 20 feet tall, mottled grey-green hide, many extra clawed arms growing from its torso, gaping maw with tusks, hunched inside a vast echoing cave chamber lined with mirror-like ice crystals, cold blue light, bones littering the floor",
 "champion": "A hobgoblin champion in black plate armor with a chain emblem on a red tabard, greatsword resting over one shoulder, standing at the top of a stone stair on a fortified ballista platform in a mountain pass, snow and wind, glowering down at the viewer",
 "gifttroll": "A venom troll, large and gaunt, sickly yellow-green hide weeping poison from open sores, long claws, crouched in a dark deep cave hall lit by green glowing fungus, toxic mist curling around its feet, two ordinary trolls looming in the dark behind it",
 "chimaere": "A chimera with a lion's head, a goat's head and a red dragon's head, bat-like wings, guarding a nest of large mottled eggs inside a windswept cave chamber high in the storm mountains, lightning flickering outside the cave mouth, breath of fire",
 "wyvern": "A grey rock wyvern, large dragon-like beast with two legs and bat wings and a long barbed poison stinger tail, chained by an iron collar in a war camp in a rocky canyon, straining against the chain and roaring, goblin handlers cowering, storm clouds",
 "verwuester": "A hobgoblin war mage in studded leather with a tall wooden staff crackling with blue arcane force bolts, standing on a wooden observation platform above a mountain pass fortification, fog cloud rolling below, fireball blooming in the distance, red chain scar on his forearm",
}
SMALL = {
 "goblin-minion": "A scrawny goblin with a rusty dagger and ragged furs, scrambling over snowy rocks with dozens of other goblins behind, northern battlefield",
 "goblin-krieger": "A goblin warrior in leather armor with a small round shield, scimitar and shortbow, grinning, crouched on a rocky ridge in a mountain pass",
 "goblin-boss": "A goblin boss in a chain shirt with a shield and scimitar, blowing a large curved war horn, standing on a wooden barricade on a mountain ramp, goblins behind him",
 "hobgoblin-krieger": "A disciplined hobgoblin soldier in half plate armor with a tall shield, longsword and longbow, standing in a shield wall line, red skin, orange eyes, snowy plain",
 "hobgoblin-hauptmann": "A hobgoblin captain in ornate half plate armor with a greatsword raised, commanding a line of hobgoblin soldiers, a chain scar on his neck, battlefield dust",
 "eisenschatten": "A hobgoblin monk assassin in dark wrappings and no armor, leaping out of shadow between barrels and crates, throwing darts, blurred shadow-teleport effect",
 "ork": "A brutal orc warrior in hide armor swinging a greataxe, charging forward with a roar, tusks bared, snowy battlefield with goblin horde",
 "wolf": "A lean grey wolf snarling in the snow, part of a pack running beside goblin riders, pine forest at dusk",
 "worg": "A worg, a large evil wolf with a spiky mane and glowing eyes, ridden by a goblin, snarling at the foot of a mountain ramp, rocks and snow",
 "winterwolf": "A huge white winter wolf with ice-blue eyes breathing a cone of freezing frost inside a wind-carved cave chamber, snow swirling",
 "mantikor": "A manticore with a lion body, bat wings, a human-like fanged face and a tail of spikes, launching spikes from a ledge inside a windy cavern crevice",
 "troll": "A troll, large, green warty hide, long arms and claws, regenerating wounds, lumbering through a deep underground hall lit by green fungus glow",
 "berserker": "An orc berserker with wild hair and bloodied greataxe, hide armor, roaring with rage beside a fire giant's feet, burning battlefield",
 "oger-kette": "An ogre chain brute swinging a massive spiked iron chain in a wide arc, standing in the gap of a wooden barricade on a narrow mountain ramp, snow",
 "oger-bolzen": "An ogre carrying a huge crude bolt launcher like a hand-held ballista, aiming from the edge of a stone platform in a mountain pass",
 "bogenschuetze": "A hobgoblin archer in studded leather drawing a longbow from behind stone battlements, quiver full of arrows, keen focused eyes, mountain pass",
 "hoellenhund": "A hell hound, a large black dog with glowing red eyes and flames licking from its jaws, lying at the foot of a chain throne in a dark castle hall",
 "greif": "A majestic griffon, eagle head and wings with a lion body, saddled with leather riding straps, perched on a castle tower at dawn over snowy farmland, ready to carry a rider",
}
def gen(key, prompt, ar):
    path = os.path.join(OUT, key + ".png")
    if os.path.exists(path): print("skip", key); return
    body = {"contents":[{"parts":[{"text": prompt + " " + STYLE}]}],
            "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":ar}}}
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(body).encode(), headers={"Content-Type":"application/json","x-goog-api-key":KEY})
    for attempt in range(4):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=180))
            for p in r["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    open(path,"wb").write(base64.b64decode(p["inlineData"]["data"])); print("ok", key); return
            print("no image", key, json.dumps(r)[:300])
        except Exception as e:
            print("err", key, attempt, str(e)[:200]); time.sleep(5*(attempt+1))
for k,p in BIG.items():
    if not only or k in only: gen(k, p, "3:2")
for k,p in SMALL.items():
    if not only or k in only: gen(k, p, "16:9")
