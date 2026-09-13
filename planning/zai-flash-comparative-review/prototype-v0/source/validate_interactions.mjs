import { chromium } from '/home/ubuntu/micro-standard-wave0-staging/node_modules/playwright/index.mjs';
const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
const page=await browser.newPage({viewport:{width:390,height:844}}); const base='http://127.0.0.1:4183/index.html';
await page.goto(base,{waitUntil:'networkidle'});
await page.locator('[data-period="مخصص"]').click(); const custom=await page.locator('[role="dialog"]').isVisible(); await page.locator('.close-btn').click(); await page.locator('#overlay-root').evaluate(e=>e.innerHTML='');
await page.locator('[data-view="detail"]').click(); const states=[]; for(let i=0;i<5;i++){states.push(await page.locator('.state-row b').first().textContent());await page.locator('[data-cycle]').click();}
await page.locator('[data-open="confirm"]').click(); const confirm=await page.locator('[role="dialog"]').isVisible(); await page.locator('.close-btn').click(); await page.locator('#overlay-root').evaluate(e=>e.innerHTML='');
await page.locator('[data-view="tools"]').click(); await page.locator('[data-tool="salary"]').click(); await page.locator('[data-tool-input]').fill('1200'); await page.locator('[data-calc]').click(); const result=await page.locator('.calc-result strong').textContent();
const out={customPeriodSheet:custom,lifecycleStates:states,confirmationBoundary:confirm,toolResult:result,pass:custom&&confirm&&states.length===5&&states.includes('قيد الانتظار')&&states.includes('يمكن إعادة الفحص')&&states.includes('نتيجة مؤكدة توضيحيًا')&&result.includes('1,416')}; console.log(JSON.stringify(out,null,2)); await browser.close();
