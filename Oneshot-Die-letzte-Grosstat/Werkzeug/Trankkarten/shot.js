const {chromium}=require('playwright');const jobs=require(process.argv[2]);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:750,height:1050}});
for(const [h,o] of jobs){await p.goto('file://'+h,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
await p.screenshot({path:o,omitBackground:true});console.log(o)}await b.close()})();
