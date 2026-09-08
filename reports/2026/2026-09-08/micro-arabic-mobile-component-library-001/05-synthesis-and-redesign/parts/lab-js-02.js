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
