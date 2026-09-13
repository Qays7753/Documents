from pathlib import Path
from playwright.sync_api import sync_playwright

proto = Path('/home/ubuntu/Documents_reconciliation_fix/planning/micro-standard-v2-reconciliation-2026-09/prototype-v1/prototype.html').resolve().as_uri()
results = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=1)
    console_errors = []
    page_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
    page.on('pageerror', lambda exc: page_errors.append(str(exc)))
    page.goto(proto, wait_until='load')
    page.wait_for_timeout(250)

    def check(name, condition):
        results.append((name, bool(condition)))

    check('page_loaded', page.locator('main.stage').count() == 1)
    check('rtl', page.locator('html[dir="rtl"]').count() == 1)
    check('six_scenes', page.locator('.chrome-tabs button').count() == 6)

    for scene in ['s1', 's2', 's3', 's4', 's5', 's6']:
        page.locator(f'.chrome-tabs button[data-scene="{scene}"]').click()
        page.wait_for_timeout(250)
        check(f'scene_{scene}_visible', not page.locator(f'#{scene}').get_attribute('hidden'))

    page.locator('.chrome-tabs button[data-scene="s1"]').click()
    page.locator('#ctrl-vp button[data-vp="320"]').click()
    page.locator('#ctrl-text button[data-text="200"]').click()
    page.wait_for_timeout(150)
    frame_w = page.locator('html').evaluate("el => getComputedStyle(el).getPropertyValue('--frame-w').trim()")
    check('viewport_320_control', frame_w == '320px')
    page.locator('#ctrl-vp button[data-vp="430"]').click()
    page.locator('#ctrl-text button[data-text="100"]').click()
    page.wait_for_timeout(150)
    frame_w = page.locator('html').evaluate("el => getComputedStyle(el).getPropertyValue('--frame-w').trim()")
    check('viewport_430_control', frame_w == '430px')

    page.locator('#ctrl-text button[data-text="200"]').click()
    page.locator('#ctrl-motion button[data-motion="reduced"]').click()
    page.wait_for_timeout(150)
    check('reduced_motion_control', page.locator('html[data-motion="reduced"]').count() == 1)

    page.locator('.chrome-tabs button[data-scene="s2"]').click()
    page.locator('#stripe-toggle').click()
    check('stripe_toggle', page.locator('#stripe-toggle[aria-pressed="true"]').count() == 1 and page.locator('.row.stripe').count() >= 1)

    page.locator('.chrome-tabs button[data-scene="s3"]').click()
    page.locator('#ctrl-route button[data-route="deep"]').click()
    page.locator('#ctrl-kb button[data-kb="open"]').click()
    page.locator('#ctx-toggle').click()
    check('aux_deep_route', page.locator('#aux-phone[data-route-kind="deep"]').count() == 1)
    check('aux_keyboard_open', page.locator('#aux-phone[data-keyboard="open"]').count() == 1)
    check('context_suppressed', page.locator('#aux-ctx.suppressed').count() == 1)
    page.locator('#aux-content').evaluate("el => { el.scrollTop = 40; el.dispatchEvent(new Event('scroll')); }")
    check('aux_scroll_border', page.locator('#aux-topbar.scrolled').count() == 1)

    page.locator('.chrome-tabs button[data-scene="s4"]').click()
    page.locator('#save-btn').click()
    check('save_loading', page.locator('#save-btn[aria-busy="true"]').count() == 1)
    page.wait_for_timeout(1550)
    check('save_completion', page.locator('#inline-result:not([hidden])').count() == 1)

    page.locator('.chrome-tabs button[data-scene="s5"]').click()
    page.locator('#open-sheet').click()
    check('sheet_open', page.locator('#sheet:not([hidden])').count() == 1 and page.locator('#scrim:not([hidden])').count() == 1)
    page.keyboard.press('Escape')
    check('sheet_escape_close', page.locator('#sheet[hidden]').count() == 1 and page.locator('#scrim[hidden]').count() == 1)
    page.locator('#open-dialog').click()
    check('dialog_open', page.locator('#dialog-wrap:not([hidden])').count() == 1)
    page.locator('#dlg-cancel').click()
    check('dialog_close', page.locator('#dialog-wrap[hidden]').count() == 1)

    for width in [320, 360, 390, 430]:
        page.set_viewport_size({'width': width, 'height': 844})
        page.wait_for_timeout(100)
        overflow = page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth')
        check(f'no_document_overflow_{width}', not overflow)

    check('no_console_errors', len(console_errors) == 0)
    check('no_page_errors', len(page_errors) == 0)
    browser.close()

failed = [name for name, ok in results if not ok]
print(f'CHECKS={len(results)}')
print(f'PASSED={len(results) - len(failed)}')
print(f'FAILED={len(failed)}')
for name in failed:
    print(f'FAIL={name}')
if console_errors:
    print('CONSOLE_ERRORS=' + repr(console_errors))
if page_errors:
    print('PAGE_ERRORS=' + repr(page_errors))
raise SystemExit(1 if failed else 0)
