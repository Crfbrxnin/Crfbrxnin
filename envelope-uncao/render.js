const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/envelope.html');await p.waitForTimeout(300);
await p.pdf({path:__dirname+'/envelope-uncao-12x15cm-vertical.pdf',width:'126mm',height:'156mm',printBackground:true,preferCSSPageSize:true});
await b.close();})();
