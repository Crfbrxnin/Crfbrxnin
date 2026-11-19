const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/envelope-v2.html');await p.waitForSelector('body[data-ready]');
await p.pdf({path:__dirname+'/envelope-uncao-v2-12x15cm-vertical.pdf',width:'126mm',height:'156mm',printBackground:true});
await b.close();})();
