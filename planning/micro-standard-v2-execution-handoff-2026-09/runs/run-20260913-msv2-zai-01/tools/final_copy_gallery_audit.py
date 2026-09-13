from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path('/home/ubuntu/Documents_final_copy')
URL=(ROOT/'micro-standard-v2'/'component-gallery.html').resolve().as_uri()
checks=[]
def ck(name, ok, detail=''):
    checks.append((ok,name,detail))

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':390,'height':844})
    errors=[]
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(f'{m.type}: {m.text}') if m.type=='error' else None)
    page.goto(URL, wait_until='load')
    page.wait_for_timeout(250)
    ck('Gallery has no page/console errors', not errors, '; '.join(errors))

    create=page.locator('.btn-create').first
    icon=page.locator('.iconbtn-primary').first
    fab=page.locator('.fab').first
    save=page.locator('.btn-save').first
    commit=page.locator('.btn-primary').first
    def style(el,prop): return el.evaluate('(e,p)=>getComputedStyle(e).getPropertyValue(p)',prop).strip()
    ck('text create uses Clay bg', style(create,'background-color')=='rgb(217, 119, 87)', style(create,'background-color'))
    ck('text create uses dark readable ink', style(create,'color')=='rgb(20, 20, 19)', style(create,'color'))
    ck('icon create uses white ink', style(icon,'color')=='rgb(255, 255, 255)', style(icon,'color'))
    ck('FAB uses white icon ink', style(fab,'color')=='rgb(255, 255, 255)', style(fab,'color'))
    ck('save uses Warm Tint', style(save,'background-color')=='rgb(245, 244, 237)', style(save,'background-color'))
    ck('save uses warm ink', style(save,'color')=='rgb(20, 20, 19)', style(save,'color'))
    ck('commit uses Warm-Ink fill', style(commit,'background-color')=='rgb(20, 20, 19)', style(commit,'background-color'))

    # Pressed save edge is represented by an explicit demo state.
    pressed=page.locator('.btn-save.is-pressed').first
    shadow=style(pressed,'box-shadow')
    ck('pressed save keeps Clay edge', '201, 100, 66' in shadow, shadow)

    # Loading duplicate protection.
    load=page.locator('[data-loading-btn]').first
    if load.count():
        load.click(); load.click(); page.wait_for_timeout(100)
        ck('loading sets aria-busy', load.get_attribute('aria-busy')=='true', str(load.get_attribute('aria-busy')))
        ck('loading disables duplicate submit', load.is_disabled(), str(load.is_disabled()))
        page.wait_for_timeout(2600)
        ck('loading restores button', load.get_attribute('aria-busy')=='false' and not load.is_disabled())
    else: ck('loading control exists',False)

    # Dialog Escape and chart cycle.
    opener=page.locator('[data-open-dialog]').first
    anchor=page.locator('[data-dialog-anchor]').first
    if opener.count() and anchor.count():
        opener.click(); page.wait_for_timeout(100); page.keyboard.press('Escape'); page.wait_for_timeout(250)
        ck('Escape closes Gallery dialog', not anchor.is_visible())
    else: ck('Gallery dialog controls exist',False)

    chart=page.locator('[data-chart-cycle]').first
    body=page.locator('[data-chart-body]').first
    if chart.count() and body.count():
        states=[]
        for _ in range(4):
            visible=body.locator('[data-chart-state]:visible').first
            states.append(visible.get_attribute('data-chart-state') if visible.count() else 'none')
            chart.click(); page.wait_for_timeout(250)
        ck('chart cycles distinct states', len(set(states))>=3, str(states))
    else: ck('chart controls exist',False)

    # Actual viewport buttons: ensure page has no horizontal overflow at 320 and 390.
    for width in [320,390]:
        page.set_viewport_size({'width':width,'height':844}); page.wait_for_timeout(100)
        overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
        ck(f'no horizontal overflow at {width}px', not overflow, f'scrollWidth={page.evaluate("document.documentElement.scrollWidth")} innerWidth={page.evaluate("window.innerWidth")}')
    browser.close()

fails=[x for x in checks if not x[0]]
for ok,name,detail in checks: print(('PASS' if ok else 'FAIL')+': '+name+((' — '+detail) if detail else ''))
print(f'SUMMARY: failures={len(fails)} checks={len(checks)}')
raise SystemExit(1 if fails else 0)
