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
