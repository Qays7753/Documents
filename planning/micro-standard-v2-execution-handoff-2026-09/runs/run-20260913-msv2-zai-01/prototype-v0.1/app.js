/* app.js — Micro Standard v2 Prototype v0.1 (run run-20260913-msv2-zai-01).
   Local demonstration interactions only: scene switching, viewport/motion
   controls, loading + quiet completion, chart state cycling, sheets, dialogs,
   FAB sheet, overflow menu, bottom nav, snackbars. No product logic, no data,
   no network. */
(function () {
  "use strict";
  var root = document.documentElement;
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function on(el, ev, fn) { if (el) el.addEventListener(ev, fn); }

  /* ---------- header controls ---------- */
  function bindSeg(id, attr, apply) {
    var seg = $(id);
    if (!seg) return;
    var buttons = $$("button", seg);
    buttons.forEach(function (b) {
      on(b, "click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        apply(b.getAttribute(attr));
      });
    });
  }
  bindSeg("#ctrl-viewport", "data-vp", function (v) {
    root.style.setProperty("--frame-w", v + "px");
  });
  bindSeg("#ctrl-motion", "data-motion", function (v) {
    root.setAttribute("data-motion", v);
  });

  /* ---------- scene switching ---------- */
  $$("[data-scene]").forEach(function (chip) {
    on(chip, "click", function () {
      var name = chip.getAttribute("data-scene");
      $$(".scene-chip").forEach(function (c) { c.classList.remove("on"); });
      chip.classList.add("on");
      $$(".scene").forEach(function (s) { s.classList.remove("is-active"); });
      var target = $("#scene-" + name);
      if (target) {
        target.classList.add("is-active");
        var body = $(".scene-body", target);
        if (body) body.scrollTop = 0;
        placeSegs(target);
      }
    });
  });

  /* ---------- segmented controls (pill thumb + underline) ---------- */
  var segPlacers = [];
  function placeSegs(ctx) { (segPlacers || []).forEach(function (fn) { fn(ctx); }); }
  function setupThumb(container, thumbSel, btnSel) {
    var thumb = $(thumbSel, container);
    var buttons = $$(btnSel, container);
    if (!thumb || !buttons.length) return;
    function move(active) {
      thumb.hidden = false;
      thumb.style.insetInlineStart = active.offsetLeft + "px";
      thumb.style.width = active.offsetWidth + "px";
    }
    buttons.forEach(function (b) {
      on(b, "click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); x.setAttribute("aria-checked", "false"); x.setAttribute("aria-selected", "false"); });
        b.classList.add("on");
        b.setAttribute("aria-checked", "true");
        b.setAttribute("aria-selected", "true");
        move(b);
      });
    });
    segPlacers.push(function (ctx) {
      var active = $("button.on", container);
      if (active && (!ctx || containerWithin(ctx, container))) move(active);
    });
    var init = $("button.on", container);
    if (init) requestAnimationFrame(function () { move(init); });
  }
  function containerWithin(ctx, el) { return !ctx || ctx === el || el.contains(ctx) || ctx.contains(el); }
  $$("[data-seg]").forEach(function (c) { setupThumb(c, ".segctl-thumb", "button"); });
  $$("[data-seg-lines]").forEach(function (c) { setupThumb(c, ".segctl-indicator", "button"); });

  /* ---------- overlay manager (focus + escape + scrim) ---------- */
  var overlayStack = [];
  function openOverlay(el, anchor) {
    if (!el) return;
    var trigger = document.activeElement;
    el.hidden = false;
    if (anchor) anchor.hidden = false;
    requestAnimationFrame(function () {
      el.classList.add("is-open");
      if (anchor) anchor.classList.add("is-open");
    });
    var scrim = el.closest(".scene-body") ? $("[data-scrim]", el.closest(".scene-body")) : null;
    if (scrim) { scrim.hidden = false; requestAnimationFrame(function () { scrim.classList.add("is-open"); }); }
    overlayStack.push({ el: el, anchor: anchor || null, scrim: scrim, trigger: trigger });
    var f = $("button, input, [href]", el);
    if (f) setTimeout(function () { try { f.focus(); } catch (e) {} }, 80);
  }
  function closeTop() {
    var rec = overlayStack.pop();
    if (!rec) return;
    rec.el.classList.remove("is-open");
    if (rec.anchor) rec.anchor.classList.remove("is-open");
    if (rec.scrim) rec.scrim.classList.remove("is-open");
    setTimeout(function () {
      rec.el.hidden = true;
      if (rec.anchor) rec.anchor.hidden = true;
      if (rec.scrim) rec.scrim.hidden = true;
      if (rec.trigger && rec.trigger.focus) { try { rec.trigger.focus(); } catch (e) {} }
    }, 200);
  }
  on(document, "keydown", function (e) {
    if (e.key === "Escape" && overlayStack.length) closeTop();
  });

  /* sheets */
  $$("[data-open-sheet]").forEach(function (btn) {
    on(btn, "click", function () {
      var body = btn.closest(".scene-body");
      var sheet = $("[data-sheet]", body);
      var scrim = $("[data-scrim]", body);
      if (sheet) openOverlay(sheet, null);
    });
  });
  $$("[data-sheet-close]").forEach(function (btn) {
    on(btn, "click", function () { if (overlayStack.length) closeTop(); });
  });
  /* dialogs */
  $$("[data-open-dialog]").forEach(function (btn) {
    on(btn, "click", function () {
      var id = btn.getAttribute("data-open-dialog");
      var anchor = $('[data-dialog-anchor="' + id + '"]');
      var dialog = $(".dialog", anchor);
      if (anchor && dialog) openOverlay(dialog, anchor);
    });
  });
  $$("[data-close-overlay]").forEach(function (btn) {
    on(btn, "click", function () { if (overlayStack.length) closeTop(); });
  });
  /* scrim click closes top overlay */
  $$("[data-scrim]").forEach(function (scrim) {
    on(scrim, "click", function () { if (overlayStack.length) closeTop(); });
  });
  /* FAB opens the add sheet (create flow) */
  $$("[data-open-fab]").forEach(function (fab) {
    on(fab, "click", function () {
      var scene = fab.closest(".scene");
      /* create = clay identity action; open the overflow/add sheet on the rows
         scene is a product decision, so here the FAB demo opens a create sheet */
      var sheet = $(".sheet[data-sheet]", $("#scene-rows"));
      if (sheet) {
        /* switch to rows scene so the sheet has a home, then open it */
        var chip = $('[data-scene="rows"]');
        if (chip) chip.click();
        setTimeout(function () {
          var body = $(".scene-body", $("#scene-rows"));
          openOverlay(sheet, null);
        }, 60);
      }
    });
  });
  /* overflow menu on a row */
  $$("[data-open-overflow]").forEach(function (btn) {
    on(btn, "click", function () {
      var body = btn.closest(".scene-body");
      var sheet = $("[data-sheet]", body);
      if (sheet) openOverlay(sheet, null);
    });
  });

  /* ---------- snackbars ---------- */
  function fireSnackbar(container, msg) {
    var sn = $("[data-snackbar]", container);
    if (!sn) return;
    var msgEl = $(".snackbar-msg", sn);
    if (msgEl) msgEl.textContent = msg;
    sn.hidden = false;
    requestAnimationFrame(function () { sn.classList.add("is-open"); });
    setTimeout(function () {
      sn.classList.remove("is-open");
      setTimeout(function () { sn.hidden = true; }, 250);
    }, 3200);
  }

  /* ---------- loading + quiet completion ---------- */
  function wireLoading(btn) {
    var label = $(".btn-label", btn);
    var iconSlot = $(".btn-icon", btn);
    var leadIcon = iconSlot ? $("svg.ic", iconSlot) : null;
    var spinner = iconSlot ? $(".spinner", iconSlot) : null;
    var check = $(".ic-check", btn);
    var original = label ? label.textContent : "حفظ";
    var busy = false;
    on(btn, "click", function () {
      if (busy) return; /* duplicate-submit guard */
      busy = true;
      btn.classList.add("is-loading");
      btn.disabled = true;
      btn.setAttribute("aria-busy", "true");
      if (leadIcon) leadIcon.hidden = true;
      if (spinner) spinner.hidden = false;
      setTimeout(function () {
        btn.classList.remove("is-loading");
        if (spinner) spinner.hidden = true;
        btn.classList.add("btn-complete");
        if (check) check.hidden = false;
        if (label) label.textContent = "تم الحفظ";
        var scene = btn.closest(".scene-body") || btn.closest(".scene");
        setTimeout(function () {
          btn.classList.remove("btn-complete");
          if (check) check.hidden = true;
          if (leadIcon) leadIcon.hidden = false;
          if (label) label.textContent = original;
          btn.disabled = false;
          btn.setAttribute("aria-busy", "false");
          busy = false;
          if (scene) fireSnackbar(scene, "تم حفظ القيد");
        }, 1100);
      }, 1500);
    });
  }
  $$("[data-loading-btn]").forEach(wireLoading);
  $$("[data-full-cycle]").forEach(wireLoading);

  /* ---------- question-led chart states ---------- */
  var chartStates = ["data", "zero", "nodata", "loading"];
  var chartIdx = 0;
  var chartCycle = $("[data-chart-cycle]");
  on(chartCycle, "click", function () {
    chartIdx = (chartIdx + 1) % chartStates.length;
    var name = chartStates[chartIdx];
    var body = $("[data-chart-body]");
    if (!body) return;
    $$("[data-chart-state]", body).forEach(function (el) {
      var st = el.getAttribute("data-chart-state");
      var visible = (st === "zero-alt") ? (name === "zero") : (st === name);
      el.hidden = !visible;
    });
    var q = $("[data-chart-question]");
    if (q) q.textContent = name === "nodata" ? "ماذا يحدث في هذه الفترة؟" : "أي يوم كان الأقوى هذا الأسبوع؟";
  });

  /* ---------- bottom nav switching (per scene) ---------- */
  $$("nav.bottomnav").forEach(function (nav) {
    $$(".navitem", nav).forEach(function (item) {
      on(item, "click", function () {
        $$(".navitem", nav).forEach(function (x) { x.classList.remove("on"); x.removeAttribute("aria-current"); });
        item.classList.add("on");
        item.setAttribute("aria-current", "page");
      });
    });
  });
})();
