import { chromium } from '/home/ubuntu/micro-standard-wave0-staging/node_modules/playwright/index.mjs';
import fs from 'node:fs';
const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
const base='http://127.0.0.1:4183/index.html';
const evidence='/home/ubuntu/prototypes/micro-standard-v2-overall-review/evidence';
fs.mkdirSync(evidence,{recursive:true});
const results=[];
for(const width of [320,360,390,430]){
  await page.setViewportSize({width,height:844}); await page.goto(base,{waitUntil:'networkidle'});
  const common=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,dir:getComputedStyle(document.documentElement).direction,nav:document.querySelectorAll('.nav-item').length,heading:document.querySelector('h2')?.textContent||''}));
  results.push({width,view:'home',...common,pass:common.scrollWidth<=width&&common.dir==='rtl'&&common.nav===4});
}
const scenes=[['home','الرئيسية'],['finance','المالية'],['orders','الطلبات'],['detail','التفاصيل'],['tools','الأدوات']];
await page.setViewportSize({width:390,height:844});
for(const [view,label] of scenes){
  await page.goto(base,{waitUntil:'networkidle'});
  if(view!=='home'){
    if(view==='detail') await page.locator('[data-view="detail"]').click();
    else await page.locator(`.nav-item[data-view="${view}"]`).click();
  }
  const has=await page.evaluate(()=>({h:document.querySelector('h2')?.textContent||'',overflow:document.documentElement.scrollWidth>innerWidth,buttons:document.querySelectorAll('button').length,rtl:getComputedStyle(document.documentElement).direction}));
  await page.screenshot({path:`${evidence}/scene-${view}-390.png`,fullPage:true});
  results.push({view,label,...has,pass:!has.overflow&&has.rtl==='rtl'&&has.buttons>0});
}
await page.goto(base,{waitUntil:'networkidle'});
await page.locator('.nav-item[data-view="finance"]').click(); await page.locator('[data-chart-alt]').click();
const chartAlt=await page.locator('.chart-alt').isVisible();
await page.locator('.nav-item[data-view="orders"]').click(); await page.locator('[data-open="order"]').click(); const sheet=await page.locator('[role="dialog"]').isVisible(); await page.locator('.close-btn').click();
await page.locator('[data-view="detail"]').count().catch(()=>{});
await page.goto(base,{waitUntil:'networkidle'}); await page.locator('.nav-item[data-view="tools"]').click(); await page.locator('[data-tool-input]').fill('50'); await page.locator('[data-calc]').click(); const toast=await page.locator('.toast').isVisible();
await page.goto(base,{waitUntil:'networkidle'}); await page.locator('[data-view="detail"]').count().catch(()=>{});
await page.goto(base,{waitUntil:'networkidle'}); await page.locator('.nav-item[data-view="finance"]').click(); await page.evaluate(()=>document.body.style.zoom='2');
await page.screenshot({path:`${evidence}/scene-finance-200pct.png`,fullPage:true});
const stateChecks={chartAlt,sheet,toolRecalcToast:toast};
const scale=[];
for(const zoom of [1,1.3,2]){await page.goto(base,{waitUntil:'networkidle'});await page.evaluate(z=>document.body.style.zoom=String(z),zoom);const r=await page.evaluate(()=>{const rect=document.querySelector('.prototype-shell').getBoundingClientRect();const bad=[...document.querySelectorAll('body *')].some(el=>{const x=el.getBoundingClientRect();return x.right>innerWidth+1||x.left<-1});return {zoom:document.body.style.zoom,scrollWidth:document.documentElement.scrollWidth,viewport:innerWidth,bodyWidth:rect.width,viewportClip:bad,overflow:document.documentElement.scrollWidth>innerWidth||bad}});scale.push({...r,pass:!r.overflow});}
const report={viewportResults:results,interactionChecks:stateChecks,scaleResults:scale,pass:results.every(x=>x.pass)&&Object.values(stateChecks).every(Boolean)&&scale.every(x=>x.pass)};
fs.writeFileSync(`${evidence}/BROWSER_VALIDATION_RESULTS.json`,JSON.stringify(report,null,2));
console.log(JSON.stringify(report,null,2));
await browser.close();
