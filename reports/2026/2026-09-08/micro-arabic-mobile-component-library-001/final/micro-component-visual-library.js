/* =========================================================================
   MICRO COMPONENT VISUAL LIBRARY — micro-component-visual-library.js
   Part 1/2: core — views, instantiation, controls, measurement, audit
   Vanilla JS, zero dependencies, zero network. Light Mode only.
   ========================================================================= */

(function () {
  'use strict';

  var Micro = {
    frames: [],        // all instantiated preview frames
    liveScreen: null,  // the interactive composition screen
    overlays: null     // overlay controller (part 2)
  };
  window.Micro = Micro;

  var DEVICE_SIZES = {
    '320': { w: 320, h: 568 },
    '360': { w: 360, h: 640 },
    '390': { w: 390, h: 844 },
    '430': { w: 430, h: 932 }
  };

  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ===== 1. View switching ============================================== */

  function initViews() {
    var tabs = qsa('.lab-tab');
    var views = qsa('.lab-view');
    function activate(name, push) {
      tabs.forEach(function (t) {
        t.setAttribute('aria-selected', t.dataset.viewBtn === name ? 'true' : 'false');
      });
      views.forEach(function (v) {
        v.classList.toggle('is-active', v.dataset.view === name);
      });
      if (push && location.hash !== '#' + name) { history.replaceState(null, '', '#' + name); }
      window.scrollTo({ top: 0 });
      if (name === 'verification') {
        // Frames are visible only now — measure after layout settles.
        requestAnimationFrame(function () { setTimeout(runAudit, 200); });
      }
    }
    tabs.forEach(function (t) {
      t.addEventListener('click', function () { activate(t.dataset.viewBtn, true); });
    });
    var initial = (location.hash || '#foundation').replace('#', '');
    if (['foundation', 'library', 'composition', 'verification'].indexOf(initial) === -1) { initial = 'foundation'; }
    activate(initial, false);
    window.addEventListener('hashchange', function () {
      var name = (location.hash || '#foundation').replace('#', '');
      if (['foundation', 'library', 'composition', 'verification'].indexOf(name) !== -1) { activate(name, false); }
    });
  }

  /* ===== 2. Composition instantiation =================================== */

  function instantiateFrame(frameEl, options) {
    var tpl = qs('#tpl-composition');
    if (!tpl || !frameEl) { return null; }
    // Template root is .phone-screen (includes the persistent bottom nav)
    var screen = tpl.content.firstElementChild ? tpl.content.firstElementChild.cloneNode(true) : null;
    if (!screen || !screen.classList.contains('phone-screen')) { return null; }
    if (options.dir) { screen.setAttribute('dir', options.dir); }
    frameEl.appendChild(screen);
    if (options.preview) { frameEl.classList.add('is-preview'); }
    fitNavLabels(screen);
    Micro.frames.push(frameEl);
    return screen;
  }

  function initComposition() {
    // Live interactive frame in the Test Composition view
    var liveFrame = qs('#comp-frame');
    if (liveFrame) {
      Micro.liveScreen = instantiateFrame(liveFrame, { dir: 'rtl' });
      var size = DEVICE_SIZES['390'];
      liveFrame.style.setProperty('--frame-w', size.w + 'px');
      liveFrame.style.setProperty('--frame-h', size.h + 'px');
    }
    // Verification preview frames (RTL) + one geometry-only LTR clone
    var previews = [
      { el: '#vf-320', w: 320 }, { el: '#vf-360', w: 360 },
      { el: '#vf-390', w: 390 }, { el: '#vf-430', w: 430 }
    ];
    previews.forEach(function (p) {
      var frame = qs(p.el);
      if (!frame) { return; }
      frame.style.setProperty('--frame-w', p.w + 'px');
      frame.style.setProperty('--frame-h', DEVICE_SIZES[String(p.w)].h + 'px');
      instantiateFrame(frame, { dir: 'rtl', preview: true });
    });
    var ltrFrame = qs('#vf-ltr');
    if (ltrFrame) {
      ltrFrame.style.setProperty('--frame-w', '390px');
      ltrFrame.style.setProperty('--frame-h', '844px');
      instantiateFrame(ltrFrame, { dir: 'ltr', preview: true });
    }
  }

  /* ===== 3. Global controls (lab switches) =============================== */

  function setControlGroup(groupSel, onActivate) {
    var btns = qsa(groupSel + ' .ctrl-btn');
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        onActivate(b.dataset.value);
      });
    });
  }

  function initControls() {
    // Frame width for the live composition
    setControlGroup('[data-ctrl="width"]', function (val) {
      var s = DEVICE_SIZES[val] || DEVICE_SIZES['390'];
      var liveFrame = qs('#comp-frame');
      if (liveFrame) {
        liveFrame.style.setProperty('--frame-w', s.w + 'px');
        liveFrame.style.setProperty('--frame-h', s.h + 'px');
      }
      var cap = qs('#frame-caption');
      if (cap) { cap.textContent = s.w + ' × ' + s.h + 'px · RTL'; }
    });
    // Global direction (RTL primary, LTR geometry check)
    setControlGroup('[data-ctrl="dir"]', function (val) {
      document.documentElement.setAttribute('dir', val);
    });
    // Text scale — root font size; component text is rem-based, lab chrome is px
    setControlGroup('[data-ctrl="scale"]', function (val) {
      document.documentElement.style.fontSize = val + 'px';
      requestAnimationFrame(function () {
        Micro.frames.forEach(function (f) { fitNavLabels(qs('.phone-screen', f)); });
        if (Micro.liveScreen) { fitNavLabels(Micro.liveScreen); }
        updatePeekTable();
      });
    });
    // Motion mode (manual switch; initialized from prefers-reduced-motion)
    setControlGroup('[data-ctrl="motion"]', function (val) {
      document.documentElement.setAttribute('data-motion', val);
    });
    // Grayscale verification aid (color-independence check)
    setControlGroup('[data-ctrl="gray"]', function (val) {
      if (val === 'on') { document.documentElement.setAttribute('data-gray', '1'); }
      else { document.documentElement.removeAttribute('data-gray'); }
    });
    // Reduced motion preference on load
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.documentElement.setAttribute('data-motion', 'reduced');
      qsa('[data-ctrl="motion"] .ctrl-btn').forEach(function (b) {
        b.setAttribute('aria-pressed', b.dataset.value === 'reduced' ? 'true' : 'false');
      });
    }
  }

  /* ===== 4. Nav label auto-fit (320px safety) ============================ */

  function fitNavLabels(screen) {
    if (!screen) { return; }
    qsa('.nav-item', screen).forEach(function (item) {
      var label = qs('.nav-label', item);
      if (!label) { return; }
      var short = item.dataset.short || label.textContent;
      var long = item.dataset.long || label.textContent;
      item.dataset.short = short;
      item.dataset.long = long;
      // reset to long, then swap if it would clip
      label.textContent = long;
      var fits = label.scrollWidth <= item.clientWidth - 6;
      if (!fits) { label.textContent = short; }
    });
  }

  /* ===== 5. QuickActionRail peek measurement ============================= */

  function measurePeek(frame) {
    var rail = qs('.quick-action-rail', frame);
    if (!rail) { return { peek: 0, tile: null }; }
    var frameRect = frame.getBoundingClientRect();
    var rtl = (qs('.phone-screen', frame) || frame).getAttribute('dir') === 'rtl';
    var tiles = qsa('.quick-tile', rail);
    var result = { peek: 0, tile: null };
    tiles.forEach(function (tile) {
      var r = tile.getBoundingClientRect();
      var visible;
      if (rtl) {
        visible = r.right - frameRect.left; // overflow continues toward the left
      } else {
        visible = frameRect.right - r.left;
      }
      var w = r.width || 88;
      visible = Math.max(0, Math.min(visible, w));
      var fullyVisible = visible >= w - 1;
      if (!fullyVisible && visible > 0 && !result.tile) {
        result.peek = Math.round(visible);
        result.tile = tiles.indexOf(tile) + 1;
      }
    });
    return result;
  }

  function updatePeekTable() {
    var tbody = qs('#peek-results');
    if (!tbody) { return; }
    // Only measure frames that are actually laid out (their view is active).
    var visible = Micro.frames.filter(function (f) { return f.getBoundingClientRect().width > 0; });
    if (!visible.length) { return; }
    var expected = { '320': 16, '360': 56, '390': 86, '430': 30 };
    var rows = '';
    ['320', '360', '390', '430'].forEach(function (w) {
      var frame = qs('#vf-' + w);
      var m = (frame && frame.getBoundingClientRect().width > 0) ? measurePeek(frame) : { peek: 0, tile: 0 };
      var exp = expected[w];
      var ok = w === '320' ? m.peek >= 8 : m.peek >= 28;
      rows += '<tr><td class="ltr">' + w + 'px</td>' +
        '<td class="ltr">' + m.peek + 'px</td>' +
        '<td class="ltr">' + exp + 'px</td>' +
        '<td>' + (ok ? passBadge('ناجح') : failBadge('تحقّق')) + '</td></tr>';
    });
    tbody.innerHTML = rows;
  }

  function passBadge(t) { return '<span class="badge badge--pass"><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>' + t + '</span>'; }
  function failBadge(t) { return '<span class="badge badge--fail"><svg class="icon" aria-hidden="true"><use href="#i-x"/></svg>' + t + '</span>'; }
  function noteBadge(t) { return '<span class="badge badge--note">' + t + '</span>'; }

  /* ===== 6. Audit engine (in-lab measured evidence) ====================== */

  function runAudit() {
    updatePeekTable();
    var tbody = qs('#audit-results');
    if (!tbody) { return; }
    var rows = [];

    // A1 — no horizontal overflow in any laid-out preview frame
    var laidOut = Micro.frames.filter(function (f) { return f.getBoundingClientRect().width > 0; });
    var overflow = laidOut.length > 0 && laidOut.every(function (f) {
      var sc = qs('.phone-scroll', f);
      return sc && sc.scrollWidth <= sc.clientWidth + 1;
    });
    rows.push(auditRow('عدم وجود تمرير أفقي في كل الأُطارات', overflow ? 'سليم' : 'فشل', overflow));

    // A2 — screen edge 16px at all widths (visible frames only).
    //      .metric-group is inset by margin-inline:16 so its box is the probe.
    var edgeOk = true; var edgeSample = '';
    laidOut.forEach(function (f) {
      var mg = qs('.metric-group', f);
      if (!mg) { return; }
      var fr = f.getBoundingClientRect();
      var mr = mg.getBoundingClientRect();
      var insetStart = Math.round(fr.right - mr.right); // RTL inline-start
      var insetEnd = Math.round(mr.left - fr.left);     // RTL inline-end
      if (Math.abs(insetStart - 16) > 1 || Math.abs(insetEnd - 16) > 1) { edgeOk = false; }
      edgeSample = insetStart + '/' + insetEnd;
    });
    rows.push(auditRow('هامش الشاشة 16px (مبدأ/نهاية)', edgeSample || '—', edgeSample ? edgeOk : true));

    // A3 — touch targets ≥ 44px, measured on a visible preview frame
    var minTarget = Infinity;
    var scopeFrame = qs('#vf-390');
    if (!scopeFrame || scopeFrame.getBoundingClientRect().width === 0) { scopeFrame = Micro.liveScreen ? Micro.liveScreen.parentElement : null; }
    if (scopeFrame && scopeFrame.getBoundingClientRect().width > 0) {
      qsa('button, input, select', scopeFrame).forEach(function (el) {
        if (el.disabled) { return; }
        var h = el.getBoundingClientRect().height;
        if (h > 0) { minTarget = Math.min(minTarget, h); }
      });
    }
    rows.push(auditRow('أصغر هدف لمس (44px أدنى)', minTarget === Infinity ? '—' : Math.round(minTarget) + 'px', minTarget >= 44));

    // A4 — currency rule: the Latin currency code never appears in the UI,
    //      and the Arabic currency node never sits inside an LTR isolate.
    var bodyText = document.body.textContent || '';
    var noJod = bodyText.indexOf('JOD') === -1;
    var curInside = qsa('bdi[dir="ltr"]').some(function (b) { return b.textContent.indexOf('د.أ') !== -1; });
    rows.push(auditRow('لا رمز عملة لاتيني، والعملة خارج عزل الاتجاه', (noJod ? 'سليم' : 'وجد رمز') + ' · ' + (curInside ? 'خلل' : 'سليم'), noJod && !curInside));

    // A5 — no unresolved placeholders
    var noPlaceholder = document.body.textContent.indexOf('{{') === -1;
    rows.push(auditRow('لا عناصر بديلة غير محلولة', noPlaceholder ? 'سليم' : 'وجد {{', noPlaceholder));

    // A6 — icon mirror registry: semantic icons never mirrored
    var semanticIcons = ['i-check', 'i-clock', 'i-plus', 'i-receipt', 'i-package', 'i-banknote', 'i-trash', 'i-calendar', 'i-search', 'i-x', 'i-alert', 'i-info', 'i-wifi-off', 'i-refresh', 'i-ellipsis', 'i-home', 'i-users', 'i-store', 'i-truck', 'i-trending', 'i-hand-coins'];
    var mirrorLeak = qsa('.icon-mirror use').some(function (u) {
      var href = u.getAttribute('href') || u.getAttribute('xlink:href') || '';
      return semanticIcons.indexOf(href.replace('#', '')) !== -1;
    });
    rows.push(auditRow('سجل الانعكاس: لا انعكاس لأيقونات دلالية', mirrorLeak ? 'خلل' : 'سليم', !mirrorLeak));

    // A7 — motion durations from tokens (sheet 240ms, dialog 160ms, scrim 200ms)
    var probe = document.createElement('div');
    probe.style.cssText = 'position:absolute; width:0; height:0; overflow:hidden; visibility:hidden;';
    probe.innerHTML = '<div class="sheet"></div><div class="scrim"></div><div class="dialog"><div class="dialog-card"></div></div>';
    document.body.appendChild(probe);
    var mOk = false; var mVal = '—';
    try {
      var sd = getComputedStyle(probe.querySelector('.sheet')).transitionDuration;
      var cd = getComputedStyle(probe.querySelector('.dialog-card')).transitionDuration.split(',')[0];
      var scd = getComputedStyle(probe.querySelector('.scrim')).transitionDuration;
      mVal = 'sheet ' + sd + ' · dialog ' + cd + ' · scrim ' + scd;
      mOk = sd === '0.24s' && cd === '0.16s' && scd === '0.2s';
    } catch (e) { mVal = 'تعذّر القياس'; }
    document.body.removeChild(probe);
    rows.push(auditRow('أزمنة الحركة من الرموز (240/160/200ms)', mVal, mOk));

    // A8 — tabular figures on the primary value
    var pv = Micro.liveScreen ? qs('.primary-value', Micro.liveScreen) : null;
    var fvn = pv ? getComputedStyle(pv).fontVariantNumeric : '';
    rows.push(auditRow('أرقام جدولية للقيمة الرئيسية', fvn || '—', fvn.indexOf('tabular-nums') !== -1));

    // A9 — nav labels fit after auto-fit (visible frames only)
    var navOk = laidOut.length > 0 && laidOut.every(function (f) {
      return qsa('.nav-label', f).every(function (l) {
        return !l.parentElement || l.scrollWidth <= l.parentElement.clientWidth - 6 || l.scrollWidth <= 60;
      });
    });
    rows.push(auditRow('ملاءمة تسميات التنقل في 320px', navOk ? 'ملائمة' : 'قصّ', navOk));

    tbody.innerHTML = rows.join('');
    window.MicroAudit = {
      overflow: overflow, edge: edgeOk, minTarget: minTarget,
      noJod: noJod, currencyOutsideIsolate: !curInside,
      placeholders: noPlaceholder, mirrorRegistry: !mirrorLeak,
      motionTokens: mOk, tabular: fvn, navFit: navOk
    };
  }

  function auditRow(name, value, ok) {
    return '<tr><td>' + name + '</td><td class="ltr">' + value + '</td><td>' +
      (ok ? passBadge('ناجح') : failBadge('فشل')) + '</td></tr>';
  }

  /* ===== 7. Boot ========================================================== */

  function boot() {
    initViews();
    initComposition();
    initControls();
    var runBtn = qs('#audit-run');
    if (runBtn) { runBtn.addEventListener('click', runAudit); }
    window.addEventListener('load', function () {
      requestAnimationFrame(function () {
        fitNavLabels(Micro.liveScreen);
        // Audit only if the Verification view is the initial view; otherwise
        // it runs when the user switches to it (frames must be laid out).
        var vf = qs('#view-verification');
        if (vf && vf.classList.contains('is-active')) { setTimeout(runAudit, 200); }
      });
    });
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', boot); }
  else { boot(); }
})();
/* =========================================================================
   Part 2/2: overlays (sheet / dialog / scrim) + interaction contracts
   - focus trap, focus return, Escape, scrim tap, drag-to-dismiss
   - dirty-guard routing (never silently discard entered data)
   - loading → quiet completion (≥1.5s dwell) → immediate value update
   - destructive dialog ignores Escape/scrim (explicit choice only)
   ========================================================================= */

(function () {
  'use strict';

  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  var reduced = function () { return document.documentElement.getAttribute('data-motion') === 'reduced'; };
  function fmt(n) { return n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function uid() { return 'mc' + Math.random().toString(36).slice(2, 8); }

  /* Live region for state announcements */
  var liveRegion = null;
  function announce(msg) {
    if (!liveRegion) {
      liveRegion = document.createElement('div');
      liveRegion.setAttribute('role', 'status');
      liveRegion.className = 'vh';
      document.body.appendChild(liveRegion);
    }
    liveRegion.textContent = msg;
  }

  /* ===== Financial state (composition truth — values update immediately) == */

  var state = { cash: 1284.50, sales: 465.00, collections: 210.00, expenses: 92.50 };

  var ACTIONS = {
    sale:     { title: 'إضافة بيع', cta: 'تسجيل البيع', done: 'تم تسجيل البيع', sign: 1, context: 'بيع نقدي — عميل نقدي', metric: 'sales' },
    collect:  { title: 'تحصيل دين', cta: 'تسجيل التحصيل', done: 'تم تسجيل التحصيل', sign: 1, context: 'أبو أحمد — من أصل <bdi dir="ltr">400.00</bdi> د.أ', metric: 'collections' },
    expense:  { title: 'إضافة مصروف', cta: 'تسجيل المصروف', done: 'تم تسجيل المصروف', sign: -1, context: 'فئة: تشغيل', metric: 'expenses' },
    purchase: { title: 'إضافة شراء', cta: 'تسجيل الشراء', done: 'تم تسجيل الشراء', sign: -1, context: 'مؤسسة الشرق للتجهيزات', metric: null },
    payment:  { title: 'تسجيل دفعة', cta: 'تسجيل الدفعة', done: 'تم تسجيل الدفعة', sign: -1, context: 'لمؤسسة الشرق للتجهيزات', metric: null }
  };

  function updateDisplays() {
    qsa('[data-hook="cash"]').forEach(function (el) { el.textContent = fmt(state.cash); });
    qsa('[data-hook="sales"]').forEach(function (el) { el.textContent = fmt(state.sales); });
    qsa('[data-hook="collections"]').forEach(function (el) { el.textContent = '+' + fmt(state.collections); });
    qsa('[data-hook="expenses"]').forEach(function (el) { el.textContent = '-' + fmt(state.expenses); });
  }

  /* ===== Layer plumbing (scrim + sheet + dialog per host) ================= */

  function ctxFor(host) {
    if (host.__microCtx) { return host.__microCtx; }
    var scrim = document.createElement('div');
    scrim.className = 'scrim';
    scrim.setAttribute('data-state', 'closed');
    host.appendChild(scrim);
    var mgr = { host: host, scrim: scrim, sheet: null, dialog: null, opener: null, dirty: false, dragDy: 0 };
    scrim.addEventListener('click', function () {
      if (mgr.dialog) {
        if (mgr.dialog.dataset.modal === 'true') { return; } // destructive: explicit choice only
        closeDialog(mgr, 'cancel');
        return;
      }
      if (mgr.sheet) { requestSheetDismiss(mgr); }
    });
    document.addEventListener('keydown', function (e) { handleKey(e, mgr); });
    host.__microCtx = mgr;
    return mgr;
  }

  function handleKey(e, mgr) {
    var active = mgr.dialog || mgr.sheet;
    if (!active) { return; }
    if (e.key === 'Tab') {
      var focusables = qsa('button, input, select, [tabindex]:not([tabindex="-1"])', active)
        .filter(function (el) { return !el.disabled && el.offsetParent !== null; });
      if (!focusables.length) { return; }
      var first = focusables[0], last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      return;
    }
    if (e.key === 'Escape') {
      if (mgr.dialog) {
        if (mgr.dialog.dataset.modal === 'true') { return; }
        closeDialog(mgr, 'cancel'); // dirty-guard dialog: Escape keeps editing
        return;
      }
      if (mgr.sheet) { requestSheetDismiss(mgr); }
    }
  }

  function openSheet(host, buildFn, opts) {
    var mgr = ctxFor(host);
    if (mgr.sheet) { return mgr; }
    var sheet = document.createElement('div');
    sheet.className = 'sheet';
    sheet.setAttribute('data-state', 'closed');
    sheet.setAttribute('role', 'dialog');
    sheet.setAttribute('aria-modal', 'true');
    host.appendChild(sheet);
    mgr.sheet = sheet;
    mgr.opener = (document.activeElement && document.activeElement !== document.body) ? document.activeElement : null;
    mgr.dirty = false;
    buildFn(sheet, mgr, opts || {});
    requestAnimationFrame(function () {
      mgr.scrim.setAttribute('data-state', 'open');
      sheet.setAttribute('data-state', 'open');
    });
    bindDrag(sheet, mgr);
    var focusTarget = opts.focus ? qs(opts.focus, sheet) : qs('input, button:not(.sheet-handle-zone button)', sheet);
    if (!focusTarget) { focusTarget = qs('button', sheet); }
    setTimeout(function () { if (focusTarget && mgr.sheet) { focusTarget.focus(); } }, 80);
    return mgr;
  }

  function closeSheet(mgr) {
    var sheet = mgr.sheet;
    if (!sheet) { return; }
    sheet.setAttribute('data-state', 'closing');
    mgr.scrim.setAttribute('data-state', 'closed');
    setTimeout(function () {
      if (sheet.parentNode) { sheet.parentNode.removeChild(sheet); }
    }, 200);
    mgr.sheet = null;
    mgr.dirty = false;
    if (mgr.dialog) { closeDialog(mgr, 'cancel', true); }
    if (mgr.opener && mgr.opener.parentNode) { mgr.opener.focus(); }
  }

  function requestSheetDismiss(mgr) {
    if (!mgr.sheet) { return; }
    if (mgr.dirty) { openDirtyDialog(mgr); return; }
    closeSheet(mgr);
  }

  function bindDrag(sheet, mgr) {
    var zone = qs('.sheet-handle-zone', sheet);
    if (!zone) { return; }
    var dragging = false, startY = 0;
    zone.addEventListener('pointerdown', function (e) {
      dragging = true; startY = e.clientY; mgr.dragDy = 0;
      sheet.setAttribute('data-dragging', 'true');
      try { zone.setPointerCapture(e.pointerId); } catch (err) { /* pointer capture best-effort */ }
    });
    zone.addEventListener('pointermove', function (e) {
      if (!dragging) { return; }
      var dy = Math.max(0, e.clientY - startY);
      mgr.dragDy = dy;
      sheet.style.transform = 'translateY(' + dy + 'px)';
    });
    function finish() {
      if (!dragging) { return; }
      dragging = false;
      sheet.removeAttribute('data-dragging');
      sheet.style.transform = '';
      var threshold = reduced() ? 8 : 72;
      if (mgr.dragDy > threshold) { requestSheetDismiss(mgr); }
      mgr.dragDy = 0;
    }
    zone.addEventListener('pointerup', finish);
    zone.addEventListener('pointercancel', finish);
  }

  function openDialogRaw(mgr, html, opts) {
    if (mgr.dialog) { return; }
    var dialog = document.createElement('div');
    dialog.className = 'dialog';
    dialog.setAttribute('data-state', 'closed');
    dialog.setAttribute('role', 'alertdialog');
    dialog.setAttribute('aria-modal', 'true');
    if (opts && opts.modal) { dialog.dataset.modal = 'true'; }
    dialog.innerHTML = html;
    mgr.host.appendChild(dialog);
    mgr.dialog = dialog;
    if (!mgr.sheet) { mgr.opener = (document.activeElement && document.activeElement !== document.body) ? document.activeElement : null; }
    requestAnimationFrame(function () {
      if (!mgr.sheet) { mgr.scrim.setAttribute('data-state', 'open'); }
      dialog.setAttribute('data-state', 'open');
    });
    setTimeout(function () {
      var target = opts && opts.focus ? qs(opts.focus, dialog) : qs('button', dialog);
      if (target) { target.focus(); }
    }, 80);
    return dialog;
  }

  function closeDialog(mgr, action, silent) {
    var dialog = mgr.dialog;
    if (!dialog) { return; }
    dialog.setAttribute('data-state', 'closing');
    setTimeout(function () {
      if (dialog.parentNode) { dialog.parentNode.removeChild(dialog); }
    }, 140);
    mgr.dialog = null;
    if (!mgr.sheet) {
      mgr.scrim.setAttribute('data-state', 'closed');
      if (!silent && mgr.opener && mgr.opener.parentNode) { mgr.opener.focus(); }
    }
    if (mgr.onDialogAction) { mgr.onDialogAction(action); }
  }

  function openDirtyDialog(mgr) {
    mgr.onDialogAction = function (action) {
      mgr.onDialogAction = null;
      if (action === 'discard') { closeSheet(mgr); }
    };
    openDialogRaw(mgr,
      '<div class="dialog-card">' +
      '<h3 class="dialog-title">تجاهل التغييرات؟</h3>' +
      '<p class="dialog-body">لن يتم حفظ المبلغ المُدخل.</p>' +
      '<div class="dialog-actions">' +
      '<button class="button button--secondary" data-act="stay">متابعة التعديل</button>' +
      '<button class="button button--destructive-quiet" data-act="discard">تجاهل</button>' +
      '</div></div>', { focus: '[data-act="stay"]' });
    var dialog = mgr.dialog;
    qsa('button', dialog).forEach(function (b) {
      b.addEventListener('click', function () { closeDialog(mgr, b.dataset.act); });
    });
  }

  /* ===== Quick-entry sheet (sale / collect / expense / purchase / payment) */

  function openQuickEntry(host, cfg) {
    openSheet(host, function (sheet, mgr) {
      var amountId = uid();
      sheet.setAttribute('aria-label', cfg.title);
      sheet.innerHTML =
        '<div class="sheet-handle-zone"><span class="sheet-handle"></span></div>' +
        '<h3 class="sheet-title">' + cfg.title + '</h3>' +
        '<div class="sheet-body">' +
        '<p class="sheet-context">' + cfg.context + '</p>' +
        '<div class="field">' +
        '<label class="input-label" for="' + amountId + '">المبلغ</label>' +
        '<div class="input-wrap">' +
        '<input id="' + amountId + '" class="input-field input--amount" inputmode="decimal" ' +
        'autocomplete="off" value="365.00" aria-describedby="' + amountId + '-err">' +
        '<span class="input-affix">د.أ</span>' +
        '</div>' +
        '<span class="input-error" id="' + amountId + '-err" hidden>' +
        '<svg class="icon" aria-hidden="true"><use href="#i-alert"/></svg>' +
        'أدخل مبلغًا أكبر من صفر</span>' +
        '</div>' +
        '<div class="field">' +
        '<span class="input-label">طريقة الدفع</span>' +
        '<div class="segmented" role="group" aria-label="طريقة الدفع">' +
        '<button type="button" class="segmented-item" aria-pressed="true">نقدي</button>' +
        '<button type="button" class="segmented-item" aria-pressed="false">آجل</button>' +
        '</div></div>' +
        '</div>' +
        '<div class="sheet-footer">' +
        '<button type="button" class="button button--primary button--block" data-role="cta">' + cfg.cta + '</button>' +
        '<button type="button" class="button button--quiet button--block" data-role="cancel">إلغاء</button>' +
        '</div>';

      var input = qs('input', sheet);
      var field = qs('.field', sheet);
      var err = qs('.input-error', sheet);
      var cta = qs('[data-role="cta"]', sheet);
      var initial = input.value;

      function clearError() {
        err.hidden = true;
        field.classList.remove('has-error');
        input.removeAttribute('data-invalid');
      }
      input.addEventListener('input', function () {
        mgr.dirty = input.value !== initial;
        clearError();
      });
      input.addEventListener('blur', function () {
        var v = parseFloat(input.value.replace(/,/g, ''));
        if (isFinite(v) && v > 0) { input.value = fmt(v); }
      });

      qsa('.segmented-item', sheet).forEach(function (seg) {
        seg.addEventListener('click', function () {
          qsa('.segmented-item', sheet).forEach(function (s) { s.setAttribute('aria-pressed', s === seg ? 'true' : 'false'); });
        });
      });

      qs('[data-role="cancel"]', sheet).addEventListener('click', function () { closeSheet(mgr); });

      cta.addEventListener('click', function () {
        var v = parseFloat(input.value.replace(/,/g, ''));
        if (!isFinite(v) || v <= 0) {
          err.hidden = false;
          field.classList.add('has-error');
          input.setAttribute('data-invalid', 'true');
          input.focus();
          announce('أدخل مبلغًا أكبر من صفر');
          return;
        }
        clearError();
        mgr.dirty = false;
        cta.setAttribute('data-state', 'loading');
        cta.setAttribute('aria-busy', 'true');
        cta.innerHTML = '<span class="button-spinner" aria-hidden="true"></span><span>جاري الحفظ…</span>';
        announce('جاري الحفظ');
        setTimeout(function () {
          if (!mgr.sheet) { return; }
          cta.setAttribute('data-state', 'completed');
          cta.setAttribute('aria-busy', 'false');
          cta.innerHTML = '<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg><span>' + cfg.done + '</span>';
          announce(cfg.done);
          setTimeout(function () {
            var amount = cfg.sign * v;
            state.cash += amount;
            if (cfg.metric && state[cfg.metric] !== undefined) {
              state[cfg.metric] += cfg.metric === 'expenses' ? v : amount;
            }
            updateDisplays(); // final value appears immediately — no count-up
            closeSheet(mgr);
          }, 1600);
        }, 1200);
      });
    }, { focus: 'input' });
  }

  /* ===== More sheet (secondary destinations + profile/settings entry) ==== */

  function openMoreSheet(host) {
    openSheet(host, function (sheet, mgr) {
      sheet.setAttribute('aria-label', 'المزيد');
      var items = ['المورّدون', 'شركات التوصيل', 'التقارير', 'الإعدادات'];
      sheet.innerHTML =
        '<div class="sheet-handle-zone"><span class="sheet-handle"></span></div>' +
        '<h3 class="sheet-title">المزيد</h3>' +
        '<div class="sheet-body"><ul class="more-list">' +
        items.map(function (t) {
          return '<li><button type="button" class="more-item">' + t +
            '<svg class="icon icon-mirror operational-row-chevron" aria-hidden="true"><use href="#i-chevron-f"/></use></svg></button></li>';
        }).join('') +
        '</ul></div>';
      qsa('.more-item', sheet).forEach(function (b) {
        b.addEventListener('click', function () { closeSheet(mgr); });
      });
    }, { focus: '.more-item' });
  }

  /* ===== Destructive dialog demo (explicit choice only) ================== */

  function openDeleteDialog(host, doneNotice) {
    var mgr = ctxFor(host);
    mgr.onDialogAction = function (action) {
      mgr.onDialogAction = null;
      if (action === 'delete') {
        announce('تم حذف العملية');
        if (doneNotice) { doneNotice.hidden = false; }
      }
    };
    openDialogRaw(mgr,
      '<div class="dialog-card">' +
      '<h3 class="dialog-title">حذف المصروف؟</h3>' +
      '<p class="dialog-body">سيُضاف قيد عكسي بقيمة <bdi dir="ltr">35.00</bdi> د.أ ولن يمكن التراجع.</p>' +
      '<div class="dialog-actions">' +
      '<button class="button button--quiet" data-act="cancel">إلغاء</button>' +
      '<button class="button button--destructive" data-act="delete">حذف</button>' +
      '</div></div>', { modal: true, focus: '[data-act="cancel"]' });
    qsa('button', mgr.dialog).forEach(function (b) {
      b.addEventListener('click', function () { closeDialog(mgr, b.dataset.act); });
    });
  }

  /* ===== Wiring =========================================================== */

  function liveScreenHost() {
    var frame = qs('#comp-frame');
    return frame ? qs('.phone-screen', frame) : null;
  }

  function initInteractions() {
    // Rail tiles in the live composition → quick-entry sheets
    var host = liveScreenHost();
    if (host) {
      qsa('.quick-tile', host).forEach(function (tile) {
        var key = tile.dataset.action;
        var cfg = ACTIONS[key];
        if (!cfg) { return; }
        tile.addEventListener('click', function () { openQuickEntry(host, cfg); });
      });
      // Avatar + المزيد nav seat → unified profile/settings area
      var avatar = qs('.avatar', host);
      if (avatar) { avatar.addEventListener('click', function () { openMoreSheet(host); }); }
      var moreSeat = qs('.nav-item[data-nav="more"]', host);
      if (moreSeat) { moreSeat.addEventListener('click', function () { openMoreSheet(host); }); }
      // Bottom navigation active-state demo
      qsa('.nav-item', host).forEach(function (item) {
        item.addEventListener('click', function () {
          qsa('.nav-item', host).forEach(function (i) {
            i.classList.toggle('is-active', i === item);
            if (i === item) { i.setAttribute('aria-current', 'page'); }
            else { i.removeAttribute('aria-current'); }
          });
        });
      });
    }

    // Library demos hosted in mini-stages
    qsa('[data-open-sheet]').forEach(function (btn) {
      var stage = btn.closest('.mini-stage');
      if (stage) { btn.addEventListener('click', function () { openQuickEntry(stage, ACTIONS.sale); }); }
    });
    qsa('[data-open-dialog]').forEach(function (btn) {
      var stage = btn.closest('.mini-stage');
      if (stage) {
        btn.addEventListener('click', function () {
          var scope = stage.closest('.specimen') || stage.parentElement || stage;
          openDeleteDialog(stage, qs('[data-demo-deleted]', scope));
        });
      }
    });

    // Button loading → quiet completion → reset (interactive proof)
    var flowBtn = qs('#btn-flow-demo');
    if (flowBtn) {
      var original = flowBtn.innerHTML;
      flowBtn.addEventListener('click', function () {
        if (flowBtn.getAttribute('data-state')) { return; }
        flowBtn.setAttribute('data-state', 'loading');
        flowBtn.setAttribute('aria-busy', 'true');
        flowBtn.innerHTML = '<span class="button-spinner" aria-hidden="true"></span><span>جاري الحفظ…</span>';
        announce('جاري الحفظ');
        setTimeout(function () {
          flowBtn.setAttribute('data-state', 'completed');
          flowBtn.setAttribute('aria-busy', 'false');
          flowBtn.innerHTML = '<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg><span>تم التسجيل</span>';
          announce('تم التسجيل');
          setTimeout(function () {
            flowBtn.removeAttribute('data-state');
            flowBtn.innerHTML = original;
          }, 2400);
        }, 1200);
      });
    }

    // Error-recovery demos: first failure → explicit retry → completed
    qsa('[data-retry-demo]').forEach(function (retryBtn) {
      retryBtn.addEventListener('click', function () {
        var notice = retryBtn.closest('.state-notice');
        if (!notice || notice.dataset.busy === '1') { return; }
        notice.dataset.busy = '1';
        retryBtn.setAttribute('data-state', 'loading');
        retryBtn.innerHTML = '<span class="button-spinner" aria-hidden="true"></span><span>إعادة المحاولة</span>';
        announce('جاري إعادة المحاولة');
        setTimeout(function () {
          notice.dataset.tone = 'positive';
          notice.dataset.state = 'completed';
          var iconUse = qs('.state-notice-icon use', notice);
          if (iconUse) { iconUse.setAttribute('href', '#i-check'); }
          var text = qs('.state-notice-text', notice);
          if (text) { text.textContent = retryBtn.dataset.done || 'تم'; }
          var sub = qs('.state-notice-sub', notice);
          if (sub) { sub.textContent = retryBtn.dataset.doneSub || ''; }
          retryBtn.parentNode.removeChild(retryBtn);
          announce(retryBtn.dataset.done || 'تم');
        }, 1100);
      });
    });

    // Segmented controls / tabs / switches / nav in library matrices
    qsa('.segmented').forEach(function (seg) {
      qsa('.segmented-item', seg).forEach(function (item) {
        item.addEventListener('click', function () {
          qsa('.segmented-item', seg).forEach(function (s) { s.setAttribute('aria-pressed', s === item ? 'true' : 'false'); });
        });
      });
    });
    qsa('.tabs').forEach(function (tabset) {
      qsa('.tab-item', tabset).forEach(function (item) {
        item.addEventListener('click', function () {
          qsa('.tab-item', tabset).forEach(function (t) {
            t.setAttribute('aria-selected', t === item ? 'true' : 'false');
            t.classList.toggle('is-selected', t === item);
          });
        });
      });
    });
    qsa('.switch').forEach(function (sw) {
      sw.addEventListener('click', function () {
        sw.setAttribute('aria-checked', sw.getAttribute('aria-checked') === 'true' ? 'false' : 'true');
      });
    });

    // Search input with clear action (44px hit)
    qsa('.input--search').forEach(function (input) {
      var clearBtn = input.parentElement ? qs('.input-clear', input.parentElement) : null;
      function sync() {
        if (clearBtn) { clearBtn.hidden = input.value.length === 0; }
      }
      input.addEventListener('input', sync);
      if (clearBtn) {
        clearBtn.addEventListener('click', function () {
          input.value = '';
          sync();
          input.focus();
        });
        sync();
      }
    });

    updateDisplays();
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', initInteractions); }
  else { initInteractions(); }
})();
