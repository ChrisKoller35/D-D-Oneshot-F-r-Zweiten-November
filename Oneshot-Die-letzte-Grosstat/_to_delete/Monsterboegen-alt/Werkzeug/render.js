// node render.js <ordner>  -> je HTML eine PDF und eine PNG
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const base = path.join(dir, f.replace('.html', ''));
    await p.goto('file://' + path.join(dir, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => { const c = document.querySelector('.cols'); return c.scrollWidth > c.clientWidth + 2; });
    await p.pdf({ path: base + '.pdf', format: 'A4', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    await p.screenshot({ path: base + '.png', fullPage: false });
    console.log(f, over ? 'UEBERLAUF' : 'passt');
  }
  await b.close();
})();
