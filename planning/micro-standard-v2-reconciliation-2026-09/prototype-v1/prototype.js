/* prototype.js — Visual validation prototype v1 (not product truth).
   Behaviors only: scene switching, viewport/text-scale/motion controls,
   AUX simulations, save lifecycle, overlays, stripe/mirror toggles.
   All displayed values are fixed literals — no computation on displayed numbers. */
(function () {
  "use strict";
  var root = document.documentElement;
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ---------- generic segmented-control binding ---------- */
  function bindSeg(id, attr, apply) {
    var seg = $(id);
    if (!seg) return;
    var buttons = $$("button", seg);
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.classList.remove("on"); x.setAttribute("aria-pressed", "false"); });
        b.classList.add("on");
        b.setAttribute("aria-pressed", "true");
        apply(b.getAttribute(attr), b);
      });
    });
  }

  /* ---------- scene switching (route transition guidance: 200ms, no layout animation) ---------- */
  var sceneNotes = {
    s1: "يُظهر: منطقة القيمة، الفراغات الصادقة، حالات المعرفة، متغيرا الفترة، سلم الأرقام.",
    s2: "يُظهر: شبكة الصف، خانة الحالة (كلمة + علامة)، شريط الحافة الاختياري ≤3px، والمقدار الثابت.",
    s3: "يُظهر: سلوك الهيكل حسب نوع المسار، إخفاء الواجهة مع لوحة المفاتيح، الأمان، كبت السياق، حد التمرير.",
    s4: "يُظهر: أصناف الأفعال، إدخال المقدار LTR، دورة الحفظ، الإتمام الهادئ، والقناة الاختيارية.",
    s5: "يُظهر: تأكيد الحذف في Sheet، العاقبة الكبرى في Dialog، والشرح المستمر داخل التدفق.",
    s6: "يُظهر: أرضية الأحجام، وأعلام مرايا الأيقونات دون فرض مكتبة إنتاج."
  };
  function showScene(id) {
    $$(".scene").forEach(function (s) { s.hidden = s.id !== id; });
    $$(".chrome-tabs button").forEach(function (b) {
      b.setAttribute("aria-selected", b.getAttribute("data-scene") === id ? "true" : "false");
    });
    var note = $("#scene-note");
    if (note) note.textContent = sceneNotes[id] || "";
  }
  $$(".chrome-tabs button").forEach(function (b) {
    b.addEventListener("click", function () { showScene(b.getAttribute("data-scene")); });
  });

  /* ---------- chrome controls ---------- */
  bindSeg("#ctrl-vp", "data-vp", function (v) {
    root.style.setProperty("--frame-w", v + "px");
  });

  /* text-scale emulation at the token level (disclosed method):
     scales the --text-* size tokens; values stay the contract's own. */
  var TEXT_TOKENS = {
    "--text-title-size": 28, "--text-title-sm-size": 20, "--text-section-size": 17,
    "--text-card-title-size": 15, "--text-body-size": 15, "--text-label-size": 13,
    "--text-caption-size": 12, "--text-kpi-size": 24, "--text-kpi-hero-size": 28,
    "--text-amount-size": 15, "--text-amount-input-size": 24
  };
  bindSeg("#ctrl-text", "data-text", function (v) {
    var scale = { "100": 1, "130": 1.3, "200": 2 }[v] || 1;
    var css = ":root{";
    Object.keys(TEXT_TOKENS).forEach(function (k) {
      css += k + ":" + (TEXT_TOKENS[k] * scale).toFixed(2) + "px;";
    });
    css += "}";
    var el = $("#ts-emul");
    if (!el) { el = document.createElement("style"); el.id = "ts-emul"; document.head.appendChild(el); }
    el.textContent = css;
  });

  bindSeg("#ctrl-motion", "data-motion", function (v) {
    root.setAttribute("data-motion", v);
  });

  /* ---------- Scene 1: period chips + honest-void action chip ---------- */
  $$(".vz-period .chip").forEach(function (c) {
    c.addEventListener("click", function () {
      $$(".vz-period .chip").forEach(function (x) { x.classList.remove("on"); x.setAttribute("aria-pressed", "false"); });
      c.classList.add("on");
      c.setAttribute("aria-pressed", "true");
    });
  });
  $$(".pv .seg button").forEach(function (b) {
    b.addEventListener("click", function () {
      $$("button", b.parentElement).forEach(function (x) { x.classList.remove("on"); });
      b.classList.add("on");
    });
  });
  $$(".chip-action").forEach(function (c) {
    c.addEventListener("click", function () {
      var note = $("#scene-note");
      if (note) { note.textContent = "فعل توضيحي: «سجّله» — رقاقة فعل للفراغ غير المسجَّل (لا يغيّر أي بيانات)."; }
    });
  });

  /* ---------- Scene 2: optional stripe toggle ---------- */
  var stripeBtn = $("#stripe-toggle");
  if (stripeBtn) {
    stripeBtn.addEventListener("click", function () {
      var on = stripeBtn.getAttribute("aria-pressed") !== "true";
      stripeBtn.setAttribute("aria-pressed", on ? "true" : "false");
      $$(".rows .row").forEach(function (r) {
        var kind = r.getAttribute("data-stripe");
        r.classList.toggle("stripe", on && kind && kind !== "none");
      });
    });
  }

  /* ---------- Scene 3: AUX behaviors ---------- */
  var phone = $("#aux-phone");
  bindSeg("#ctrl-route", "data-route", function (v) {
    phone.setAttribute("data-route-kind", v);
  });
  bindSeg("#ctrl-kb", "data-kb", function (v) {
    phone.setAttribute("data-keyboard", v);
  });
  var ctxBtn = $("#ctx-toggle");
  if (ctxBtn) {
    ctxBtn.addEventListener("click", function () {
      var on = ctxBtn.getAttribute("aria-pressed") !== "true";
      ctxBtn.setAttribute("aria-pressed", on ? "true" : "false");
      ctxBtn.textContent = on ? "كبت تسمية السياق: مفعّل" : "تسمية السياق: ظاهرة";
      var ctx = $("#aux-ctx");
      if (ctx) ctx.classList.toggle("suppressed", on); /* suppression when it duplicates the h1 */
    });
  }
  var content = $("#aux-content");
  var topbar = $("#aux-topbar");
  if (content && topbar) {
    content.addEventListener("scroll", function () {
      topbar.classList.toggle("scrolled", content.scrollTop > 4);
    });
  }
  $$(".bottomnav .navitem").forEach(function (n) {
    n.addEventListener("click", function () {
      $$(".bottomnav .navitem").forEach(function (x) { x.classList.remove("on"); });
      n.classList.add("on");
    });
  });
  var transitionBtn = $("#aux-transition");
  if (transitionBtn) {
    var pages = [
      ["بيان محتوى أول", "قيمة توضيحية: 12,480 د.أ (آخر 30 يوم)"],
      ["بيان محتوى ثانٍ", "قيمة توضيحية: 9,040 د.أ (هذا الشهر)"]
    ];
    var pageIdx = 0;
    transitionBtn.addEventListener("click", function () {
      pageIdx = 1 - pageIdx;
      var body = $("#aux-body");
      body.classList.remove("transitioning");
      void body.offsetWidth; /* restart the 200ms transition */
      body.classList.add("transitioning");
      var h = body.querySelector("p");
      if (h) h.textContent = pages[pageIdx][0];
      var second = body.querySelectorAll("p")[1];
      if (second) second.textContent = pages[pageIdx][1];
    });
  }
  var fab = $("#aux-fab");
  if (fab) {
    fab.addEventListener("click", function () {
      var note = $("#scene-note");
      if (note) note.textContent = "زر الإنشاء (Clay #D97757، رمز أبيض) في ميزابه الخاص — دور الهوية/الإنشاء، ولا يعرض قيمة مالية أبدًا.";
    });
  }

  /* ---------- Scene 4: save lifecycle (loading guard + quiet completion + optional snackbar) ---------- */
  var saveBtn = $("#save-btn");
  var snackOptOn = false;
  var saveTimer = null;
  if (saveBtn) {
    saveBtn.addEventListener("click", function () {
      if (saveBtn.classList.contains("is-loading")) return; /* duplicate-submit guard */
      saveBtn.classList.add("is-loading");
      saveBtn.setAttribute("aria-busy", "true");
      var spinner = $(".spinner", saveBtn);
      if (spinner) spinner.hidden = false;
      saveTimer = window.setTimeout(function () {
        saveBtn.classList.remove("is-loading");
        saveBtn.setAttribute("aria-busy", "false");
        if (spinner) spinner.hidden = true;
        var res = $("#inline-result");
        if (res) { res.hidden = false; } /* inline quiet completion: word + check + role=status */
        if (snackOptOn) {
          var sn = $("#snackbar");
          if (sn) {
            sn.hidden = false;
            window.setTimeout(function () { sn.hidden = true; }, 5000); /* recorded hold */
          }
        }
        window.setTimeout(function () { if (res) res.hidden = true; }, 4000);
      }, 1400);
    });
  }
  var snackOpt = $("#snack-opt");
  if (snackOpt) {
    snackOpt.addEventListener("click", function () {
      snackOptOn = snackOpt.getAttribute("aria-pressed") !== "true";
      snackOpt.setAttribute("aria-pressed", snackOptOn ? "true" : "false");
      if (!snackOptOn) { var sn = $("#snackbar"); if (sn) sn.hidden = true; }
    });
  }

  /* ---------- Scene 5: overlays (shared scrim, Escape, focus restore) ---------- */
  var lastFocus = null;
  function openOverlay(scrimEl, panel) {
    lastFocus = document.activeElement;
    scrimEl.hidden = false;
    panel.hidden = false;
    var first = panel.querySelector("button");
    if (first) first.focus();
  }
  function closeOverlay(scrimEl, panel) {
    panel.hidden = true;
    scrimEl.hidden = true;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  var scrim = $("#scrim");
  var sheet = $("#sheet");
  var dlgWrap = $("#dialog-wrap");
  var openSheetBtn = $("#open-sheet");
  var openDlgBtn = $("#open-dialog");
  if (openSheetBtn) openSheetBtn.addEventListener("click", function () { openOverlay(scrim, sheet); });
  if (openDlgBtn) openDlgBtn.addEventListener("click", function () { openOverlay(scrim, dlgWrap); });
  var sheetCancel = $("#sheet-cancel");
  var sheetConfirm = $("#sheet-confirm");
  if (sheetCancel) sheetCancel.addEventListener("click", function () { closeOverlay(scrim, sheet); });
  if (sheetConfirm) sheetConfirm.addEventListener("click", function () {
    closeOverlay(scrim, sheet);
    var res = $("#overlay-result");
    if (res) { res.hidden = false; window.setTimeout(function () { res.hidden = true; }, 3000); }
  });
  var dlgCancel = $("#dlg-cancel");
  var dlgConfirm = $("#dlg-confirm");
  if (dlgCancel) dlgCancel.addEventListener("click", function () { closeOverlay(scrim, dlgWrap); });
  if (dlgConfirm) dlgConfirm.addEventListener("click", function () {
    closeOverlay(scrim, dlgWrap);
    var res = $("#overlay-result");
    if (res) { res.hidden = false; window.setTimeout(function () { res.hidden = true; }, 3000); }
  });
  if (scrim) scrim.addEventListener("click", function () {
    if (!sheet.hidden) closeOverlay(scrim, sheet);
    if (!dlgWrap.hidden) closeOverlay(scrim, dlgWrap);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (sheet && !sheet.hidden) closeOverlay(scrim, sheet);
    else if (dlgWrap && !dlgWrap.hidden) closeOverlay(scrim, dlgWrap);
    else if (drawer && !drawer.hidden) closeDrawer();
  });

  /* ---------- Scene 6: icon mirror toggle (adapter-applied transform) ---------- */
  $$(".ic-cell").forEach(function (cell) {
    var flag = cell.querySelector(".ic-flag");
    if (flag && flag.textContent.indexOf("ينعكس") >= 0) {
      cell.classList.add("mirrored"); /* RTL context mirrors directional roles */
    }
  });

  /* ---------- authority drawer ---------- */
  var drawer = $("#authority-drawer");
  var openAuth = $("#open-authority");
  var closeAuth = $("#close-authority");
  function openDrawer() { lastFocus = document.activeElement; drawer.hidden = false; if (closeAuth) closeAuth.focus(); }
  function closeDrawer() { drawer.hidden = true; if (lastFocus && lastFocus.focus) lastFocus.focus(); }
  if (openAuth) openAuth.addEventListener("click", openDrawer);
  if (closeAuth) closeAuth.addEventListener("click", closeDrawer);

  /* ---------- init ---------- */
  showScene("s1");
})();
