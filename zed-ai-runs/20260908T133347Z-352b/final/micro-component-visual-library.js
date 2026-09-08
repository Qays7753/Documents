/* ==========================================================================
   MICRO COMPONENT VISUAL LIBRARY — micro-component-visual-library.js
   Lab engine: view switching, review controls, sheet/dialog engine with
   focus return + drag dismissal, live operational demos (loading → quiet
   completion → immediate final values, never count-up), verification-frame
   cloning and runtime audits. Vanilla JS, no dependencies, no network.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var MINUS = "\u2212"; // U+2212 — primary financial-direction signal

  /* ---------------------------------------------------------------- helpers */
  function fmt(n) {
    var sign = n < 0 ? MINUS : "";
    var abs = Math.abs(n);
    var parts = abs.toFixed(3).split(".");
    var int = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return sign + int + "." + parts[1];
  }
  function parseNum(text) {
    var clean = String(text).replace(/,/g, "").replace(/\u2212/g, "-").trim();
    var v = parseFloat(clean);
    return isNaN(v) ? 0 : v;
  }
  function announce(scope, message) {
    var live = (scope && scope.querySelector('[role="status"][aria-live]')) || document.getElementById("liveRegion");
    if (live) { live.textContent = message; }
  }
  function setBtnState(btn, state, labelHTML) {
    if (!btn.dataset.origHTML) { btn.dataset.origHTML = btn.innerHTML; }
    btn.dataset.state = state;
    if (state === "loading") {
      btn.innerHTML = '<span class="mc-spinner" aria-hidden="true"></span>' + labelHTML;
      btn.setAttribute("aria-disabled", "true");
      btn.setAttribute("tabindex", "-1");
    } else if (state === "completed") {
      btn.innerHTML = '<svg class="mc-icon mc-icon-20" aria-hidden="true"><use href="#i-check"/></svg>' + labelHTML;
      btn.setAttribute("aria-disabled", "true");
    } else {
      btn.innerHTML = btn.dataset.origHTML;
      btn.removeAttribute("data-state");
      btn.removeAttribute("aria-disabled");
      btn.removeAttribute("tabindex");
    }
  }

  /* ---------------------------------------------------------- view switching */
  var stage = document.getElementById("labStage");
  var stageSingle = document.getElementById("stageSingle");
  var stageVerify = document.getElementById("stageVerify");
  var phoneScreen = document.getElementById("phoneScreen");
  var clonesBuilt = false;

  function closeOverlays(scope) {
    $$(".mc-sheet.is-open, .mc-dialog.is-open", scope).forEach(closeOverlay);
  }

  function switchView(name) {
    var isVerify = name === "verification";
    if (isVerify) {
      buildClones();
      requestAnimationFrame(function () { runAudits(); });
    }
    if (stage) { stage.dataset.stage = isVerify ? "verify" : "single"; }
    if (stageSingle) { stageSingle.hidden = isVerify; }
    if (stageVerify) { stageVerify.hidden = !isVerify; }
    $$(".view", phoneScreen).forEach(function (v) {
      v.hidden = v.dataset.viewPanel !== name;
    });
    if (!isVerify) { closeOverlays(phoneScreen); }
    var scroller = phoneScreen ? phoneScreen.querySelector(".phone-scroll") : null;
    if (scroller) { scroller.scrollTop = 0; }
  }

  $$(".lab-tab").forEach(function (tab) {
    tab.addEventListener("click", function () {
      $$(".lab-tab").forEach(function (t) {
        t.classList.toggle("is-active", t === tab);
        t.setAttribute("aria-selected", t === tab ? "true" : "false");
      });
      switchView(tab.dataset.view);
    });
  });
  switchView("foundation");

  /* -------------------------------------------------------- review controls */
  function wireSeg(control, onPick) {
    var seg = (typeof control === "string") ? $('[data-control="' + control + '"]') : control;
    if (!seg) { return; }
    $$("button", seg).forEach(function (btn) {
      btn.addEventListener("click", function () {
        $$("button", seg).forEach(function (b) {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        onPick(btn);
      });
    });
  }

  wireSeg("dir", function (btn) {
    document.documentElement.setAttribute("dir", btn.dataset.dir);
    var label = document.getElementById("phoneDirLabel");
    if (label) { label.textContent = btn.dataset.dir === "rtl" ? "من اليمين" : "من اليسار"; }
  });

  wireSeg("scale", function (btn) {
    document.documentElement.setAttribute("data-text-scale", btn.dataset.scale);
    if (stage && stage.dataset.stage === "verify") { requestAnimationFrame(runAudits); }
  });

  wireSeg("motion", function (btn) {
    document.documentElement.setAttribute("data-motion", btn.dataset.motion);
  });

  var phoneFrame = document.getElementById("phoneFrame");
  var phoneWidthLabel = document.getElementById("phoneWidthLabel");
  wireSeg("width", function (btn) {
    if (phoneFrame) { phoneFrame.dataset.w = btn.dataset.width; }
    if (phoneWidthLabel) { phoneWidthLabel.textContent = btn.dataset.width; }
  });

  /* honor the system preference unless the reviewer explicitly chose */
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.documentElement.setAttribute("data-motion", "reduced");
    $$('[data-control="motion"] button').forEach(function (b) {
      var on = b.dataset.motion === "reduced";
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  /* ------------------------------------------------------ sheet & dialog */
  var lastFocused = null;

  function findOverlay(trigger, name, kind) {
    /* overlays live at phone-screen level (one set per screen), so a
       trigger from ANY view opens the same overlay in its own screen */
    var screen = trigger.closest(".phone-screen");
    var scope = screen || document;
    var sel = '[' + (kind === "dialog" ? "data-dialog" : "data-sheet") + '="' + name + '"]';
    return $(sel, scope);
  }

  function openOverlay(overlay, kind) {
    if (!overlay) { return; }
    lastFocused = document.activeElement;
    var name = kind === "dialog" ? overlay.dataset.dialog : overlay.dataset.sheet;
    var screen = overlay.closest(".phone-screen") || document.body;
    var scrim = $('[data-scrim-for="' + name + '"]', screen);
    overlay.hidden = false;
    if (scrim) { scrim.hidden = false; }
    /* force reflow so the transition runs after unhide */
    void overlay.offsetHeight;
    requestAnimationFrame(function () {
      overlay.classList.add("is-open");
      if (scrim) { scrim.classList.add("is-open"); }
    });
    var focusables = $$('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])', overlay)
      .filter(function (el) { return !el.disabled && el.offsetParent !== null; });
    /* focus the first data-entry field, not the close affordance */
    var field = focusables.filter(function (el) { return /^(INPUT|SELECT|TEXTAREA)$/.test(el.tagName); })[0];
    if (field) { field.focus(); }
    else if (focusables.length) { focusables[0].focus(); }
    overlay.__scrim = scrim;
  }

  function closeOverlay(overlay) {
    if (!overlay) { return; }
    var scrim = overlay.__scrim;
    overlay.classList.remove("is-open");
    if (scrim) { scrim.classList.remove("is-open"); }
    var isDialog = overlay.hasAttribute("data-dialog");
    var dur = isDialog ? 120 : 180;
    window.setTimeout(function () {
      overlay.hidden = true;
      if (scrim) { scrim.hidden = true; }
    }, dur + 20);
    if (lastFocused && document.contains(lastFocused)) { lastFocused.focus(); }
    lastFocused = null;
  }

  /* event delegation — works in the main frame AND in verification clones */
  document.addEventListener("click", function (ev) {
    var el;

    el = ev.target.closest("[data-sheet-open]");
    if (el) {
      openOverlay(findOverlay(el, el.dataset.sheetOpen, "sheet"), "sheet");
      return;
    }

    el = ev.target.closest("[data-dialog-open]");
    if (el) { openOverlay(findOverlay(el, el.dataset.dialogOpen, "dialog"), "dialog"); return; }

    el = ev.target.closest("[data-close]");
    if (el) {
      var overlay = el.closest(".mc-sheet, .mc-dialog");
      if (overlay) { closeOverlay(overlay); }
      return;
    }

    el = ev.target.closest("[data-scrim-for]");
    if (el && el.classList.contains("is-open")) {
      var name = el.dataset.scrimFor;
      var scope = el.closest(".phone-screen") || document;
      closeOverlay($('.mc-sheet[data-sheet="' + name + '"].is-open, .mc-dialog[data-dialog="' + name + '"].is-open', scope));
      return;
    }

    /* bottom navigation (demo state switching) */
    el = ev.target.closest(".mc-nav-item");
    if (el) {
      var nav = el.closest(".mc-bottomnav");
      if (nav) {
        $$(".mc-nav-item", nav).forEach(function (item) {
          var active = item === el;
          item.classList.toggle("is-active", active);
          if (active) { item.setAttribute("aria-current", "page"); }
          else { item.removeAttribute("aria-current"); }
        });
      }
      return;
    }

    /* segmented control + tabs (generic, demo-level) */
    el = ev.target.closest("[data-segmented] button, [data-tabs] button");
    if (el) {
      var group = el.parentElement;
      $$("button", group).forEach(function (b) {
        var active = b === el;
        b.classList.toggle("is-active", active);
        if (b.getAttribute("role") === "radio") { b.setAttribute("aria-checked", active ? "true" : "false"); }
        if (b.getAttribute("role") === "tab") { b.setAttribute("aria-selected", active ? "true" : "false"); }
      });
      return;
    }

    handleDemo(ev.target);
  });

  /* Escape closes the topmost overlay; Tab is trapped inside open overlays */
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") {
      var open = $(".mc-sheet.is-open, .mc-dialog.is-open");
      if (open) { closeOverlay(open); }
      return;
    }
    if (ev.key === "Tab") {
      var overlay = ev.target.closest(".mc-sheet.is-open, .mc-dialog.is-open");
      if (!overlay) { return; }
      var focusables = $$('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])', overlay)
        .filter(function (el) { return !el.disabled && el.offsetParent !== null; });
      if (!focusables.length) { return; }
      var first = focusables[0], last = focusables[focusables.length - 1];
      if (ev.shiftKey && document.activeElement === first) { ev.preventDefault(); last.focus(); }
      else if (!ev.shiftKey && document.activeElement === last) { ev.preventDefault(); first.focus(); }
    }
  });

  /* drag-to-dismiss on the sheet grabber */
  document.addEventListener("pointerdown", function (ev) {
    var grab = ev.target.closest("[data-grab]");
    if (!grab) { return; }
    var sheet = grab.closest(".mc-sheet");
    if (!sheet || !sheet.classList.contains("is-open")) { return; }
    ev.preventDefault();
    var startY = ev.clientY;
    var dy = 0;
    sheet.classList.add("is-dragging");
    function onMove(e) {
      dy = Math.max(0, e.clientY - startY);
      sheet.style.transform = "translateY(" + dy + "px)";
    }
    function onUp() {
      document.removeEventListener("pointermove", onMove);
      document.removeEventListener("pointerup", onUp);
      sheet.classList.remove("is-dragging");
      sheet.style.transform = "";
      if (dy > 100) { closeOverlay(sheet); }
    }
    document.addEventListener("pointermove", onMove);
    document.addEventListener("pointerup", onUp);
  });

  /* --------------------------------------------------------------- demos */
  function handleDemo(target) {
    var btn = target.closest("[data-demo]");
    if (!btn) { return; }
    var demo = btn.dataset.demo;
    if (demo === "cycle-primary") { cyclePrimary(btn); }
    else if (demo === "retry-ops") { retryOps(btn); }
    else if (demo === "confirm-cancel") { confirmCancel(btn); }
    else if (demo.indexOf("save-") === 0) { runSave(btn, demo); }
  }

  function cyclePrimary(btn) {
    if (btn.dataset.state) { return; }
    setBtnState(btn, "loading", "جارٍ الحفظ…");
    window.setTimeout(function () {
      setBtnState(btn, "completed", "تم الحفظ");
      window.setTimeout(function () { setBtnState(btn, "default"); }, 1400);
    }, 1000);
  }

  function retryOps(btn) {
    var panel = btn.closest("[data-demo-panel='ops-loader']");
    if (!panel) { return; }
    var result = panel.parentElement.querySelector("[data-ops-result]");
    /* the error card IS the panel: one automatic attempt already failed;
       this click is the manual retry, so the error card steps aside */
    panel.hidden = true;
    if (result) {
      result.hidden = false;
      result.innerHTML =
        '<li class="mc-skeleton-row"><span class="sk sk-ic"></span><span class="sk sk-line"></span><span class="sk sk-amount"></span></li>' +
        '<li class="mc-skeleton-row"><span class="sk sk-ic"></span><span class="sk sk-line"></span><span class="sk sk-amount"></span></li>' +
        '<li class="mc-skeleton-row"><span class="sk sk-ic"></span><span class="sk sk-line"></span><span class="sk sk-amount"></span></li>';
      window.setTimeout(function () {
        result.innerHTML =
          opRowHTML("i-banknote", "تحصيل من مطعم الديرة", "سداد كامل · فاتورة " + wrapNum("05/09/2026"), "+762.400", "") +
          opRowHTML("i-wallet", "شراء مستلزمات نظافة", "مصروف · تصنيف تشغيلية", MINUS + "64.250", "") +
          opRowHTML("i-package", "شراء من مؤسسة الأمل", "12 صنفًا · دفعة نقدية", MINUS + "128.000", "");
      }, 1300);
    }
  }

  function confirmCancel(btn) {
    var overlay = btn.closest(".mc-dialog");
    closeOverlay(overlay);
    var screen = btn.closest(".phone-screen");
    var row = screen ? screen.querySelector('[data-op="purchase-invoice"]') : null;
    if (row) {
      row.classList.add("is-cancelled");
      var label = row.querySelector("[data-op-state-label]");
      if (label) {
        label.innerHTML = 'معلَّمة: <span class="mc-op-status mc-op-status--pending"><svg class="mc-icon mc-icon-16" aria-hidden="true"><use href="#i-x"/></svg><span>ملغاة</span></span> — يمكن عكسها لاحقًا';
      }
    }
    announce(screen, "أُلغيت فاتورة الشراء بمبلغ 95.000 د.أ");
  }

  function wrapNum(s) { return '<bdi dir="ltr">' + s + "</bdi>"; }

  function opRowHTML(icon, title, qualifier, amount, time) {
    return (
      '<li><button type="button" class="mc-operational-row">' +
      '<span class="mc-op-ic"><svg class="mc-icon mc-icon-20" aria-hidden="true"><use href="#' + icon + '"/></svg></span>' +
      '<span class="mc-op-main"><span class="mc-op-title-text">' + title + "</span>" +
      '<span class="mc-op-qualifier">' + qualifier + "</span></span>" +
      '<span class="mc-op-side"><span class="mc-op-amount">' + wrapNum(amount) + '<span class="mc-op-unit">د.أ</span></span>' +
      (time ? '<span class="mc-op-time">' + wrapNum(time) + "</span>" : '<span class="mc-op-time">الآن</span>') +
      "</span></button></li>"
    );
  }

  function readAmount(sheet) {
    var input = sheet ? sheet.querySelector("[data-amount-input]") : null;
    if (!input) { return null; }
    var v = parseNum(input.value);
    return v > 0 ? v : null;
  }

  function updateMetric(screen, key, value) {
    var el = screen.querySelector('[data-metric="' + key + '"]');
    if (el) { el.textContent = fmt(value); }
  }

  function updateCash(screen, delta) {
    var el = screen.querySelector("[data-amount]");
    if (el) {
      var current = parseNum(el.textContent);
      el.textContent = fmt(current + delta);
    }
  }

  function prependRow(screen, html) {
    var list = screen ? screen.querySelector("[data-op-list]") : null;
    if (list) { list.insertAdjacentHTML("afterbegin", html); }
  }

  var SAVE_DEMOS = {
    "save-expense": function (screen, amount) {
      updateMetric(screen, "expenses", parseNum(getMetricText(screen, "expenses")) - amount);
      updateCash(screen, -amount);
      prependRow(screen, opRowHTML("i-wallet", "مصروف نقدي", "تصنيف تشغيلية", MINUS + fmt(amount), ""));
      return "تم حفظ المصروف · " + fmt(amount) + " د.أ";
    },
    "save-collect": function (screen, amount) {
      updateMetric(screen, "collections", parseNum(getMetricText(screen, "collections")) + amount);
      updateMetric(screen, "receivables", parseNum(getMetricText(screen, "receivables")) - amount);
      updateCash(screen, amount);
      prependRow(screen, opRowHTML("i-banknote", "تحصيل من خالد الحوراني", "دفعة جزئية", "+" + fmt(amount), ""));
      return "تم التحصيل · " + fmt(amount) + " د.أ";
    },
    "save-sale": function (screen, amount) {
      updateMetric(screen, "sales", parseNum(getMetricText(screen, "sales")) + amount);
      updateCash(screen, amount);
      prependRow(screen, opRowHTML("i-receipt", "بيع نقدي", "فاتورة جديدة", "+" + fmt(amount), ""));
      return "تم حفظ البيع · " + fmt(amount) + " د.أ";
    },
    "save-purchase": function (screen, amount) {
      updateCash(screen, -amount);
      prependRow(screen, opRowHTML("i-building", "شراء من مستودع زهران", "دفعة نقدية", MINUS + fmt(amount), ""));
      return "تم حفظ الشراء · " + fmt(amount) + " د.أ";
    },
    "save-payment": function (screen, amount) {
      updateCash(screen, -amount);
      prependRow(screen, opRowHTML("i-arrow-down-left", "دفعة لمستودع زهران", "سداد جزئي", MINUS + fmt(amount), ""));
      return "تم تسجيل الدفعة · " + fmt(amount) + " د.أ";
    }
  };

  var DEFAULT_AMOUNTS = {
    "save-expense": 35, "save-collect": 150, "save-sale": 25,
    "save-purchase": 60, "save-payment": 80
  };
  var COMPLETION_LABELS = {
    "save-expense": "تم الحفظ", "save-collect": "تم التحصيل", "save-sale": "تم الحفظ",
    "save-purchase": "تم الحفظ", "save-payment": "تم التسجيل"
  };
  var LOADING_LABELS = {
    "save-expense": "جارٍ الحفظ…", "save-collect": "جارٍ التأكيد…", "save-sale": "جارٍ الحفظ…",
    "save-purchase": "جارٍ الحفظ…", "save-payment": "جارٍ التسجيل…"
  };

  function getMetricText(screen, key) {
    var el = screen.querySelector('[data-metric="' + key + '"]');
    return el ? el.textContent : "0";
  }

  var entrySeq = 1286; /* persistent entry-ID proof (Agent 04 §4, AC note) */

  function runSave(btn, demo) {
    if (btn.dataset.state) { return; }
    var sheet = btn.closest(".mc-sheet");
    var screen = btn.closest(".phone-screen");
    var amount = (readAmount(sheet) || DEFAULT_AMOUNTS[demo] || 0);
    setBtnState(btn, "loading", LOADING_LABELS[demo]);
    window.setTimeout(function () {
      setBtnState(btn, "completed", COMPLETION_LABELS[demo]);
      var message = SAVE_DEMOS[demo](screen, amount);
      entrySeq += 1;
      var firstRowQualifier = screen ? screen.querySelector("[data-op-list] .mc-op-qualifier") : null;
      if (firstRowQualifier) { firstRowQualifier.innerHTML += ' · قيد <bdi dir="ltr">' + entrySeq + "</bdi>"; }
      announce(screen, message + " · قيد " + entrySeq);
      window.setTimeout(function () {
        closeOverlay(sheet);
        window.setTimeout(function () { setBtnState(btn, "default"); }, 400);
      }, 1100);
    }, 1100);
  }

  /* ------------------------------------------------- verification clones */
  var WIDTHS = [320, 360, 390, 430];

  function buildClones() {
    if (clonesBuilt) { return; }
    clonesBuilt = true;
    var host = document.getElementById("vvFrames");
    var source = $(".view-composition", document.getElementById("phoneScreen"));
    if (!host || !source) { return; }
    var overlaySource = $$("#phoneScreen > .mc-sheet, #phoneScreen > .mc-scrim, #phoneScreen > .mc-dialog, #phoneScreen > [role=\"status\"]");
    WIDTHS.forEach(function (w) {
      var frame = document.createElement("div");
      frame.className = "vv-frame";
      frame.innerHTML =
        '<div class="phone-frame" data-w="' + w + '">' +
        '<div class="phone-screen"><div class="phone-scroll"></div></div></div>' +
        '<p class="vv-frame-caption"><bdi dir="ltr">' + w + "px</bdi> · تركيبة اختبار</p>";
      var screen = $(".phone-screen", frame);
      var scroller = $(".phone-scroll", frame);
      var clone = source.cloneNode(true);
      clone.hidden = false;
      /* strip ids and id-based aria references inside clones */
      $$("[id]", clone).forEach(function (el) { el.removeAttribute("id"); });
      $$("[aria-labelledby], [aria-describedby]", clone).forEach(function (el) {
        el.removeAttribute("aria-labelledby");
        el.removeAttribute("aria-describedby");
      });
      scroller.appendChild(clone);
      /* clone the overlay layer so sheets work inside the preview frames */
      overlaySource.forEach(function (ov) {
        var o = ov.cloneNode(true);
        $$("[id]", o).forEach(function (el) { el.removeAttribute("id"); });
        $$("[aria-labelledby], [aria-describedby]", o).forEach(function (el) {
          el.removeAttribute("aria-labelledby");
          el.removeAttribute("aria-describedby");
        });
        screen.appendChild(o);
      });
      host.appendChild(frame);
    });
  }

  /* --------------------------------------------------------- runtime audits */
  function measurePeek(frameScreen, width) {
    var rail = $(".mc-rail-scroll", frameScreen);
    if (!rail) { return null; }
    var railRect = rail.getBoundingClientRect();
    var rtl = getComputedStyle(document.documentElement).direction === "rtl";
    var viewportW = railRect.width;
    var tiles = $$("li", rail);
    for (var i = 0; i < tiles.length; i++) {
      var t = tiles[i].getBoundingClientRect();
      var startOffset = rtl ? (railRect.right - t.right) : (t.left - railRect.left);
      if (startOffset > 0 && startOffset < viewportW && startOffset + t.width > viewportW) {
        return Math.round(viewportW - startOffset);
      }
    }
    return null;
  }

  function scanOverflow(frameScreen) {
    var scroller = frameScreen.querySelector(".phone-scroll") || frameScreen;
    var screenRect = scroller.getBoundingClientRect();
    var clipped = [];
    $$(".mc-operational-row, .mc-metric-row, .mc-primary-figure, .mc-btn, .mc-input, .mc-sheet, .mc-nav-item, .mc-chart", frameScreen).forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) { return; }
      if (r.left < screenRect.left - 1 || r.right > screenRect.right + 1) {
        clipped.push(el.className.toString().split(" ")[0]);
      }
    });
    var docOverflow = scroller.scrollWidth > scroller.clientWidth + 1;
    return { docOverflow: docOverflow, clipped: clipped };
  }

  function scanTouchTargets(frameScreen) {
    var interactive = $$("button, input, select, label.mc-check, label.mc-switch", frameScreen)
      .filter(function (el) { return el.offsetParent !== null && !el.disabled; });
    var violations = [];
    interactive.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.width < 43.5 || r.height < 43.5) {
        violations.push((el.className || el.tagName).toString().split(" ")[0]);
      }
    });
    return { count: interactive.length, violations: violations };
  }

  function addRow(tableId, cells, verdictClass) {
    var table = document.getElementById(tableId);
    if (!table || !table.tBodies.length) { return; }
    var tr = document.createElement("tr");
    cells.forEach(function (c) {
      var td = document.createElement("td");
      if (typeof c === "object" && c.text) { td.innerHTML = c.text; if (c.cls) { td.className = c.cls; } }
      else { td.textContent = c; }
      tr.appendChild(td);
    });
    if (verdictClass) { tr.className = verdictClass; }
    table.tBodies[0].appendChild(tr);
  }

  function clearTable(tableId) {
    var table = document.getElementById(tableId);
    if (table && table.tBodies.length) { table.tBodies[0].innerHTML = ""; }
  }

  function runAudits() {
    /* text scans — scoped to PRODUCT surfaces (phone screens) only, so lab
       annotations (like the note describing this very scan) cannot trigger
       false positives */
    clearTable("vvTextScanTable");
    var bodyText = $$(".phone-screen").map(function (s) { return s.innerText || s.textContent || ""; }).join("\n");
    var hasJod = /jod/i.test(bodyText);
    var arabicIndic = $$("bdi, .mc-primary-figure, .mc-metric-value, .mc-op-amount, .mc-chart-value").filter(function (el) {
      return /[\u0660-\u0669\u06F0-\u06F9]/.test(el.textContent || "");
    }).length;
    var hasDarkClass = !!$(".dark, .dark *");
    var hasColorScheme = false;
    try {
      Array.prototype.slice.call(document.styleSheets).forEach(function (sheet) {
        Array.prototype.slice.call(sheet.cssRules || []).forEach(function (rule) {
          if (rule.media && /prefers-color-scheme/i.test(String(rule.media.mediaText))) { hasColorScheme = true; }
        });
      });
    } catch (e) { /* file:// protections — static assert only */ }

    addRow("vvTextScanTable", ["البحث عن «JOD»", hasJod
      ? { text: "موجود — خلل", cls: "is-fail" }
      : { text: "غائب ✓", cls: "is-pass" }]);
    addRow("vvTextScanTable", ["أرقام عربية-هندية داخل القيم", arabicIndic > 0
      ? { text: arabicIndic + " قيمة — خلل", cls: "is-fail" }
      : { text: "غائبة ✓ (أرقام إنجليزية معزولة)", cls: "is-pass" }]);
    addRow("vvTextScanTable", ["وضع داكن (.dark)", hasDarkClass
      ? { text: "موجود — خلل", cls: "is-fail" }
      : { text: "غائب ✓", cls: "is-pass" }]);
    addRow("vvTextScanTable", ["استعلام prefers-color-scheme", hasColorScheme
      ? { text: "موجود — خلل", cls: "is-fail" }
      : { text: "غائب ✓ (الوضع الفاتح فقط)", cls: "is-pass" }]);

    /* per-frame measurements */
    clearTable("vvPeekTable");
    clearTable("vvOverflowTable");
    var touchTotals = { count: 0, violations: [] };
    $$("#vvFrames .vv-frame").forEach(function (frame) {
      var screen = $(".phone-screen", frame);
      if (!screen) { return; }
      var w = $(".phone-frame", frame).dataset.w;
      var peek = measurePeek(screen, parseInt(w, 10));
      var verdict, cls;
      if (peek === null) { verdict = "غير قابل للقياس"; cls = "is-exception"; }
      else if (parseInt(w, 10) === 320) { verdict = peek + "px — استثناء موثّق"; cls = "is-exception"; }
      else if (peek >= 28) { verdict = peek + "px — اجتياز"; cls = "is-pass"; }
      else { verdict = peek + "px — أخفق"; cls = "is-fail"; }
      addRow("vvPeekTable", [w + "px", { text: (peek === null ? "—" : peek + "px"), cls: cls }, { text: verdict, cls: cls }]);

      var overflow = scanOverflow(screen);
      var scale = document.documentElement.getAttribute("data-text-scale") || "100";
      addRow("vvOverflowTable", [w + "px · " + scale + "%",
        overflow.docOverflow ? { text: "تجاوز", cls: "is-fail" } : { text: "لا تجاوز ✓", cls: "is-pass" },
        overflow.clipped.length ? { text: overflow.clipped.length + " عنصر", cls: "is-fail" } : { text: "صفر ✓", cls: "is-pass" }
      ]);

      var touch = scanTouchTargets(screen);
      touchTotals.count += touch.count;
      touchTotals.violations = touchTotals.violations.concat(touch.violations);
    });

    clearTable("vvTouchTable");
    addRow("vvTouchTable", ["عناصر تفاعلية في التركيبة (×4 إطارات)", String(touchTotals.count)]);
    addRow("vvTouchTable", ["أهداف أصغر من " + 44 + "px", touchTotals.violations.length
      ? { text: touchTotals.violations.join(" · ") + " — أخفق", cls: "is-fail" }
      : { text: "صفر ✓ (44/48px مطبّقة)", cls: "is-pass" }]);
  }

  /* audits run once fonts are ready so measurements use real metrics;
     geometric audits re-run whenever the verification view becomes visible */
  function ready() {
    buildClones();
  }
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { ready(); });
  } else {
    window.addEventListener("load", ready);
  }
})();
