// node render.js <ordner> [datei...] -> je HTML eine PDF und eine PNG; meldet Überlauf
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = path.resolve(process.argv[2]); const only = process.argv.slice(3);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html') && (!only.length || only.includes(f.replace('.html',''))))) {
    const base = path.join(dir, f.replace('.html', ''));
    await p.goto('file://' + path.join(dir, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => {
      const c = document.querySelector('.cols'); if (c) return c.scrollWidth > c.clientWidth + 2 ? 'UEBERLAUF' : 'passt';
      const r = []; document.querySelectorAll('.card').forEach((card, i) => {
        const body = card.querySelector('.body'), foot = card.querySelector('.foot');
        const last = body.lastElementChild.getBoundingClientRect().bottom, ft = foot.getBoundingClientRect().top;
        r.push((i+1) + ':' + (last > ft - 2 ? 'UEBERLAUF ' + Math.round(last - ft) + 'px' : 'frei ' + Math.round(ft - last) + 'px'));
      }); return r.join('  ');
    });
    await p.pdf({ path: base + '.pdf', format: 'A4', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    await p.screenshot({ path: base + '.png', fullPage: false });
    console.log(f, over);
  }
  await b.close();
})();
