/* component-gallery.js — offline gallery behavior (repair run 20260908T222534Z-g53-5538).
   No dependencies, no network. Controls: viewport width, direction, text scale
   (100/130/200), motion. Interactions: six-state loading button with duplicate-
   submit guard, staged filter sheet (Apply/Reset/Cancel + drag-to-dismiss),
   select menus with Escape/outside close, segmented pill + sliding underline
   with arrow keys, summary metric with immediate numbers and moving bar, row
   wrap grid with directional chevron feedback, local row insert/remove with
   real undo, quick-action rail with pointer drag + snap, snackbars, error
   recovery near the control, focus management (trap + restore). */
(function () {
  "use strict";
  var root = document.documentElement;
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function on(el, ev, fn) { if (el) el.addEventListener(ev, fn); }
  function nextFrame(fn) { requestAnimationFrame(function () { requestAnimationFrame(fn); }); }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  var segPlacers = []; /* initialized before first setViewport call (R-08 fix) */

  /* ---------- header controls ---------- */
  function bindSeg(id, attr, apply) {
    var seg = $(id);
    if (!seg) return;
    var buttons = $$("button", seg);
    buttons.forEach(function (b) {
      on(b, "click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); x.setAttribute("aria-pressed", "false"); });
        b.classList.add("on");
        b.setAttribute("aria-pressed", "true");
        apply(b.getAttribute(attr), b);
      });
    });
    var initial = seg.querySelector("button.on");
    if (initial) initial.setAttribute("aria-pressed", "true");
  }

  var frameLabels = $$("[data-w-label]");
  function setViewport(vp) {
    root.style.setProperty("--frame-w", vp === "auto" ? "100%" : vp + "px");
    frameLabels.forEach(function (el) { el.textContent = vp === "auto" ? "auto" : vp; });
    placeAllSegs();
  }

  bindSeg("#ctrl-viewport", "data-vp", setViewport);
  bindSeg("#ctrl-dir", "data-dir", function (v) { root.setAttribute("dir", v); placeAllSegs(); });
  bindSeg("#ctrl-text", "data-text", function (v) {
    root.setAttribute("data-text-size", v);
    placeAllSegs();
  });
  bindSeg("#ctrl-motion", "data-motion", function (v) { root.setAttribute("data-motion", v); });
  setViewport("auto");

  /* ---------- evidence panel ---------- */
  var evPanel = $("#evidence-panel");
  var evBtn = $("#btn-evidence");
  function toggleEvidence(openState) {
    if (!evPanel) return;
    evPanel.hidden = !openState;
    if (evBtn) evBtn.setAttribute("aria-expanded", String(openState));
  }
  on(evBtn, "click", function () { toggleEvidence(evPanel.hidden); });
  on($("#btn-evidence-close"), "click", function () { toggleEvidence(false); });

  var RAMPS = {
    primary: ["#FAF9F5", "#F5F4ED", "#E8E6DC", "#D97757", "#C96442", "#141413"],
    accent: ["#FAF9F5", "#F5F4ED", "#D1CFC5", "#2C84DB", "#1490FF", "#141413"],
    positive: ["#FAF9F5", "#F5F4ED", "#E8E6DC", "#629987", "#4D4C48"],
    negative: ["#FAF9F5", "#F5F4ED", "#E8E6DC", "#B53333", "#3D3D3A"],
    operational: ["#FAF9F5", "#F5F4ED", "#E8E6DC", "#2C84DB", "#1490FF"],
    gold: ["#FAF9F5", "#F5F4ED", "#D1CFC5", "#4D4C48"]
  };
  $$("[data-ramp]").forEach(function (holder) {
    var vals = RAMPS[holder.getAttribute("data-ramp")] || [];
    vals.forEach(function (hex, i) {
      var s = document.createElement("span");
      s.style.background = hex;
      s.setAttribute("data-step", "role-" + String(i + 1));
      s.title = hex;
      holder.appendChild(s);
    });
  });

  /* ---------- overlay manager (motion + focus + scroll lock) ----------
     Corrected R-02/R-03/R-07: overlays really transition (240/180 sheet,
     160/120 dialog, 200 scrim), hidden really hides, focus restores to the
     trigger, and the page scroll locks while an overlay is open. */
  var overlayStack = []; /* [{el, kind, close}] — top = last */
  var bodyScrollLocked = false;
  function lockScroll(lock) {
    if (lock && !bodyScrollLocked) { root.style.overflow = "hidden"; bodyScrollLocked = true; }
    else if (!lock && bodyScrollLocked && overlayStack.length === 0) { root.style.overflow = ""; bodyScrollLocked = false; }
    else if (!lock && bodyScrollLocked) { /* keep locked while others open */ }
  }
  function focusables(el) {
    return $$("button, input, textarea, select, a[href]", el).filter(function (x) {
      return !x.disabled && x.offsetParent !== null;
    });
  }
  function firstFocusable(el) { return focusables(el)[0]; }

  function openOverlay(el, screen, opts) {
    opts = opts || {};
    if (!el || !screen) return null;
    var trigger = opts.trigger || null;
    /* mount the overlay + a scrim into the triggering screen (sheets, dialogs,
       and the shared scrim live in their home screen until invoked elsewhere) */
    if (el.parentElement !== screen) screen.appendChild(el);
    var scrim = screen.querySelector("[data-scrim]") || $("[data-scrim]");
    if (scrim && scrim.parentElement !== screen) screen.appendChild(scrim);
    if (el.hidden !== undefined) el.hidden = false;
    if (scrim) { scrim.hidden = false; nextFrame(function () { scrim.classList.add("is-open"); }); }
    nextFrame(function () { el.classList.add("is-open"); });
    lockScroll(true);
    var rec = { el: el, kind: opts.kind || "overlay", trigger: trigger, onAfterClose: opts.onAfterClose || null };
    rec.close = function () { closeOverlay(rec); };
    overlayStack.push(rec);
    var f = firstFocusable(el);
    if (f) setTimeout(function () { try { f.focus(); } catch (e) {} }, 60);
    return rec;
  }
  function closeOverlay(rec) {
    if (!rec || rec.closed) return;
    rec.closed = true;
    var idx = overlayStack.indexOf(rec);
    if (idx > -1) overlayStack.splice(idx, 1);
    var el = rec.el;
    var screen = el.closest(".screen");
    var scrim = screen ? screen.querySelector("[data-scrim]") : null;
    var isSheet = el.classList.contains("sheet");
    var isDialog = el.classList.contains("dialog") || el.classList.contains("dialog-anchor");
    var outMs = isSheet ? 180 : (isDialog ? 120 : 120);
    el.classList.remove("is-open", "is-expanded");
    el.style.transform = "";
    if (scrim) scrim.classList.remove("is-open");
    setTimeout(function () {
      el.hidden = true;
      if (scrim && overlayStack.length === 0) scrim.hidden = true;
    }, outMs + 40);
    lockScroll(false);
    /* corrected R-07: focus returns to the trigger that opened the overlay */
    if (rec.trigger && rec.trigger.focus) { try { rec.trigger.focus(); } catch (e) {} }
    if (rec.onAfterClose) rec.onAfterClose();
  }

  /* shared scrim click — closes the top overlay */
  $$("[data-scrim]").forEach(function (scrim) {
    on(scrim, "click", function () {
      var top = overlayStack[overlayStack.length - 1];
      if (top) top.close();
    });
  });

  /* ---------- generic sheet (Add record) ---------- */
  var sheet = $("[data-sheet]");
  $$("[data-open-sheet]").forEach(function (btn) {
    on(btn, "click", function () {
      var screen = btn.closest(".screen") || $("#overlays .screen");
      if (sheet) openOverlay(sheet, screen, { kind: "sheet", trigger: btn });
    });
  });
  $$("[data-sheet-close]").forEach(function (btn) {
    on(btn, "click", function () {
      var host = btn.closest(".sheet");
      var rec = overlayStack.filter(function (r) { return r.el === host; })[0];
      if (rec) rec.close();
    });
  });

  /* ---------- dialog (centered, scale in/out) ---------- */
  var dialogAnchor = $("[data-dialog-anchor]");
  $$("[data-open-dialog]").forEach(function (btn) {
    on(btn, "click", function () {
      var screen = btn.closest(".screen") || $("#overlays .screen");
      if (dialogAnchor) openOverlay(dialogAnchor, screen, { kind: "dialog", trigger: btn });
    });
  });
  if (dialogAnchor) {
    on(dialogAnchor, "click", function (e) {
      if (e.target !== dialogAnchor) return; /* click outside the card closes */
      var rec = overlayStack.filter(function (r) { return r.el === dialogAnchor; })[0];
      if (rec) rec.close();
    });
  }
  $$("[data-close-overlay]").forEach(function (btn) {
    on(btn, "click", function () {
      var top = overlayStack[overlayStack.length - 1];
      if (top) top.close();
    });
  });

  /* ---------- sheet drag-to-dismiss + expand snap (R-06/source port) ---------- */
  $$(".sheet").forEach(function (sh) {
    var handle = sh.querySelector("[data-sheet-drag]");
    if (!handle) return;
    var startY = 0, dy = 0, active = false;
    on(handle, "pointerdown", function (e) {
      if (sh.hidden) return;
      active = true; startY = e.clientY; dy = 0;
      sh.classList.add("is-dragging");
      try { handle.setPointerCapture(e.pointerId); } catch (err) {}
      e.preventDefault();
    });
    on(handle, "pointermove", function (e) {
      if (!active) return;
      dy = e.clientY - startY;
      var expanded = sh.classList.contains("is-expanded");
      var y = dy > 0 ? dy : (expanded ? dy : Math.max(dy, -44)); /* clamp up when collapsed */
      sh.style.transform = "translateY(" + Math.max(y, -44) + "px)";
    });
    function release() {
      if (!active) return;
      active = false;
      var expanded = sh.classList.contains("is-expanded");
      sh.classList.remove("is-dragging");
      if (dy > 130) {
        if (expanded) { sh.style.transform = ""; sh.classList.remove("is-expanded"); }
        else {
          /* dismiss from the dragged position */
          var rec = overlayStack.filter(function (r) { return r.el === sh; })[0];
          if (rec) rec.close(); else { sh.classList.remove("is-open"); sh.style.transform = ""; }
        }
      } else if (dy < -50 && !expanded) {
        sh.style.transform = "";
        sh.classList.add("is-expanded");
      } else {
        sh.style.transform = ""; /* spring back through the open transition */
      }
    }
    on(handle, "pointerup", release);
    on(handle, "pointercancel", release);
  });

  /* ---------- Escape + focus trap ---------- */
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      var top = overlayStack[overlayStack.length - 1];
      if (top) { top.close(); return; }
      if (menuState.open) closeMenu();
    }
    if (e.key === "Tab" && overlayStack.length) {
      var topEl = overlayStack[overlayStack.length - 1].el;
      var f = focusables(topEl);
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* ---------- menus (single-choice dropdowns) ---------- */
  var menuState = { open: false, field: null, trigger: null, menu: null };
  function closeMenu() {
    if (!menuState.open) return;
    var m = menuState.menu, t = menuState.trigger;
    if (m) { m.classList.remove("is-open"); setTimeout(function () { m.hidden = true; }, 130); }
    if (t) { t.setAttribute("aria-expanded", "false"); try { t.focus(); } catch (e) {} }
    menuState = { open: false, field: null, trigger: null, menu: null };
  }
  $$("[data-menu]").forEach(function (field) {
    var trigger = $(".input-select", field) || $(".sort-ctl", field);
    var menu = $(".menu", field);
    if (!trigger || !menu) return;
    on(trigger, "click", function () {
      if (menuState.menu === menu && menuState.open) { closeMenu(); return; }
      if (menuState.open) closeMenu();
      menu.hidden = false;
      nextFrame(function () { menu.classList.add("is-open"); });
      trigger.setAttribute("aria-expanded", "true");
      menuState = { open: true, field: field, trigger: trigger, menu: menu };
    });
    $$("button", menu).forEach(function (opt) {
      on(opt, "click", function () {
        $$("button", menu).forEach(function (o) {
          o.classList.remove("on"); o.setAttribute("aria-selected", "false");
        });
        opt.classList.add("on");
        opt.setAttribute("aria-selected", "true");
        var val = $(".sel-value", trigger);
        if (val) val.textContent = opt.textContent.replace(/\s+/g, " ").trim();
        if (opt.hasAttribute("data-sort")) applySort(opt.getAttribute("data-sort"));
        closeMenu();
      });
    });
  });
  document.addEventListener("click", function (e) {
    if (!menuState.open) return;
    if (menuState.field && menuState.field.contains(e.target)) return;
    closeMenu();
  });

  /* ---------- filter state machine (Repair C) ----------
     One Filter control + a staged sheet. Applied state filters and sorts the
     live list; staged edits commit on Apply and are discarded on Cancel,
     scrim, Escape, or drag-to-dismiss. */
  var ERAS = { any: 0, month: 1, week: 2, today: 3 };
  var DATE_LABELS = { any: "any time", today: "today", week: "this week", month: "this month" };
  var DEFAULTS = { status: [], date: "any", type: [] };
  var applied = { status: [], date: "any", type: [] };
  var staged = { status: [], date: "any", type: [] };

  var filterSheet = $("[data-filter-sheet]");
  var filterList = $("[data-filter-list]");
  var filterEmpty = $("[data-filter-empty]");
  var filterSummary = $("[data-filter-summary]");
  var filterCount = $("[data-filter-count]");
  var filterOpenBtn = $("[data-filter-open]");

  function cloneState(s) { return { status: s.status.slice(), date: s.date, type: s.type.slice() }; }
  function syncChips(state) {
    $$("[data-fgroup]").forEach(function (chip) {
      var g = chip.getAttribute("data-fgroup"), v = chip.getAttribute("data-fval");
      var isOn = g === "date" ? state.date === v : state[g].indexOf(v) > -1;
      chip.classList.toggle("on", isOn);
      if (chip.getAttribute("role") === "radio") chip.setAttribute("aria-checked", String(isOn));
      else chip.setAttribute("aria-pressed", String(isOn));
    });
  }
  function countActive(s) {
    return s.status.length + (s.date !== "any" ? 1 : 0) + s.type.length;
  }
  function labelize(list, cap) {
    var labels = list.map(function (v) {
      var chip = document.querySelector('[data-fgroup] [data-fval="' + v + '"]');
      return chip ? chip.textContent.trim() : v;
    });
    if (labels.length <= cap) return labels.join(" · ");
    return labels.slice(0, cap).join(" · ") + " +" + (labels.length - cap);
  }
  function applyFilters() {
    if (!filterList) return;
    var rows = $$(".row", filterList);
    var visible = 0;
    rows.forEach(function (r) {
      var okStatus = !applied.status.length || applied.status.indexOf(r.getAttribute("data-status")) > -1;
      var okType = !applied.type.length || applied.type.indexOf(r.getAttribute("data-type")) > -1;
      var okEra = (ERAS[r.getAttribute("data-era")] || 0) >= ERAS[applied.date];
      var show = okStatus && okType && okEra;
      r.hidden = !show;
      if (show) visible++;
    });
    if (filterEmpty) filterEmpty.hidden = visible !== 0;
    filterList.hidden = visible === 0;
    var n = countActive(applied);
    if (filterCount) {
      filterCount.hidden = n === 0;
      filterCount.textContent = String(n);
    }
    if (filterOpenBtn) filterOpenBtn.setAttribute("aria-expanded", "false");
    if (filterSummary) {
      var parts = [];
      if (applied.status.length) parts.push(labelize(applied.status, 2));
      if (applied.date !== "any") parts.push(DATE_LABELS[applied.date]);
      if (applied.type.length) parts.push(labelize(applied.type, 1));
      filterSummary.textContent = parts.length ? parts.join(" · ") : "All records · any time";
    }
  }
  function applySort(mode) {
    if (!filterList) return;
    var rows = $$(".row", filterList);
    rows.sort(function (a, b) {
      if (mode === "old") return (+b.getAttribute("data-order")) - (+a.getAttribute("data-order"));
      if (mode === "amount") return (+b.getAttribute("data-amount")) - (+a.getAttribute("data-amount"));
      return (+a.getAttribute("data-order")) - (+b.getAttribute("data-order"));
    });
    rows.forEach(function (r) { filterList.appendChild(r); });
  }
  /* sheet chip staging */
  $$("[data-fgroup]").forEach(function (chip) {
    on(chip, "click", function () {
      if (chip.disabled) return;
      var g = chip.getAttribute("data-fgroup"), v = chip.getAttribute("data-fval");
      if (g === "date") {
        staged.date = v;
      } else {
        var i = staged[g].indexOf(v);
        if (i > -1) staged[g].splice(i, 1); else staged[g].push(v);
      }
      syncChips(staged);
    });
  });
  on(filterOpenBtn, "click", function () {
    if (!filterSheet) return;
    staged = cloneState(applied); /* reopen preserves the applied selections */
    syncChips(staged);
    var screen = filterOpenBtn.closest(".screen");
    openOverlay(filterSheet, screen, {
      kind: "sheet", trigger: filterOpenBtn,
      onAfterClose: function () { filterOpenBtn.setAttribute("aria-expanded", "false"); }
    });
    filterOpenBtn.setAttribute("aria-expanded", "true");
  });
  on($("[data-filter-apply]"), "click", function () {
    applied = cloneState(staged);
    var rec = overlayStack.filter(function (r) { return r.el === filterSheet; })[0];
    if (rec) rec.close();
    applyFilters();
  });
  on($("[data-filter-reset]"), "click", function () {
    staged = cloneState(DEFAULTS);
    syncChips(staged);
  });
  $$("[data-filter-clear]").forEach(function (btn) {
    on(btn, "click", function () {
      applied = cloneState(DEFAULTS);
      staged = cloneState(DEFAULTS);
      syncChips(staged);
      applyFilters();
      /* BLK-01 fix: the snackbar ELEMENT is first, the target screen last */
      fireSnackbar(mainSnack, "Filters cleared", null, null, btn.closest(".screen"));
    });
  });
  applyFilters();

  /* ---------- snackbars (one at a time, per screen) ---------- */
  var snackTimers = new WeakMap();
  function fireSnackbar(snack, msg, actionLabel, onAction, screen) {
    if (!snack) return;
    var m = $(".snackbar-msg", snack);
    var act = $(".snackbar-action", snack);
    if (m) m.textContent = msg;
    if (screen && snack.parentElement !== screen) screen.appendChild(snack);
    if (act) {
      if (actionLabel) {
        act.hidden = false;
        act.textContent = actionLabel;
        act.onclick = function () {
          if (onAction) onAction();
          hideSnack(snack);
        };
      } else {
        act.hidden = true;
        act.onclick = null;
      }
    }
    snack.hidden = false;
    nextFrame(function () { snack.classList.add("is-open"); });
    var t = snackTimers.get(snack);
    if (t) clearTimeout(t);
    snackTimers.set(snack, setTimeout(function () { hideSnack(snack); }, 5000));
  }
  function hideSnack(snack) {
    if (!snack) return;
    var t = snackTimers.get(snack);
    if (t) clearTimeout(t);
    snack.classList.remove("is-open");
    setTimeout(function () { snack.hidden = true; }, 140);
  }
  var mainSnack = $("[data-snackbar]");
  $$("[data-fire-snackbar]").forEach(function (btn) {
    on(btn, "click", function () {
      fireSnackbar(mainSnack, "Record saved", null, null, btn.closest(".screen"));
    });
  });

  /* ---------- six-state loading button (Repair A) ---------- */
  $$("[data-loading-btn]").forEach(function (btn) {
    var label = $(".btn-label", btn);
    var iconSlot = $(".btn-icon", btn);
    var leadIcon = iconSlot ? $("svg.ic", iconSlot) : null;
    var spinner = iconSlot ? $(".spinner", iconSlot) : null;
    var check = $(".ic-check", btn);
    var busy = false;
    on(btn, "click", function () {
      if (busy) return; /* duplicate-submit guard */
      busy = true;
      btn.classList.add("is-loading");
      btn.disabled = true;
      btn.setAttribute("aria-busy", "true");
      if (leadIcon) leadIcon.hidden = true;   /* spinner takes the icon slot */
      if (spinner) spinner.hidden = false;    /* label persists; width stable */
      setTimeout(function () {
        btn.classList.remove("is-loading");
        if (spinner) spinner.hidden = true;
        btn.classList.add("btn-complete");
        if (check) check.hidden = false;
        if (label) label.textContent = "Saved";
        setTimeout(function () {
          btn.classList.remove("btn-complete");
          if (check) check.hidden = true;
          if (leadIcon) leadIcon.hidden = false;
          if (label) label.textContent = "Save";
          btn.disabled = false;
          btn.setAttribute("aria-busy", "false");
          busy = false;
          fireSnackbar(mainSnack, "Record saved", null, null, btn.closest(".screen"));
        }, 800);
      }, 1600);
    });
  });
  var completeDemo = $("[data-complete-demo]");
  on(completeDemo, "click", function () {
    fireSnackbar(mainSnack, "Already saved", null, null, completeDemo.closest(".screen"));
  });

  /* ---------- error recovery near the control (Repair G) ---------- */
  var recForm = $("[data-recovery-form]");
  on($("[data-recovery-save]"), "click", function () {
    if (!recForm) return;
    var btn = this;
    if (btn.disabled) return;
    var input = $("input", recForm);
    var err = $("[data-recovery-error]", recForm);
    var label = $(".btn-label", btn);
    var iconSlot = $(".btn-icon", btn);
    var leadIcon = iconSlot ? $("svg.ic", iconSlot) : null;
    var spinner = iconSlot ? $(".spinner", iconSlot) : null;
    var done = $(".ic-done", btn);
    var digits = input ? input.value.replace(/[^\d]/g, "") : "";
    if (!digits) {
      if (err) err.hidden = false;                    /* message at the control */
      if (input) { input.setAttribute("aria-invalid", "true"); input.focus(); }
      return;                                          /* input preserved as typed */
    }
    if (err) err.hidden = true;
    if (input) input.setAttribute("aria-invalid", "false");
    btn.disabled = true;
    btn.setAttribute("aria-busy", "true");
    btn.classList.add("is-loading");
    if (leadIcon) leadIcon.hidden = true;
    if (spinner) spinner.hidden = false;
    setTimeout(function () {
      btn.classList.remove("is-loading");
      if (spinner) spinner.hidden = true;
      btn.classList.add("btn-complete");
      if (done) done.hidden = false;
      if (label) label.textContent = "Saved";
      setTimeout(function () {
        btn.classList.remove("btn-complete");
        if (done) done.hidden = true;
        if (leadIcon) leadIcon.hidden = false;
        if (label) label.textContent = "Save entry";
        btn.disabled = false;
        btn.setAttribute("aria-busy", "false");
        fireSnackbar(mainSnack, "Entry saved", null, null, btn.closest(".screen"));
      }, 800);
    }, 900);
  });

  /* ---------- summary metric: bar moves, numbers land immediately ---------- */
  var METRIC_STATES = [
    { a: 620000, b: 230400 },
    { a: 470400, b: 380000 },
    { a: 696900, b: 153500 }
  ];
  var metricIdx = 0;
  function fmt(n) { return n.toLocaleString("en-US"); }
  on($("[data-metric-update]"), "click", function () {
    metricIdx = (metricIdx + 1) % METRIC_STATES.length;
    var s = METRIC_STATES[metricIdx];
    var total = s.a + s.b;
    var elA = $("[data-metric-a]"), elB = $("[data-metric-b]");
    var segA = $("[data-metric-seg-a]"), segB = $("[data-metric-seg-b]");
    var bar = $("[data-metric-bar]");
    /* final numbers appear immediately — never a count-up */
    if (elA) elA.textContent = fmt(s.a);
    if (elB) elB.textContent = fmt(s.b);
    var pa = (s.a / total) * 100, pb = 100 - pa;
    if (segA) segA.style.width = pa.toFixed(1) + "%"; /* 200ms width motion */
    if (segB) segB.style.width = pb.toFixed(1) + "%";
    if (bar) bar.setAttribute("aria-label",
      "Reserved " + fmt(s.a) + " of " + fmt(total) + " total; free " + fmt(s.b));
  });

  /* ---------- rows: chevron direction feedback ---------- */
  $$("[data-row-chev]").forEach(function (btn) {
    on(btn, "click", function () {
      var row = btn.closest(".row");
      if (!row) return;
      row.classList.add("chev-fire");
      setTimeout(function () { row.classList.remove("chev-fire"); }, 300);
    });
  });

  /* ---------- local row insert / remove with real undo (Repair G) ---------- */
  var manageList = $("[data-manage-list]");
  var manageSnack = $("[data-manage-snackbar]");
  var addCount = 0;
  var pendingRestore = null;
  on($("[data-add-row]"), "click", function () {
    if (!manageList) return;
    addCount++;
    var row = document.createElement("div");
    row.className = "row is-new";
    row.innerHTML =
      '<div class="row-tile t-op"><svg class="ic" aria-hidden="true"><use href="#i-receipt"/></svg></div>' +
      '<div class="row-main"><p class="row-title">Draft entry — new ' + addCount + '</p>' +
      '<p class="row-sub num" dir="ltr">17/07/2026 · 14:00</p></div>' +
      '<div class="row-trail"><p class="row-amt num op" dir="ltr">−60</p>' +
      '<button type="button" class="row-remove press" data-remove-row aria-label="Remove draft entry — new ' + addCount + '">' +
      '<svg class="ic" aria-hidden="true"><use href="#i-close"/></svg></button></div>';
    manageList.insertBefore(row, manageList.firstChild);
    bindRemove(row.querySelector("[data-remove-row]"));
    setTimeout(function () { row.classList.remove("is-new"); }, 700);
  });
  function bindRemove(btn) {
    on(btn, "click", function () {
      var row = btn.closest(".row");
      if (!row || row.classList.contains("is-removing")) return;
      var next = row.nextSibling;
      row.classList.add("is-removing");
      pendingRestore = { row: row, next: next };
      setTimeout(function () {
        if (row.parentNode) row.parentNode.removeChild(row);
        fireSnackbar(manageSnack, "Entry removed", "Undo", function () {
          if (pendingRestore) {
            var p = pendingRestore; pendingRestore = null;
            p.row.classList.remove("is-removing", "is-new");
            if (p.next && p.next.parentNode === manageList) manageList.insertBefore(p.row, p.next);
            else manageList.appendChild(p.row);
            fireSnackbar(manageSnack, "Entry restored");
          }
        }, btn.closest(".screen"));
      }, 200);
    });
  }
  $$("[data-remove-row]").forEach(bindRemove);

  /* ---------- quick action rail: pointer drag to scroll (touch is native) ---------- */
  $$("[data-rail]").forEach(function (rail) {
    var down = false, startX = 0, startScroll = 0, moved = false;
    on(rail, "pointerdown", function (e) {
      if (e.pointerType === "touch") return; /* native scroll + snap on touch */
      down = true; moved = false;
      startX = e.clientX; startScroll = rail.scrollLeft;
    });
    on(rail, "pointermove", function (e) {
      if (!down) return;
      var dx = e.clientX - startX;
      if (Math.abs(dx) > 4) moved = true;
      rail.scrollLeft = startScroll - dx;
    });
    on(rail, "pointerup", function () { down = false; });
    on(rail, "pointerleave", function () { down = false; });
    on(rail, "click", function (e) {
      if (moved) { e.preventDefault(); e.stopPropagation(); } /* tap vs drag */
      moved = false;
    });
  });

  /* ---------- segmented controls: pill thumb + sliding underline + arrows ---------- */
  $$("[data-seg]").forEach(function (seg) {
    var thumb = $(".segctl-thumb", seg);
    var buttons = $$("button", seg);
    function place() {
      var activeBtn = seg.querySelector("button.on");
      if (!activeBtn || !thumb) return;
      var segRect = seg.getBoundingClientRect();
      var onRect = activeBtn.getBoundingClientRect();
      var start = onRect.left - segRect.left;
      if (getComputedStyle(root).direction === "rtl") start = segRect.right - onRect.right;
      thumb.style.width = onRect.width + "px";
      thumb.style.insetInlineStart = start + "px";
      thumb.hidden = false;
    }
    segPlacers.push(place);
    function activate(b) {
      buttons.forEach(function (x) {
        x.classList.remove("on");
        x.setAttribute("aria-checked", "false");
      });
      b.classList.add("on");
      b.setAttribute("aria-checked", "true");
      place();
    }
    buttons.forEach(function (b) { on(b, "click", function () { activate(b); }); });
    on(seg, "keydown", function (e) {
      var idx = buttons.indexOf(seg.querySelector("button.on"));
      var nextIdx = null;
      var rtl = getComputedStyle(root).direction === "rtl";
      if (e.key === (rtl ? "ArrowLeft" : "ArrowRight")) nextIdx = Math.min(idx + 1, buttons.length - 1);
      if (e.key === (rtl ? "ArrowRight" : "ArrowLeft")) nextIdx = Math.max(idx - 1, 0);
      if (nextIdx !== null && idx !== nextIdx) { e.preventDefault(); activate(buttons[nextIdx]); }
    });
    window.addEventListener("resize", place);
    place();
  });
  $$("[data-seg-lines]").forEach(function (seg) {
    var indicator = $(".segctl-indicator", seg);
    var buttons = $$("button", seg);
    function place() {
      var activeBtn = seg.querySelector("button.on");
      if (!activeBtn || !indicator) return;
      var segRect = seg.getBoundingClientRect();
      var onRect = activeBtn.getBoundingClientRect();
      var start = onRect.left - segRect.left;
      if (getComputedStyle(root).direction === "rtl") start = segRect.right - onRect.right;
      indicator.style.width = onRect.width + "px";
      indicator.style.insetInlineStart = start + "px";
      indicator.hidden = false;
    }
    segPlacers.push(place);
    function activate(b) {
      buttons.forEach(function (x) {
        x.classList.remove("on");
        x.setAttribute("aria-selected", "false");
      });
      b.classList.add("on");
      b.setAttribute("aria-selected", "true");
      place();
    }
    buttons.forEach(function (b) { on(b, "click", function () { activate(b); }); });
    on(seg, "keydown", function (e) {
      var idx = buttons.indexOf(seg.querySelector("button.on"));
      var nextIdx = null;
      var rtl = getComputedStyle(root).direction === "rtl";
      if (e.key === (rtl ? "ArrowLeft" : "ArrowRight")) nextIdx = Math.min(idx + 1, buttons.length - 1);
      if (e.key === (rtl ? "ArrowRight" : "ArrowLeft")) nextIdx = Math.max(idx - 1, 0);
      if (nextIdx !== null && idx !== nextIdx) { e.preventDefault(); activate(buttons[nextIdx]); }
    });
    window.addEventListener("resize", place);
    place();
  });
  function placeAllSegs() { segPlacers.forEach(function (p) { p(); }); }

  /* ---------- search clear ---------- */
  $$("input[type=search]").forEach(function (input) {
    var wrap = input.closest(".search-wrap");
    var clear = wrap ? $(".clear-btn", wrap) : null;
    function refresh() { if (clear) clear.hidden = !input.value; }
    on(input, "input", refresh);
    if (clear) on(clear, "click", function () {
      input.value = ""; refresh(); input.focus();
    });
    refresh();
  });

  /* ---------- amount live grouping ---------- */
  $$("input.input-amount").forEach(function (input) {
    on(input, "input", function () {
      var digits = input.value.replace(/[^\d]/g, "").slice(0, 12);
      input.value = digits ? digits.replace(/\B(?=(\d{3})+(?!\d))/g, ",") : "";
    });
  });

  /* ---------- retry ---------- */
  $$("[data-retry]").forEach(function (btn) {
    var busy = false;
    on(btn, "click", function () {
      if (busy) return;
      busy = true;
      var original = btn.textContent;
      btn.textContent = "Retrying";
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = original;
        btn.disabled = false;
        busy = false;
        fireSnackbar(mainSnack, "Connection restored — records loaded", null, null, btn.closest(".screen"));
      }, 1400);
    });
  });

  /* ---------- bottom nav switching ---------- */
  $$("[data-nav]").forEach(function (item) {
    on(item, "click", function () {
      var nav = item.closest(".bottomnav");
      if (!nav) return;
      $$("[data-nav]", nav).forEach(function (x) {
        x.classList.remove("on");
        x.removeAttribute("aria-current");
      });
      item.classList.add("on");
      item.setAttribute("aria-current", "page");
    });
  });

})();
