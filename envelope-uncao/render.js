const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:1});
await p.goto('file://'+__dirname+'/envelope.html');await p.waitForTimeout(300);
await p.pdf({path:__dirname+'/envelope-uncao-15x12cm.pdf',width:'156mm',height:'126mm',printBackground:true,preferCSSPageSize:true});
await b.close();})();
