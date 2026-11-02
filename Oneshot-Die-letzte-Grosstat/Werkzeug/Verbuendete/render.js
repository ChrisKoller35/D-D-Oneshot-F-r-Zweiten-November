// node render.js <ordner> -> je HTML eine PDF und eine PNG; meldet, ob der Text in die Seite passt
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort()) {
    const base = path.join(dir, f.replace('.html', ''));
    await p.goto('file://' + path.join(dir, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => {
      const foot = document.querySelector('.foot'); if (!foot) return 'Karte';
      const ft = foot.getBoundingClientRect().top; let worst = 1e9;
      document.querySelectorAll('.links, .rechts').forEach(c => { const last = c.lastElementChild.getBoundingClientRect().bottom; worst = Math.min(worst, ft - last); });
      return worst < 2 ? 'UEBERLAUF ' + Math.round(-worst) + 'px' : 'frei ' + Math.round(worst) + 'px';
    });
    await p.pdf({ path: base + '.pdf', format: 'A4', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    await p.screenshot({ path: base + '.png', fullPage: false });
    console.log(f, over);
  }
  await b.close();
})();
